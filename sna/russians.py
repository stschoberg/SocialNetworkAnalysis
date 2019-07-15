import networkx as nx
import urllib
import matplotlib

def read_lj_friends(g, name):
    response = urllib.urlopen('https://www.livejournal.com/misc/fdata.bml?user=valerois')

    for line in response.readlines():
        # Ignore comment lines
        if line.startswith('#'):continue

        parts = line.split()
        # Ignore empty lines
        if len(parts) == 0: continue

        if parts[0][0] == '<':
            g.add_edge(parts[1], name)
        else:
            g.add_edge(name, parts[1])

g = nx.Graph()
read_lj_friends(g, 'valerois')
nx.draw(g)
