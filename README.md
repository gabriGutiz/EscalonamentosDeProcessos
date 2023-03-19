# Simulação de Escalonamento de Processos

- [Simulação de Escalonamento de Processos](#simulação-de-escalonamento-de-processos)
  1. [Como Utilizar?](#como-utilizar)
        - [Arquivo de Entrada](#arquivo-de-entrada)
            - [Local do Arquivo](#local-do-arquivo)
            - [Formato do Arquivo](#formato-do-arquivo)
        - [Execução](#execucao)
        - [Opções de Simulação](#opções-de-simulação)

&nbsp;

# Como Utilizar?
Informações para utilização do simulador

&nbsp;
## Arquivo de Entrada
#
### Local do Arquivo
O arquivo deve estar no caminho relativo ao local do main.py:
```
\input\simulacao.csv
```

&nbsp;
### Formato do Arquivo
O arquivo deve estar na extenção `.csv`, sem necessidade de cabeçalho, com a formatação:
```csv
    ID,TEMPO_ENTRADA,TEMPO_PROCESSAMENTO
```
- ID: `string` - identificador único de qualquer formato
- TEMPO_ENTRADA: `int` - ciclo de chegada ao processador
- TEMPO_PROCESSAMENTO: `int` - quantidades de ciclos no processador

&nbsp;
## Execução
Após salvar o arquivo no local correto, executar o script `main.py`. Quando o script é iniciado, será requisitado a opção de simulação. Para escolher a opção, digite o número e aperte enter. Caso o número passado não possua uma opção válida, será perguntado novamente até que o usuário digite a opção de saída.

&nbsp;
### Opções de simulação