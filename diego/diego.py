#!/usr/bin/python
from matplotlib import *
from numpy import *
from scipy import *
from matplotlib import *
from pylab import *
########################################################################
#Ordem das colunas do arquivo table3_diego
#ID		Teff	sigma_Teff		[Fe/H]		sigma_[Fe/H]	log(g)		sigma_log(g)	FHa		sigma_inf_FHa	sigma_sup_FHa	Firt	sigma_inf_Firt	sigma_sup_Firt

with open("C:\Users\Ellen\Desktop\may_2018\python_ic\diego\table3_diego.txt") as f:
	data = f.read()
	
data = data.split('\n')
data.pop()

#Nomenclatura HIP e tipos espectrais
#HIP	ST

with open("C:\Users\Ellen\Desktop\may_2018\python_ic\diego\hip_st.txt") as f:
	hip_st = f.read()
	
hip_st = hip_st.split('\n')
hip_st.pop()

#Nomenclatura NLTT e magnitude V
with open("C:\Users\Ellen\Desktop\may_2018\python_ic\diego\nltt_v.txt") as f:
	nltt_v = f.read()
	
nltt_v = nltt_v.split('\n')
nltt_v.pop()

ID = [row.split(';')[0] for row in data]
teff = [float(row.split(';')[1]) for row in data]
feh = [float(row.split(';')[3]) for row in data]
Firt = [float(row.split(';')[10]) for row in data]
HIP = [row.split(';')[0] for row in hip_st]
ST = [row.split(';')[1] for row in hip_st]
NLTT = [row.split(';')[0] for row in nltt_v]
V = [float(row.split(';')[1]) for row in nltt_v]

#Lista de estrelas ja observadas
observadas = ['HIP87937','HIP36208','HIP80824','HIP82809','HIP72944','HIP68469',
'HIP49986','HIP78353','HIP88574','HIP117473','HIP113296','HIP51007','HIP25878','HIP113576']

comum_teff = []
comum_flux = []
for i in range(len(data)):
	for j in range(len(observadas)):
		if ID[i]==observadas[j] or HIP[i]==observadas[j] or NLTT[i]==observadas[j]:
			comum_teff.append(teff[i])
			comum_flux.append(Firt[i])
			
#Parte grafica

scatter(comum_teff,comum_flux,color='red')
xlabel('Teff')
ylabel('Fluxo absoluto')
title('Estrelas do Diego observadas')
axis([2700,4300,-0.1,5])
xticks(range(2700,4300,100))
show()
