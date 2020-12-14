again="y"

while again !="n":

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


    text=input("Please input your text: ")

    dig1=text[1-1]
    dig2=text[2-1]

    print("There are these many colours to choose from:",len(colours))
    print("Here are the colours: \n black, dark blue, dark green, dark aqua, dark red, dark purple, gold, gray, dark gray, indigo, green, aqua, red, pink, yellow, white")
    

    col1=input(str("please enter your first colour from the list: "))

    print ("\n","Here is the final MOTD code:",col1,dig1)

    again=input("\nWould you like to repeat? [y/n] ")

