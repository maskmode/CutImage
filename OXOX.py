# Код игры крестики-нолики

# Импортируем модуль для работы с графическим интерфейсом
from tkinter import *

# Создаем окно
window = Tk()
window.title("Крестики-нолики")

# Создаем переменные для хранения состояния игры
player = "X"
moves = 0


# Функция для обработки нажатия на кнопку
def click(button):
    global player, moves
    if button["text"] == " " and player == "X":
        button["text"] = "X"
        player = "O"
    elif button["text"] == " " and player == "O":
        button["text"] = "O"
        player = "X"
    moves += 1


# Функция для проверки победителя
def check_winner():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        return "X"
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        return "O"
    elif moves == 9:
        return "draw"
    else:
        return None


# Создаем кнопки
button1 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button1))
button1.grid(row=1, column=0)

button2 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button2))
button2.grid(row=1, column=1)

button3 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button3))
button3.grid(row=1, column=2)

button4 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button4))
button4.grid(row=2, column=0)

button5 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button5))
button5.grid(row=2, column=1)

button6 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button6))
button6.grid(row=2, column=2)

button7 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button7))
button7.grid(row=3, column=0)

button8 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button8))
button8.grid(row=3, column=1)

button9 = Button(window, text=" ", font=("Arial 20"), height=4, width=8, command=lambda: click(button9))
button9.grid(row=3, column=2)

# Запускаем главный цикл
window.mainloop()
