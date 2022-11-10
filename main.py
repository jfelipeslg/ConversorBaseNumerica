from tkinter import *
from tkinter import ttk

colorPurple = '#311432'
colorWhite  = '#feffff'
colorBlue   = '#6f9fbd'
colorOrange = '#e89613'

janela = Tk()
janela.title('')
janela.geometry('600x400')
janela.configure(bg=colorPurple)

style = ttk.Style()
style.theme_use('clam')

# Divisão em dois frames
frame_up = Frame(janela, width=600, height=80, bg=colorPurple, pady=0, padx=0)
frame_up.grid(row=1, column=0)

frame_down = Frame(janela, width=600, height=300, bg=colorPurple, pady=12, padx=20)
frame_down.grid(row=2, column=0, sticky=NW)

# Titulo da aplicação
titleApp = Label(frame_up, text='Conversor de Bases Númericas', relief=FLAT,
                 anchor='center', font=("Times", 24), bg=colorPurple, fg=colorWhite)
titleApp.place(x=100, y=30)

# Filtro de escolha → base do número que será convertido 
base = ['Binário', 'Decimal', 'Octal', 'Hexadecimal']

baseBox = ttk.Combobox(frame_down, width=12, justify='center', font=('Ivy 12 bold'))
baseBox['values'] = (base)
baseBox.place(x=40, y=60)

Label_baseBox= Label(frame_down, text='Base do número a ser convertido',
                     width=28, relief=FLAT, anchor='nw', font=("Verdana", 9), bg=colorPurple, fg=colorWhite)
Label_baseBox.place(x=37, y=40)

# Escolha da base do número que será convertido
inputValue = Entry(frame_down, width=16, justify='center', font=("", 13), 
                   highlightthickness=1, relief='solid')
inputValue.place(x=40, y=120)

Label_inputValue= Label(frame_down, text='Número a ser convertido',
                        width=28, relief=FLAT, anchor='nw', font=("Verdana", 9), bg=colorPurple, fg=colorWhite)
Label_inputValue.place(x=37, y=100)


# Função de converter
def function_baseConverter():
    def baseConverter(num, base):
        numDec = int(str(num), base)
        
        valueBinario['text']     = bin(numDec)[2:]
        valueDecimal['text']     = str(numDec)
        valueOctal['text']       = oct(numDec)[2:]
        valueHexadecimal['text'] = hex(numDec)[2:].upper()
    
    num = inputValue.get()
    baseNum = baseBox.get()
    
    if baseNum == base[0]:
        baseNum = 2
    elif baseNum == base[1]:
        baseNum = 10
    elif baseNum == base[2]:
        baseNum = 8
    else:
        baseNum = 16
    
    baseConverter(num, baseNum)
    
# Botão de converter as bases
boxConvert = Button(frame_down, command=function_baseConverter, text='Converter', relief=RAISED, overrelief=RIDGE,
                    font=("Ivy", 10), bg=colorWhite, fg=colorPurple)
boxConvert.place(x=40, y=160)

# Visualização do número binário
valueBinario = Label(frame_down, text='Binário', width=12, relief=FLAT,
                 anchor='center', font=("Verdana", 13), bg=colorOrange, fg=colorWhite)
valueBinario.place(x=270, y=40)
valueBinario = Label(frame_down, text='', width=13, relief=FLAT,
                 anchor='center', font=("Verdana", 13), bg=colorWhite, fg=colorPurple)
valueBinario.place(x=400, y=40)

# Visualização do número decimal
valueDecimal = Label(frame_down, text='Decimal', width=12, relief=FLAT,
                 anchor='center', font=("Verdana", 13), bg=colorOrange, fg=colorWhite)
valueDecimal.place(x=270, y=80)
valueDecimal = Label(frame_down, text='', width=13, relief=FLAT,
                 anchor='center', font=("Verdana", 13), bg=colorWhite, fg=colorPurple)
valueDecimal.place(x=400, y=80)

# Visualização do número octal
valueOctal = Label(frame_down, text='Octal', width=12, relief=FLAT,
                 anchor='center', font=("Verdana", 13), bg=colorOrange, fg=colorWhite)
valueOctal.place(x=270, y=120)
valueOctal = Label(frame_down, text='', width=13, relief=FLAT,
                 anchor='center', font=("Verdana", 13), bg=colorWhite, fg=colorPurple)
valueOctal.place(x=400, y=120)

# Visualização do número hexadecimal
valueHexadecimal = Label(frame_down, text='Hexadecimal', width=12, relief=FLAT,
                 anchor='center', font=("Verdana", 13), bg=colorOrange, fg=colorWhite)
valueHexadecimal.place(x=270, y=160)
valueHexadecimal = Label(frame_down, text='', width=13, relief=FLAT,
                 anchor='center', font=("Verdana", 13), bg=colorWhite, fg=colorPurple)
valueHexadecimal.place(x=400, y=160)

janela.mainloop()
