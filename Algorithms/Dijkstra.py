'''
Dijkstras's algorithms finds a path to a goal by taking the least weight edge between nodes
All weights need to be positive in order to funtion 

Breadth-first is a similar algorithms but finds shortest segments to goal 

Both use hash tables!
'''

def find_lowest_cost_node(costs: dict):
    pass

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  #go through all neighbors of this node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:     #if it's cheaper to get to this neighbor by going through this node...
            costs[n] = new_cost     #update the cost for this node
            parents[n] = node       #this node becomes the new parent for this neighbor
    processed.append(node)          #mark node as processed
    node = find_lowest_cost_node(costs) #find the next node to the processes and loop
