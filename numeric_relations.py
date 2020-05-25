import operator as op
from kanren_ex import goalify

lesser_than = goalify(op.lt)
greater_than = goalify(op.gt)
odd_number = goalify(lambda n: n % 2 == 1)
even_number = goalify(lambda n: n % 2 == 0)
