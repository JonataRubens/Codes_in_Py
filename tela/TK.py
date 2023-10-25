import random
import string
from tkinter import Button, Label, Tk, IntVar, Checkbutton, messagebox

def genpass():

    senha = ''
    lista = string.ascii_lowercase  # Comece com letras minúsculas

    if incluir_maiusculas.get() == 1:
        lista += string.ascii_uppercase
    if incluir_numeros.get() == 1:
        lista += string.digits

    for c in range(12):
        senha += random.choice(lista)
    mensagem = f"A senha gerada é: {senha}"
    messagebox.showinfo("Senha Gerada", mensagem)
    print(f'senha gerada = {senha}')
    
    
janela = Tk()
janela.title('generator password')

tamanho_janela = 280  # Tamanho quadrado da janela

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x = (largura_tela - tamanho_janela) // 2
y = (altura_tela - tamanho_janela) // 2

janela.geometry(f'{tamanho_janela}x{tamanho_janela}+{x}+{y}')

text_orientacao = Label(janela, text="Gerador de senha 1.0")
text_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Gerar senha!", command=genpass)
botao.grid(column=0, row=2)

janela_code = Label(janela, text="")
janela_code.grid(column=0, row=3)

# Variáveis de controle para as caixas de seleção
incluir_maiusculas = IntVar()
incluir_minusculas = IntVar()
incluir_numeros = IntVar()

# Caixas de seleção para escolher as opções
check_maiusculas = Checkbutton(janela, text="Incluir maiúsculas", variable=incluir_maiusculas)
check_maiusculas.grid(column=0, row=4)


check_numeros = Checkbutton(janela, text="Incluir números", variable=incluir_numeros)
check_numeros.grid(column=0, row=5)


janela_escolha = Label(janela, text="--Clique para gerar--")

janela.mainloop()
