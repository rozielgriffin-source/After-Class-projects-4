from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Rock Paper Scissors")
root.configure(bg="light blue")
root.geometry("600x450")

rock = Image.open("rock.jpg")
rock = rock.resize((100, 100))
rock_image = ImageTk.PhotoImage(rock)

paper = Image.open("paper.jpg")
paper = paper.resize((100, 100))
paper_image = ImageTk.PhotoImage(paper)

scissors = Image.open("scissors.jpg")
scissors = scissors.resize((100, 100))
scissors_image = ImageTk.PhotoImage(scissors)

title = Label(root, text="Rock Paper Scissors", font=("Arial", 24, "bold"), bg="light blue")

title.place(relx=0.5, y=40, anchor=CENTER)

player_label = Label(root, text="You", font=("Arial", 16, "bold"), bg="light blue")
player_label.place(x=170, y=90)


computer_label = Label(root, text="Computer", font=("Arial", 16, "bold"), bg="light blue")
computer_label.place(x=410, y=90)

player_image = Label(root, bg="light blue")
player_image.place(x=140, y=120)

computer_image = Label(root, bg="light blue")
computer_image.place(x=380, y=120)

computer_choice = 0

def play(player_choice):
    global computer_choice

    computer_choice = computer_choice + 1

    if computer_choice > 3:
        computer_choice = 1

    if player_choice == 1:
        player_image.config(image=rock_image)

    elif player_choice == 2:
        player_image.config(image=paper_image)

    elif player_choice == 3:
        player_image.config(image=scissors_image)

    if computer_choice == 1:
        computer_image.config(image=rock_image)

    elif computer_choice == 2:
        computer_image.config(image=paper_image)

    elif computer_choice == 3:
        computer_image.config(image=scissors_image)

    if player_choice == computer_choice:
        messagebox.showinfo("Result", "It's a tie!")

    elif player_choice == 1 and computer_choice == 3:
        messagebox.showinfo("Result", "You win! Rock beats Scissors.")

    elif player_choice == 2 and computer_choice == 1:
        messagebox.showinfo("Result", "You win! Paper beats Rock.")

    elif player_choice == 3 and computer_choice == 2:
        messagebox.showinfo("Result", "You win! Scissors beats Paper.")

    else:
        messagebox.showinfo("Result", "Computer wins!")

rock_button = Button( root, text="Rock", command=lambda: play(1), bg="brown", fg="white", width=10)
rock_button.place(x=100, y=330)


paper_button = Button(root, text="Paper",command=lambda: play(2), bg="brown", fg="white", width=10)
paper_button.place(x=250, y=330)

scissors_button = Button(
    root, text="Scissors", command=lambda: play(3), bg="brown", fg="white", width=10)
scissors_button.place(x=400, y=330)

root.mainloop()