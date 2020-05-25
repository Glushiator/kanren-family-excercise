from kanren import Relation, lall, lany, eq
from kanren.constraints import neq
from kanren.core import Zzz
from unification import var

from base_relations import woman, man


__all__ = (
    "parent",
    "grandparent",
    "grandmother",
    "child",
    "grandchild",
    "sibling",
    "cousin",
    "niece",
    "mother",
    "father",
    "daughter",
    "grandson",
    "granddaughter",
    "ancestor",
)


parent = Relation()


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


def ancestor(an_adult, a_child):
    parent_of_child = var()
    return lall(
        parent(parent_of_child, a_child),
        lany(
            eq(an_adult, parent_of_child),
            Zzz(ancestor, an_adult, parent_of_child)
        )
    )
