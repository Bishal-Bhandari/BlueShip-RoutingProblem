import math
import matplotlib.pyplot as plt
import random

# Plotting field
sfield_x = [-10]
sfield_y = [-10]
efield_x = [15]
efield_y = [15]

# Goal point for chromosomes
end_x = [5]
end_y = [10]

# Obstacles
obs_x = [-5, 1, 3, 2, 2.5, 3, 4, 8, 4, 5, 6, 8, 4, 8, 5, 7, 8, 7, 2, 2, 4, 6, 9]
obs_y = [-5, 5, 7, 5, 5, 5, 5, 8, 4, 4, 2, 3, 7, 8, 2, 2, 8, 1, 8, 7, 3, 4, 9]

# plotting the points for chromosomes
hold_x = []
hold_y = []

# list of list for chromosome
for_multi_chromosome_x = []
for_multi_chromosome_y = []

# Value for iteration
val_iteration = 10


# Random value generator
def randomize():
    return random.uniform(-2, 2), random.choice([1, 2])


# Gives fitness value
def fitness_fun(hol_x, hol_y):
    Euclidean_distance = math.dist(hol_x, hol_y)
    return True


# Generate points for the chromosomes
def points_chromosome(x_al, y_al):
    val_distance = []

    val_distance_1 = math.sqrt((end_x[0] - (x_al + 1)) ** 2 + (end_y[0] - (y_al + 1)) ** 2)
    val_distance.append(val_distance_1)
    val_distance_2 = math.sqrt((end_x[0] - x_al) ** 2 + (end_y[0] - (y_al + 1)) ** 2)
    val_distance.append(val_distance_2)
    val_distance_3 = math.sqrt((end_x[0] - (x_al - 1)) ** 2 + (end_y[0] - (y_al + 1)) ** 2)
    val_distance.append(val_distance_3)
    val_distance_4 = math.sqrt((end_x[0] - (x_al - 1)) ** 2 + (end_y[0] - y_al) ** 2)
    val_distance.append(val_distance_4)
    val_distance_5 = math.sqrt((end_x[0] - (x_al - 1)) ** 2 + (end_y[0] - (y_al - 1)) ** 2)
    val_distance.append(val_distance_5)
    val_distance_6 = math.sqrt((end_x[0] - x_al) ** 2 + (end_y[0] - (y_al - 1)) ** 2)
    val_distance.append(val_distance_6)
    val_distance_7 = math.sqrt((end_x[0] - (x_al + 1)) ** 2 + (end_y[0] - (y_al - 1)) ** 2)
    val_distance.append(val_distance_7)
    val_distance_8 = math.sqrt((end_x[0] - (x_al + 1)) ** 2 + (end_y[0] - y_al) ** 2)
    val_distance.append(val_distance_8)

    min_val = min(val_distance)

    if min_val == val_distance_1:
        # print(f'x1-{x_al + 0.5},y{y_al + 0.5}')
        return x_al + 1, y_al + 1
    elif min_val == val_distance_2:
        # print(f'x2-{x_al},y{y_al + 0.5}')
        return x_al, y_al + 1
    elif min_val == val_distance_3:
        # print(f'x3-{x_al - 0.5},y{y_al + 0.5}')
        return x_al - 1, y_al + 1
    elif min_val == val_distance_4:
        # print(f'x4-{x_al - 0.5},y{y_al}')
        return x_al - 1, y_al
    elif min_val == val_distance_5:
        # print(f'x5-{x_al - 0.5},y{y_al - 0.5}')
        return x_al - 1, y_al - 1
    elif min_val == val_distance_6:
        # print(f'x6-{x_al},y{y_al - 0.5}')
        return x_al, y_al - 1
    elif min_val == val_distance_7:
        # print(f'x7-{x_al + 0.5},y{y_al - 0.5}')
        return x_al + 1, y_al - 1
    elif min_val == val_distance_8:
        # print(f'x-{x_al + 0.5},y{y_al}')
        return x_al + 1, y_al
    else:
        pass


def gene_computation():
    # Initial point for chromosomes
    start_x = [0]
    start_y = [0]
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
                        start_x[i] = start_x[i] + 0.5 * random_val[0]
                    else:
                        start_y[i] = start_y[i] + 1.5 * random_val[0]
                else:
                    pass

        # If chromosome's value is bigger then end value, then reroute it towards end point.
        if start_x[i] > end_x[0]:
            start_x[i] = start_x[i] - (start_x[i] - end_x[0])
        elif start_y[i] > end_y[0]:
            start_y[i] = start_y[i] - (start_y[i] - end_y[0])
        else:
            pass

        # Assign the value to the holder.
        hold_x.append(start_x[i])
        hold_y.append(start_y[i])

        # If final coordinates of chromosome and end points are same then break the loop.
        if start_x[i] == end_x[0] and start_y[i] == end_y[0] or i == 100:
            Check_Condition = False
        else:
            pass

        # Calling the function for shortest route
        a_chromosome, b_chromosome = points_chromosome(start_x[i], start_y[i])
        start_x.append(a_chromosome)
        start_y.append(b_chromosome)
        i += 1

    return hold_x, hold_y


def plot_grid():
    Cont_run = True
    i = 0
    while Cont_run:
        hold_xx, hold_yy = gene_computation()
        for_multi_chromosome_x.append(hold_xx)
        for_multi_chromosome_y.append(hold_yy)
        if i == val_iteration:
            Cont_run = False
        else:
            i += 1

    # fitness_value = fitness_fun(hold_x, hold_y)
    print(f'ForX-{for_multi_chromosome_x},\n ForY--{for_multi_chromosome_y}')
    # Size of a field plot
    plt.plot(sfield_x, sfield_y, c='white')
    plt.plot(efield_x, efield_y, c='white')

    chromosome_color = ['blue', 'red', 'black', 'blue', 'red', 'black', 'blue', 'red', 'black', 'blue', 'red', 'black']
    for ite in range(val_iteration):
        # Line data holder
        plt.plot(for_multi_chromosome_x[ite], for_multi_chromosome_y[ite], color='black')

    # Plotting points for obstacle
    plt.scatter(obs_x, obs_y, label="stars", color=['red'])
    # For end point of line
    plt.scatter(end_x, end_y, color=['Black'])
    # For start point of line
    plt.scatter(0, 0, color=['Black'])

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('Blue Ship Route')

    # Display the graph
    plt.grid(True, which='major')
    plt.show()


plot_grid()
