# -*- coding: cp1252 -*-
def valorTipoDato(tipo):
    return ['', '', 0, 0.0, False][['string', 'char', 'integer', 'real', 'bool'].index(tipo)]

class Variables():
    lista_variables = {}

    def agregarVariable(self, nombre, tipo):
        if nombre not in self.lista_variables:
            self.lista_variables[nombre] = [tipo, valorTipoDato(tipo)]
        else:
            return 'Error, variable ya declarada.'

    def establecerValor(self, variable, valor):
        if variable in self.lista_variables:
            self.lista_variables[variable][1] = valor
        else:
            return 'Error, no existe la variable.'

    def obtenerValor(self, variable):
        return self.lista_variables[variable][1]

    def tablaVariables(self):
        for i, j in self.lista_variables.items():
            print i, '\t', j[0], '\t', j[1]
