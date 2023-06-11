wierzcholek = {
    1: "dom",
    2: "szkola",
    3: "kosciol",
    4: "bar",
    5: "szpital",
    6: "kino",
    7: "teatr"
}

graph = {
    1: [2, 4, 3],
    2: [1, 5],
    3: [1, 4, 6],
    4: [3, 1, 5],
    5: [4, 2, 6, 7],
    6: [3, 5, 7],
    7: [6, 5]
}

for i in graph:
    for j in graph[i]:
        print(f'{wierzcholek[i]} -> {wierzcholek[j]}')
    print("---" * 2)