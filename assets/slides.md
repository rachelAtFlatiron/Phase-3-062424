---

title: ""
output:
  theme: white

--- 

# OOP

---

## ✅ Objectives 

- Define Object Oriented Programming
- Review the benefits of OOP
- Review the principles of OOP
- Demonstrate classes, instances, _ _ init _ _, instance methods, the *self* keyword
- Demonstrate object properties

---

## Object Oriented Programming

- Programming that is oriented around *data* rather than *functionality*

- Based on the concept of *objects* containing *data* (attributes/properties) and *procedures* (functions/methods)

<aside class="notes">

- IT IS A PROGRAMMING PARADIGM - a way of approaching writing code
- Not all lagnuages are OOP (JS has features to mimic classes but is not inheritantly a OOP language)
- use python to mimic database 
- real life situation that we want to mock/model 
-  mimic complexities world through abstractions

</aside>


--- 

## Benefits of OOP

- Modularity and easier troubleshooting
- Inheritance and reusability of code
- Scalability and making it easier to build out

<aside class="notes">

- been doing things procedurality - doing things step by step
- functions are not methods 
- domain modeling - all different ways data point of application will be interacting (ORMs)

</aside>

---

## OOP Pillars

1. Inheritance
2. Abstraction
3. Encapsulation
4. Polymorphism

<aside class="notes">

- Inheritance, class inherits from other class.  JS has prototypes which is slightly different since JS isn't originally a class language
- Abstraction, modeling real world into abstract world
- ABC: Abstract Base Class - don't instantiate instances, you make subclasses
- Concrete classes - make instances of those classes
- Encapsulation - as a child of class I encapsulate properties/attributes/data and know how to do certain things (behavior/data is available - don't have to pass arguments) 
- allows access control protected (class and subclasses) /private (class only) /public (client can use it)
- in Python protected/privacy is a suggestion displayed with a writing convention, it is not real
- Building methods that can be invoked on different types of objects of different classes 
-  [1, 2, 3].__add_ _ ([4])
- [1, 2, 3] + [4]

</aside>