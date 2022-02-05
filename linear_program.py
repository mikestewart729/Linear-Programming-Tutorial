# linear_program.py

from scipy.optimize import linprog

# Maximize z = x + 2y by minimizing -z = -x -2y
#obj = [-1, -2]

# Define the toy problem inequality LHS's
#lhs_ineq = [[2, 1],
#            [-4, 5],
#            [1, -2]]

# Define the toy problem inequality RHS's
#rhs_ineq = [20,
#            10,
#            2]

# Add in the toy problem equality constraints
#lhs_eq = [[-1, 5]]
#rhs_eq = [15]

# Define the bounds for x and y
#bnd = [(0, float("inf")),
#       (0, float("inf"))]

# Instantiate the optimizer and solve
#opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
#              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
#              method="revised simplex")

# Display the output
#print(opt)

# Now look at the example problem given in the tutorial
# Maximize: 20 x1 + 12 x2 + 40 x3 + 25 x4
# by minimizing its negative
obj = [-20, -12, -40, -25]

# Subject to
# x1 + x2 + x3 + x4 <= 50 (can only make 50 units in a day)
# 3 x1 + 2 x2 + x3 <= 100 (only have 100 units of material A)
# x2 + 2 x3 + 3 x4 <= 90 (only have 90 units of material B)
# all xi'x must be positive
lhs_ineq = [
    [1, 1, 1, 1], #manpower
    [3, 2, 1, 0], #material A
    [0, 1, 2, 3]  #material B
]

rhs_ineq = [ 50, #manpower
            100, #material A
             90]  #material B

# optimize it!
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method='revised simplex')
print(opt)