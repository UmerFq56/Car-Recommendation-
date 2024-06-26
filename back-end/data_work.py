"""CSC111 Winter 2024 Project: Car Recommender System

Module Description
==================
This module contains functions for preprocessing car data retrieved from a CSV file. It includes
functions for normalizing numerical data, one-hot encoding categorical data and removing
irrelevant columns. The processed data is used in the Car Recommender System to analyze
and recommend cars based on user preferences.

Copyright and Usage Information
===============================



This file is Copyright (c) 2024 CSC111 Students Winter (Yaseen Sadat, Muhammad Aneeq, Umer Farooqui, Zarif Ali
"""
import csv


def create_full_data(dataset: str) -> tuple:
    """
    Read car data from a CSV file and return a tuple containing raw car attributes and one-hot encoded features.

    Preconditions:
    - dataset is the path to a CSV file that is properly formatted with car attributes.
    - The CSV file must include headers.
    - The car type must be the 6th column and engine type must be the 2nd column in the CSV.
    """

    is_sedan = []
    is_suv = []
    is_sports = []
    is_luxury = []

    is_v4 = []
    is_v6 = []
    is_v8 = []
    is_v12 = []
    is_electric = []

    one_hot_encoded_list = [is_sedan, is_suv, is_sports, is_luxury, is_v4, is_v6, is_v8, is_v12, is_electric]

    full_list = []

    with open(dataset, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[5] == 'Sedan':
                is_sedan.append(1)
                is_suv.append(0)
                is_sports.append(0)
                is_luxury.append(0)
            elif row[5] == 'SUV':
                is_sedan.append(0)
                is_suv.append(1)
                is_sports.append(0)
                is_luxury.append(0)
            elif row[5] == 'Sports':
                is_sedan.append(0)
                is_suv.append(0)
                is_sports.append(1)
                is_luxury.append(0)
            elif row[5] == 'Luxury':
                is_sedan.append(0)
                is_suv.append(0)
                is_sports.append(0)
                is_luxury.append(1)
            else:
                is_sedan.append(0)
                is_suv.append(0)
                is_sports.append(0)
                is_luxury.append(0)

            if row[1] == 'V4':
                is_v4.append(1)
                is_v6.append(0)
                is_v8.append(0)
                is_v12.append(0)
                is_electric.append(0)
            elif row[1] == 'V6':
                is_v4.append(0)
                is_v6.append(1)
                is_v8.append(0)
                is_v12.append(0)
                is_electric.append(0)
            elif row[1] == 'V8':
                is_v4.append(0)
                is_v6.append(0)
                is_v8.append(1)
                is_v12.append(0)
                is_electric.append(0)
            elif row[1] == 'V12':
                is_v4.append(0)
                is_v6.append(0)
                is_v8.append(0)
                is_v12.append(1)
                is_electric.append(0)
            elif row[1] == 'Electric':
                is_v4.append(0)
                is_v6.append(0)
                is_v8.append(0)
                is_v12.append(0)
                is_electric.append(1)
            else:
                is_v4.append(0)
                is_v6.append(0)
                is_v8.append(0)
                is_v12.append(0)
                is_electric.append(0)

            full_list.append(row)

    return full_list, one_hot_encoded_list


def complete_specific_data(dataset: list) -> list:
    """
    Creates a list of lists, each containing all instances of a specific attribute across all cars.

    Preconditions:
    - dataset is a list of lists, with each sublist containing attributes for a single car.
    """

    car_names = []
    engine_types = []
    hp = []
    price = []
    torque = []
    car_type = []
    rating = []
    reliability = []
    zts = []
    max_speed = []
    image_paths = []

    indicators = [car_names, engine_types, hp, price, torque, car_type, rating, reliability, zts, max_speed,
                  image_paths]

    for i in range(len(indicators)):
        for item in dataset:
            indicators[i].append(item[i])
    for lst in [hp, price, torque, rating, reliability, zts, max_speed]:
        for i in range(len(lst)):
            lst[i] = float(lst[i])

    return indicators


def normalize_specific_data(indi: list[list]) -> None:
    """
    Normalize the numerical data in each list of a list of lists in-place.
    """
    for ind in indi:
        if isinstance(ind[0], float):
            minim = min(ind)
            maxim = max(ind)
            for i in range(len(ind)):
                ind[i] = (ind[i] - minim) / (maxim - minim)


def finalize_all_data(dataset: str) -> list:
    """
    Finalize car data by combining all attributes and one-hot encoded lists into a single list.

    Preconditions:
    - dataset is the path to a CSV file that is properly formatted with car attributes.
    - The CSV file must include headers and be compatible with create_full_data and complete_specific_data functions
    """
    full_data = create_full_data(dataset)
    indicators = complete_specific_data(full_data[0])
    normalize_specific_data(indicators)
    final_indicators = indicators + full_data[1]  # This is the one hot encoded list added to the indicators list.
    del final_indicators[1]
    del final_indicators[4]
    del final_indicators[8]

    return final_indicators


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['csv'],  # the names (strs) of imported modules
        'allowed-io': ['create_full_data'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
