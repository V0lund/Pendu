from io import StringIO
from pytest import mark


def initial_setup():
    """
    Testing pytest functionality. Ignored in game testing
    """
    assert True


def test_choix_joueur(monkeypatch):
    """
    Test for function choix_joueur(). The stdin is emulated by monkeypatch.
    Letter input: 'm'.
    Expected return: "M"
    code source: https://gist.github.com/GenevieveBuckley/efd16862de9e2fe7adfd2bf2bef93e02
    """
    monkeypatch.setattr('sys.stdin', StringIO('m\n') )
    from pendu import choix_joueur
    assert choix_joueur() == 'M'


@mark.parametrize('input, expected',
                  [('maison', '______'),
                   ('anticonstitutionnellement', '_________________________'),
                   ('intergouvernementalisations', '___________________________'),
                   ('trois', '_____'),
                   ('un', '__'),
                   ('moyenne', '_______')])
def test_mot_en_dash(input, expected):
    """
    code source: https://docs.pytest.org/en/stable/parametrize.html?highlight=parame
    :param input: str alpha
    :param expected: str _____
    :return: as expected
    """
    from pendu import mot_en_dash
    assert mot_en_dash(input) == expected


@mark.parametrize('input_int, input_str, expected',
                  [('5', 'maison', 'Victoire!'),
                   ('1', 'trois', 'Victoire!'),
                   ('2', 'anticonstitutionnellement', 'Victoire!'),
                   ('0', 'moye__e', 'Perdu!'),
                   ('0', '______', 'Perdu!'),
                   ('0', 'u_', 'Perdu!')])
def test_assert_victoire(input_int, input_str, expected):
    from pendu import assert_victoire
    assert assert_victoire(int(input_int), input_str) == expected
