# Python implementation of basic queueing theory

## Queue(lam, mu, server)

**Queue(lam, mu, server)** - main object, charactarized by **lam** - intensity of incoming flow; **mu** - intensity of service flow, **server** - number of serving instances. If all servers are occupied, the request is denied.

### Queue attributes

 - **Queue.lam**: arrival flow intensity;  
 - **Queue.mu**: service flow intensity;   
 - **Queue.server**:  number of servers;   
 - **Queue.free_period**: Expected value of an interval between two arrivals;   
 - **Queue.ro**: lam/mu;   
 - **Queue.rejection**: Probability of a claim being rejected;   
 - **Queue.p_service**: relative serving rate (probability of a claim being served);  
 - **Queue.service**: absolute serving rate (number of claims being served during time 1);   

### Queue methods

 - **Queue.arrivals_pdf(delta_t)**:  probability function of at least one arrival during delta_t  
 - **Queue.arrivals(n, delta_t)**: probability of number of arrivals being n during delta_t  
 - **Queue.state(x)**: limit probability of x servers being occupied  
 - **Queue.state_table(rounder=None)**: probability table for different states of Queue. If rounder is specified, results are rounded.
 - **Queue.revenue(price, wage)**: calculates revenue given that the wage of server is wage and price of service is price

 ## Functions

  - **state_table(lam, mu, server)**: realisation of Queue.state_table() as a function

