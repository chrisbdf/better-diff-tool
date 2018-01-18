#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from random import choice
from random import shuffle

# Note:
# let splitstring be some string
# then:
# text == splitstring.join(text.split(splitstring))

# Also note: This is incomplete

class Scrambler():
    '''Used to produce sample scrambled texts from the sample corpus'''

    def __init__(self):
        self.master_text = self.read()


    def read(self):
        '''Read the document into a string and return the string.'''

        with open('3/hhgg_Original.txt', 'r') as i:
            return i.read()


    def scramble(self):
        '''Transform text'''

        print(self.master_text)

        doc = self.shuffle_paragraphs(self.master_text)
        doc = self.shuffle_sentences(doc)
        doc = self.shuffle_words(doc)

        print('\n\n\n\n' + doc)

        with open('3/hhgg_Scrambled.txt', 'w') as o:
            o.write(doc)


    def shuffle_paragraphs(self, document):
        '''Randomize the ordering of paragraphs in a document'''

        splitstring = '\n\n'
        tokenized_document = document.split(splitstring)

        # Delete things maybe
        tokenized_document =\
            [u for u in tokenized_document if not self.roll_a_zero(100)]

        shuffle(tokenized_document)

        return splitstring.join(tokenized_document)


    def shuffle_sentences(self, document):
        '''Randomize the ordering of sentences in a paragraph'''

        # Tokenize into paragraphs
        paragraph_splitstring = '\n\n'
        paragraphs = document.split(paragraph_splitstring)

        # For each paragraph
        sentence_splitstring = '.'
        for i in range(len(paragraphs)):
            # Randomly choose paragraphs to be shuffled
            if self.roll_a_zero(2):
                tokenized_paragraph = paragraphs[i].split(sentence_splitstring)

                # Delete things maybe
                tokenized_paragraph =\
                    [u for u in tokenized_paragraph if not self.roll_a_zero(5)]

                shuffle(tokenized_paragraph)

                paragraphs[i] = sentence_splitstring.join(tokenized_paragraph)

        # Recombine
        return paragraph_splitstring.join(paragraphs)


    def shuffle_words(self, document):
        '''Randomize the ordering of words in a sentence'''

        # Tokenize document into sentences
        sentence_splitstring = '.'
        sentences = document.split(sentence_splitstring)

        # Randomly select some sentences to scramble
        word_splitstring = ' '
        for i in range(len(sentences)):
            if self.roll_a_zero(8):
                tokenized_sentence = sentences[i].split(word_splitstring)

                # Delete things maybe
                tokenized_sentence =\
                    [u for u in tokenized_sentence if not self.roll_a_zero(10)]

                shuffle(tokenized_sentence)

                sentences[i] = word_splitstring.join(tokenized_sentence)

        doc = sentence_splitstring.join(sentences)

        return doc


    def roll_a_zero(self, n_sides):
        '''Roll a 100-sided die. If it comes up on 0, return True.'''

        sides = [u for u in range(n_sides)]
        roll = choice(sides)
        if roll == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    the_scrambler = Scrambler()
    the_scrambler.scramble()
