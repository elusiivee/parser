import requests
import json


class Writing:

    @classmethod
    def write_data_to_file(cls, data):
        with open('data.json', 'w') as f:
            f.write(json.dumps(data))

    @classmethod
    def write_car_to_file(cls, data):
        with open('car.json', 'w') as f:
            f.write(json.dumps(data))


class Link:
    # https://developers.ria.com/auto/search?api_key=gGAx2DB74m3qaRoNPf5elaWuC3cdUCaZgP8h1pXd&category_id=1&marka_id=2/
    # https://developers.ria.com/auto/info?api_key=gGAx2DB74m3qaRoNPf5elaWuC3cdUCaZgP8h1pXd&auto_id={auto_id}

    def __init__(self, car):
        self._DOMAIN = f'https://developers.ria.com/auto/search?'
        self.car = car  # Composition
        self._middle_url = self.build_middle_url()
        self.API_KEY = 'gGAx2DB74m3qaRoNPf5elaWuC3cdUCaZgP8h1pXd'
        self.__full_link = self.full_link

    @property
    def full_link(self):
        return self._DOMAIN + self.bulid_request_api_key() + self._middle_url

    def bulid_request_api_key(self):
        return f'api_key={self.API_KEY}'

    def build_middle_url(self):
        car_1 = self.car.all_cars_to_str()
        return car_1


class LinkCar(Link):

    def __init__(self, car_link, car):
        self.car_link = car_link
        print(ParsingData.allrequests(car_link.full_link)['result']['search_result']['ids'])  # це ужас
        super().__init__(car)

        self._DOMAIN = f'https://developers.ria.com/auto/info?'

    # оно как обьект воспринимает его не как строку, А КАК КЛАСС
    @property
    def full_link(self):
        return self._DOMAIN + self.bulid_request_api_key() + self._middle_url

    def build_middle_url(self):
        car_1 = self.car.car_id_to_str()
        return car_1


class ParsingData:

    @classmethod  # is this right
    def allrequests(cls, link):
        data = requests.get(link)
        return data.json()

    @classmethod
    def idrequest(cls, link):
        data = requests.get(link)
        return data.json()


class ProcessData:
    def __init__(self, car_link, link_id):
        self.jsonAllFile = ParsingData.allrequests(car_link.full_link)  # data.json
        self.jsonFile = ParsingData.idrequest(link_id.full_link)  # car.json#s

    def get_location(self):
        jsonDataLocation = self.jsonFile['locationCityName']
        print(f'City: {jsonDataLocation}')

    def get_price(self):
        jsonPriceUSD = self.jsonFile['USD']
        jsonPriceUAH = self.jsonFile['UAH']
        jsonPriceEUR = self.jsonFile['EUR']
        print(f'USD: {jsonPriceUSD}\n'
              f'UAH: {jsonPriceUAH}\n'
              f'EUR: {jsonPriceEUR}')

    def get_data(self):
        jsonData = self.jsonFile['addDate']
        print(f'Data: {jsonData}')

    def get_race(self):
        jsonRace = self.jsonFile['autoData']['race']
        print(f'Race: {jsonRace}')

    def get_bodyId(self):
        jsonBodyId = self.jsonFile['autoData']['bodyId']
        print(f'Body id: {jsonBodyId}')

    def get_year(self):
        jsonYear = self.jsonFile['autoData']['year']
        print(f'Year: {jsonYear}')

    def get_description(self):
        jsonDescription = self.jsonFile['autoData']['description']
        print(f'Description: {jsonDescription}')

    def get_active(self):
        jsonActive = self.jsonFile['autoData']['active']
        print(f'Active: {jsonActive}')

    def get_gearboxName(self):
        jsonGearBoxName = self.jsonFile['autoData']['gearboxName']
        print(f'GearboxName: {jsonGearBoxName}')

    def get_linkToView(self):
        jsonlinkToView = self.jsonFile['linkToView']
        print(f'Link to view: {jsonlinkToView}')

    def get_car_id(self):
        jsonCarId = self.jsonAllFile['result']['search_result']['ids']
        print(f'Car id : {jsonCarId}')
        return jsonCarId


class Car:

    def __init__(self):
        self.category_id = None
        self.car_brand = None
        self.auto_id = None
        self.initialise_data()      #TODO переделать на тг бота

    def initialise_data(self):
        #TODO получить данные с ввода пользователя в тг боте и записать их в переменные
        self.category_id = int(input('Input category_id: '))
        self.car_brand = int(input('Input car_brand: '))

    def all_cars_to_str(self):
        return f"&category_id={self.category_id}&car_brand={self.car_brand}/"

    def car_id_to_str(self):
        self.auto_id = int(input('Input auto_id: '))
        return f'&auto_id={self.auto_id}'


# we created an object of the class Car and passed it to the Link class
car = Car()
link = Link(car)
link_id = LinkCar(link, car)

prdt1 = ProcessData(link, link_id)
prdt = ProcessData(link, link_id)  # link_id = Link ALL#

print(link.full_link)
print(link_id.full_link)

data = ParsingData.allrequests(link.full_link)

Writing.write_data_to_file(data)
car_data = ParsingData.idrequest(link_id.full_link)

Writing.write_car_to_file(car_data)
prdt.get_location()
prdt.get_data()
prdt.get_price()
prdt.get_race()
prdt.get_bodyId()
prdt.get_year()
prdt.get_description()
prdt.get_active()
prdt.get_gearboxName()
prdt.get_linkToView()

'''
1) логіка по файлам
2) коментарії
3) general rev cod
4) уьрати двойний вивід                               
5) телеграм бот і прикрутити логіку 
6) library telebot dont aiogram
7) закінчити проект


'''

'''
1) Убрати двойний ввід марки і категорії не виходить бо потрібно мені дві силки зробити, а класи то наслідуються

'''
