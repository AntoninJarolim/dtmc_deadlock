import stormpy

# Set the environment
environment = stormpy.Environment()
# environment.solver_environment.set_linear_equation_solver_type(stormpy.EquationSolverType.native)
# ^ uncomment this to see the difference

# Parse program
prism_program = stormpy.parse_prism_program("dtmc.templ")
dtmc = stormpy.build_model(prism_program)

# Parse properties
properties = stormpy.parse_properties('LRA=? [ "goal"]')
prop = properties[0]
result = stormpy.model_checking(dtmc, prop, environment=environment)
print(result.at(0))
