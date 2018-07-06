import pygame
import graphics
import jugador
import tablero
from variables import azul, blanco
pygame.mixer.init(44100, -16,2,2048)
pygame.mixer.music.load('kirby.ogg')

pygame.mixer.music.play(-1)

pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'GO!'
        if e.type == pygame.QUIT: break
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        continue
    break





class Juego:

    def __init__(self):
        self.graphics = graphics.Graphics()
        self.tablero = tablero.Tablero()
        self.opciones()

    def opciones(self):
        jugador1, jugador2, nivel = self.graphics.mostraropciones()
        if jugador1 == "humano":
            self.jugadoractual = jugador.Humano(self.graphics, azul)
        else:
            self.jugadoractual = jugador.Computadora(azul, nivel + 3)
        if jugador2 == "humano":
            self.otrojugador = jugador.Humano(self.graphics, blanco)
        else:
            self.otrojugador = jugador.Computadora(blanco, nivel + 3)

        self.graphics.mostrarjuego()
        self.graphics.update(self.tablero.tablero, 2, 2)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if self.tablero.juegotermino():
                blancos, azules, vacios = self.tablero.contarpiezas()
                if blancos > azules:
                    ganador = blanco
                elif azules > blancos:
                    ganador = azul
                else:
                    ganador = None
                break
            self.jugadoractual.obtenertableroactual(self.tablero)
            if self.tablero.movimientovalido(self.jugadoractual.color) != []:
                puntuacion, self.tablero = self.jugadoractual.obtenermovida()
                blancos, azules, vacios = self.tablero.contarpiezas()
                self.graphics.update(self.tablero.tablero, azules, blancos)
            self.jugadoractual, self.otrojugador = self.otrojugador, self.jugadoractual
        self.graphics.mostrarganador(ganador)
        pygame.time.wait(1000)
        self.restart()

    def restart(self):
        self.tablero = tablero.Tablero()
        self.opciones()
        self.run()


def main():
    game = Juego()
    game.run()


if __name__ == '__main__':
    main()


import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, RLEACCEL

class Make_Countdown(pygame.sprite.DirtySprite):
    """
    xpos and ypos are the coords where the text will be centeres and printed. By defaault they are screen_centerx and screen_centery. If you leave posx = None and posy = None these values will be used. If you enter any values, those will be used.
    Font size need to be supplied along with the colour of text, lownum and hinum.
    Countdown = True by default. hinum -> lownum
    Countdown = False lownum -> hinum
    if a font is not supplied (path), the default pygame font will be used.
    Fading out is set by default.
    Time will hold each number on screen for that duration If fade is set that time will be used to fade out."""

    def __init__(self, posx = None, posy = None, colour = (255, 50, 64), number = 5, font = None, fontsize = 200, fade_speed = 20, countdown = True, fadeout = True):

        pygame.sprite.DirtySprite.__init__(self)

        self.screen = pygame.display.get_surface()

        if self.screen == None:
            print("none")
            self.screen =pygame.display.set_mode((300, 300), 1, 32)

        self.subsurface = self.screen.subsurface(0, 0, self.screen.get_width(), self.screen.get_height()).convert_alpha()
        self.back = self.screen
        self.background = (0, 0, 0)
        self.alpha = 255
        if posx == None:
            self.posx = self.screen.get_width() / 2
        else:
            self.posx = posx
        if posy == None:
            self.posy = self.screen.get_height() / 2
        else:
            self.posy = posy
        self.fontsize = fontsize
        self.colour = colour
        self.lownum = 1
        self.hinum = number
        self.font = font
        self.count_down = countdown
        self.fade = fadeout
        self.fade_speed = fade_speed
        self.imagelist = []

        self.renderedfont = pygame.font.Font(self.font, self.fontsize)

        for x in xrange(self.lownum, self.hinum + 1):  # we want to count hinum as well so + 1

            matext = self.renderedfont.render(str(x), True, self.colour, (0, 0, 0)).convert()

            matext.set_colorkey(0, RLEACCEL)

            matext.set_alpha(255)

            self.imagelist.append(matext)



    def run(self, variable):

        direction = variable

        if direction == "down":

            self.imagelist = reversed(self.imagelist)

        for image in self.imagelist:

            self.alpha = 255
            # the calculation below makes the sprite be printed by its center coord
            posx = self.posx - (image.get_width() / 2)
            posy = self.posy - (image.get_height() / 2)
            self.subsurface = self.screen.subsurface(posx, posy, image.get_width(), image.get_height()).convert_alpha()
            for x in xrange(50):

                self.alpha -= 5
                image.set_alpha(self.alpha)

                self.screen.blit(image, (posx, posy))

                pygame.display.update()
                pygame.time.wait(self.fade_speed)  # how long to pause
                self.screen.blit(self.subsurface, (posx, posy))

            for e in pygame.event.get():
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit



if __name__ == '__main__':
    pygame.init()
    counter = Make_Countdown()
    #counter.run("up")
    counter.run("down")
