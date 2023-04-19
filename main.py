from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants1 import *
from math import *
from random import *
import pygame

step = .5
asteroid_angle = [0, 0, 0]
# asteroid_position_z = -100
spaceship_position = 0
number_asteroid = 0
positions_x_of_asteroids = []
positions_z_of_asteroids = []
RIGHT = False
LEFT = False

TEXTURE_NAMES = [0]
def keyboard_callback(key, x, y):
    global spaceship_position
    if key == b"q":
        sys.exit(0)
    if key == GLUT_KEY_LEFT:
        spaceship_position = max(spaceship_position - 20, -20)
    elif key == GLUT_KEY_RIGHT:
        spaceship_position = min(spaceship_position + 20, 20)

def init_projection_ortho():
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1000, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1200 / 800, .5, 1000)
    glMatrixMode(GL_MODELVIEW)


def reposition_camera():
    gluLookAt(0, 20, 35,
              0, 0, -100,
              0, 1, 0)

def init_textures():
    loadTextures()


def texture_setup(texture_image_binary, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
                    GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D,
                 0,
                 3,
                 width, height,
                 0,
                 GL_RGBA,
                 GL_UNSIGNED_BYTE,
                 texture_image_binary)


def loadTextures():
    glEnable(GL_TEXTURE_2D)
    images = [pygame.image.load("pexels-hristo-fidanov-1252890.jpg")]
    textures = [pygame.image.tostring(image, "RGBA", True)
                for image in images]

    glGenTextures(len(images), TEXTURE_NAMES)

    for i in range(len(images)):
        texture_setup(textures[i],
                      TEXTURE_NAMES[i],
                      images[i].get_width(),
                      images[i].get_height())


def background_draw():
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1)
    glVertex(-1, 1)

    glTexCoord2f(0, 0)
    glVertex(-1, -1)

    glTexCoord2f(1, 0)
    glVertex(1, -1)

    glTexCoord2f(1, 1)
    glVertex(1, 1)
    glEnd()

def spaceship_draw():
    global spaceship_position
    glPushMatrix()
    glColor3d(0, 0, 1)
    glTranslate(spaceship_position, 0, 0)
    glRotate(-180, 0, 1, 0)
    glScale(.12, .12, .12)
    glBegin(GL_LINES)
    for edge in spaceship_edges_vector2:
        for vertex in edge:
            glVertex3fv(spaceship_verticies_vector3[vertex])
    glEnd()
    glPopMatrix()


def asteroid_draw(position_x, position_z):
    global asteroid_angle
    rand_direction = choice(["x", "y", "z"])
    glColor3d(0.502, 0.502, 0.502)
    glPushMatrix()
    glTranslate(position_x, 0, position_z)
    glScale(.01, .01, .01)
    glRotate(asteroid_angle[0], 1, 0, 0)
    glRotate(asteroid_angle[1], 0, 1, 0)
    glRotate(asteroid_angle[2], 0, 0, 1)
    if rand_direction == "x":
        asteroid_angle[0] += .5
    elif rand_direction == "y":
        asteroid_angle[1] += .5
    else:
        asteroid_angle[2] += .5
    # glBegin(GL_QUADS)
    # for face in asteroid_faces_vector4:
    #     for vertex in face:
    #         glColor3fv(asteroid_color)
    #         glVertex3fv(asteroid_verticies_vector3[vertex])
    # glEnd()
    glBegin(GL_LINES)
    for edge in asteroid_edges_vector2:
        for vertex in edge:
            glVertex3fv(asteroid_verticies_vector3[vertex])
    glEnd()
    glPopMatrix()
    # position_z += step


def draw():
    global LEFT, RIGHT, number_asteroid
    rand_number = randrange(361)
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glColor(1, 1, 1)
    init_projection_ortho()
    glBindTexture(GL_TEXTURE_2D, TEXTURE_NAMES[0])
    background_draw()
    glBindTexture(GL_TEXTURE_2D, -1)
    init_projection()
    reposition_camera()
    spaceship_draw()
    if rand_number == 360:
        position = choice([-20, 0, 20])
        asteroid_draw(position, -100)
        positions_x_of_asteroids.append(position)
        positions_z_of_asteroids.append(-100)
        number_asteroid += 1
    for i in range(number_asteroid):
        if positions_z_of_asteroids[i] < -5:
            asteroid_draw(positions_x_of_asteroids[i], positions_z_of_asteroids[i])
        positions_z_of_asteroids[i] += step
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGBA)
glutInitWindowSize(1200, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Dancing teapots")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(keyboard_callback)
init_textures()
init_projection()
glutMainLoop()