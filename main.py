import random

score = 0
turns = 0
words = ["car", "tree", "cave", "blood", "team", "dice", "animal", "plane", "world", "house", "school", "captain",
         "teacher", "laptop", "street", "door", "wall", "head", "arm", "phone", "pizza", "food"]

print("_" * 21)
print("|\t Anagram Game \t|")
print("_" * 21, "\n")


def startGame():
    try:
        global turns, score
        turns = 5
        chosenWord = words[random.randint(0, len(words) - 1)]
        print("Your Anagram Word:", mixString(chosenWord))
        words.remove(chosenWord)

        while turns > 0:
            guess = input("Your Answer: ")

            if guess.lower() == chosenWord:
                print("Your Answer is Correct!")
                print("_" * 20)
                score += 1
                break
            else:
                print("Your Answer is Wrong!")
                turns -= 1
                print(f"{turns} Turns Left!")
                print("_" * 20)
        else:
            print("GAME OVER!")
            print(f"The Correct Word Was ( {chosenWord.capitalize()} ).")
    except KeyboardInterrupt:
        print()
        print("_" * 20)
        print("\nError: Something Went Wrong!")
        quit()


def mixString(word=""):
    while True:
        shoveledWord = ""
        charWord = []

        for i in word:
            charWord.append(i)

        for _ in charWord:
            char = charWord[random.randint(0, len(word) - 1)]
            charWord.remove(char)
            charWord.insert(random.randint(0, len(charWord) - 1), char)

        for h in charWord:
            shoveledWord += h

        if word != shoveledWord:
            break

    return shoveledWord


def main():
    startGame()
    while True:
        try:
            if len(words) == 0:
                print("Congratulation! You solved all the words.")
                break

            q = input("Do you want to play a new game? (Y/N)")

            if q.upper() == "N":
                print("_" * 20)
                print(f"Highest Score: {score}")
                print("Good Bye!")
                break
            elif q.upper() == "Y":
                print("_" * 20)
                main()
        except KeyboardInterrupt:
            print()
            print("_" * 20)
            print("\nError: Something Went Wrong!")
            quit()


main()
