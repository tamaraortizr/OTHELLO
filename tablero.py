import pygame, sys, time, os
from pygame.locals import *
import time
from variables import azul, blanco, dificultad, humano, computadora

class Graphics:

    def __init__(self):
        pygame.init()

        self.negro = (0, 0, 0)
        self.fondo = (143, 188, 143)
        self.blanco = (255, 255, 255)
        self.azul = (0, 0, 128)
        self.moradooscuro = (72, 61, 139)

        self.screensize = (640, 480)
        self.posiciontablero = (100, 20)
        self.TABLERO = (120, 40)
        self.tablerotamano = 400
        self.espaciotamano = 50
        self.screen = pygame.display.set_mode(self.screensize)

        self.azulpalabrapos = (5, self.screensize[1] / 4)
        self.blancopalabrapos = (560, self.screensize[1] / 4)
        self.font = pygame.font.Font("LemonMilklight.otf", 22)
        self.puntuacionfont = pygame.font.Font("LemonMilk.otf", 50)

        self.tableroimg = pygame.image.load('tablero.png')
        self.azulimg = pygame.image.load('ficha azul.png')
        self.blancoimg = pygame.image.load('ficha blanca.png')
        self.tipimg = pygame.image.load('ficha tips.png')
        self.vacioimg = pygame.image.load('vacio.png')
        self.animacion1img = pygame.image.load('animacion 1.png')
        self.animacion2img = pygame.image.load('animacion 2.png')

    def mostraropciones(self):
        jugador1 = humano
        jugador2 = computadora
        nivel = dificultad

        while True:
            self.screen.fill(self.fondo)
            titulofont = pygame.font.Font("Candle Mustard.ttf", 80)
            titulo = titulofont.render("Othello", True, self.blanco)
            tituloposicion = titulo.get_rect(centerx=self.screen.get_width() / 2, centery=100)

            comenzartexto= self.font.render("Comenzar", True, self.blanco)
            comenzarposicion = comenzartexto.get_rect(centerx=self.screen.get_width() / 2, centery=220)
            jugador1texto = self.font.render("Primer jugador ", True, self.blanco)
            jugador1pos = jugador1texto.get_rect(centerx=self.screen.get_width() / 2, centery=260)
            jugador2texto = self.font.render("Segundo jugador ", True, self.blanco)
            jugador2pos = jugador2texto.get_rect(centerx=self.screen.get_width() / 2, centery=300)
            niveltexto = self.font.render("Nivel de computadora ", True, self.blanco)
            nivelpos = niveltexto.get_rect(centerx=self.screen.get_width() / 2, centery=340)

            self.screen.blit(titulo, tituloposicion)
            self.screen.blit(comenzartexto, comenzarposicion)
            self.screen.blit(jugador1texto, jugador1pos)
            self.screen.blit(jugador2texto, jugador2pos)
            self.screen.blit(niveltexto, nivelpos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if comenzarposicion.collidepoint(mouse_x, mouse_y):
                        return jugador1, jugador2, nivel
                    elif jugador1pos.collidepoint(mouse_x, mouse_y):
                        jugador2 = self.elegirjugador()
                    elif jugador2pos.collidepoint(mouse_x, mouse_y):
                        jugador2 = self.elegirjugador()
                    elif nivelpos.collidepoint(mouse_x, mouse_y):
                        nivelpos = self.elegirnivel()

            pygame.display.flip()

    def mostrarganador(self, colorjugador):
        self.screen.fill(pygame.Color(self.fondo))
        font = pygame.font.SysFont("Courier-Bold", 34)
        if colorjugador == blanco:
            msg = font.render("Blanco ganó", True, self.blanco)
        elif colorjugador == azul:
            msg = font.render("Azul ganó", True, self.blanco)
        else:
            msg = font.render("Empate", True, self.blanco)
        self.screen.blit(msg, msg.get_rect(centerx=self.screen.get_width() / 2, centery=120))
        pygame.display.flip()

    def elegirjugador(self):
        while True:
            self.screen.fill(self.fondo)
            titulofont = pygame.font.Font("Candle Mustard.ttf", 80)
            titulo = titulofont.render("Othello", True, self.moradooscuro)
            tituloposicion = titulo.get_rect(centerx=self.screen.get_width() / 2,centery=100)
            humanotexto = self.font.render("Humano", True, self.blanco)
            humanopos = humanotexto.get_rect(centerx=self.screen.get_width() / 2, centery=180)
            computadoratexto = self.font.render("Computer", True, self.blanco)
            computadorapos = computadoratexto.get_rect(centerx=self.screen.get_width() / 2,centery=360)

            self.screen.blit(titulo, tituloposicion)
            self.screen.blit(humanotexto, humanopos)
            self.screen.blit(computadoratexto, computadorapos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if humanopos.collidepoint(mouse_x, mouse_y):
                        return humano
                    elif computadorapos.collidepoint(mouse_x, mouse_y):
                        return computadora
            pygame.display.flip()

    def elegirnivel(self):
        while True:
            self.screen.fill(self.fondo)
            titulofont = pygame.font.Font("Candle Mustard.ttf", 80)
            titulo = titulofont.render("Othello", True, self.moradooscuro)
            tituloposicion = titulo.get_rect(centerx=self.screen.get_width() / 2,centery=100)
            unotexto = self.font.render("Nivel 1", True, self.blanco)
            unopos = unotexto.get_rect(centerx=self.screen.get_width() / 2,centery=180)
            dostexto = self.font.render("Nivel 2", True, self.blanco)
            dospos = dostexto.get_rect(centerx=self.screen.get_width() / 2,centery=240)
            trestexto = self.font.render("Nivel 3", True, self.blanco)
            trespos = trestexto.get_rect(centerx=self.screen.get_width() / 2,centery=300)

            self.screen.blit(titulo, tituloposicion)
            self.screen.blit(unotexto, unopos)
            self.screen.blit(dostexto, dospos)
            self.screen.blit(trestexto, trespos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if unopos.collidepoint(mouse_x, mouse_y):
                        return 1
                    elif dospos.collidepoint(mouse_x, mouse_y):
                        return 2
                    elif trespos.collidepoint(mouse_x, mouse_y):
                        return 3

            pygame.display.flip()
            time.sleep(.05)

    def mostrarjuego(self):
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill(self.fondo)
        self.puntajetamano = 50
        self.puntaje1 = pygame.Surface((self.puntajetamano, self.puntajetamano))
        self.puntaje2 = pygame.Surface((self.puntajetamano, self.puntajetamano))
        self.screen.blit(self.background, (0, 0), self.background.get_rect())
        self.screen.blit(self.tableroimg, self.posiciontablero, self.tableroimg.get_rect())
        self.ponerpieza((3, 3), blanco)
        self.ponerpieza((4, 4), blanco)
        self.ponerpieza((3, 4), azul)
        self.ponerpieza((4, 3), azul)
        pygame.display.flip()

    def ponerpieza(self, pos, color):
        if pos == None:
            return
        pos = (pos[1], pos[0])
        if color == azul:
            img = self.azulimg
        elif color == blanco:
            img = self.blancoimg
        else:
            img = self.tipimg

        x = pos[0] * self.espaciotamano + self.TABLERO[0]
        y = pos[1] * self.espaciotamano + self.TABLERO[1]

        self.screen.blit(img, (x, y), img.get_rect())
        pygame.display.flip()

    def espaciovacio(self, pos):
        pos = (pos[1], pos[0])
        x = pos[0] * self.espaciotamano + self.TABLERO[0]
        y = pos[1] * self.espaciotamano + self.TABLERO[1]
        self.screen.blit(self.vacioimg, (x, y), self.vacioimg.get_rect())
        pygame.display.flip()

    def movimientomouse(self):
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if mouse_x > self.tablerotamano + self.TABLERO[0] or \
                       mouse_x < self.TABLERO[0] or \
                       mouse_y > self.tablerotamano + self.TABLERO[1] or \
                       mouse_y < self.TABLERO[1]:
                        continue

                    posicion = ((mouse_x - self.TABLERO[0]) // self.espaciotamano), \
                               ((mouse_y - self.TABLERO[1]) // self.espaciotamano)
                    posicion = (posicion[1], posicion[0])
                    return posicion
                elif event.type == QUIT:
                    sys.exit(0)
            time.sleep(.05)

    def update(self, tablero, azules, blancos):
        for f in range(8):
            for c in range(8):
                if tablero[f][c] != 0:
                    self.ponerpieza((f, c), tablero[f][c])

        azulesstr = '%02d ' % int(azules)
        blancosstr = '%02d ' % int(blancos)
        self.mostrarpuntaje(azulesstr, blancosstr)
        pygame.display.flip()

    def mostrarpuntaje(self, azulstr, blancostr):
        texto = self.puntuacionfont.render(azulstr, True, self.azul, self.fondo)
        texto2 = self.puntuacionfont.render(blancostr, True, self.blanco, self.fondo)
        self.screen.blit(texto, (self.azulpalabrapos[0], self.azulpalabrapos[1] + 40))
        self.screen.blit(texto2, (self.blancopalabrapos[0], self.blancopalabrapos[1] + 40))

    def quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break

