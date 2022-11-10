"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""

import pandas as pd
import numpy as np
import os
import sys

def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    file = 'ChicagoSketch_net.tntp'
    
    try:
        # Enter your code here
        graph = pd.read_csv(file, skiprows=8, sep='\t')
        cleaned= [s.strip().lower() for s in graph.columns]
        graph.columns = cleaned
        graph.drop(['~', ';'], axis=1, inplace=True)
        
        # connections holds the graph. It is a dictionary of dictionaries that stores the neighbor nodes and their 
        # costs for each node
        graph_object = {}
    
        for node in range(1,max(graph["init_node"])+1):
            graph_object[node] = {}    
    
        for i in range(graph.shape[0]):
            row = graph.iloc[i]
            start = row.init_node
            end = row.term_node
            cost = row.free_flow_time 
            graph_object[start][int(end)] = cost
          
            
        return graph_object
    
    except:
        return graph_object


def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1

        Link generalized cost = Link travel time + toll_factor * toll + distance_factor * distance
    """
    shortest_path_distance = -1

    try:
        # Enter your code here

        # storing the mincost for each node

        mincost = [sys.maxsize for i in range(len(graph_object))]
        mincost[source] = 0

        # creating a dictionary of neighbor node and its cost. the node with min cost is popped 
        # from here and used to find neighbors from that

        node_pq = {}
        node_pq[source] = 0

        while len(node_pq) > 0:
            
            node_min = min(node_pq, key=lambda x: node_pq[x])      # return node with min cost from the dict
            node_min_cost = node_pq[node_min]
            
            for neighbor,cost in graph_object[node_min].items():
                if node_min_cost + cost < mincost[neighbor-1]:
                    mincost[neighbor-1] = node_min_cost + cost
                    node_pq[neighbor] = mincost[neighbor-1]
                    
            del node_pq[node_min]

        if(mincost[destination] != sys.maxsize):
            shortest_path_distance =  mincost[destination-1]

        return shortest_path_distance

    except:
        return shortest_path_distance
