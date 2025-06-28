START_POSITION_CAR = -0.5


def reward_engineering_mountain_car(state, action, reward, next_state, done):
    """
    Makes reward engineering to allow faster training in the Mountain Car environment.

    :param state: state.
    :type state: NumPy array with dimension (1, 2).
    :param action: action.
    :type action: int.
    :param reward: original reward.
    :type reward: float.
    :param next_state: next state.
    :type next_state: NumPy array with dimension (1, 2).
    :param done: if the simulation is over after this experience.
    :type done: bool.
    :return: modified reward for faster training.
    :rtype: float.
    """
    
    # Extrai a posição e a velocidade do próximo estado, que é o resultado da ação.
    pos = next_state[0]
    vel = next_state[1]
    
    # Adiciona um componente de recompensa proporcional à distância ao quadrado do ponto inicial.
    # Isso incentiva o agente a se mover para longe do fundo do vale.
    reward += (pos - START_POSITION_CAR) ** 2
    
    # Adiciona um componente de recompensa proporcional à velocidade ao quadrado.
    # Isso incentiva o agente a ganhar momento, que é crucial para resolver o problema.
    reward += vel ** 2
    
    # Se o agente atingiu o objetivo (posição >= 0.5) e o episódio terminou,
    # ele recebe uma grande recompensa adicional.
    if done and pos >= 0.5:
        reward += 50.0
    return reward


