import random
import math
from constants import *


class FiniteStateMachine(object):
    """
    A finite state machine.
    """
    def __init__(self, state):
        self.state = state

    def change_state(self, new_state):
        self.state = new_state

    def update(self, agent):
        self.state.check_transition(agent, self)
        self.state.execute(agent)


class State(object):
    """
    Abstract state class.
    """
    def __init__(self, state_name):
        """
        Creates a state.

        :param state_name: the name of the state.
        :type state_name: str
        """
        self.state_name = state_name

    def check_transition(self, agent, fsm):
        """
        Checks conditions and execute a state transition if needed.

        :param agent: the agent where this state is being executed on.
        :param fsm: finite state machine associated to this state.
        """        
        raise NotImplementedError("This method is abstract and must be implemented in derived classes")

    def execute(self, agent):
        """
        Executes the state logic.

        :param agent: the agent where this state is being executed on.
        """
        raise NotImplementedError("This method is abstract and must be implemented in derived classes")


class MoveForwardState(State):
    def __init__(self):
        super().__init__("MoveForward")
        # Todo: add initialization code
        
        # Initializing the counter
        self.counter = 0

    def check_transition(self, agent, state_machine):
        # Todo: add logic to check and execute state transition
        
        # Checking if the roomba collided
        collided = agent.get_bumper_state()
        
        if collided:
            state_machine.change_state(GoBackState())
        else:
            # If did not collide, verify the elapsed time
            if (self.counter * SAMPLE_TIME) > MOVE_FORWARD_TIME:
                state_machine.change_state(MoveInSpiralState())

    def execute(self, agent):
        # Todo: add execution logic
        
        # State behavior
        agent.set_velocity(FORWARD_SPEED, 0)
        
        # incrementing the counter to calculate the elapsed time
        self.counter += 1

class MoveInSpiralState(State):
    def __init__(self):
        super().__init__("MoveInSpiral")
        # Todo: add initialization code
        
        # Initializing the counter
        self.counter = 0
    
    def check_transition(self, agent, state_machine):
        # Todo: add logic to check and execute state transition
        
        # Checking if the roomba collided
        collided = agent.get_bumper_state()
        
        if collided:
            state_machine.change_state(GoBackState())
        else:
            # If did not collide, verify the elapsed time
            if (self.counter * SAMPLE_TIME) > MOVE_IN_SPIRAL_TIME:
                state_machine.change_state(MoveForwardState())

    def execute(self, agent):
        # Todo: add execution logic
        
        # R(t) = Ro + b * t
        r_t = INITIAL_RADIUS_SPIRAL + SPIRAL_FACTOR * (self.counter * SAMPLE_TIME)
        
        # w(t) = v / R(t)
        w_t = FORWARD_SPEED / (r_t)
        
        # State behavior
        agent.set_velocity(FORWARD_SPEED, w_t)
        
        # incrementing the counter to calculate the elapsed time
        self.counter += 1


class GoBackState(State):
    def __init__(self):
        super().__init__("GoBack")
        # Todo: add initialization code
        
        # Initializing the counter
        self.counter = 0

    def check_transition(self, agent, state_machine):
        # Todo: add logic to check and execute state transition
        
        # checking the time moving back
        if (self.counter * SAMPLE_TIME) > GO_BACK_TIME:
            state_machine.change_state(RotateState())

    def execute(self, agent):
        # Todo: add execution logic
        
        # State behavior
        agent.set_velocity(BACKWARD_SPEED, 0)
        
        # incrementing the counter to calculate the elapsed time
        self.counter += 1


class RotateState(State):
    def __init__(self):
        super().__init__("Rotate")
        # Todo: add initialization code
        
        # Initializing the counter
        self.counter = 0
        
        # Select a random value in [-π, π)
        self.rotate_angle = random.uniform(-PI, PI - 1e-10)

    def check_transition(self, agent, state_machine):
        # Todo: add logic to check and execute state transition
        if (self.counter * SAMPLE_TIME) > abs(self.rotate_angle / ANGULAR_SPEED):
            state_machine.change_state(MoveForwardState())
    
    def execute(self, agent):
        # Todo: add execution logic
        
        # State behavior
        if self.rotate_angle < 0:
            agent.set_velocity(0, -ANGULAR_SPEED)
        else:
            agent.set_velocity(0, ANGULAR_SPEED)
        
        # incrementing the counter to calculate the elapsed time
        self.counter += 1
