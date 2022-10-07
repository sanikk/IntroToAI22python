import math
import os
import numpy as np
from PIL import Image
import random

NUMBER_OF_PIXELS = 28 * 28
IMAGE_SIZE = 28


def get_chars(filename):
    """
    Reads the classes of characters
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            chars = [line[0] for line in file]

        return chars

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


def get_images(filename):
    """
    Reads the images (black pixel is 1, white pixel is 0 in the input)
    Trasnforms (0, 1) values to (-1.0, 1.0)
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    vectors = []

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            for line in file:
                vectors.append([1.0 if float(v) == 1 else -
                               1.0 for v in line.strip().split(',')])

        return vectors

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


class Perceptron:
    """ Perceptron
        :attr data: list of objects that represent images
    """

    def __init__(self, images, chars):
        idata = get_images(images)
        cdata = get_chars(chars)

        self.data = [{'vector': v, 'char': c} for (v, c) in zip(idata, cdata)]
        random.seed()
        self.weights = [0 for i in range(NUMBER_OF_PIXELS)]

    def train(self, target_char, opposite_char, steps):
        # Implement method
        # maksimitarkkuus 0.988950276243094 ?
        # toi tuli aika pienellä toistomäärällä loppujen lopuks, varmaan lähdeaineiston koosta johtuen.

        print("Starting training")

        #print(f"{self.weights = }")

        step = 0
        while step < steps:
            i = random.randint(0, 4999)
            y = self.data[i]['char']
            x = self.data[i]['vector']
            # print(f"{y = }")

            if y != target_char and y != opposite_char:
                # print(
                #    f"mismatch {y} != {target_char} and {opposite_char} is {y != target_char and y!=opposite_char}")
                continue

            z = 0
            for j in range(NUMBER_OF_PIXELS):
                z += self.weights[j] * x[j]
            if z >= 0 and y == opposite_char:
                self.weights = [self.weights[j] - x[j]
                                for j in range(NUMBER_OF_PIXELS)]
            if z < 0 and y == target_char:
                self.weights = [self.weights[j] + x[j]
                                for j in range(NUMBER_OF_PIXELS)]
            step += 1
        # print(f"{self.weights}")

    def test(self, target_char, opposite_char):
        """Tests the learned perceptron with the last 1000 x,y pairs.
        (Note that this only counts those ones that belong either to the plus or minus classes.)

        :param target_char: the target character we are trying to distinguish
        :param opposite_char: the opposite character
        :return: the ratio of correctly classified characters
        """
        success = 0
        examples = self.data[5000:]

        examples = [e for e in examples if e['char']
                    in (target_char, opposite_char)]

        for e in examples:
            z = np.dot(e['vector'], self.weights)
            if (z >= 0 and e['char'] == target_char) or (z < 0 and e['char'] == opposite_char):
                success += 1

        return float(success) / len(examples)

    def save_weights(self, filename):
        """Draws a 28x28 grayscale picture of the weights

        :param filename: Name of the file where weights will be saved
        """
        pixels = [.01 + .98 / (1.0 + float(math.exp(-w)))
                  for w in self.weights]

        Image.fromarray(np.array(pixels).reshape(
            IMAGE_SIZE, IMAGE_SIZE), mode="L").save(filename)
class NearestFlanders(Perceptron):
    """ Nearest Neighbor using parts of Perceptron
        :attr data: list of objects that represent images
    """

    def __init__(self, images, chars):
        idata = get_images(images)
        cdata = get_chars(chars)

        self.data = [{'vector': v, 'char': c} for (v, c) in zip(idata, cdata)]
        random.seed()
        #self.weights = [0 for i in range(NUMBER_OF_PIXELS)]
        # dict jossa jokaiselle
        self.weights = {}

    def train(self, target_char, opposite_char, steps):
        # Implement method
        # maksimitarkkuus 0.988950276243094 ?
        # toi tuli aika pienellä toistomäärällä loppujen lopuks, varmaan lähdeaineiston koosta johtuen.

        print("Starting training")

        #print(f"{self.weights = }")

        step = 0
        while step < steps:
            i = random.randint(0, 4999)
            y = self.data[i]['char']
            x = self.data[i]['vector']
            # print(f"{y = }")

            if y != target_char and y != opposite_char:
                # print(
                #    f"mismatch {y} != {target_char} and {opposite_char} is {y != target_char and y!=opposite_char}")
                continue

            z = 0
            for j in range(NUMBER_OF_PIXELS):
                z += self.weights[j] * x[j]
            if z >= 0 and y == opposite_char:
                self.weights = [self.weights[j] - x[j]
                                for j in range(NUMBER_OF_PIXELS)]
            if z < 0 and y == target_char:
                self.weights = [self.weights[j] + x[j]
                                for j in range(NUMBER_OF_PIXELS)]
            step += 1
        # print(f"{self.weights}")

    def test(self, target_char, opposite_char):
        """Tests the learned perceptron with the last 1000 x,y pairs.
        (Note that this only counts those ones that belong either to the plus or minus classes.)

        :param target_char: the target character we are trying to distinguish
        :param opposite_char: the opposite character
        :return: the ratio of correctly classified characters
        """
        success = 0
        examples = self.data[5000:]

        examples = [e for e in examples if e['char']
                    in (target_char, opposite_char)]

        for e in examples:
            z = np.dot(e['vector'], self.weights)
            if (z >= 0 and e['char'] == target_char) or (z < 0 and e['char'] == opposite_char):
                success += 1

        return float(success) / len(examples)

    def save_weights(self, filename):
        """Draws a 28x28 grayscale picture of the weights

        :param filename: Name of the file where weights will be saved
        """
        pixels = [.01 + .98 / (1.0 + float(math.exp(-w)))
                  for w in self.weights]

        Image.fromarray(np.array(pixels).reshape(
            IMAGE_SIZE, IMAGE_SIZE), mode="L").save(filename)
