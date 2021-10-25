from Domain.entity import Entity

class Rezervare(Entity):
    '''
    Descrie o rezervare.
    '''

    def __init__(self,id_rezervare,nume,clasa,pret,checkin):
        super().__init__(id_rezervare)
        self.__nume = nume
        self.__clasa = clasa
        self.__pret = pret
        self.__checkin = checkin



    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def clasa(self):
        return self.__clasa

    @clasa.setter
    def clasa(self, value):
        self.__clasa = value

    @property
    def pret(self):
        return self.__pret

    @pret.setter
    def pret(self, value):
        self.__pret = value

    @property
    def checkin(self):
        return self.__checkin

    @checkin.setter
    def checkin(self, value):
        self.__checkin = value


    def __str__(self):
        return f'{self.id_entity} - nume:{self.nume}, clasa:{self.clasa}, ' \
               f'pret:{self.pret}; checkin:{self.checkin}'
