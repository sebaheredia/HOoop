# -*- coding: utf-8 -*-

"""
A signal generator is responsible for generating a carrier signal.

"""

class Generador(object):

    
    #import numpy as np
    def __init__(self, amplitud, fase, frecuencia, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
       

    def generar(self, tiempo_inicial, tiempo_final):

        import math
        import matplotlib.pyplot as pp
        import numpy as np
        cantidad_muestras = int((tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo)
        self.cantidad_muestras=cantidad_muestras

        muestras = range(cantidad_muestras)
        tiempo_muestreo=[i/self.frecuencia_muestreo for i in muestras]
        #TODO agregar un ruido blanco a la senal
        noise=np.random.normal(0,1,cantidad_muestras)/100 
        
         
        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]

        retwithnoise=ret+noise

        return retwithnoise
