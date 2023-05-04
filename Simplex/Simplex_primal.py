import numpy as np
import sys
import os


## np.eye(3) Identidad n = 3
class SimplexP:
    #TODO
    def __init__(self, c, A, b):
        # Debo buscar una solución básica factible
        self.__A = A #Coeficientes de las variables en las resticciones
        self.__c = c #Coeficientes de las variables en la solución
        self.__b = b #Terminos independientes de las restricciones
        self.__m, self.__n = A.shape #num restricciones, num variables
        self.__iteration = 1

    def do_simplex(self):
        print("Fase I")
        z = self.__first_phase()
        print()
        print("Acaba fase I")
        print()
        if z == 0:
            print("Fase II")
            print()
            acotado = self.__second_phase(self.__A, self.__c, self.__Binv, self.__basic, self.__notbasic, self.__b, self.__m)
            if acotado != "F":
                print(f"Solució óptima trobada, iteració {self.__iteration - 1}, z = {self.__z}")
                print()
                print("Acaba fase II")
                print("\nSolució òptima:\n")
                print(f"vb =\n{self.__vb}")
                print(f"xb =\n{self.__xb}")
                print(f"z =\n{self.__z}")
                print(f"r =\n{self.__r}\n")
        else:
            print("Problema no factible")
        print("Fi simplex primal")

    #TODO
    def __first_phase(self):
        ## Afegir variables artificials
        self.__AI = self.__A.copy()
        for x in range (self.__m):
            column = np.zeros(self.__m)
            column[x] = 1
            self.__AI = np.c_[ self.__AI, column]
        #Preparar variables
        Im, In = self.__AI.shape
        self.__cI = np.array([0 for x in range(self.__n)])
        self.__cI = np.r_[self.__cI, np.array([1 for x in range(self.__m)])]
        self.__Ibasic = [x for x in range(self.__n, In)] #Variables básicas de la primera fase
        self.__Inotbasic = [x for x in range(self.__n)] #Varialbes no básicas de la primera fase
        self.__IB = self.__AI[0:,self.__Ibasic]
        self.__IBinv = self.__IB.copy()
        #Executar fase 2 amb el problema artificial
        z = self.__second_phase(self.__AI, self.__cI, self.__IBinv, self.__Ibasic, self.__Inotbasic, self.__b, Im)
        if z > 0:
            print("Problema no factible")
        else:
            print(f"Solució básica factible trobada, iteració {self.__iteration - 1}")
            for x in range(self.__n, In):
                self.__Inotbasic.remove(x)
            #### Parametros para el simplex primal 2n fase
            self.__basic = self.__Ibasic
            self.__notbasic = self.__Inotbasic
            self.__Binv = self.__IBinv
        return z
    #TODO
    def __second_phase(self, A, c, Binv, basic, notbasic, b, m):
        #Se debe actualizar bien B y Binv para que funcione.
        ######## Primera etapa
        notbasic.sort()
        xb = np.matmul(Binv, b)
        An = A[0:,notbasic]
        cb = c[basic]
        cn = c[notbasic]
        z = np.matmul(cb, xb)
        ######## Fin primera etapa
        optimo = False
        while not optimo:
            ######## Segunda etapa
            r = cn - np.matmul(np.matmul(cb, Binv),An)
            i = 0
            while i < len(r) and r[i] >= 0:
                i += 1
            if i >= len(r) or r[i] >= 0:
                self.__z = z
                self.__vb = basic
                self.__xb = xb
                self.__r = r
                optimo = True
                break
            q = notbasic[i]
            ######## Tercera etapa
            db = -Binv @ A[0:,q]
            acotado = False
            select_theta = []
            i = 0
            while i < len(db):
                if db[i] < 0:
                    select_theta +=[(-(xb[i] / db[i]), basic[i], i)]
                    acotado = True
                i += 1
            if not acotado:
                print("Solució no acotada")
                print(f"r =\n{self.__r}\n")
                return "F"
            ######## Cuarta etapa
            bland = min(select_theta) #Agafo la theta més petita, en cas d'empat el de índex (de variable) més petit
                                      #Regla de Bland
            theta = bland[0]
            p = bland[2]
            bpp = bland[1]
            notbasic += [basic[p]] # Coloco la que sale en las no básicas
            notbasic.remove(q) # Elimino la que sale
            notbasic.sort() # ordeno
            basic[p] = q # Intercambio la que sale por la que entra
            ######## Quinta etapa
            #### Actualización de la inversa
            E = []
            i = 0
            j = 0
            while i < m:
                E.append([]) #Preparo la fila a rellenar
                while j < len(basic):
                    #Relleno matriz E por filas (primero fila 1, después fila 2...)
                    if i == j:
                        if j != p:
                            E[i] += [1]
                        else:
                            E[i] += [-1 / db[p]]
                    else:
                        if j == p:
                            E[i] += [-db[i] / db[p]]
                        else:
                            E[i] += [0]
                    j += 1
                i += 1
                j = 0
            E = np.array(E)
            Binv = np.matmul(E, Binv) #Hago la actualización de la inversa
            #### Fin actualización de la inversa
            i = 0
            while i < len(basic):
                antnum = xb[i]
                xb[i] = xb[i] + theta * db[i]
                if xb[i] < 0:
                    # Codi comentat per veure la comprobació del perquè igualo xb[i] a 0 quan és negatiu
                    # print(f"xb[{i}] sense actualitzar = {antnum}\nxb[{7}] amb actualització = {xb[i]}\ntheta*db = {theta * db[i]}\ndb[i]= {db[i]}\ntheta = {theta}")
                    # input()
                    xb[i] = 0
                i += 1
            # Actualizaciones del cambio de base
            xb = np.matmul(Binv, b)
            An = A[0:,notbasic]
            cb = c[basic]
            cn = c[notbasic]
            z = np.matmul(cb, xb)
            ######## sexta etapa
            print(f"\tIteració   {self.__iteration}: q = {q}, B[p] = {bpp}, p = {p} theta* = {theta}, z = {z}")
            self.__iteration += 1
        self.__IBinv = Binv
        return z
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Error:")
        print("\tPer utilitzar la implementació has de posar els .txt desprès de cridar-ho.")
        print("\tPer exemple:\n\t\tpy .\Simplex_primal.py S1 S2")
    else:
        for x in sys.argv[1:]:
            os.system("cls")
            c = []
            A = []
            b = []
            with open(f'./Data/{x}.txt', 'r', encoding = 'UTF-8') as f:
                f.readline()
                content = f.readline().split()
                c = [eval(i) for i in content]
                content = f.readline()
                while content[0] != "A":
                        content = f.readline()
                content = f.readline()
                while content[0] != "\n":
                    A += [[eval(i) for i in content.split()]]
                    content = f.readline()
                f.readline()
                content = f.readline()
                b = [eval(i) for i in content.split()]

            c = np.array(c) #Coeficientes de las variables en la solución
            A = np.array(A) #Coeficientes de las variables en las resticciones
            b = np.array(b) #Terminos independientes de las restricciones
            print(f"Inici {x}.txt\n")
            simplex = SimplexP(c, A, b)
            simplex.do_simplex()
            print(f"Fi {x}.txt\n")
            print("Per continuar pressiona qualsevol tecla")
            input()
        print("Finalització del programa")