from tkinter import *
from functools import partial
import random

root=Tk()
root.config(bg='brown')
root.title('Tic Tac Toe')
root.geometry('600x400')
root.resizable(False,False)

p1=0
p2=0
turn='p2'
marks=[]
global winner_found
def play(n):
    global winner_found,turn,p1,p2,marks
    winner_found=False
    turn='p2'
    marks=[]
    bs.place_forget()
    bt.place_forget()

    def playagain():
        for item in root.winfo_children():
            item.place_forget()
        play(n)

    Label(text='Scores', font='Abc 25 bold underline', fg='white', bg='brown').place(x=370, y=50)
    Button(text='Reset', command=playagain, bg='black', fg='white', font='Abc 20 underline').place(x=370, y=200)

    if (n == 1):
        Lp1 = Label(text='Computer: %d' % (p1), font='Abc 22 italic', fg='gray', bg='brown')
        Lp1.place(x=360, y=100)
        Lp2 = Label(text='You: %d' % (p2), font='Abc 22 italic', fg='yellow', bg='brown')
        Lp2.place(x=360, y=150)
        turn = 'p2'
    elif (n==2):
        Lp1 = Label(text='Player1: %d' % (p1), font='Abc 22 italic', fg='gray', bg='brown')
        Lp1.place(x=360, y=100)
        Lp2 = Label(text='Player2: %d' % (p2), font='Abc 22 italic', fg='yellow', bg='brown')
        Lp2.place(x=360, y=150)

    def update_score():
        Lp1.config(text=(Lp1.cget('text').split(' ')[0]+ ' ' + str(p1)))
        Lp2.config(text=(Lp2.cget('text').split(' ')[0] + ' ' + str(p2)))


    def won(z):
        global winner_found
        winner_found=True
        global p1,p2
        if(z==1):
            p1+=1
            update_score()
            for i in range(3):
                for j in range(3):
                    marks[i][j].config(state='disabled')
            Label(text=(Lp1.cget('text').split(':')[0] + ' won !'),bg='brown',
                  fg='magenta',font='Abc 20 bold italic').place(x=110, y=350)
            Lp1.config(fg='gray')
            Lp2.config(fg='gray')
            Button(text='Play Again',command=playagain, bg='black',fg='white',font='Abc 20 underline').place(x=350,y=200)

        elif(z==2):
            p2+=1
            update_score()
            for i in range(3):
                for j in range(3):
                    marks[i][j].config(state='disabled')
            Label(text=(Lp2.cget('text').split(':')[0] + ' won !'),bg='brown',
                  fg='magenta',font='Abc 20 bold italic').place(x=110, y=350)
            Lp1.config(fg='gray')
            Lp2.config(fg='gray')
            Button(text='Play Again', command=playagain, bg='black',fg='white',font='Abc 20 underline').place(x=350, y=200)



    def enter(i,j):
        global turn,winner_found
        if(turn=='p1'):
            turn='p2'
            marks[i][j].config(text='X',state='disabled',disabledforeground='midnight blue')
            Lp1.config(fg='gray')
            Lp2.config(fg='yellow')

            if(i==0):
                try:
                    if( marks[i+1][j].cget('text')=='X' and marks[i+2][j].cget('text')=='X' ):
                        marks[i][j].config(bg='green')
                        marks[i+1][j].config(bg='green')
                        marks[i+2][j].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if( marks[i][j+1].cget('text')=='X' and marks[i][j+2].cget('text')=='X' ):
                        marks[i][j].config(bg='green')
                        marks[i][j+1].config(bg='green')
                        marks[i][j+2].config(bg='green')
                        won(1)
                        return
                except:
                        pass
                try:
                    if( marks[i][j+1].cget('text')=='X' and marks[i][j-1].cget('text')=='X' and (j-1 >= 0)):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j -1].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if( marks[i+1][j+1].cget('text')=='X' and marks[i+2][j+2].cget('text')=='X' ):
                        marks[i][j].config(bg='green')
                        marks[i+1][j + 1].config(bg='green')
                        marks[i+2][j + 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if( marks[i+1][j-1].cget('text')=='X' and marks[i+2][j-2].cget('text')=='X' and (j-2 >= 0)):
                        marks[i][j].config(bg='green')
                        marks[i + 1][j - 1].config(bg='green')
                        marks[i + 2][j - 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if( marks[i][j-1].cget('text')=='X' and marks[i][j-2].cget('text')=='X' and j-2 >=0 ):
                        marks[i][j].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        marks[i][j - 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass

            elif(i==1):
                try:
                    if (marks[i + 1][j].cget('text') == 'X' and marks[i -1][j].cget('text') == 'X' and i-1>=0):
                        marks[i][j].config(bg='green')
                        marks[i + 1][j].config(bg='green')
                        marks[i - 1][j].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'X' and marks[i][j + 2].cget('text') == 'X'):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j + 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i][j - 1].cget('text') == 'X' and marks[i][j - 2].cget('text') == 'X' and j-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        marks[i][j - 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i + 1][j + 1].cget('text') == 'X' and marks[i -1][j -1].cget('text') == 'X' and j-1>=0
                    and i-1>=0):
                        marks[i][j].config(bg='green')
                        marks[i + 1][j + 1].config(bg='green')
                        marks[i -1][j -1].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i + 1][j - 1].cget('text') == 'X' and marks[i -1][j +1].cget('text') == 'X' and j-1>=0
                    and i-1>=0):
                        marks[i][j].config(bg='green')
                        marks[i -1][j +1].config(bg='green')
                        marks[i + 1][j - 1].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'X' and marks[i][j - 1].cget('text') == 'X' and j-1>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        won(1)
                        return
                except:
                    pass
            elif (i == 2):
                try:
                    if (marks[i - 1][j].cget('text') == 'X' and marks[i - 2][j].cget('text') == 'X' and i-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i - 1][j].config(bg='green')
                        marks[i - 2][j].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'X' and marks[i][j + 2].cget('text') == 'X'):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j + 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i][j - 1].cget('text') == 'X' and marks[i][j - 2].cget('text') == 'X' and j-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        marks[i][j - 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'X' and marks[i][j - 1].cget('text') == 'X' and j-1>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i -1][j +1].cget('text') == 'X' and marks[i - 2][j + 2].cget('text') == 'X' and i-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i - 1][j + 1].config(bg='green')
                        marks[i - 2][j + 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass
                try:
                    if (marks[i-1][j - 1].cget('text') == 'X' and marks[i-2][j - 2].cget('text') == 'X' and i-2>=0
                    and j-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i-1][j - 1].config(bg='green')
                        marks[i-2][j - 2].config(bg='green')
                        won(1)
                        return
                except:
                    pass


        else:
            turn = 'p1'
            marks[i][j].config(text='O',state='disabled',disabledforeground='midnight blue')
            Lp1.config(fg='yellow')
            Lp2.config(fg='gray')

            if (i == 0):
                try:
                    if (marks[i + 1][j].cget('text') == 'O' and marks[i + 2][j].cget('text') == 'O'):
                        marks[i][j].config(bg='green')
                        marks[i + 1][j].config(bg='green')
                        marks[i + 2][j].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'O' and marks[i][j + 2].cget('text') == 'O'):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j + 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'O' and marks[i][j - 1].cget('text') == 'O' and j-1>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i + 1][j + 1].cget('text') == 'O' and marks[i + 2][j + 2].cget('text') == 'O'):
                        marks[i][j].config(bg='green')
                        marks[i + 1][j + 1].config(bg='green')
                        marks[i + 2][j + 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i + 1][j - 1].cget('text') == 'O' and marks[i + 2][j - 2].cget('text') == 'O' and j-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i + 1][j - 1].config(bg='green')
                        marks[i + 2][j - 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j - 1].cget('text') == 'O' and marks[i][j - 2].cget('text') == 'O' and j-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        marks[i][j - 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass

            elif (i == 1):
                try:
                    if (marks[i + 1][j].cget('text') == 'O' and marks[i - 1][j].cget('text') == 'O' and i-1>=0):
                        marks[i][j].config(bg='green')
                        marks[i + 1][j].config(bg='green')
                        marks[i - 1][j].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'O' and marks[i][j + 2].cget('text') == 'O'):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j + 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j - 1].cget('text') == 'O' and marks[i][j - 2].cget('text') == 'O' and j-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        marks[i][j - 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i + 1][j + 1].cget('text') == 'O' and marks[i - 1][j - 1].cget('text') == 'O' and i-1>=0
                            and j-1>=0 ):
                        marks[i][j].config(bg='green')
                        marks[i + 1][j + 1].config(bg='green')
                        marks[i - 1][j - 1].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i + 1][j - 1].cget('text') == 'O' and marks[i - 1][j + 1].cget('text') == 'O' and i-1>=0
                            and j-1>=0 ):
                        marks[i][j].config(bg='green')
                        marks[i - 1][j + 1].config(bg='green')
                        marks[i + 1][j - 1].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'O' and marks[i][j - 1].cget('text') == 'O' and j-1>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        won(2)
                        return
                except:
                    pass
            elif (i == 2):
                try:
                    if (marks[i - 1][j].cget('text') == 'O' and marks[i - 2][j].cget('text') == 'O' and i-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i - 1][j].config(bg='green')
                        marks[i - 2][j].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'O' and marks[i][j + 2].cget('text') == 'O'):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j + 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j - 1].cget('text') == 'O' and marks[i][j - 2].cget('text') == 'O' and j-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        marks[i][j - 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i][j + 1].cget('text') == 'O' and marks[i][j - 1].cget('text') == 'O' and j-1>=0 ):
                        marks[i][j].config(bg='green')
                        marks[i][j + 1].config(bg='green')
                        marks[i][j - 1].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i - 1][j + 1].cget('text') == 'O' and marks[i - 2][j + 2].cget('text') == 'O' and i-2>=0):
                        marks[i][j].config(bg='green')
                        marks[i - 1][j + 1].config(bg='green')
                        marks[i - 2][j + 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass
                try:
                    if (marks[i - 1][j - 1].cget('text') == 'O' and marks[i - 2][j - 2].cget('text') == 'O' and i-2>=0
                            and j-2>=0 ):
                        marks[i][j].config(bg='green')
                        marks[i - 1][j - 1].config(bg='green')
                        marks[i - 2][j - 2].config(bg='green')
                        won(2)
                        return
                except:
                    pass

            if(n==1):
                available_blocks=[]
                no_win=[]
                turn='p1'
                for u in range(3):
                    for v in range(3):
                        if(marks[u][v].cget('text')==''):
                            available_blocks.append((u,v))
                opp_win=[]
                for ab in available_blocks:
                    u=ab[0]
                    v=ab[1]
                    if (u == 0):
                        try:
                            if (marks[u + 1][v].cget('text') == 'O' and marks[u + 2][v].cget('text') == 'O'):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v + 1].cget('text') == 'O' and marks[u][v + 2].cget('text') == 'O'):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v + 1].cget('text') == 'O' and marks[u][v - 1].cget(
                                    'text') == 'O' and v - 1 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u + 1][v + 1].cget('text') == 'O' and marks[u + 2][v + 2].cget('text') == 'O'):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u + 1][v - 1].cget('text') == 'O' and marks[u + 2][v - 2].cget(
                                    'text') == 'O' and v - 2 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v - 1].cget('text') == 'O' and marks[u][v - 2].cget(
                                    'text') == 'O' and v - 2 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass

                    elif (u == 1):
                        try:
                            if (marks[u + 1][v].cget('text') == 'O' and marks[u - 1][v].cget(
                                    'text') == 'O' and u - 1 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v + 1].cget('text') == 'O' and marks[u][v + 2].cget('text') == 'O'):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v - 1].cget('text') == 'O' and marks[u][v - 2].cget(
                                    'text') == 'O' and v - 2 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u + 1][v + 1].cget('text') == 'O' and marks[u - 1][v - 1].cget(
                                    'text') == 'O' and u - 1 >= 0
                                    and v - 1 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u + 1][v - 1].cget('text') == 'O' and marks[u - 1][v + 1].cget(
                                    'text') == 'O' and u - 1 >= 0
                                    and v - 1 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v + 1].cget('text') == 'O' and marks[u][v - 1].cget(
                                    'text') == 'O' and v - 1 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                    elif (u == 2):
                        try:
                            if (marks[u - 1][v].cget('text') == 'O' and marks[u - 2][j].cget(
                                    'text') == 'O' and u - 2 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v + 1].cget('text') == 'O' and marks[u][v + 2].cget('text') == 'O'):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v - 1].cget('text') == 'O' and marks[u][v - 2].cget(
                                    'text') == 'O' and v - 2 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u][v + 1].cget('text') == 'O' and marks[u][v - 1].cget(
                                    'text') == 'O' and v - 1 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u - 1][v + 1].cget('text') == 'O' and marks[u - 2][v + 2].cget(
                                    'text') == 'O' and u - 2 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass
                        try:
                            if (marks[u - 1][v - 1].cget('text') == 'O' and marks[u - 2][v - 2].cget(
                                    'text') == 'O' and u - 2 >= 0
                                    and v - 2 >= 0):
                                opp_win.append((u,v))
                        except:
                            pass

                for ab in available_blocks:
                    enter(ab[0], ab[1])
                    if(winner_found==True):
                        return
                    else:
                        turn = 'p1'
                        marks[ab[0]][ab[1]].config(text='', state='normal')
                        no_win.append(ab)

                if(opp_win !=[]):
                    cwin=random.choice(opp_win)
                    enter(cwin[0],cwin[1])
                else:
                    try:
                        selected=random.choice(no_win)
                        enter(selected[0],selected[1])
                    except:
                        pass




    y=50
    for i in range(3):
        x=30
        l = []
        for j in range(3):
            h=Button(text='',height=2,width=3,highlightbackground='black',bg='cyan',fg='midnight blue',font='Abc 25 bold',
                               command=partial(enter,i,j))
            h.place(x=x,y=y)
            l.append(h)
            x+=95
        marks.append(l)
        y+=90


bs=Button(text='Play with Computer',bg='plum3',fg='black',font='Abc 12 bold',command=partial(play,1))
bs.place(x=200, y=100)

bt=Button(text='Two Player',bg='plum3',fg='black',font='Abc 12 bold',command=partial(play,2))
bt.place(x=230,y=170)


root.mainloop()