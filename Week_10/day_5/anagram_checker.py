class Anagram:
    def __init__(self, file_name):
        self.anagrams = open(file_name)

    def is_valid_word(self):
        word = input("Choose a word: ")
        if word in self.anagrams:
            print("Word is not valid. Choose a word: ")
        else:
            print("Word is Valid")

    def get_anagrams(self, word):
        if self.is_valid_word():
            for line in self.anagrams:
                if sorted(word) == sorted(line):
                    return line
                else:
                    print("No anagrams found")


ana = Anagram('sowpods.txt')
ana.is_valid_word()
