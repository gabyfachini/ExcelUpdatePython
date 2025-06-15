## Limpador de Excel - Remove "\_x000D\_" de Arquivos do Excel

Este projeto é um script Python que lê um arquivo Excel e substitui todas as ocorrências de \_x000D\_ por um espaço, mantendo a estrutura da planilha.

---

### 🚀 Como Instalar o Python

1. Baixe o Python do site oficial:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Durante a instalação, **marque a caixa que diz "Adicionar Python ao PATH"**.

3. Conclua a instalação.

---

### 📦 Instale as Bibliotecas Necessárias

Abra seu terminal (Prompt de Comando, PowerShell ou terminal no VSCode) e execute:

`pip install pandas openpyxl`

Se o pip não funcionar, tente:

`python -m pip install --upgrade pip`

`python -m pip install pandas openpyxl`

---

### ▶️ Como Executar o Script
1. Salve o arquivo de script como UpdateExcel.py
2. Coloque o arquivo do Excel que deseja processar na mesma pasta do script
3. Abra o terminal e navegue até a pasta onde tem o código e a pasta de excel, seria algo como:

     `cd C:\Usuários\SeuNome\Caminho\Para\Sua\Pasta`
5. Execute no terminal:

    `python UpdateExcel.py`
8. Um novo arquivo do Excel chamado `cleaned_spreadsheet.xlsx` será criado na mesma pasta. Você pode renomear o nome do arquivo final no próprio código do Python
9. **CUIDADO**: Se já tiver feito alguma extração na planilha e for gerar uma nova, o sistema não cria uma planilha nova, ele apenas atualiza a já existente com o nome `cleaned_spreadsheet.xlsx`, para criar uma nova, precisa renomear o nome final da plnailha no próprio código
