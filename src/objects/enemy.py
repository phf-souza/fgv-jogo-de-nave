import pygame
from pygame import Vector2
import random 

from src.objects.object import Object
from src.sprites import sprites

#criar a classe inimigo
class Enemy(Object):
    def __init__(self, screen, speed,typo):
        self.screen = screen
        self.speed = speed
        self.type=typo
        self.direction=1
           
#posição
        super().__init__(1000,0, 50, 50)

        self.sprite = pygame.transform.scale(sprites.red_ship_3, (int(self.size.x), int(self.size.y)))

#movimentos dos inimigos
   
    
    #(movimento para 
    def update (self ,dt):
        if self.type==5:
            if self.pos.x <=0 or self.pos.x+self.size.x >= 600 :
                self.direction=self.direction*(-1)
            if self.direction== 1 :
                delta=pygame.Vector2(self.speed*dt*(-1),self.speed*dt)  
            else :
                delta=pygame.Vector2(self.speed*dt*(-1),self.speed*dt*(-1))
            self.move_by(delta)
        else:
            delta=pygame.Vector2(-self.speed*dt,0) 
            self.move_by(delta) 

    def draw(self):
        self.screen.blit(self.sprite, (self.pos.x, self.pos.y))
#spawn 

    def spawn(self):
        delta=pygame.Vector2(1050,random.randint(0,550))     
        self.move_to(delta)

    