#K-closest points
import random
from typing import List
import heapq
from time import time
x_range=10000
y_range=10000
point_count=5000000
points=[(random.randint(0,x_range), random.randint(0,y_range)) for i in range(point_count)]

def kClosest(points: list, k: int) -> List[List]:
	closest_points={}
	for point in points:
		dist=sum([point[i]**2 for i in range(len(point))])
		closest_points[point]=dist

	return sorted(closest_points.items(), key=lambda kv: kv[1])[:k]

def kClosestHeap(points: list, k: int) -> List[List]:
	heap=[]
	for x,y in points:
		dist=-(x**2+y**2)
		if len(heap)==k:
			heapq.heappushpop(heap, (dist,(x,y)))
		else:
			heapq.heappush(heap, (dist,(x,y)))

	return [point for (dist,(point)) in heap][::-1]

start=time()
print(kClosest(points, 5))
end=time()
print("Time taken to find K-closest without heap: {:.3f} seconds".format(end-start))

start=time()
print(kClosestHeap(points, 5))
end=time()
print("Time taken to find K-closest with heap: {:.3f} seconds".format(end-start))

