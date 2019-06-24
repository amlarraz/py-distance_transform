import numpy as np

# Distance transform for a 1-dimensional vector using square distance
def dt(vector, n, inf=1e20):
    f = vector
    d = np.zeros(n, dtype=np.float64)
    v = np.zeros(n, dtype=int)
    z = np.zeros(n+1, dtype=np.float64)
    z[0] = -inf
    z[1] = inf
    k = 0
    for q in range(n)[1:]:
        s = ((f[q]+ q*q) - (f[v[k]] + v[k]*v[k]))/(2*q-2*v[k])
        while s<= z[k]:
            k -= 1
            s  = ((f[q]+q*q)-(f[v[k]]+v[k]*v[k]))/(2*q-2*v[k])
        k +=1
        v[k] = q
        z[k] = s
        z[k+1] = inf

    k=0
    for q in range(n):
        while (z[k+1] < q):
            k +=1
        d[q] = (q-v[k])*(q-v[k]) + f[v[k]]
    
    return d

# Distance transform for a 2-dimensional vector using square distance
def dt_img(image):
    height = image.shape[0]
    width = image.shape[1]
    # Columns
    for x in range(width):
        f = image[:,x]
        image[:,x] = dt(f, height)
    # Rows
    for y in range(height):
        f = image[y,:]
        d = dt(f, width)
        image[y,:] = d
    return image

# Distance transform for a 2-dimensional binary vector using square distance
def dt_img_bin(image, inf=1e20, on=0):
    # image: 0:object, other_value:bg
    height = image.shape[0]
    width = image.shape[1]
    out = np.ones([height, width], dtype=np.float64)*inf
    out[image==on]=0
    out = dt_img(out)
    
    return out

def to_grayscale(image):
    scale = 255./(np.max(image) - np.min(image))
    gray = (image - np.min(image))*scale

    return gray
