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

(![image](https://github.com/user-attachments/assets/8b1cca88-0e7a-4948-846a-2c352f0d8179)
