#!/usr/bin/python
from matplotlib import *
from numpy import *
import os
import glob
from scipy import *
from matplotlib import *
from pylab import *
########################################################################
#Dados Winters et al. 2015 com magnitude V<13 e d<=20pc
#Tabela com os dados -> winters15.txt
#ID;Nc;Np;alpha;delta;pm;pmPA;plx;Bmag;Fmag;Nmag;Vmag;Rmag;Imag;Jmag;Hmag;Kmag;2M;dbest;f_dbest;n_dbest;SimbadName(SN);GJ;Gaia DR1;HD;2MASS;NLTT;LTT;HIP;L;LHS;GL

with open("/home/ellen/Documentos/python_ic/winters/winters15.txt") as f:
	data = f.read()
	
data = data.split('\n')
data.pop()

#IDs
SN = [row.split(';')[21] for row in data]
GJ = [row.split(';')[22] for row in data]
Gaia = [row.split(';')[23] for row in data]
HD = [row.split(';')[24] for row in data]
N2MASS = [row.split(';')[25] for row in data]
NLTT = [row.split(';')[26] for row in data]
LTT = [row.split(';')[27] for row in data]
HIP = [row.split(';')[28] for row in data]
L = [row.split(';')[29] for row in data]
LP = [row.split(';')[30] for row in data]
LHS = [row.split(';')[31] for row in data]

#Data 
alpha = [row.split(';')[3] for row in data]
delta = [row.split(';')[4] for row in data]
coor = [a+';'+b for a,b in zip(alpha,delta)]
pm = [float(row.split(';')[5]) for row in data]
V = [float(row.split(';')[11]) for row in data]
R = [float(row.split(';')[12]) for row in data]
I = [float(row.split(';')[13]) for row in data]
J = [float(row.split(';')[14]) for row in data]
H = [float(row.split(';')[15]) for row in data]
K = [float(row.split(';')[16]) for row in data]
dbest = [float(row.split(';')[18]) for row in data]	
ST = [row.split(';')[32] for row in data]


def final_name():
	'''Nomenclatura por importancia de catalogo -> HIP,GJ,LTT,NLTT,L,LHS,HD,2MASS E Gaia'''
	final_name=[]
	for i in range(len(data)):
		if HIP[i] != '-':
			final_name.append(HIP[i])
		else:
			if GJ[i] != '-':
				final_name.append(GJ[i])
			else:
				if LTT[i]!=	'-':
					final_name.append(LTT[i])
				else:
					if NLTT[i]!='-':
						final_name.append(NLTT[i])
					else:
						if L[i]!='-':
							final_name.append(L[i])
						else:
							if LHS[i]!='-':
								final_name.append(LHS[i])
							else:
								if LP[i]!='-':
									final_name.append(LP[i])
								else:
									if HD[i]!='-':
										final_name.append(HD[i])
									else:
										if N2MASS[i]!='-':
											final_name.append(N2MASS[i])
										else:
											if Gaia[i]!='-':
												final_name.append(Gaia[i])
											else:
												final_name.append(SN[i])
	f=open('final_name.txt','w')
	for ele in final_name:
		f.write(ele+'\n')
	f.close()																		
		
def observed_mission(mission_folder,save=False):
	stars = []
	observed = []
	folders = glob.glob(mission_folder+'*')
	for i in range(len(folders)):
		files = glob.glob(folders[i]+'/*.fits')
		for j in range(len(files)):
			symbol = '/'
			position = [pos for pos, char in enumerate(files[j]) if char == symbol]
			stars.append(files[j][(position[-1]+1):-22].upper())					
	for k in stars:
		if k[:4] != 'BIAS' and k[:2] != 'FF' and k[:4] != 'THAR' and k[:4] != 'LIXO' and k[:4] != 'FOCO' and k not in observed:
			if k[-5:-1] == '_EXP':
				if k[:-5] not in observed:	
					observed.append(k[:-5])	
			if k[-2] == 'S':
				if k[:-3] not in observed:	
					observed.append(k[:-3])		
			else:
				observed.append(k)																
	if save == 'True':
		f=open('observed_'+mission_folder[-4:-1]+'.txt','w')
		for ele in observed:
			f.write(ele+'\n')
		f.close()
	if save == 'False':
		print observed

def observed(save=False):
	with open("/home/ellen/Documentos/python_ic/winters/input_eo.txt") as f:
		input_eo = f.read()
	input_eo = input_eo.split('\n')
	input_eo.pop()
	observed = []
	for i in input_eo:
		if (i in SN) or (i in GJ) or (i in Gaia) or (i in HD) or (i in N2MASS) or (i in NLTT) or (i in LTT) or (i in HIP) or (i in L) or (i in LHS) or (i in LP):
			if i not in observed:
				observed.append(i)
	if save == False:
		print 'Observadas '+str(len(observed))+' estrelas de '+str(len(data))+'.', observed
	if save == True:
		observed.append('Observadas '+str(len(observed))+' estrelas de '+str(len(data))+'.')
		f=open('observed_winters.txt','w')
		for ele in observed:
			f.write(ele+'\n')
		f.close()				

observed(save=True)				
