# text = "A good book would sometimes cost as much as a good house."


def freq():

    str = str.split()
    str2 = []

    for i in str:

        if i not in str2:
            str2.append(i)

    for i in range(0, len(str2)):
        # count the frequency of each word(present
        # in str2) in str and print
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))


class Text:
    def __init__(self, str):
        self.str = str


text = Text("A good book would sometimes cost as much as a good house.")

