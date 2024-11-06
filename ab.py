def is_leaf_node(graph,node):
    return len(graph[node]) == 0
def minimax(graph, values,node,depth, ismaximizingplayer, alpha, beta):
    if is_leaf_node(graph,node):  
        return values[node]
    if ismaximizingplayer:
        best = -1000
        for i in graph[node]:
            val = minimax(graph,values,i,depth+1, False, alpha, beta)
            best = max(best,val)
            alpha = max(alpha,best)
            if beta <= alpha:
                break
        return best 
    else:
        best = 1000
        for i in graph[node]:
            val = minimax(graph,values,i,depth+1, True, alpha, beta)
            best = min(best,val)
            beta = max(beta,best) 
            if beta <= alpha:
                break
        return best
    
graph = {
    "A" : ["B","C"],
    "B" : ["D","E"],
    "C" : ["F","G"],
    "D" : [],
    "E" : [],
    "F" : [],
    "G" : []
}
values = {
    "D" : 6,
    "E" : 3,
    "F" : 4,
    "G" : -1,
}
print("The optimal value is : ",minimax(graph,values,"A",0,True,-1000,1000))