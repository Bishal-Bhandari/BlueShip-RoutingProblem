
# Initial point for chromosomes
for_x_initial = -9.840600  # Longitude
for_y_initial = 30.999678  # Latitude
# Goal point for chromosomes
end_x = [-76.430303]  # Longitude
end_y = [35.085791]  # Latitude
abs_end_x = end_x[0]
abs_end_y = end_y[0]
# Obstacles
obs_x = [-18.957707699807273, -19.957707699807273, -57.38221644849669, -58.38221644849669, -15.15, -20,
         -16.840600000000002, -10.8406, -11.8406, -12.8406, -13.8406, -14.8406, -15.8406, -16.840600000000002]
obs_y = [34.999678, 34.999678, 34.999678, 34.999678, 32.56, 35, 34.999678, 31.999678, 32.999678, 33.999678, 34.999678,
         34.999678, 34.999678, 34.63786600808995]
# Number of new randomly generated obstacles
number_of_obstacles = 20
# plotting the points for chromosomes
hold_x = []
hold_y = []
# list of list for chromosome
for_multi_chromosome_x = []
for_multi_chromosome_y = []
# Value for iteration
val_iteration = 5
# For global lowest value of distance
global_fittest_val = []
# Number of chromosome to select from pool
Fitness_selection_val = 1
# Loop limit for end condition
End_loop_limit = 150
# Added value from neighbourhood search point
Graph_plot_value = 0.5

