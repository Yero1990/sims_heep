#Python code for plotting relevant quantities like: 
# --> theoretical derivatives of W or fractional momentum, ... 
# --> measured quantities like chi2, . . .

import numpy as np
import LT.box as B
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Define Some Constants                                                                                                     
dtr = np.pi / 180.    #degrees to radians                                                                                                                                 
Mp = 0.938272           #proton mass                                                                                                                                                
     


# Plotting reduced chi2 vs. relative quantities, while holding fixed other relative quantities, to observe sensitivity
'''
f = B.get_file('sorted_chi2.txt')
dEb_Eb = B.get_data(f, 'dEb_Eb')
dP_P = B.get_data(f, 'dP_P')
dth = B.get_data(f, 'dth')
redchi2 = B.get_data(f, 'total_redChi2')


#When plotting lists with multiple conditions, put a single boolean like '&' or '|', for some reason, '&&' does NOT work. 
#See 'python plot with conditions on other lists' in Google, and search for it in "StackOverflow" link

B.plot_exp(dth[(dP_P==-0.0025) & (dEb_Eb==0.0)], redchi2[(dP_P==-0.0025) & (dEb_Eb==0.0)], color='red', marker='^', label=r'$\frac{dEb}{Eb}$ = 0.0,  $\frac{dP}{P}$ = -0.0025')
B.plot_exp(dth[(dP_P==-0.0025) & (dEb_Eb==0.001)], redchi2[(dP_P==-0.0025) & (dEb_Eb==0.001)], color='red', marker='^', markerfacecolor='none', label=r'$\frac{dEb}{Eb}$ = 0.001,  $\frac{dP}{P}$ = -0.0025')

B.plot_exp(dth[(dP_P==-0.0015) & (dEb_Eb==0.000)], redchi2[(dP_P==-0.0015) & (dEb_Eb==0.0)], color='blue', marker='o', label=r'$\frac{dEb}{Eb}$ = 0.0,  $\frac{dP}{P}$ = -0.0015')
B.plot_exp(dth[(dP_P==-0.0015) & (dEb_Eb==0.001)], redchi2[(dP_P==-0.0015) & (dEb_Eb==0.001)], color='blue', marker='o', markerfacecolor='none', label=r'$\frac{dEb}{Eb}$ = 0.001,  $\frac{dP}{P}$ = -0.0015')

B.plot_exp(dth[(dP_P==-0.0005) & (dEb_Eb==0.0)], redchi2[(dP_P==-0.0005) & (dEb_Eb==0.0)], color='cyan', marker='s', label=r'$\frac{dEb}{Eb}$ = 0.0,  $\frac{dP}{P}$ = -0.0005')
B.plot_exp(dth[(dP_P==-0.0005) & (dEb_Eb==0.001)], redchi2[(dP_P==-0.0005) & (dEb_Eb==0.001)], color='cyan', marker='s', markerfacecolor='none', label=r'$\frac{dEb}{Eb}$ = 0.001,  $\frac{dP}{P}$ = -0.0005')

B.plot_exp(dth[(dP_P==0.0005) & (dEb_Eb==0.0)], redchi2[(dP_P==0.0005) & (dEb_Eb==0.0)], color='green', marker='v', label=r'$\frac{dEb}{Eb}$ = 0.0,  $\frac{dP}{P}$ = 0.0005')
B.plot_exp(dth[(dP_P==0.0005) & (dEb_Eb==0.001)], redchi2[(dP_P==0.0005) & (dEb_Eb==0.001)], color='green', marker='v', markerfacecolor='none',label=r'$\frac{dEb}{Eb}$ = 0.001,  $\frac{dP}{P}$ = 0.0005')

B.plot_exp(dth[(dP_P==0.0025) & (dEb_Eb==0.0)], redchi2[(dP_P==0.0025) & (dEb_Eb==0.0)], color='magenta', marker='P', label=r'$\frac{dEb}{Eb}$ = 0.0,  $\frac{dP}{P}$ = 0.0025')
B.plot_exp(dth[(dP_P==0.0025) & (dEb_Eb==0.001)], redchi2[(dP_P==0.0025) & (dEb_Eb==0.001)], color='magenta', marker='P', markerfacecolor='none',label=r'$\frac{dEb}{Eb}$ = 0.001,  $\frac{dP}{P}$ = 0.0025')

B.plot_exp(dth[(dP_P==-0.0035) & (dEb_Eb==0.0)], redchi2[(dP_P==-0.0035) & (dEb_Eb==0.0)], color='black', marker='D', label=r'$\frac{dEb}{Eb}$ = 0.0,  $\frac{dP}{P}$ = -0.0035')
B.plot_exp(dth[(dP_P==-0.0035) & (dEb_Eb==0.001)], redchi2[(dP_P==-0.0035) & (dEb_Eb==0.001)], color='black', marker='D', markerfacecolor='none',label=r'$\frac{dEb}{Eb}$ = 0.001,  $\frac{dP}{P}$ = -0.0035')

B.pl.legend()
B.pl.xlabel(r'Relative Angle, d$\theta$[rad]')
B.pl.ylabel(r'Total Reduced $\chi^{2}_{\nu}$')
B.pl.yscale('log')

B.pl.show("same")
'''


'''
#-------chi2 vs. HMS Angle Variations, dtheta-------------

dP_P_arr = [-0.0035, -0.0025, -0.0015, -0.0005, 0.0005, 0.0025]
dEb_Eb_arr = [0.0, 0.001]
color_arr = ['black', 'red', 'blue', 'cyan', 'green', 'magenta']
fcolor_arr = ['none']
marker_arr = ['D', '^', 'o', 's', 'v', 'P']

for i in range(0, len(dP_P_arr)):
    for j in range(0, len(dEb_Eb_arr)):
        print ('dP_P[i] = ', dP_P_arr[i], 'dEb_Eb[j] = ',dEb_Eb_arr[j], 'color[k] = ',color_arr[i])
        if j==0:
            B.plot_exp(dth[(dP_P==dP_P_arr[i]) & (dEb_Eb==dEb_Eb_arr[j])], redchi2[(dP_P==dP_P_arr[i]) & (dEb_Eb==dEb_Eb_arr[j])], color=color_arr[i], marker=marker_arr[i], label=r'$\frac{dEb}{Eb}$ = %s,  $\frac{dP}{P}$ = %s'%(dEb_Eb_arr[j],dP_P_arr[i]))
        if j==1:
            B.plot_exp(dth[(dP_P==dP_P_arr[i]) & (dEb_Eb==dEb_Eb_arr[j])], redchi2[(dP_P==dP_P_arr[i]) & (dEb_Eb==dEb_Eb_arr[j])], color=color_arr[i], markerfacecolor='none', marker=marker_arr[i], label=r'$\frac{dEb}{Eb}$ = %s,  $\frac{dP}{P}$ = %s'%(dEb_Eb_arr[j],dP_P_arr[i]))


B.pl.legend(loc='lower right')
B.pl.grid(True, which='both')
B.pl.yscale('log')
B.pl.title(r'Reduced Chi2 ($\chi^{2}_{\nu}$) vs. HMS Angle Variations')
B.pl.xlabel(r'HMS Angle Variations, d$\theta$[rad]')
B.pl.ylabel(r'Total Reduced $\chi^{2}_{\nu}$')
B.pl.xticks(np.arange(-0.0030, 0.0030, step=0.0005))
B.pl.xlim(-0.0022, 0.0032)
B.pl.show()

#----------------------------
'''

'''
#-------chi2 vs. HMS Relative Momentum, dtheta-------------

dth_arr = [-0.0015, -0.001, -0.0005, 0.0005, 0.001, 0.0015]

dEb_Eb_arr = [0.0, 0.001]

color_arr = ['black', 'red', 'blue', 'cyan', 'green', 'magenta']
fcolor_arr = ['none']
marker_arr = ['D', '^', 'o', 's', 'v', 'P']

for i in range(0, len(dth_arr)):
    for j in range(0, len(dEb_Eb_arr)):
        #print ('dP_P[i] = ', dP_P_arr[i], 'dEb_Eb[j] = ',dEb_Eb_arr[j], 'color[k] = ',color_arr[i])
        if j==0:
            B.plot_exp(dP_P[(dth==dth_arr[i]) & (dEb_Eb==dEb_Eb_arr[j])], redchi2[(dth==dth_arr[i]) & (dEb_Eb==dEb_Eb_arr[j])], color=color_arr[i], marker=marker_arr[i], label=r'$\frac{dEb}{Eb}$ = %s,  $\delta\theta$ = %s (rad)'%(dEb_Eb_arr[j],dth_arr[i]))
        if j==1:
            B.plot_exp(dP_P[(dth==dth_arr[i]) & (dEb_Eb==dEb_Eb_arr[j])], redchi2[(dth==dth_arr[i]) & (dEb_Eb==dEb_Eb_arr[j])], color=color_arr[i], markerfacecolor='none', marker=marker_arr[i], label=r'$\frac{dEb}{Eb}$ = %s,  $\delta\theta$ = %s (rad)'%(dEb_Eb_arr[j],dth_arr[i]))


B.pl.legend(loc='lower right')
B.pl.grid(True, which='both')
B.pl.yscale('log')
B.pl.title(r'Reduced Chi2 ($\chi^{2}_{\nu}$) vs. HMS Angle Variations')
B.pl.xlabel(r'HMS Momentum, $\frac{dP}{P}$')
B.pl.ylabel(r'Total Reduced $\chi^{2}_{\nu}$')
B.pl.xticks(np.arange(-0.0045, 0.0060, step=0.0005))
B.pl.xlim(-0.0045, 0.0060)
B.pl.show()
'''

'''
#-------------chi2 vs. relative beam energy---------
#dth_arr = [-0.001, -0.0005]  
#dP_P_arr = [-0.0015, -0.0005, 0.0005, 0.0015]  #, -0.0015, -0.0005, 0.0005, 0.0025]

dth_arr = [-0.001, -0.0005]  
dP_P_arr = [-0.0015, -0.001, -0.0005, 0.00]


color_arr = ['red', 'blue', 'cyan', 'green']#, 'magenta']
fcolor_arr = ['none']
marker_arr = ['o', 's']#, 'v', 'P']

for i in range(0, len(dth_arr)):
    for j in range(0, len(dP_P_arr)):
        #print ('dP_P[i] = ', dP_P_arr[i], 'dEb_Eb[j] = ',dEb_Eb_arr[j], 'color[k] = ',color_arr[i])
        if j==0:
            B.plot_exp(dEb_Eb[(dth==dth_arr[i]) & (dP_P==dP_P_arr[j])], redchi2[(dth==dth_arr[i]) & (dP_P==dP_P_arr[j])], color=color_arr[i], marker=marker_arr[i], label=r'$\frac{dP}{P}$ = %s,  $\delta\theta$ = %s (rad)'%(dP_P_arr[j],dth_arr[i]))
        if j==1:
            B.plot_exp(dEb_Eb[(dth==dth_arr[i]) & (dP_P==dP_P_arr[j])], redchi2[(dth==dth_arr[i]) & (dP_P==dP_P_arr[j])], color=color_arr[i], markerfacecolor='none', marker=marker_arr[i], label=r'$\frac{dP}{P}$ = %s,  $\delta\theta$ = %s (rad)'%(dP_P_arr[j],dth_arr[i]))
        if j==2:
            B.plot_exp(dEb_Eb[(dth==dth_arr[i]) & (dP_P==dP_P_arr[j])], redchi2[(dth==dth_arr[i]) & (dP_P==dP_P_arr[j])], color=color_arr[i], fillstyle='right', marker=marker_arr[i], label=r'$\frac{dP}{P}$ = %s,  $\delta\theta$ = %s (rad)'%(dP_P_arr[j],dth_arr[i]))
        if j==3:
            B.plot_exp(dEb_Eb[(dth==dth_arr[i]) & (dP_P==dP_P_arr[j])], redchi2[(dth==dth_arr[i]) & (dP_P==dP_P_arr[j])], color=color_arr[i], fillstyle='left', marker=marker_arr[i], label=r'$\frac{dP}{P}$ = %s,  $\delta\theta$ = %s (rad)'%(dP_P_arr[j],dth_arr[i]))


            
B.pl.legend(loc='lower right')
B.pl.grid(True, which='both')
B.pl.yscale('log')
B.pl.title(r'Reduced Chi2 ($\chi^{2}_{\nu}$) vs. Beam Energy Variations')
B.pl.xlabel(r'Beam Energy Variations, $\frac{dE_{b}}{E_{b}}$')
B.pl.ylabel(r'Total Reduced $\chi^{2}_{\nu}$')
#B.pl.xticks(np.arange(-0.0045, 0.0060, step=0.0005))
B.pl.xlim(-0.0011, 0.00155)
B.pl.show()

#----------------------------
'''

#PLOT (W_simc - W_data) vs. E' for difference beam energies (Measured DATA/SIMC quantities)
f = B.get_file('hms_kin.data')
particle = B.get_data(f, 'particle')
hmsP = B.get_data(f, 'nmr_P')
hmsAng = B.get_data(f, 'hms_Angle')
Eb = B.get_data(f, 'beam_e')
data_W = B.get_data(f, 'data_W_mean')
data_W_err = B.get_data(f, 'data_W_mean_err')
simc_W = B.get_data(f, 'simc_W_mean')
simc_W_err = B.get_data(f, 'simc_W_mean_err')

dW_meas = simc_W - data_W
dW_meas_err = np.sqrt(simc_W_err**2 + data_W_err**2)


B.plot_exp(hmsP[(Eb==10.6005) & (particle=='e')], dW_meas[(Eb==10.6005) & (particle=='e') ], dW_meas_err[(Eb==10.6005) & (particle=='e')], color='r', marker='o', label = 'Eb = 10.6005 GeV' )
B.plot_exp(hmsP[(Eb==6.42765) & (particle=='e')], dW_meas[(Eb==6.42765) & (particle=='e') ], dW_meas_err[(Eb==6.42765) & (particle=='e')], color='b', marker='s', label = 'Eb = 6.42765 GeV' )
B.plot_exp(hmsP[(Eb==3.83350) & (particle=='e')], dW_meas[(Eb==3.83350) & (particle=='e') ], dW_meas_err[(Eb==3.83350) & (particle=='e')], color='g', marker='^', label = 'Eb = 3.83350 GeV' )
B.plot_exp(hmsP[(Eb==4.93090) & (particle=='e')], dW_meas[(Eb==4.93090) & (particle=='e') ], dW_meas_err[(Eb==4.93090) & (particle=='e')], color='c', marker='v', label = 'Eb = 4.93090 GeV' )

#B.pl.legend()
#B.pl.xlabel('HMS Central Momentum [GeV]')
#B.pl.ylabel(r'W Variations, $dW_{SIMC} - dW_{DATA}$ [GeV]')
#B.pl.title('HMS Electrons: dW vs. Momentum')
#B.pl.show()

#Plot Predicted dW vs. P
#Assume: dP/P = -0.0015,  dth = -0.0005, dEb/Eb = 0.0004
dP_P = -0.0015
dth = -0.0005
dEb_Eb = 0.0004


#Calculated W derivatives

#dW_dEb = hmsP[particle=='e']/Eb[particle=='e']
#dW_dP = -Eb[particle=='e']/hmsP[particle=='e']
#dW_dth = -2 * Eb[particle=='e'] * hmsP[particle=='e'] * np.sin(th/2) * np.cos(th/2) / Mp
Eb_0 = 10.6005
Eb_1 = 6.42765
Eb_2 = 3.83350
Eb_3 = 4.93090

dW_pred0 = hmsP[(Eb==Eb_0) & (particle=='e')] * dEb_Eb - Eb[(Eb==Eb_0) & (particle=='e')]*dP_P - 2 * Eb[(Eb==Eb_0) & (particle=='e')] * hmsP[(Eb==Eb_0) & (particle=='e')] * np.sin(hmsAng[(Eb==Eb_0) & (particle=='e')]*dtr/2) * np.cos(hmsAng[(Eb==Eb_0) & (particle=='e')]/2) / Mp * dth
dW_pred1 = hmsP[(Eb==Eb_1) & (particle=='e')] * dEb_Eb - Eb[(Eb==Eb_1) & (particle=='e')]*dP_P - 2 * Eb[(Eb==Eb_1) & (particle=='e')] * hmsP[(Eb==Eb_1) & (particle=='e')] * np.sin(hmsAng[(Eb==Eb_1) & (particle=='e')]*dtr/2) * np.cos(hmsAng[(Eb==Eb_1) & (particle=='e')]/2) / Mp * dth
dW_pred2 = hmsP[(Eb==Eb_2) & (particle=='e')] * dEb_Eb - Eb[(Eb==Eb_2) & (particle=='e')]*dP_P - 2 * Eb[(Eb==Eb_2) & (particle=='e')] * hmsP[(Eb==Eb_2) & (particle=='e')] * np.sin(hmsAng[(Eb==Eb_2) & (particle=='e')]*dtr/2) * np.cos(hmsAng[(Eb==Eb_2) & (particle=='e')]/2) / Mp * dth
dW_pred3 = hmsP[(Eb==Eb_3) & (particle=='e')] * dEb_Eb - Eb[(Eb==Eb_3) & (particle=='e')]*dP_P - 2 * Eb[(Eb==Eb_3) & (particle=='e')] * hmsP[(Eb==Eb_3) & (particle=='e')] * np.sin(hmsAng[(Eb==Eb_3) & (particle=='e')]*dtr/2) * np.cos(hmsAng[(Eb==Eb_3) & (particle=='e')]/2) / Mp * dth


B.plot_exp(hmsP[(Eb==Eb_0) & (particle=='e')], dW_pred0, color='r', marker='o', markersize=12, markerfacecolor='none', label = 'dW Predicted: Eb = 10.6005 GeV' )
B.plot_exp(hmsP[(Eb==Eb_1) & (particle=='e')], dW_pred1, color='b', marker='s', markersize=12, markerfacecolor='none', label =  'dW Predicted: Eb = 6.42765 GeV' )
B.plot_exp(hmsP[(Eb==Eb_2) & (particle=='e')], dW_pred2, color='g', marker='^', markersize=12, markerfacecolor='none', label =  'dW Predicted: Eb = 3.83350 GeV' )
B.plot_exp(hmsP[(Eb==Eb_3) & (particle=='e')], dW_pred3, color='c', marker='v', markersize=12, markerfacecolor='none', label =  'dW Predicted: Eb = 4.93090 GeV' )

B.pl.legend()
B.pl.xlabel('HMS Central Momentum [GeV]')
B.pl.ylabel(r'W Variations, dW [GeV]')
B.pl.title('HMS Electrons: dW vs. Momentum')
B.pl.grid(True)
B.pl.show()



'''
#---------------------------------
#---PLOTTING W derivatives--------
#---------------------------------

#-------Possible independent variables-------------

#dW can be plotted as a function of relative uncertainties or absolute values Eb, P, theta

#relative uncertainties
#dEb_Eb = np.linspace(-0.001, 0.001, 100, endpoint=True)    #(-0.1 to 0.1 %)
#dP_P = np.linspace(-0.004, 0.004, 100, endpoint=True)      #(-0.4 to 0.4 %)
#dth = np.linspace(-0.002, 0.002, 100, endpoint=True )      #(-2 mr to 2 mr %)

#Beam, momentum, angle
#Eb = np.linspace(3, 11, 100, endpoint=True)   #beam energy, steps of 1 MeV
#P = np.linspace(1, 5, 100, endpoint=True)      #momentum, steps of 1 MeV
#theta = np.linspace(10, 60, 100, endpoint=True)     #angle, steps of 0.01 deg

#------------------------------------------------

#derivatives
#dW_dEb = P/Eb
#dW_dP = -Eb/P
#dW_dth = -2 * Eb * P * np.sin(theta/2) * np.cos(theta/2) / Mp

#------If the independent variables are absolute quantities-------

#relative beam energy configurations
dEb_Eb1 = -0.01  
dEb_Eb2 = -0.008
dEb_Eb3 = -0.006
dEb_Eb4 = -0.004
dEb_Eb5 = -0.002

dEb_Eb6 = 0.002
dEb_Eb7 = 0.004
dEb_Eb8 = 0.006
dEb_Eb9 = 0.008
dEb_Eb10 = 0.01

dW_beam1 = P * dEb_Eb1
dW_beam2 = P * dEb_Eb2
dW_beam3 = P * dEb_Eb3
dW_beam4 = P * dEb_Eb4
dW_beam5 = P * dEb_Eb5
dW_beam6 = P * dEb_Eb6
dW_beam7 = P * dEb_Eb7
dW_beam8 = P * dEb_Eb8
dW_beam9 = P * dEb_Eb9
dW_beam10 = P * dEb_Eb10


fig1 = plt.figure()
plt.plot(P, dW_beam1, color='r', label='dEb/Eb = -0.01')
plt.plot(P, dW_beam2, color='g', label='dEb/Eb = -0.008')
plt.plot(P, dW_beam3, color='b', label='dEb/Eb = -0.006')
plt.plot(P, dW_beam4, color='cyan', label='dEb/Eb = -0.004')
plt.plot(P, dW_beam5, color='black', label='dEb/Eb = -0.002')

plt.plot(P, dW_beam6, color='black', linestyle='--', label='dEb/Eb = 0.002')
plt.plot(P, dW_beam7, color='cyan', linestyle='--', label='dEb/Eb = 0.004')
plt.plot(P, dW_beam8, color='b', linestyle='--', label='dEb/Eb = 0.006')
plt.plot(P, dW_beam9, color='g', linestyle='--', label='dEb/Eb = 0.008')
plt.plot(P, dW_beam10, color='r', linestyle='--', label='dEb/Eb = 0.01')

plt.title('W variations vs. HMS Central Momentum')
plt.xlabel('HMS Central Momentum [GeV]')
plt.ylabel(r'$\delta$W Variations [GeV]')

plt.legend()

#----------------------------------

#relative momentum configurations
dP_P1 = -0.01  
dP_P2 = -0.008
dP_P3 = -0.006
dP_P4 = -0.004
dP_P5 = -0.002

dP_P6 = 0.002
dP_P7 = 0.004
dP_P8 = 0.006
dP_P9 = 0.008
dP_P10 = 0.01

dW_P1 = -Eb * dP_P1
dW_P2 = -Eb * dP_P2
dW_P3 = -Eb * dP_P3
dW_P4 = -Eb * dP_P4
dW_P5 = -Eb * dP_P5
dW_P6 = -Eb * dP_P6
dW_P7 = -Eb * dP_P7
dW_P8 = -Eb * dP_P8
dW_P9 = -Eb * dP_P9
dW_P10 = -Eb * dP_P10


fig2 = plt.figure()
plt.plot(Eb, dW_P1, color='r', label='dP/P = -0.01')
plt.plot(Eb, dW_P2, color='g', label='dP/P = -0.008')
plt.plot(Eb, dW_P3, color='b', label='dP/P = -0.006')
plt.plot(Eb, dW_P4, color='cyan', label='dP/P = -0.004')
plt.plot(Eb, dW_P5, color='black', label='dP/P = -0.002')

plt.plot(Eb, dW_P6, color='black', linestyle='--', label='dP/P = 0.002')
plt.plot(Eb, dW_P7, color='cyan', linestyle='--', label='dP/P = 0.004')
plt.plot(Eb, dW_P8, color='b', linestyle='--', label='dP/P = 0.006')
plt.plot(Eb, dW_P9, color='g', linestyle='--', label='dP/P = 0.008')
plt.plot(Eb, dW_P10, color='r', linestyle='--', label='dP/P = 0.01')

plt.title('W variations vs. Beam Energy')
plt.xlabel('Beam Energy [GeV]')
plt.ylabel(r'$\delta$W Variations [GeV]')

plt.legend()

plt.show()
'''

#dW_mom = -Eb * dP_P
#dW_ang = -2 * Eb * P * np.sin(theta/2) * np.cos(theta/2) / Mp * dth


#-----------------------------------------------------------------




#fig1 = plt.figure()
#plt.plot(dEb_Eb, dW_beam, color='r')
#plt.show()

#fig2 = plt.figure()
#plt.plot(dP_P, dW_mom, color='b')
#plt.show()

#fig3 = plt.figure()
#plt.plot(dth, dW_ang, color='b')
#plt.show()
