import sys
import queue
from file_operation import *
from ucs import *

# [DEBUG]
# print("Number of arguments: " + str(len(sys.argv)) + " arguments.")
# print("Argument List: " + str(sys.argv) + "\n")

nodes_generated = 0


def graph_search(G, initial_node):
    nodes_popped = 0
    nodes_expanded = 0
    closed = set()  # set of visited nodes
    fringe = queue.PriorityQueue()
    # (cost, node, path)
    # cost: the cumulative cost,
    # node: the current node,
    # path: the path that led to the expansion of the current node

    # insert initial node into the fringe
    fringe.put((0, initial_node, [initial_node]))

    while not fringe.empty():
        cost, node, path = fringe.get()  # remove the front of the fringe
        nodes_popped += 1
        closed.add(node)
        if node.is_goal:  # goal-test
            print("Nodes Popped: " + str(nodes_popped))
            print("Nodes Expanded: " + str(nodes_expanded))
            return (cost, path)
        else:  # else we add node's child into the PriorityQueue
            nodes_expanded += 1
            for edge in node.out_edges:
                child = edge.to()  # reference to nodes child
                if child not in closed:
                    fringe.put(
                        (cost + edge.weight, G.node(child.label), path + [child]))
    print("Nodes Popped: " + str(nodes_popped))
    print("Nodes Expanded: " + str(nodes_expanded))
    # if the loop exited, means we didn't find any path to destination
    return (0, [])


# this function returns populated graph from the parsed_file
def populate_graph(parsed_file, goal_label):
    g = Graph()
    for node in parsed_file:
        is_goal = True if goal_label == node[0] else False
        g.add_new_node(node[0], node[1], node[2], is_goal)
    return g


def print_path(result_path):
    for node in result_path[1]:
        print(node.label)


parsed_file = parse_file("input1.txt")
g = populate_graph(parsed_file, sys.argv[2])
g.print_graph()
result_path = graph_search(g, g.node(sys.argv[1]))
print(result_path)
# print_path(result_path)
