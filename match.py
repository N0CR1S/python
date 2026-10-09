name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ronald":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
