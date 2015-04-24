## Theory of computation to revive my university days knowledge 

Resume of Sipser - Introduction to the theory of computation

-

There are three traditionally central areas of the theory of computation: 

* **automata**, deals with the definitions and properties of mathematical models of computation.
* **computability**, certain basic problems cannot be solved by computers. As for example the determination of a mathematical statement has true or false. The theory objective is to classify problems as solvable or not.
* **complexity**, *What makes some problems computationally hard and others easy?* we don't know the answer to it, but researchers have discovered an elegant scheme for classifying problems according to their computational difficulty.

-


### Chapter 1 - Regular Languages

A computational model is a idealized computer, accurate in some ways but not in others.

The simplest model is the **finite state machine** or **finite automata**

A finite automata is a model with finite states and inputs. For example a automatic door with two states: open and closed, with two inputs (some pads in the rear and front of the door) that reflect four possible inputs: front, read, both, none. Depending on the input the model jumps from one state to another: 


![State diagram](https://raw.githubusercontent.com/joaoantonioverdade/docs/master/resources/State_diagram_for_automatic_door.png)


The probabilistic counterpart are the **markov chains**.


