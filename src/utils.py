import numpy as np


def calculate_euclidean_distance(subject_x, subject_y):
    summation = 0
    for index in range(0, len(subject_x)):
        summation += (float(subject_x[index]) - float(subject_y[index])) ** 2
    return round(summation ** (1 / 2), 3)


def calculate_manhattan_distance(subject_x, subject_y):
    summation = 0
    for index in range(0, len(subject_x)):
        summation += abs(float(subject_x[index]) - float(subject_y[index]))
    return round(summation, 3)


def calculate_mean(subjects):
    np.set_printoptions(precision=3, suppress=True)
    subjects = np.array(subjects)
    return np.mean(subjects, axis=0)
