# Python principles


Multi-paradigm: object-oriented, imperative, functional, procedural, structured and reflective.

Cross-platform, minimalist, readability

## Typing

Typing discipline: duck, dynamic, strong, gradual.

**Duck** typing is concerned with assigning a type to any object. Duck typing is concerned with establishing the suitability of an object for some purpose. With normal typing, suitability is assumed to be determined by an object's type only. In duck typing, an object's suitability is determined by the presence of certain methods and properties (with appropriate meaning), rather than the actual type of the object.

```
try:
    dog.quack()
except AttributeError:
    dog.woof()
```

**Strong** typing means every variable name is (unless it is null) bound only to an object and never convert implicitly. The contrasting weak typing, bounds every variable to a type and an object.

**Dynamic** typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type.

```
a = 0
b = "zero"
c = concatenate(str(a), b)
d = add(a, int(b))
```

**Gradual** is a type system in which variables may be typed either at compile-time (which is static typing) or at run-time (which is dynamic typing).

```
def say_hello(name : str = "Anon") -> None: # <- return value annotation
    #              ^^^^^   ^
    #              |       `- default value
    #              `- parameter annotation
    print("Hello, {}".format(name))
```

Suport of functional programming with map(), reduce(), filter(), comprehensions for lists, dictionaries, sets, generator expressions.