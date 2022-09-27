# Exercises for week 3


## Exercise 2

### Part1

| Word | Spam | Spamfaktor| Ham | Hamfaktor | OutOfAllWords(4) |
| --- | --- | --- | --- | --- | --- |
| million | 156 | 0.0016285 | 98 | 0.0003198 | 0.00063148
| dollars | 29  | 0.0003027 |119 | 0.0003883 | 0.00036795
| adclick | 51  | 0.0005324 | 0 | 0          | 0.00012679
| conferences | 0 | 0 | 12 | 0.0000391       | 0.00002983
| total | 95791 | | 306438 | 

402229 words in total


### Part2

1 - ('millions'spam + 'millions'ham) / total_words = 1 - (156+98) / 402229 = 0.9993685

### Part3 (väärin)

P(spam|'million')         P(spam)P('million'|spam)

-------------------------  = -------------------------------------

P(ham |'million')        P(ham)P('million'|ham)


= P('million'|spam) / P('million'|ham) = n. 5.1. 

Eli luultavasti spammia!

### Part4

P (spam | 'million', 'dollars', 'adclick', 'conferences')

= P(spam) P('million', 'dollars', 'adclick', 'conferences'|spam) / P('million', 'dollars', 'adclick', 'conferences')

= P(spam) * P('million'|spam) * P('dollars'|spam) * P('adclick'|spam) * P('conferences'|spam) / ( P('million') * P('dollars') * P('adclick') * P('conferences') )

= 0.5 * 0.0016285 * 0.0003027 * 0.0005324 * 0.000001 /
(0.00063148 * 0.00036795 * 0.00012679 * 0.00002983)
= noin 0.14932

R= 0.0016285/0.0003198*0.0003027/0.0003883*0.0005324/0.000001*0.000001/0.0000391 = 54.0524798