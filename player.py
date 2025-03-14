import pygame

# Player class
class Player:
    def __init__(self, screen_width, screen_height):
        # Player dimensions
        self.size = 25  # 25x25 pixels
        self.scale = 2
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Movement and speed
        self.x = screen_width // 2 - self.size // 2  # Centered horizontally
        self.y = screen_height - self.size - 40
        self.speed = 3
        self.moving = False
        
        # Load sprite sheet
        self.sprite_sheet = pygame.image.load("cat.png").convert_alpha()
        self.frame_width = 25
        self.frame_height = 25
        self.number_of_frames = 4
        self.images = self.load_images()
        self.current_image = 0
        self.direction = "right"
        
        # Animation timing
        self.animation_timer = 0
        self.animation_speed = 10
    
    def load_images(self):
        images = []
        for i in range(self.number_of_frames):
            img = self.sprite_sheet.subsurface(pygame.Rect(i * self.frame_width, 0, self.frame_width, self.frame_height))
            img = pygame.transform.scale(img, (self.size * self.scale, self.size * self.scale))  # Scale by 2
            images.append(img)
        return images
    
    def animate(self):
        # Handles sprite animation while moving
        if self.moving:  # Only animate when moving
            self.animation_timer += 1
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_image = (self.current_image + 1) % len(self.images)
        
        if not self.moving:
            self.current_image = 1 # return to starting position
            # TODO
            # Update sprite sheet and implement idle player animation
    
    def update(self):
        # Updates player movement and animation
        keys = pygame.key.get_pressed()
        self.moving = False  # Reset moving state
        
        if keys[pygame.K_LEFT]:
            self.direction = "left"  # change to left
            self.x -= self.speed
            self.moving = True
        if keys[pygame.K_RIGHT]:
            self.direction = "right"  # change to right
            self.x += self.speed
            self.moving = True
        
        # Keep player within screen boundaries
        self.x = max(0, min(self.x, self.screen_width - self.size * self.scale))
        
        # Animate
        self.animate()
    
    def draw(self, screen):
        # Get the current frame
        current_frame = self.images[self.current_image]
        
        # Flip if facing left
        if self.direction == "left":
            current_frame = pygame.transform.flip(current_frame, True, False)
        
        # Draw the player
        screen.blit(current_frame, (self.x, self.y))