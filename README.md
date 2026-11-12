
# Experimento – Geração de Testes Unitários com IA

## Sobre o projeto

Este repositório contém os artefatos e instrumentos utilizados no experimento de avaliação da geração de testes unitários em Python por meio de Inteligência Artificial Generativa (ChatGPT GPT-6).

O objetivo é analisar a qualidade dos testes gerados, considerando a cobertura de linhas e ramificações, em métodos e funções classificados conforme sua complexidade ciclomática.

O experimento contempla 30 artefatos, divididos em três categorias: baixa, média e alta complexidade.

## Tecnologias utilizadas

- Python 3.13
- Pytest
- Pytest-cov
- Radon
- ChatGPT GPT-6
- GitHub
- Git
- Visual Studio Code

## Estrutura do repositório

```text
repositorio/
├── artefatos/          # Códigos originais utilizados no experimento
├── evidencias/         # Registros e resultados das execuções
├── testes/             # Testes unitários gerados pela IA
├── requirements.txt    # Dependências do projeto
└── README.md
```

## Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Verificar o ambiente

```bash
python --version
python -m pytest --version
python -m pip show pytest-cov
python -m radon --version
```

Executar a verificação do ambiente:

```bash
python scripts/verificar_ambiente.py
```

### 5. Verificar a complexidade ciclomática

Para analisar um artefato específico:

```bash
python -m radon cc artefatos/A01_arredondar_para_baixo.py -s
```

Para analisar todos os artefatos:

```bash
python -m radon cc artefatos -s
```

Classificação utilizada:

- Baixa: complexidade de 1 a 5.
- Média: complexidade de 6 a 10.
- Alta: complexidade igual ou superior a 11.

### 6. Gerar os testes unitários

1. Localize o artefato original na pasta `artefatos/`.
2. Abra um novo chat no ChatGPT GPT-6.
3. Utilize o prompt padronizado disponível na pasta `instrumentos/`.
4. Insira o código original no espaço indicado no prompt.
5. Salve a primeira resposta gerada, sem alterações.

Os testes devem ser armazenados na pasta `testes/`, seguindo o padrão:

```text
test_AXX_nome_da_funcao.py
```

### 7. Executar os testes e medir a cobertura

Para executar os testes:

```bash
python -m pytest testes/test_A01_nome_da_funcao.py -v
```

Para medir a cobertura de linhas e ramificações, utilize:

```bash
python scripts/medir_cobertura.py A01
```

Os resultados e as evidências devem ser armazenados na pasta `evidencias/`, conforme as orientações do Manual do Pesquisador.

### 8. Registrar os resultados

Após cada execução:

1. Conferir os resultados dos testes.
2. Registrar a cobertura de linhas e ramificações.
3. Salvar as evidências da execução.
4. Preencher a Planilha de Resultados.
5. Registrar eventuais problemas ou desvios do protocolo.

## Observações

- Os códigos originais não devem ser modificados.
- Cada artefato deve ser submetido individualmente à IA.
- O prompt deve permanecer padronizado para todos os participantes.
- Deve ser utilizada a primeira resposta gerada pelo ChatGPT.
- Os testes gerados devem ser armazenados sem alterações.
- Todas as execuções devem possuir suas respectivas evidências.

---

**Experimento acadêmico – Engenharia de Software**

**Grupo 3**
