from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from math import *


def init_projection_plus_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, .5, 1000)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 20, 35,
              0, 0, -100,
              0, 1, 0)



def spaceship_draw():
    # glBegin(GL_QUADS)
    # for face in chair_faces_vector4:
    #     x = 0
    #     for vertex in face:
    #         x+=1
    #         glColor3fv(colors[x])
    #         glVertex3fv(chair_verticies_vector3[vertex])
    # glEnd()
    glPushMatrix()
    glRotate(-180, 0, 1, 0)
    glScale(.12, .12, .12)
    glBegin(GL_LINES)
    for edge in chair_edges_vector2:
        for vertex in edge:
            glVertex3fv(chair_verticies_vector3[vertex])
    glEnd()
    glPopMatrix()

def draw():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    spaceship_draw()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Dancing teapots")
init_projection_plus_camera()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
