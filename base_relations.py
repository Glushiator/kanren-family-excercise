from kanren import Relation, lany

woman = Relation()
man = Relation()
year_of_birth = Relation()


def human(a_person):
    return lany(
        woman(a_person),
        man(a_person),
    )
