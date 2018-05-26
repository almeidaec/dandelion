#!/usr/bin/python
from matplotlib import *
from numpy import *
from scipy import *
from matplotlib import *
from pylab import *

#-------------------------ARQUIVO AMOSTRA WINTERS-----------------------

#Ordem das colunas do arquivo winters_2015.tsv
#ID	Nc	Np	alpha	delta	pm	pmPA	plx	Bmag	Fmag	Nmag	Vmag	Rmag	Imag	Jmag	Hmag	Kmag	2M	dbest	f_dbest	n_dbest	SimbadName

with open("/home/ellen/Documentos/python_ic/winters_2015.tsv") as f:
	data = f.read()
	
data = data.split('\n')
data.pop()
data.pop()	

	
#-------------------------LIMPEZA DAS ESTRELAS NAO DESEJADAS
sID = [row.split('\t')[0] for row in data]
sVmag = [row.split('\t')[11] for row in data]
sRmag = [row.split('\t')[12] for row in data]
sImag = [row.split('\t')[13] for row in data]
sJmag = [row.split('\t')[14] for row in data]
sHmag = [row.split('\t')[15] for row in data]
sKmag = [row.split('\t')[16] for row in data]
sdbest = [row.split('\t')[18] for row in data]

#-------------------------Limpar as estrelas com V>13:
index_sVmag=[]
for i in range(0,1735):
	if sVmag[i]=='     ' or float(sVmag[i])>13:
		index_sVmag.append(i)
		
for i in reversed(range(0,len(index_sVmag))):
	data.pop(index_sVmag[i])
	
#-------------------------Limpar estrelas com d>20pc
index_d=[]
d = [float(row.split('\t')[18]) for row in data]

for i in range(0,len(data)):
	if d[i] > 20:
		index_d.append(i)
		
for i in reversed(range(0,len(index_d))):
	data.pop(index_d[i])
	
#-------------------------Nomenclatura correta
with open("/home/ellen/Documentos/python_ic/nomes_winters_simbad.txt") as f:
	WID = f.read()
	
WID = WID.split('\n')
WID.pop()	

#-------------------------Dados  em float

#WID = nomes em HIP, GJ e LTT
W_old_ID = [row.split('\t')[0] for row in data]
Walpha = [row.split('\t')[3] for row in data]
Wdelta = [row.split('\t')[4] for row in data]
WCOOR = [a+';'+b for a,b in zip(Walpha,Wdelta)]
Wpm = [float(row.split('\t')[5]) for row in data]
WV = [float(row.split('\t')[11]) for row in data]
WR = [float(row.split('\t')[12]) for row in data]
WI = [float(row.split('\t')[13]) for row in data]
WJ = [float(row.split('\t')[14]) for row in data]
WH = [float(row.split('\t')[15]) for row in data]
WK = [float(row.split('\t')[16]) for row in data]
Wdbest = [float(row.split('\t')[18]) for row in data]


#-------------------------DIVISOES DOS DADOS WINTERS

#D1 - V<=10 E D<=10 [BLUE]
WD1=[]
for i in range(0,len(data)):
	if WV[i]<=10 and Wdbest[i]<=10:
		WD1.append(data[i])
		
#D2 - 10<V<12 E D<10 [GREEN]
WD2=[]
for i in range(0,len(data)):
	if WV[i]>10 and WV[i]<12 and Wdbest[i]<10:
		WD2.append(data[i])
		
#D3 - 10<V<12 E d>10 [ORANGE]
WD3=[]
for i in range(0,len(data)):
	if WV[i]>10 and WV[i]<12 and Wdbest[i]>10:
		WD3.append(data[i])
		
#D4 - 12<=V<=13 [RED]
WD4=[]
for i in range(0,len(data)):
	if WV[i]>=12 and WV[i]<=13:
		WD4.append(data[i])

#----------------------QUADRANTES	
WQ = []
for i in range(len(data)):
	if (WV[i]<=10.):
		WQ.append('Q1Q2')
	if (WV[i]>10.) and (WV[i]<=12.) and (Wdbest[i]<=10.):
		WQ.append('Q3')
	if (WV[i]>10.) and (WV[i]<=11.) and (Wdbest[i]>10.):
		WQ.append('Q4')
	if (WV[i]>11.) and (WV[i]<=12.) and (Wdbest[i]>10.):
		WQ.append('Q5')
	if (WV[i]>12.) and (WV[i]<=13.):
		WQ.append('Q6')	
	else:
		WQ.append('sem_Q')	
				
#-------------------------Operacoes com os dados WINTERS
WJH = [j-h for j,h in zip(WJ,WH)]
WVJ = [v-j for v,j in zip(WV,WJ)]
WVR = [v-r for v,r in zip(WV,WR)]
WRJ = [r-j for r,j in zip(WR,WJ)]                           #Cor J-H
WRK = [r-k for r,k in zip(WR,WK)]                           #Cor R-K
WMv = [v + 5 - 5*log10(d) for v,d in zip(WV,Wdbest)]
WHr = [r + 5 + 5*log10(m) for r,m in zip(WR,Wpm)]

#-------------------------MANN_EQUATION_4-------------------------------
teff_mann = []

for i in range(len(data)):
	t = 3500*(2.796-1.421*WVJ[i]+0.4284*WVJ[i]*WVJ[i]-0.06133*WVJ[i]*WVJ[i]+0.00331*WVJ[i]*WVJ[i]*WVJ[i]+0.1333*WJH[i]-0.05416*WJH[i]*WJH[i])
	teff_mann.append(WID[i]+';'+str(t))	

f=open('uauuuu.txt','w')
for ele in teff_mann:
    f.write(ele+'\n')
f.close()

#----------------ST------------------
valores = [0.910,0.939,0.934,0.968,1.038,
1.044,1.083,1.157,1.252,1.336,1.515,1.558,
1.770,2.110,2.150,2.290,2.207,2.295,2.310]
spt = ['M0','M0.5','M1','M1.5','M2','M2.5',
'M3','M3.5','M.4','M4.5','M5','M5.5','M6',
'M6.5','M7','M7.5','M8','M8.5','M9.5']

WST = []

for i in range(len(data)):
		for j in range(len(spt)):
			if WVR[i] >= valores[j] and WVR[i] < valores[j+1]:
				WST.append(spt[j])

				
print WID[300],WST[300],WVR[300],WRK[300]
