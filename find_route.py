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
    nodes_generated = 0
    closed = set()  # set of visited nodes
    fringe = queue.PriorityQueue()
    # (cost, node, path)
    # cost: the cumulative cost,
    # node: the current node,
    # path: the path that led to the expansion of the current node

    # insert initial node into the fringe
    fringe.put((0, initial_node, [(initial_node, 0)]))

    while not fringe.empty():
        cost, node, path = fringe.get()  # remove the front of the fringe
        nodes_popped += 1
        closed.add(node)
        if node.is_goal:  # goal-test
            return (cost, path, nodes_popped, nodes_expanded, nodes_generated)
        else:  # else we add node's child into the PriorityQueue
            nodes_expanded += 1
            for edge in node.out_edges:
                child = edge.to()  # reference to nodes child
                if child not in closed:
                    nodes_generated += 1
                    fringe.put(
                        (cost + edge.weight, G.node(child.label), path + [(child, edge.weight)]))
    # if the loop exited, means we didn't find any path to destination
    return (0, [], nodes_popped, nodes_expanded, nodes_generated)


# this function returns populated graph from the parsed_file
def populate_graph(parsed_file, goal_label):
    g = Graph()
    for node in parsed_file:
        is_goal = True if goal_label == node[0] else False
        g.add_new_node(node[0], node[1], node[2], is_goal)
    return g


def print_path(result_path):
    print("Route:")
    if result_path:
        previous_node = result_path[0]
    else:
        print("None")
        return
    for node in result_path[1:]:
        print(previous_node[0].label + " to " +
              node[0].label + ", " + str(node[1]) + " km")
        previous_node = node


parsed_file = parse_file(sys.argv[1])
g = populate_graph(parsed_file, sys.argv[3])
result_path = graph_search(g, g.node(sys.argv[2]))
print("Nodes Popped: " + str(result_path[2]))
print("Nodes Expanded: " + str(result_path[3]))
print("Nodes Generated: " + str(result_path[4]))
if not result_path[0] == 0:
    print("Distance: " + str(result_path[0]) + " km")
else:
    print("Distance: Infinity")
print_path(result_path[1])
