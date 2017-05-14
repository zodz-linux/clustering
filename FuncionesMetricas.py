import numpy as np

def DistanciaEuclidiana(v1,v2):
    v1=np.array(v1)
    v2=np.array(v2)
    if v1.shape[0]!=v1.shape[0]:
        print "Error: vectores de diferente  longitud"
        return  0
    if  sum((v1-v2)) == 0.0:
        return 0.0
    value=0.0
    value=sum((v1-v2)**2)
    return value

def Norma(v1):
    v1=np.array(v1)
    value=np.sqrt(v1.dot(v1))
    return value

def DistanciaManhattan(v1,v2):
    v1=np.array(v1)
    v2=np.array(v2)
    if v1.shape[0]!=v1.shape[0]:
        print "Error: vectores de diferente  longitud"
        return  0
    return sum((v1-v2))

def SimilaridadCoseno(v1,v2):
    v1=np.array(v1)
    v2=np.array(v2)
    if DistanciaManhattan(v1,v2) == 0.0:
        return 0.0
    value=0
    value+=v1.dot(v2)
    value/=(Norma(v1)*Norma(v2))
    return value

## Metricas entre clusters
def DistanciaIntraCluster(centroides,clusters,funcionDistancia):
    value=0
    for index in xrange(len(centroids)):
        for  vector in clusters[index]:
            value+=funcionDistancia(vector,centroids[index])
    return value
