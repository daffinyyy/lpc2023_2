from tank import Tank

class Game:
    def __init__(self):
        self.tank = Tank(0, 0)

    def run(self):
        while True:
            command = input("Pressione w/a/s/d para mover o tanque, f para atirar ou q para sair: ").lower()
            if command == 'q':
                break
            elif command in ['w', 'a', 's', 'd']:
                self.tank.move(command)
                print("O tanque se moveu para", self.get_direction_name(command))
            elif command == 'f':
                self.tank.shoot()
                print("O tanque atirou!")
            else:
                print("Comando inválido. Use w/a/s/d para mover, f para atirar ou q para sair.")

    def get_direction_name(self, direction):
        if direction == 'w':
            return "para cima"
        elif direction == 'a':
            return "para a esquerda"
        elif direction == 's':
            return "para baixo"
        elif direction == 'd':
            return "para a direita"
