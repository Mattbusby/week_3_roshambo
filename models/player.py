class Player():

    def __init__(self, name, weapon):
        self.weapon = weapon
        self.name = name
        
    def roshambo(name1, weapon1, name2, weapon2):
        if weapon1 == weapon2:
            return f"It's a draw"
        elif weapon1 == "rock" and weapon2 == "scissors":
            return f"{name1} wins with rock"
        elif weapon1 == "rock" and weapon2 == "paper":
            return f"{name2} wins with paper"
        elif weapon1 == "paper" and weapon2 == "scissors":
            return f"{name2} wins with scissors"
        elif weapon1 == "paper" and weapon2 == "rock":
            return f"{name1} wins with paper"
        elif weapon1 == "scissors" and weapon2 == "paper":
            return f"{name1} wins with scissors"
        elif weapon1 == "scissors" and weapon2 == "rock":
            return f"{name2} wins with rock"

