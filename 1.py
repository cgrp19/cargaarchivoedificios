import csv
class Departamento:
    __id=int
    __nya=str
    __npiso=int
    __ndepartamento=int
    __canth=int
    __cantb=int
    __sup=float
    def __init__(self,id,nya,npiso,ndepartamento,canth,cantb__cantb,sup):
        self.__id=id
        self.__nya=nya
        self.__npiso=npiso
        self.__ndepartamento=ndepartamento
        self.__canth=canth
        self.__cantb=cantb__cantb
        self.__sup=sup
    def getsup(self):
        return self.__sup
    def MostrarPropietariosDep(self):
        print('Propietarios de departamento {}: {}'.format(self.__id,self.__nya))
    def getnombre(self):
        return self.__nya
    def getpiso(self):
        return self.__npiso
    def getcanth(self):
        return self.__canth
    def getcantb(self):
        return self.__cantb
class Edificio:
    __id=int
    __nombre=str
    __dir=str
    __nempresa=str
    __cantpisos=int
    __cantdep=int
    __departametos=list
    def __init__(self,id,nombre,dir,nempresa,cantpisos,cantdep):
        self.__id=id
        self.__nombre=nombre
        self.__dir=dir
        self.__nempresa=nempresa
        self.__cantpisos=cantpisos
        self.__cantdep=cantdep
        self.__departamentos=[]
    def AgregarDepartamento(self,departamento):
        
        self.__departamentos.append(departamento)
    def MostrarSuperficieTotal(self):
        suptotal=0
        for departamento in self.__departamentos:
            suptotal+=departamento.getsup()
        print('Superficie del edificio {} : {}'.format(self.__nombre,suptotal))
        return suptotal
    def getid(self):
        return self.__id
    def MostrarPropietariosEd(self):
        for departamento in self.__departamentos:
            departamento.MostrarPropietariosDep()
    def getnombre(self):
        return self.__nombre
    def superficie(self,nombre):
        for departamento in self.__departamentos:
            if departamento.getnombre()==nombre:
                print('Superficie del departamento:{}'.format(departamento.getsup()))
                sup= (departamento.getsup()*100/self.MostrarSuperficieTotal())
                print('Reperesenta el {} por ciento del edificio'.format(sup))
    def Piso(self,piso):
        cant=0
        for departamento in self.__departamentos:
            print('piso:{}'.format(departamento.getpiso()))
            if departamento.getpiso()==int(piso):
                
                #print('habitaciones:{}, banos:{}'.format(departamento.getcanth(),departamento.getcantb()))
                if departamento.getcantb() > 1 and departamento.getcanth() ==3:
                    cant+=1
        print('Cantidad del edificio{}:{}'.format(self.__id, cant))
                
                
            
    

class Coleccion:
    __listaedificios=list
    def __init__(self):
        self.__listaedificios=[]
    def AgregarEdificio(self,edificio):
        self.__listaedificios.append(edificio)
    def MostrarSuperficieEdificio(self,id):
        
        for edificio in self.__listaedificios:
            
            if edificio.getid()==int(id):
                
                edificio.MostrarSuperficieTotal()
        return
    def MostrarProp(self,nombre):
        for edificio in self.__listaedificios:
            if edificio.getnombre()==nombre:
                edificio.MostrarPropietariosEd()
    def Superficie(self,nombre):
        for edificio in self.__listaedificios:
            edificio.superficie(nombre)
    def MostrarDep(self,piso):
        for edificio in self.__listaedificios:
            edificio.Piso(piso)
                
        
    def CargarArchivo(self):
            archivo = open("C:/Users/Usuario/Desktop/POO edificios/EdificioNorte.csv", "r", encoding="UTF-8")
            reader = csv.reader(archivo, delimiter = ";")
            xEdificio = None
            next(reader)
            for fila in reader:
                if len(fila) == 7:
                    xEdificio = Edificio(int(fila[0]), fila[2], fila[3], fila[4], int(fila[5]), int(fila[6]))
                    self.AgregarEdificio(xEdificio)

                elif len(fila) == 8 and xEdificio is not None:
                    xDpto = Departamento(int(fila[1]), fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), float(fila[7]))
                    xEdificio.AgregarDepartamento(xDpto)
                else:
                    print(f"Fila inesperada con longitud: {len(fila)}")
                    print(fila)
            print("Se cargaron los edificios y departamentos correctamente")
            archivo.close()
if __name__=='__main__':
    c=Coleccion()
    c.CargarArchivo()
    opcion=0
    while opcion!='5':
        opcion=input('Ingrese 1 para saber la superficie del edificio con su id.\nIngrese 2 si desea saber los propietarios de un edificio por su nombre\nIngrese 3 si desea saber la superficie por nombre de propietario\nIngrese 4 si desea ingresar piso')
        if opcion=='1':
            id=input('Ingrese id')
            c.MostrarSuperficieEdificio(id)
        elif opcion=='2':
            nombre=input('Ingrese nombre edificio')
            c.MostrarProp(nombre)
        elif opcion=='3':
            nombre=input('Ingrese nombre de propietario')
            c.Superficie(nombre)
        elif opcion=='4':
            piso=input('Ingrese piso')
            c.MostrarDep(piso)

    