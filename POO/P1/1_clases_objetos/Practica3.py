import os
os.system("cls")

class profesores:
    def __init__(self, nombre, experiencia, num_profesor, impartir, evaluar):
        self.__nombre = nombre
        self.__experiencia = experiencia
        self.__num_profesor = num_profesor
        self.impartir = impartir
        self.evaluar = evaluar
          

        #metodos del objeto

        def impartir(self):
            return f"El profesor {self.__nombre} imparte la materia de {self.impartir}"
        
        def evaluar(self):
            return f"El profesor {self.__nombre} evalua a los alumnos de {self.evaluar}"
        
        @property
        def getnombre(self):
            return self.__nombre
        
        def getnombre(self):
            return self.__nombre
        
        @property
        def setnombre(self, nombre):
            self.__nombre = nombre

        def getexperiencia(self):
            return self.__experiencia
        
        @property
        def setexperiencia(self, experiencia):
            self.__experiencia = experiencia
        
        def getnum_profesor(self):
            return self.__num_profesor
        
        def setnum_profesor(self, num_profesor):
            self.__num_profesor = num_profesor
        


class alumnoss:
    def __init__(self, nombre, edad, matricula, inscribirse, estudiar):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula
        self.inscribirse = inscribirse
        self.estudiar = estudiar



        #metodos del objeto
        def inscribirse(self):
            return f"El alumno {self.__nombre} se ha inscrito en el curso de {self.inscribirse}"
        def estudiar(self):
            return f"El alumno {self.__nombre} esta estudiando {self.estudiar}"
        
        def getnombre(self):
            return self.__nombre
        def setnombre(self, nombre):
            self.__nombre = nombre
        
        def getedad(self):
            return self.__edad
        def setedad(self, edad):
            self.__edad = edad

        def getmatricula(self):
            return self.__matricula
        def setmatricula(self, matricula):
            self.__matricula = matricula
        



class cursos:
    def __init__(self, nombre, codigo, creditos, asignar):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos
        self.asignar = asignar


        #metodos del objeto
        def asignar(self):
            return f"El curso {self.__nombre} con codigo {self.__codigo} ha sido asignado al profesor {self.asignar}"
        
        def getnombre(self):
            return self.__nombre
        def setnombre(self, nombre):
            self.__nombre = nombre

        def getcodigo(self):
            return self.__codigo
        def setcodigo(self, codigo):
            self.__codigo = codigo
        
        def getcreditos(self):
            return self.__creditos
        def setcreditos(self, creditos):
            self.__creditos = creditos
        

        print(f"El curso {curso1.getnombre()} con codigo {curso1.getcodigo()} tiene {curso1.getcreditos()} creditos")
        print(f"El curso {curso2.getnombre()} con codigo {curso2.getcodigo()} tiene {curso2.getcreditos()} creditos")

        


profesor1 = profesores("Juan Perez", 10, 12345, "Matematicas", "Examenes")
profesor2 = profesores("Ana Gomez", 5, 67890, "Historia", "Trabajos")

alumno1 = alumnoss("Carlos Ruiz", 20, 54321, "Matematicas", "Algebra")
alumno2 = alumnoss("Luisa Fernandez", 22, 98765, "Historia", "Edad Media")

curso1 = cursos("Matematicas", "MAT101", 5, "Juan Perez")
curso2 = cursos("Historia", "HIS202", 4, "Ana Gomez")