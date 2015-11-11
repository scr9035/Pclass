from __future__ import print_function
import random


class Combat:
    """Set success or failure of combat moves based on range.
    Values may be changed by player or monster attributes."""
    dodge_limit = 6
    attack_limit = 6
    block_limit = 6
    run_limit = 4

    def dodge(self):
        """Set success or failure of dodging an attack."""
        roll = random.randint(1, self.dodge_limit)
        return roll > 3

    def attack(self):
        """Set success or failure of attack."""
        roll = random.randint(1, self.attack_limit)
        return roll > 3

    def block(self):
        """Set success or failure of blocking an attack."""
        roll = random.randint(1, self.block_limit)
        return roll > 3

    def run(self):
        """Set success or failure of running away from a monster."""
        roll = random.randint(1, self.run_limit)
        return roll > 3