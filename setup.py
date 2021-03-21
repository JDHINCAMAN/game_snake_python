import cx_Freeze

executables = [cx_Freeze.Executable("mision.py",
                                    base = "Win32GUI")]

build_exe_options = {"packages": ["pygame"],
                     "include_files":["Pixelmania.ttf",
                                      "fondo juego.jpg",
                                      "serp.png", "pausa.jpg", "inicio.jpg", "sonido juego.ogg", "manzana roja.ogg", "manzana morada.ogg", "manzana verde.ogg"]}


cx_Freeze.setup(
    name = "Juego serpiente 2.0",
    version = "2.0",
    description = "Este es mi primer juego",
    options = {"build_exe": build_exe_options},
    executables = executables
    )
