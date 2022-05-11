import abc
import json
from variable import FILE_STORAGE



class Cassette:
    def __init__(self, code, par):
        self.code = f'RCL_04_0{code}_'
        self.par = par
        # self.par = model

    @abc.abstractmethod
    def get_qrcode(self):
        pass


class AC(Cassette):

    def get_qrcode(self):
        return f'{self.code}0000'


class Denomination(Cassette):

    def get_qrcode(self):
        return f'{self.code}{self.par}'


class CassetteFactory:
    types = {
        'ac': AC,
        'dm': Denomination,

    }

    @classmethod
    def create(cls, type_, qr, par):
        return cls.types[type_](qr, par)


class Storage:
    auto_id = 0

    def __init__(self, request: dict):
        self.id = Storage.auto_id
        Storage.auto_id += 1
        self.params = request['post_params']
        self.name = request['name']
        self.storage = {}

    def create_cassette_qr(self):
        qr, par = self.params['qr_code'], self.params['par']
        if par == 'ac':
            cassette = CassetteFactory.create('ac', qr, par)
        else:
            cassette = CassetteFactory.create('dm', qr, par)

        return cassette.get_qrcode()

    def add_storage(self):

        self.params['qr_code'] = self.create_cassette_qr()
        self.params['name'] = self.name
        print('GFH', self.params)
        with open(FILE_STORAGE) as f:
            data = json.load(f)
            self.id = len(data)
            cassette = {self.id: self.params}
            data.update(cassette)
        with open(FILE_STORAGE, 'w') as f:
            json.dump(data, f, indent=4)
