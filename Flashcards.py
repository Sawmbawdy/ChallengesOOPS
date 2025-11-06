class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+'('+self.meaning+ ')'
    
flashcards = []
while True:
    WORD = str(input("Enter Word:"))
    MEANING = str(input("Enter Meaning:"))

    flashcards.append(flashcard(WORD, MEANING))
    options = int(input("If you want to make another, type 1 and you don't want to type 0:"))

    if (options) == 0:
        break
    else:
        pass

print("\nYour Flashcards ------")
for i in flashcards:
    print(">", i)