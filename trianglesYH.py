def triangles(max):
    a=1
    tris=[1]
    yield(tris)
    while a<max:
        trins=[0] + tris[:] + [0]
        tris = [trins[n] + trins[n+1] for n in range(len(trins)-1)]
        yield(tris)
        a += 1
       
t = triangles(6)
print(type(t))
        
