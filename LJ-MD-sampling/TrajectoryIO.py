import numpy as np


def writePostionsToFileXYZ(filename,postions,particle_names,cell=None,append=True):
    num_particles = postions.shape[0]
    if len(particle_names)==1: particle_names = particle_names*num_particles
    if append:
        f = open(filename,'a')
    else:
        f = open(filename,'w')

    f.write("  {0}\n\n".format(num_particles))
    for i in range(num_particles):
        a = particle_names[i]
        p = postions[i]
        if cell is not None: p = p - np.floor(p/cell) * cell
        out_str = "  {0}   {1:20.9f}  {2:20.9f}  {3:20.9f}\n".format(a,p[0],p[1],p[2])
        f.write(out_str)
    f.close()
    #-------------------------------

def writePostionsToFileGro(filename,postions,particle_names,header,cell=None,append=True):
    num_particles = postions.shape[0]
    if len(particle_names)==1: particle_names = particle_names*num_particles
    if append:
        f = open(filename,'a')
    else:
        f = open(filename,'w')
    f.write("  {0}\n".format(header))
    f.write("  {0}\n".format(num_particles))
    for i in range(num_particles):
        rstr = "SOL"
        a = particle_names[i]
        p = postions[i]
        if cell is not None: p = p - np.floor(p/cell) * cell
        out_str = "{0:5d}{1:5s}{2:5s}{3:5d}{4:8.3f}{5:8.3f}{6:8.3f}\n".format(i,rstr,a,i,p[0],p[1],p[2])
        f.write(out_str)
    if cell is not None:
        out_str = "{0:10.5f}{1:10.5f}{2:10.5f}\n".format(cell[0],cell[1],cell[2])
        f.write(out_str)
    f.close()
    #-------------------------------

def readPostionsFromFileGro(filename):
    f = open(filename,'r')
    rawdata = f.readlines()
    f.close()
    #
    num_particles = int(rawdata[1])
    #
    cell_str = rawdata[-1]
    cell = []
    cell.append(float(cell_str[0:10]))
    cell.append(float(cell_str[10:20]))
    cell.append(float(cell_str[20:30]))
    cell = np.array(cell)
    postions = np.zeros([num_particles,3])
    #
    for i in range(num_particles):
        l = rawdata[i+2]
        postions[i][0] = float(l[20:28])
        postions[i][1] = float(l[28:36])
        postions[i][2] = float(l[36:44])
    return postions,cell
#-------------------------------
