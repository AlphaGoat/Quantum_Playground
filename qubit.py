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
        state = tf.reshape(tf.stack(p0, p1), [2,1])
        self.state = tf.norm(q_state)

        # Number of qubits in system (will always be one when
        # a single qubit is initialized)
        self.register = 1 

    def bra(self):
        '''Get the 'bra' representation of q_state'''
        return tf.reshape(self.q_state, [2, self.n])

    def ket(self):
        '''Get the 'ket' representation of q_state'''
        return tf.reshape(self.q_state, [1,self.n])

    def __measurement__(self):
        '''Perform measurement on quantum system'''
        # NOTE: obviously, not a real quantum implementation.
        # This means that the probability of measuring a state
        # is not perfectly reflected by the quantum state vector.
        # Hence, you will not be able to perfectly simulate a 
        # quantum system with this operation. Our goal is to get
        # 'close enough'
        probabilities = np.square(self.state)
        measured_state = np.random.choice(2^self.register, 
                                         probabilities)
        np.zeros(2^self.register)




    #def __mul__(self, q_other):
        
        


class Q_State(Qubit):
    instanceNum = 0

    def __init__(self, register=1, state=None):
        '''Initializing a state consisting of a number of qbits.
           If no values for the state are offered, the Q_state
           is initialized as |000...00>
        '''
        # Parameters
        #   Input:
        #       register_size (int): number of qubits to intialize
        #                            state with
        #       state (np.array, dtype=np.complex128): state vector
        #                            to initialize state with

        super(Q_state, self).__init__()
        # keep track of number of initialized quantum states (so we
        # can keep track of each instance in in the larger tf graph
        Q_State.instanceNum += 1
        self.register = register
        self.n = 2^register

        if state:
            # Check if state is in correct format. Otherwise raise
            # error
            if state.dtype != np.complex128:
                raise ValueError('\nInput needs to be numpy array
                            of dtype np.complex128')
            # check if state is 2^n long. If not, raise error
            if state.shape[0] != 2^num_qbits:
                raise ValueError('\nLength of state vector not 
                        consistent with the number of qubits
                        being initialized')
            state = state/np.sqrt(np.linalg.norm(state))
            self.state = tf.Variable("q_state{}".format(
                                Q_State.instanceNum-1),
                                state)
        else:
            # initialize |0000...00> state
            state = np.ones([2^register, 1])
            state[0] = 1
            self.state = tf.Variable("q_state{}".format(
                                Q_State.instanceNum-1),
                                state)


def find_bit_representation(register_len, measured_state):
    '''helper function to help determined 'measured' bit string
       for quantum state
    '''



