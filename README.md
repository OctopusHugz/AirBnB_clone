# **AirBnB Clone - The Console**

## **Project Description**

This project is the beginning of building the AirBnB Clone. It focuses on the concepts of data models and data persistence. Data models are how users interact with real-world objects that are represented in the computer's memory. Data persistence is the idea that any changes we make to the objects are permanently saved and persist indefinitely. An example might be an AirBnB host that wants to change their nightly rate. Without data persistence, that change would occur, but there would be no record that it happened. And thus, the user would still see the same nightly rate. The goal of this project is to architect both the infrastructure to store objects in file storage, and also the command line interface through which we will manipulate the objects in file storage. Enter the console.

---
## **Console Description**

The console is a simple command line interpreter, built specifically to interact with the data models in file storage for the AirBnB Clone. This interaction can occur either internally or externally (interactive mode vs. non-interactive mode). File storage occurs in `file.json`. On startup, an instance of the `FileStorage` class is created. Then, the data models in file storage, if any exist, are loaded from a JSON string into their object representations and stored in the `FileStorage` instance created at startup. The user is then able to issue a command from the command list:

`help, quit, create, show, destroy, all, update, count`

for the console to execute. The console runs the command, manipulates the object specified in the command, serializes all of the objects in the `FileStorage` instance, if any exist, to JSON format, and then saves the data changes to file storage in the form of a JSON string. The objects can be instances of any of the following classes:

`BaseModel, User, Place, State, City, Amenity, Review`

The console then prompts the user for more input. This is the default behavior and is repeated indefinitely until the console is terminated.

The console can be run in both interactive mode and non-interactive mode. Interactive mode indicates that the console is connected to the `STDIN` and prints the prompt `(hbnb) ` accordingly. If run in non-interactive mode, no prompt will be printed. Also, the command and arguments must be piped into the console at the command line of the user's shell.

---
## **Starting the Console**

Starting the console is easy! Just type:

`./console.py` - if the program file is in the current working directory.

This command will start the console and begin interpreting commands. You'll know the console has launched when you see the prompt:

`(hbnb) `

Now that you've launched the console, let's explore how to use it!

---
## **Using the Console**

It would be a shame to let the incredible power of the console go to waste! It's deceptively easy to use. Please note the syntax will vary slightly depending on whether you're running the console in interactive mode or non-interactive mode. Also, in interactive mode, you have the choice between space syntax and method syntax. Also note, the `count` function is only available using method syntax. In non-interactive mode, you must pipe the commands into the `./console.py` file.

### Space Syntax

`command class id`

### Method Syntax

`class.command("id")`

The `update` command has special powers. It has 2 different ways to update the instance by either selecting a specific attribute to update, or by updating from a dictionary:

#### Specific Attribute

`class.update("id", attribute, value)`

#### From Dictionary

`class.update("id", {key: value, key:value})`

### Interactive Mode

`(hbnb) create BaseModel` - interactive mode<br>
`(hbnb) show BaseModel 64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce` - interactive mode using space syntax<br>
`(hbnb) BaseModel.show("64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce")` - interactive mode using method syntax

### Non-Interactive Mode

`echo "create BaseModel" | ./console.py` - non-interactive mode<br>
`echo "show BaseModel 64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce" | ./console.py` - non-interactive mode using space syntax<br>
`echo "BaseModel.show(\"64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce\")" | ./console.py` - non- interactive mode using method syntax

### Exiting the Console

You can exit the console in multiple ways:

`CTRL-D` to signal `EOF`<br>
`quit` command

---
## **Example**

Below is a sample session showing all the functions available in the console. If you copy the commands in the example, you can track the changes to your objects in real-time by observing the `file.json`:

	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  all  create  destroy  help  quit  show  update

	(hbnb) help all
	All command to print the string representation of all instances in
	storage, based on the class name if given. If not, print the
	string representation of all instances in storage

	(hbnb) all
	[]
	(hbnb) create BaseModel
	64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce
	(hbnb) show BaseModel 64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce
	[BaseModel] (64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce) {'id': '64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce', 'updated_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684304), 'created_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684237)}
	(hbnb) BaseModel.show("64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce")
	[BaseModel] (64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce) {'id': '64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce', 'updated_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684304), 'created_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684237)}
	(hbnb) create User
	8e8b40ef-c1be-4493-8e43-1c3139c7c5f3
	(hbnb) show User 8e8b40ef-c1be-4493-8e43-1c3139c7c5f3
	[User] (8e8b40ef-c1be-4493-8e43-1c3139c7c5f3) {'id': '8e8b40ef-c1be-4493-8e43-1c3139c7c5f3', 'updated_at': datetime.datetime(2020, 7, 1, 23, 59, 8, 3382), 'created_at': datetime.datetime(2020, 7, 1, 23, 59, 8, 3340)}
	(hbnb) all
	["[BaseModel] (64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce) {'id': '64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce', 'updated_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684304), 'created_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684237)}", "[User] (8e8b40ef-c1be-4493-8e43-1c3139c7c5f3) {'id': '8e8b40ef-c1be-4493-8e43-1c3139c7c5f3', 'updated_at': datetime.datetime(2020, 7, 1, 23, 59, 8, 3382), 'created_at': datetime.datetime(2020, 7, 1, 23, 59, 8, 3340)}"]
	(hbnb) all BaseModel
	["[BaseModel] (64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce) {'id': '64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce', 'updated_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684304), 'created_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684237)}"]
	(hbnb) BaseModel.count()
	1
	(hbnb) User.all()
	["[User] (8e8b40ef-c1be-4493-8e43-1c3139c7c5f3) {'id': '8e8b40ef-c1be-4493-8e43-1c3139c7c5f3', 'updated_at': datetime.datetime(2020, 7, 1, 23, 59, 8, 3382), 'created_at': datetime.datetime(2020, 7, 1, 23, 59, 8, 3340)}"]
	(hbnb) User.count()
	1
	(hbnb) create User
	48af6bdf-db51-4d95-8a73-ab007401f4d0
	(hbnb) all User
	["[User] (8e8b40ef-c1be-4493-8e43-1c3139c7c5f3) {'id': '8e8b40ef-c1be-4493-8e43-1c3139c7c5f3', 'updated_at': datetime.datetime(2020, 7, 1, 23, 59, 8, 3382), 'created_at': datetime.datetime(2020, 7, 1, 23, 59, 8, 3340)}", "[User] (48af6bdf-db51-4d95-8a73-ab007401f4d0) {'id': '48af6bdf-db51-4d95-8a73-ab007401f4d0', 'updated_at': datetime.datetime(2020, 7, 2, 0, 6, 23, 898204), 'created_at': datetime.datetime(2020, 7, 2, 0, 6, 23, 898178)}"]
	(hbnb) User.count()
	2
	(hbnb) destroy User 8e8b40ef-c1be-4493-8e43-1c3139c7c5f3
	(hbnb) show User 8e8b40ef-c1be-4493-8e43-1c3139c7c5f3
	** no instance found **
	(hbnb) User.all()
	["[User] (48af6bdf-db51-4d95-8a73-ab007401f4d0) {'id': '48af6bdf-db51-4d95-8a73-ab007401f4d0', 'updated_at': datetime.datetime(2020, 7, 2, 0, 6, 23, 898204), 'created_at': datetime.datetime(2020, 7, 2, 0, 6, 23, 898178)}"]
	(hbnb) update User 48af6bdf-db51-4d95-8a73-ab007401f4d0 first_name "Monty"
	[User] (48af6bdf-db51-4d95-8a73-ab007401f4d0) {'updated_at': datetime.datetime(2020, 7, 2, 0, 11, 33, 25782), 'first_name': 'Monty', 'created_at': datetime.datetime(2020, 7, 2, 0, 6, 23, 898178), 'id': '48af6bdf-db51-4d95-8a73-ab007401f4d0'}
	(hbnb) User.update("48af6bdf-db51-4d95-8a73-ab007401f4d0", "last_name", "Python")
	[User] (48af6bdf-db51-4d95-8a73-ab007401f4d0) {'updated_at': datetime.datetime(2020, 7, 2, 0, 36, 25, 197321), 'last_name': 'Python', 'first_name': 'Monty', 'created_at': datetime.datetime(2020, 7, 2, 0, 6, 23, 898178), 'id': '48af6bdf-db51-4d95-8a73-ab007401f4d0'}
	(hbnb) User.update("48af6bdf-db51-4d95-8a73-ab007401f4d0", {'pet': 'snake', 'age': 42})
	(hbnb) User.show("48af6bdf-db51-4d95-8a73-ab007401f4d0")
	[User] (48af6bdf-db51-4d95-8a73-ab007401f4d0) {'first_name': 'Monty', 'age': 42, 'pet': 'snake', 'id': '48af6bdf-db51-4d95-8a73-ab007401f4d0', 'updated_at': datetime.datetime(2020, 7, 2, 0, 36, 25, 197321), 'last_name': 'Python', 'created_at': datetime.datetime(2020, 7, 2, 0, 6, 23, 898178)}
	(hbnb) all
	["[BaseModel] (64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce) {'updated_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684304), 'id': '64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce', 'created_at': datetime.datetime(2020, 7, 1, 23, 34, 41, 684237)}", "[User] (48af6bdf-db51-4d95-8a73-ab007401f4d0) {'first_name': 'Monty', 'age': 42, 'pet': 'snake', 'id': '48af6bdf-db51-4d95-8a73-ab007401f4d0', 'updated_at': datetime.datetime(2020, 7, 2, 0, 36, 25, 197321), 'last_name': 'Python', 'created_at': datetime.datetime(2020, 7, 2, 0, 6, 23, 898178)}"]
	(hbnb) destroy BaseModel 64dfa5b0-33e8-4aa0-8bd7-b622e1ae04ce
	(hbnb) destroy User 48af6bdf-db51-4d95-8a73-ab007401f4d0
	(hbnb) all
	[]
	(hbnb) quit
	octopushugs:~/AirBnB_clone$
