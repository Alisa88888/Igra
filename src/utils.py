from dataclasses import dataclass


@dataclass
class MaxSpeed:
    x: tuple[int, int]
    y: tuple[int, int]

    @property
    def all_max(self):
        return sum(map(abs, self.x)) + sum(map(abs, self.y))

