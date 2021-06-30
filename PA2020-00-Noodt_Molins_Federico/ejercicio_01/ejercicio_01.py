import conversor

def save_transaction(price, qtty, description):
    file = open("sales.txt", "a")
    file.write("%3d;%8.2f;%-16s\n" % (qtty, price * qtty, description))
    file.close()



running = True

while running:
    option = 1
    for choice in conversor.Items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")

    choice = int(input("Elija opción: "))

    if choice == option:
        running = False
    else:
        msg = conversor.Items[choice - 1] + " cantidad? "
        qtty = int(input(msg))
        save_transaction(conversor.Precios[choice - 1], qtty, conversor.Items[choice - 1])
