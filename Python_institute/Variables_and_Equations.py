# Angelea is three years older than twice her brother
# thomas's age. If Angela is 17, How old is thomas
# 3+2t=17
# 17 - 10
thomas = 17 - 10
print(thomas)

# 3x - 7 = 8
from sympy import symbols, Eq, solve
x = symbols('x')
eq2 = Eq(3*x - 7, 8)
sol = solve(eq2)
print(sol)

# 2 - 3x = 7
from sympy import symbols, Eq, solve
x = symbols('x')
eq3 = Eq(2 - 3*x, 7)
sol = solve(eq3)
print(sol)

# 2x - 7 = 8 - x
from sympy import symbols, Eq, solve
x = symbols('x')
eq4 = Eq(2*x - 7, 8 - x)
sol = solve(eq4)
print(sol)

# 3(x-4) = 8 - 2x
from sympy import symbols, Eq, solve
x = symbols('x')
eq5 = Eq(3*(x - 4), 8 - 2*x)
sol = solve(eq5)
print(sol)

# x - 7 / 2 = 4
from sympy import symbols, Eq, solve
x = symbols('x')
eq6 = Eq(x - 7 / 2, 4)
sol = solve(eq6)
print(sol)

# 2 / 3 x - 5 = (6-x) / 3
from sympy import symbols, Eq, solve
x = symbols('x')
eq7 = Eq(2 / 3 * x - 5, (6 - x) / 3)
sol = solve(eq7)
print(sol)