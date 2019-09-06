class Blog(object):
    def __init__(self,nom,des,sex):
        self.nombre =nom
        self.descripcion =des
        self.sexo = sex
        self.sexo_nombres=('Mujer','Hombre')
    def get_sexo(self):
        return self.sexo_nombres[self.sexo]

class Blog2(object):
    def __init__(self,nom,des,sex):
        self.nombre =nom
        self.descripcion =des
        self.sexo = sex
        self.sexo_nombres=('Mujer','Hombre')
    def get_sexo(self):
        return self.sexo_nombres[self.sexo]        

