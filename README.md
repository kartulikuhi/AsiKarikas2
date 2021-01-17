OVERALL:
I used the knife, class and push libraries as well as the Statemachine.lua and Basestate.lua files that are used across all the LOVE2D projects in the course. The rest of the files are handwritten by myself. I believe my implementation of Connect Four satisfies all the requirements of the final project and is different from all the other games in the course because it is an implementation of a board game that is not similar and is of the same complexity as the other LOVE2D games in the course.

main.lua:
The main.lua file is a basic setup for all the states and other stuff needed for the operation of the game. Due to the background image being too small to cover the entire screen and to achieve the scrolling effect, I made it so it renders 3 background images next to eachother, and then scrolls it through (3 is needed so the entire screen is always covered by the background while scrolling). When 1 of the background images leaves the left border of the screen, it will change its x coordinate to the end of the last background image. The main file also setups the statemachine and timer.

Dependencies.lua:
Just a place to acquire all the files to be used in the game.

constants.lua:
Just a place to store global variables

StartState.lua:
This is the starting screen of Connect Four and the logo's letters are changing color using the same technique used in the MATCH3 lecture. Upon pressing ENTER it will take the player to the PlayState.

PlayState.lua:
This is the state that the gameplay takes place in. It first initializes a yellow coin and a gameboard. The coin can be moved using A and D or the LEFT and RIGHT arrow keys. When the player presses ENTER the coin will drop into the last available slot. The coin can be seen moving and will appear as though it went inside the board like in real life, which is achieved by rendering the board after the coin and tweening the coin's y value. After a player has made their turn, the next player can move and the other colored coin will spawn at the spot where the coin was thrown (this is because it felt a bit frustrating to move to the part of the board the coin was thrown from every time to counter the play).
When there is either 4 yellow or 4 red coins in a straight line (either horizontally, vertically or diagonally), a short sound effect will play and the game will be brought to the GameOverState. When a draw happens (this means that all of the slots have been filled by coins but there isn't a single winning 4 in a row line), the game will end and the players will be brought to the GameOverState. 

GameOverState.lua:
When the game ends the players will be brought to a screen of the board and depending on who won or if it was a draw, the colors of the CONGRATULATIONS and PLAYER X won text will be changed. Upon pressing ENTER the players will be brought back to the StartState.

Board.lua:
Upon initialization, it will create a table of the x and y grids of the board. Every coordinate in the table will be given a value of false(which means that its an empty slot that does not have a coin in it). A table that cointains all the coins will also be generated. When a coin is dropped into the board in the PlayState, the table of falses will have the coordinates of the slot the coin fell into be changed to true, so the next coin would fall into the slot above that. This was inspired from the maze generation algorithm of the dreadhalls lecture. The Board:calculateWins() function will go over all the possible win conditions after every move and if it finds 4 coins of the same color connected with a straight line, it will return true to indicate that after that move the player who made the move won.

Coin.lua:
This is the coin used in the game and the coins x and y value represent it's location on the board's grid (for example a coin with an x value of 1 and a y value of 6 will be at the bottom left corner of the board). It's also identified as a yellow or a red coin depending on who made the move.