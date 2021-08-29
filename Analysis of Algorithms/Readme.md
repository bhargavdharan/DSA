# Analysis of Algorithm

## Asymptotic Analysis

**why performance Analysis?**

--- *There are many important things that should be taken care of , like user friendliness,modularity,security,maintainability etc.,*

**why to worry about performance?**

--- *1.we can have all the above things only if we have performance*

--- *2.performance is like currency through which we can buy all the above things*

--- *3.main reason we want performance to speed up the code*

**Given two algorithms for a task,how do we find out which one is better?**

#### -- *one naive way of doing this is - implement both algorithms and run the two programs on your computer for different inputs and see which one takes less time*

#### -- *They are many problems with this approach for analysis of algorithms*

#### --------- *it might be possible that for some inputs,first algorithm performs better than second.And for some inputs second performs better*
#### --------- *it might also be possible for some inputs,first algorithm perform better on one machine and the second works better on other machine for some other inputs*

### **NOTE:** -- Asymptotic analysis is the big idea that handles above issues in analyzing algorithms.

### In Asymptotic Analysis,
###           --- we evaluate the performance of an algorithm in terms of input size(we don't measure actual running time)
###           --- we calculate, how the time or space taken by algorithm increases with the input size.

## we have three cases to analyze an algorithm
### * The worst case
### * Average case
### * Best case

## Worst case Analysis

### -- In the worst case analysis, we calculate upper bound on running time of algorithm
### -- We must know the case that causes maximum no.of operations to be executed.
### -- For linear search, the worst case happens when the element to be searched is not present in the array.when x is not present,the search() functions compares it with all the elements of arr[] one by one.
### -- therefore, the worst case time complexity of linear search would be 0(n)

## Average case Analysis

### -- In average case analysis, we take all possible inputs and calculate computing time for all the inputs.
### -- sum of all the calculated values and divide the sum by total number of inputs.
### -- we must know distribution of cases
### --In linear search problem, let us assume that all the cases are uniformly distributed.so we sum all the cases and divide the sum by (n+1)

`
(n+1)E(n=1) O(n) / n+1
`

## Best case Analysis












