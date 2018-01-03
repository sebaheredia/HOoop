# -*- coding: utf-8 -*-

class Detector(object):
    import numpy as np
    def __init__(self,senal,umbral):
        #TODO: completar con la inicializacion de los parametros del objeto
        self.umbral=umbral
        self.senal=senal

    def detectar(self):   
        if max(pow(self.senal,2))>self.umbral:
            return 1
        else:
            return 0
    