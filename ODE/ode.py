# Author: Hsuan-Hao Fan
import numpy as np

class ODE:
    """
    ==================================================
    
    Solve ODE in the general form: dy(t)/dt = f(t,y)
    
    ==================================================
    """
    
    def __init__(self, fun, y0, tspan, steps=101):
        """
        fun:   function f(t, y)
        y0:    initial conditions
        
               y0[i] = y(t=0)[i],
               
               where i = 0, ..., len(y0) - 1
        
        tspan: tspan = [t0, tf] is the time interval with 
               starting time t0 and ending time tf
               
        steps: int 
        
               number of points in [t0, tf]
        """
        self.f = fun
        self.y0 = np.array(y0)
        self.tspan = tspan
        self.steps = steps
        
       
        

class Euler(ODE):
    """
    ====================================================
    
            Solve ODE by Euler algorithm
    
    ====================================================
    """
    
    def integrate(self):
        """
        =================================================
        
        Find y=y(t), set y = y0 as an initial condition
        
        =================================================
        
        Returns
        -------
        t:      independent variable
        target: y(t)
                
                y[i] = y(t)[i],
               
                where i = 0, ..., len(y) - 1
        
        """
        # Set-up
        t0 = self.tspan[0]
        tf = self.tspan[1]
        n = self.steps
        h = (tf - t0)*1.0/(self.steps - 1)
        
        t = np.linspace(t0, tf, n)
        target = np.zeros((len(self.y0), n))               # Response variable at various t
        target[:,0] = self.y0
        y = self.y0

        
        if len(self.y0) == 1:
            f = self.f(t[0], self.y0[0]) 
        else:
            f = np.concatenate( (self.y0[-len(self.y0) + 1:], np.array([self.f(t[0], self.y0)]) ), axis = 0)
        
       
        # The forward difference algorithm for the derivative
        for i in range(1, self.steps):
            
            # update y
            y = y + h* f
            
            # Record response variable at t[i]
            target[:,i] = y
            
            # update f 
            if len(self.y0) == 1:
                f = self.f(t[i], y[0]) 
            else:
                f = np.concatenate( (y[-len(self.y0) + 1:], np.array([self.f(t[i], y)]) ), axis = 0)
          
        return t, target
  
        