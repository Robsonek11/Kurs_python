building = ['dom', 'szkola', 'kosciol', 'bar', 'szpital']

graph = [(0, 1), (0, 2), (0, 3),
          (1, 0), (1, 4),
          (2, 0), (2, 3),
          (3, 0), (3, 2), (3, 4),
          (4, 1), (4, 3)]

for e in graph:
     b1, b2 = e
     print(building[b1], '---->', building[b2])