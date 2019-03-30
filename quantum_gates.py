import tensorflow as tf
import numpy as np



class Q_Gate(object):

    def __init__(self):
        # random accessories I want for all quantum gates

    def __mul__(self, qbit):

        if isinstance(qbit, Q_State):
            return tf.tensordot(self.operator, qbit)

        else:
            print("Error: Object input not of type 'Qubit'")


class HadamardTransform(Q_Gate):

    def __init__(self):

        super(HadamardTransform, self).__init__()
        mat = tf.constant([[1., 1.],[1., -1.]], dtype=tf.complex128)
        self.operator = tf.multiply(mat, 1/np.sqrt(2)) 


class PhaseShifterGate(Q_Gate):

    def __init__(self, theta, mode='rad'):
        '''Performs a phase shift operation on qubit being
           operated on
        '''
        # Parameters:
        #   Input:
        #       theta (np.float64): degree of phase shift to
        #                           be induced on operated
        #                           qubit
        #       mode (str): whether or not the input phase 
        #                   shift is in degrees or radians.
        #                   'rad' for radians, 'deg' for degrees
        super(PhaseShifterGate, self).__init__()
        if mode == 'deg':
            theta = theta * (np.pi/180)
        self.operator = tf.constant([[1., 0],
                            [1.,np.exp(np.complex(0,-theta)))


class ControlledGate(Q_Gate):

    def __init__(self): 
        pass


class ControlledNotGate(Q_Gate):

    def __init__(self):
        
        super(ControlledNotGate, self).__init__()
        self.operator = tf.constant([1., 0., 0., 0.],
                                    [0., 1., 0., 0.],
                                    [0., 0., 0., 1.],
                                    [0., 0., 1., 0.]
                                   )


class PauliMatrices(Q_Gate):

    def __init__(self):

        super(









