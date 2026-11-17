
import sys
from pathlib import Path
from importlib.metadata import version, PackageNotFoundError

# Diretório raiz do projeto
ROOT = Path(__file__).resolve().parent.parent

# Dependências necessárias
DEPENDENCIAS = {
    "pytest": "pytest",
    "pytest-cov": "pytest_cov",
    "coverage": "coverage",
    "radon": "radon"
}

# Estrutura esperada
PASTAS = [
    "artefatos",
    "testes",
    "evidencias"
]


def verificar_python():
    print("\n=== VERIFICAÇÃO DO PYTHON ===")

    print(f"Versão instalada: {sys.version.split()[0]}")
    print(f"Executável: {sys.executable}")

    if sys.version_info[:2] == (3, 13):
        print("[OK] Python 3.13 encontrado.")
        return True

    print("[ERRO] É necessário utilizar Python 3.13.")
    return False


def verificar_dependencias():
    print("\n=== VERIFICAÇÃO DAS DEPENDÊNCIAS ===")

    sucesso = True

    for pacote, modulo in DEPENDENCIAS.items():
        try:
            versao = version(pacote)
            print(f"[OK] {pacote}: {versao}")

        except PackageNotFoundError:
            print(f"[ERRO] {pacote} não está instalado.")
            sucesso = False

    return sucesso


def verificar_estrutura():
    print("\n=== VERIFICAÇÃO DA ESTRUTURA ===")

    sucesso = True

    for pasta in PASTAS:
        caminho = ROOT / pasta

        if caminho.is_dir():
            print(f"[OK] Pasta encontrada: {pasta}/")
        else:
            print(f"[ERRO] Pasta não encontrada: {pasta}/")
            sucesso = False

    requirements = ROOT / "requirements.txt"

    if requirements.is_file():
        print("[OK] requirements.txt encontrado.")
    else:
        print("[ERRO] requirements.txt não encontrado.")
        sucesso = False

    return sucesso


def main():
    print("=" * 50)
    print(" VERIFICAÇÃO DO AMBIENTE DO EXPERIMENTO")
    print("=" * 50)

    resultados = [
        verificar_python(),
        verificar_dependencias(),
        verificar_estrutura()
    ]

    print("\n" + "=" * 50)

    if all(resultados):
        print("[SUCESSO] Ambiente pronto para o experimento!")
        return 0

    print("[ERRO] Foram encontrados problemas no ambiente.")
    return 1


if __name__ == "__main__":
    sys.exit(main())