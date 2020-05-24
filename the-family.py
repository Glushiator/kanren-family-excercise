import operator as op
from kanren import *
from kanren.goals import not_equalo

parent = Relation()
woman = Relation()
man = Relation()
year_of_birth = Relation()


def mother(an_adult, a_child):
    return lall(
        (parent, an_adult, a_child),
        (woman, an_adult)
    )


def father(an_adult, a_child):
    return lall(
        (parent, an_adult, a_child),
        (man, an_adult)
    )


def sibling(person1, person2):
    common_parent = var()
    return lall(
        (not_equalo, (person1, person2), True),
        (parent, common_parent, person1),
        (parent, common_parent, person2),
    )


def cousin(person1, person2):
    parent1 = var()
    parent2 = var()
    return lall(
        (parent, parent1, person1),
        (parent, parent2, person2),
        (sibling, parent1, parent2),
    )


def sibling_of_parent(a_person, a_child):
    parent_of_child = var()
    return lall(
        (parent, parent_of_child, a_child),
        (sibling, a_person, parent_of_child),
    )


def child_of_sibling(a_child, an_adult):
    parent_of_child = var()
    return lall(
        (parent, parent_of_child, a_child),
        (sibling, an_adult, parent_of_child),
    )


def niece(a_child, an_adult):
    return lall(
        (child_of_sibling, a_child, an_adult),
        (woman, a_child)
    )


def nephew(a_child, an_adult):
    return lall(
        (child_of_sibling, a_child, an_adult),
        (man, a_child)
    )


def aunt(an_adult, a_child):
    return lall(
        (sibling_of_parent, an_adult, a_child),
        (woman, an_adult)
    )


def uncle(an_adult, a_child):
    return lall(
        (sibling_of_parent, an_adult, a_child),
        (man, an_adult)
    )


def child(a_child, an_adult):
    return parent, an_adult, a_child


def son(a_child, an_adult):
    return lall(
        (child, a_child, an_adult),
        (man, a_child)
    )


def daughter(a_child, an_adult):
    return lall(
        (child, a_child, an_adult),
        (woman, a_child)
    )


def grandparent(an_adult, a_child):
    common_relative = var()
    return lall(
        (parent, an_adult, common_relative),
        (parent, common_relative, a_child),
    )


def grandmother(an_adult, a_child):
    return lall(
        (grandparent, an_adult, a_child),
        (woman, an_adult),
    )


def grandfather(person1, person2):
    return lall(
        (grandparent, person1, person2),
        (man, person1),
    )


def grandchild(person1, person2):
    return grandparent, person2, person1


def grandson(a_child, an_adult):
    return lall(
        (grandchild, a_child, an_adult),
        (man, a_child)
    )


def granddaughter(a_child, an_adult):
    return lall(
        (grandchild, a_child, an_adult),
        (woman, a_child)
    )


def human(a_person):
    return lany(
        (woman, a_person),
        (man, a_person),
    )


lesser_than = goalify(op.lt, 'lesser_than')
greater_than = goalify(op.gt, 'greater_than')
odd_number = goalify(lambda n: n % 2 == 1, 'odd_number')


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


def _main():
    x = var()

    print("all known women", run(0, x, woman(x)))
    print("all known men", run(0, x, man(x)))
    print("all known humans", run(0, x, human(x)))
    print("parents of Ursula", run(0, x, parent(x, 'Ursula')))
    print("grandparents of Ursula", run(0, x, grandparent(x, 'Ursula')))
    print("grandmothers of Ursula", run(0, x, grandmother(x, 'Ursula')))
    print("children of Dominique", run(0, x, child(x, 'Dominique')))
    print("grandchildren of Dominique", run(0, x, grandchild(x, 'Dominique')))
    print("siblings of Felix", run(0, x, sibling(x, 'Felix')))
    print("siblings of Ursula", run(0, x, sibling(x, 'Ursula')))
    print("cousins of Felix", run(0, x, cousin(x, 'Felix')))
    print("parents of Paul", run(0, x, parent(x, 'Paul')))
    print("nieces of Paul", run(0, x, niece(x, 'Paul')))
    print("mother of Ursula", run(0, x, mother(x, 'Ursula')))
    print("mother of Paul", run(0, x, mother(x, 'Paul')))
    print("father of Ursula", run(0, x, father(x, 'Ursula')))
    print("children of John", run(0, x, child(x, 'John')))
    print("is Elizabeth a woman", run(0, True, woman('Elizabeth')))
    print("is John a man", run(0, True, man('John')))
    print("is Paul a woman", run(0, True, woman('Paul')))
    print("grandparents", run(0, x, grandparent(x, var())))
    print("grandparents of Felix", run(0, x, grandparent(x, 'Felix')))
    print("cousins of Xander", run(0, x, cousin(x, 'Xander')))
    print("grandchildren", run(0, x, grandparent(var(), x)))
    print("mothers", run(0, x, mother(x, var())))
    print("daughters", run(0, x, daughter(x, var())))
    print("granddaughters of Kim", run(0, x, granddaughter(x, 'Kim')))
    print("grandsons of Kim", run(0, x, grandson(x, 'Kim')))
    print("born on 1931", run(0, x, year_of_birth(1931, x)))

    print("daughters of Paul and Natalie", run(0, x,
        (daughter, x, 'Natalie'),
        (daughter, x, 'Paul'),
    ))

    print("ancestors of Cesar", run(0, x,
        lany(
            (parent, x, 'Cesar'),
            (grandparent, x, 'Cesar')
        )
    ))

    a_year = var()

    print("born after 2000", run(0, x,
        (year_of_birth, a_year, x),
        (lesser_than, (2000, a_year), True)
    ))

    print("born before 1960", run(0, x,
        (year_of_birth, a_year, x),
        (lesser_than, (a_year, 1960), True)
    ))

    print("born on an odd year", run(0, x,
        (year_of_birth, a_year, x),
        (odd_number, (a_year,), True)
    ))

    print("born on an even year", run(0, x,
        (year_of_birth, a_year, x),
        (odd_number, (a_year,), False)
    ))

    Pauls_yob = var()  # Paul's year of birth

    print("people younger than Paul", run(0, x,
        (year_of_birth, Pauls_yob, 'Paul'),
        (year_of_birth, a_year, x),
        (greater_than, (a_year, Pauls_yob), True),
    ))

    print("people older than Paul", run(0, x,
        (year_of_birth, Pauls_yob, 'Paul'),
        (year_of_birth, a_year, x),
        (greater_than, (Pauls_yob, a_year), True),
    ))


if __name__ == '__main__':
    _main()
