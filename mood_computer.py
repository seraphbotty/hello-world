# Mood Computer
# Demonstrates the if/elif clause and
# random function

from random import *

print("I sense your energy. Your true emotions are coming accross my screen.")
print("You are ...\n")

mood = randint(1, 3) # A random integer between 1 and 3
                        # will be generated by the computer
                        # and assigned to mood.


if mood == 1:
    #happy
    print(\
        """
           -------------
           |           |
           |  O    O   |
           |    <      |
           | .       . |
           |  .     .  |
           |    . .    |
           -------------
                       """)
elif mood == 2:
    # neutral
    print(\
        """
           -------------
           |           |
           |  O    O   |
           |    <      |
           |           |
           |  ______   |
           |           |
           -------------
                       """)
else:
    #sad
    print(\
        """
           -------------
           |           |
           |  O    O   |
           |    <      |
           |    .      |
           |  .   .    |
           | .     .   |
           -------------
                       """)

input("\n\nPress ENTER to exit")
