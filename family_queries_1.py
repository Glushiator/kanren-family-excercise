from unification import var

from base_relations import woman, year_of_birth, man, human
from family_facts import family_facts
from family_relations import *
from kanren_ex import run_all, run_is_true
from numeric_relations import lesser_than, odd_number, even_number, greater_than


def _main():
    family_facts()

    x = var()

    print("all known women", run_all(x, woman(x)))
    print("all known men", run_all(x, man(x)))
    print("all known humans", run_all(x, human(x)))
    print("parents of Ursula", run_all(x, parent(x, 'Ursula')))
    print("grandparents of Ursula", run_all(x, grandparent(x, 'Ursula')))
    print("grandmothers of Ursula", run_all(x, grandmother(x, 'Ursula')))
    print("children of Dominique", run_all(x, child(x, 'Dominique')))
    print("grandchildren of Dominique", run_all(x, grandchild(x, 'Dominique')))
    print("siblings of Felix", run_all(x, sibling(x, 'Felix')))
    print("siblings of Ursula", run_all(x, sibling(x, 'Ursula')))
    print("cousins of Felix", run_all(x, cousin(x, 'Felix')))
    print("parents of Paul", run_all(x, parent(x, 'Paul')))
    print("nieces of Paul", run_all(x, niece(x, 'Paul')))
    print("mother of Ursula", run_all(x, mother(x, 'Ursula')))
    print("mother of Paul", run_all(x, mother(x, 'Paul')))
    print("father of Ursula", run_all(x, father(x, 'Ursula')))
    print("children of John", run_all(x, child(x, 'John')))
    print("is Elizabeth a woman", run_is_true(woman('Elizabeth')))
    print("is John a man", run_is_true(man('John')))
    print("is Paul a woman", run_is_true(woman('Paul')))
    print("grandparents", run_all(x, grandparent(x, var())))
    print("grandparents of Felix", run_all(x, grandparent(x, 'Felix')))
    print("cousins of Xander", run_all(x, cousin(x, 'Xander')))
    print("grandchildren", run_all(x, grandparent(var(), x)))
    print("mothers", run_all(x, mother(x, var())))
    print("daughters", run_all(x, daughter(x, var())))
    print("granddaughters of Kim", run_all(x, granddaughter(x, 'Kim')))
    print("grandsons of Kim", run_all(x, grandson(x, 'Kim')))
    print("born on 1931", run_all(x, year_of_birth(1931, x)))

    print("daughters of Paul and Natalie", run_all(
        x,
        daughter(x, 'Natalie'),
        daughter(x, 'Paul'),
    ))

    print("ancestors of Cesar", run_all(x, ancestor(x, 'Cesar')))

    a_year = var()

    print("born after 2000", run_all(x,
        year_of_birth(a_year, x),
        lesser_than(2000, a_year)
    ))

    print("born before 1960", run_all(x,
        year_of_birth(a_year, x),
        lesser_than(a_year, 1960)
    ))

    print("born on an odd year", run_all(x,
        year_of_birth(a_year, x),
        odd_number(a_year)
    ))

    print("born on an even year", run_all(x,
        year_of_birth(a_year, x),
        even_number(a_year)
    ))

    Pauls_yob = var()  # Paul's year of birth

    print("people younger than Paul", run_all(x,
        year_of_birth(Pauls_yob, 'Paul'),
        year_of_birth(a_year, x),
        greater_than(a_year, Pauls_yob),
    ))

    print("people older than Paul", run_all(x,
        year_of_birth(Pauls_yob, 'Paul'),
        year_of_birth(a_year, x),
        greater_than(Pauls_yob, a_year),
    ))


if __name__ == '__main__':
    _main()
