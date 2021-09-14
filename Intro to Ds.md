# Real time Example

## *when you building a home you need certain building blocks and raw-materials such as bricks,wooden-plank,metal-rods and top of that we have to apply instructions to build home and you get home as a result*

## How to build software applications?

### *similarly, when u building software applications, u need raw building blocks which are basically data structures such as arrays,linked-list,etc., on top of that we have apply code instructions which operates on DS and as a result we get software applications*

## Data Structures

* *Data structure is a storage that is used to store and organize data. it is a way of arranging data on a computer so that can be accessed and updated efficiently.*

* *Data structures are building blocks or raw material for any software programs*

* *Data structures are containers storing data in a specific memory layout*

## Types of Data structure

Basically, data structures are divided into two categories.

* PRIMITIVE Data structures

1. Primitive data types are the data types available in most programming languages.

2. These data types are used to represent single values.

3. it is a basic data type available in most programming languages

* NON-PRIMITIVE Data structures

1. Data structures derived from primitive data types are known as Non-Primitive data types.

2. It can be divided into two data types

* **Linear Data structure**.

* **Non-Linear Data structure**

## Linear Data structure

* In linear data structures, the elements can be arranged in sequence one after the other

* Since elements are arranged in particular order, they are easy to implement.

* Whenever the complexity of the program increases, the linear data structures might not be the best choice because of operational complexities.

Popular linear data structures are:

1. Array Data structure

2. Stack Data structure

3. Linkedlist Data structure

4. Queue Data structure

## Non-linear Data Structure

* unlike linear data structures, elements in non-linear data structures are not in any sequence.

* Instead they are arranged in a hierarchical manner where one element will be connected to one or another

* Non-linear data structures are further divided into graph and tree based data structures.

1. Graph Data Structure

        * In graph data structure, each node is called vertex and each vertex is connected to other vertices through edges.

    Popular graph based data structures:

    1. Spanning Tree and Minimum spanning tree
    2. Strongly Connected components
    3. Adjacency Matrix
    4. Adjacency List

2. Tree Data Structure

        * Similar to graph, a tree is a collection of vertices and edges. However, in tree data structure, there can only be one edge between two vertices.

    Popular tree based data structures:

    1. Binary Tree
    2. Binary Search Tree
    3. AVL Tree
    4. B-Tree
    5. B+ Tree
    6. Red-Black Tree


## Table of DS in diff langs:

| `DataStructure`     | `Python`          | `java`                | `c++`     |
|---------------------|:-----------------:|:---------------------:|--------:|
| **Array**           |   List            |NativeArray,arrayList  | NativeArray,std::vector
| **Hash Table**      |   dictionary      |HashMap,Linked H.M     | std::map
| **Linked List**     |   not available   |LinkedList             | std::list

## In python Data structures is defined in two ways

1. Built-in DS(list,tuple,set,Dictionary)

2. user defined DS(stack,queue,linked list,tree,graph)

## What is an Algorithm ?

* An algorithm is a set of well-designed, step-by-step instructions designed to solve a problem or perform a specific task.

### Categories of algorithms

From the data structure point of view, the following are some important categories of algorithms

* Search --- Algorithm to search an item in a data structure.

* Sort   --- Algorithm to sort items in a certain order.

* Insert --- Algorithm to insert items in a data structure.

* Update --- Algorithm to update an existing item from a data structure.

* Delete --- Algorithm to delete an existing item from a data structure.

Not all procedures can be called an algorithm. an algorithm should have the following characteristics.

* Input         --- An algorithm has some input values. we can pass 0 or some input value of an algorithm.

* Output        --- We will get one or more output at the end of an algorithm.

* Unambiguity   --- An algorithm should be unambiguous which means that the instructions in an algorithm should be clear and simple.

* Finiteness    --- Algorithm must terminate after a finite number of steps.

* Effectiveness --- An algorithm should be effective with the available resources.

* Language independent  --- An algorithm must be language-independent so that the instructions in an algorithm can be implemented in any of the languages with the same output.

## The complexity of Algorithm : Time

How do you do "Measure" your code ? would you clock "How long" it takes to run ?

### Time Complexity

* The time complexity is not about how long the algorithm takes.Instead, how many operations are executed.The number of instructions executed by a program is affected by the input's size and how their elements are arranged

* Time complexity (or running time) is estimated time an algorithm takes to run. However, you do not measure time complexity in seconds, but as a function of the input.

* **Why is that the complexity is expressed as a function of the input?**

* We can say for each algorithm have the following times:

1. Worst-case time complexity

2. Best-case time complexity

3. Average-case time complexity

