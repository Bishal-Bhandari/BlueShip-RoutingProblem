import timeit
from Algorithm.pathfinder import *
import keyboard
import numpy as np
import pandas
from matplotlib import animation
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import random
from Algorithm.VarUsed import *

# Value for generation
val_gen = 0


# Plot lines in RT
def plot_grid(dummy):
    start = timeit.default_timer()
    global val_gen
    # To clear previous value in the list
    for_multi_chromosome_x.clear()
    for_multi_chromosome_y.clear()

    # For obstacles as mutation
    excel_data_df = pandas.read_excel('SmallData.xlsx', sheet_name='Sheet1')  # Read from file
    obs_lat = excel_data_df['Lat'].tolist()
    obs_lon = excel_data_df['Lon'].tolist()
    # Add value from file to existing list of obstacle
    obs_x.extend(obs_lon)
    obs_y.extend(obs_lat)
    # Call value from function
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

    # print(for_multi_chromosome_x)
    # print(for_multi_chromosome_y)

    # Length of each route in Kilometer
    distance_route = route_length(for_multi_chromosome_x, for_multi_chromosome_y)
    print("Distance in Kilometer:", distance_route)

    # Clearing the current figure state
    plt.clf()

    # Giving details and view size for Basemap
    map_basemap = Basemap(projection='mill',
                          llcrnrlat=10,
                          urcrnrlat=60,
                          llcrnrlon=-80,
                          urcrnrlon=10,
                          resolution='l')

    # Setting up for the mapping points
    map_basemap.drawcoastlines()
    map_basemap.drawparallels(np.arange(-90, 90, 10), labels=[0, 1, 0, 1])
    map_basemap.drawmeridians(np.arange(-180, 180, 10), labels=[0, 0, 0, 1])

    for ite in range((val_iteration + len_child_Chromosome)):
        # Color list for lines to plot
        chromosome_color = random.choice(['blue', 'red', 'black', 'green', 'cyan',
                                          'magenta', 'yellow', 'olive', 'gray', 'brown',
                                          'purple', 'pink', 'teal', 'navy', 'tan',
                                          'maroon', 'steelblue', 'orchid', 'orange', 'tomato',
                                          'chocolate', 'forestgreen', 'slategrey', 'crimson'])
        # Line data holder
        temp_x, temp_y = map_basemap(for_multi_chromosome_x[ite], for_multi_chromosome_y[ite])
        map_basemap.plot(temp_x,
                         temp_y,
                         color=chromosome_color)

    # Plotting points for obstacle
    for_temp_obs_x, for_temp_obs_y = map_basemap(obs_x, obs_y)
    map_basemap.scatter(for_temp_obs_x,
                        for_temp_obs_y,
                        label="Obstacles",
                        color=['green'],
                        s=3)

    # Removing the newly added obstacles
    del obs_x[-number_of_obstacles:]
    del obs_y[-number_of_obstacles:]
    # obs_x.clear()
    # obs_y.clear()

    # For end point of line
    temp_end_x, temp_end_y = map_basemap(end_x, end_y)
    map_basemap.scatter(temp_end_x,
                        temp_end_y,
                        label='Number of Population- ' + str(len(for_multi_chromosome_x) + 1),  # For number of
                        # population
                        color=['Black'])
    # For start point of line
    temp_start_x, temp_start_y = map_basemap(for_multi_chromosome_x[0][0], for_multi_chromosome_y[0][0])
    map_basemap.scatter(temp_start_x,
                        temp_start_y,
                        color=['Black'])

    # Naming the x axis and including the info of generations
    plt.xlabel('\nLatitude' + '\nGeneration: ' + str(val_gen) +
               '\n Fittest Chromosome per gen: ' + str(fittest_val) +
               '   Fittest Chromosome: ' + str(min(global_fittest_val)))
    val_gen = val_gen + 1

    # Naming the y axis
    plt.ylabel('Longitude')

    # Adding the color to the map
    map_basemap.drawmapboundary(fill_color='aqua')
    map_basemap.fillcontinents(color='coral', lake_color='aqua')

    # Giving a title to the graph
    plt.title('Blue Ship Route')

    # Display line details
    plt.legend()

    # Exit the loop
    keyboard.add_hotkey('q', lambda: quit())

    stop = timeit.default_timer()
    execution_time = stop - start
    print("Program Executed in " + str(execution_time))  # It returns time in seconds


# # THE MAIN PART
anime = animation.FuncAnimation(plt.gcf(),
                                plot_grid,
                                interval=1000,
                                frames=5)

plt.tight_layout()
plt.show()
