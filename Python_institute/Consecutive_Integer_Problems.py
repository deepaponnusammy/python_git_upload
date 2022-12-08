# The sum of consecutive integer is 80.
# what is the smallest of these integers?
from sympy import symbols, Eq, solve
x = symbols('x')
eq1 = Eq(x+(x+1)+(x+2)+(x+3)+(x+4), 80)
sol = solve(eq1)
print(sol)
# Solving Middle number
eq2 = Eq((x-2)+(x-1)+x+(x+1)+(x+2), 80)
sol = solve(eq2)
print(sol)

# The sum of three consecutive odd numbers is 63. Find the numbers.
from sympy import symbols, Eq, solve
x = symbols('x')
eq1 = Eq(x+(x+2)+(x+4), 63)
sol = solve(eq1)
print(sol)

# the sum of four consecutive odd integers is 184
from sympy import symbols, Eq, solve
x = symbols('x')
eq1 = Eq(x+(x+2)+(x+4)+(x+6), 184)
sol = solve(eq1)
print(sol)

# the sum of three consecutive integers is 81, then what is the product of the first and the third integer?
from sympy import symbols, Eq, solve
x = symbols('x')
eq1 = Eq(x+(x+1)+(x+2), 81)
sol = solve(eq1)
print(sol)
