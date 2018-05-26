#!/usr/bin/python
from matplotlib import *
from numpy import *
from scipy import *
from matplotlib import *
from pylab import *
########################################################################
#Ordem das colunas do arquivo parametros_hip
#HIP	ST	[Fe/H]	sigma_[Fe/H]	Teff	sigma_Teff

with open("/home/ellen/Documentos/python_ic/hiparcos/parametros_hip.txt") as f:
	data = f.read()
	
data = data.split('\n')
data.pop()

HIP= [row.split(';')[0] for row in data]
teff = [float(row.split(';')[4]) for row in data]
feh = [float(row.split(';')[2]) for row in data]

scatter(teff,feh,color='green')
xlabel('Teff')
ylabel('[Fe/H]')
title('Hiparcos com parametros')
#xticks(range(2700,4300,100))
show()
