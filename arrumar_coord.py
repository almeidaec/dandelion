#!/usr/bin/python
from matplotlib import *
from numpy import *
from scipy import *
from matplotlib import *
from pylab import *
#-------------------------ARQUIVO AMOSTRA HIPARCOS----------------------
#Ordem das colunas do arquivo hiparcos.csv
#Numero	ID	COORD	plx	Umag	Bmag	Vmag	Rmag	Imag	Jmag	Hmag	Kmag	SpecType 
with open("/home/ellen/Documentos/python_ic/hiparcos_smg.csv") as f:
	hip_smg = f.read()
	
hip_smg = hip_smg.split('\n')
hip_smg.pop()

#-------------------------Dados HIPARCOS (ALGUNS SEM MAGNITUDE)
sHID = [row.split(';')[1] for row in hip_smg]
sHCOOR = [row.split(';')[2] for row in hip_smg]
sHplx = [row.split(';')[3] for row in hip_smg]
sHU = [row.split(';')[4] for row in hip_smg]
sHB= [row.split(';')[5] for row in hip_smg]
sHV= [row.split(';')[6] for row in hip_smg]
sHR = [row.split(';')[7] for row in hip_smg]
sHI = [row.split(';')[8] for row in hip_smg]
sHJ = [row.split(';')[9] for row in hip_smg]
sHH = [row.split(';')[10] for row in hip_smg]
sHK = [row.split(';')[11] for row in hip_smg]
sHST = [row.split(';')[12] for row in hip_smg]
		
#-------------------------Dados HIPARCOS (TODOS COM MAGNITUDE)
with open("/home/ellen/Documentos/python_ic/hiparcos_cmg.csv") as f:
	hip_cmg = f.read()
	
hip_cmg = hip_cmg.split('\n')
hip_cmg.pop()


HID = [row.split(';')[1] for row in hip_cmg]
Hplx = [float(row.split(';')[3]) for row in hip_cmg]
HU = [float(row.split(';')[4]) for row in hip_cmg]
HB= [float(row.split(';')[5]) for row in hip_cmg]
HV= [float(row.split(';')[6]) for row in hip_cmg]
HR = [float(row.split(';')[7]) for row in hip_cmg]
HI = [float(row.split(';')[8]) for row in hip_cmg]
HJ = [float(row.split(';')[9]) for row in hip_cmg]
HH = [float(row.split(';')[10]) for row in hip_cmg]
HK = [float(row.split(';')[11]) for row in hip_cmg]
HST = [row.split(';')[12] for row in hip_cmg]
Hdbest = [1000/plx for plx in Hplx]
HJH = [j-h for j,h in zip(HJ,HH)]
HRJ = [r-j for r,j in zip(HR,HJ)]                           #Cor J-H
HRK = [r-k for r,k in zip(HR,HK)]                           #Cor R-K
HMv = [v + 5 - 5*log10(d) for v,d in zip(HV,Hdbest)] 


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
	if (sVmag[i]=='     ') or (float(sVmag[i])>13):
		index_sVmag.append(i)
		
for i in reversed(range(len(index_sVmag))):
	data.pop(index_sVmag[i])
	
#-------------------------Limpar estrelas com d>20pc
index_d=[]
d = [float(row.split('\t')[18]) for row in data]

for i in range(len(data)):
	if d[i] > 20:
		index_d.append(i)
		
for i in reversed(range(len(index_d))):
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
for i in range(len(data)):
	if WV[i]<=10 and Wdbest[i]<=10:
		WD1.append(data[i])
		
#D2 - 10<V<12 E D<10 [GREEN]
WD2=[]
for i in range(len(data)):
	if WV[i]>10 and WV[i]<12 and Wdbest[i]<10:
		WD2.append(data[i])
		
#D3 - 10<V<12 E d>10 [ORANGE]
WD3=[]
for i in range(len(data)):
	if WV[i]>10 and WV[i]<12 and Wdbest[i]>10:
		WD3.append(data[i])
		
#D4 - 12<=V<=13 [RED]
WD4=[]
for i in range(len(data)):
	if WV[i]>=12 and WV[i]<=13:
		WD4.append(data[i])

#----------------------QUADRANTES	
for i in range(len(data)):
	if (WV[i]<=10.0):
		data[i] = data[i]+'\tQ1Q2'
	if (WV[i]>10.0) and (WV[i]<=12.0) and (Wdbest[i]<=10.0):
		data[i] = data[i]+'\tQ3'
	if (WV[i]>10.0) and (WV[i]<=11.0) and (Wdbest[i]>10.0):
		data[i] = data[i]+'\tQ4'
	if (WV[i]>11.0) and (WV[i]<=12.0) and (Wdbest[i]>10.0):
		data[i] = data[i]+'\tQ5'
	if (WV[i]>12.0) and (WV[i]<=13.0):
		data[i] = data[i]+'\tQ6'	

WQ = [row.split('\t')[22] for row in data]				
#-------------------------DIVISOES DOS DADOS GERAIS--------------------- 

#D1 - V<=10 E D<=10 [BLUE]
D1=[]
for i in range(len(data)):
	if WV[i]<=10 and Wdbest[i]<=10:
		D1.append(data[i])
for i in range(len(hip_cmg)):
	if HV[i]<=10 and Hdbest[i]<=10:
		D1.append(hip_cmg[i])		
		
		
#D2 - 10<V<12 E D<10 [GREEN]
D2=[]
for i in range(len(data)):
	if WV[i]>10 and WV[i]<12 and Wdbest[i]<10:
		D2.append(data[i])
		
#D3 - 10<V<12 E d>10 [ORANGE]
D3=[]
for i in range(len(data)):
	if WV[i]>10 and WV[i]<12 and Wdbest[i]>10:
		D3.append(data[i])
		
#D4 - 12<=V<=13 [RED]
D4=[]
for i in range(len(data)):
	if WV[i]>=12 and WV[i]<=13:
		D4.append(data[i])		
	
#-------------------------Operacoes com os dados WINTERS
WJH = [j-h for j,h in zip(WJ,WH)]
WRJ = [r-j for r,j in zip(WR,WJ)]                           #Cor J-H
WRK = [r-k for r,k in zip(WR,WK)]                           #Cor R-K
WMv = [v + 5 - 5*log10(d) for v,d in zip(WV,Wdbest)]
WHr = [r + 5 + 5*log10(m) for r,m in zip(WR,Wpm)]

#-------------------------AMOSTRA COOL WINTERS--------------------------
ind_cool_w = []
cool_w = []
for i in range(len(data)):
	if WRK[i] > 4.0:
		ind_cool_w.append(i)

for i in ind_cool_w:
	cool_w.append(data[i])	
		
CWID = [row.split('\t')[0] for row in cool_w]
CWpm = [float(row.split('\t')[5]) for row in cool_w]
CWV = [float(row.split('\t')[11]) for row in cool_w]
CWR = [float(row.split('\t')[12]) for row in cool_w]
CWI = [float(row.split('\t')[13]) for row in cool_w]
CWJ = [float(row.split('\t')[14]) for row in cool_w]
CWH = [float(row.split('\t')[15]) for row in cool_w]
CWK = [float(row.split('\t')[16]) for row in cool_w]
CWdbest = [float(row.split('\t')[18]) for row in cool_w]

CWJH = [j-h for j,h in zip(CWJ,CWH)]
CWRJ = [r-j for r,j in zip(CWR,CWJ)]                           #Cor J-H
CWRK = [r-k for r,k in zip(CWR,CWK)]                           #Cor R-K
CWMv = [v + 5 - 5*log10(d) for v,d in zip(CWV,CWdbest)]
CWHr = [r + 5 + 5*log10(m) for r,m in zip(CWR,CWpm)]	
#-------------------------ESTRELAS OBSERVADAS---------------------------
with open("/home/ellen/Documentos/python_ic/input_eo.txt") as f:
	input_eo = f.read()
	
input_eo = input_eo.split('\n')
input_eo.pop()

output_eo = []
for i in input_eo:
	if i not in output_eo:
		output_eo.append(i)

output_eo.append(str(len(output_eo)))

f=open('output_eo.txt','w')
for ele in output_eo:
    f.write(ele+'\n')
f.close()

num_w = []
num_h = []
obs_w = []
obs_h = []
#eo_win = []
#eo_hip = []

for i in output_eo:
	if i in WID:
		num_w.append(WID.index(i))
		obs_w.append(i)

obs_w.append('Observadas '+str(len(obs_w))+' de '+str(len(WID)))

f=open('observadas_winters.txt','w')
for ele in obs_w:
    f.write(ele+'\n')
f.close()

for i in output_eo:
	if i in HID:
		num_h.append(HID.index(i))
		obs_h.append(i)	

obs_h.append('Observadas '+str(len(obs_h))+' de '+str(len(HID)))

f=open('observadas_hiparcos.txt','w')
for ele in obs_h:
    f.write(ele+'\n')
f.close()

cor_w = []					
for i in range(len(data)):
	if i not in num_w:
		cor_w.append('red')
	else:
		cor_w.append('green')	

cor_h = []
for i in range(len(hip_smg)):
	if i not in num_h:
		cor_h.append('red')
	else:
		cor_h.append('green')

  
#-------------------------Parte grafica---------------------------------




#-------------------------ALMIC WINTERS
list_winters = []
for i in range(len(data)):
	if WRK[i] >= 3.8:
		if WID[i] in obs_w:
			list_winters.append(WID[i]+';'+WCOOR[i]+';0 0;'+str(WV[i])+';'+WQ[i]+';OBSERVADA;COOL')
		else:
			list_winters.append(WID[i]+';'+WCOOR[i]+';0 0;'+str(WV[i])+';'+WQ[i]+';NAO_OBSERVADA;COOL')	
	if WRK[i]< 3.8:
		if WID[i] in obs_w:
			list_winters.append(WID[i]+';'+WCOOR[i]+';0 0;'+str(WV[i])+';'+WQ[i]+';OBSERVADA')
		else:
			list_winters.append(WID[i]+';'+WCOOR[i]+';0 0;'+str(WV[i])+';'+WQ[i]+';NAO_OBSERVADA')

f=open('winters_almic.txt','w')
for ele in list_winters:
    f.write(ele+'\n')
f.close()

#--------------------------------COORDENADAS_HIPARCOS------------------------------------------------------------------------------

novo_alpha = []
for i in range(len(sHCOOR)):
	if float(sHCOOR[i][10]) >= 5:
		a = int(sHCOOR[i][9]) + 1
		novo_alpha.append(sHCOOR[i][:9]+str(a))
	else:
		novo_alpha.append(sHCOOR[i][:10])

novo_delta = []
for i in range(len(sHCOOR)):
	if (sHCOOR[i][13] == '+') or (sHCOOR[i][13] == '-'):
		if float(sHCOOR[i][24]) >= 5:
			a = int(sHCOOR[i][23]) + 1
			novo_delta.append(sHCOOR[i][13:23]+str(a))
		else:
			novo_delta.append(sHCOOR[i][13:24])
	if (sHCOOR[i][14] == '+') or (sHCOOR[i][14] == '-'):
		if float(sHCOOR[i][25]) >= 5:
			a = int(sHCOOR[i][24]) + 1
			novo_delta.append(sHCOOR[i][14:24]+str(a))
		else:
			novo_delta.append(sHCOOR[i][14:25])
	if (sHCOOR[i][15] == '+') or (sHCOOR[i][15] == '-'):
		if float(sHCOOR[i][26]) >= 5:
			a = int(sHCOOR[i][25]) + 1
			novo_delta.append(sHCOOR[i][15:25]+str(a))
		else:
			novo_delta.append(sHCOOR[i][15:26])
	if (sHCOOR[i][16] == '+') or (sHCOOR[i][16] == '-'):
		if float(sHCOOR[i][27]) >= 5:
			a = int(sHCOOR[i][26]) + 1
			novo_delta.append(sHCOOR[i][16:26]+str(a))	    	
		else:
			novo_delta.append(sHCOOR[i][16:27])			

#-------------------------ALMIC HIPARCOS
list_hip = []
for i in range(len(hip_smg)):
	if sHID[i] in obs_h:
		list_hip.append(sHID[i]+';'+novo_alpha[i]+';'+novo_delta[i]+';0 0;'+sHV[i]+';'+sHST[i]+';OBSERVADA')
	else:
		list_hip.append(sHID[i]+';'+novo_alpha[i]+';'+novo_delta[i]+';0 0;'+sHV[i]+';'+sHST[i]+';NAO_OBSERVADA')
		
f=open('hip_almic.txt','w')
for ele in list_hip:
    f.write(ele+'\n')
f.close()	

