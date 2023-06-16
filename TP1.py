import os # Esta libreria me permite hacer el clear screen

# Global Variables
consoleLength = 80
breakLine = '\n'

def welcomeMessageFunction():
    os.system('cls') # Clears console   
    lineSeparator(consoleLength) # Roof of the box

    customPrintCentered('Bienvenido al Trabajo practico de Tecnicas de Programacion')
    customPrint('')
    customPrint('Programadores: ')
    customPrint('- Maria Navares')
    customPrint('- Martin Borzi')
    customPrint('- Tiago Altstadt')

    lineSeparator(consoleLength) # Floor of the box
    input(' Apreta cualquier tecla para continuar...')
    mainMenu()

def main():
    studentfile=open('student.txt','w')
    studentfile.write('DNI\tNombre\tApellido\tDomicilio\tMateria1\tMateria1-Nota1\tMateria1-nota2\tMateria1-Promedio\tMateria1-Situacion\tMateria2\tMateria2-Nota2\tMateria1-nota2\tMateria2-Promedio\tMateria2-Situacion'+'\n')
    studentfile.close()
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
#    else: # por default reinicia la funcion
    mainMenu()
    
def studentMenu():
    os.system('cls') # Clears console   
    lineSeparator(consoleLength) # Roof of the box

    customPrint(' Menu de alumno')
    customPrint('  1) Agregar Alumno')
    customPrint('  2) Modificar Alumno')
    customPrint('  3) Eliminar Alumno')
    customPrint('  4) Listar Alumnos')
    customPrint('  5) <- Menu Principal')

    lineSeparator(consoleLength) # Roof of the box
    selectedValue = input('Seleccion: ')

    if selectedValue == '1':
        print('Agregar alumno')
        newstudent()
    elif selectedValue == '2':
        print('Modificar alumno')
        modifystudent()
    elif selectedValue == '3':
        print('Eliminar alumno')
    elif selectedValue == '4':
        print('Listar alumnos')
        liststudent()
    elif selectedValue == '5':
        mainMenu()
    else: # por default reinicia la funcion
        studentMenu()

def subjectMenu():
    os.system('cls') # Clears console   
    lineSeparator(consoleLength) # Roof of the box

    customPrint(' Menu de materia')
    customPrint('  1) Agregar materia')
    customPrint('  2) Agregar nota')
    customPrint('  3) Modificar nota')
    customPrint('  4) Listar alumnos')
    customPrint('  5) <- Menu Principal')

    lineSeparator(consoleLength) # Roof of the box
    selectedValue = input('Seleccion: ')

    if selectedValue == '1':
        print('Agregar materia')
        newsubject()
    elif selectedValue == '2':
        print('Agregar nota')
        newnote()
    elif selectedValue == '3':
        print('Modificar nota')
        modifynote()
    elif selectedValue == '4':
        liststudent()
    elif selectedValue == '5':
        mainMenu()  
    else: # por default reinicia la funcion
        subjectMenu()
        
  
#NUEVA MATERIA------------------------------------------------------      
def newsubject(): # definir una nueva materia
    dni=input(' Ingrese el DNI del alumno del que quiere agregar una materia: ')
    studentfile=open('student.txt','r')
    data_list = [] # Initialize an empty list to store the dictionaries1
    for line in studentfile: # Read each individual's information
        values = line.strip().split("\t")  # tab-separated values
        data_list.append(values)     # Append the individual's line to the list
    studentfile.close()
    for index in range(len(data_list)):
        if data_list[index][0]==dni:
            aux=str(input('Seleccione que materia quiere agregar: 1. Materia 1; 2. Materia 2 '))
            if aux=='1':
                data_list[index][4]=input('Ingrese Materia 1: ')
            elif aux=='2':
                data_list[index][9]=input('Ingrese Materia 2: ')
            else:
                print ('La opcion no es valida')
    studentfile=open('student.txt','w')
    studentfile.write('DNI\tNombre\tApellido\tDomicilio\tMateria1\tMateria1-Nota1\tMateria1-nota2\tMateria1-Promedio\tMateria1-Situacion\tMateria2\tMateria2-Nota2\tMateria1-nota2\tMateria2-Promedio\tMateria2-Situacion'+'\n')
    for index in range(1,len(data_list)):
        studentfile.write(str(data_list[index][0])+'\t'+str(data_list[index][1])+'\t'+str(data_list[index][2])+'\t'+str(data_list[index][3])+'\t'+str(data_list[index][4])+'\t'+str(data_list[index][5])+'\t'+str(data_list[index][6])+'\t'+str(data_list[index][7])+'\t'+str(data_list[index][8])+'\t'+str(data_list[index][9])+'\t'+str(data_list[index][10])+'\t'+str(data_list[index][11])+'\t'+str(data_list[index][12])+'\t'+str(data_list[index][13])+'\n')
    studentfile.close()
    subjectMenu()

#NUEVA NOTA------------------------------------------------------
def newnote(): # definir una nueva materia
    dni=input(' Ingrese el DNI del alumno del que quiere agregar una nota: ')
    studentfile=open('student.txt','r')
    data_list = [] # Initialize an empty list to store the dictionaries
    for line in studentfile: # Read each individual's information
        values = line.strip().split("\t")  # tab-separated values
        data_list.append(values)     # Append the individual's line to the list
    studentfile.close()
    for index in range(len(data_list)):
        if data_list[index][0]==dni:
            auxn=int(input('Seleccione que nota quiere agregar: 1. Nota 1 - Materia 1; 2. Nota 2 - Materia 1; 3. Nota 1 - Materia 2; 4. Nota 2 - Materia 2 '))
        if auxn==1:
            data_list[index][5]=input('Ingrese Nota 1 - Materia 1: ')
        elif auxn==2:
            data_list[index][6]=input('Ingrese Nota 2 - Materia 1: ')
        elif auxn==2:
            data_list[index][10]=input('Ingrese Nota 1 - Materia 2: ')
        elif auxn==2:
            data_list[index][11]=input('Ingrese Nota2 - Materia 2: ')
        else:
            print('El alumno no esta registrado')
            
            Promedio=(data_list[index][5] + data_list[index][6])/2
            data_list[index][7]=input(Promedio)
            Promedio2=(data_list[index][10] + data_list[index][11])/2
            data_list[index][12]=input(Promedio2)
            
            # for index in range(len(data_list)):
            #     if data_list[index][7]>= '6':
            #         data_list[index][8]=input('Regular')
            #     else data_list[index][7]< '6':
            #         data_list[index][8]=input('No Regular')
                    
            #  for index in range(len(data_list)):
            #     if data_list[index][12]>= '6':
            #         data_list[index][13]=input('Regular')
            #     else data_list[index][12]< '6':
            #         data_list[index][13]=input('No Regular')
                    
    studentMenu() 
    
    studentfile=open('student.txt','w')
    studentfile.write('DNI\tNombre\tApellido\tDomicilio\tMateria1\tMateria1-Nota1\tMateria1-nota2\tMateria1-Promedio\tMateria1-Situacion\tMateria2\tMateria2-Nota2\tMateria1-nota2\tMateria2-Promedio\tMateria2-Situacion'+'\n')
    for index in range(1,len(data_list)):
        studentfile.write(str(data_list[index][0])+'\t'+str(data_list[index][1])+'\t'+str(data_list[index][2])+'\t'+str(data_list[index][3])+'\t'+str(data_list[index][4])+'\t'+str(data_list[index][5])+'\t'+str(data_list[index][6])+'\t'+str(data_list[index][7])+'\t'+str(data_list[index][8])+'\t'+str(data_list[index][9])+'\t'+str(data_list[index][10])+'\t'+str(data_list[index][11])+'\t'+str(data_list[index][12])+'\t'+str(data_list[index][13])+'\n')
    studentfile.close()
    subjectMenu()
    

#MODIFICAR NOTA------------------------------------------------------
def modifynote(): # definir una nueva materia
    dni=input(' Ingrese el DNI del alumno del que quiere agregar una nota: ')
    studentfile=open('student.txt','r')
    data_list = [] # Initialize an empty list to store the dictionaries
    for line in studentfile: # Read each individual's information
        values = line.strip().split("\t")  # tab-separated values
        data_list.append(values)     # Append the individual's line to the list
    studentfile.close()
    for index in range(len(data_list)):
        if data_list[index][0]==dni:
            auxm=int(input('Seleccione que nota quiere modificar: 1. Nota 1 - Materia 1; 2. Nota 2 - Materia 1; 3. Nota 1 - Materia 2; 4. Nota 2 - Materia 2 '))
        if auxm==1:
            data_list[index][5]=input('Ingrese Nota 1 - Materia 1: ')
        elif auxm==2:
            data_list[index][6]=input('Ingrese Nota 2 - Materia 2: ')
        elif auxm==2:
            data_list[index][10]=input('Ingrese Nota 1 - Materia 2: ')
        elif auxm==2:
            data_list[index][11]=input('Ingrese Nota2 - Materia 2: ')
        else:
            print('El alumno no esta registrado')
        studentMenu() 

def newstudent(): #Esta funcion agrega una nueva linea con los datos del alumno, falta agreagar que verifique si el DNI ya existe para no duplicarlo
    dni=input(' ingrese DNI del alumno: ')
    Name=input(' ingrese Nombre del alumno: ')
    Lastname=input(' ingrese Apellido del alumno: ')
    Address=input(' ingrese Dirección del alumno: ')
    Newline=dni+'\t'+Name+'\t'+Lastname+'\t'+Address+'\t 0'+'\t 0'+'\t 0'+'\t 0'+'\t 0'+'\t 0'+'\t 0'+'\t 0'+'\t 0'+'\t 0'+'\n'
    studentfile=open('student.txt','a')
    studentfile.write(Newline)
    studentfile.close()
    studentMenu()

def modifystudent(): #Función para modificar uno o varios datos del alumno
    dni=input(' Ingrese el DNI del alumno al que quiere modificar sus datos: ')
    studentfile=open('student.txt','r')
    data_list = [] # Initialize an empty list to store the dictionaries
    for line in studentfile: # Read each individual's information
        values = line.strip().split("\t")  # tab-separated values
        data_list.append(values)     # Append the individual's line to the list
    studentfile.close()
    for index in range(len(data_list)):
        if data_list[index][0]==dni:
            aux=int(input('Seleccione que dato quiere modificar: 1. Nombre; 2. Apellido; 3. Domicilio '))
            if aux==1:
                data_list[index][1]=input('Ingrese el nuevo nombre: ')
            elif aux==2:
                data_list[index][2]=input('Ingrese el nuevo apellido: ')
            elif aux==3:
                data_list[index][3]=input('Ingrese el nuevo domicilio: ')
            else:
                print('La opcion ingresada no es valida')
    studentfile=open('student.txt','w')
    studentfile.write('DNI\tNombre\tApellido\tDomicilio\tMateria1\tMateria1-Nota1\tMateria1-nota2\tMateria1-Promedio\tMateria1-Situacion\tMateria2\tMateria2-Nota2\tMateria1-nota2\tMateria2-Promedio\tMateria2-Situacion'+'\n')
    for index in range(1,len(data_list)):
        studentfile.write(str(data_list[index][0])+'\t'+str(data_list[index][1])+'\t'+str(data_list[index][2])+'\t'+str(data_list[index][3])+'\t'+str(data_list[index][4])+'\t'+str(data_list[index][5])+'\t'+str(data_list[index][6])+'\t'+str(data_list[index][7])+'\t'+str(data_list[index][8])+'\t'+str(data_list[index][9])+'\t'+str(data_list[index][10])+'\t'+str(data_list[index][11])+'\t'+str(data_list[index][12])+'\t'+str(data_list[index][13])+'\n')
    studentfile.close()
    studentMenu()

def liststudent():
    studentfile=open('student.txt','r')
    for line in studentfile: # Read each individual's information
        values = line.strip().split("\t")  # tab-separated values
        print(str(values[0]+'\t'+values[1]+'\t'+values[2]+'\t'+values[3]+'\t'+values[4]+'\t'+values[5]+'\t'+values[6]+'\t'+values[7]+'\t'+values[8]+'\t'+values[9]+'\t'+values[10]+'\t'+values[11]+'\t'+values[12]+'\t'+values[13]))
    studentfile.close()
    input(' Apreta cualquier tecla para continuar...')
    studentMenu()

def lineSeparator(number): # Esta funcion toma un numero cualquera, y genera un string con el caracter seleccionado, en este caso es consoleLength que esta definido en las variables globales
    ret = ''
    for _ in range(number):
        ret = ret + '-'
    print(' -'+ret)

def customPrint(string): # Esta funcion toma un string, al largo total definido de la consola le resta el largo del string para poder calcular donde agregar las paredes iniciales y finales
    spaces = ''
    for _ in range(consoleLength - len(string)):
        spaces = spaces + ' '
    
    print('| ' + string  + spaces +'|')

def customPrintCentered(string): # Misma funcion que customPrint() pero separa los espacios en dos y los mete uno de cada lado para que quede centrado
    spaces = ''
    customRange = round((consoleLength - len(string)) / 2)
    for _ in range(customRange):
        spaces = spaces + ' '
    
    print('|'+ spaces + string  + spaces +' |')

main() # Funcion principal donde se ejecuta todo