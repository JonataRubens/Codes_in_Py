import random
from tkinter import *

def ale():
    nomes = ['a','b','c']
    resu = (nomes[random.randint(0,2)])
    resultado["text"] = resu
    return resultado

cor = "#dedcdc" #cinza

janela=Tk()
janela.title('---------------')
janela.geometry('380x280')
#janela.resizable(width = False, height = False)
#janela.configure(bg=cor)


label1= Label(
    janela,
    text = 'texto qualquer',
    font= 'Arial 20',
    justify= CENTER
    )
label1.pack()

botton = Button(
    janela, 
    text ='Button',
    command = ale
)
botton.pack()

resultado = Label(
    janela,
    text=''
)
resultado.pack()


janela.mainloop()