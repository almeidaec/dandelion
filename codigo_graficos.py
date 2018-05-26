#------------------SUB_ANA_HrvsRJ--------------------------------

x = arange(1,5.5,0.01)
plot(x,13+(7./5.35)*x,linewidth=1.5,color='black')
scatter(WRJ,WHr,s=40)
xlabel('R-J')
ylabel('Proper motion')
ylim(ylim()[::-1])
axis([1,5.5,19,8])
title('Amostra Winters')

show()

#------------------TIPO_ESPECTRAL_JHvsRK_WINTERS------------------------

scatter(WRK,WJH,s=40)
xlabel('R-K')
ylabel('J-H')
ylim(ylim()[::-1])
axis([2.5,5.7,1.3,0.3])
title('Amostra Winters')
axvline(x=2.9,color='purple',linestyle='--')
axvline(x=3.8,color='green',linestyle='--')
axvline(x=5.5,color='orange',linestyle='--')
text(2.8,1.27,'M0',color='purple',fontweight='bold')
text(3.7,1.27,'M3',color='green',fontweight='bold')
text(5.4,1.27,'M6',color='orange',fontweight='bold')

show()

#------------------TIPO_ESPECTRAL_JHvsRK_HIPARCOS-----------------------

scatter(HRK,HJH,s=40,color=cor_h)
xlabel('R-K')
ylabel('J-H')
ylim(ylim()[::-1])
axis([1.0,5.7,0.9,0.2])
title('Amostra Hiparcos')
axvline(x=2.9,color='purple',linestyle='--')
axvline(x=3.8,color='green',linestyle='--')
axvline(x=5.5,color='orange',linestyle='--')
text(2.8,0.88,'M0',color='purple',fontweight='bold')
text(3.7,0.88,'M3',color='green',fontweight='bold')
text(5.4,0.88,'M6',color='orange',fontweight='bold')

show()

#----------------------ARQUIVO DE TEXTO DE UMA LISTA


