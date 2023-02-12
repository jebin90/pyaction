from fenics import *

# Create a mesh and define the function space
mesh = IntervalMesh(100, 0, 10)
V = FunctionSpace(mesh, 'P', 1)

# Define the boundary conditions
def left_boundary(x, on_boundary):
    return on_boundary and near(x[0], 0)

def right_boundary(x, on_boundary):
    return on_boundary and near(x[0], 10)

bc_left = DirichletBC(V, Constant(0), left_boundary)
bc_right = DirichletBC(V, Constant(1), right_boundary)

# Define the loading
traction = Expression('-x[0]', degree=1)

# Define the variational problem
u = TrialFunction(V)
v = TestFunction(V)
a = dot(grad(u), grad(v))*dx
L = traction*v*ds

# Compute the solution
u = Function(V)
solve(a == L, u, [bc_left, bc_right])

# Plot the solution and save the plot
import matplotlib.pyplot as plt

plt.plot(mesh.coordinates(), u.compute_vertex_values())
plt.xlabel('x')
plt.ylabel('u')
plt.title('Finite Element Solution of a Simple Beam under Mechanical Loads')
plt.savefig('beam_mech.png')
