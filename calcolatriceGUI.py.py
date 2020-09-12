import tkinter as tk
f = tk.Tk()
f.geometry('260x360')
f.title('Calcolatrice')
f.resizable(False, False)
numeri = [1,2,3,4,5,6,7,8,9,0]
operatori = ['x','/','+','-']
N1 = []
N2 = []
#funzione per l'inserimento dei numeri tramite i pulsanti della GUI
def inserimento(i):
    snum1 = ''
    snum2 = ''
    print('inserimento >',str(i))
    if i in numeri:
        if '/' not in N1:
            N1.append(str(i))
            for i in N1:
                snum1 += i
            et.config(text = snum1)
        else:
            N2.append(str(i))
            for i in N2:
                snum2 += i
            et.config(text = snum2)
    elif i in operatori:
        if len(N1) != 0:
             N1.append('/')
             et.config(text = i)
             N1.append(str(i))
        else:
            print('errore')
            et.config(text = '0')
    elif i == '=':
        if len(N1) != 0 and len(N2) != 0:
            risolvi()
        else:
            N1.clear()
            N2.clear()
            et.config(text = '0')
            print('errore')
            return None

#funzione matematica per la risoluzione delle operazioni
def risolvi():
    print('risolvo!')
    print('N1 = ',N1[:-2])
    print('N2 = ',N2)
    et.config(text = '')
    snum1 = ''
    snum2 = ''
    op = N1[len(N1) - 1]
    for i in N1[0:(N1.index('/'))]:
        snum1 += i
    print('snum1 =',snum1)
    for i in N2:
        snum2 += i
    print('snum2 =',snum2)
    num1 = int(snum1)
    num2 = int(snum2)
    r = 0
    print('operatore =',op)
    if op == 'x':
        r = num1 * num2
    elif op == '/':
        r = num1 / num2
    elif op == '+':
        r = num1 + num2
    elif op == '-':
        r = num1 - num2
    print('risultato =',r)
    et.config(text = str(r))
    N1.clear()
    N2.clear()
    return

#definizione canvas,pulsanti, e etichette per interfaccia grafica
color = 'lightcyan'
color2 = 'khaki'
back = tk.Canvas(f, width = 230, height = 300, bg = 'LightBlue', borderwidth = 3, relief = 'solid' )
back.place(x = 15,y = 44)
b1 = tk.Button(text = '1', command = lambda: inserimento(1), width = 5, height = 2,bg = color)
b1.place(relx = 0.1,rely = 0.30)
b2 = tk.Button(text = '2', command = lambda: inserimento(2), width = 5, height = 2,bg = color)
b2.place(relx = 0.34, rely = 0.30)
b3 = tk.Button(text = '3', command = lambda: inserimento(3), width = 5, height = 2,bg = color)
b3.place(relx = 0.57, rely = 0.30)
b4 = tk.Button(text = '4', command = lambda: inserimento(4), width = 5, height = 2,bg = color)
b4.place(relx = 0.1, rely = 0.45)
b5 = tk.Button(text = '5', command = lambda: inserimento(5), width = 5, height = 2,bg = color)
b5.place(relx = 0.34, rely = 0.45)
b6 = tk.Button(text = '6', command = lambda: inserimento(6), width = 5, height = 2,bg = color)
b6.place(relx = 0.57, rely = 0.45)
b7 = tk.Button(text = '7', command = lambda: inserimento(7), width = 5, height = 2,bg = color)
b7.place(relx = 0.1, rely = 0.6)
b8 = tk.Button(text = '8', command = lambda: inserimento(8), width = 5, height = 2,bg = color)
b8.place(relx = 0.34, rely = 0.6)
b9 = tk.Button(text = '9', command = lambda: inserimento(9), width = 5, height = 2,bg = color)
b9.place(relx = 0.57, rely = 0.6)
b0 = tk.Button(text = '0', command = lambda: inserimento(0), width = 4, height = 2,bg = color)
b0.place(relx = 0.423, rely = 0.73)

bu = tk.Button(text = '=', command = lambda: inserimento('='), width = 29, bg = 'sandybrown', height = 1)
bu.place(relx = 0.1, rely = 0.857)

bd = tk.Button(text = '/', command = lambda: inserimento('/'), width = 9, height = 2,bg = color2)
bd.place(relx = 0.1, rely = 0.73)

bm = tk.Button(text = 'x', command = lambda: inserimento('x'), width = 10, height = 2,bg = color2)
bm.place(relx = 0.61, rely = 0.73)

ba = tk.Button(text = '+', command = lambda: inserimento('+'), width = 4, height = 4,bg = color2)
ba.place(relx = 0.773, rely = 0.3)

bs = tk.Button(text = '-', command = lambda: inserimento('-'), width = 4, height = 4,bg = color2)
bs.place(relx = 0.773, rely = 0.518)

et = tk.Label(text = '0', bg = color, width = 23, height = 1, anchor = 'e', font = (100))
et.place(relx = 0.107, rely = 0.187)

f.mainloop()
