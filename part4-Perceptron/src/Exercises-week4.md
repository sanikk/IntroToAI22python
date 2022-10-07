# Exercises for week 4

## Exercise 1
### Bavarian newtorgs (pencil-and-paper) (1p)

In Part 3, we briefly discussed how Bayesian networks lead to compact representation of probabilistic models.

    Consider a model with N=4 variables, each of which has k possible values (0,1,...,k–1). How many different elementary events are there in the domain? One less is the number of probabilities that we'd have to determine in order to fully specify the model. (For example, in the Car model of Part 3, with N=6 and k=2, this number was 63.)

#### answer:
k^N - 1 so k⁴ - 1

    How many parameters would we have to define to specify the model using an "empty" Bayesian network, i.e, a network with no edges at all?

#### answer:
wut? Like, if we have 4 variables with independent values maybe 4?

    What is the maximum number of parameters we'd have to define in a Bayesian network in this domain (N variables with k values each)? Remember that the graph has to be a DAG, i.e., no directed cycles are allowed.
    Optional: Generalize to arbitrary values of N. It may be helpful to recall the sum of a geometric series 1+k+k2+...+kN–1 = (kN–1)/(k–1), where k≠1. 

## Exercise 2
### Bayesian networks: Car (programming) (1p)

Implement an algorithm for generating data from the Car network discussed in Part 3. You should generate n tuples, each of which is a six element list of bits (or Boolean values). You should start by choosing the value of B so that it takes value 1 (or True) with probability 0.9. After choosing the value of B, choose the value of R. If B=0, then R=0 with probability 1. If B=1, then R=0 with probability 0.1. Continue this way, choosing the probabilities from the CPTs, until you have generated a complete tuple.

Generate a sample of n=100 000 tuples. Use it to approximate the following conditional probabilities:

    P(B | R,G,¬S)

hel

    P(S | R,I,G)
hel

    P(S | ¬R,I,G) 
hel

and (don't forget this part):


    Give an interpretation to the above probabilities. Are they in line with your intuition? In other words, do they make sense? 

## Exercise 3