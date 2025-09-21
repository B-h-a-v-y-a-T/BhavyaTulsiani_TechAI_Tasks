from random import randint

freq = {}
chances = 6
output = ["Gray","Gray","Gray","Gray","Gray"]
num = randint(1,100)

with open ("data.txt", "r") as file:
    line =  file.read().splitlines()
    word = line[num]
word = word.upper()


while chances>0:
    flag = 1
    freq = {}
    output = ["Gray","Gray","Gray","Gray","Gray"]

    guess = input("Enter a 5 letter word: ").upper()

    if len(guess)!=5:
        print("Wrong Length. Please Enter a 5 Letter Word")
        continue
    
    for i in range(len(word)):
        if word[i] in freq:
            freq[word[i]] += 1
        else:
            freq[word[i]]=1

    for i in range(5):
        if(guess[i]==word[i]):
            output[i]="Green"
            freq[word[i]] -= 1
    
    for i in range(5):
        if guess[i] in freq:
            if output[i]!="Green" and freq[guess[i]]>0:
                output[i] = "Yellow"
                freq[guess[i]] -= 1

    print(*output)
    for i in range(5):
        if(output[i]!="Green"):
            flag = 0
            print(f"Wrong Answer. You have {chances-1} chances left.")
            break
    
    if flag == 1:
        print(f"You have won the Game with {chances} chances left.")
        exit()
    chances -= 1
    print()

print("The Right Word is:", word)


