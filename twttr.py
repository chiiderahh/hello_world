answer = input("input: ")

print("output: ", end="")

for letter in answer:

    if not letter in ['a', 'e', 'i', 'o', 'u']:
        print(letter, end="")

print()
