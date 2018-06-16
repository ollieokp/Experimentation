name = input("what is your name? ")
number = input("how old are you? ")
while name != "":
    for x in range(int(number)):
        print(name, end =" ")
    print()
    name = input("tipe another name, or just hold [ENTER]  to quit: ")
    number = input ("how old is this other person: ")
print("thanks for playing!")
