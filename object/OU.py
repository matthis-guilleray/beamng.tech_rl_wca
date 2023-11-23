import numpy as np

class OrnsteinUhlenbeckNoise():
    """
    Noise function use to train the network, the math to reproduce can be found on the wikipedia 
    page : Ornstein Uhlenbeck Noise

    """

    def __init__(self, m, s=0.15, t=0.2, dt=1e-2, x=None):
        """
        Initialisation of the Ornstein Uhlenbeck Noise class, 
        - m : mu variable
        - s : Sigma
        - t : tau
        - dt : 
        - x : to init the fct using a previous state
        
        """
        self.t = t
        self.m = m
        self.s = s
        self.dt = dt
        if x is None : 
            self.reset()
        else :
            self.x_prev = x

    def get(self):
        """
        get the noise
        """
        x = self.x_prev + self.t * (self.m - self.x_prev) * self.dt + self.s * np.sqrt(self.dt)*np.random.normal(size=self.m.shape)
        self.x_prev = x
        return x


    def reset(self):
        """
        Reseting the X
        """
        self.x_prev = np.zeros_like(self.m)