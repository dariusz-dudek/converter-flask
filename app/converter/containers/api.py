from litex.regon import REGONAPI
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class RegonApi:
    def __init__(self, nip: str):
        api = REGONAPI(getenv('API_REGONAPI'))
        api.login(getenv('API_LOGIN'))
        self.data = api.search(nip=nip)

    def get_regon(self):
        return self.data[0].Regon

    def get_name(self):
        return self.data[0].Nazwa

    def get_city_name(self):
        return self.data[0].Miejscowosc

    def get_postal_code(self):
        return self.data[0].KodPocztowy

    def get_street_and_number(self):
        return f'{self.data[0].Ulica} {self.data[0].NrNieruchomosci}' \
               f'{f"/{self.data[0].NrLokalu}" if not self.data[0].NrLokalu == "" else ""}'

    @staticmethod
    def get_country_code():
        return 'PL'
