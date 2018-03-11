import numpy as np

# the 2d array of our samples,
# each component is a category label

# 
def one_2d_to_3d(a,new_dim):
# the 3d array that will be the one-hot representation
# a.max() + 1 is the number of labels we have
    # print a
    # print a.shape
    b = np.zeros(( a.shape[0], a.shape[1], new_dim))

    # if you visualize this as a stack of layers,
    # where each layer is a sample,
    # this first index selects each layer separately
    layer_idx = np.arange(a.shape[0]).reshape(a.shape[0], 1)

    # this index selects each component separately
    component_idx = np.tile(np.arange(a.shape[1]), (a.shape[0], 1))

    # then we use `a` to select indices according to category label
    b[layer_idx, component_idx, a] = 1

    b = b.transpose(1,0,2)
    # voila!
    # print(b)

    # print b.shape

    return b


def uncompress(a,num_dim):
    # 

    ans = []
    for x in a:

        oh = one_2d_to_3d(np.squeeze(x),num_dim)
        # print 'oh',oh.shape
        ans.append(oh)

    ans2 = np.vstack(ans)

    ans2 = np.expand_dims(ans2,3)
    # print 'ans2', ans2

    # print ans2.shape

    return ans2

if __name__=='__main__':
    
    a = np.arange(12).reshape(2,2,3,1)
    print uncompress(a,12).shape
