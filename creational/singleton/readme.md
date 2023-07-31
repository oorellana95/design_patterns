Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

## Implementation 
For a class to behave as a Singleton, it should **not contain any references to self** but **use static variables, static methods and/or class methods.**

Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.

Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.

## Examples of use
- Logging
- Database connection
- Game with a score

