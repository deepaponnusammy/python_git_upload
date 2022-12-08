# 4x+2=0
from sympy import symbols, Eq, solve
x = symbols('x')
eq1 = Eq(4*x + 2, 0)
print(eq1)
sol = solve(eq1)
print(sol)

# 2y - x = 5
# subtract the right hand side of the equation from the left hand side of the equation first.
# 2y -x -5 = 0
x, y = symbols('x y')
eq1 = Eq(2*y - x - 5, 0)
print(eq1)
sol = solve(eq1)
print(sol)
x, y = symbols('x y')
eq2 = Eq(2*y - x, 5)
print(eq2)
sol = solve(eq2)
print(sol)
x, y, z = symbols('x y z')
eq3 = Eq(2*y - x - 5)
eq4 = eq3.subs(x,z)
print(eq4)

#x − 4 − 2 = 0
from sympy import symbols, solve
x = symbols('x')
expr = x-4-2
sol = solve(expr)
print(sol)

from sympy import symbols, Eq, solve
y = symbols('y')
eq1 = Eq(y + 3 + 8, 0)
sol = solve(eq1)
print(sol)

#x^2 − 5x + 6 = 0
from sympy import symbols, Eq, solve
y = symbols('x')
eq1 = Eq(x**2 -5*x + 6, 0)
sol = solve(eq1)
print(sol)

from sympy import symbols, Eq, solve
y = symbols('x')
eq1 = Eq(x**2 -5*x + 6, 0)
sol = solve(eq1, dict=True)
print(sol)

# importing library sympy
from sympy import symbols, Eq, solve
# defining symbols used in equations
# or unknown variables
x, y = symbols('x,y')
# defining equations
eq1 = Eq((x+y), 1)
print("Equation 1:")
print(eq1)
eq2 = Eq((x-y), 1)
print("Equation 2")
print(eq2)
# solving the equation
print("Values of 2 unknown variable are as follows:")
print(solve((eq1, eq2), (x, y)))


# defining symbols used in equations
# or unknown variables
x, y, z = symbols('x,y,z')
# defining equations
eq1 = Eq((x + y + z), 1)
print("Equation 1:")
print(eq1)
eq2 = Eq((x - y + 2 * z), 1)
print("Equation 2")
print(eq2)
eq3 = Eq((2 * x - y + 2 * z), 1)
print("Equation 3")
# solving the equation and printing the
# value of unknown variables
print("Values of 3 unknown variable are as follows:")
print(solve((eq1, eq2, eq3), (x, y, z)))


# x + y − 5 = 0
# x - y + 3 = 0
from sympy import symbols, Eq, solve
x, y = symbols('x y')
eq1 = Eq(x + y - 5, 0)
eq2 = Eq(x - y + 3, 0)
solve((eq1,eq2), (x, y))
sol_dict = solve((eq1,eq2), (x, y))
print(f'x = {sol_dict[x]}')
print(f'y = {sol_dict[y]}')



#A weight of 22 lbs is hung from a ring. The ring is supported by two cords.
# The first cord, cord CE, is 30 degrees above the horizontal and to the right.
# The second cord, cord BD, is 45 degrees to the left and above the horizontal.
import numpy as np
from sympy import symbols, Eq, solve
Tce, Tbd = symbols('Tce Tbd')
eq1=Eq(Tce*np.cos(np.radians(30)) - Tbd*np.cos(np.radians(45)), 0)
print(eq1)
eq2=Eq(Tce*np.sin(np.radians(30)) + Tbd*np.sin(np.radians(45))-22, 0)
print(eq2)
solve((eq1,eq2),(Tce, Tbd))
sol_dict = solve((eq1,eq2),(Tce, Tbd))
print(f'Tce = {sol_dict[Tce]}')
print(f'Tce = {sol_dict[Tbd]}')

# OR

w, Tce, Tbd = symbols('w, Tab, Tac')
eq1=Eq(Tce*np.cos(np.radians(30)) - Tbd*np.cos(np.radians(45)), 0)
eq2=Eq(Tce*np.sin(np.radians(30)) + Tbd*np.sin(np.radians(45))-w, 0)
solve((eq1,eq2),(Tce,Tbd))
sol_dict = solve((eq1,eq2),(Tce, Tbd))
print(f'Tce = {sol_dict[Tce]}')
print(f'Tce = {sol_dict[Tbd]}')
