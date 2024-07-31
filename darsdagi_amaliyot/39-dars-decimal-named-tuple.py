from collections import namedtuple
from decimal import Decimal
# p = namedtuple('colors', ('red', 'green', 'blue'))
#
# colors = (p(255, 0, 0), p(0, 255, 0), p(0, 0, 255))
#
# for color in colors:
#     print(color.red)

reason = namedtuple('g', ('coffee', 'taxi', 'charity'))

days = (reason(Decimal('0.6'), Decimal('5.6'), Decimal('9.6')), reason(Decimal('4.6'), Decimal('0.7'), Decimal('4.6')))
i = 0
for day in days:
    print(f'{i+1}-kun -> {day.coffee + day.taxi + day.charity}')
    i += 1


text = """
enter reason - 1
calculate - 2
"""
while True:
    reasons = ()
    costs = ()
    reason = input('Enter reason>>>')
    cost = Decimal(input('Cost>>>'))
    reasons =
