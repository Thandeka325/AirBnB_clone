# AirBnB clone
# Project: 0x00. AirBnB clone - The console

This is the beginning of the AirBnB clone project, the goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.co.za/?locale=en&_set_bev_on_new_domain=1731312276_EAYWIzMDVhMGE1OD)
The project will be divided into 6 steps: The console, Web static, MySQL storage, Web framework - templating, RESTful API, Web dynamic.

# The console:
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

![image](https://github.com/user-attachments/assets/8b1cca88-0e7a-4948-846a-2c352f0d8179)

# Background Context
# Welcome to the AirBnB clone project!

__First step: Write a command interpreter to manage your AirBnB objects.__
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine.

__What’s a command interpreter?__
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

# Resources
[cmd module](https://docs.python.org/3.8/library/cmd.html)  [cmd module in depth](https://pymotw.com/2/cmd/)  [packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
[uuid module](https://docs.python.org/3.8/library/uuid.html)  [datetime](https://docs.python.org/3.8/library/datetime.html)  [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
[args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)  [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)  [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
[python unittest](https://realpython.com/python-testing/)

# Execution
The shell(console) should work in an interactive and non-interactive mode.

## __Interactive mode__:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

## __Non-interactive mode__:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
```

