import numpy

def initialisation(m, n):
    # on peut bien faire return numpy.hstack(( numpy.random.randn(m, n), numpy.ones((m, 1)) )), mais pas assez lisible
    alea = numpy.random.randn(m, n)
    ones = numpy.ones((m, 1))
    return numpy.hstack((alea, ones))