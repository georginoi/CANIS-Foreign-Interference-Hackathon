import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

df = pd.read_excel('dataset.xlsx')

df['Total Followers'] = df[['X (Twitter) Follower #', 'Facebook Follower #', 'Instagram Follower #']].sum(axis=1)

top_entities = df.nlargest(5, 'Total Followers')['Name (English)']

G = nx.DiGraph()

for _, row in df.iterrows():
    entity = row['Name (English)']
    parent = row['Parent entity (English)']
    G.add_node(entity, type='entity')
    G.add_node(parent, type='parent')
    G.add_edge(entity, parent)

    if pd.notna(row['X (Twitter) Follower #']) and row['X (Twitter) Follower #'] > 0:
        G.add_node(f"{entity} Twitter", type='platform')
        G.add_edge(entity, f"{entity} Twitter")
    if pd.notna(row['Facebook Follower #']) and row['Facebook Follower #'] > 0:
        G.add_node(f"{entity} Facebook", type='platform')
        G.add_edge(entity, f"{entity} Facebook")
    if pd.notna(row['Instagram Follower #']) and row['Instagram Follower #'] > 0:
        G.add_node(f"{entity} Instagram", type='platform')
        G.add_edge(entity, f"{entity} Instagram")

color_map = []
size_map = []
labels = {}
for node in G:
    if G.nodes[node]['type'] == 'entity':
        color_map.append('skyblue')
        size_map.append(300)
        labels[node] = node if node in top_entities.values else ''
    elif G.nodes[node]['type'] == 'parent':
        color_map.append('lightgreen')
        size_map.append(700)
    else:
        color_map.append('orange')
        size_map.append(100)

plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, k=0.5, iterations=50)
nx.draw_networkx_nodes(G, pos, node_color=color_map, node_size=size_map, alpha=0.7)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
nx.draw_networkx_labels(G, pos, labels, font_size=8)

plt.title('Network Diagram of Entities and their Parent Organizations with Social Media Presence')
plt.axis('off')
plt.savefig('network.png')
