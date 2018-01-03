# -*- coding: utf-8 -*-

# This object define the transmission medium, this may be the atmosphere
class Medio(object):

    def __init__(self,signal,attenuation_coeff):
        self.signal = signal
        self.attenuation_coeff = attenuation_coeff


    def attenuation(self):
        """
        Los blancos en el medio reflejan la senal
        """
        
        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #y devolver la senal reflejada
        #        pass
        return self.signal*self.attenuation_coeff
