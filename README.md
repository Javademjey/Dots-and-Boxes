# Dots-and-Boxes
This is a Dot and Box game.

### Game description:
The goal in this game is to occupy a square, and this happens if four lines are placed in a square, and someone gets the points of the square that has inserted the last line.
The dot and box game is a two-player game. I designed the game so that your opponent is the system.
When you start the game, the first move is yours, then the game screen is shown, and when you pass the game screen, your opponent's system move is shown.
At the beginning of the game, you will be asked how many squares the board has and you enter the game.
It will then ask you to select a number from 1 to n (n = the number of squares you have entered) this number represents the number of the square you have selected and again it will ask you to
select a number from 1 to 4 and this indicates the line number that you insert in the desired square.
This process continues until all the squares are occupied, and when all the squares are occupied, the game ends and the one who occupies the most squares wins the game.

### Code description:
DeterminationOfPoints: 
The input of this function is the number of points (if we enter the number 4 in the input, it means
we have a game board with 16 points and 9 squares) and the output of this function gives us two lists, the first of which is
the coordinates of all x's and the second of the coordinates of all y.

UserSeparating_X_and_Y and SysSeparating_X_and_Y:
When the user or the system finishes his movement by inserting a line, it will be directed to one of these two functions
according to who the movement belongs to. These two functions organize the inputs and prepare them for display on the game screen.

Your opponent in this game is the system and I programmed it to predict the next two moves and choose the best position and move.
I used tree structure and linked list to write this program.
Linked list to navigate between nodes and tree to predict next states.
My node class is box, which has the properties of nodes, but due to a bug encountered by the program, I had to create another node class called TempBox.
#### In the box class:
Index: box/square number (each node has a specific number)
Number: line number (top=1, right=2, bottom=3, left=4)
Next: The next node
prev: previous node
Scoring: Each node is given a unique score based on the number of four lines inserted (25 points per line).
If any line is inserted, the position of that line changes from False to True.
list_of_branches: Before the system moves, it creates a tree and continues it to several levels and chooses the best mode.
The root of the tree is a node (square) that is evaluated and selected
from among the existing nodes. Each node contains a list of all the nodes of the next level. In the next level,
a node is again evaluated and selected among the nodes, and inside the selected 
node there is a list of nodes of the next level, and if needed, we go to the next level and this process continues.
The name of this list is list_of_branches.



