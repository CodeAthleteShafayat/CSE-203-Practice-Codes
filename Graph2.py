graph_name = ["a","b","c","d","e"]
graph = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
graph[0][1] = 1
graph[0][3] = 1
graph[1][2] = 1
graph[1][4] = 1
graph[2][0] = 1
graph[2][4] = 1
graph[3][2] = 1
graph[3][4] = 1
graph[4][4] = 1
print(graph)


graphl = {
    "a" : ["b","c","e"],
    "b" : ["c","d"],
    "c" : ["a","b","e"],
    "d": ["b","d","e"],
    "e" : ["a","c"],
}


print(graphl)


def getdegreeM(grf,node,name = graph_name):
    ind = name.index(node)
    return grf[ind].count(1)

getdegreeM(graph,"c")
def getdegreeL(grf,node):
    li = grf[node]
    return len(li)
getdegreeL(graphl,"c")

def mutualM(graph,node1,node2,name = graph_name):
    ind1 = name.index(node1)
    ind2 = name.index(node2)
    for i in range(len(graph)):
        if graph[ind1][i] == graph[i][ind2] and graph[i][ind1] == 1 :
            return [graph.append[i]]
print(mutualM(graph,"a","b"))