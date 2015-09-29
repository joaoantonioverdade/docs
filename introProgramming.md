## Programming foundation


# Programming paradigms

* Imperative: describes computation in terms of statements that change a program state. In much the same way that the imperative mood in natural languages expresses commands to take action, imperative programs define sequences of commands for the computer to perform (Java, C, Python).

* Declarative: a style of building the structure and elements of computer programs, that expresses the logic of a computation without describing its control flow. Many languages applying this style attempt to minimize or eliminate side effects by describing what the program should accomplish in terms of the problem domain, rather than describing how to go about accomplishing it as a sequence of the programming language primitives; the how is left up to the language's implementation, (Prolog, HTML, SQL).

* Functional: a style of building the structure and elements of computer programs, that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. It is a declarative programming paradigm, which means programming is done with expressions (Java, Python).

* Logic: a set of sentences in logical form, expressing facts and rules about some problem domain, (Prolog).

* Procedural: derived from structured programming, based upon the concept of the procedure call. Procedures, also known as routines, subroutines, methods, or functions (not to be confused with mathematical functions, but similar to those used in functional programming), simply contain a series of computational steps to be carried out. Any given procedure might be called at any point during a program's execution, including by other procedures or itself. Procedural programming is a list or set of instructions telling a computer what to do step by step and how to perform from the first code to the second code, (C, Python, PHP).

* Object-Oriented:  based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods. A distinguishing feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated (objects have a notion of "this"). In object-oriented programming, computer programs are designed by making them out of objects that interact with one another. There is significant diversity in object-oriented programming, but most popular languages are class-based, meaning that objects are instances of classes, which typically also determines their type, (Java, C++, Python).

-

# General concepts


In a *statically typed language*, every variable name is bound both to a type (at compile time, by means of a data declaration) or to an object (strongly typed language).

In a *dynamically typed language*, every variable name is (unless it is null) bound only to an object. (employeeName = 9; employeeName = "Steve Ferg")

*Object-oriented programming* (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods.

*Object* is a unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.

*Class* is a user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

*Inheritance* is the transfer of the characteristics of a class to other classes that are derived from it.

*Instance* is an individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

*Method* is a special kind of function that is defined in a class definition.

*Function overloading* is the assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.

*Operator overloading* is the assignment of more than one function to a particular operator.

*Polymorphism* is the ability (in programming) to present the same interface for differing underlying forms (data types).

*Reflection* is the ability of a computer program to examine (see type introspection) and modify its own structure and behavior (specifically the values, meta-data, properties and functions) at runtime.

The difference between a function and a procedure is due to the returning value of the function. A procedure is a set of command which can be executed in order. 
A method differs from a function for its capacity to interact with the class data members.

TODO:

Dynamic programming
Memoization
Currying
Closures
Reflection
Decorators