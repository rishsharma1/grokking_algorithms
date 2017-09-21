import sys

example_graph = {
        "S": {"A": 6,"B": 2},
        "B": {"A": 3, "F": 5},
        "A": {"F": 1},
        "F": {}
        }

# rama wishes to trade his shitty book for a piano
# since rama is cheap and a nerd he will use dijkstra's
# to find the cheapest way to trade for a piano
rama_rags_to_riches = {
        "BOOK": {"LP": 5, "POSTER": 0},
        "LP": {"BASS GUITAR": 15, "DRUM SET": 20},
        "POSTER": {"BASS GUITAR": 30, "DRUM SET": 35},
        "BASS GUITAR": {"PIANO": 20},
        "DRUM SET": {"PIANO": 10},
        "PIANO": {}
        }

def create_tracking_table(graph,start):
    table = {}
    table[start] = {"parent": None, "cost": 0, "visited" : False}
    keys = list(set(graph.keys()) - set([start]))
    for key in keys:
        table[key] = {"parent": '', "cost": sys.maxint, "visited": False}
    return table

def find_next_cheapest_node(table):
    # we are only interested in ones that we have not visited yet
    non_visited = list(filter(lambda (x,y): y["visited"] == False,table.items()))
    non_visited.sort(key=lambda (x,y): y["cost"])
    if non_visited:
        return non_visited[0][0]
    return None

def find_cheapest_path(table, finish):

    if finish is None:
        return []
    return find_cheapest_path(table,table[finish]["parent"]) + [finish]

def dijkstra(graph, start, finish):
    table = create_tracking_table(graph,start)
    node = find_next_cheapest_node(table)
    while node != None:

        neighbors_dict = graph[node]
        table[node]["visited"] = True
        for neighbor in neighbors_dict.keys():
            totalCost = table[node]["cost"] + neighbors_dict[neighbor]
            if totalCost < table[neighbor]["cost"]:
                table[neighbor]["cost"] = totalCost
                table[neighbor]["parent"] = node

        node = find_next_cheapest_node(table)
    return find_cheapest_path(table,finish)

def main():
    print dijkstra(example_graph,"S","F")
    print dijkstra(rama_rags_to_riches, "BOOK", "PIANO")
if __name__ == "__main__":
    main()
