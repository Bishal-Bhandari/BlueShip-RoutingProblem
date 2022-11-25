import matplotlib.pyplot as plt
import random
import numpy as np

Check_Condition = True
# Plotting field
sfield_x = [-10]
sfield_y = [-10]
efield_x = [15]
efield_y = [15]

# Initial point
start_x = []
start_y = []

# Goal point
end_x = [8]
end_y = [8]

# Obstacles
obs_x = [-5, 1, 8, 4, 5, 6, 8, 4, 8, 5, 7, 8, 7, 2, 2, 4, 6]
obs_y = [-5, 5, 8, 4, 4, 2, 3, 7, 8, 2, 2, 8, 1, 8, 7, 3, 4]

# plotting the points
hold_x = []
hold_y = []


def randomize():
    return random.uniform(-1, 1), random.choice([1, 2])


def gene_computation():
    global Check_Condition
    i, j = 0, 0

    while Check_Condition:
        start_x.append(i)
        start_y.append(j)
        for idx in range(len(obs_x)):
            if start_x[i] == obs_x[idx] and start_y[i] == obs_y[idx]:
                random_val = randomize()
                if random_val[1] == 1:
                    start_x[i] = start_x[i] + 1.5 * random_val[0]
                else:
                    start_y[i] = start_y[j] + 1.5 * random_val[0]

        if start_x[i] > end_x[0] or start_y[j] > end_y[0]:
            start_x[i] = start_x[i] - (start_x[i] - end_x[0])
            start_y[j] = start_y[j] - (start_x[j] - end_x[0])

        hold_x.append(start_x[i])
        hold_y.append(start_y[i])

        if start_x[i] == end_x[0] or start_y[j] == end_y[0]:
            Check_Condition = False
            return hold_x, hold_y

        i = i + 1
        j = j + 1


def plot_grid():
    hold_x, hold_y = gene_computation()
    print(f'x{hold_x}-y{hold_y}')
    # Max field plot
    plt.plot(sfield_x, sfield_y, c='white')
    plt.plot(efield_x, efield_y, c='white')
    plt.plot(hold_x, hold_y, c='black')

    # Plotting points for scatter
    plt.scatter(obs_x, obs_y, label="stars", color=['red'])
    # For goal point
    plt.scatter(end_x, end_y, color=['Black'])

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('Blue Ship Route')

    # Display
    plt.show()


plot_grid()
