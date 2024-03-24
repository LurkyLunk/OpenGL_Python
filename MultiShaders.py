from glapp.PyOGLApp import *
from glapp.LoadMesh import *
from glapp.Light import *
from glapp.Material import *
from glapp.Axes import *




class MultiShaders(PyOGLApp):

    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.plane = None
        self.cube = None
        self.light = None
        self.axes = None
        glEnable(GL_CULL_FACE)

    def initialise(self):
        mat = Material("shaders/texturedvert.vs", "shaders/texturedfrag.vs")
        axesmat = Material("shaders/vertexcolvert.vs", "shaders/vertexcolfrag.vs")

        self.axes = Axes(pygame.Vector3(0, 0, 0), axesmat)
        self.plane = LoadMesh("models/plane.obj", "images/window.png",
                              location=pygame.Vector3(0, 0, 0),
                              material=mat)
        self.cube = LoadMesh("models/cube.obj", "images/crate.png",
                              location=pygame.Vector3(0, -1, 0),
                              material=mat)
        self.light = Light(pygame.Vector3(0, 1, 0), pygame.Vector3(1, 1, 1), 0)
        self.camera = Camera(self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.axes.draw(self.camera, self.light)
        self.cube.draw(self.camera, self.light)
        self.plane.draw(self.camera, self.light)






MultiShaders().mainloop()
