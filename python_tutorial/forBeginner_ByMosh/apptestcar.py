select = ""
started = False
while select.lower() != "quit":
    select= input("> ").lower()
    if select == 'help':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")       
    if select == 'start':
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif select == 'stop':
        if not started:
            print("Car is already stoped!")
        else:
            started = False
            print("Car stopped.")
    else:
        print("I don't understand that ...")