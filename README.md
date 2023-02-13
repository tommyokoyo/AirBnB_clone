# AirBnB_clone
![image](https://user-images.githubusercontent.com/39227748/218501765-1862a654-09dc-4d14-9d93-e22e00fcabfc.png)
The goal of the project is to deploy on my server a simple copy of the AirBnB website.

The web application will be composed of:

  - A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
  - A website (the front-end) that shows the final product to everybody: static and dynamic
  - A database or files that store data (data = objects)
  - An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


**Final product**
![image](https://user-images.githubusercontent.com/39227748/218503104-a586d3ae-f5ce-45d6-a53f-738b9def7d50.png)

![image](https://user-images.githubusercontent.com/39227748/218503156-0cbfd882-deaa-43a2-893d-c924dd24de49.png)

**The console**
  - create my data model
  - manage (create, update, destroy, etc) objects via a console / command interpreter
  - store and persist objects to a file (JSON file)

This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from my console code (the command interpreter itself) and from the front-end and RestAPI I will build later, I won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

![image](https://user-images.githubusercontent.com/39227748/218504190-7231c2a5-48cc-4a5b-89b1-cdf0394b2eff.png)
