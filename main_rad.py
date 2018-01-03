# -*- coding: utf-8 -*-

'''
This is the main function where the principal attributes of the radar object are defined.
In addition, the the radar object is imported and excecuted.
'''

import Radar_ob
import math
import datetime
amplitud = 0.2
fase = 1
frecuencia = 20*math.pi
tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
tiempo_final = datetime.datetime(2016, 3, 5, 10)
attenuation_coeff=0.8
target_refl_coeff = 0.7 # Target reflection coefficient
attenuation_coeff_back=0.75
radar_threshold=0.007

rad_ob2=Radar_ob.Radar_object(amplitud, fase, frecuencia, tiempo_inicial, tiempo_final, attenuation_coeff,target_refl_coeff,attenuation_coeff_back,radar_threshold)
rad_ob2.calculator()
rad_ob2.plotear_senal()