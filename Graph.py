graph_name = ["a","b","c","d","e"]
graph = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

graph[0][3] = 1
graph[0][4] = 1

graph[1][3] = 1
graph[1][2] = 1
graph[1][4] = 1

graph[2][3] = 1
graph[2][4] = 1

graph[3][1] = 1
graph[3][2] = 1
graph[3][4] = 1

graph[4][1] = 1
graph[4][2] = 1


print(graph)

def countdegree(graph,node,namenode = graph_name):
    ind = namenode.index(node)
    return  graph[ind].count(1)
print(countdegree(graph,"a"))


# def countdegree(graph,node, nodename = graph_name):
#     ind = graph.index(node)
#     return graph[ind].count(1)
# print(countdegree(graph, "b" ))

graphl = {
    "a" : ["b", "c", "e"],
    "b" : ["c"],
    "c" : ["e"],
    "d" : [],
    "e" : ["b", "c"],
}
def getdegree(graph,node):
    li = graph[node]
    return  len(li)
    
print(getdegree(graphl , "b"))


def mutual(graph,node1,node2,namenode = graph_name):
    ind1 = namenode.index(node1)
    ind2 = namenode.index(node2)
    li = []
    for i in range(len(graph)):
        if graph[ind1][i] == graph[i][ind2] and graph [ind1][i] == 1:
            li.append(namenode[i])
    return li
print(mutual(graph, "a","c"))
def mutualL(graph,node1,node2):
    li = []
    for i in graph[node1]:
        if  i in graph[node2]:
            li.append(i)
    return li
print(mutualL(graphl,"b","c"))

def getdegreeM(graph,node,name =graph_name):
    ind = name.index(node)
    return graph[ind].count(1)
print(getdegreeM(graph,"a"))


def getdegreeL(graph,node):
    li = graph[node]
    return len(li)
print(getdegreeL(graphl,"b"))


def getmutualM(graph,node1,node2,name = graph_name):
    ind1  =  name.index(node1)
    ind2  =  name.index(node2)
    li   =   []
    for i in range(len(graph)):
        if graph[ind1][i] == graph[i][ind2] and graph[i][ind1] == 1 :
            li.append(i)

    return li
print(getmutualM(graph, "b", "c"))


def getmutualL(graph, node1, node2):
    li = []
    for i in graph[node1]:
        if i in graph[node2]:
            li.append(i)

    return li
print(getmutualL(graphl, "b", "d"))

graph_name.append("f")
add = [0 for i in range(len(graph))]
graph.append(add)
for i in (graph):
    i.append(0)
print(graph)

def find(graph,namenode = graph_name):
    li = []
    for i in range(len(graph)):
        if graph[i].count(1) == 0:
            li.append(namenode[i])
    return li 
print(find(graph))


def isundirected(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != graph[j][i]  :
                return False
        
    return True
print(isundirected(graph))


def undirected_to_directed(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == graph[j][i] and graph[i][j] == 1 :
                graph[i][j] = 0

        return graph
    
print(undirected_to_directed(graph))

def directed_to_undirected(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != graph[j][i] and graph[i][j] == 0:
                graph[i][j] = 1
    return graph


def isundirected_L(graph):
    for i in graph:
        for j in graph[i] :
            if i not in graph[j]:
                return False
            
    return True
print(isundirected_L(graphl))


def un_to_dirL(graph):
    for i in graph:
        for j in graph[i]:
            if i in graph[j]:
                graph[j].remove(i)
    return graph

def dir_to_dirL(graph):
    for i in graph:
        for j in graph[i]:
            if i not in graph[j]:
                graph[j].append(i)



