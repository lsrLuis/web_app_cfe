# encoding: utf-8
import csv
#Tipo,Estado,Ciudad,Colonia,Direccion,Latitud,Longitud,DiasAtencion,HorarioAtencion
#  0    1       2       3       4       5         6         7               8

class Cfe_data:
    data_temp = []

    def __init__(self):
        pass

    def data_read(self, filename):
        with open(filename,"r") as file:
            data = csv.reader(file, dialect='excel')
            for row in data:
               self.data_temp.append(row)

    def data_state(self):
        list_state = []
        for row in self.data_temp:
            state = row[1]
            if state not in list_state:
                list_state.append(state)
        return list_state

    def data_city(self, state):
        list_city = []
        for row in self.data_temp:
            if row[1] == state:
                city = row[2]
                if city not in list_city:
                    list_city.append(row[2])
        return list_city

    def data_cfematicos(self,city):
        list_cfematicos = []
        for row in self.data_temp:
            if row[2] == city:
                dat = row
                if dat not in list_cfematicos:
                    list_cfematicos.append(row)
        return list_cfematicos

