import heapq

def solution(graph, start, end, max_extra_edges):
    pq = [(0, start, 0)]
    distances = {start: (0, 0)}

    while pq:
        current_weight, current_node, extra_edges_used = heapq.heappop(pq)
        if current_node == end:
            return current_weight

        for neighbor, weight, is_extra in graph[current_node]:
            next_weight = current_weight + weight
            next_extra_edges_used = extra_edges_used + 1 if is_extra else extra_edges_used

            if next_extra_edges_used > max_extra_edges: 
                continue

            if neighbor not in distances or (next_weight < distances[neighbor][0] or next_extra_edges_used < distances[neighbor][1]):
                distances[neighbor] = (next_weight, next_extra_edges_used)
                heapq.heappush(pq, (next_weight, neighbor, next_extra_edges_used))

    return float('inf') #если пути нет
graph = {
    0: [(1, 10, False), (2, 2, True)],
    1: [(0, 10, False), (2, 10, False)],
    2: [(0, 2, True), (1, 10, False), (3, 3, True)],
    3: [(2, 3, True)]
}
start = 0
end = 3
max_extra_edges = 2
print(solution(graph, start, end, max_extra_edges))