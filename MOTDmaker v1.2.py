 #colours
colours = {
    "black": r"\u00A70",
    "dark blue": r"\u00A71",
    "dark green": r"\u00A72",
    "dark aqua": r"\u00A73",
    "dark red": r"\u00A74",
    "dark purple": r"\u00A75",
    "gold": r"\u00A76",
    "gray": r"\u00A77",
    "dark gray": r"\u00A78",
    "indigo": r"\u00A79",
    "green": r"\u00A7a",
    "aqua": r"\u00A7b",
    "red": r"\u00A7c",
    "pink": r"\u00A7d",
    "yellow": r"\u00A7e",
    "white": r"\u00A7f"
}
#split string into seperate characters of an array
def getchar(str):
    return [char for char in str]
def gui():
    global digits
    #dictionary for characters and their colour values
    digits = {
    }
    text=input("Please input your text: ")
    print("WARNING! IF DUPLICATE CHARACTERS ARE PRESENT ONLY THE COLOUR CODE FOR THE LAST IN THE STRING WILL BE OUTPUT!")
    print("There are these many colours to choose from:",len(colours))
    print("Here are the colours: ")
    for key in colours:
        print(key)
    #ask user what colour they want for each digit
    for i in range(0,len(text)):
        digits[getchar(text)[i]] = colours.get(
            str(
                input(
                    "What colour do you want for digit {}? (Enter as shown) ".format(getchar(text)[i])
                    )
                )
            )

def output():
    #printing the final product with colour
    print("Here is the final MOTD code: ")
    #print the code in the format of MOTD code
    for key in digits:
        print("{} {}".format(digits.get(key),key))
again = "y"
while again.lower() != "n":
    gui()
    output()
    again = input("Repeat?(y/n) ")