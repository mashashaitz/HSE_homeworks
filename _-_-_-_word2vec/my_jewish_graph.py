import sys
import gensim, logging
import networkx as nx
import matplotlib.pyplot as plt 

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


m = 'ruscorpora_upos_skipgram_300_5_2018.vec.gz'
if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.KeyedVectors.load(m)
    
    
model.init_sims(replace=True)


words = ['раввин_NOUN', 'талмуд_NOUN', 'хедер_NOUN', 'шмон_NOUN', 'мусор_NOUN', 'халява_NOUN', 'ермолка_NOUN', 'кипа_NOUN', 'еврей_NOUN', 'иудей_NOUN', 'еврейка_NOUN', 'иудаизм_NOUN', 'антисемитизм_NOUN', 'маца_NOUN']


G = nx.Graph()
G.add_nodes_from(words)


for i, word in enumerate(words):
    for j, other_word in enumerate(words):
        if j > i and model.similarity(word, other_word) > 0.5:
            G.add_edge(word, other_word)
            
            
nx.write_gexf(G, 'graph_file.gexf')


pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='red', node_size=10)
nx.draw_networkx_edges(G, pos, edge_color='yellow')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='Arial')
plt.axis('off') 
plt.show()


deg = nx.degree_centrality(G)
print('самое центральное слово графа:')
print(sorted(deg, key=deg.get, reverse=True)[0])


print('коэффициент кластеризации:')
print(nx.average_clustering(G))


for word in words:
    if G.neighbors(word) == []:
        G.remove_node(word)

print('у нас всего одна компонента связности, ее радиус:')
print(nx.radius(G))
