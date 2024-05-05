#declaracion de variables
import numpy as np
#import random
#tablero =   [['-','-','-','-'],
#            ['-','-','-','-'],
#            ['-','-','-','-'],
#            ['-','-','-','-']]

ganador=False
salida =False

#funciones
def fn_tableros(tmn): #Que tablero queremos ahora?
    global tablero
    global ganador
    if tmn == 3:
      tablero = np.full((3, 3), '-')
    elif tmn == 4:
      tablero = np.full((4, 4), '-')
    else:
      print('')
      print(f"Por que elegiste como opción {tmn}" + " animalongo")
      print('')
      ganador = "No hubo"
      tablero = []

    return ganador

def fn_imprimir(tablero,tmn): #Que tablero tan lindoo!
  print(" ")
  if tmn == 3:
      print('      1   2   3')
      print('    -------------')
      print('1  ','|',tablero[0][0],'|',tablero[0][1],'|',tablero[0][2],'|')
      print('    -------------')
      print('2  ','|',tablero[1][0],'|',tablero[1][1],'|',tablero[1][2],'|')
      print('    -------------')
      print('3  ','|',tablero[2][0],'|',tablero[2][1],'|',tablero[2][2],'|')
      print('    -------------')

  if tmn == 4:
      print('      1   2   3   4')
      print('    -----------------')
      print('1  ','|',tablero[0][0],'|',tablero[0][1],'|',tablero[0][2],'|',tablero[0][3],'|')
      print('    -----------------')
      print('2  ','|',tablero[1][0],'|',tablero[1][1],'|',tablero[1][2],'|',tablero[1][3],'|')
      print('    -----------------')
      print('3  ','|',tablero[2][0],'|',tablero[2][1],'|',tablero[2][2],'|',tablero[2][3],'|')
      print('    -----------------')
      print('4  ','|',tablero[3][0],'|',tablero[3][1],'|',tablero[3][2],'|',tablero[3][3],'|')
      print('    -----------------')

def fn_Nombres(): #Quien va a participar en los juegos Olim...en el juego de Triki?
    Nx = input("El nombre del jugador 'X' es: ")
    No = input("El nombre del jugador 'O' es: ")
    print(" ")

    return Nx,No

def fn_datosUsuario(): #Que vas colocar en cada casilla?
  print(" ")
  num_f=int(input("Ingrese el valor de la fila: "))-1
  num_c=int(input("Ingrese el valor de la columna: "))-1
  return num_f,num_c,

def jb_dePartida(jgdr): #turnos de los jugadores
    if jgdr == 'X':
      jgdr='O'
    else:
      if jgdr == 'O':
        jgdr='X'
    return jgdr

def fn_ponerFicha(tablero,jgdr): #Posición de las fichas en la partida
    casillas = False

    while casillas == False: #'while' para permitir ó bloquear casillas
        NUM_F,NUM_C = fn_datosUsuario()
        if tablero[NUM_F][NUM_C] == '-':
            casillas = True
        else:
            print(" ")
            print("Elije otra casilla")

    tablero[NUM_F][NUM_C]=jgdr


def jb_comosegana(tablero,Nx,No,tmn,jgdr): #Como se gano la partida?!
    global ganador
    ganaFila(tablero,Nx,No,tmn,jgdr)
    ganaColumna(tablero,Nx,No,tmn,jgdr)
    ganaDiagonal(tablero,Nx,No,tmn,jgdr)
    empate(tablero)
    return ganador

def jb_quienGano(Nx,No): #Pero quien gano?!!
    global ganador
    if ganador == "No hubo":
      return ganador
    else:
      if jgdr == 'O': #El codigo apesar de que ya haya un ganador, el sigue cambiando el turno...
          ganador = Nx #a ultima hora.
      elif jgdr == 'X':
          ganador = No

    return ganador

def ganaFila(tablero,Nx,No,tmn,jgdr): #Ganador en fila
    global ganador
    for fl in range(tmn):
      cont=0
      for cl in range(tmn):
        if tablero[fl][cl]==jgdr:
          cont+=1

      if cont==tmn:
          if jgdr=='X':
              print(" ")
              print(Nx,"gano por fila",fl+1,"!!!!! ")
              ganador=True
          elif jgdr=='O':
              print(" ")
              print(No,"gano por fila",fl+1,"!!!!! ")
              ganador=True

    return ganador

def ganaColumna(tablero,Nx,No,tmn,jgdr): #Ganador en columna
  global ganador
  for cl in range(tmn):
    cont=0
    for fl in range(tmn):
      if tablero[fl][cl]==jgdr:
        cont+=1

        if cont==tmn:
            if jgdr=='X':
                print(" ")
                print(Nx,"gano por columna",cl+1,"!!!!! ")
                ganador=True
            elif jgdr=='O':
                print(" ")
                print(No,"gano por columna",cl+1,"!!!!! ")
                ganador=True

  return ganador

def ganaDiagonal(tablero, Nx, No, tmn, jgdr): #Ganador en diagonal
    global ganador
    dgnal_1 = all(tablero[i][i] == jgdr for i in range(tmn))
    dgnal_2 = all(tablero[i][tmn-i-1] == jgdr for i in range(tmn))

    if dgnal_1 or dgnal_2:
        print("")
        if jgdr == 'X':
            print(Nx, "gano por diagonal !!!!!")
        else:
            print(No, "gano por diagonal !!!!!")
        ganador = True

    return ganador

def empate(tablero): #Acaso no quieren ganar?
    global ganador
    vacias = np.count_nonzero(tablero == '-')
    if ganador:
        return False  # Si hay un ganador, no hay empate
    elif vacias == 0:
        ganador = "No hubo"
        print("Celdas vacías: ", vacias)
        return True  # Si no hay ganador pero no hay casillas vacías, hay un empate
    else:
        return False  # Si aún hay casillas vacías y no hay ganador, no hay empate

def granganador(ganador): #El gran ganador fue
  if ganador == "No hubo":
    print("No puedo creer que hubo un empate, ¿Eso es posible?")
  else:
    print("El gran ganador de esta partida es el jugador " + ganador + "!!!")

def seguimosJugando(): #Por que querian dejar de jugar?
  global salida
  rspt = int(input("¿Otra partida? 1(Si) 2(No) "))
  match rspt:
    case 1:
      print(" ")
      print("Nada mejor que una revancha!!")
      
      salida = False
    
    case 2:
      print(" ")
      print("Gracias por participar!!")
      
      salida = True

# llamados-PROGRAMA PRINCIPAL

NX,NO = fn_Nombres()

while not salida:
  ganador = False
  jgdr='X'
  
  print("BIENVENIDOS AL JUEGO TRIKIENLINEA")
  print(" ")
  tmn=int(input("Ingrese el tamaño de su tablero 3(3X3) 0 4(4x4): "))
  
  fn_tableros(tmn)

  while ganador==False:
    fn_imprimir(tablero,tmn)
    
    print(" ")
    print("Turno del jugador " + jgdr)
    
    fn_ponerFicha(tablero,jgdr)
    jb_comosegana(tablero,NX,NO,tmn,jgdr)
    
    jgdr = jb_dePartida(jgdr)
    
  jb_quienGano(NX,NO)
  fn_imprimir(tablero,tmn)
  print(" ")
  granganador(ganador)
 
  print(" ")
  seguimosJugando()
print(" ")
