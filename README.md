# **AirBnB Clone - The Console**

## **Project Description**

This project is the beginning of building the AirBnB Clone. It focuses on the concepts of data models and data persistence. Data models are how users interact with real-world objects that are represented in the computer's memory. Data persistence is the idea that any changes we make to the objects are permanently saved and persist indefinitely. An example might be an AirBnB host that wants to change their nightly rate. Without data persistence, that change would occur, but there would be no record that it happened. And thus, the user would still see the same nightly rate. The goal of this project is to architect both the infrastructure to store objects in file storage, and also the command line interface through which we will manipulate the objects in file storage. Enter the console.

## **Console Description**

The console is a simple command line interpreter, built specifically to interact with the data models in file storage for the AirBnB Clone. This interaction can occur either internally or externally (interactive mode vs. non-interactive mode). File storage occurs in `file.json`. On startup, an instance of the `FileStorage` class is created. Then, the data models in file storage, if any exist, are loaded from a JSON string into their object representations and stored on the `FileStorage` instance created at startup. The user is then able to issue a command from the command list:

`help, quit, create, show, destroy, all, update`

for the console to execute. The console runs the command, manipulates the object specified in the command, serializes all of the objects in the `FileStorage` instance, if any exist, to JSON format, and then saves the data changes to file storage in the form of a JSON string. The console then prompts the user for more input. This is the default behavior and is repeated indefinitely until the console is terminated.

The console can be run in both interactive mode and non-interactive mode. Interactive mode indicates that the console is connected to the `STDIN` and prints the prompt `(hbnb) ` accordingly. If run in non-interactive mode, no prompt will be printed. Also, the command and arguments must be piped into the console at the command line of the user's shell.

## **Starting the Console**

Starting the console is easy! Just type:

`./console.py` - if the program file is in the current working directory.\

This command will start the console and begin interpreting commands. You'll know the console has launched when you see the prompt:

`(hbnb) `

Now that you've launched the console, let's explore how to use it!

## **Using the Console**

It would be a shame to let the incredible power of the console go to waste! It's deceptively easy to use. Do note the syntax will vary slightly depending on whether you're running the console in interactive mode or non-interactive mode. In non-interactive mode, you must pipe the commands into the `./console.py` file.

`(hbnb) create BaseModel` - interactive mode\
`echo "create BaseModel" | ./console.py` - non-interactive mode\

## **Examples**

Here is a sample session showing all the available functions:
