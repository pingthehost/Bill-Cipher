"""Gravity Falls: to solve the Bill Cipher.
Code to inspire people who don't know where mystery starts"""

#Use "-" to delimit integers, and "--" to create spaces
key = "abcdefghijklmnopqrstuvwxyz"
code = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
        "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]

mystery_solved=True

while mystery_solved:
    def decrypt(cipher):
        decoded = ""
        cipher = str(cipher)
        cipher = cipher.split("-")
        for string in cipher:
            if string in code:
                decoded += str(key[int(string) - 1])
            elif string == "":
                decoded += " "
            else:
                decoded += string
        print(decoded)

    bill_cipher = input('Enter the Bill Cipher: \n')
    decrypt(bill_cipher)

    while True:
        question = (input("Is the mystery solved [y/n]?\n"))
        if question == 'n':
            mystery_solved = True
            break
        elif question == 'y' :
            mystery_solved = False
            break
