#get user input
greeting= input("Greeting: ")

new_greeting = greeting.lower().strip()

#print $0 if greeting is hello
if 'hello' in new_greeting:
    print("$0")

#if greeting starts with 'h' print $20
elif 'h' == new_greeting[0]:
    print("$20")

#otherwise print $100
else:
    print("$100")
