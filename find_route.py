import sys
import queue
from file_operation import *
from graph import *

# [DEBUG]
# print("Number of arguments: " + str(len(sys.argv)) + " arguments.")
# print("Argument List: " + str(sys.argv) + "\n")

# This uninformed search algorithm uses uniform-cost search
# to find optimal solution within the given graph from initial_node
def uninformed_search(G, initial_node):
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1  # 1 because of the initial node that we generated manually
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
        if node not in closed:
            closed.add(node)
            if node.is_goal:  # goal-test
                return (cost, path, nodes_popped, nodes_expanded, nodes_generated)
            else:  # else we add node's child into the PriorityQueue
                nodes_expanded += 1
                for edge in node.out_edges:
                    nodes_generated += 1
                    child = edge.to()  # reference to nodes child
                    fringe.put(
                        (
                            cost + edge.weight,
                            G.node(child.label),
                            path + [(child, edge.weight)],
                        )
                    )
    # if the loop exited, means we didn't find any path to destination
    return (0, [], nodes_popped, nodes_expanded, nodes_generated)


# This informed search algorithm uses A* search
# to find optimal solution within the given graph from initial_node
def informed_search(G, initial_node):
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1  # 1 because of the initial node that we generated manually
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
        if node not in closed:
            closed.add(node)
            if node.is_goal:  # goal-test
                return (cost, path, nodes_popped, nodes_expanded, nodes_generated)
            else:  # else we add node's child into the PriorityQueue
                nodes_expanded += 1
                local_fringe = queue.PriorityQueue()
                for edge in node.out_edges:
                    nodes_generated += 1
                    child = edge.to()  # reference to nodes child
                    local_fringe.put(
                        (
                            cost + edge.weight + child.heuristic_value,
                            G.node(child.label),
                            path + [(child, edge.weight)],
                        )
                    )
                fringe.put(
                    local_fringe.get()
                )  # we are only putting the smallest path out of all the local_fringe in the global fringe
    # if the loop exited, means we didn't find any path to destination
    return (0, [], nodes_popped, nodes_expanded, nodes_generated)


# this function returns populated graph from the parsed_file
def populate_graph(parsed_file, goal_label):
    g = Graph()
    for node in parsed_file:
        is_goal = True if goal_label == node[0] else False
        g.add_new_node(node[0], node[1], node[2], is_goal)
    return g


def add_heuristic_value(G, parsed_file):
    for node in parsed_file:
        for iterated in G.nodes:
            if iterated.label == node[0]:
                iterated.modify_heuristic_value(node[1])


def print_path(result_path):
    if result_path:
        previous_node = result_path[0]
    else:
        print("Distance: Infinity")
        print("Route:")
        print("None")
        return
    total_cost = 0
    for node in result_path[1:]:
        print(
            previous_node[0].label
            + " to "
            + node[0].label
            + ", "
            + str(node[1])
            + " km"
        )
        previous_node = node
        total_cost += node[1]
    print("Distance: " + str(total_cost) + " km")


parsed_file = parse_file(sys.argv[1])
g = populate_graph(parsed_file, sys.argv[3])

if len(sys.argv) > 4:
    parsed_heuristic_file = parse_file(sys.argv[4])
    add_heuristic_value(g, parsed_heuristic_file)
    result_path = informed_search(g, g.node(sys.argv[2]))
    print("Nodes Popped: " + str(result_path[2]))
    print("Nodes Expanded: " + str(result_path[3]))
    print("Nodes Generated: " + str(result_path[4]))
    print_path(result_path[1])
else:
    result_path = uninformed_search(g, g.node(sys.argv[2]))
    print("Nodes Popped: " + str(result_path[2]))
    print("Nodes Expanded: " + str(result_path[3]))
    print("Nodes Generated: " + str(result_path[4]))
    print_path(result_path[1])
