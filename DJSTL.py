graph={}
graph['start']={}
graph['start']['f']=5
graph['start']['b']=2

graph['b']={}
graph['b']['f']=8
graph['b']['c']=7

graph['f']={}
graph['f']['e']=4
graph['f']['c']=2

graph['e']={}
graph['e']['c']=6
graph['e']['fin']=3

graph['c']={}
graph['c']['fin']=1

graph['fin']={}

#print(graph)

parents={}
parents['f']='start'
parents['b']='start'
parents['fin']=None

infinity=float('inf')
costs={}
costs['f']=5
costs['b']=2
costs['fin']=infinity
costs['c']=infinity
costs['e']=infinity
# # #{'a': 6, 'b': 2, 'fin': inf}
# # #node is   a   b   fin
#
processed=[]

def find_lowest_cost_node(costs):
     lowest_cost=float('inf')
     lowest_cost_node=None
     for node in costs:
         cost=costs[node]
         if cost<lowest_cost and node not in processed:
             lowest_cost=cost
             lowest_cost_node=node
     return lowest_cost_node

node=find_lowest_cost_node(costs)
#其实可以声明的是 while 每循环一次都会检测判断一次
while node is not None:
    cost=costs[node]
    neighbors=graph[node]
#   {'a': 3, 'fin': 5}
    for n in neighbors.keys():
        new_cost=cost+neighbors[n]
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)
    node=find_lowest_cost_node(costs)

print(costs)
print(parents)
