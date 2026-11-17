
import sys
import json
import argparse
import subprocess
from pathlib import Path

# Diretório raiz do projeto
ROOT = Path(__file__).resolve().parent.parent

PASTA_ARTEFATOS = ROOT / "artefatos"
PASTA_TESTES = ROOT / "testes"
PASTA_EVIDENCIAS = ROOT / "evidencias"


def localizar_arquivo(pasta, padrao, descricao):
    arquivos = list(pasta.glob(padrao))

    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo encontrado para {descricao}: {padrao}"
        )

    if len(arquivos) > 1:
        raise ValueError(
            f"Mais de um arquivo encontrado para {descricao}: "
            f"{[arquivo.name for arquivo in arquivos]}"
        )

    return arquivos[0]


def calcular_percentual(valor, total):
    if total == 0:
        return None

    return (valor / total) * 100


def medir_cobertura(codigo):
    # Localiza os arquivos correspondentes
    artefato = localizar_arquivo(
        PASTA_ARTEFATOS,
        f"{codigo}_*.py",
        "artefato original"
    )

    teste = localizar_arquivo(
        PASTA_TESTES,
        f"test_{codigo}_*.py",
        "arquivo de testes"
    )

    PASTA_EVIDENCIAS.mkdir(parents=True, exist_ok=True)

    # Arquivos de saída
    relatorio_json = PASTA_EVIDENCIAS / f"{codigo}_cobertura.json"
    relatorio_txt = PASTA_EVIDENCIAS / f"{codigo}_cobertura.txt"

    print("=" * 55)
    print(f"AVALIAÇÃO DE COBERTURA - {codigo}")
    print("=" * 55)

    print(f"Artefato: {artefato.name}")
    print(f"Testes: {teste.name}")

    # Executa os testes e mede a cobertura
    comando = [
        sys.executable,
        "-m",
        "pytest",
        str(teste),
        "-v",
        f"--cov={PASTA_ARTEFATOS}",
        "--cov-branch",
        "--cov-report=term-missing",
        f"--cov-report=json:{relatorio_json}"
    ]

    print("\nExecutando testes e calculando cobertura...\n")

    resultado = subprocess.run(comando, cwd=ROOT)

    # Verifica se o relatório foi gerado
    if not relatorio_json.exists():
        raise RuntimeError(
            "Não foi possível gerar o relatório de cobertura."
        )

    # Lê os resultados do Coverage
    with open(relatorio_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    # Localiza os dados específicos do artefato
    dados_artefato = None

    for caminho, informacoes in dados["files"].items():
        caminho_completo = (ROOT / caminho).resolve()

        if caminho_completo == artefato.resolve():
            dados_artefato = informacoes
            break

    if dados_artefato is None:
        raise RuntimeError(
            f"O artefato {artefato.name} não foi encontrado "
            "no relatório de cobertura. Verifique se ele foi importado "
            "pelos testes."
        )

    resumo = dados_artefato["summary"]

    # Cobertura de linhas
    linhas_cobertas = resumo["covered_lines"]
    total_linhas = resumo["num_statements"]

    percentual_linhas = calcular_percentual(
        linhas_cobertas,
        total_linhas
    )

    # Cobertura de ramificações
    ramificacoes_cobertas = resumo["covered_branches"]
    total_ramificacoes = resumo["num_branches"]

    percentual_ramificacoes = calcular_percentual(
        ramificacoes_cobertas,
        total_ramificacoes
    )

    # Formatação dos resultados
    linhas_texto = (
        f"{percentual_linhas:.2f}%"
        if percentual_linhas is not None else "N/A"
    )

    ramificacoes_texto = (
        f"{percentual_ramificacoes:.2f}%"
        if percentual_ramificacoes is not None else "N/A (sem ramificações)"
    )

    status = "APROVADOS" if resultado.returncode == 0 else "FALHARAM"

    # Exibe os resultados
    print("\n" + "=" * 55)
    print("RESULTADOS DO EXPERIMENTO")
    print("=" * 55)

    print(f"Artefato: {artefato.name}")
    print(f"Testes: {teste.name}")
    print(f"Resultado dos testes: {status}")

    print(
        f"Cobertura de linhas: {linhas_texto} "
        f"({linhas_cobertas}/{total_linhas})"
    )

    print(
        f"Cobertura de ramificações: {ramificacoes_texto} "
        f"({ramificacoes_cobertas}/{total_ramificacoes})"
    )

    # Salva o resumo textual
    conteudo = f"""
RESULTADOS DO EXPERIMENTO

Identificador: {codigo}
Artefato: {artefato.name}
Arquivo de testes: {teste.name}

Resultado dos testes: {status}

COBERTURA DE LINHAS
Linhas cobertas: {linhas_cobertas}
Total de linhas executáveis: {total_linhas}
Percentual: {linhas_texto}

COBERTURA DE RAMIFICAÇÕES
Ramificações cobertas: {ramificacoes_cobertas}
Total de ramificações: {total_ramificacoes}
Percentual: {ramificacoes_texto}
"""

    relatorio_txt.write_text(conteudo.strip(), encoding="utf-8")

    print("\nEvidências geradas:")
    print(f"- {relatorio_json.relative_to(ROOT)}")
    print(f"- {relatorio_txt.relative_to(ROOT)}")

    print("=" * 55)

    return resultado.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Mede a cobertura de linhas e ramificações "
                    "de um artefato do experimento."
    )

    parser.add_argument(
        "codigo",
        help="Identificador do artefato (exemplo: A01)"
    )

    args = parser.parse_args()

    codigo = args.codigo.upper()

    if not codigo.startswith("A") or not codigo[1:].isdigit():
        parser.error("Informe um identificador válido, como A01.")

    try:
        return medir_cobertura(codigo)

    except (FileNotFoundError, ValueError, RuntimeError) as erro:
        print(f"\n[ERRO] {erro}")
        return 1


if __name__ == "__main__":
    sys.exit(main())