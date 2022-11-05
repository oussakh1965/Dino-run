# DINO RUN

This is our project for the coding weeks at CentraleSupélec.

## Membres (Contributeurs):

* Mohammed El-Adli
* Oussama Kharouiche
* Oussama Er-rahmany
* Douae Amzil
* Nizar El Ghazal
* Mohamed Reda Mouqed

## Description:

Ce projet est un jeu integré à Google Chrome qui apparait lorsqu'on n'a pas accès à internet.
Le jeu est programmé à la base du module *pygame* de Python, et a été amélioré en ajoutant un nouveau thème : Noël, et d'autres fonctionnalités.

Le but du jeu est de contrôler le dinosaure pour qu'il puisse avancer le plus possible en présence d'obstacles. La difficulté du jeu consiste en la vitesse des obstacles qui augmente en fonction du score.

## Modules importées:
  pygame
 
  os
 
  random

## Comment lancer le jeu:
L'éxecution du module **play.py** permet d'afficher une fenêtre qui permet de choisir le mode souhaité.

En cliquant (en utilisant la souris) sur le mode choisi, une nouvelle fenêtre apparait. Le jeu commence lorsqu'on appuie sur une touche au clavier.

Le jeu s'arrête lorsque le dinosaure touche un obstacle. Il faut donc appuyer sur une touche au clavier pour se retrouver au menu d'accueil.
  ## Commandes du jeu:
       
       Flèche haut : sauter (le temps d'appui correspond à la hauteur du saut)
       Flèche bas : baisser
       Espace : sauter à la plus grande hauteur
       Echap : quitter le jeu et retourner au menu principal
**IMPORTANT : Pour que le jeu fonctionne correctement, il faut s'assuer que pygame est bien installé et que le répertoire courant est bien le dossier du projet.**

## Contribution au jeu:

Cette partie est réservée pour celles et ceux qui souhaitent contribuer à l'amélioration du jeu, elle contient donc des détails sur les contenus des autres fichiers Python. Ces fichiers sont dans */gamefiles/modules*.

 * **game.py :**
  Ce module contient le programme qui permet d'executer le jeu avec prise en charge des themes
 * **mvp.py :**
  Ce module est la version MVP du jeu, son éxecution lance directement le mode MVP : le joueur est representé par un bloc jaune et les obstacles par des rectangles rouges.
 * **theme_files.py :**
  Ce module permet de charger les images à partir du dossier assets selon le thème choisi dans le jeu; et contient aussi tous les fonctions permettant d'implementer les themes et les effets visuels.

  Les fichiers sont commentés en détails ce qui permet une compréhension plus facile des fonctions utilisées.

Le dossier */gamefiles/assets* contient tous les fichiers images utilisés dans les thèmes, les thèmes sont placés dans des dossiers de même stucture pour faciliter l'importation.
