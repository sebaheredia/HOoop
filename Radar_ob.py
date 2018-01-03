# -*- coding: utf-8 -*-

"""
The object radar calculate (and graphs with method graphicator) the involved signals in the general radar acquisition process. In addition this object determines if a target is or not detected 

"""

class Radar_object(object):
    import os, sys
    root_dir="/home/sebaheredia/Dropbox/documentos/cursos/TecnicasDeProgramacionCientifica/ejercicios/labdia2/HOoop.git/HOoop"
    os.chdir(root_dir)
    os.getcwd()
    os.listdir(".")

    def __init__(self, amplitud, fase, frecuencia, tiempo_inicial, tiempo_final, attenuation_coeff,target_refl_coeff,attenuation_coeff_back,radar_threshold):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia
        self.frecuencia_muestreo = frecuencia*3
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
        self.attenuation_coeff = attenuation_coeff
        self.target_refl_coeff = target_refl_coeff
        self.attenuation_coeff_back = attenuation_coeff_back
        self.radar_threshold = radar_threshold



    def calculator(self):
        import medio
        import blanco
        import generador
        import datetime
        import detector
        import numpy as np
        
        # Signal Generator with noise
        gen=generador.Generador(self.amplitud,self.fase,self.frecuencia,self.tiempo_inicial,self.tiempo_final)
        # Calculationof the generated signal with the method generar of class Generador
        gen_sig = gen.generar(self.tiempo_inicial, self.tiempo_final)
        # Save the generated signal as an attribute
        self.gen_sig=gen_sig
        self.cantidad_muestras=gen.cantidad_muestras
        
        #Transmission medium
        att=medio.Medio(gen_sig, self.attenuation_coeff)
        # The method attenuation of class Medio calculate the attenuation due to trasnmission medium
        att_sig=att.attenuation()
        self.att_sig=att_sig
    
        #Target   
        refl=blanco.Blanco(att_sig,self.target_refl_coeff)
        #Reflected signal
        refl_sig = refl.reflejar()
        self.refl_sig=refl_sig
    
        # Signal is attenuates again on its back way to radar. 
        att_back=medio.Medio(refl_sig,self.attenuation_coeff_back)
        measured_signal=att_back.attenuation()
        self.measured_signal=measured_signal
        
        #Detector
        det=detector.Detector(measured_signal,self.radar_threshold)
        # for detected target: detection=1, in other case detection=0
        detection=det.detectar()
        self.detection=detection
        
        if detection==1:
            print "La señal fue detectada"
        else:
            print "La señal no fue detectada"
            
            
    def plotear_senal(self):
        import matplotlib.pyplot as pp
        fig_sig=pp.figure()
        line1, =pp.plot(pow(self.gen_sig,2), '-k')
        line2, =pp.plot(pow(self.att_sig,2), '-g')
        line3, =pp.plot(pow(self.refl_sig,2), '-b')
        line4, =pp.plot(pow(self.measured_signal,2), '-c')    
        line5, =pp.plot([1, self.cantidad_muestras], [self.radar_threshold, self.radar_threshold], 'r-')
        pp.legend([line1,line2,line3,line4,line5], ['Generated Sig.','Forward Att. Sig.','Target Ref. Sig.','Measured Sig.','Detection Threshold'])
        pp.title('Radar Signals')
        pp.ylabel('Pot')
        pp.grid(True)
        pp.xlabel('Muestra #')
        pp.show()
        fig_sig.savefig('/home/sebaheredia/Dropbox/documentos/cursos/TecnicasDeProgramacionCientifica/ejercicios/labdia2/HOoop.git/HOoop/radar_signals.png') #fig.show()



   