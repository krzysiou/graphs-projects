import sys
import numpy as np

def generateVertices(N, layerSizes = []):
	
	N=N+2
	vertexInLayerCount=[0 for _ in range(N)]
	vertexInLayerCount[0]=vertexInLayerCount[-1]=1 

	for layer in range(1, N-1):
		if layerSizes != []:
			vertexInLayerCount[layer] = layerSizes[layer-1]
		else:
			vertexInLayerCount[layer] = np.random.randint(2, N-1)
	verticesPositionsDict={}
	layerVerticesList=[[] for _ in range(N)]
	index=1

	for layer in range(N):
		for i in range(vertexInLayerCount[layer]):
			verticesPositionsDict[index]=np.array([ layer , -i*2+vertexInLayerCount[layer]-1])
			layerVerticesList[layer].append(index)
			index+=1
			
	return verticesPositionsDict,layerVerticesList

def generateMinimalEdges(layerVerticesList):
	edges = []
	layers = len(layerVerticesList)

	for i in layerVerticesList[1]:
		edges.append([layerVerticesList[0][0], i])

	for i in layerVerticesList[layers-2]:
		edges.append([i, layerVerticesList[layers-1][0]])
	
	for i in range(1,layers-2):
		nextLayer=layerVerticesList[i+1]
		currentLayer=layerVerticesList[i]
		case=len(nextLayer)-len(currentLayer)
		
		if case == 0:
			nextCopy=nextLayer[:]
			for j in currentLayer:
				vertex = np.random.choice(nextCopy)
				edges.append([j, vertex])
				nextCopy.remove(vertex)
		elif case > 0:
			currentCopy=currentLayer[:]
			for j in nextLayer:
				if not currentCopy:
					currentCopy=currentLayer[:]
				vertex = np.random.choice(currentCopy)
				edges.append([vertex, j])
				currentCopy.remove(vertex)
		else:
			nextCopy=nextLayer[:]
			for j in currentLayer:
				if not nextCopy:
					nextCopy=nextLayer[:]
				vertex = np.random.choice(nextCopy)
				edges.append([j, vertex])
				nextCopy.remove(vertex)		
		
	return edges
		