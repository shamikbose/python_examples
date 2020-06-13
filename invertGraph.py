import numpy as np
import pandas as pd
test={1: [2, 4], 2: [4,1], 3: [5], 4: [2, 3], 5:[2,1,3]}
adj_matrix=np.zeros((len(test),len(test)))
for key in test.keys():
	edges=test[key]
	for edge in edges:
		adj_matrix[key-1][edge-1]=1
adj_matrix=np.transpose(adj_matrix)
test_out={}
for count, row in enumerate(adj_matrix):
	test_out[count+1]=[]
	for count_in, el in enumerate(row):
		if adj_matrix[count][count_in]==1:
			#print(count+1,test_out[count+1])
			test_out[count+1].append(count_in+1)
print(test_out)