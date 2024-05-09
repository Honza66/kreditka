from tkinter import *
root = Tk()
root.title('Platnost čísla karty')
root.geometry('300x200')
root.resizable(False, False)


def card_valid():

    card_number = card_entry.get()
    numbers = [int(number) for number in card_number]


    sum_odd_num = sum(numbers[1::2])
    
    sum_even_num = sum((number * 2) % 9 if number != 9 else 9 for number in numbers[::2])
    
    valid = (sum_even_num + sum_odd_num) % 10 == 0
    if valid:
        card_result_label = Label(root, text='Karta je platná!')
        card_result_label.grid(row=2, column=1)
    else:
        card_result_label = Label(root, text='Karta je neplatná!')
        card_result_label.grid(row=2, column=1)

card_label = Label(root, text='Zadejte číslo karty')
card_label.grid(row=0, column=0)
card_entry = Entry(root)
card_entry.grid(row=0,column=1)
card_button = Button(root, text='Ověřit kartu',command=card_valid)
card_button.grid(row=1, column=1)


root.mainloop()

