class Vehicle:
    running = False

    def __init__(self, owner):
        self.owner = owner

    def is_running(self):
        if self.running:
            print(f"It is running")
        else:
            print(f"It is not running")


v1 = Vehicle(owner="Divine Favour")
