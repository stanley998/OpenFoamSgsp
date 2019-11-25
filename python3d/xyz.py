from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def dd(*args):# {{{
    '''debugging function, much like print but handles various types better'''
    print()
    for struct in args:
        if isinstance(struct, list):
            for i in struct:
                print(struct)
        elif isinstance(struct, tuple):
            for i in struct:
                print(i)
        elif isinstance(struct, dict):
            for k, v in struct.items():
                print (str(k)+':', v)
        else:
            print(struct)
# }}}
def LoG(x, y, sigma):# {{{
    temp = (x ** 2 + y ** 2) / (sigma ** 2)
    return -1 / (np.pi * sigma ** 4) * (1 - temp) * np.exp(-temp)
# }}}

def fsin():# {{{
    N = 5
    X, Y= np.meshgrid(np.arange(-N,N,0.1), np.arange(-N,N,0.1))
    Z = np.sin(X ** 2 + Y ** 2 ) / (X ** 2 + Y ** 2)
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z)
# }}}
def fbell():# {{{
    N = 50
    X, Y = np.meshgrid(range(-N,N), range(-N,N))
    Z = -LoG(X, Y, sigma=20)
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z)
# }}}

#fsin()
fbell()
