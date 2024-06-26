"""CSC111 Winter 2024 Project: Car Recommender System

Module Description
==================
This module contains functions for creating and analyzing a complete graph based on car
similarity scores. Each vertex in the graph represents a car, and edges are weighted by
the similarity score between cars, calculated using the Euclidean distance formula.
The similarity scores are used to recommend similar cars to the user's preferred choice.
The module also includes functions for normalizing data and one-hot encoding categorical
attributes to prepare the car data for graph analysis.

Copyright and Usage Information
===============================

This file is Copyright (c) 2024 CSC111 Students Winter (Yaseen Sadat, Muhammad Aneeq, Umer Farooqui, Zarif Ali)
"""
from __future__ import annotations

from typing import Any, Union

import math
import data_work


def generate_car_dict(csv_data: str) -> dict:
    """
    Generate a dictionary mapping each car name to its corresponding attributes.

    This function processes car data provided in a CSV format to create a dictionary.
    Each key in the dictionary is a car name and the value is a list of attributes for that car.

    Preconditions:
    - The CSV file must have a header row with the following fields:
      'Car Name', 'HP', 'Price', 'Torque', 'Car Type', 'Rating', 'Reliability', '0-60', 'Image Path'.
    """
    car_dict = {}
    ind_lst = data_work.finalize_all_data(csv_data)

    car_names = ind_lst[0]
    for j in range(len(car_names)):
        temp = []
        for i in range(1, len(ind_lst)):
            temp.append(ind_lst[i][j])
        car_dict[car_names[j]] = temp

    return car_dict


class WeightedGraph:
    """A weighted graph used to represent a book review network that keeps track of review scores.

    Note that this is a subclass of the Graph class from Exercise 3, and so inherits any methods
    from that class that aren't overridden here.
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _WeightedVertex object.
    _vertices: dict[Any, _WeightedVertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:
        """Add a vertex with the given item and kind to this graph.

        The new vertex is not adjacent to any other vertices.
        Do nothing if the given item is already in this graph.

        Preconditions:
            - kind in {'user', 'book'}
        """
        if item not in self._vertices:
            self._vertices[item] = _WeightedVertex(item)

    def add_edge(self, item1: Any, item2: Any, weight: Union[int, float] = 1) -> None:
        """Add an edge between the two vertices with the given items in this graph,
        with the given weight.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            # Add the new edge
            v1.neighbours[v2] = weight
            v2.neighbours[v1] = weight
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def get_euc_sim_score(self, item1: Any, item2: Any, car_d: dict) -> float:
        """
        Calculates the Euclidean similarity score between two vertices, representing cars.

        Preconditions:
        - item1 and item2 must be vertices item names in the graph.
        - car_d must be a dictionary returned by generate_car_dict.
        """
        if item1 not in self._vertices or item2 not in self._vertices:
            raise ValueError
        i1 = self._vertices[item1]
        i2 = self._vertices[item2]
        return i1.euc_similiarity_score(i2, car_d)

    def recommend_cars(self, car: str) -> list:
        """
        Recommend a list of cars similar to the specified car based on the Euclidean similarity score.

        Preconditions:
        - The car must be a vertex in the graph.
        - The graph must have weighted edges representing Euclidean similarity scores.
        """
        lst = []

        car_v = self._vertices[car]
        nei_d = car_v.neighbours
        sorted_dict = dict(sorted(nei_d.items(), key=lambda item: (item[1]), reverse=True))
        for elem in sorted_dict:
            lst.append((elem.item, round(car_v.neighbours[elem] * 100)))
        return lst[:5]


class _WeightedVertex:
    """A vertex in a weighted book review graph, used to represent a user or a book.

    Same documentation as _Vertex from Exercise 3, except now neighbours is a dictionary mapping
    a neighbour vertex to the weight of the edge to from self to that neighbour.
    Note that for this exercise, the weights will be integers between 1 and 5.

    Instance Attributes:
        - item: The data stored in this vertex, representing a user or book.

        - neighbours: The vertices that are adjacent to this vertex, and their corresponding
            edge weights.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
    """
    item: Any
    neighbours: dict[_WeightedVertex, Union[int, float]]

    def __init__(self, item: Any) -> None:
        """Initialize a new vertex with the given item and kind.

        This vertex is initialized with no neighbours.

        """
        self.item = item
        self.neighbours = {}

    def euc_similiarity_score(self, other: _WeightedVertex, car_d: dict) -> float:
        """
        Calculates the Euclidean similarity score between this vertex and another _WeightedVertex.

        The score is computed based on the attributes of the cars that these vertices represent.
        A higher score indicates greater similarity between the cars.

        Preconditions:
            - self.item and other.item must be keys in the car_d dictionary.
            - car_d[self.item] and car_d[other.item] must be lists of numerical attributes of equal length.
        """

        l1 = car_d[self.item]
        l2 = car_d[other.item]
        squared_diff_sum = sum((a - b) ** 2 for a, b in zip(l1, l2))
        distance = math.sqrt(squared_diff_sum)
        return 1 / (1 + distance)


def load_complete_graph(dataset: str) -> WeightedGraph:
    """
    Creates and loads a complete weighted graph from car data stored in a CSV file.In this graph
    each vertex is connected to each vertex.


    The edges are weighted based on the Euclidean similarity scores between the cars represented by the vertices.
    """
    car_d = generate_car_dict(dataset)

    g = WeightedGraph()
    for car in car_d:
        g.add_vertex(car)
    for car1 in car_d:
        for car2 in car_d:
            if car1 != car2:
                g.add_edge(car1, car2, g.get_euc_sim_score(car1, car2, car_d))

    return g


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['data_work', 'math'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
