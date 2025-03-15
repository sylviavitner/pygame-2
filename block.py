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
        self.sprite_sheet = pygame.image.load("dirt-temp.png") # temp sprite sheet
        self.image = self.get_block(block_type)

    # Get the specified block from the sprite sheet
    def get_block(self, block_type):
        # Handle non block-type errors
        if block_type not in self.block_dict:
            raise ValueError(f"Unknown block type: {block_type}")
        
        x, y = self.block_dict[block_type] # Get the position of the block in the sprite sheet

        # Return the specified block
        return self.sprite_sheet.subsurface(pygame.Rect(x, y, self.width, self.height))
