# Dealectable - CutieHack2018
Project for CutieHack 2018 at the University of California, Riverside. 

Inspiration

Dealectable was inspired by a simple need for finding a good place for lunch. Currently, there are no streamlined platforms for finding food to eat when there are multiple options around. Most platforms involve going through multiple web pages or apps before the user finds the menu.

What it does

The application uses images of different restaurant menus and uses ComputerVision in Python in order to convert that information into a data file that can be readable by programs. The data is then exported to a Google Firebase Database to be stored and accessed remotely. That subsequently is accessed by AndroidStudio to allow an Android application to access that information.

How we built it

We used ComputerVision to create an Optical Character Recognition program that converted the images to a saved output from Terminal. That output is saved Pyrebase to a Google Firebase database to then be accessed by Android Studio that returns information to the users.

Challenges we ran into

Pyrebase was a big challenge for us because it was difficult synchronizing our data from Python files and Terminal outputs to an external database, that could be accessed by Android Studio.

Accomplishments that we're proud of

We're proud in the way we stored our data that was outputted to us from Terminal and how we used that data to be stored externally.


