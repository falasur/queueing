# Module with basic functions and objects of queueing theory
import math
from scipy import stats


class Queue:
    def __init__(self, lam, mu, server):
        if not (isinstance(lam, float) and isinstance(mu, float)):
            raise TypeError('lam, mu must be floats')
        elif not isinstance(server, int):
            raise TypeError('Number of servers must be an integer')
        # Arrival flow intensity;
        self.lam = lam
        # Service flow intensity;
        self.mu = mu
        # Number of servers;
        self.server = server
        # Expected value of an interval between two arrivals;
        self.free_period = 1/lam
        self.ro = lam/mu
        # Probability of a claim being rejected;
        self.rejection = self.state(server)
        # Relative serving rate (probability of a claim being served);
        self.p_service = 1 - self.rejection  
        # Absolute serving rate (number of claims being served during time 1);
        self.service = self.lam*self.p_service

    def arrivals_pdf(self, delta_t): 
        # Probability function of at least one arrival during delta_t
        return 1 - math.exp(-self.lam*delta_t) 
        # must be eventually rewritten using scipy.stats
 
    def arrivals(self, n, delta_t):
        # Probability of number of arrivals being n during delta_t
        return (math.exp(-(self.lam*delta_t))*(self.lam*delta_t)**n)/math.factorial(n) # must be tested

    def state(self, n):
        # Probability of n servers being busy, if n = self.server, system is being fully occupied
        if n > self.server and isinstance(n, int):
            raise ValueError('n cannot exceed the number of servers')
        elif not isinstance(n, int):
            raise TypeError('n must be integer')
        return (self.ro**n/math.factorial(n)) * \
               (sum([self.ro**x/math.factorial(x) for x in range(self.server + 1)]))**-1 

    def state_table(self, rounder=None):  
        # Returns dictionary of states and their respective probabilities
        if rounder is None:
            return {x: self.state(x) for x in range(self.server + 1)}
        else:
            return {x: round(self.state(x), rounder)
                    for x in range(self.server + 1)}

    def revenue(self, price, wage): 
        '''Estimates revenue given that the wage of server is wage and price of service is price'''
        return self.service * price - wage * self.server


def state_table(lam, mu, server):  # Not tested yet
    """Realisation of Queue.state_table() as a function."""
    if not isinstance(server, int):
        raise ValueError('server must be integer')
    return {i: ((lam/mu)**i/math.factorial(i)) *
                (sum([(lam/mu)**x/math.factorial(x) for x in range(server + 1)]))**-1
            for i in range(server+1)}
