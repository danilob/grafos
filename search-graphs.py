import networkx as nx
vis = []
v = []

G = nx.Graph()

f = open("graph.txt", "r")
list_vertice = []
nv = int(f.readline())
#print (nv)
v = f.readline().replace("\n","").split(" ")
#print (v)
G.add_nodes_from(v)
ne = int(f.readline())
for x in range(ne):
    edge = f.readline().replace("\n","").split(" ")
    G.add_edge(edge[0],edge[1])

def kDFS(G):
    print ("--> Algoritmo DFS")
    global vis
    vis = []
    for i in range(G.number_of_nodes()):
        vis.append(False)
    k = 0
    for i in range(G.number_of_nodes()):
        if (vis[i]==False):
            k = k + 1
            print ("Componente: "+str(k))
            depth(G,i,k)
            print ("\n------------------")

    print("\n")


def depth(G,vs,mk):
    global vis
    global v
    vis[vs] = mk
    print(v[vs]+" ",end="")
    for w in list(G.adj[v[vs]]):
       if (vis[v.index(w)]==False):
           depth(G,v.index(w),mk)


def kBFS(G):
    print ("--> Algoritmo BFS")
    global vis
    vis = []
    for i in range(G.number_of_nodes()):
        vis.append(False)
    k = 0
    for i in range(G.number_of_nodes()):
        if (vis[i]==False):
            k = k + 1
            print ("Componente: "+str(k))
            searchAmpl(G,i,k)
            print ("\n------------------")

    print("\n")

def searchAmpl(G,vs,mk):
    global vis
    global v
    vis[vs] = mk
    print(v[vs]+" ",end="")
    fila = []
    fila.append(v[vs])
    while fila:
        w = fila.pop(0)
        for i in list(G.adj[w]):
            if (vis[v.index(i)]==False):
                vis[v.index(i)] = mk
                print(v[v.index(i)]+" ",end="")
                fila.append(i)


kDFS(G)
print("======================================================\n")
kBFS(G)
import matplotlib.pyplot as plt
nx.draw_networkx(G,with_labels=True, 
    pos=nx.spring_layout(G), 
    node_color='r', 
    edge_color='b')
plt.show()
#print (G.number_of_nodes())
#print (G.number_of_edges())


               
        
