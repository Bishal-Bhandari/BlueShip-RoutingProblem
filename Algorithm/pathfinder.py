import math
import numpy as np
import random
from mpl_toolkits.basemap import Basemap

from Algorithm.SelectionCnM import CrossoverMutation
from Algorithm.VarUsed import *

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

    # Mapping the projection for the map
    map_projection = Basemap(projection='mill',
                             llcrnrlat=10,
                             urcrnrlat=60,
                             llcrnrlon=-80,
                             urcrnrlon=10,
                             resolution='l')

    # Flush previous values
    hold_x.clear()
    hold_y.clear()
    i = 0
    Check_Condition = True
    # while condition for calculation of chromosome.
    while Check_Condition:

        for idx in range(len(obs_x)):
            for idy in range(len(obs_y)):
                lon, lat = (start_x[i], start_y[i])  # test coordinates
                xpt, ypt = map_projection(lon, lat)  # convert to projection map
                value = map_projection.is_land(xpt, ypt)  # Checking if point is on land or not
                # Check coordinates from chromosome and obstacle, if same change the chromosome coordinate.
                if start_x[i] == obs_x[idy] and start_y[i] == obs_y[idy]:
                    random_val = randomize()
                    if random_val[1] == 1:
                        print("Strike with X", start_x[i], start_x[i - 1])
                        start_x[i] = start_x[i - 1] + 0.5 * random_val[0]
                    else:
                        print("Strike with Y", start_y[i], start_y[i - 1])
                        start_y[i] = start_y[i - 1] + 0.5 * random_val[0]
                elif value:
                    random_val = randomize()
                    if random_val[1] == 1:
                        print("On land - X", start_x[i], start_x[i - 1])
                        start_x[i] = start_x[i - 1] + 0.5 * random_val[0]
                    else:
                        print("On land - Y", start_y[i], start_y[i - 1])
                        start_y[i] = start_y[i - 1] + 0.5 * random_val[0]
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
