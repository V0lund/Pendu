# MODULE
# from random import randint pour future version

# VARIABLES GLOBALES
essaies: int = 8
mot = ''
m_list = []
m_dash = ''
m_dash_list = []


def fichier():
    """
    Function qui charge en memoire le fichier dico. Elle ne prandre aucune input mais revoie le contenu du fichier.
    :return: textIO: le contenu du fichier dico.txt
    """
    return open('dico', 'r')


def mot_en_fichier() -> str:
    """
    Fonction qui renvoie un mot contenu dans le fichier dico en utilisent la methode randint et la function fichier().
    :return: le mot du fichier dico
    """
    # variable pour garder le mot qui se trouver dans le fichier en majiscules dico.txt
    line = (fichier().readline()).upper()
    # option pour future version  -> renvoyer un entier entre 1 et la valeur stocke dans la variable lenght -1
    return line


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
    check = False
    l = input('Saisissez une lettre: ').upper()
    while check == False:
        if l.isalpha() and len(l) == 1:
            check = True
        else:
            l = input('Saisissez une lettre: ').upper()
    return l


def insertion_lettre(l: str):
    """
    FONCTION pour inserer dans la variable m_dash la lettre choisie par le joueur et remplacer la meme lettre par un '_' dans la variable mot
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


def affichage_pendu(t:int):
    """
    Fonction qui return le fichier hanged.txt en fonction du nombre d’essaies.
    :param: int: il prendre comme input un entier == le nombre d’essaies restes pour le jouer.
    :return: str: affiche part de fichier hanged.txt
    """
    hanged = open('hanged', 'r')
    hanged_lines = hanged.readlines()
    last_lines = hanged_lines[(t-8)*3:]
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
        return 'Victoire!'
    else:
        return 'Perdu!'


if __name__ == '__main__':
    print('LE PENDU!')
    print('Bientot disponible!!!')
    print('vs 0.1')
    print()
    mot = mot_en_fichier()
    m_dash = mot_en_dash(mot)
    m_list = list(mot)
    m_dash_list = list(m_dash)
    while essaies > 0 and '_' in m_dash:
        print()
        print(m_dash)
        j_ch = choix_joueur()
        print()
        if j_ch in mot and j_ch not in m_dash:
            insertion_lettre(j_ch)
            m_dash = ''.join(_ for _ in m_dash_list)
        elif j_ch in m_dash:
            essaies -= 1
            print('Vous avez deja choisiez cette lettre!')
            print()
            print(affichage_pendu(essaies))
        else:
            essaies -= 1
            print(affichage_pendu(essaies))

    print(assert_victoire(essaies, m_dash))


