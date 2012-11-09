import math
import re
import string
import sys

class Bayesian:
    """ A Bayesian classifier with Laplacian smoothing
    """
    def __init__(self, k):
        """ k = # of categories
        """
        self.k = k
        self.m = 0
        self.x_counts = {}
        self.y_counts = [0] * k

    def train(self, X, y):
        """ X is an array of keys which occur in the sample with category y
        """
        for key in X:
            if key not in self.x_counts:
                self.x_counts[key] = [0] * self.k
            self.x_counts[key][y] += 1
        self.y_counts[y] += 1
        self.m += 1

    def prob(self, X, y):
        """ Returns the log probability that the sample X belongs to category y
        """
        p = 0
        for key in X:
            if key in self.x_counts:
                p_i = math.log(1 + self.x_counts[key][y]) - math.log(self.k + sum(self.x_counts[key]))
            else:
                p_i = -math.log(self.k)
            p += p_i
            #print p_xi, p_y, p_xi_y, p
        return p, math.exp(p)

    def show(self):
        for key in self.x_counts:
            print key, self.x_counts[key]
        print self.y_counts
        print self.m
        print self.k

def get_words(lines):
    """ Returns the set of words occuring in |lines| after some cleanup
    """
    cleanup = re.compile('[%s]' % re.escape(string.punctuation))
    words = set()
    for line in lines:
        clean_line = cleanup.sub('', line)
        for word in clean_line.strip().lower().split(" "):
            words.add(word)
    return words

def get_paras(filename):
    paragraphs = []
    lines = []
    for line in open(filename):
        l = line.strip()
        if len(l) == 0:
            paragraphs.append(get_words(lines))
            lines = []
        else:
            lines.append(l)
    return paragraphs

if __name__ == "__main__":
    """ Sample use case: classify input text between lines from Sherlock Holmes
        and Alice in Wonderland. I couldn't find a simple enough sample set of
        spam/non-spam e-mails.
    """
    b = Bayesian(2)

    paras = get_paras("sherlock.txt")
    for para in paras:
        b.train(para, 0)

    paras = get_paras("alice.txt")
    for para in paras:
        b.train(para, 1)

    #b.show()

    print 'Type in a paragraph of text to be classified. A blank line starts the classifier.'

    while True:
        lines = []
        line = sys.stdin.readline().strip()
        while len(line) > 0:
            lines.append(line)
            line = sys.stdin.readline().strip()
        words = get_words(lines)
        print words
        print b.prob(words, 0), b.prob(words, 1)
