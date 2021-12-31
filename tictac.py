# Check out the readme.md for a high level description of the program
# Made by Jonan for the final project of CS50. Shoutout David J. Malan

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import webbrowser
import math

# Creating the main window and the four frames. Doing it at the top because some function relies on root
root = Tk()
root.title("TicTac50")
root.iconbitmap("C:\\Users\\Jonan\\Desktop\\project\\tictac.ico")
root.resizable(False, False)
pvp = Frame(root)
pve = Frame(root)
settings = Frame(root, bg="black")
mainmenu = Frame(root, bg="black")
pvp.grid(row=0, column=0, sticky="nsew")
pve.grid(row=0, column=0, sticky="nsew")
settings.grid(row=0, column=0, sticky="nsew")
mainmenu.grid(row=0, column=0, sticky="nsew")


# Global variables 
counter = 0
active_frame = "none"
hum = 0
ai = 1
players = [{"symbol": "X", "num": 0}, {"symbol": "O", "num": 1}]

# A practical list of lists to make checking for wins easy
winconditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# The board which is initially set to all 2. Player 1 will put a 0 in the board, Player 2 a 1.
board = [2, 2, 2, 2, 2, 2, 2, 2, 2]

# Function behind the "New Game" button on the GUI. Also used after clicking "OK" on end of game message
def reset():
    global counter
    
    for i in range(9):
        pvp_field[i]["text"] = ' '
        pve_field[i]["text"] = ' '
        board[i] = 2
    
    counter = 0
    first()

# A simple function that calls minimax to start if the human chooses to be Player 2
def first():
    if hum == 1:
        click(minimax(board, True)["position"])

# Showing end of round messages to the human
def end():
    if won(0):
        if active_frame == "pvp":
            messagebox.showinfo("TicTac50", "Player 1 wins!")
        
        elif hum == 0:
            messagebox.showinfo("TicTac50", "You beat SkyNet!")
        
        else:
            messagebox.showinfo("TicTac50", "SkyNet beat you!")
        
        return True
    
    elif won(1):
        if active_frame == "pvp":
            messagebox.showinfo("TicTac50", "Player 2 wins!")
        
        elif hum == 1:
            messagebox.showinfo("TicTac50", "You beat SkyNet!")
        
        else:
            messagebox.showinfo("TicTac50", "SkyNet beat you!")
        
        return True

    elif counter == 9:
        messagebox.showinfo("TicTac50", "Tie!")
        return True
    
    return False

# Comparing the board to all possible win combinations for the either player
def won(i):
    for win in winconditions:
        if board[win[0]] == i and board[win[1]] == i and board[win[2]] == i:
            return True

    return False

# Main game loop is found here. The design is a bit messy I think, because it may be even cleaner if the main loop was somehow seperate from the "clicking" function
def click(i):
    global counter
    
    if board[i] != 2:
        return
    
    if counter % 2 == 0:
        pve_field[i]["text"] = players[0]["symbol"]
        pvp_field[i]["text"] = players[0]["symbol"]
        board[i] = players[0]["num"]
    
    else:
        pve_field[i]["text"] = players[1]["symbol"]
        pvp_field[i]["text"] = players[1]["symbol"]
        board[i] = players[1]["num"]

    counter += 1
    if end():
        reset()
    
    if active_frame == "pve":
        if ai == counter % 2:
            click(minimax(board, True)["position"])
        if end():
            reset()

# A small helper function that I took from https://www.codegrepper.com/code-examples/python/python+find+all+positions+of+value+in+list
def indices(list, i):
    indices = [index for index, element in enumerate(list) if element == i]
    return indices

# This is my baby, courtesy to the top 5 videos that pop up on YouTube when you type in "tic tac toe minimax"
def minimax(board, max):
    # If SkyNet starts, let him choose randomly
    if board.count(2) == 9:
        random.seed()
        return {"position": random.randrange(0, 9, 1), "score": 0}
        
    # All base cases covered
    elif won(ai):
        return {"position": None, "score": (board.count(2) + 1) * 1}
    elif won(hum):
        return {"position": None, "score": (board.count(2) + 1) * -1}
    elif board.count(2) == 0:
        return {"positon": None, "score": 0}
    
    # This is where the magic happens: A minimax calling himself but for calculating future moves. Split up in two parts that alternate for each player.
    if max == True:
        best = {"position": None, "score": -math.inf}

        for i in indices(board, 2):
            board[i] = ai
            sim = minimax(board, False)
            board[i] = 2
            sim["position"] = i
            if sim["score"] > best["score"]:
                best = sim

    else:
        best = {"position": None, "score": math.inf}

        for i in indices(board, 2):
            board[i] = hum
            sim = minimax(board, True)
            board[i] = 2
            sim["position"] = i
            if sim["score"] < best["score"]:
                best = sim

    return best

# Enables switching between the frames
def show_frame(frame):
    global active_frame, hum
    frame.tkraise()
    
    if frame == mainmenu:
        hum = 0
        reset()
        active_frame == "none"

    if frame == pve:
        active_frame = "pve"
    
    elif frame == pvp:
        active_frame = "pvp"

# Handling the player's choice and making the buttons cooler
def choose_player(p, btn):
    global hum, ai
    hum = p
    if hum == 0:
        rb1["text"] = "$ Player 1 $"
        rb2["text"] = "Player 2"
        ai = 1
    else:
        rb1["text"] = "Player 1"
        rb2["text"] = "$ Player 2 $"
        ai = 0

# For making the buttons cooler
def hover(btn):
    tmp = btn["text"]
    btn.bind("<Enter>", func=lambda e: btn.config(text=("$ " + tmp + " $")))

    btn.bind("<Leave>", func=lambda e: btn.config(text=tmp))

# Another helper function that handles URLs
def callback(url):
    webbrowser.open_new(url)

# Initializing and placing the main menu elements in two large blocks
btn_pvp = Button(mainmenu, fg="white", text="Play against your friend :)", command=lambda: show_frame(pvp), bg="black", font=("Impact", 14), borderwidth=0, width=25, height=2, activebackground="black", activeforeground="white")
btn_pve = Button(mainmenu, fg="white", text="Play against SkyNet!", command=lambda: show_frame(settings), bg="black", font=("Impact", 14), borderwidth=0, width=25, height=2, activebackground="black", activeforeground="white")
text = Label(mainmenu, fg="white", text="TicTac50", font=("Impact", 55), bg="black")
desc = Label(mainmenu, fg="white", font=("Impact", 14), bg="black", text="Play Tic-Tac-Toe against your friend next to you or\nSkyNet, a pretty strong minimax algorithm\nThis is my final project for CS50, I hope you like it.\nCheck readme.md for all relevant info.\nText in blue will open your browser.")
link1 = Label(mainmenu, text="Rules", font=("Impact", 14), bg="black", fg="blue", cursor="hand2")
link2 = Label(mainmenu, text="For nerds only", font=("Impact", 14), bg="black", fg="blue", cursor="hand2")
link3 = Label(mainmenu, text="Minimax", font=("Impact", 14), bg="black", fg="blue", cursor="hand2")
link1.bind("<Button-1>", lambda e: callback("https://www.exploratorium.edu/brain_explorer/tictactoe.html"))
link2.bind("<Button-1>", lambda e: callback("https://www.reddit.com/r/TrueTicTacToe/"))
link2.bind("<Button-1>", lambda e: callback("https://www.javatpoint.com/mini-max-algorithm-in-ai"))

text.place(relx=0.5, rely=0.13, anchor=CENTER)
desc.place(relx=0.5, rely=0.4, anchor=CENTER)
link1.place(relx=0.2, rely=0.6, anchor=CENTER)
link2.place(relx=0.8, rely=0.6, anchor=CENTER)
link3.place(relx=0.5, rely=0.6, anchor=CENTER)
btn_pvp.place(relx=0.25, rely=0.9, anchor=CENTER)
btn_pve.place(relx=0.8, rely=0.9, anchor=CENTER)

# Same for the settings menu
settings_title = Label(settings, font=("Impact", 40), text="Choose your player", bg="black", fg="white")
settings_label2 = Label(settings, font=("Impact", 20), text="Player 1 ( X ) starts", bg="black", fg="white")
settings_label3 = Label(settings, font=("Impact", 20), text="Player 2 ( O ) is trailing", bg="black", fg="white")
rb1 = Button(settings, text="Player 1", command=lambda: choose_player(0, rb1), font=("Impact", 14), bg="black", fg="white", relief="flat", borderwidth=0, activeforeground="white", activebackground="black")
rb2 = Button(settings, text="Player 2", command=lambda: choose_player(1, rb2), font=("Impact", 14), bg="black", fg="white", relief="flat", borderwidth=0, activeforeground="white", activebackground="black")
sbtn = Button(settings, text="Start", command=lambda: [show_frame(pve), first()], bg="black", fg="white", width=25, height=2, font=("Impact", 14), borderwidth=0, activeforeground="white", activebackground="black")
bbtn = Button(settings, text="Back", command=lambda: show_frame(mainmenu), bg="black", fg="white", width=25, height=2, font=("Impact", 14), borderwidth=0, activeforeground="white", activebackground="black")

settings_title.place(anchor=CENTER, relx=0.5, rely=0.13)
settings_label2.place(anchor=CENTER, relx=0.5, rely=0.3)
settings_label3.place(anchor=CENTER, relx=0.5, rely=0.6)
rb2.place(anchor=CENTER, relx=0.5, rely=0.7)
rb1.place(anchor=CENTER, relx=0.5, rely=0.4)
bbtn.place(anchor=CENTER, relx=0.15, rely=0.95)
sbtn.place(anchor=CENTER, relx=0.85, rely=0.95)

# And again same for the pvp page. Here, I utilize a smart loop for creating and gridding the squares. Still had to use a stupid block because the command functions somehow wouldn't work
pvp_field = []
for i in range(9):
    pvp_field.append(Button(pvp, height=5, width=10, command=lambda: click(i), text=" ", font=("Helvetica", 20)))
    
pvp_field[0]["command"] = lambda: click(0)
pvp_field[1]["command"] = lambda: click(1)
pvp_field[2]["command"] = lambda: click(2)
pvp_field[3]["command"] = lambda: click(3)
pvp_field[4]["command"] = lambda: click(4)
pvp_field[5]["command"] = lambda: click(5)
pvp_field[6]["command"] = lambda: click(6)
pvp_field[7]["command"] = lambda: click(7)

k = 0
for i in range(9):
    o = i % 3
    
    if k < 3:
        j = 0
    elif k < 6:
        j = 1
    else:
        j = 2
    k += 1

    pvp_field[i].grid(row = j, column = o)

pvp_reset = Button(pvp, text="New Game", command=reset)
pvp_menu = Button(pvp, text="Main Menu", command=lambda: show_frame(mainmenu))
pvp_reset.grid(row = 12, column=0)
pvp_menu.grid(row = 12, column=2)

# Exactly the same for the pve page
pve_field = []
for i in range(9):
    pve_field.append(Button(pve, height=5, width=10, command=lambda: click(i), text=" ", font=("Helvetica", 20)))
    
pve_field[0]["command"] = lambda: click(0)
pve_field[1]["command"] = lambda: click(1)
pve_field[2]["command"] = lambda: click(2)
pve_field[3]["command"] = lambda: click(3)
pve_field[4]["command"] = lambda: click(4)
pve_field[5]["command"] = lambda: click(5)
pve_field[6]["command"] = lambda: click(6)
pve_field[7]["command"] = lambda: click(7)

k = 0
for i in range(9):
    o = i % 3
    
    if k < 3:
        j = 0
    elif k < 6:
        j = 1
    else:
        j = 2
    k += 1

    pve_field[i].grid(row = j, column = o)

pve_reset = Button(pve, text="New Game", command=reset)
pve_menu = Button(pve, text="Main Menu", command=lambda: show_frame(mainmenu))
pve_reset.grid(row = 12, column=0)
pve_menu.grid(row = 12, column=2)

# Here I activate the hover function for that swag 
hover(btn_pvp)
hover(btn_pve)
hover(sbtn)
hover(bbtn)

# Idk why my code doesn't feel clean but it is what it is
choose_player(0, rb1)

# idek what this does ???
root.mainloop()