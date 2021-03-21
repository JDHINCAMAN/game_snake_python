import pygame
import time
import os, pygame
import random

def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert()

pygame.init()

icono = pygame.image.load("serp.png")
pygame.display.set_icon(icono)


Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Azul = (0, 0, 255)
Verde = (0, 255, 0)
Morado = (255, 0, 255)

ancho = 1280
altura = 720


superficie = pygame.display.set_mode((ancho,altura))
pygame.display.set_caption('Juego serpiente 2.0')


background = load_image('fondo juego.jpg')

superficie.blit(background, [0, 0])


reloj = pygame.time.Clock()

serp_tamano = 20
CPS = 15

font = pygame.font.SysFont("Pixelmania.ttf", 35)
      

def pausa():
    pausado = True
   
    while pausado:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        background = load_image('pausa.jpg')
        superficie.blit(background, [0, 0])
        #superficie.fill(blanco)      
        pygame.display.update()
        reloj.tick(5)


def puntos(score):
    text = font.render("PUNTOS: "+str(score), True, Blanco)
    superficie.blit(text, [0,0])

def rapidez(run):
    text = font.render("RAPIDEZ: "+str(run), True, Negro)
    superficie.blit(text, [150,0])

def intro_juego():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        background = load_image('inicio.jpg')
        superficie.blit(background, [0, 0])
        pygame.display.update()
        reloj.tick(15)

def serpiente(serp_tamano, listaSerpiente):
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Negro, [i[0],i[1],serp_tamano,serp_tamano])

def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()
def message_to_screen(msg, color, y_displace=0):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (ancho/2), (altura/2)+ y_displace
    superficie.blit(textSur, textRect)
    #pantalla_texto = font.render(msg, True, color)
    #superficie.blit(pantalla_texto,[display_ancho/2, display_altura/2])

    
    
def gameLoop():
    gameExit = False
    gameOver = False

    mover_x = 300
    mover_y = 300

    mover_x_cambio = 0
    mover_y_cambio = 0

    listaSerpiente = []
    largoSerpiente = 1

    MAS = reloj.tick(0)

    azarManzanaX = round(random.randrange(0, 1280 - 20)/20.0)*20.0
    azarManzanaY = round(random.randrange(0, 720 - 20)/20.0)*20.0
    azarManzanaMoradoX = round(random.randrange(0, 1280 - 20)/20.0)*20.0
    azarManzanaMoradoY = round(random.randrange(0, 720 - 20)/20.0)*20.0
    azarManzanaVerdeX = round(random.randrange(0, 1280 - 20)/20.0)*20.0
    azarManzanaVerdeY = round(random.randrange(0, 720 - 20)/20.0)*20.0

    pulsar_sonido = pygame.mixer.Sound("sonido juego.ogg")
    pulsar_sonido.set_volume(0.50)
    pulsar_sonido.play(18)
    

    
    while not gameExit:

        while gameOver == True:


      
            ##superficie.fill(blanco)
            superficie.blit(background, [0, 0])
            pulsar_sonido.stop()
            message_to_screen("GAME OVER", Blanco, -50)
            message_to_screen("PARA CONTINUAR PRESIONE C. PARA TERMINAR PRESIONE Q", Blanco, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    


    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mover_x_cambio = -serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    mover_x_cambio = serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_UP:
                    mover_y_cambio = -serp_tamano
                    mover_x_cambio = 0
                elif event.key == pygame.K_DOWN:
                    mover_y_cambio = serp_tamano
                    mover_x_cambio = 0   
                elif event.key == pygame.K_p:
                    pulsar_sonido.set_volume(0.0)
                    pausa()
                    pulsar_sonido.set_volume(0.50)


                     
                
        if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
            gameOver = True


        mover_x += mover_x_cambio
        mover_y += mover_y_cambio
        ##superficie.fill(blanco)
        superficie.blit(background, [0, 0])

        pygame.draw.rect(superficie, Rojo, [azarManzanaX, azarManzanaY, 20, 20])
        pygame.draw.rect(superficie, Morado, [azarManzanaMoradoX, azarManzanaMoradoY, 20, 20])
        pygame.draw.rect(superficie, Verde, [azarManzanaVerdeX, azarManzanaVerdeY, 20, 20])

        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        listaSerpiente.append(cabezaSerpiente)
        if len(listaSerpiente) > largoSerpiente:
            del listaSerpiente[0]

        for eachSegment in listaSerpiente[:-1]:
            if eachSegment == cabezaSerpiente:
                gameOver = True


        serpiente(serp_tamano,listaSerpiente)
        puntos(largoSerpiente-1)
        rapidez(MAS-1)
        pygame.display.update()

        

        if mover_x == azarManzanaX and mover_y == azarManzanaY: 
            pygame.mixer.music.load("manzana roja.ogg")
            azarManzanaX = round(random.randrange(0, 1280-20)/20.0)*20.0
            azarManzanaY = round(random.randrange(0, 720-20)/20.0)*20.0
            largoSerpiente += 1
            pygame.mixer.music.play(0)

        if mover_x == azarManzanaMoradoX and mover_y == azarManzanaMoradoY: 
            pygame.mixer.music.load("manzana morada.ogg")
            azarManzanaMoradoX = round(random.randrange(0, 1280-20)/20.0)*20.0
            azarManzanaMoradoY = round(random.randrange(0, 720-20)/20.0)*20.0
            largoSerpiente += 10
            pygame.mixer.music.play(0)

        if mover_x == azarManzanaVerdeX and mover_y == azarManzanaVerdeY: 
            pygame.mixer.music.load("manzana verde.ogg")
            MAS += 1
            azarManzanaVerdeX = round(random.randrange(0, 1280-20)/20.0)*20.0
            azarManzanaVerdeY = round(random.randrange(0, 720-20)/20.0)*20.0
            pygame.mixer.music.play(0)
            
   
        reloj.tick(CPS)


    pygame.quit()
    quit()

intro_juego()
gameLoop()
