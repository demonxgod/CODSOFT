import tkinter as tk
import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"


def on_choice(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    winner = determine_winner(user_choice, computer_choice)
    
    user_label.config(text=f'You chose: {user_choice}')
    computer_label.config(text=f'Computer chose: {computer_choice}')
    
    if winner == "tie":
        result_label.config(text="It's a tie!")
    elif winner == "user":
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")


user_label = tk.Label(root, text="You chose: ")
user_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer chose: ")
computer_label.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)


rock_button = tk.Button(root, text="Rock", width=10, command=lambda: on_choice('rock'))
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: on_choice('paper'))
paper_button.pack(side=tk.LEFT, padx=20)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: on_choice('scissors'))
scissors_button.pack(side=tk.LEFT, padx=20)


root.mainloop()
