import random

import numpy as np


def mutation(x_value, y_value):
    for m_index in range(len(x_value)):
        random_val = int(np.random.uniform(1, (len(x_value) - 1)))
        w_index = 0
        while w_index < len(x_value[m_index]):
            if w_index == random_val:
                temp_x_value, temp_y_value = x_value[m_index][random_val], y_value[m_index][random_val]
                x_value[m_index][random_val], y_value[m_index][random_val] = \
                    temp_x_value + random.choice([0.25, -0.25]), temp_y_value + random.choice([0.25, -0.25])
            w_index += 1
    return x_value, y_value


class CrossoverMutation:
    def __init__(self, selected_chromosome):
        self.selected_chromosome = selected_chromosome
        self.dict_value = 0
        self.min_range_Crossover = 5  # Range for crossover
        self.crossover_max_len = []
        self.temp_x = []
        self.temp_y = []
        self.child_x = []
        self.child_y = []
        self.crossover_int = []

    def crossover(self):
        dict_value = list(self.selected_chromosome.values())
        for i in range(len(self.selected_chromosome)):
            self.temp_x.append(dict_value[i][0])
            self.temp_y.append(dict_value[i][1])
            self.crossover_max_len.append(len(self.temp_x[i]))

        for x_index in range(len(self.selected_chromosome)):
            self.crossover_int.append(np.random.uniform(
                self.min_range_Crossover,
                self.crossover_max_len[x_index],
                size=1))

        i_index = 0
        while i_index < (len(self.temp_x) - 1):
            temp_child_x = []
            temp_child_y = []
            for j_index in range(min(len(self.temp_x[i_index]), len(self.temp_x[i_index + 1]))):
                if self.crossover_int[i_index] <= j_index <= self.crossover_max_len[i_index]:
                    temp_child_x.insert(j_index, self.temp_x[i_index + 1][j_index])
                    temp_child_y.insert(j_index, self.temp_y[i_index + 1][j_index])
                else:
                    temp_child_x.insert(j_index, self.temp_x[i_index][j_index])
                    temp_child_y.insert(j_index, self.temp_y[i_index][j_index])
            self.child_x.append(temp_child_x)
            self.child_y.append(temp_child_y)
            i_index += 1
        self.child_x, self.child_y = mutation(self.child_x, self.child_y)
        return self.child_x, self.child_y
