
from os import system;

ciclistas = [];
system('cls');

opcion = 9999;
codigo = 1;
while (opcion != 0):
    print('1. Ingresar 1 ciclista');
    print('2. Mostrar tabla de posiciones de la prueba');
    print('3. Cambiar el tiempo de un ciclista');
    print('4. Retirar ciclista de la tabla de posiciones');
    print('0. Salir');
    opcion = int(input("Escoger opción: "))
    system('cls');
    if opcion == 1:
        ciclista = {
        "codigo": int(codigo),
        "nombre": input('Nombre del ciclista: '),
        "edad": int(input('Edad del ciclista: ')),
        "pais": input('País del ciclista: '),
        "equipo": input('Equipo del ciclista: '),
        "tiempo": int(input('El tiempo del ciclista: '))
        }
        ciclistas.append(ciclista);
        codigo = codigo + 1;
        system('cls');
        print('Se agregó el ciclista correctamente \n\n');
    elif opcion == 2:
        
        if(len(ciclistas) != 0):
            print("| CÓDIGO | NOMBRE | EDAD | PAIS | EQUIPO | TIEMPO |");
            for ciclista in ciclistas:
                 print(f"| {ciclista['codigo']} | {ciclista['nombre']} | {ciclista['edad']} | {ciclista['pais']} | {ciclista['equipo']}| {ciclista['tiempo']} |");
            print('\n\n')
        else:
            print('No hay ciclistas en la tabla de posiciones \n\n');
    elif opcion == 3:
        if(len(ciclistas) != 0):
            ciclistaBuscar = int(input('Código del ciclista a cambiar el tiempo: '));
            hayCiclista: bool = False;
            for ciclista in ciclistas:
                if(ciclista['codigo'] == ciclistaBuscar):
                    print(f"Tiempo actual del ciclista:  {ciclista['tiempo']}" );
                    ciclista['tiempo'] = int(input('El tiempo nuevo: '));
                    print('Se cambió el tiempo correctamente \n\n');
                    hayCiclista = True;
                if(hayCiclista == False):
                    print('El ciclista no se encontró en la tabla\n\n');
        else:
            print('No hay ciclistas en la tabla de posiciones \n\n');
    elif opcion == 4:
        if(len(ciclistas) != 0):
            hayCiclista: bool = False;
            ciclistaBuscar = int(input('Código del ciclista: '));
            for ciclista in ciclistas:
                if(ciclista['codigo'] == ciclistaBuscar):
                    ciclistas.remove(ciclista);
                    print('Ciclista retirado correctamente\n\n');
                    hayCiclista = True;
                if(hayCiclista == False):
                    print('El ciclista no se encontró en la tabla\n\n');
        else:
            print('No hay ciclistas en la tabla de posiciones \n\n');
    elif opcion == 0:
        pass
    
    
