import igraph as ig

g = ig.Graph(directed=True)

v = {'A', 'B', 'C', 'D'}
e = {('A', 'B'), ('A', 'C'), ('B', 'D'), ('D', 'C')}

v = list(v)
e = list(e)

g.add_vertices(v)
g.vs['label'] = v
g.add_edges(e)


visual_style = {}
#visual_style["bbox"] = 
visual_style['margin'] = 60
visual_style['edge_color'] = 'grey'
visual_style['vertex_color'] = 'orange'
visual_style['layout'] = g.layout('auto')

ig.plot(g, target='graph.pdf', **visual_style)
