'''Come prima cosa determinate dei valori di n, p e m tali che la procedura ER e la procedura UPA generino un grafo
con lo stesso numero di nodi ed un numero di archi simile a quello della rete reale.

Quindi, per ognuno dei tre grafi (rete reale, ER, UPA), simulate un attacco che disabiliti i nodi
della rete uno alla volta seguendo un ordine casuale, fino alla disattivazione di tutti i nodi del grafo,
e calcolate la resilienza del grafo dopo ogni rimozione di un nodo.

Dopo aver calcolato la resilienza dei tre grafi, mostrate il risultato in un grafico con scala
lineare (non log/log) che combini le tre curve ottenute. Usate un grafico a punti oppure a linea
per ognuna delle curve.
L'asse orizzontale del grafico deve corrispondere al numero di nodi disattivati dall'attacco (che variano da 0 a n),
mentre l'asse verticale alla dimensione della componente connessa più grande rimasta dopo aver rimosso un certo numero di nodi.
Aggiungete una legenda al grafico che permetta di distinguere le tre curve e che specifici i valori di p e m utilizzati.
Allegate il file con la figura nell'apposito spazio.'''

from utils.generateUndirectedGraphFromFile import generateUndirectedGraphFromFile
from utils.generateUndirectedGraphER import generateUndirectedGraphER
n = 1476
p = 0.15 #(n archi*100/n^2)
m = 1

generalGraph = generateUndirectedGraphFromFile("as19991212.txt")
ERgraph = generateUndirectedGraphER(n,p)
# UPAgraph =

def resilience(graph):
    color = ["white" for i in range(len(graph.V))]
    CC = []
    for i in range(len(graph.V)):
        if (color[i] == "white"):
            comp = DFSVisited(graph,i,[])

def DFSVisited(graph,u,visited):
    
