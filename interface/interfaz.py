import Game as g
import chooseOption as co


def interface(numFallo, pokeSpaces):
    print("\n\n===============WHO'S THAT POKÉMON???===============\n")

    print(getAhorcado(numFallo, pokeSpaces)+"\n"+
          "===================================================")

def showGame(intentos, pistas, pokeSpaces, vidas, msj, numFallos, dificultad, pistasDisponibles, lettersUsed):
    print("\n"+msj)
    print(f"\nTurno: {intentos}\t Vidas Restantes: {vidas}")
    if len(pistas) > 0 and len(pistas) < 3:
        print("Pistas => ", end="")
        for i in range(len(pistas)):
            print(f"{pistas[i]}", end="\t")
    print("\n")
    if dificultad != "d":
        print(f"Letras Usadas:", end=" ")
        for letra in lettersUsed:
            print(f"{letra}", end="   ")
    if dificultad == "f":
        interface(numFallos, pokeSpaces)
    elif dificultad == "n":
        interface(numFallos+1, pokeSpaces)
    elif dificultad == "d":
        interface(numFallos + 3, pokeSpaces)

    co.menu.menu(pistasDisponibles)

def getAhorcado(numFallo, pokeSpaces):
    ahorcado = [
        "+-------+\n"
        "|       |\n"
        "|\n"
        "|                         "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|                         "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /                  "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /|                 "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /|\\               "+pokeSpaces+"\n"+
        "|\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /|\\               "+pokeSpaces+"\n"+
        "|      /\n"
        "|\n"
        "=============",
        "+-------+\n"
        "|       |\n"
        "|       O\n"
        "|      /|\\               "+pokeSpaces+"\n"+
        "|      / \\\n"
        "|\n"
        "============="
    ]
    return ahorcado[numFallo]