# Given V=sbunny_v and F=sbunny_f, print out the vertex-to-face relations
vf, ni = igl.vertex_triangle_adjacency(sbunny_f, sbunny_v.shape[0])

#Extra information
print('sbunny_f', sbunny_f)
print ('size of sbunny_v', sbunny_v.shape[0])
print ('vf',vf)
print ('ni', ni);
print ('size of ni', ni.shape[0])
print ('size of vf', vf.shape[0])

adj_list=[]

for i in range (sbunny_v.shape[0]):
    faces=[]
    for j in range (sbunny_f.shape[0]):
        inner=ni[i]+j
        if inner<vf.shape[0]:
            f=vf[inner]
            if f not in faces:
                faces.append(str(f))
    adj_list.append([str(sbunny_v[i]),faces])

f = open('NeighborhoodRelations.txt', 'w')

f.write(adj_list)
f.write('---------------------------------------------------------------------------\n')

# Given V=sbunny_v and F=sbunny_f print out the vertex-to-vertex relations
connections = igl.adjacency_list(sbunny_f)

adj_list = []
for i in range (sbunny_v.shape[0]):
    adj_list.append([i, connections[i]])

f = open('NeighborhoodRelations.txt', 'w')
f.write(adj_list)
f.write('---------------------------------------------------------------------------\n')