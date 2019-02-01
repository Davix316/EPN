
# -- coding: utf-8 --

import numpy

data = numpy.memmap("lion.wav", dtype='h', mode='r')
print ("VALUES:",data)

import numpy, pylab
data = numpy.memmap("lion.wav", dtype='h', mode='r')
print (data)
pylab.plot(data)
pylab.show()

