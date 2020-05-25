import operator as op
from functools import partial

from kanren import *
from kanren.constraints import neq
from kanren.core import Zzz
from kanren.util import unique

from kanren_ex import goalify

parent = Relation()
woman = Relation()
man = Relation()
year_of_birth = Relation()


def mother(an_adult, a_child):
    return lall(
        parent(an_adult, a_child),
        woman(an_adult)
    )


def father(an_adult, a_child):
    return lall(
        parent(an_adult, a_child),
        man(an_adult)
    )


def sibling(person1, person2):
    common_parent = var()
    return lall(
        neq(person1, person2),
        parent(common_parent, person1),
        parent(common_parent, person2),
    )


def cousin(person1, person2):
    parent1 = var()
    parent2 = var()
    return lall(
        parent(parent1, person1),
        parent(parent2, person2),
        sibling(parent1, parent2),
    )


def sibling_of_parent(a_person, a_child):
    parent_of_child = var()
    return lall(
        parent(parent_of_child, a_child),
        sibling(a_person, parent_of_child),
    )


def child_of_sibling(a_child, an_adult):
    parent_of_child = var()
    return lall(
        parent(parent_of_child, a_child),
        sibling(an_adult, parent_of_child),
    )


def niece(a_child, an_adult):
    return lall(
        child_of_sibling(a_child, an_adult),
        woman(a_child)
    )


def nephew(a_child, an_adult):
    return lall(
        child_of_sibling(a_child, an_adult),
        man(a_child)
    )


def aunt(an_adult, a_child):
    return lall(
        sibling_of_parent(an_adult, a_child),
        woman(an_adult)
    )


def uncle(an_adult, a_child):
    return lall(
        sibling_of_parent(an_adult, a_child),
        man(an_adult)
    )


def child(a_child, an_adult):
    return parent(an_adult, a_child)


def son(a_child, an_adult):
    return lall(
        child(a_child, an_adult),
        man(a_child)
    )


def daughter(a_child, an_adult):
    return lall(
        child(a_child, an_adult),
        woman(a_child)
    )


def grandparent(an_adult, a_child):
    common_relative = var()
    return lall(
        parent(an_adult, common_relative),
        parent(common_relative, a_child),
    )


def grandmother(an_adult, a_child):
    return lall(
        grandparent(an_adult, a_child),
        woman(an_adult),
    )


def grandfather(person1, person2):
    return lall(
        grandparent(person1, person2),
        man(person1),
    )


def grandchild(person1, person2):
    return grandparent(person2, person1)


def grandson(a_child, an_adult):
    return lall(
        grandchild(a_child, an_adult),
        man(a_child)
    )


def granddaughter(a_child, an_adult):
    return lall(
        grandchild(a_child, an_adult),
        woman(a_child)
    )


def human(a_person):
    return lany(
        woman(a_person),
        man(a_person),
    )


lesser_than = partial(goalify, op.lt, True)
greater_than = partial(goalify, op.gt, True)
odd_number = partial(goalify, lambda n: n % 2 == 1, True)
even_number = partial(goalify, lambda n: n % 2 == 0, True)


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


def ancestor(an_adult, a_child):
    parent_of_child = var()
    return lall(
        parent(parent_of_child, a_child),
        lany(
            eq(an_adult, parent_of_child),
            Zzz(ancestor, an_adult, parent_of_child)
        )
    )


def _find_all(vars_, *goals_):
    return run(0, vars_, *goals_, results_filter=unique)


def _is_true(*goals_):
    return bool(run(1, True, *goals_))


def _main():
    x = var()

    _find_any = partial(run, 1)

    print("all known women", _find_all(x, woman(x)))
    print("all known men", _find_all(x, man(x)))
    print("all known humans", _find_all(x, human(x)))
    print("parents of Ursula", _find_all(x, parent(x, 'Ursula')))
    print("grandparents of Ursula", _find_all(x, grandparent(x, 'Ursula')))
    print("grandmothers of Ursula", _find_all(x, grandmother(x, 'Ursula')))
    print("children of Dominique", _find_all(x, child(x, 'Dominique')))
    print("grandchildren of Dominique", _find_all(x, grandchild(x, 'Dominique')))
    print("siblings of Felix", _find_all(x, sibling(x, 'Felix')))
    print("siblings of Ursula", _find_all(x, sibling(x, 'Ursula')))
    print("cousins of Felix", _find_all(x, cousin(x, 'Felix')))
    print("parents of Paul", _find_all(x, parent(x, 'Paul')))
    print("nieces of Paul", _find_all(x, niece(x, 'Paul')))
    print("mother of Ursula", _find_all(x, mother(x, 'Ursula')))
    print("mother of Paul", _find_all(x, mother(x, 'Paul')))
    print("father of Ursula", _find_all(x, father(x, 'Ursula')))
    print("children of John", _find_all(x, child(x, 'John')))
    print("is Elizabeth a woman", _is_true(woman('Elizabeth')))
    print("is John a man", _is_true(man('John')))
    print("is Paul a woman", _is_true(woman('Paul')))
    print("grandparents", _find_all(x, grandparent(x, var())))
    print("grandparents of Felix", _find_all(x, grandparent(x, 'Felix')))
    print("cousins of Xander", _find_all(x, cousin(x, 'Xander')))
    print("grandchildren", _find_all(x, grandparent(var(), x)))
    print("mothers", _find_all(x, mother(x, var())))
    print("daughters", _find_all(x, daughter(x, var())))
    print("granddaughters of Kim", _find_all(x, granddaughter(x, 'Kim')))
    print("grandsons of Kim", _find_all(x, grandson(x, 'Kim')))
    print("born on 1931", _find_all(x, year_of_birth(1931, x)))

    print("daughters of Paul and Natalie", _find_all(
        x,
        daughter(x, 'Natalie'),
        daughter(x, 'Paul'),
    ))

    print("ancestors of Cesar", _find_all(x, ancestor(x, 'Cesar')))

    a_year = var()

    print("born after 2000", _find_all(x,
        year_of_birth(a_year, x),
        lesser_than(2000, a_year)
    ))

    print("born before 1960", _find_all(x,
        year_of_birth(a_year, x),
        lesser_than(a_year, 1960)
    ))

    print("born on an odd year", _find_all(x,
        year_of_birth(a_year, x),
        odd_number(a_year)
    ))

    print("born on an even year", _find_all(x,
        year_of_birth(a_year, x),
        even_number(a_year)
    ))

    Pauls_yob = var()  # Paul's year of birth

    print("people younger than Paul", _find_all(x,
        year_of_birth(Pauls_yob, 'Paul'),
        year_of_birth(a_year, x),
        greater_than(a_year, Pauls_yob),
    ))

    print("people older than Paul", _find_all(x,
        year_of_birth(Pauls_yob, 'Paul'),
        year_of_birth(a_year, x),
        greater_than(Pauls_yob, a_year),
    ))


if __name__ == '__main__':
    _main()
