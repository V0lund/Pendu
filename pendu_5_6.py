# LES MODULES
import random
import time
import database


# VARIABLES GLOBALES
essaies: int = 8
tries: int = 0
mot = ''
m_list = []
m_dash = ''
m_dash_list = []
mega_list = []
short_list = []
player_stat = {'name': '', 'level': '', 'tries': '', 'time': ''}


# FONCTIONS
def option_jouer_menu():
    print("Choisi une option de jeux.")
    print("Apuyez sur 'n' pour un nouveau jeux, 'q' pour quitter ou 'a' pour ajouter une mot a la dictionnaire")
    c = True
    o = ''
    while c:
        o = input('Votre choix:>> ').lower()
        if not (o == 'n' or o == 'a' or o == 'q'):
            print("Selon 'n', 'a' et 'q' sont des option valides!")
            print()
        else:
            c = False
            return o


def option_difficulte() -> int:
    """
    FONCTION qui return une valeur numerique qui correspond au niveau de difficulte choisi par le jouer: 1 pour facile;
    2 pour normale; 3 pour difficile; 4 pour maitre.
    :rtype: int
    :return: variable option de type int.
    """
    print("Vous avez choisi de jouer un nouveau tour!")
    print()
    print("Choisi la difficulte. Vous aves quatre niveaux de difficulte:\n"
          "'facile' (mot de 6 lettres) - apuyer sur 1;\n"
          "'normale' (mot entre 6 et 9 lettres) - apuyer sur 2;\n"
          "'difficile' (mot entre 8 et 12 lettres) - apuyer sur 3;\n"
          "'maitre' (mot de plus 12 lettres) - apuyer sur 4.\n")
    c = True
    while c:
        option = input("Votre choix:> ")
        if option == '1' or option == '2' or option == '3' or option == '4':
            player_stat.update({"level": int(option)})
            print(f"Vous avez choisi l'option {option}.")
            print()
            c = False
            return int(option)
        else:
            print("Choisi l'une des variates sugerees: 1, 2, 3 ou 4")
            print()


def sorter_dico():
    """
    :PROCEDURE: pour sorter les mots qui se trouve dans le dictionnaire dico par leur longuere
    :source: https://www.codespeedy.com/sorting-contents-of-a-text-file-using-a-python-program/
    """
    # Les mots du fichier dico sont charge dans la variable dico
    dico = open('dico')
    for i in dico:  # iteration finite sur dico pour assigne chaque element a une list
        mega_list.append(i)  # Les elements sont suave dans la variable globale 'mega_list'
    dico.close()  # le fichier e dealoche de la memoire
    mega_list.sort(key=len)  # les elements de la mega_list sont sorte, soit par leur longuere (key = len), soit dans l'ordre alphabetique.
    # Le contenu du fichier dico est ecraser. ON utilise la methode 'write' pour ecrire une espace vide.
    dico = open('dico', 'w')
    dico.write("")
    dico.close()
    # Les elements du mega_list sont reajouster a la fichier dico dans leur ordre
    with open('dico', 'a') as a:
        for i in mega_list:
            a.write(i)
    mega_list.clear()


def ajouter_mot_dico():
    """
    PROCEDURE pour ajouter des mot a fichier dico. Les mots sont ajoute si il n'existe deja dans le dictionnaire!
    source des donnes: https://www.liste-de-mots.com/
    """

    dico = set(fichier().readlines())  # chargement des mots dans le memoire
    print()
    print("Quelle mot voudriez vous ajouter a le dictionnaire?")
    c = True
    while c:
        uti_mot = input('Votre mot::>  ').upper()
        if len(uti_mot) >= 6 and uti_mot.isalpha():
            if uti_mot + '\n' not in dico:
                with open('dico', 'a+') as f:
                    f.write(uti_mot)
                    f.write('\n')

                print(f"Le mot '{uti_mot}' a ete ajouter a la dictionnaire!")
                c = False
            else:
                print(f"Le mot '{uti_mot}' se trouve deja dans le dictionnaire. Choississez une autre!")
                print()
        else:
            print("C'est pas un vrai mot, n'est pas ? Reyesseyez svpl.")
            print()


def fichier():
    """
    Function qui charge en memoire le fichier dico. Elle ne prandre aucune input mais revoie le contenu du fichier.
    :return: textIO: le contenu du fichier dico.txt
    """
    dico_load = open('dico', 'r')
    return dico_load


def mot_en_fichier(i: int) -> str:
    """
    Fonction qui renvoie un mot contenu dans le fichier dico en utilisent la methode randint et la function fichier().
    :param: integer
    :rtype: string
    """
    m = 0
    n = 0
    if i == 1:
        n = 8
    elif i == 2:
        m = 8
        n = 11
    elif i == 3:
        m = 10
        n = 14
    else:
        m = 15
        n = 100
    d = open('dico', 'r')
    ls = list(d.readlines())  # test OK -- type list
    for x in ls:
        if m <= len(x) <= n:
            x = x.rstrip("\n")
            short_list.append(x)
    d.close()
    return short_list[random.randint(0, len(short_list) - 1)]


def mot_en_dash(m) -> str:
    """
    Fonction qui affiche le mot sous forme de "_ _ _ _ _ _" à l’écran.
    """
    return ''.join(str('_') for _ in m)


def choix_joueur() -> str:
    """
    Fonction d'évaluation de l'input du joueur. Le joueur doit choisir une seule lettre.
    :return: str: la lettre choisie par jouer.
    """
    check = True
    l = input('Saisissez une lettre: ').upper()
    while check:
        if l.isalpha() and len(l) == 1:
            check = False
        else:
            l = input('Saisissez une lettre: ').upper()
    return l


def insertion_lettre(l: str):
    """
    FONCTION pour inserer dans la variable m_dash la lettre choisie par le joueur et
    remplacer la meme lettre par un '_' dans la variable mot
    :param l: str: la lettre choisie par joueur.
    :return: aucune
    """
    for x in m_list:
        if x == l:
            i = m_list.index(l)
            del m_dash_list[i]
            m_dash_list.insert(i, l)
            del m_list[i]
            m_list.insert(i, "_")
    return True


def affichage_pendu(t: int):
    """
    Fonction qui return le fichier hanged.txt en fonction du nombre d’essaies.
    :type t: int -- le int sauver dans le variable globale essaies
    :param: int: il prendre comme input un entier == le nombre d’essaies restes pour le jouer.
    :return: str: affiche part de fichier hanged.txt
    """
    hanged = open('hanged', 'r')
    hanged_lines = hanged.readlines()
    last_lines = hanged_lines[(t - 8) * 3:]
    for _ in last_lines:
        print(_, end='')
    pass


def assert_victoire(i: int, s: str) -> str:
    """
    FONCTION pour tester si le joueur a gagne ou pas.
    :param i: entier qui corresponde o variable essaies
    :param s: parametre pour verifie si toutes les lettres ont ete decouvertes.
    :return: string avec le message: 'Victoire!' ou 'Perdu!'
    """
    if i > 0 and '_' not in s:
        return 'Très bien! Vous avez gagne!'
    else:
        return 'Dommage! Vous avez perdu!'


def nom_joueur() -> str:
    """
    FONCTION qui renvoie un string avec le nom du joueur. Le mot est sauvé dans le dictionnaire player_stat
    :return: string
    """
    name = ''
    c = True
    while c:
        print('Quel est votre nom?')
        name = input(':>> ').lower()
        if len(name) < 6:
            print('Choisissez un nom de minimum 6 lettres.')
        else:
            player_stat.update({"name": name})
            c = False
            return name


def insertion_player_stat_en_db(d):
    """
    FONCTION pour sauver les valeurs du dict player_stat dans le db leaderboards. Elle appelle la fonction
    db_insert du fichier database. Le but final est d'inserer dans la table player_stat du db leadersboard
    les valeurs sauver dans le dictionnaire player_stat / Dieu a pitié de mon pauvre cerveau !
    :param: dictionary
    """
    database.db_insert(d)


# DEBUT DU PROGRAM
if __name__ == '__main__':
    print('LE PENDU!')
    print('Bientot disponible!!!')
    print('vs 0.5')
    print()
    database.show_leadersboard()
    print()

    # MENU et OPTIONS
    nom_joueur()
    c = True
    while c == True:
        print()
        opt_uti = option_jouer_menu()  # variable pour stocke l'option d'utilisateur
        if opt_uti == 'n':  # option pour jouer/rejouer le jeux
            niveau_uti = option_difficulte()  # variable pour stocke l'option du jeux du jouer.
            mot = mot_en_fichier(niveau_uti)
            m_dash = mot_en_dash(mot)
            m_list = list(mot)
            m_dash_list = list(m_dash)

            # DEBUT DU JEUX
            start_time = time.time()
            while essaies > 0 and '_' in m_dash:
                print()
                print(m_dash)
                j_ch = choix_joueur()
                print()
                if j_ch in mot and j_ch not in m_dash:
                    insertion_lettre(j_ch)
                    m_dash = ''.join(_ for _ in m_dash_list)
                    tries += 1
                elif j_ch in m_dash:
                    essaies -= 1
                    print('Vous avez deja choisiez cette lettre!')
                    print()
                    print(affichage_pendu(essaies))
                    tries += 1
                else:
                    essaies -= 1
                    print(affichage_pendu(essaies))
                    tries += 1
            end_time = time.time()
            player_stat.update({'tries': tries})
            player_stat.update({"time": round((float(end_time - start_time)), 2)})
            insertion_player_stat_en_db(player_stat)

            # RENVOYER LE RESULTAT
            print(assert_victoire(essaies, m_dash))
            print()
            database.show_leadersboard()
            essaies = 8
            tries = 0
        elif opt_uti == 'a':  # option pour ajouter un mot a la dictionnaire
            print("Vous avez choisi d'ajouter un nouveau mot au dictionnaire!")
            ajouter_mot_dico()
            sorter_dico()

            # FIN du jeux
        else:
            print()
            print('Merci pour avoir joue le PENDU! À bientôt!')
            print()
            c = False