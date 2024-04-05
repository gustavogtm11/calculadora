import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox

numero1 = ''
numero2 = ''
adicao = False
subtracao = False
multiplicacao = False
divisao = False

app= CTk()
app.title('Calculadora')
app.geometry('348x400')
app.maxsize(348, 400)
app.minsize(348, 400)

def limite_entrada(entry):
    if len(entry.get()) > 18:
        entry.delete(18, 'end')



def click_num(num):
    tela.insert(END, num)


def limpar_tudo(limpar):
    global numero1, numero2, adicao, subtracao, multiplicacao, divisao
    if limpar == 'C':
        numero1 = ''
        numero2 = ''
        adicao = False
        subtracao = False
        multiplicacao = False
        divisao = False
        tela.delete(0, END)
    elif limpar == 'seta':
        tela.delete(len(tela.get())-1)


def operacao(op):
    global numero1, adicao, subtracao, divisao, multiplicacao

    adicao = False
    subtracao = False
    divisao = False
    multiplicacao = False

    if op == '+':
        adicao = True
    elif op == '-':
        subtracao = True
    elif op == '/':
        divisao = True
    elif op == '*':
        multiplicacao = True
        
    numero1 = tela.get()
    tela.delete(0, END)
    print(numero1)

def calcular():
    global numero1, numero2, adicao, subtracao, divisao, multiplicacao
    numero2 = tela.get()
    tela.delete(0, END)
    if adicao == True:
        resultado = (float(numero1) + float(numero2))
    elif subtracao == True:
        resultado=(float(numero1) - float(numero2))
    elif multiplicacao == True:
        resultado=(float(numero1) * float(numero2))
    elif divisao == True:
        try:
            if numero1 != 0 or numero2 != 0:
                resultado=(float(numero1) / float(numero2))
        except ZeroDivisionError:
                messagebox.showerror('Error', 'Divisão por 0 não permitida')
    tela.insert(0, str(resultado))


def btn_num(num, row, column):
    botao = ctk.CTkButton(app, 
                          text=num,
                          command=lambda:click_num(num),
                          width=87,
                          height=64,
                          fg_color='#fff',
                          text_color='#000',
                          hover_color='#ddd',
                          font=('futura', 20), border_width=1, border_color='#000')
    botao.grid(row=row, column=column)

def btn_fun(op, fun, row, column, columnspan):
    if columnspan == 2:
        botao_fun = ctk.CTkButton(app, text=op, command= lambda: limpar_tudo(fun), width=174, height=64, font=('futura', 20), border_width=1, border_color='#000')
    else:        
        botao_fun = ctk.CTkButton(app, text=op, command= lambda: limpar_tudo(fun), width=87, height=64, font=('futura', 20), border_width=1, border_color='#000')
    botao_fun.grid(row=row, column=column, columnspan=columnspan)

def btn_op(op, fun, row, column, columnspan):
    botao = ctk.CTkButton(app, 
                          text=op,
                          command=lambda:operacao(fun),
                          width=87,
                          height=64,
                          font=('futura', 20), border_width=1, border_color='#000')
    botao.grid(row=row, column=column, columnspan=columnspan)


tela = ctk.CTkEntry(app,width=348, height=80, fg_color='transparent', justify='right', font=('futura', 28, 'bold'),border_width=0,insertwidth=0)
tela.grid(row=0, column=0, columnspan=4)

tela.bind('<KeyRelease>', lambda event: limite_entrada(tela))

#Linha 1
btn_fun('C', 'C', 1, 0, 2)
btn_fun('\u2190','seta',1,2,1)
btn_op('÷','/', 1,3,1)

#Linha 2
btn_num(7, 4, 0)
btn_num(8, 4, 1)
btn_num(9, 4, 2)
btn_op('-','-', 4,3,1)

#Linha 3
btn_num(4, 5, 0)
btn_num(5, 5, 1)
btn_num(6, 5, 2)
btn_op('x','*', 5,3,1)

#Linha 4
btn_num(1, 6, 0)
btn_num(2, 6, 1)
btn_num(3, 6, 2)
btn_op('+','+',6, 3, 1)

#Linha 5
btn_num(0, 7, 0)
btn_num('.', 7, 1)
total = ctk.CTkButton(app, text='=', command=calcular, width=174, height=64)
total.grid(row=7,column=2, columnspan=2)

app.mainloop()