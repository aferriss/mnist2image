import os, struct
from array import array as pyarray
from numpy import append, array, int8, uint8, zeros
from pylab import *
from numpy import *
from PIL import Image

# data from  http://yann.lecun.com/exdb/mnist/
#sliced from here http://g.sweyla.com/blog/2012/mnist-numpy/

def load_mnist(dataset="training", digits=np.arange(10), path='.'):
	fname_img = os.path.join(path, 'train-images-idx3-ubyte')

	fimg = open(fname_img, 'rb')
	magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
	img = pyarray("B", fimg.read())
	fimg.close()

	ind = [ k for k in range(size) ]
	N = len(ind)


	images = zeros((N, rows, cols), dtype=uint8)
	for i in range(len(ind)):
		images[i] = array(img[ind[i]*rows*cols : (ind[i]+1)*rows*cols ]).reshape((rows, cols))

	return images

images = load_mnist('training', digits='0')

for i in range(60000):
	im = Image.fromarray(images[i])
	im.save("numbers/img"+str(i)+".jpg")


