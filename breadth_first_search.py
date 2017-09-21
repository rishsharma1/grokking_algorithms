
def shortest_path(graph,start,finish):

    visited = {}
    path_length = 1
    queue = [[start]]

    while queue:

        path = queue.pop(0)
        node = path[-1]
        if visited.get(node) is None:
            visited[node] = "Y"
            neighbours = graph[node]

            if node == finish:
                return path

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)




def main():


    example_graph = {
        "S": ["A","B"],
        "B": ["F","C"],
        "A": ["C","D"],
        "D": ["F"],
        "C": [],
        "F": []
        }

    example_graph_two = {
            "CAB": ["CAT","CAR"],
            "CAR": ["BAR","CAT"],
            "CAT": ["MAT","BAT"],
            "BAR": ["BAT"],
            "MAT": ["BAT"],
            "BAT": []
            }
    print len(shortest_path(example_graph,"S","F"))
    print len(shortest_path(example_graph_two,"CAB","BAT"))
if __name__ == "__main__":
    main()
