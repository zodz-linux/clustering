import numpy as np

def Compute_Mean_Vector(vectors):
    dimension=len(vectors[0])
    media=np.zeros(dimension)
    for v in vectors:
        media+=np.array(v)
    media/=len(vectors)
    media=list(media)
    return media

def ComputeClusters(centroids,vectors,k,DistanceFunction):
    clusters=[[] for i in xrange(k)]
    for current_v in vectors:
        current_index=0
        current_distance=9e4
        for centroid in centroids:
            aux=DistanceFunction(current_v,centroid)
            if (aux < current_distance):
                current_distance=aux
                index=current_index
            current_index+=1
        clusters[index].append(current_v)
    return clusters

def kmeans(vectors,k,iterations,DistanceFunction):
    dimension=len(vectors[0])
    np.random.shuffle(vectors)
    current_centroids=vectors[-k:]
    it=0
    while it <=iterations:
        clusters=ComputeClusters(current_centroids,vectors,k,DistanceFunction)
        current_centroids=[Compute_Mean_Vector(group) for group in clusters]
        it+=1
    return centroids,clusters
