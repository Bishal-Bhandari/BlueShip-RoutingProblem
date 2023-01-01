import math
import keyboard
import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt
import random
from SelectionCnM import CrossoverMutation
from VarUsed import *

# Value for generation
val_gen = 0


# Generate random obstacle as part of mutation
def obstacle_generation():
    generated_obs_x = []
    generated_obs_y = []
    for o_index in range(number_of_obstacles):
        generated_obs_x.extend(np.random.uniform(for_x_initial, abs_end_x, size=1))
        generated_obs_y.extend(np.random.uniform(for_y_initial, abs_end_y, size=1))
    return generated_obs_x, generated_obs_y


# Random value generator
def randomize():
    return random.uniform(-2, 2), random.choice([1, 2])


# Gives fitness value
def fitness_fun(hol_x, hol_y):
    Total_distance = []
    i_index = 0
    while i_index < len(hol_x):
        Euclidean_distance = []
        for j_index in range(len(hol_x[i_index]) - 1):
            x1, x2 = float(hol_x[i_index][j_index]), float(hol_x[i_index][j_index + 1])
            y1, y2 = float(hol_y[i_index][j_index]), float(hol_y[i_index][j_index + 1])
            Euclidean_distance.append(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        Sum_distance = sum(Euclidean_distance)
        Total_distance.append(Sum_distance)
        i_index += 1
    temp_list_dict = {z[0]: list(z[1:]) for z in zip(Total_distance, hol_x, hol_y)}
    # Selecting the 50% of chromosome from the pool
    fitness_val = Fitness_selection_val * len(temp_list_dict)
    temp_list_dict = dict(sorted(temp_list_dict.items()))
    temp_list_dict = {k: temp_list_dict[k] for k in list(temp_list_dict)[:int(fitness_val)]}
    # Class object
    cross_mutation = CrossoverMutation(temp_list_dict)
    crossover_child_x, crossover_child_y = cross_mutation.crossover()
    return Total_distance, crossover_child_x, crossover_child_y


# Generate points for the chromosomes
def points_chromosome(x_al, y_al):
    val_distance = []

    val_distance_1 = math.sqrt((abs_end_x - (x_al + Graph_plot_value)) ** 2 +
                               (abs_end_y - (y_al + Graph_plot_value)) ** 2)
    val_distance.append(val_distance_1)
    val_distance_2 = math.sqrt((abs_end_x - x_al) ** 2 +
                               (abs_end_y - (y_al + Graph_plot_value)) ** 2)
    val_distance.append(val_distance_2)
    val_distance_3 = math.sqrt((abs_end_x - (x_al - Graph_plot_value)) ** 2 +
                               (abs_end_y - (y_al + Graph_plot_value)) ** 2)
    val_distance.append(val_distance_3)
    val_distance_4 = math.sqrt((abs_end_x - (x_al - Graph_plot_value)) ** 2 +
                               (abs_end_y - y_al) ** 2)
    val_distance.append(val_distance_4)
    val_distance_5 = math.sqrt((abs_end_x - (x_al - Graph_plot_value)) ** 2 +
                               (abs_end_y - (y_al - Graph_plot_value)) ** 2)
    val_distance.append(val_distance_5)
    val_distance_6 = math.sqrt((abs_end_x - x_al) ** 2 +
                               (abs_end_y - (y_al - Graph_plot_value)) ** 2)
    val_distance.append(val_distance_6)
    val_distance_7 = math.sqrt((abs_end_x - (x_al + Graph_plot_value)) ** 2 +
                               (abs_end_y - (y_al - Graph_plot_value)) ** 2)
    val_distance.append(val_distance_7)
    val_distance_8 = math.sqrt((abs_end_x - (x_al + Graph_plot_value)) ** 2 +
                               (abs_end_y - y_al) ** 2)
    val_distance.append(val_distance_8)

    min_val = min(val_distance)
    if min_val == val_distance_1:
        return x_al + Graph_plot_value, y_al + Graph_plot_value
    elif min_val == val_distance_2:
        return x_al, y_al + Graph_plot_value
    elif min_val == val_distance_3:
        return x_al - Graph_plot_value, y_al + Graph_plot_value
    elif min_val == val_distance_4:
        return x_al - Graph_plot_value, y_al
    elif min_val == val_distance_5:
        return x_al - Graph_plot_value, y_al - Graph_plot_value
    elif min_val == val_distance_6:
        return x_al, y_al - Graph_plot_value
    elif min_val == val_distance_7:
        return x_al + Graph_plot_value, y_al - Graph_plot_value
    elif min_val == val_distance_8:
        return x_al + Graph_plot_value, y_al
    else:
        pass


# For chromosome computation
def gene_computation():
    # Initial point for chromosomes
    start_x = [for_x_initial]
    start_y = [for_y_initial]

    # Flush previous values
    hold_x.clear()
    hold_y.clear()
    i = 0
    Check_Condition = True
    # while condition for calculation of chromosome.
    while Check_Condition:

        for idx in range(len(obs_x)):
            for idy in range(len(obs_y)):
                # Check coordinates from chromosome and obstacle, if same change the chromosome coordinate.
                if start_x[i] == obs_x[idy] and start_y[i] == obs_y[idy]:
                    random_val = randomize()
                    if random_val[1] == 1:
                        print("Strike with X")
                        start_x[i] = start_x[i] + 0.5 * random_val[0]
                    else:
                        print("Strike with Y")
                        start_y[i] = start_y[i] + 0.5 * random_val[0]
                else:
                    pass

        # If chromosome's value is bigger then end value, then reroute it towards end point.
        if abs_end_x >= 0 and abs_end_y >= 0:
            if start_x[i] > abs_end_x:
                start_x[i] = start_x[i] - (start_x[i] - abs_end_x)
            elif start_y[i] > abs_end_y:
                start_y[i] = start_y[i] - (start_y[i] - abs_end_y)
            else:
                pass
        else:
            pass

        # Assign the value to the holder for return.
        hold_x.append(start_x[i])
        hold_y.append(start_y[i])

        # If final coordinates of chromosome and end points are same then break the loop.
        if start_x[i] == abs_end_x and start_y[i] == abs_end_y or i == End_loop_limit:
            Check_Condition = False
        else:
            pass

        # Calling the function for shortest route
        a_chromosome, b_chromosome = points_chromosome(start_x[i], start_y[i])
        start_x.append(a_chromosome)
        start_y.append(b_chromosome)
        i += 1

    return hold_x, hold_y


# Plot lines in RT
def plot_grid(dummy):
    global val_gen

    # For obstacles as mutation
    temp_obs_x, temp_obs_y = obstacle_generation()
    obs_x.extend(temp_obs_x)
    obs_y.extend(temp_obs_y)

    Cont_run = True
    i = 1
    while Cont_run:
        hold_xx, hold_yy = gene_computation()
        for_multi_chromosome_x.append(hold_xx.copy())
        for_multi_chromosome_y.append(hold_yy.copy())
        if i == val_iteration:
            Cont_run = False
        else:
            i += 1
            del hold_xx[:]
            del hold_yy[:]

    # Fitness function
    fitness_value, grid_child_x, grid_child_y = fitness_fun(for_multi_chromosome_x, for_multi_chromosome_y)
    fittest_val = min(fitness_value)
    global_fittest_val.append(fittest_val)

    # Add crossover and mutated value to the main gene pool
    len_child_Chromosome = len(grid_child_x)
    for_multi_chromosome_x.extend(grid_child_x)
    for_multi_chromosome_y.extend(grid_child_y)
    print(for_multi_chromosome_x)
    print(for_multi_chromosome_y)
    # Clearing the current figure state
    plt.clf()

    for ite in range((val_iteration + len_child_Chromosome)):
        # Color list for lines to plot
        chromosome_color = random.choice(['blue', 'red', 'black', 'green', 'cyan',
                                          'magenta', 'yellow', 'olive', 'gray', 'brown',
                                          'purple', 'pink', 'teal', 'navy', 'tan',
                                          'maroon', 'steelblue', 'orchid', 'orange', 'tomato',
                                          'chocolate', 'forestgreen', 'slategrey', 'crimson'])
        # Line data holder
        plt.plot(for_multi_chromosome_x[ite],
                 for_multi_chromosome_y[ite],
                 label='Line- ' + str(ite + 1),
                 color=chromosome_color)

    # Plotting points for obstacle
    plt.scatter(obs_x,
                obs_y,
                label="Obstacles",
                color=['green'],
                s=5)
    # Removing the added obstacles
    del obs_x[-number_of_obstacles:]
    del obs_y[-number_of_obstacles:]

    # For end point of line
    plt.scatter(end_x,
                end_y,
                color=['Black'])
    # For start point of line
    plt.scatter(for_multi_chromosome_x[0][0],
                for_multi_chromosome_y[0][0],
                color=['Black'])
    plt.legend()
    # Size of a field plot
    plt.plot(sfield_x, sfield_y, c='white')
    plt.plot(efield_x, efield_y, c='white')

    # Naming the x axis and including the info of generations
    plt.xlabel('x - axis' + '\nGeneration: ' + str(val_gen) +
               '\n Fittest Chromosome per gen: ' + str(fittest_val) +
               '   Fittest Chromosome: ' + str(min(global_fittest_val)))
    val_gen = val_gen + 1

    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('Blue Ship Route')

    # Display the graph
    plt.grid(True, which='major')

    for_multi_chromosome_x.clear()
    for_multi_chromosome_y.clear()

    # Exit the loop
    keyboard.add_hotkey('q', lambda: quit())


# THE MAIN PART
anime = animation.FuncAnimation(plt.gcf(),
                                plot_grid,
                                interval=1000,
                                frames=5)
plt.show()
