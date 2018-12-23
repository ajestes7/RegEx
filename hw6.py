import re 
import unittest

def sumNums(fileName):
    inFile = open(fileName, 'r')
    
    startLine = str(inFile.readlines())
    stripLine = startLine.strip('-')

    findInt = re.findall(r'\d+', stripLine)

    allInt = map(int, findInt)
    sumInt = sum(allInt)

    inFile.close()

    return(int(sumInt))

def countWord(fileName, word):
    inFile = open(fileName, 'r')

    startLine = str(inFile.readlines())
    findWords = re.findall(r'\b'+word+r'\b', startLine, re.IGNORECASE)

    wordCount = 0

    for x in findWords:
        wordCount += 1

    inFile.close()
    
    return wordCount

def listURLs(fileName):
    inFile = open(fileName, 'r')

    startLine = str(inFile.readlines())
    splitLine = startLine.split(',')

    findURL = re.findall(r'www.(?:[-\w.]|(?:%[\da-fA-F]{2}))+', startLine)

    inFile.close()
    
    return findURL

class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
