# Autor: Jose
# version: 0.0.1
# data: 15/03/2022

# description: kata IV - sesión de clase

from kata4.Alumno import Alumno
from kata4.Asignatura import Asignatura
from kata4.Clase import Clase

if __name__ == '__main__':
    # Instancias de clase
    al1 = Alumno('Jose', 'Marín', '123456789A', 35)

    # Uso de metodos de clase
    al1.addNota(9)
    al1.addNota(5)
    al1.addNota(7)
    al1.addAge()

    # Instancia de Asignatura
    as1 = Asignatura('ciencias')
    as1.addNota(10)

    as2 = Asignatura('literatura')
    as2.addNota(7)

    as3 = Asignatura('python')
    as3.addNota(7)

    # Pasamos en objeto asignatura por composición al objeto alumno
    al1.addAsignatura(as1)
    al1.addAsignatura(as2)

    print(al1)

    # Creación de objeto clase
    cl1 = Clase('78AB','Juan Martinez')
    print(cl1.profesor)

    cl1.addAsig(as3)
    cl1.addAsig(as1)
    print('Lista de asignaturas en Clase ----------------------------------')

    for asig in cl1.asignaturas:
        print(asig)

    cl1.addAlum(al1)
    print('Alumnos matriculados en Clase----------------------------------')

    for alu in cl1.alumnos:
        print(alu)

    cl1.__id = 457

    print(cl1.id)

    print(dir(cl1))
