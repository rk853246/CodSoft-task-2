#<-----------------------Important library files----------------------->
import tkinter as tk
from tkinter import messagebox

#<-----------------------Game Matric GUI funtion---------------------------------->
def Matrix():
    global cells
    global states
    cells=[[0,0,0],
           [0,0,0],
           [0,0,0]]
    
    states = [['', '', ''],
              ['', '', ''],
              ['', '', '']]


    cells[0][0]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua",command=lambda: On_Button_Click(0,0,states))
    cells[0][0].grid(row=0,column=0)

    cells[0][1]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua", command=lambda: On_Button_Click(0,1,states))
    cells[0][1].grid(row=0,column=1)

    cells[0][2]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua", command=lambda: On_Button_Click(0,2,states))
    cells[0][2].grid(row=0,column=2)

    cells[1][0]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua", command=lambda: On_Button_Click(1,0,states))
    cells[1][0].grid(row=1,column=0)

    cells[1][1]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua", command=lambda: On_Button_Click(1,1,states))
    cells[1][1].grid(row=1,column=1)

    cells[1][2]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua", command=lambda: On_Button_Click(1,2,states))
    cells[1][2].grid(row=1,column=2)

    cells[2][0]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua", command=lambda: On_Button_Click(2,0,states))
    cells[2][0].grid(row=2,column=0)

    cells[2][1]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua", command=lambda: On_Button_Click(2,1,states))
    cells[2][1].grid(row=2,column=1)

    cells[2][2]=tk.Button(root,text="", font=("Helvetica", 55),height=1,width = 4,bg="Aqua", command=lambda: On_Button_Click(2,2,states))
    cells[2][2].grid(row=2,column=2)

#<------------------------------------Minimax algorithm-------------------------->
def evaluate(states):
    for row in states:
        if row.count(row[0]) == len(row) and row[0] != '':
            return row[0]

    for col in range(3):
        if states[0][col] == states[1][col] == states[2][col] and states[0][col] != '':
            return states[0][col]

    if states[0][0] == states[1][1] == states[2][2] and states[0][0] != '':
        return states[0][0]
    if states[0][2] == states[1][1] == states[2][0] and states[0][2] != '':
        return states[0][2]

    if any('' in row for row in states):
        return None  # Game is still ongoing
    return 'Tie'

def find_best_move(states):
    best_eval = float('-inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if states[row][col] == '':
                states[row][col] = 'X'
                eval = minimax(states, 0, False)
                states[row][col] = ''

                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)

    return best_move
    

def minimax(states, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'Tie': 0}

    if evaluate(states) != None:
        return scores[evaluate(states)]

    if is_maximizing:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if states[row][col] == '':
                    states[row][col] = 'X'
                    eval = minimax(states, depth + 1, False)
                    states[row][col] = ''
                    max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if states[row][col] == '':
                    states[row][col] = 'O'
                    eval = minimax(states, depth + 1, True)
                    states[row][col] = ''
                    min_eval = min(min_eval, eval)
        return min_eval

#<-----------------------Button Click---------------------------------->  
def On_Button_Click(row,column,states):
    if states[row][column] == '':
        states[row][column]= 'O'
        cells[row][column]['text']='O'
        
    else:
        messagebox.showinfo("information","Cell already occupied. Try again.")

    if evaluate(states) != None:
            result = evaluate(states)
            if result == 'Tie':
                 messagebox.showinfo("Infomation","Game Tie!")
                 #print("Tie")
            else:
                messagebox.showinfo("Information",f"{result} wins!")
                #print(f"{result} wins!")
            return 0
                
            

    #print("Computer's move:")
    best_move = find_best_move(states)
    states[best_move[0]][best_move[1]] = 'X'
    cells[best_move[0]][best_move[1]]['text']='X'

    if evaluate(states) != None:
        result = evaluate(states)
        if result == 'Tie':
            messagebox.showinfo("Information","Game Tie!")
            print("It's a tie!")
        else:
            messagebox.showinfo("Information",f"{result} wins!")
            #print(f"{result} wins!")
        return 0






    

#<-----------------------GUI for game---------------------------------->
root=tk.Tk()
root.title("Tic Tac Toe")
root.geometry("546x432")
Matrix()
# Welcome_Label()

root.mainloop()   