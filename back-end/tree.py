"""
CSC111 Winter 2024 Project: Car Recommendation and Ranking System

Module Description ================== This module is integral to a car recommendation and ranking system designed to
assist users in finding cars that match their preferences across multiple attributes. Utilizing a decision tree,
this module efficiently filters and suggests car models that align with user inputs. Additionally, it features a
ranking algorithm that evaluates and ranks recommended cars based on a set of criteria including rating, reliability,
acceleration, and maximum speed, aiding users in making informed decisions.

The decision tree approach allows for an organized and efficient search through the dataset based on user
preferences. The module defines several functions for: - Encoding car attributes into numerical categories. -
Building the decision tree from a dataset. - Searching the tree based on user-defined preferences. - Ranking the cars
based on performance scores derived from the users' weighted preferences.

Usage of this file is intended for educational purposes within the CSC111 course framework, focusing on the
application of data structures, algorithms, and object-oriented programming concepts to real-world problems.

Copyright and Usage Information
===============================

This file is Copyright (c) 2024 CSC111 Students Winter (Yaseen Sadat, Muhammad Aneeq, Umer Farooqui, Zarif Ali)

"""
from __future__ import annotations

import csv
import os
from typing import Any, Optional


def encode_engine(engine: str) -> int:
    """
    Converts an engine type into a numerical value based on a predefined mapping.
    This function takes an engine type as input, represented as a string, and returns
    a corresponding numerical value.
    """
    mapping = {'V4': 1, 'V6': 2, 'V8': 3, 'V10': 4, 'V12': 5, 'Electric': 6}

    value = mapping[str(engine)]
    return value


def encode_hp(hp: int) -> int:
    """
    Converts horsepower (hp) into a categorical value based on defined ranges.
    """
    hp = int(hp)
    if hp < 450:
        return 1
    elif 450 <= hp <= 620:
        return 2
    elif hp > 620:
        return 3
    raise ValueError


def encode_hp2(hp: str) -> int:
    """
    This function takes in a string reperesentation of  horspower and converts it in to a numerical value based on the
    input range from the user.
    """
    if hp == '0-449':
        return 1
    elif hp == '450-620':
        return 2
    elif hp == '620+':
        return 3
    raise ValueError


def encode_price(price: int) -> int:
    """
    This function takes the price of a vehicle, converts it into an integer, and then
    assigns a numerical category based on where the price falls within specific ranges.
    If the price does not fit into these categories due to an unexpected value, it defaults to 0.
    """
    price = int(price)
    if price < 50000:
        return 1
    elif 50000 <= price < 100000:
        return 2
    elif 100000 <= price < 200000:
        return 3
    elif price > 200000:
        return 4
    else:
        return 0


def encode_price2(price: str) -> int:
    """
    This function takes a string representing a price range for a vehicle and assigns a numerical
    category based on predefined price range categories.
    If the input price range does not match any of the predefined categories, it defaults to 0.
    """
    if price == '$0-$49,999':
        return 1
    elif price == '$50,000-$99,999':
        return 2
    elif price == '$100,000-$199,999':
        return 3
    elif price == '$200,000+':
        return 4
    else:
        return 0


def encode_torque(torque: int) -> int:
    """
    This function takes the torque of a vehicle as input and converts it into an integer, and categorizes it into one
    of three predefined categories based on the torque value.
    If the torque value does not match any of these categories, it defaults to 0.
    """
    torque = int(torque)
    if torque < 500:
        return 1
    elif 500 <= torque <= 750:
        return 2
    elif torque > 750:
        return 3
    else:
        return 0


def encode_torque2(torque: str) -> int:
    """

    This function takes in a string reperesentation of torque and converts it in to a numerical value based on the
    input range from the user.
    """
    if torque == '0-499':
        return 1
    elif torque == '500-750':
        return 2
    elif torque == '750+':
        return 3
    else:
        return 0


def encode_car_type(car_type: str) -> int:
    """
    This function takes the type of  car as input, represented as a string, and returns a corresponding
    numerical category based on a predefined mapping.
    """
    mapping = {'Sedan': 1, 'SUV': 2, 'Sports': 3, 'Luxury': 4}
    value = mapping[str(car_type)]
    return value


class Tree:
    """
       A recursive tree data structure.
       A decision tree data structure for organizing and retrieving car information.

       This class implements a recursive tree structure designed to categorize cars based on their attributes like
       engine type, horsepower (hp), price, torque, and car type. Each node in the tree represents a decision point
       based on these attributes, leading to the final leaf nodes that represent specific car models matching the
       criteria.


       Representation Invariants:
           - self._root is not None or self._subtrees == []
           - all(not subtree.is_empty() for subtree in self._subtrees)

       Instance Attributes:
          - _root:
             The item stored at this tree's root, or None if the tree is empty.
          - _subtrees:
              The list of subtrees of this tree. This attribute is empty when
              self._root is None (representing an empty tree). However, this attribute
              may be empty when self._root is not None, which represents a tree consisting
              of just one item.


       """

    _root: Optional[Any]
    _subtrees: list[Tree]

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If root is None, the tree is empty.

        Preconditions:
            - root is not none or subtrees == []
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None

    def find_cars(self, attributes: list, index: int = 0) -> list:
        """
        Searches the tree to find car models that match a sequence of given attributes. This method navigates through
        the tree, using a list of attributes to find all car models that match these attributes exactly. The
        attributes should be provided in a specific order and encoded to their respective numerical categories before
        calling this method. Each attribute in the list searches deeper into the tree, matching nodes at
        each level until car models are found or the search criteria are exhausted.
        Returns A list of car models that match the given attributes.
        If no matches are found or the tree is empty, returns an empty list.
        """
        if self.is_empty():
            return []

        if index >= len(attributes):
            return [current_sub._root for current_sub in self._subtrees if isinstance(current_sub._root, str)]

        # Directly use the attribute without encoding
        attribute = attributes[index]

        for sub in self._subtrees:
            if sub._root == attribute:
                return sub.find_cars(attributes, index + 1)

        return []

    def insert_sequence(self, items: list) -> None:
        """
        Adds a sequence of attributes ending with a car model into the tree.

        This method takes a list of car attributes and the car model itself, then adds them into the tree, creating a
        path from the root to the car model. If any part of the sequence already exists in the tree,
        it skips creating a new one and continues from that point. This way, each car model is placed in the tree
        according to its attributes.

        For example, if the items list is [engine, horsepower, price, torque, car type, car model], the tree will
        have a path that starts with the engine attribute and ends with the car model. If a path already exists for
        some attributes, it adds the new attributes and car model to the existing path.
        """

        if not items:
            return

        insert = None
        for sub in self._subtrees:
            if sub._root == items[0]:
                insert = sub
                break

        if insert is None:
            insert = Tree(items[0], [])
            self._subtrees.append(insert)

        insert.recursive_helper(items[1:])

    def recursive_helper(self, items: list) -> None:
        """
        A helper method to recursively insert items into the tree to form a chain.
        Helps add a sequence of items to the tree, one step at a time.

        This method works to add each item from a list into the tree. It checks if part of the sequence already
        exists and adds new items as needed, making sure every item leads to the next one in the list. If it finds an
        item already in the tree, it moves on to add the next item in the sequence from there. If not, it creates a
        new spot for the item and keeps going until all items are added. This way, it builds up the paths in the tree
        that represent different sequences of car attributes ending in car models.
        """
        if not items:
            return

        for sub in self._subtrees:
            if sub._root == items[0]:
                sub.recursive_helper(items[1:])
                return

        new_sub = Tree(items[0], [])
        self._subtrees.append(new_sub)

        new_sub.recursive_helper(items[1:])


def build_decision_tree(file: str) -> Tree:
    """Build a decision tree storing the car data from the given file.

    Preconditions:
        - file is the path to a csv file in the format of the car_data_set.csv
    """
    tree = Tree('', [])

    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            car_model = row.pop(0)
            engine = encode_engine(row[0])
            hp = encode_hp(int(row[1]))
            price = encode_price(int(row[2]))
            torque = encode_torque(int(row[3]))
            car_type = encode_car_type(row[4])

            attributes_sequence = [engine, hp, price, torque, car_type] + [car_model]
            tree.insert_sequence(attributes_sequence)

    return tree


def car_dict(file: str) -> dict:
    """
    Read car data from a file and return a dictionary with car models as keys and their
    attributes as values.
    """
    car_attributes_dict = {}

    with open(file, mode='r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            car_model = row[0]
            attributes = [
                float(row[6]),  # rating
                float(row[7]),  # reliability
                float(row[8]),  # zero_to_sixty
                int(row[9]),  # max_speed
                row[10],  # image path
                row[1],  # engine
                int(row[2]),  # horsepower
                int(row[3]),  # price
                int(row[4]),  # torque
                row[5]  # car type
            ]
            car_attributes_dict[car_model] = attributes

    return car_attributes_dict


def car_guesser(car_file: str, preferences: list) -> list:
    """

    Suggests car models based on user preferences by querying a decision tree built from car data.

    This function first builds a decision tree from a given CSV file containing car data. Then, it takes a list of
    user preferences for car features (like engine type, horsepower, price range, torque, and car type),
    encodes these preferences into a format that matches the tree's structure, and uses the tree to find car models
    that match these preferences.
    """
    decision_tree = build_decision_tree(car_file)
    lst = ['x', 'x', 'x', 'x', 'x']
    lst[0] = encode_engine(preferences[0])
    lst[1] = encode_hp2(preferences[1])
    lst[2] = encode_price2(preferences[2])
    lst[3] = encode_torque2(preferences[3])
    lst[4] = encode_car_type(preferences[4])
    possible_cars = decision_tree.find_cars(lst)

    if not possible_cars:
        return []
    else:
        lst = []
        for car in possible_cars:
            lst.append(car)
        return lst


def car_ranker(preferences: list[str], chosen_cars: list[str], all_cars: dict) -> Any:
    """
     Ranks cars based on user preferences and calculates a performance score for each.

    This function evaluates and ranks car models from a given list ('chosen_cars') according to user preferences on
    different metrics such as rating, reliability, acceleration (zero to sixty time), and max speed. Each preference
    is weighted by the user, indicating the importance of each metric. The function then calculates a score for each
    car based on these preferences and the car's attributes, ranking them from highest to lowest score.

    The performance score is adjusted based on the car's attributes relative to maximum and minimum values across all
    cars, aiming to highlight cars with better overall performance.
    1) In the first step we factor out the max/min hp, max/min torque,the max/min zero_to_sixty and max/min speed. Then
    we normalize hp, torque and speed on a scale of  0-1. Without normalization comparing a 700hp to a 200hp would seem
    unfair.  This rescales the actual HP and torque to a value between 0 and 1 based on where they lie between the
    minimum and maximum values in the dataset.
    2) In the next step we normalize zero_to_sixty. If we normalize directly then the car with a lower time score
    would have a lower which is the opposite of what we wantThe formula 1 - ((value - min_value) / (max_value -
    min_value)) inverts the scale so that a lower 0-60 time translates to a higher normalized score.
    3) In the third step, we just combine the scores to give us a final performance score.
    """

    if not chosen_cars:
        return None
    rating_weight = int(preferences[0]) / 100
    reliability_weight = int(preferences[1]) / 100
    zero_to_sixity_weight = int(preferences[2]) / 100
    max_speed_weight = int(preferences[3]) / 100

    max_hp, min_hp = 1020, 169
    max_torque, min_torque = 1050, 205
    max_zero_to_sixty, min_zero_to_sixty = 11, 2
    max_speed, min_speed = 340, 170

    dictionary = {}
    for car in chosen_cars:
        speed = all_cars[car][3]
        horsepower = all_cars[car][6]
        torque = all_cars[car][8]
        zero_to_sixity = all_cars[car][2]
        print(zero_to_sixity)

        rate_score = all_cars[car][0] * rating_weight
        reliability_score = all_cars[car][1] * reliability_weight
        zero_to_sixity_score = all_cars[car][2] * zero_to_sixity_weight
        max_speed_score = all_cars[car][3] * max_speed_weight
        total_score = (rate_score + reliability_score - zero_to_sixity_score + max_speed_score) / 4
        img_path = all_cars[car][4]
        image = os.path.join(img_path + '.jpg')

        normalized_speed = (speed - min_speed) / (max_speed - min_speed)
        normalized_hp = (horsepower - min_hp) / (max_hp - min_hp)
        normalized_torque = (torque - min_torque) / (max_torque - min_torque)
        normalized_zero_to_sixty = 1 - ((zero_to_sixity - min_zero_to_sixty) / (max_zero_to_sixty - min_zero_to_sixty))

        combined_score = (normalized_hp + normalized_torque + normalized_zero_to_sixty + normalized_speed) / 4
        performance_score = combined_score * 100

        if performance_score < 50:
            performance_score += 20

        if 51 <= performance_score < 75:
            performance_score += 20
        pf = round(performance_score)

        dictionary[car] = total_score, image, pf

    ranked_cars = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return ranked_cars


if __name__ == '__main__':
    # You can uncomment the following lines for code checking/debugging purposes.
    # However, we recommend commenting out these lines when working with the large
    # datasets, as checking representation invariants and preconditions greatly
    # increases the running time of the functions/methods.
    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()

    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['E1136'],
        'extra-imports': ['csv', 'os'],
        'allowed-io': ['car_dict', 'build_decision_tree'],
        'max-nested-blocks': 4
    })
