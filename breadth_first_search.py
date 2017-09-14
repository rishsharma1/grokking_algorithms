
def length_of_shortest_path(graph,start,finish):

    visited = {}
    path_length = 1
    queue = [start]

    while len(queue) > 0:

        next = []
        for u in queue:

            for v in graph[u]:

                if v == finish:
                    return path_length

            path_length += 1

            queue = next

    return path_length


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
    print length_of_shortest_path(example_graph,"S","F")
    print length_of_shortest_path(example_graph_two,"CAB","BAT")
if __name__ == "__main__":
    main()
