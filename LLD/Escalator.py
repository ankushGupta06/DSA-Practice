from enum import Enum


# ======================
# ENUMS
# ======================

class Direction(Enum):
    UP = 1
    DOWN = 2


class EscalatorState(Enum):
    RUNNING = 1
    STOPPED = 2


# ======================
# ESCALATOR
# ======================

class Escalator:
    def __init__(self, max_weight: int):
        self.direction = None
        self.state = EscalatorState.STOPPED
        self.current_weight = 0
        self.max_weight = max_weight

    def set_direction(self, direction: Direction):
        if self.state == EscalatorState.RUNNING:
            raise Exception("Stop escalator before changing direction")
        self.direction = direction

    def add_weight(self, weight: int):
        if self.current_weight + weight > self.max_weight:
            raise Exception("Overload detected")
        self.current_weight += weight

    def remove_weight(self, weight: int):
        self.current_weight = max(0, self.current_weight - weight)

    def start(self):
        if self.direction is None:
            raise Exception("Set direction first")
        if self.current_weight > self.max_weight:
            raise Exception("Overloaded")
        self.state = EscalatorState.RUNNING
        print(f"Escalator started moving {self.direction.name}")

    def stop(self):
        self.state = EscalatorState.STOPPED
        print("Escalator stopped")


# ======================
# DEMO
# ======================

if __name__ == "__main__":
    escalator = Escalator(max_weight=500)

    escalator.set_direction(Direction.UP)
    escalator.add_weight(300)
    escalator.start()

    escalator.stop()
