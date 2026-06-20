from queue import PriorityQueue

from egz1atesty import runtests

inf = float('inf')


def v_to_all(G: list[list[tuple[int,int]]], v:int):
	n = len(G)
	weights = [inf] * n
	to_do = n
	pq = PriorityQueue()
	pq.put((0, v))
	while not pq.empty() and to_do > 0:
		min_w, u = pq.get()
		if min_w < weights[u]:
			weights[u] = min_w
			to_do -= 1
			for v, w in G[u]:
				if weights[v] == inf:
					pq.put((weights[u] + w, v))
	return weights

def E_to_G(E: list[tuple[int, int, int]]):
	n = max(max([e[0] for e in E]), max([e[1] for e in E])) + 1
	G = [[] for _ in range(n)]
	for u,v,w in E:
		G[u].append((v,w))
		G[v].append((u,w))
	return G

def armstrong(B, G, s, t):
	G = E_to_G(G)
	s_weights = v_to_all(G, s)
	t_weights = v_to_all(G, t)

	best_time = s_weights[t]
	for v,m,d in B:
		time = s_weights[v]
		time += (t_weights[v] * m) // d
		best_time = min(best_time, time)

	return best_time


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(armstrong, all_tests=True)
