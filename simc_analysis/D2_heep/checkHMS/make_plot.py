import LT.box as B
import numpy as np
import matplotlib.pyplot as plt


x = [1,2,3,4]
#Open File
f = B.get_file('hmsPCorrected/momentum_fraction_diff.data')
run = B.get_data(f, 'Run')
Pf_data = B.get_data(f, 'Pf_data')
Pf_data_err = B.get_data(f, 'Pf_data_err')
Pf_simc = B.get_data(f, 'Pf_simc')
Pf_simc_err = B.get_data(f, 'Pf_simc_err')

dP = Pf_simc - Pf_data
dP_err = np.sqrt(Pf_simc_err**2 + Pf_data_err**2)

B.plot_exp(x, dP, dP_err, marker='s', color='red', label='Corrected HMS Momentum')


f = B.get_file('UnCorrected/momentum_fraction_diff.data')
run = B.get_data(f, 'Run')                                             
Pf_data = B.get_data(f, 'Pf_data')                                                                                          
Pf_data_err = B.get_data(f, 'Pf_data_err')                                                                                                  
Pf_simc = B.get_data(f, 'Pf_simc')                                                                                                         
Pf_simc_err = B.get_data(f, 'Pf_simc_err')                                                                              

dP = Pf_simc - Pf_data                                                                                                    
dP_err = np.sqrt(Pf_simc_err**2 + Pf_data_err**2)     

B.plot_exp(x, dP, dP_err, marker='s', color='blue', label='UnCorrected HMS Momentum')   

B.pl.xlabel('D2 Heep Runs: 3288, 3371, 3374, 3377')
B.pl.ylabel(r'$dP_{simc} -  dP_{data} [GeV]$ ')
B.pl.title('HMS Calculate/Measured Momentum Difference')

B.pl.legend()
B.pl.grid(True)
B.pl.show()