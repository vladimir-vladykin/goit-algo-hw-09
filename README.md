# goit-algo-hw-09
Algo homework 09

## Greedy and dynamic algorithms for coins withdraw solution
1. coins_algo.py -> contains implementation of both algorithms, and code for test performance

## Results of test runs
    Testing amount 20...
    Greedy algorithm spent 0.00000333 for calculation, result is:
    {50: 0, 25: 0, 10: 2, 5: 0, 2: 0, 1: 0}
    Dynamic algorithm spent 0.00001163 for calculation, result is:
    {50: 0, 25: 0, 10: 2, 5: 0, 2: 0, 1: 0}


    Testing amount 113...
    Greedy algorithm spent 0.00000183 for calculation, result is:
    {50: 2, 25: 0, 10: 1, 5: 0, 2: 1, 1: 1}
    Dynamic algorithm spent 0.00003792 for calculation, result is:
    {50: 2, 25: 0, 10: 1, 5: 0, 2: 1, 1: 1}


    Testing amount 60000...
    Greedy algorithm spent 0.00012804 for calculation, result is:
    {50: 1200, 25: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    Dynamic algorithm spent 0.02235500 for calculation, result is:
    {50: 1200, 25: 0, 10: 0, 5: 0, 2: 0, 1: 0}


    Testing amount 60131...
    Greedy algorithm spent 0.00009850 for calculation, result is:
    {50: 1202, 25: 1, 10: 0, 5: 1, 2: 0, 1: 1}
    Dynamic algorithm spent 0.01848221 for calculation, result is:
    {50: 1202, 25: 1, 10: 0, 5: 1, 2: 0, 1: 1}

Answers usually the same from both algorithms (at least for this combination of amounts and possible coins). 
Speed is good for both, but greedy approach is faster, and it might be improved even more via small optimizations in code.
Dynamic approach might be better for finding best solution possible, but it's irrelevent on set of coins we have by task, which is [50, 25, 10, 5, 2, 1].
For another coins set dynamic approach would be better, because greedy might give not best result (for instance in case of coin=6).

So usually greedy approach is preferred for task like that, it provides better performance while gives good result, especially when you can be sure set of coins is not gonna change anytime soon (for instance creating solution for single country).
But dynamic approach might be better if you need to build more general implementation, which should work for world-wide, with dynamic set of coins, and you value precise result more than fast result.