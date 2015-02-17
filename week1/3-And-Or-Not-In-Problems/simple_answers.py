txt=''
while txt!='q':
    print("Type 'q' to exit something else to have a chat!")
    txt=str(input("The system is waiting for your input: "))
    if 'hello' in txt.lower():
        print()
        print("Hello there, good stranger!")
        print()
    elif 'how are you?' in txt.lower():
        print()
        print("I am fine, thanks. How are you?")
        print()
    elif 'feelings' in txt.lower():
        print('\n I am a machine. I have no feelings.\n')
    elif 'age' in txt.lower():
        print('\n I have no age. Only current timestamp.\n')
    elif txt=='q':
        quit()
    else:
        continue