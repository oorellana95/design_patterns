# Abstract Factory Method

This pattern is best suited when one wishes to create multiple categories of an object by abstracting its implementation. Use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.

You may be familiar with the concept factories - these are objects that create other objects. The Abstract Factory Pattern is primarily concerned with the interface for factory objects.

![Screenshot 2023-07-30 at 17.30.18.png](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fjl%2Fb5bwl2qd3817hty9bd0jn1b00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_TBL0Cg%2FScreenshot%202023-07-30%20at%2017.30.18.png)

Assume that you are designing a family of two products (a browser and a messenger).

**Abstract Products**: Two abstract classes are created, one for the browser and another for the messenger. These classes contain abstract methods that are mandatory for the construction of the products. These abstract classes are referred to as interfaces.

In the example shown above, the Web Browser and Messenger are the abstract products.

**Concrete Products**: Concrete products inherit the abstract methods from the abstract classes i.e. abstract products. Using the interfaces, different families of products can be created.

For example, in the diagram above, three different kinds of web browsers are created for three different sets of users. If there's one thing that all these concrete products have in common, that would be the abstract methods that were defined in the abstract class.

**Concrete Factories**: Concrete Factories create Concrete Products as directed by the Abstract Factories. The concrete factories are only capable of creating those products that are specified in them - a BrowserFactory creates browsers, while a MessengerFactory creates messengers. Alternatively, you can focus on some common features, and say - create a BasicFactory and SecureFactory which create basic or secure web browsers and messenger instances.

In the diagram mentioned above, the Vanilla Products Factory is capable of creating both vanilla concrete products (browser and messenger), while the Secure Products Factory makes safe versions.

**Abstract Factories**: The Abstract factories possess interfaces to create the abstract products i.e. they contain several methods that return abstract products.

In the example, the interfaces of concrete factories are invoked to get the abstract products as a web browser and messenger.