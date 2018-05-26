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
WSN = [row.split('\t')[21] for row in data]

f=open('winters15_SN.txt','w')
for ele in WSN:
    f.write(ele+'\n')
f.close()

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
			
#-------------------------DIVISOES DOS DADOS GERAIS--------------------- 

#D1 - V<=10 E D<=10 [BLUE]
D1=[]
for i in range(0,len(data)):
	if WV[i]<=10 and Wdbest[i]<=10:
		D1.append(data[i])
for i in range(0,len(hip_cmg)):
	if HV[i]<=10 and Hdbest[i]<=10:
		D1.append(hip_cmg[i])		
		
		
#D2 - 10<V<12 E D<10 [GREEN]
D2=[]
for i in range(0,len(data)):
	if WV[i]>10 and WV[i]<12 and Wdbest[i]<10:
		D2.append(data[i])
		
#D3 - 10<V<12 E d>10 [ORANGE]
D3=[]
for i in range(0,len(data)):
	if WV[i]>10 and WV[i]<12 and Wdbest[i]>10:
		D3.append(data[i])
		
#D4 - 12<=V<=13 [RED]
D4=[]
for i in range(0,len(data)):
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
for i in range(0,len(data)):
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

for i in output_eo:
	if i in WID:
		num_w.append(WID.index(i))
		obs_w.append(i)

f=open('observadas_winters.txt','w')
for ele in obs_w:
    f.write(ele+'\n')
f.close()

f=open('winters15_names.txt','w')
for ele in W_old_ID:
	f.write(ele+'\n')
f.close()	

for i in output_eo:
	if i in HID:
		num_h.append(HID.index(i))
		obs_h.append(i)

for ele in HID:
	if ele not in obs_h:
		print ele	

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
	if WRK >= 3.8:
		if WID[i] in obs_w:
			list_winters.append(WID[i]+';'+WCOOR[i]+';'+str(WV[i])+';'+WQ[i]+';OBSERVADA;COOL')
		else:
			list_winters.append(WID[i]+';'+WCOOR[i]+';'+str(WV[i])+';'+WQ[i]+';NAO_OBSERVADA;COOL')	
	else:
		if WID[i] in obs_w:
			list_winters.append(WID[i]+';'+WCOOR[i]+';'+str(WV[i])+';'+WQ[i]+';OBSERVADA')
		else:
			list_winters.append(WID[i]+';'+WCOOR[i]+';'+str(WV[i])+';'+WQ[i]+'NAO_OBSERVADA')

f=open('winters_almic.txt','w')
for ele in list_winters:
    f.write(ele+'\n')
f.close()

#-------------------------ALMIC HIPARCOS
list_hip = []
for i in range(len(hip_smg)):
	if sHID[i] in obs_h:
		list_hip.append(sHID[i]+';'+sHCOOR[i]+';'+sHV[i]+';'+sHST[i]+';OBSERVADA')
	else:
		list_hip.append(sHID[i]+';'+sHCOOR[i]+';'+sHV[i]+';'+sHST[i]+';NAO_OBSERVADA')
		
f=open('hip_almic.txt','w')
for ele in list_hip:
    f.write(ele+'\n')
f.close()	


#-------------------------------------------
estrelas_diego_id = ['GJ406',
'HZ43B',
'GJ905',
'HIP89560',
'HIP87937',
'Wolf672B',
'HIP36208',
'HIP91768',
'HIP91772',
'GJ1289',
'HIP112460',
'HIP36626',
'HIP36627',
'HIP72896',
'HIP80824',
'HIP84794',
'HIP101180',
'GJ905.2A',
'HIP79762',
'GJ388',
'HIP86162',
'HIP82809',
'HIP80459',
'G148-6',
'GJ860A',
'GJ1142A',
'LP356-88',
'HIP54035',
'GJ3117',
'HIP47650',
'HIP72944',
'HIP32984',
'HD50281B',
'HIP68469',
'HIP49986',
'HIP29277',
'HIP78353',
'G111-72',
'HIP83043',
'HIP88574',
'HIP117473',
'G59-39',
'HIP64880',
'HIP113296',
'HIP103096',
'HIP47513',
'HIP63253',
'HIP66625',
'HIP106811',
'HIP51007',
'HIP53985',
'HIP26801',
'HIP25878',
'LP775-52',
'HIP104217',
'HIP113576',
'L619-49',
'LP705-30',
'BD+201790',
'HIP21482',
'HIP83599',
'HIP104214',
'HIP59519',
'HIP81988',
'HIP71181',
'BD+39539',
'HIP114622',
'GL406',
'HZ43B',
'GJ905',
'GJ709',
'GL699',
'Wolf672B',
'GJ273',
'GJ725',
'GJ1289',
'GJ873',
'GJ277',
'GJ568A',
'GJ628',
'GL669A',
'GJ793',
'LP347-5',
'GJ617B',
'GL388',
'GJ687',
'GJ643',
'GL625',
'NLTT28469',
'GJ860A',
'NLTT26385',
'NLTT10977',
'GL411',
'NLTT6164',
'GJ362',
'GL569',
'GJ250',
'GJ536',
'GJ382',
'GJ226',
'GJ606',
'NLTT19314',
'GL649',
'GJ701',
'GJ908',
'GJ6520',
'NLTT31888',
'GJ1170',
'GJ880',
'GJ809',
'GJ361',
'GL490A',
'GL521',
'GJ835',
'GJ390',
'GL410',
'GJ212',
'GJ205',
'NLTT13109',
'HIP104217',
'HIP113576',
'LP856-54',
'NLTT1370',
'BD+20 1790',
'NLTT13601',
'GJ654',
'HIP104214',
'NLTT29948',
'HIP81988',
'HD128165',
'NLTT7887',
'HD219134']

estrelas_diego_st = ['M6V',
'M3.5Ve',
'M5.0V',
'M0V',
'M4V',
'M4',
'M3.5V',
'M3V',
'M3.5V',
'M4.5V',
'M4.0V',
'M2.5V',
'M4.0V',
'M3V',
'M3V',
'M3.5V',
'M3V',
'M1.5V',
'M3.0Ve',
'M4Vae',
'M3.0V',
'M3.5V',
'M1.5V',
'M3V',
'M3V',
'M3V',
'M2.5',
'M2+V',
'M2.5Ve',
'M3.5V',
'M3V',
'K3.5V',
'M2.5V',
'M0V',
'M2V',
'M2.5V',
'M1V',
'M2',
'M2V',
'M0V',
'M1VFe-1',
'M0',
'M1.0V',
'M1.5Ve',
'M1.0Ve',
'M2.5V',
'M0V+M4/5V',
'M1.0V',
'M1V',
'M1V',
'M1.0V',
'M1.0V',
'M1.5Ve',
'M2',
'K7V',
'K7+Vk',
'M3V:',
'K6',
'K5e',
'K2.5Ve',
'M1.5V',
'K5V',
'K3/4:V',
'K3',
'K3V',
'K2',
'K3V']

comum_diego_hip=[]
comum_diego_win = []
comum_diego_obs = []
for i in estrelas_diego_id:
	if i in WID:
		comum_diego_win.append(i)
	if i in HID:
		comum_diego_hip.append(i)
	if i in output_eo:
		comum_diego_obs.append(i)	

	
f=open('diego_win.txt','w')
for ele in comum_diego_win:
    f.write(ele+'\n')
f.close()

f=open('diego_hip.txt','w')
for ele in comum_diego_hip:
    f.write(ele+'\n')
f.close()

f=open('diego_obs.txt','w')
for ele in comum_diego_obs:
    f.write(ele+'\n')
f.close()	

#-------------------verificar r-k na mao
RK = []

quad5 = ['HIP31555',
'HIP48336',
'HIP46706',
'HIP48477',
'GJ3543',
'HIP51007',
'HIP50341',
'L142-086',
'HIP49969',
'HIP50808',
'GJ438',
'HIP54373',
'HIP54532',
'GJ3728',
'HIP63550',
'HIP65520',
'HIP69454',
'HIP69285',
'HIP78353',
'HIP80268',
'HIP80440',
'HIP82283',
'HIP84051',
'HIP86961',
'LTT07419',
'HIP91608',
'LTT07246',
'HIP100490',
'HIP102235',
'HIP104432',
'LP875-068',
'HIP110534',
'GJ4288',
'HIP114719']

for i in range(len(data)):
	for j in range(len(quad5)):
		if WRK[i] >= 3.75 and WID[i] == quad5[j]:
			RK.append(quad5[j]+';'+Walpha[i]+';'+str(WRK[i]))

f=open('rk.txt','w')
for ele in RK:
    f.write(ele+'\n')
f.close()

ages=['NLTT1370','NLTT7055','L577-72','NLTT4616','NLTT26385','LP856-54','NLTT13109','NLTT29948','HIP83599','LTT4616','LTT5381']
for i in range(len(data)):
	for j in range(len(ages)):
		if WID[i]==ages[j]:
			print ages[j]
						
		
				
		
