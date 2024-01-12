import pyperclip 
import openpyxl
import pyautogui

def preencher_campo(coordenadas, valor):
    pyperclip.copy(valor)
    pyautogui.click(*coordenadas, duration=1)
    pyautogui.hotkey('ctrl', 'v')

workbook = openpyxl.load_workbook('F:/Repo_GitHub/Codes_in_Py/auto preenchimento/produtos_ficticios.xlsx')
sheet_produto = workbook['Produtos']

coordenadas_campos = [
    (375, 335),  # Nome do produto
    (366, 434),  # Descrição do produto
    (365, 560),  # Categoria do produto
    (383, 651),  # Código do produto
    (382, 725),  # Peso
    (416, 820),  # Dimensões
    (351, 869),  # (Coordenadas após preencher os campos)
    (456, 367),  # Preço
    (387, 448),  # Quantidade
    (409, 528),  # Data de validade
    (403, 625),  # Cor
    (371, 710),  # Tamanho
    (372, 799),  # Material
    (343, 852),  # (Coordenadas após preencher os campos)
    (357, 381),  # Fabricante
    (365, 467),  # País de origem
    (349, 563),  # Observações
    (393, 689),  # Código de barras
    (357, 770),  # Localização no armazém
    (343, 834),  # (Coordenadas finais)
    (1130, 164),  # (Coordenadas finais)
    (934, 616)    # (Coordenadas finais)
]

for linha in sheet_produto.iter_rows(min_row=2):
    for indice, coordenadas in enumerate(coordenadas_campos):
        valor = linha[indice].value
        preencher_campo(coordenadas, valor)
        
        if indice == 11:
            # Adicione a condição para clicar com base no valor do tamanho
            if valor == 'Pequeno':
                pyautogui.click(x=357, y=739, duration=1)
            elif valor == 'Médio':
                pyautogui.click(x=348, y=764, duration=1)
            else:
                pyautogui.click(x=377, y=781, duration=1) 
    # Clique em outros elementos após preencher os campos

# Clique nos últimos elementos
pyautogui.click(x=343, y=834, duration=1)
pyautogui.click(x=1130, y=164, duration=1)
pyautogui.click(x=934, y=616, duration=1)
