class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        directions=collections.defaultdict(list)
        for u,v,i in times:
            directions[u].append((v,i))
        minHeap=[(0,k)]

        total=0
        seen=set()

        while minHeap:
            weight,node=heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            total=max(total,weight)
            for node2,weight2 in directions[node]:
                if node2 not in seen:
                    heapq.heappush(minHeap,(weight+weight2,node2))
        return total if len(seen)==n else -1





