import numpy as np
import random
from math import inf 


class Particle:
    """
    Represents a particle of the Particle Swarm Optimization algorithm.
    """
    def __init__(self, lower_bound, upper_bound):
        """
        Creates a particle of the Particle Swarm Optimization algorithm.

        :param lower_bound: lower bound of the particle position.
        :type lower_bound: numpy array.
        :param upper_bound: upper bound of the particle position.
        :type upper_bound: numpy array.
        """
        
        # Creating a list to input the particle parameters (v, Kp, Ki, Kd)
        delta = upper_bound - lower_bound
        self.pos = np.random.uniform(lower_bound, upper_bound)        
        self.vel = np.random.uniform(-delta, delta)
        self.x_min = lower_bound
        self.x_max = upper_bound
        self.v_min = - delta
        self.v_max = delta
        self.best_pos = self.pos.copy()
        self.best_value = -inf   

class ParticleSwarmOptimization:
    """
    Represents the Particle Swarm Optimization algorithm.
    Hyperparameters:
        inertia_weight: inertia weight.
        cognitive_parameter: cognitive parameter.
        social_parameter: social parameter.

    :param hyperparams: hyperparameters used by Particle Swarm Optimization.
    :type hyperparams: Params.
    :param lower_bound: lower bound of particle position.
    :type lower_bound: numpy array.
    :param upper_bound: upper bound of particle position.
    :type upper_bound: numpy array.
    """
    def __init__(self, hyperparams, lower_bound, upper_bound):
        # Todo: implement
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_particles = hyperparams.num_particles
        self.inertia_weight = hyperparams.inertia_weight
        self.cognitive_parameter = hyperparams.cognitive_parameter
        self.social_parameter = hyperparams.social_parameter
        self.best_global_value = -inf
        self.current_index = 0
        
        # Creating a particle swarm
        self.swarm = []
        for _ in range(self.num_particles):
            self.swarm.append(Particle(lower_bound, upper_bound))
            
        self.best_global_pos = self.swarm[0].pos.copy()
                  

    def get_best_position(self):
        """
        Obtains the best position so far found by the algorithm.

        :return: the best position.
        :rtype: numpy array.
        """
        # Todo: implement
        return self.best_global_pos

    def get_best_value(self):
        """
        Obtains the value of the best position so far found by the algorithm.

        :return: value of the best position.
        :rtype: float.
        """
        return self.best_global_value

    def get_position_to_evaluate(self):
        """
        Obtains a new position to evaluate.

        :return: position to evaluate.
        :rtype: numpy array.
        """
        current_particle = self.swarm[self.current_index]
        return current_particle.pos
            

    def advance_generation(self):
        """
        Advances the generation of particles. Auxiliary method to be used by notify_evaluation().
        """
        w = self.inertia_weight
        phi_p = self.cognitive_parameter
        phi_g = self.social_parameter
        
        for particle in self.swarm:
            rp = random.uniform(0.0, 1.0)
            rg = random.uniform(0.0, 1.0)
            
            # Updating velocity
            particle.vel = w * particle.vel + phi_p * rp * (particle.best_pos - particle.pos) + phi_g * rg * (self.best_global_pos - particle.pos)
            particle.vel = np.clip(particle.vel, particle.v_min, particle.v_max)
            
            # Updating position
            particle.pos = particle.pos + particle.vel
            particle.pos = np.clip(particle.pos, particle.x_min, particle.x_max)
            
            
    def notify_evaluation(self, value):
        """
        Notifies the algorithm that a particle position evaluation was completed.

        :param value: quality of the particle position.
        :type value: float.
        """
        
        if value > self.swarm[self.current_index].best_value:
            self.swarm[self.current_index].best_value = value
            self.swarm[self.current_index].best_pos = self.swarm[self.current_index].pos.copy()
            
        if value > self.best_global_value:
            self.best_global_value = value
            self.best_global_pos = self.swarm[self.current_index].pos.copy()
            
        self.current_index += 1
            
        if self.current_index >= self.num_particles:
            self.advance_generation()
            self.current_index = 0
        

