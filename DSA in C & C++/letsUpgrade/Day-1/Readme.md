# Fundamentals of Time Complexity

## Measure of an algorithm

## What is an algorithm ?

* An Algorithm is a **finite** set of instructions that are carried in a specific order to perform specific task.

* Algorithms typically have following characteristics:

1.inputs
2.outputs
3.Unambiguity  -- clear and simple instructions
4.Finiteness   -- limited number of instructions
5.Effectiveness -- each instructions has an impact an impact on the overall process

* **Example of an algorithm in programming**.

## what is Algorithm Analysis?

* Algorithm analysis is a study to provide theoretical estimations for the required resources of an algorithm to solve a specific computational problem i.e, calculating efficiency.

* Generally, the efficiency of an algorithm is related to the input length(number of steps), known as time complexity or volume of memory, known as space complexity.

* What is the need of Analysis ?

* --> Generally, there are multiple approaches given to a problem statement.

## what does a BETTER Algorithm mean ?

* Faster ? (less execution time)

* Less memory ? Space Complexity --

* Easy to read ?

* Less lines of code ?

* Less HW / SW needs ?

## Time Complexity of an algorithm - example

* rate of growth ==> At what rate the complexity increase when number of inputs 'n' increases.

* consider a problem statement: Find the sum of "n" numbers

```Linear behaviour``

```Algorithm1
int sum = 0;
for(int i=1;i<=n;i++){
    sum = sum + i;
}
```

```constant behaviour```

```Algorithm2

int sum = n * (n+1) / 2;
```

## Space Complexity of an algorithm - example

* For any algorithm, memory is required for the following purposes:

1. To store program instructions
2. To store constant values
3. To store local variable values
4. And few other instructions address during function calls, jumping statements, etc.,...

* Space Complexity = input space + Auxiliary Space.

* Auxiliary Space ==>

* Consider a function which computes factorial of a number

```constant space```

```Algorithm1

int fact = 1;
for(int i=1;i<=n;i++){
    fact = fact * i;
}
```

```linear space```

```Algorithm2

void fact(int n)
{
    if(n<=1){
        return 1;
    }
    else{
        return (n*fact(n-1));
    }
}
```

* **Auxiliary space keeps increasing with every recursive call of value n and because of input size**

## What is Asymptotic Algorithm Analysis ?

* A method of defining the mathematical boundaries of its run-time performance.Mathematically calculate the running time of any operation inside an algorithm

* Using asymptotic analysis, we can easily estimate about the average case, best case and worst-case scenario of an algorithm

* big oh

* big omega

*

* How to find the Big O notation ?

1. Find the fastest growing variable term

2. Eliminate the co-efficients/constant terms

* Following is a list of some common asymptotic notations:

1. Constant time - O(1)

2. Logarithmic complexity - O(log n)

3. Linear complexity - O(n)

4. Logarithmic linear - O(n log n)

5. Quadratic - O(n^2)

6. Cubic - O(n^3)

7. Exponential - O(2^n)

**Note:** 1 < log(n) < sqrt(n) <......

## Find the time complexities of the below code snippet

* ```for(int i=0; i<n; i++) {cout <<"Hello <<endl;}```

* --- 0(n)

* ```for(int i=n; i>0; i--) { cout<<"Hello"<<endl;}```

* --- O(n)
