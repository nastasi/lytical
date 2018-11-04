#!/usr/bin/env python
import time
from visual import *

# , userspin=True, userzoom=True
scene2 = display(title='Examples of Tetrahedrons',
     x=-200, y=-200, width=1200, height=800,
                 center=(0,0,0), autoscale=False)

data_white = materials.loadTGA('img/white-dotty.tga')
data_orange = materials.loadTGA('img/orange-dotty.tga')
tex_white = materials.texture(data=data_white, mapping="spherical", interpolate=True)
tex_orange = materials.texture(data=data_orange, mapping="spherical", interpolate=True)

ball_white = sphere(pos=(-5,-2,0), radius=0.5, material=tex_white)
ball_orange = sphere(pos=(-5,2,0), radius=0.5, material=tex_orange)

wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)

ball_white.velocity = vector(25,0,0)
ball_orange.velocity = vector(25,0,0)
deltat = 0.0005
t = 0
while t < 3:
    rate(50)
    if ball_white.pos.x > wallR.pos.x:
        ball_white.velocity.x = -ball_white.velocity.x
    ball_white.pos = ball_white.pos + ball_white.velocity*deltat
    ball_white.rotate(angle=pi/120, axis=(0,1,0), origin=ball_white.pos)
    ball_white.rotate(angle=pi/120, axis=(1,0,0), origin=ball_white.pos)

    if ball_orange.pos.x > wallR.pos.x:
        ball_orange.velocity.x = -ball_orange.velocity.x
    ball_orange.pos = ball_orange.pos + ball_orange.velocity*deltat
    ball_orange.rotate(angle=pi/120, axis=(0,1,0), origin=ball_orange.pos)
    ball_orange.rotate(angle=pi/120, axis=(1,0,0), origin=ball_orange.pos)

    t = t + deltat    
