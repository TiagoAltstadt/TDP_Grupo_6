import os # Esta libreria me permite hacer el clear screen

# Global Variables
consoleLength = 80
breakLine = '\n'

def main():
    welcomeMessageFunction()

def mainMenu():
    os.system('cls') # Clears console   
    lineSeparator(consoleLength) # Roof of the box

    customPrint('Seleccione una opcion del menu:')
    customPrint(' 1) Gestionar Alumnos')
    customPrint(' 2) Gestionar Materias')

    lineSeparator(consoleLength) # Roof of the box
    selectedValue = input()

    if selectedValue == '1':
        studentMenu()
    elif selectedValue == '2':
        subjectMenu()
    else: # por default reinicia la funcion
        mainMenu()
    
def studentMenu():
    os.system('cls') # Clears console   
    lineSeparator(consoleLength) # Roof of the box

    customPrint(' Menu de alumno')
    customPrint('  1) Agregar Alumno')
    customPrint('  2) Modificar Alumno')
    customPrint('  3) Eliminar Alumno')
    customPrint('  4) <- Menu Principal')

    lineSeparator(consoleLength) # Roof of the box
    selectedValue = input('Seleccion: ')

    if selectedValue == '1':
        print('Agregar alumno')
    elif selectedValue == '2':
        print('Modificar alumno')
    elif selectedValue == '3':
        print('Eliminar alumno')
    elif selectedValue == '4':
        mainMenu()
    else: # por default reinicia la funcion
        studentMenu()


def subjectMenu():
    os.system('cls') # Clears console   
    lineSeparator(consoleLength) # Roof of the box

    customPrint(' Menu de materia')
    customPrint('  1) Agregar materia')
    customPrint('  2) Modificar materia')
    customPrint('  3) Eliminar materia')
    customPrint('  4) <- Menu Principal')

    lineSeparator(consoleLength) # Roof of the box
    selectedValue = input('Seleccion: ')

    if selectedValue == '1':
        print('Agregar materia')
    elif selectedValue == '2':
        print('Modificar materia')
    elif selectedValue == '3':
        print('Eliminar materia')
    elif selectedValue == '4':
        mainMenu()
    else: # por default reinicia la funcion
        subjectMenu()

def welcomeMessageFunction():
    os.system('cls') # Clears console   
    lineSeparator(consoleLength) # Roof of the box

    customPrint('Bienvenido al Trabajo practico de Tecnicas de Programacion')
    customPrint('Programadores: ')
    customPrint('- Maria Navares')
    customPrint('- Martin Borzi')
    customPrint('- Tiago Altstadt')

    lineSeparator(consoleLength) # Floor of the box
    input(' Apreta cualquier tecla para continuar...')
    mainMenu()


def lineSeparator(number): # Esta funcion toma un numero cualquera, y genera un string con el caracter seleccionado, en este caso es consoleLength que esta definido en las variables globales
    ret = ''
    for _ in range(number):
        ret = ret + '-'
    print('  '+ret)

def customPrint(string): # Esta funcion toma un string, al largo total definido de la consola le resta el largo del string para poder calcular donde agregar las paredes iniciales y finales
    spaces = ''
    for _ in range(consoleLength - len(string)):
        spaces = spaces + ' '
    
    print('| ' + string  + spaces +'|')

main() # Funcion principal donde se ejecuta todo