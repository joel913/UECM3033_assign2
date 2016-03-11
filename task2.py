import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import linalg
import copy


def image_svd(n):
    img=mpimg.imread('rainbow.jpg')

    [j,k,m] = [img[:,:,i] for i in range(3)]
        
    j1, j2, j3 = linalg.svd(j)
    k1, k2, k3 = linalg.svd(k)
    m1, m2, m3 = linalg.svd(m)
    
    j2_nonzero=(j2!=0).sum()
    k2_nonzero=(k2!=0).sum()
    m2_nonzero=(m2!=0).sum()
    print("The number of non zero elements in decompose sigma of red, green, blue matrices are", j2_nonzero,"," ,k2_nonzero,"and" ,m2_nonzero, "respectively.")
    
    
    j2[n:800] = np.zeros_like(j2[n:800])
    k2[n:800] = np.zeros_like(k2[n:800])
    m2[n:800] = np.zeros_like(m2[n:800])
    
    j2 = linalg.diagsvd(j2,800,1000)
    k2 = linalg.diagsvd(k2,800,1000)
    m2 = linalg.diagsvd(m2,800,1000)
    
    j_new = np.dot(j1, np.dot(j2, j3))
    k_new = np.dot(k1, np.dot(k2, k3))
    m_new = np.dot(m1, np.dot(m2, m3))
      
    img[:,:,0]=j_new
    img[:,:,1]=k_new
    img[:,:,2]=m_new
    
    fig2 = plt.figure(2)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(j_new, cmap = 'Blues')
    ax3.imshow(k_new, cmap = 'Reds')
    ax4.imshow(m_new, cmap = 'Greens')
    plt.show() 
    

img=mpimg.imread('rainbow.jpg')
img_ori = copy.deepcopy(img)
[j,k,m] = [img[:,:,i] for i in range(3)]
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img_ori)
ax2.imshow(j, cmap = 'Blues')
ax3.imshow(k, cmap = 'Reds')
ax4.imshow(m, cmap = 'Greens')
plt.show()


#keep the first n none zero elements in sigma.input n into image_svd.
#image_svd(30)


image_svd(200)


