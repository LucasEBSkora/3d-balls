import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# import pygame
# from pygame.locals import *

# from OpenGL.GL import glVertex3fv, glBegin, GL_QUADS, glEnd, glTranslatef, glRotatef, glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
# from OpenGL.GLU import gluPerspective

from math import ceil, sin, cos, pi

def draw_axis():
  glBegin(GL_LINES)

  glColor3fv( ( 1, 0, 0)) #eixo x: vermelho
  glVertex3fv(( 0, 0, 0))
  glVertex3fv((10, 0, 0))
  
  glColor3fv( ( 0, 1, 0)) #eixo y: verde
  glVertex3fv(( 0, 0, 0))
  glVertex3fv(( 0,10, 0))
  
  glColor3fv( ( 0, 0, 1)) #eixo z: azul
  glVertex3fv(( 0, 0, 0))
  glVertex3fv(( 0, 0,10))

  glEnd()
  
angular_step = pi/15

def get_ball_point(phi, theta, K, N) :
  r = K*(abs(sin(phi)*cos(theta))**N + abs(sin(phi)*sin(theta))**N + abs(cos(phi))**N)**(-1.0/N)
  return (r*sin(phi)*cos(theta), r*sin(phi)*sin(theta), r*cos(phi))

def draw_ball(K, N): #K -> raio da bola; N-> norma N-ésima usada
  glBegin(GL_QUADS)
  phi = 0
  theta = 0
  glColor4fv((0.5, 0.5, 0.5, 0.25))

  while (phi < pi) :
    while (theta < 2*pi) :
      glVertex3fv(get_ball_point(phi, theta, K, N))
      glVertex3fv(get_ball_point(phi, theta + angular_step, K, N))
      glVertex3fv(get_ball_point(phi + angular_step, theta + angular_step, K, N))
      glVertex3fv(get_ball_point(phi + angular_step, theta, K, N))
      theta += angular_step
    theta = 0
    phi += angular_step
  glEnd()

def main():
  pygame.init()
  display = (800, 600)
  pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
  glEnable(GL_BLEND);
  gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
  glTranslatef(.0, .0, -10)
  glRotatef(-60, 1, 0, 0)
  glRotatef(-135, 0, 0, 1)
  
  add = 0.02
  K = 2
  N = 1

  while True:
    if (N <= 1) :
      N = 1
      add *= -1
    elif (N >= 10):
      N = 10
      add *= -1

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    glRotatef(-0.25, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_axis()
    draw_ball(K, N)
    pygame.display.flip()
    pygame.time.wait(10)
    N += add*N

main()

# vertices = (
#   ( 1, -1, -1),
#   ( 1,  1, -1),
#   (-1,  1, -1),
#   (-1, -1, -1),
#   ( 1, -1,  1),
#   ( 1,  1,  1),
#   (-1, -1,  1),
#   (-1,  1,  1),
# )

# edges = (
#   (0,1),
#   (0,3),
#   (0,4),
#   (2,1),
#   (2,3),
#   (2,7),
#   (6,3),
#   (6,4),
#   (6,7),
#   (5,1),
#   (5,4),
#   (5,7),
# )

# surfaces = (
#   (0,1,2,3),
#   (3,2,7,6),
#   (6,7,5,4),
#   (4,5,1,0),
#   (1,5,7,2),
#   (4,0,3,6),
  
# )

# def CubeLines() :
#   glBegin(GL_LINES)
#   for edge in edges:
#     for vertex in edge:
#       glVertex3fv(vertices[vertex])
#   glEnd()

# def Cube() :
#   glBegin(GL_TRIANGLES)
#   for surface in surfaces:
#     glColor3fv((0.5, 0.5, 0.5))
#     for vertex in surface:
#       glVertex3fv(vertices[vertex])
#   glEnd()