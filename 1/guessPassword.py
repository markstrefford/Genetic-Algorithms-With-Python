"""
Guess a password using a genetic algorithm

From chapter 1 of Genetic Algorithms with Python by Clinton Shephard

"""

import datetime
import genetic


def test_Hello_World():
    target = "Hello World!"
    guess_password(target)


def guess_password(target):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)

    def fnDisplay(genes):
        display(genes, target, startTime)

    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneSet, fnDisplay)



def display(genes, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    print('{}\t{}\t{}'.format(genes, fitness, timeDiff))


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)


if __name__ == '__main__':
    test_Hello_World()











