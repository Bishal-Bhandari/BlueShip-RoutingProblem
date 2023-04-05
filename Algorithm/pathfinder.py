import math
import numpy as np
import random
from mpl_toolkits.basemap import Basemap
from Algorithm.SelectionCnM import CrossoverMutation
from Algorithm.VarUsed import *
import mpu
from openpyxl import load_workbook
import pandas as pd


# Mapping the projection for the map
# map_projection = Basemap(projection='mill',
#                          llcrnrlat=10,
#                          urcrnrlat=60,
#                          llcrnrlon=-80,
#                          urcrnrlon=10,
#                          resolution='l')


# Generate random obstacle as part of mutation
def obstacle_generation():
    generated_obs_x = []
    generated_obs_y = []
    for o_index in range(number_of_obstacles):
        generated_obs_x.extend(np.random.uniform(for_x_initial, abs_end_x, size=1))
        generated_obs_y.extend(np.random.uniform(for_y_initial, abs_end_y, size=1))
    return generated_obs_x, generated_obs_y


# Calculate the length of each route
def route_length(cal_x, cal_y):
    dist_route = []
    for i_cal in range(len(cal_x)):
        for j_cal in range(len(cal_y) - 1):
            dist = mpu.haversine_distance((cal_x[i_cal][j_cal], cal_y[i_cal][j_cal]),
                                          (cal_x[i_cal][j_cal + 1], cal_y[i_cal][j_cal + 1]))
        dist_route.append(dist)
    # Save some detail in JASON file format
    min_length = min(dist_route)
    time_taken = min_length / Ship_Speed
    fuel_used = (Fuel_used / 24) * time_taken
    ships_detail = {
        'Length_route': min_length,
        'Time': time_taken,
        'Fuel_Consumed': fuel_used
    }
    df = pd.DataFrame([ships_detail])
    # read  file content
    reader = pd.read_excel('save_routes_info.xlsx')
    # create writer object
    writer = pd.ExcelWriter('save_routes_info.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")
    # append new dataframe
    df.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)
    # close file
    writer.close()

    return dist_route


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


# # Generating the points if land is on the way of route
# def avoid_land(x_pt, y_pt):
#     value_distance = []
#     x_val = []
#     y_val = []
#
#     value_distance_1 = math.sqrt((abs_end_x - (x_pt + Graph_plot_value)) ** 2 +
#                                  (abs_end_y - (y_pt + Graph_plot_value)) ** 2)
#     value_distance.append(value_distance_1)
#     x_val.append(x_pt + Graph_plot_value), y_val.append(y_pt + Graph_plot_value)
#
#     val_distance_2 = math.sqrt((abs_end_x - x_pt) ** 2 +
#                                (abs_end_y - (y_pt + Graph_plot_value)) ** 2)
#     value_distance.append(val_distance_2)
#     x_val.append(x_pt), y_val.append(y_pt + Graph_plot_value)
#
#     value_distance_3 = math.sqrt((abs_end_x - (x_pt - Graph_plot_value)) ** 2 +
#                                  (abs_end_y - (y_pt + Graph_plot_value)) ** 2)
#     value_distance.append(value_distance_3)
#     x_val.append(x_pt - Graph_plot_value), y_val.append(y_pt + Graph_plot_value)
#
#     value_distance_4 = math.sqrt((abs_end_x - (x_pt - Graph_plot_value)) ** 2 +
#                                  (abs_end_y - y_pt) ** 2)
#     value_distance.append(value_distance_4)
#     x_val.append(x_pt - Graph_plot_value), y_val.append(y_pt)
#
#     val_distance_5 = math.sqrt((abs_end_x - (x_pt - Graph_plot_value)) ** 2 +
#                                (abs_end_y - (y_pt - Graph_plot_value)) ** 2)
#     value_distance.append(val_distance_5)
#     x_val.append(x_pt - Graph_plot_value), y_val.append(y_pt - Graph_plot_value)
#
#     value_distance_6 = math.sqrt((abs_end_x - x_pt) ** 2 +
#                                  (abs_end_y - (y_pt - Graph_plot_value)) ** 2)
#     value_distance.append(value_distance_6)
#     x_val.append(x_pt), y_val.append(y_pt - Graph_plot_value)
#
#     value_distance_7 = math.sqrt((abs_end_x - (x_pt + Graph_plot_value)) ** 2 +
#                                  (abs_end_y - (y_pt - Graph_plot_value)) ** 2)
#     value_distance.append(value_distance_7)
#     x_val.append(x_pt + Graph_plot_value), y_val.append(y_pt - Graph_plot_value)
#
#     value_distance_8 = math.sqrt((abs_end_x - (x_pt + Graph_plot_value)) ** 2 +
#                                  (abs_end_y - y_pt) ** 2)
#     value_distance.append(value_distance_8)
#     x_val.append(x_pt + Graph_plot_value), y_val.append(y_pt)
#     for while_index in range(len(value_distance)):
#         print('Inside the basemap function.')
#         lon, lat = (x_val[while_index], y_val[while_index])  # test coordinates
#         xpt, ypt = map_projection(lon, lat)  # convert to projection map
#         value = map_projection.is_land(xpt, ypt)  # Checking if point is on land or not
#         if value:
#             x_val.pop(while_index), y_val.pop(while_index), value_distance.pop(while_index)
#         else:
#             min_pos = value_distance.index(min(value_distance))
#             return x_val[min_pos], y_val[min_pos]


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

                # lon, lat = (start_x[i], start_y[i])  # test coordinates
                # xpt, ypt = map_projection(lon, lat)  # convert to projection map
                # value = map_projection.is_land(xpt, ypt)  # Checking if point is on land or not

                # Check coordinates from chromosome and obstacle, if same change the chromosome coordinate.
                if start_x[i] == obs_x[idy] and start_y[i] == obs_y[idy]:
                    random_val = randomize()
                    if random_val[1] == 1:
                        start_x[i] = start_x[i] + (0.5 * random_val[0])
                        print("Strike with Obs(X). ", start_x[i], start_x[i])
                    else:
                        start_y[i] = start_y[i] + (0.5 * random_val[0])
                        print("Strike with Obs(Y). ", start_y[i], start_y[i])
                # elif value:
                #     start_x[i], start_y[i] = avoid_land(start_x[i], start_y[i])
                #     print("Strike with land.", start_x[i], start_y[i], idy)
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
        if start_x[i] >= abs_end_x and start_y[i] >= abs_end_y or i == End_loop_limit:
            Check_Condition = False
        else:
            pass

        # Calling the function for next point calculation
        a_chromosome, b_chromosome = points_chromosome(start_x[i], start_y[i])
        start_x.append(a_chromosome)
        start_y.append(b_chromosome)
        i += 1

    return hold_x, hold_y
