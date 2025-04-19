#get user input
answer= input("what is the answer to the great question of life,the universe and evertyhing?")

#print yes if answer is 42 or forty two or forty-two
if answer.strip() == "42":
    print("yes")
elif answer.lower().strip() == "forty two":
    print("yes")
elif answer.lower().strip() == "forty-two":
    print("yes")

#otherwise print no
else:
    print("no")
