**************************
SHMS Mispointing Studies                             
**************************

---December 28, 2018-----

Observation: A mis-match between DATA/SIMC z-vertex was observed. This quantity depends on Spectrometer
Ytar mispointing and beam offsets (which are equivalent to Ytar mispointing.

Run 3288 was analyzed with and without beam/mispointing offsets.  

DATA Observations: Without any offstes, SHMS Ytar appeared centerd at zero, as well as beam_x offset.
With SHMS Y Mispointing offset and BMP X Offset:

SHMS Ytar ---> Shifted spectrometer beam right ('-' Ytar values)
BPM X ------> Shifted hall beam right (also equivalently '-' Ytar values)  (Assuming this is in EPICS Coordinate System)

This is consistent with the overall SHMS React Z offset observed, as the effect does not cancel out.

This is contradictory to the SHMS X BPM sign given in hcana (which supposedly is in BPM Coordinate System)
                                                   
*****************************                                                   
*SPECTROMETER MISPOINTING*                                                      
*****************************                                                   
                                                                                
HMS X Mispointing   : 0.083188 cm                                               
HMS Y Mispointing   : 0.286020 cm                                               
                                                                                
SHMS X Mispointing   : -0.126000 cm                                             
SHMS Y Mispointing   : -0.060000 cm                                             
                                                                                
                                                                                
************************************                                            
*Calibrated Beam Positions @ Target                                             
************************************                                            
                                                                                
HMS X BPM   : -0.147567 cm                                                      
HMS Y BPM   : -0.125786 cm                                                      
                                                                             
SHMS X BPM   : -0.147567 cm                                                     
SHMS Y BPM   : -0.125786 cm     