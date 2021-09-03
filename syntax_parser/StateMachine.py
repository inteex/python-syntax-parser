class StateMachine:
    def __init__(self, states: list[str], initial=None):
        self.currentState = initial
        self.endStates = states

    def add_state(self, name: str):
        self.endStates.append(name)

    def set_state(self, name: str):
        self.currentState = name
