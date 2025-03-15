import pygame

# Class that is given a block_type and creates a block object of that type

class Block:
    def __init__ (self, block_type):
        # Block dimensions
        self.width = 24
        self.height = 24

        # Dictionary containing all blocks and sprite sheet positions
        self.block_dict = {
            "dirt": (0, 0),
            "grass": (self.width, 0)
        }

        # Call a function to get the specified block on the sprite sheet
        self.image = self.get_block(block_type)

    # Get the specified block from the sprite sheet
    def get_block(block_type):
        return