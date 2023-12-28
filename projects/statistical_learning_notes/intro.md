# Introduction

Machine Learning problems are generally framed into problems of minimizing some kind of **Loss Function**.
Intuitively, Loss Functions are functions that measure how well some model is performing in the available data of the problem at hand. Models with lower Losses are preferred. 

A natural and important question that arises is precisely which Loss Function to choose for some given problem. There is a extensive list of available Loss Functions to choose from (and you can always invent new ones) and although some choices might be obvious or straightforward for some problems (you might usually not even think about it and just choose the default ones from your library at hand), it might not always be the case. If you find yourself in the latter case, it might be useful to look at the problem from some a "first principles" angle to help understand how to choose it more wisely.

The goal here is to briefly discuss how Loss Functions in ML problems arise naturally from a Bayesian perspective. 
We'll focus on **supervised learning** problems.



```{tableofcontents}
```
