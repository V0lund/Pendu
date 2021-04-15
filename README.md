# Pendu
Programme permettant de jouer au pendu. Programme sur plusieurs niveaux. 
Ce programme sera constitué d’un fichier python (pendu.py) et d’un fichier texte vide qui contiendra une liste de mots (dico.txt).
Niveau 1
Au premier niveau, ajoutez manuellement dans dico.txt le mot maison. Concevez le jeu de la façon suivante:
• Créez une fonction qui charge le fichier dico.txt en mémoire.
• Créez une fonction qui choisit au hasard un mot dans la liste.
• Créez une fonction qui affiche le mot sous forme de "_ _ _ _ _ _" à l’écran.
Chaque lettre trouvée sera affichée à sa bonne place. Le mot sera affiché en MAJUSCULES. Les accents ne seront pas traités.
• Créez une fonction qui demande une lettre au joueur. Cette fonction répète la question tant que le joueur ne satisfait pas la demande ou tape une lettre déjà
jouée précédement.
• Créez une fonction qui affiche progressivement un pendu en ascii art (ou un simple texte =PENDU...=) en fonction du nombre d’essais. Le joueur à 8
essais pour gagner.
• Créez une fonction qui indique si le joueur à gagné ou perdu.
• Créez une fonction principale qui permet de lancer le jeu et de jouer indéfiniment
jusqu’à ce que le joueur décide de quitter l’application.

Niveau 2
Écrivez des tests avec PyTest pour tester ces différentes fonctions.

Niveau 3
Améliorez le jeu en y apportant les fonctionnalités suivantes:
• Créez une fonction qui permette au joueur d’ajouter des mots au dictionnaire.
La fonction vérifie si le mot est dans le dictionnaire et que le mot soit d’au moins 6 lettres. S’il n’y est pas, le mot sera ajouté au fichier texte. 
Si le mot existe déjà dans le dictionnaire ou s’il contient moins de 6 lettres, il sera indiqué à l’écran que le mot est non conforme ou existant et il sera ignoré.
• Modifiez le stockage des mots en mémoire. Ceux-ci seront désormais classés en fonction du nombre de lettres dans le mots.
• Modifiez la fonction qui choisit aléatoirement un mot. Désormais, un mot d’une certaine taille sera choisi aléatoirement, en fonction d’un niveau de difficulté :
1.La difficulté facile choisira des mots de 6 lettres uniquement.
2. La difficulté normale choisira des mots entre 6 et 9 lettres.
3. La difficulté difficile choisira des mots entre 8 et 12 lettres.
4. La difficulté maître choisira des mots de plus de 12 lettres uniquement.
Faites en sorte que l’utilisateur puisse choisir sa difficulté à chaque partie.
Niveau 4
Écrivez les tests des nouvelles fonctions. Attention, les tests précédents doivent toujours être validés !
