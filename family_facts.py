from kanren import facts

from base_relations import woman, man, year_of_birth
from family_relations import parent


def family_facts():
    facts(
        woman,
        ("Elizabeth",),
        ("Natalie",),
        ("Dominique",),
        ("Ursula",),
        ("Roberta",),
        ("Joanna",),
    )

    facts(
        man,
        ("John",),
        ("Paul",),
        ("Alex",),
        ("Felix",),
        ("Xander",),
        ("Keith",),
        ("Anthony",),
        ("Cesar",),
        ("Kim",),
    )

    facts(
        year_of_birth,
        (1961, 'Paul'),
        (1963, "Natalie"),
        (1951, "John"),
        (1964, "Elizabeth"),
        (1988, "Cesar"),
        (1989, "Ursula"),
        (1931, "Dominique"),
        (1930, "Alex"),
        (1930, "Kim"),
        (1993, 'Felix'),
        (1972, 'Roberta'),
        (1989, 'Xander'),
        (1921, 'Joanna'),
        (2002, 'Keith'),
        (1997, 'Anthony'),
        (1926, 'Kim')
    )

    facts(
        parent,
        ("Paul", "Ursula"),
        ("Paul", "Cesar"),
        ("Natalie", "Ursula"),
        ("Natalie", "Cesar"),
        ("Dominique", "Paul"),
        ("Dominique", "Elizabeth"),
        ("Dominique", "John"),
        ("John", "Roberta"),
        ("John", "Xander"),
        ("John", "Felix"),
        ("Elizabeth", "Keith"),
        ("Elizabeth", "Anthony"),
        ("Alex", "Paul"),
        ("Alex", "Elizabeth"),
        ("Alex", "John"),
        ("Joanna", "Natalie"),
        ("Kim", "Natalie"),
    )
