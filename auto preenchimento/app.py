import pyperclip 
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('/F:\Repo_GitHub\Codes_in_Py\auto preenchimento\produtos_ficticios.xlsx')
sheet_produto = workbook['produtos']

for linha in sheet_produto.iter_rows(min_row=2):
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(x=375, y=335)
    pyautogui.hotkey('ctrl', 'v')
    #descricao_produto = linha[1].value
    #categoria_produto = linha[2].value
    #codigo_produto = linha[3].value
    #peso = linha[4].value
    #dimesoes = linha[5].value
    #preco = linha[6].value
    #quantidade = linha[7].value
    #data_validade = linha[8].value
    #cor = linha[9].value
    #tamanho = linha[10].value
    #material = linha[11].value
    #fabricante = linha[12].value
    