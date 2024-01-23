import raylib 

def creer_toile(taille):
    raylib.init_window(taille, taille, "Toile Blanche")
    raylib.set_target_fps(60)

def main():
    taille_toile = 400  # Taille initiale de la toile
    creer_toile(taille_toile)

    while not raylib.window_should_close():
        raylib.begin_drawing()
        raylib.clear_background(raylib.RAYWHITE)
        # code que les fourmis doivent faire..
        # code pour colorier la grille raylib.drawpixel
        raylib.end_drawing()

    raylib.close_window()

if __name__ == "__main__":
    main()

