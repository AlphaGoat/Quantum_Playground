'''Model of the two mode interferometric lidar scheme as presented
   in the paper "Super-resolving quantum lidar: entangled coherent-state
   sources with binary-outcome photon counting measurement suffice to
   beat the shot-noise limit", Wang et. al
'''

import numpy as np
import tensorflow as tf


class two_mode_interferometer(object):
    '''Builds objects necessary to simulate effects stacking Mach-Zehnder
       Interferometer (MZI) with two fictitious beam splitters (FBS)
       and phase shifter (del_alpha) have on the wave functions of the
       entangled state consisting of the coherent superposition
       state (CSS) and coherent state (CS) injected into either port'''

    def __init__(self, N, wavelength, range, css=None, cs=None, T=1):
        '''Input: two beam states that we want to simulate'''
        # Input parameters:
        #   N: number of photons we would like to simulate in each state
        #   wavelength: photon wavelength to be used
        #   range: range of the target being imaged
        #   css: state of the coherent superposition state
        #   cs: state of the coherent state
        #   T: Transmissivity. T = 1 corresponds to a lossless case
        #
        self.N = N
        self.scalar_alpha = np.sqrt(self.N)
        self.N_alpha = (2*(1 + np.euler(-(np.abs(self.scalar_alpha))^2)))^(-1/2)
        if css != None:
            self.css = css
        else:
            self.css =

        if cs != None:
            self.cs = cs
        else:
            self.scalar_alpha/np.sqrt(2)

        # Parameters for the fictitious beam splitter
        self.T = T
        # Reflectivity
        self.R = 1 - self.T

        # Density matrix
        density_matrix = np.zeros()



    def fifty_fifty_beam_splitter(self, ):
        '''Splits incident beam 50/50 via reflection and refraction'''
        pass
        return

    def fictitous_beam_splitter(self, percent_drop=0.05):
        '''Fictitous beam splitter to represent photon loss through
           beam path
        '''
        pass
        return

    def phase_shift_function(self, t):
        '''Operation representing the phase shift accumulated for the ECS
           in path a
        '''
        # Unitary evolution U_
        # k: wave number
        k = 2 * pi / wavelength
        psi = 2 * k * r
