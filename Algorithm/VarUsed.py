# For Pathfinder
# Plotting field
sfield_x = [-5]
sfield_y = [-5]
efield_x = [15]
efield_y = [15]
# Initial point for chromosomes
for_x_initial = 2
for_y_initial = 2
# Goal point for chromosomes
end_x = [15]
end_y = [8]
abs_end_x = end_x[0]
abs_end_y = end_y[0]
# Obstacles
obs_x = [-5, 1, 3, 2, 2.5, 3, 4, 8, 4, 5, 6, 8, 4, 8, 5, 7, 8, 7, 2, 2, 4, 6, 9, 12, 15, 8, 7, 8, 4, 8, 5, 7]
obs_y = [-5, 5, 7, 5, 5, 5, 5, 8, 4, 4, 2, 3, 7, 8, 2, 2, 8, 1, 8, 7, 3, 4, 9, 8, 15, 6, 4, 7, 5, 5, 5, 5]
# Number of obstacles
number_of_obstacles = 15
# plotting the points for chromosomes
hold_x = []
hold_y = []
# list of list for chromosome
for_multi_chromosome_x = []
for_multi_chromosome_y = []
# Value for iteration
val_iteration = 10
# For global lowest value of distance
global_fittest_val = []
# Number of chromosome to select from pool
Fitness_selection_val = 1
# Loop limit for end condition
End_loop_limit = 100
# Added value from neighbourhood search point
Graph_plot_value = 1
# Global max search range
max_x = 15
max_y = 15
min_x = 0
min_y = 0
