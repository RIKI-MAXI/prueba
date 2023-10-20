from datetime import datetime
import json
import os

# Definiciones de las clases de las entidades
class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = []

    def agregar_nota(self, carrera, semestre, asignatura, seccion, valor):
        nota = Nota(self, carrera, semestre, asignatura, seccion, valor)
        self.notas.append(nota)

class Semestre:
    def __init__(self, nivel, inicio_semestre, fin_semestre):
        self.nivel = nivel
        self.inicio_semestre = datetime.strptime(inicio_semestre, "%d/%m/%Y")
        self.fin_semestre = datetime.strptime(fin_semestre, "%d/%m/%Y")

class Nota:
    def __init__(self, alumno, carrera, semestre, asignatura, seccion, n1, n2, exa1, n3, n4, exa2):
        self.alumno = alumno
        self.carrera = carrera
        self.semestre = semestre
        self.asignatura = asignatura
        self.seccion = seccion
        self.n1 = n1
        self.n2 = n2
        self.exa1 = exa1
        self.n3 = n3
        self.n4 = n4
        self.exa2 = exa2

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre

class Seccion:
    def __init__(self, nombre, paralelo):
        self.nombre = nombre
        self.paralelo = paralelo

# Funciones CRUD para Carrera
carreras = []

def crear_carrera():
    nombre = input("Ingrese el nombre de la carrera: ")
    nueva_carrera = Carrera(nombre)
    carreras.append(nueva_carrera)
    guardar_datos_json("carreras.json", carreras)
    return nueva_carrera

def consultar_carreras():
    return [carrera.nombre for carrera in carreras]

def actualizar_carrera(carrera, nuevo_nombre):
    carrera.nombre = nuevo_nombre
    guardar_datos_json("carreras.json", carreras)

def eliminar_carrera(carrera):
    carreras.remove(carrera)
    guardar_datos_json("carreras.json", carreras)

# Funciones CRUD para Alumno
alumnos = []

def crear_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    nuevo_alumno = Alumno(nombre, apellido)
    alumnos.append(nuevo_alumno)
    guardar_datos_json("alumnos.json", alumnos)
    return nuevo_alumno

def consultar_alumnos():
    return [(alumno.nombre, alumno.apellido) for alumno in alumnos]

def actualizar_alumno(alumno, nuevo_nombre, nuevo_apellido):
    alumno.nombre = nuevo_nombre
    alumno.apellido = nuevo_apellido
    guardar_datos_json("alumnos.json", alumnos)

def eliminar_alumno(alumno):
    alumnos.remove(alumno)
    guardar_datos_json("alumnos.json", alumnos)

# Funciones CRUD para Seccion
secciones = []

def crear_seccion():
    nombre = input("Ingrese el nombre de la sección: ")
    paralelo = input("Ingrese el paralelo de la sección: ")
    nueva_seccion = Seccion(nombre, paralelo)
    secciones.append(nueva_seccion)
    guardar_datos_json("secciones.json", [s.__dict__ for s in secciones])
    return nueva_seccion

def consultar_secciones():
    return [(seccion.nombre, seccion.paralelo) for seccion in secciones]

def actualizar_seccion(seccion, nuevo_nombre, nuevo_paralelo):
    seccion.nombre = nuevo_nombre
    seccion.paralelo = nuevo_paralelo
    guardar_datos_json("secciones.json", [s.__dict__ for s in secciones])

def eliminar_seccion(seccion):
    secciones.remove(seccion)
    guardar_datos_json("secciones.json", [s.__dict__ for s in secciones])

# Funciones CRUD para Profesor
profesores = []

def crear_profesor():
    nombre = input("Ingrese el nombre del profesor: ")
    apellido = input("Ingrese el apellido del profesor: ")
    nuevo_profesor = Profesor(nombre, apellido)
    profesores.append(nuevo_profesor)
    guardar_datos_json("profesores.json", [p.__dict__ for p in profesores])
    return nuevo_profesor

def consultar_profesores():
    return [(profesor.nombre, profesor.apellido) for profesor in profesores]

def actualizar_profesor(profesor, nuevo_nombre, nuevo_apellido):
    profesor.nombre = nuevo_nombre
    profesor.apellido = nuevo_apellido
    guardar_datos_json("profesores.json", [p.__dict__ for p in profesores])

def eliminar_profesor(profesor):
    profesores.remove(profesor)
    guardar_datos_json("profesores.json", [p.__dict__ for p in profesores])

# Funciones CRUD para Asignatura
asignaturas = []

def crear_asignatura():
    nombre = input("Ingrese el nombre de la asignatura: ")
    nueva_asignatura = Asignatura(nombre)
    asignaturas.append(nueva_asignatura)
    guardar_datos_json("asignaturas.json", [a.__dict__ for a in asignaturas])
    return nueva_asignatura

def consultar_asignaturas():
    return [asignatura.nombre for asignatura in asignaturas]

def actualizar_asignatura(asignatura, nuevo_nombre):
    asignatura.nombre = nuevo_nombre
    guardar_datos_json("asignaturas.json", [a.__dict__ for a in asignaturas])

def eliminar_asignatura(asignatura):
    asignaturas.remove(asignatura)
    guardar_datos_json("asignaturas.json", [a.__dict__ for a in asignaturas])

# Funciones CRUD para Semestre
semestres = []

def crear_semestre():
    nivel = input("Ingrese el nivel del semestre: ")
    inicio_semestre = input("Ingrese la fecha de inicio (DD/MM/AAAA): ")
    fin_semestre = input("Ingrese la fecha de fin (DD/MM/AAAA): ")
    nuevo_semestre = Semestre(nivel, inicio_semestre, fin_semestre)
    semestres.append(nuevo_semestre)
    guardar_datos_json("semestres.json", [s.__dict__ for s in semestres])
    
def consultar_semestres():
    return [(semestre.nivel, semestre.inicio_semestre.strftime("%d/%m/%Y"), semestre.fin_semestre.strftime("%d/%m/%Y")) for semestre in semestres]

def actualizar_semestre(semestre, nuevo_inicio, nuevo_fin):
    semestre.inicio_semestre = datetime.strptime(nuevo_inicio, "%d/%m/%Y")
    semestre.fin_semestre = datetime.strptime(nuevo_fin, "%d/%m/%Y")
    guardar_datos_json("semestres.json", [s.__dict__ for s in semestres])

def eliminar_semestre(semestre):
    semestres.remove(semestre)
    guardar_datos_json("semestres.json", [s.__dict__ for s in semestres])

# Funciones CRUD para Nota
notas = []

def crear_nota():
    # Lógica para crear nota
    nombre_alumno = input("Nombre del alumno: ")
    nombre_carrera = input("Nombre de la carrera: ")
    nombre_semestre = input("Nivel del semestre: ")
    nombre_asignatura = input("Nombre de la asignatura: ")
    nombre_seccion = input("Nombre de la sección: ")
    
    alumno = buscar_alumno(nombre_alumno)
    carrera = buscar_carrera(nombre_carrera)
    semestre = buscar_semestre(nombre_semestre)
    asignatura = buscar_asignatura(nombre_asignatura)
    seccion = buscar_seccion(nombre_seccion)
    
    if alumno is not None and carrera is not None and semestre is not None and asignatura is not None and seccion is not None:
        # Solicitar las 5 notas
        n1 = float(input("Ingrese el valor de n1: "))
        n2 = float(input("Ingrese el valor de n2: "))
        exa1 = float(input("Ingrese el valor de examen 1: "))
        n3 = float(input("Ingrese el valor de n3: "))
        n4 = float(input("Ingrese el valor de n4: "))
        exa2 = float(input("Ingrese el valor de examen 2: "))
        
        nueva_nota = Nota(alumno, carrera, semestre, asignatura, seccion, n1, n2, exa1, n3, n4, exa2)
        notas.append(nueva_nota)
        guardar_datos_json("notas.json", [n.__dict__ for n in notas])
        print("Nota creada exitosamente.")
    else:
        print("Alumno, carrera, semestre, asignatura o sección no encontrados.")

def consultar_notas():
    for nota in notas:
        alumno_nombre = nota.alumno.nombre if nota.alumno is not None else "Desconocido"
        carrera_nombre = nota.carrera.nombre if nota.carrera is not None else "Desconocido"
        semestre_nivel = nota.semestre.nivel if nota.semestre is not None else "Desconocido"
        asignatura_nombre = nota.asignatura.nombre if nota.asignatura is not None else "Desconocido"
        seccion_nombre = nota.seccion.nombre if nota.seccion is not None else "Desconocido"
        print(f"Alumno: {alumno_nombre}\nCarrera: {carrera_nombre}\nSemestre: {semestre_nivel}\nAsignatura: {asignatura_nombre}\nSección: {seccion_nombre}\nN1: {nota.n1}\nN2: {nota.n2}\nExamen 1: {nota.exa1}\nN3: {nota.n3}\nN4: {nota.n4}\nExamen 2: {nota.exa2}\n")

        
        
def actualizar_nota():
    nombre_alumno = input("Nombre del alumno cuya nota deseas actualizar: ")
    nombre_carrera = input("Nombre de la carrera: ")
    nombre_semestre = input("Nivel del semestre: ")
    nombre_asignatura = input("Nombre de la asignatura: ")
    nombre_seccion = input("Nombre de la sección: ")

    alumno = buscar_alumno(nombre_alumno)
    carrera = buscar_carrera(nombre_carrera)
    semestre = buscar_semestre(nombre_semestre)
    asignatura = buscar_asignatura(nombre_asignatura)
    seccion = buscar_seccion(nombre_seccion)

    if alumno is not None and carrera is not None and semestre is not None and asignatura is not None and seccion is not None:
        for nota in notas:
            if (nota.alumno == alumno and nota.carrera == carrera and nota.semestre == semestre and
                nota.asignatura == asignatura and nota.seccion == seccion):

                # Solicitar los nuevos valores de las notas
                nuevo_n1 = float(input("Nuevo valor de n1: "))
                nuevo_n2 = float(input("Nuevo valor de n2: "))
                nuevo_exa1 = float(input("Nuevo valor de examen 1: "))
                nuevo_n3 = float(input("Nuevo valor de n3: "))
                nuevo_n4 = float(input("Nuevo valor de n4: "))
                nuevo_exa2 = float(input("Nuevo valor de examen 2: "))
                
                # Actualizar las notas en la instancia de Nota
                nota.n1 = nuevo_n1
                nota.n2 = nuevo_n2
                nota.exa1 = nuevo_exa1
                nota.n3 = nuevo_n3
                nota.n4 = nuevo_n4
                nota.exa2 = nuevo_exa2

                guardar_datos_json("notas.json", [n.__dict__ for n in notas])
                print("Notas actualizadas exitosamente.")
                break
        else:
            print("No se encontró la nota para los datos especificados.")
    else:
        print("Alumno, carrera, semestre, asignatura o sección no encontrados.")

def eliminar_nota():
    # Lógica para eliminar nota
    nombre_alumno = input("Nombre del alumno cuya nota deseas eliminar: ")
    nombre_carrera = input("Nombre de la carrera: ")
    nombre_semestre = input("Nivel del semestre: ")
    nombre_asignatura = input("Nombre de la asignatura: ")
    nombre_seccion = input("Nombre de la sección: ")

    # Buscar las instancias correspondientes a los nombres ingresados
    alumno = buscar_alumno(nombre_alumno)
    carrera = buscar_carrera(nombre_carrera)
    semestre = buscar_semestre(nombre_semestre)
    asignatura = buscar_asignatura(nombre_asignatura)
    seccion = buscar_seccion(nombre_seccion)

    if alumno is not None and carrera is not None and semestre is not None and asignatura is not None and seccion is not None:
        for nota in notas:
            if (nota.alumno == alumno and nota.carrera == carrera and nota.semestre == semestre and
                nota.asignatura == asignatura and nota.seccion == seccion):
                notas.remove(nota)
                guardar_datos_json("notas.json", [n.__dict__ for n in notas])
                print("Nota eliminada exitosamente.")
                break
        else:
            print("No se encontró la nota para los datos especificados.")
    else:
        print("Alumno, carrera, semestre, asignatura o sección no encontrados.")
        
# Funciones genéricas para cargar y guardar datos JSON

def cargar_datos_json(archivo):
    try:
        with open(archivo, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def guardar_datos_json(archivo, data):
    with open(archivo, 'w') as file:
        json.dump(data, file, default=convert_to_dict, indent=4)

def convert_to_dict(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%d/%m/%Y')
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    return obj

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funciones para buscar entidades
def buscar_alumno(nombre_alumno):
    for alumno in alumnos:
        if alumno.nombre == nombre_alumno:
            return alumno
    print(f"No se encontró al alumno con el nombre: {nombre_alumno}")
    return None

def buscar_carrera(nombre_carrera):
    for carrera in carreras:
        if carrera.nombre == nombre_carrera:
            return carrera
    print(f"No se encontró la carrera con el nombre: {nombre_carrera}")
    return None

def buscar_semestre(nombre_semestre):
    for semestre in semestres:
        if semestre.nivel == nombre_semestre:
            return semestre
    print(f"No se encontró el semestre con el nivel: {nombre_semestre}")
    return None

def buscar_asignatura(nombre_asignatura):
    for asignatura in asignaturas:
        if asignatura.nombre == nombre_asignatura:
            return asignatura
    print(f"No se encontró la asignatura con el nombre: {nombre_asignatura}")
    return None

def buscar_seccion(nombre_seccion):
    for seccion in secciones:
        if seccion.nombre == nombre_seccion:
            return seccion
    print(f"No se encontró la sección con el nombre: {nombre_seccion}")
    return None

def buscar_profesor(nombre_profesor):
    for profesor in profesores:
        if profesor.nombre == nombre_profesor:
            return profesor
    return None

alumnos_data = cargar_datos_json("alumnos.json")
carreras_data = cargar_datos_json("carreras.json")
semestres_data = cargar_datos_json("semestres.json")
asignaturas_data = cargar_datos_json("asignaturas.json")
secciones_data = cargar_datos_json("secciones.json")
notas_data = cargar_datos_json("notas.json")

alumnos = [Alumno(alumno['nombre'], alumno['apellido']) for alumno in alumnos_data]
carreras = [Carrera(carrera['nombre']) for carrera in carreras_data]
semestres = [Semestre(semestre['nivel'], semestre['inicio_semestre'], semestre['fin_semestre']) for semestre in semestres_data]
asignaturas = [Asignatura(asignatura['nombre']) for asignatura in asignaturas_data]
secciones = [Seccion(seccion['nombre'], seccion['paralelo']) for seccion in secciones_data]
notas = [Nota(
    buscar_alumno(nota['alumno']),
    buscar_carrera(nota['carrera']),
    buscar_semestre(nota['semestre']),
    buscar_asignatura(nota['asignatura']),
    buscar_seccion(nota['seccion']),
    nota['n1'],
    nota['n2'],
    nota['exa1'],
    nota['n3'],
    nota['n4'],
    nota['exa2']
) for nota in notas_data]

while True:
    limpiar_pantalla()
    print("Seleccione la entidad para administrar:")
    print("1. Carrera")
    print("2. Alumno")
    print("3. Sección")
    print("4. Profesor")
    print("5. Asignatura")
    print("6. Semestre")
    print("7. Nota")
    print("8. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        limpiar_pantalla()
        print("Gestión de Carreras")
        print("1. Crear Carrera")
        print("2. Consultar Carreras")
        print("3. Actualizar Carrera")
        print("4. Eliminar Carrera")
        subopcion = input("Elija una opción: ")
        if subopcion == "1":
            crear_carrera()
        elif subopcion == "2":
            print("Carreras disponibles:")
            print(consultar_carreras())
            input("Presiona Enter para continuar...")
        elif subopcion == "3":
            nombre_carrera = input("Nombre de la carrera a actualizar: ")
            nuevo_nombre = input("Nuevo nombre de la carrera: ")
            carrera = buscar_carrera(nombre_carrera)
            if carrera is not None:
                actualizar_carrera(carrera, nuevo_nombre)
                print("Carrera actualizada exitosamente.")
            else:
                print("Carrera no encontrada.")
        elif subopcion == "4":
            nombre_carrera = input("Nombre de la carrera a eliminar: ")
            carrera = buscar_carrera(nombre_carrera)
            if carrera is not None:
                eliminar_carrera(carrera)
                print("Carrera eliminada exitosamente.")
            else:
                print("Carrera no encontrada.")
        else:
            print("Opción no válida.")

    elif opcion == "2":
        limpiar_pantalla()
        print("Gestión de Alumnos")
        print("1. Crear Alumno")
        print("2. Consultar Alumnos")
        print("3. Actualizar Alumno")
        print("4. Eliminar Alumno")
        subopcion = input("Elija una opción: ")
        if subopcion == "1":
            crear_alumno()
        elif subopcion == "2":
            print("Alumnos disponibles:")
            print(consultar_alumnos())
            input("Presiona Enter para continuar...")
        elif subopcion == "3":
            nombre_alumno = input("Nombre del alumno a actualizar: ")
            nuevo_nombre = input("Nuevo nombre del alumno: ")
            nuevo_apellido = input("Nuevo apellido del alumno: ")
            alumno = buscar_alumno(nombre_alumno)
            if alumno is not None:
                actualizar_alumno(alumno, nuevo_nombre, nuevo_apellido)
                print("Alumno actualizado exitosamente.")
            else:
                print("Alumno no encontrado.")
        elif subopcion == "4":
            nombre_alumno = input("Nombre del alumno a eliminar: ")
            alumno = buscar_alumno(nombre_alumno)
            if alumno is not None:
                eliminar_alumno(alumno)
                print("Alumno eliminado exitosamente.")
            else:
                print("Alumno no encontrado.")
        else:
            print("Opción no válida.")

    elif opcion == "3":
        limpiar_pantalla()
        print("Gestión de Secciones")
        print("1. Crear Sección")
        print("2. Consultar Secciones")
        print("3. Actualizar Sección")
        print("4. Eliminar Sección")
        subopcion = input("Elija una opción: ")
        if subopcion == "1":
            crear_seccion()
        elif subopcion == "2":
            print("Secciones disponibles:")
            print(consultar_secciones())
            input("Presiona Enter para continuar...")
        elif subopcion == "3":
            nombre_seccion = input("Nombre de la sección a actualizar: ")
            nuevo_nombre = input("Nuevo nombre de la sección: ")
            nuevo_paralelo = input("Nuevo paralelo de la sección: ")
            seccion = buscar_seccion(nombre_seccion)
            if seccion is not None:
                actualizar_seccion(seccion, nuevo_nombre, nuevo_paralelo)
                print("Sección actualizada exitosamente.")
            else:
                print("Sección no encontrada.")
        elif subopcion == "4":
            nombre_seccion = input("Nombre de la sección a eliminar: ")
            seccion = buscar_seccion(nombre_seccion)
            if seccion is not None:
                eliminar_seccion(seccion)
                print("Sección eliminada exitosamente.")
            else:
                print("Sección no encontrada.")
        else:
            print("Opción no válida.")

    elif opcion == "4":
        limpiar_pantalla()
        print("Gestión de Profesores")
        print("1. Crear Profesor")
        print("2. Consultar Profesores")
        print("3. Actualizar Profesor")
        print("4. Eliminar Profesor")
        subopcion = input("Elija una opción: ")
        if subopcion == "1":
            crear_profesor()
        elif subopcion == "2":
            print("Profesores disponibles:")
            print(consultar_profesores())
            input("Presiona Enter para continuar...")
        elif subopcion == "3":
            nombre_profesor = input("Nombre del profesor a actualizar: ")
            nuevo_nombre = input("Nuevo nombre del profesor: ")
            nuevo_apellido = input("Nuevo apellido del profesor: ")
            profesor = buscar_profesor(nombre_profesor)
            if profesor is not None:
                actualizar_profesor(profesor, nuevo_nombre, nuevo_apellido)
                print("Profesor actualizado exitosamente.")
            else:
                print("Profesor no encontrado.")
        elif subopcion == "4":
            nombre_profesor = input("Nombre del profesor a eliminar: ")
            profesor = buscar_profesor(nombre_profesor)
            if profesor is not None:
                eliminar_profesor(profesor)
                print("Profesor eliminado exitosamente.")
            else:
                print("Profesor no encontrado.")
        else:
            print("Opción no válida.")
    elif opcion == "5":
        limpiar_pantalla()
        print("Gestión de Asignaturas")
        print("1. Crear Asignatura")
        print("2. Consultar Asignaturas")
        print("3. Actualizar Asignatura")
        print("4. Eliminar Asignatura")
        subopcion = input("Elija una opción: ")
        if subopcion == "1":
            crear_asignatura()
        elif subopcion == "2":
            print("Asignaturas disponibles:")
            print(consultar_asignaturas())
            input("Presiona Enter para continuar...")
        elif subopcion == "3":
            nombre_asignatura = input("Nombre de la asignatura a actualizar: ")
            nuevo_nombre = input("Nuevo nombre de la asignatura: ")
            asignatura = buscar_asignatura(nombre_asignatura)
            if asignatura is not None:
                actualizar_asignatura(asignatura, nuevo_nombre)
                print("Asignatura actualizada exitosamente.")
            else:
                print("Asignatura no encontrada.")
        elif subopcion == "4":
            nombre_asignatura = input("Nombre de la asignatura a eliminar: ")
            asignatura = buscar_asignatura(nombre_asignatura)
            if asignatura is not None:
                eliminar_asignatura(asignatura)
                print("Asignatura eliminada exitosamente.")
            else:
                print("Asignatura no encontrada.")
        else:
            print("Opción no válida.")
    elif opcion == "6":
        limpiar_pantalla()
        print("Gestión de Semestres")
        print("1. Crear Semestre")
        print("2. Consultar Semestres")
        print("3. Actualizar Semestre")
        print("4. Eliminar Semestre")
        subopcion = input("Elija una opción: ")
        if subopcion == "1":
            crear_semestre()
        elif subopcion == "2":
            print("Semestres disponibles:")
            for semestre in consultar_semestres():
                print(f"Nivel: {semestre[0]}, Inicio: {semestre[1]}, Fin: {semestre[2]}")
            input("Presiona Enter para continuar...")
        elif subopcion == "3":
            nivel_semestre = input("Nivel del semestre a actualizar: ")
            nuevo_inicio = input("Nueva fecha de inicio (DD/MM/AAAA): ")
            nuevo_fin = input("Nueva fecha de fin (DD/MM/AAAA): ")
            semestre = buscar_semestre(nivel_semestre)
            if semestre is not None:
                actualizar_semestre(semestre, nuevo_inicio, nuevo_fin)
                print("Semestre actualizado exitosamente.")
            else:
                print("Semestre no encontrado.")
        elif subopcion == "4":
            nivel_semestre = input("Nivel del semestre a eliminar: ")
            semestre = buscar_semestre(nivel_semestre)
            if semestre is not None:
                eliminar_semestre(semestre)
                print("Semestre eliminado exitosamente.")
            else:
                print("Semestre no encontrado.")
        else:
            print("Opción no válida.")
    elif opcion == "7":
        limpiar_pantalla()
        print("Gestión de Notas")
        print("1. Crear Nota")
        print("2. Consultar Notas")
        print("3. Actualizar Nota")
        print("4. Eliminar Nota")
        subopcion = input("Elija una opción: ")
        if subopcion == "1":
            crear_nota()
        elif subopcion == "2":
            print("Notas disponibles:")
            consultar_notas()
            input("Presiona Enter para continuar...")
        elif subopcion == "3":
            actualizar_nota()
        elif subopcion == "4":
            eliminar_nota()
        else:
            print("Opción no válida.")
    elif opcion == "8":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

    input("Presiona Enter para continuar...")

