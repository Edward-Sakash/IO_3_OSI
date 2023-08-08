"""

To avoid manipulating the file system outside of our working folder
you will define the constants ROOT and DATA_ROOT.

These constants will be used throughout the rest of the exercise.

Define a constant, named ROOT that points to the full path of your
current script.

Now, define another constant, named DATA_ROOT that defines the
full path of the initial directory, based on the ROOT.

In pseudocode:

ROOT = detect the current path of the script
DATA_ROOT = ROOT + src/data/initial
You are not allowed to type in the paths. The script should produce
the correct answer if you clone this repository in a different
location of your file system.

You are not allowed to concatenate strings or use string formatting.
Only the methods from the os and os.path modules are allowed.

Once defined, print them on the console. Your output should look
similar to this(*):
/home/DCI/PythonCourse/Python-basics-io-os
/home/DCI/PythonCourse/Python-basics-io-os/src/data/initial
(*) The exact path will depend on where you cloned this repository
and the type of Operating System used.

"""

# Solution

import os

# Define the ROOT constant pointing to the current script's path
ROOT = os.path.abspath(os.path.dirname(__file__))

# Define the DATA_ROOT constant based on the ROOT constant
DATA_ROOT = os.path.join(ROOT, 'src', 'data', 'initial')

# Print the constants
print(ROOT)
print(DATA_ROOT)
