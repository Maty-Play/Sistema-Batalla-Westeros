import os, random as rd
os.system("cls")

BONO_STARK = 2
BONO_LANNISTER = -3
BONO_TARGARYEN = 5
BONO_BARATHEON = 0
PODER_MIN = 1
PODER_MAX = 20

try:
    print("BIENVENIDO JUGADOR :D")
    
    print("---------------------")
    print("CASAS EXISTENTES")
    print("1. Stark ")
    print("2. Lannister ")
    print("3. Targaryen")
    print("4. Baratheon ")
    print("---------------------")
    
    nombre_jugador = input("Ingrese su Nombre: ").title()
    edad = int(input("Ingrese su Edad: "))
    casa = input("Ingrese la casa a la que pertenece (S,L,T,B): ").lower()
    
    if edad > 0 and casa == "s" or casa == "l" or casa == "t" or casa == "b":
        poder_base = rd.randint(PODER_MIN,PODER_MAX)
        
        if casa == "s":
            casa_str = "Stark"
            poder_final = BONO_STARK + poder_base
        elif casa == "l":
            casa_str = "Lannister"
            poder_final = BONO_LANNISTER + poder_base
        elif casa == "t":
            casa_str = "Targaryen"
            poder_final = BONO_TARGARYEN + poder_base
        else:
            casa_str = "Baratheon"
            poder_final = BONO_BARATHEON + poder_base
        
        if poder_final >= 20:
            resultado = "Victoria Epica"
        elif poder_final >= 10 and poder_final < 20:
            resultado = "Victoria Ajustada"
        else:
            resultado = "Derrota Aplastante :("
        
        print("---------------------")
        print(f"Nombre: {nombre_jugador}")
        print(f"Edad: {edad}")
        print(f"Casa: {casa_str}")
        print(f"Poder Base: {poder_base}")
        print(f"Poder Final: {poder_final}")
        print(f"Resultado Batalla: {resultado}")
        
    else:
        print("Alguno de sus datos es incorrecto")
except:
    print("Deben ser variables numericas")