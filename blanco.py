# -*- coding: utf-8 -*-

class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, senal, refl_coeff):
        #TODO: completar con la inicializacion de los parametros del objeto
        self.senal=senal
        self.refl_coeff=refl_coeff
        

    def reflejar(self):

        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        return self.senal*self.refl_coeff
       
        
