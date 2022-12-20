from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.title("Rock Paper Scissors Game")
app_font =("Comic Sans MS", 10, "bold")
root.config(bg = '#000311')
root.geometry('750x350')

player_score = 0
computer_score = 0
options = [('rock', 0), ('paper', 1), ('scissors', 2)]


Label(text = 'Python Gaɱe ', font = font.Font(family = "Comic Sans MS",size = 20), fg = 'SeaGreen',bg = '#000311').pack()
Label(text = 'Rock  Paper  Scissors', font = font.Font(family =  "Comic Sans MS",size = 20), fg = 'Khaki',bg = '#000311').pack()


def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'You Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if player_input == computer_input:
        winner_label.config(text = "Tie",fg ='white')
    elif (player_input[1]-computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text="You Won!!!",fg ='green')
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!",fg ='red')
        computer_score_label.config(text='Computer Score : ' + str(computer_score))


def get_computer_choice():
    return random.choice(options)



winner_label = Label(text = "Let's Start the Game...", fg = 'AliceBlue', bg = '#000311', font = font.Font(family = "Comic Sans MS",size = 12), pady = 8)
winner_label.pack()

input_frame = Frame(root, bg = '#000311')
input_frame.pack()


player_options = Label(input_frame, text = "Choose Options : ", font = app_font, fg = 'PaleTurquoise', bg = '#000311')
player_options.grid(row = 1, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'SaddleBrown', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 2, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'DimGray', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 2, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'RoyalBlue', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 2, column = 3, padx = 8, pady = 5)


score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'DarkSeaGreen', bg = '#000311')
score_label.grid(row = 3, column = 0)

player_choice_label = Label(input_frame, text = 'You Selected : --»', fg = 'grey',font = app_font, bg = '#000311')
player_choice_label.grid(row = 4, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : 0', fg = 'green',font = app_font, bg = '#000311')
player_score_label.grid(row = 4, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : --»', font = app_font, fg = 'MistyRose', bg = '#000311')
computer_choice_label.grid(row = 5, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = ' Computer Score : 0', font = app_font, fg = 'red', bg = '#000311')
computer_score_label.grid(row = 5, column = 2, padx = (10,0), pady = 5)

root.mainloop()