# DINO RUN

This is our project for the coding weeks at CentraleSupélec.

## Members (Contributors):

* Mohammed El-Adli
* Oussama Kharouiche
* Oussama Er-rahmany
* Douae Amzil
* Nizar El Ghazal
* Mohamed Reda Mouqed

## Description:

This project is a game integrated to Google Chrome that appears when you don't have access to the internet.
The game is programmed on the basis of the *pygame* library of Python, and has been improved by adding a new theme: Christmas, and other features.

The goal of the game is to control the dinosaur so that it can advance as much as possible in the presence of obstacles. The difficulty of the game consists in the speed of the obstacles, which increases according to the score.

## Imported libraries:
  pygame
 
  os
 
  random

## How to launch the game:
The execution of the **play.py** module displays a window that allows you to choose the desired mode.

By clicking (using the mouse) on the chosen mode, a new window appears. The game starts when a key is pressed on the keyboard.

The game stops when the dinosaur touches an obstacle. You have to press a key on the keyboard to go back to the home menu.
  ## Game controls:
       
       Arrow up: jump (the time the key is pressed corresponds to the height of the jump)
       Arrow down: go down
       Space: jump to the highest height
       Escape: quit the game and return to the main menu
**IMPORTANT : For the game to work properly, you must make sure that pygame is installed and that the current directory is the project folder.**

## Contribution to the game:

This part is reserved for those who want to contribute to the improvement of the game, so it contains details about the contents of other Python files. These files are in */gamefiles/modules*.

 * **game.py :**
  This module contains the program that allows you to run the game with theme support.
 * **mvp.py :**
  This module is the MVP version of the game, its execution launches directly the MVP mode : the player is represented by a yellow block and the obstacles by red rectangles.
 * **theme_files.py :**
  This module allows to load images from the assets folder according to the theme chosen in the game; and also contains all the functions to implement the themes and visual effects.

  The files are commented in detail which allows an easier understanding of the functions used.

The folder */gamefiles/assets* contains all the image files used in the themes, the themes are placed in folders of the same structure to facilitate the import.
