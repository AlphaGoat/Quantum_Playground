'''File defining basic structure of a qubit'''

import tensorflow as tf
import numpy as np

# Overloaded operators specific to Qubit arithmetic


class Qubit(object):

    def __init__(self, p0, p1):
        '''initial state of qubit'''
        # Parameters:
        #   p0 (): probability of qubit being in state 0
        #                      or state 1, represented as 
        #                      dtype=tf.complex
        #   p1 (tf.scalar): probability of qubity being in state 1,
        #                   represented as dtype=tf.complex 
        q_state = tf.stack(p0, p1)
        norm_q_state = tf.norm(q_state)]
        self.q0 = norm_q_state[0]
        self.q1 = norm_q_state[1]

    def bra(self):
        '''Get the 'bra' representation of q_state'''
        return tf.reshape(self.q_state, [2, 1]_

    def ket(self):
        '''Get the 'ket' representation of q_state'''
        return tf.reshape(self.q_state, [1,2])

    def __mul__(self, q_other):
        


class Q_State(Qubit):

    def __init__
