from mmap import MAP_ANON
from random import Random
from raylib import *
from fourmi import *


WINDOW_SIZE = (900, 900)
NB_FOURMIS = 100
MATRIX_COLOR = [[[255, 255, 255]] * WINDOW_SIZE[0] for _ in range(WINDOW_SIZE[1])]
MULTIPLICATOR = 10

InitWindow(WINDOW_SIZE[0], WINDOW_SIZE[0], b"les fourmis...")

render = LoadRenderTexture(WINDOW_SIZE[0], WINDOW_SIZE[0])

SetTargetFPS(15)

# 1000 fourmis avec des positions aléatoires
fourmis = []
rand = Random()
for i in range(NB_FOURMIS):
    fourmis.append(Fourmi((rand.randint(0, WINDOW_SIZE[0]), rand.randint(0,WINDOW_SIZE[1])), Direction(rand.randint(0, 7))))

def observer_couleurs_environnantes(position):
        # Déterminer la position de la fourmi sur la toile
        x, y = int(position[0]), int(position[1])

        # Récupérer les couleurs des pixels environnants (8 pixels autour de la fourmi)
        couleurs_environnantes = [
            MATRIX_COLOR.get_pixel_color(WINDOW_SIZE[0] if x == 0 else x - 1, WINDOW_SIZE[0] if y == 0 else y - 1),  # en haut à gauche
            MATRIX_COLOR.get_pixel_color(x, WINDOW_SIZE[1] if y == 0 else y - 1),      # en haut
            MATRIX_COLOR.get_pixel_color(0 if x==WINDOW_SIZE[0] else x + 1, WINDOW_SIZE[0] if y == 0 else y - 1),  # en haut à droite
            MATRIX_COLOR.get_pixel_color(WINDOW_SIZE[0] if x == 0 else x - 1, y),      # à gauche
            MATRIX_COLOR.get_pixel_color(0 if x==WINDOW_SIZE[0] else x + 1, y),      # à droite
            MATRIX_COLOR.get_pixel_color(WINDOW_SIZE[0] if x == 0 else x - 1,0 if y==WINDOW_SIZE[0] else y + 1),  # en bas à gauche
            MATRIX_COLOR.get_pixel_color(x,0 if y==WINDOW_SIZE[0] else y + 1,),      # en bas
            MATRIX_COLOR.get_pixel_color(0 if x==WINDOW_SIZE[0] else x + 1,0 if y==WINDOW_SIZE[0] else y + 1,)   # en bas à droite
        ]

        return couleurs_environnantes


while(not WindowShouldClose()):

    BeginDrawing()
    ClearBackground(RAYWHITE)

    BeginTextureMode(render)
    for fourmi in fourmis:
        couleurs_env = observer_couleurs_environnantes(fourmi.position)
        fourmi.move(couleurs_env)
        DrawPixel(fourmi.position[0],fourmi.position[1],1,fourmi.couleur)
    EndTextureMode()

    DrawTexturePro(render.texture, (0, 0, render.texture.width, -render.texture.height), (0, 0, GetScreenWidth(), GetScreenHeight()), (0, 0), 0, WHITE)  # Draw the render texture on the screen with stretching
    EndDrawing()

UnloadRenderTexture(render)
CloseWindow()


