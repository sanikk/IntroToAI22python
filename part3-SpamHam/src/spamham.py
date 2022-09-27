from cmath import exp, log
import os

SMALL_NUMBER = 0.00001


def get_occurrences(filename):
    results = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            for line in file:
                count, word = line.strip().split(' ')
                results[word] = int(count)

        return results

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s" % str(e))
        raise


def get_words(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            words = [word for line in file for word in line.split()]

        return words

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


class SpamHam:
    """ Naive Bayes spam filter
        :attr spam: dictionary of occurrences for spam messages {word: count}
        :attr ham: dictionary of occurrences for ham messages {word: count}
    """

    def __init__(self, spam_file, ham_file):
        self.spam = get_occurrences(spam_file)
        self.ham = get_occurrences(ham_file)

    def evaluate_from_file(self, filename):
        words = get_words(filename)
        return self.evaluate(words)

    def evaluate_from_input(self):
        words = input().split()
        return self.evaluate(words)

    def evaluate_nolog(self, words):
        # def evaluate(self, words):
        """
        :param words: Array of str
        :return: probability that the message is spam (float)
        """
        # Implement me
        R = 1  # priori_spam / priori_ham
        for word in words:
            if word in self.spam:
                spamfaktor = self.spam[word] / 75268  # * 0.5 supistuu pois
            else:
                spamfaktor = SMALL_NUMBER
            if word in self.ham:
                hamfaktor = self.ham[word] / 290673  # * 0.5 supistuu pois
            else:
                hamfaktor = SMALL_NUMBER
            R *= spamfaktor / hamfaktor

        # total words in spam messages: 75268

        # total words in ham messages: 290673
        # if P(spam | message) > 0.5, classify as spam
        return R / (R + 1)

    def evaluate(self, words):
        # def paskaa(self, words):
        """
        :param words: Array of str
        :return: probability that the message is spam (float)
        """
        # Implement me
        calculated = {}
        logR = log(0.5) - log(0.5)
        for word in words:
            if word in calculated:
                spamfaktor, hamfaktor = calculated[word]
            else:
                if word in self.spam:
                    spamfaktor = self.spam[word] / 75268
                else:
                    spamfaktor = SMALL_NUMBER
                if word in self.ham:
                    hamfaktor = self.ham[word] / 290673
                else:
                    hamfaktor = SMALL_NUMBER
                calculated[word] = (spamfaktor, hamfaktor)
            logR += log(spamfaktor) - log(hamfaktor)

        # total words in spam messages: 75268

        # total words in ham messages: 290673
        # if P(spam | message) > 0.5, classify as spam
        return exp(logR) / (1 + exp(logR))
