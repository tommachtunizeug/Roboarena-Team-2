import typing
import numpy as np
import time
import random
from PyQt5.QtCore import QObject, QThread

class Bullet:
    def __init__(self, x, y, angle, radius, speed, damage):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.radius = radius
        self.damage = damage

    #calculate new point and update own position
    def move(self):
        dx = self.speed * np.cos(self.angle)
        dy = -self.speed * np.sin(self.angle)
        self.x += dx
        self.y += dy

class BulletThread(QThread):
    is_paused = False
    bullets: list[Bullet] = []
    abort = False                   #this attribute is to be able to end the thread in a controlled manner

    def __init__(self, arena) -> None:
        super().__init__()
        self.arena = arena
        self.pawns = self.arena.pawns

    def run(self) -> None:
        while not self.abort:
            #update internal pawn list
            self.pawns = self.arena.pawns
            if not self.is_paused:
                #traverse a copy of the bullets list to be able to manipulate the original list
                for bullet in self.bullets.copy():
                    bullet.move()
                    #if bullet exits boundaries
                    if not self.isBulletInsideArena(bullet) or self.isTileImpassable(bullet):
                            self.bullets.remove(bullet)
                            continue
                    #check if any pawn is hit and if yes exit this loop
                    for pawn in self.pawns:
                        if self.checkBulletCollision(pawn, bullet):
                            self.bullets.remove(bullet)
                            pawn.applyDamage(bullet.damage)
                            break
            self.msleep(30)
    
    def unpauseBullets(self):
        self.is_paused = False

    def pauseBullets(self):
        self.is_paused = True
    
    def addBullet(self, bullet: Bullet):
        self.bullets.append(bullet)

    def removeBullet(self, bullet: Bullet):
        self.bullets.remove(bullet)

    #checks bullet collision by calculating the distance to the center of the robot and comparing it to the radius of the robot
    def checkBulletCollision(self, robot, bullet):
        distance_squared = (robot.xpos - bullet.x - robot.radius)**2 + (robot.ypos - bullet.y - robot.radius)**2
        return distance_squared <= (robot.radius + bullet.radius)**2
    
    #checks against arena boundaries
    def isBulletInsideArena(self, bullet):
        return 0 <= bullet.x <= self.arena.ArenaWidth * self.arena.TileWidth and 0 <= bullet.y <= self.arena.ArenaHeight * self.arena.TileHeight
    
    #checks for impassable tiles at current position
    def isTileImpassable(self, bullet):
        return self.arena.getTileAtPos(bullet.x, bullet.y).isImpassable
    
    #returns bullet list for drawing
    def getBullets(self):
        return self.bullets

#weapon class, basically a pistol
class Weapon:
    type = ''                           
    damage = 0                      #needs to be defined for each weapon
    radius = 0                      #needs to be defined for each weapon
    speed = 0                       #needs to be defined for each weapon
    time_to_cycle = 0               #needs to be defined for each weapon
    cdcycle = 0                     #cooldown for cycling
    mag = 0                         #needs to be defined for each weapon
    magMax = 0                      #needs to be defined for each weapon
    time_to_reload = 0              #needs to be defined for each weapon
    cdreload = 0                    #cooldown for reloading
    recoil = 0                      #needs to be defined for each weapon
    consecutive_shot_factor = 0     #needs to be defined for each weapon
    speed_factor = 0                #needs to be defined for each weapon
    last_shot = 0                   #time of the last shot
    consecutive_shots = 0           #number of consecutive shots
    recoil_duration = 0             #needs to be defined for each weapon
    alternate = 1                   #needs to be set to -1 for dual-wield weapons
    alternating = 1

    def __init__(self) -> None:
        self.type = 'projectile'                #attribute to indicate the type of projectile in case of further expansion, might be implemented as interface
        self.damage = 5                         #damage of one projectile
        self.radius = 2                         #size of one projectile
        self.speed = 5                          #speed of one projectile
        self.time_to_cycle = 0.2                #how fast projectiles can be fired (here one per 50ms)
        self.cdcycle = 0                        #cooldown on the cycle time
        self.mag = 10                           #magazine capacity
        self.magMax = 10                        #maximum magazine capacity
        self.time_to_reload = 2                 #how fast the magazine can be reloaded (here 2 seconds)
        self.cdreload = 0                       #cooldown on the reload time
        self.recoil = 2                         #recoil as percentage of pi
        self.consecutive_shot_factor = 0.08     #increase in recoil/spread when weapon keeps shooting
        self.speed_factor = 0.02                #increase in recoil/spread when moving
        self.last_shot = 0                      #time of the last shot
        self.consecutive_shots = 0              #number of consecutive shots
        self.recoil_duration = 0.2              #duration of the recoil effecting the weapon (together with cycle time)
        self.alternate = 1                      #this attribute should be set for dual wield weapons
        self.alternating = 1                    #this attribute tracks which weapon should be fired next (for dual-wield weapons)

    def shoot(self, x, y, radius, offset_radius, offset_angle, alpha, speed):
        t = time.time()
        #if the weapon is not reloading and not cycling
        if self.cdreload < t and self.cdcycle < t:
            #if there's ammunition in the magazine
            if self.mag > 0:
                #update number of consecutive shots based on the recoil duration
                if self.last_shot + self.time_to_cycle + self.recoil_duration > t:
                    if self.consecutive_shots < 10:
                        self.consecutive_shots = self.consecutive_shots + 1
                else:
                    #recoil 'decays' faster
                    if self.consecutive_shots - 2 >= 0:
                        self.consecutive_shots = self.consecutive_shots - 2

                bullet_radius = self.radius
                bullet_speed = self.speed

                #establish the spawn point in the arena of the bullet
                bullet_x = (x - radius) + (radius+offset_radius)*np.cos(-alpha+(offset_angle*self.alternating))
                bullet_y = (y - radius) + (radius+offset_radius)*np.sin(-alpha+(offset_angle*self.alternating))
                #
                self.alternating = self.alternating * self.alternate

                #simulates recoil by calculating a angle offset and then drawing a random value from the range offered by the offset
                bullet_recoil = (self.consecutive_shot_factor * self.consecutive_shots + speed**2*self.speed_factor + self.recoil)*np.pi/100
                bullet_alpha = alpha + random.uniform(-bullet_recoil, bullet_recoil)

                bullet = Bullet(bullet_x, bullet_y, bullet_alpha, bullet_radius, bullet_speed, self.damage)

                #reduce the mag and update the cooldown for cycling
                self.mag = self.mag - 1
                self.cdcycle = t + self.time_to_cycle
                self.last_shot = t
                return True, bullet
            else:
                #set mag to magMax and update the cooldown for reloading
                self.mag = self.magMax
                self.cdreload = t + self.time_to_reload
        return False, 0
    
    #manual reload, currently only implemented by enemies
    def reload(self) -> None:
        self.mag = self.magMax
        self.cdreload = time.time() + self.time_to_reload

    #return mag as percentage of magMax
    def getAmmoLeft(self) -> float:
        return self.mag*100/self.magMax
    
    #returns true if the weapon is reloading
    def isReloading(self) -> bool:
        return self.cdreload > time.time()
    
class Cannon(Weapon):
    def __init__(self) -> None:
        self.damage = 10
        self.radius = 4
        self.speed = 18
        self.time_to_cycle = 0.75
        self.mag = 6
        self.magMax = 6
        self.time_to_reload = 6
        self.recoil = 5
        self.consecutive_shot_factor = 0.5
        self.speed_factor = 0.03
        self.recoil_duration = 0.3

class MachineGun(Weapon):
    def __init__(self) -> None:
        self.damage = 5
        self.radius = 2
        self.speed = 20
        self.time_to_cycle = 0.02
        self.mag = 50
        self.magMax = 50
        self.time_to_reload = 10
        self.recoil = 3
        self.consecutive_shot_factor = 0.75
        self.speed_factor = 0.04
        self.recoil_duration = 0.1

class DualPistols(Weapon):
    def __init__(self) -> None:
        self.damage = 5
        self.radius = 2
        self.speed = 10
        self.time_to_cycle = 0.1
        self.mag = 20
        self.magMax = 20
        self.time_to_reload = 6
        self.recoil = 4
        self.consecutive_shot_factor = 0.08
        self.speed_factor = 0.02
        self.recoil_duration = 0.2
        self.alternate = -1

class SniperRifle(Weapon):
    def __init__(self) -> None:
        self.damage = 15
        self.radius = 3
        self.speed = 20
        self.time_to_cycle = 1
        self.mag = 5
        self.magMax = 5
        self.time_to_reload = 8
        self.recoil = 1
        self.consecutive_shot_factor = 1
        self.speed_factor = 0.5
        self.recoil_duration = 1

class AssaultRifle(Weapon):
    def __init__(self) -> None:
        self.damage = 8
        self.radius = 1
        self.speed = 16
        self.time_to_cycle = 0.05
        self.mag = 24
        self.magMax = 24
        self.time_to_reload = 5
        self.recoild = 2
        self.consecutive_shot_factor = 0.5
        self.speed_factor = 0.06
        self.recoil_duration = 0.05