class Puzzle:


    def __init__(self, type):

        self.__type = type

        print("Puzzle of type %s initiated" % self.__type)



class WordSearchPuzzle(Puzzle):


    __type = "Word Search Puzzle"




    def __init__(self, words):

        self.__words = words

        super().__init__(WordSearchPuzzle.__type)

    

    def is_substring_of(self, word_portion):

        '''

        This method should check how many words it is a sibstring of.

        Note that your solution should not be case sensitive

        returns: an int representing the number of words this is a substring of

        '''

        counter = 0

        for word in self.__words:
            if word_portion in word:
                counter += 1

        return counter

    

    def is_match(self, player_word):

        '''

        This method should check to see if the word played by the player is

        in the word search array.

        Solution should not be case sensitive.

        returns: True if contained in array, false otherwise.

        '''

        match = False

        return match

    




answers = ["Jungle", "Forest", "Trees", "Green", "Amazon", "Dessert", "Ambient"]

wordsearch = WordSearchPuzzle(answers)