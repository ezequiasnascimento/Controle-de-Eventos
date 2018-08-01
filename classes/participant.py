class Participant:
    cpf = None
    user_type = None

    def __init__(self, cpf: object = None, user_type: object = None):
        self.cpf = cpf
        self.user_type = user_type
