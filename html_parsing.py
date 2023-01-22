# my_list = [3, 4, 6, 8, 9, 10, 12, 16, 17, 18, 20, 22, 24, 26, 30, 33, 34, 35, 36, 37]  # ignore pages
# for i in my_list:
#     i += 1
#
# import PyPDF2
# import pandas as pd
#
# my_file = open('2023 IT-PDP.pdf', 'rb')
#
# reader = PyPDF2.PdfReader(my_file)
#
# # page = reader.pages[0]
#
# # print(type(page.extract_text()))
# # print(page.extract_text())
#
# parsed_pages = list()
# for i in range(len(reader.pages)):
#     if i in my_list:
#         continue
#     page = reader.pages[i]
#     parsed_page = page.extract_text()
#     parsed_pages.append(parsed_page.split())
#     for i in parsed_pages:
#         print(i)
#     #TODO operations for cleaning data
#
#
# print(parsed_pages)
#

import time

import pandas as pd
from bs4 import BeautifulSoup
import requests
dataa= requests.get('https://auto.ria.com/uk/search/?categories.main.id=1&indexName=auto,order_auto,newauto_search&region.id[0]=10&brand.id[0]=48&model.id[0]=425&size=20') #this
data = requests.get(
                    'https://auto.ria.com/uk/search/?categories.main.id=1&indexName=auto,order_auto,newauto_search&region.id[0]=10&brand.id[0]=48&model.id[0]=425&size=20')
                    'https://auto.ria.com/uk/search/?categories.main.id=1&indexName=auto,order_auto,newauto_search&brand.id[0]=6&year[0].gte=2005&year[0].lte=2023&size=20'



# here we got the response from get request


# TODO write data to file and after that read from this file

# with open('pars_data.html','w', encoding="utf-8") as f:
#     f.write(data.text)


# Created the soup object , converted to data html and passed to our parser
soup = BeautifulSoup(data.text, 'html.parser')
mylinks = soup.find_all("a", {"class": "m-link-ticket"})  # found all links <a> with class
links_list = []



for i in range(len(mylinks)):
    first_id = str(mylinks[i]).find('https')  # found elements to further slice
    second_id = str(mylinks[i]).find('">')  # found elements to further slice
    test = str(mylinks[i])
    links_list.append(test[first_id:second_id])
    # TODO rewrite smartly  -->> links_list.append(mylinks[i])

print(links_list)

"""
<h1 class="head" title="Mercedes-Benz C-Class 2015">Mercedes-Benz C-Class 2015</h1>
<strong class="">22 900 $</strong>
<span class="argument">208 тис.км <span class="point">•</span> 9 міс. тому <span class="size13 boxed">останній зафіксований від 24.03.2022<br>джерело фіксації — дилерське СТО</span></span>

"""

"""
<dl class="unstyle"><dd><div class="mb-10"><dl class="unstyle" id="nais-block"><dd> <span class="bold">Перевірено AUTO.RIA</span> <span class="i-block"><span class="bold">за реєстрами рухомого майна</span> <span data-tooltip="Дата останньої перевірки 08.01.2023. AUTO.RIA перевірив обтяження, пов’язані з авто. Перевірка не включає штрафи та заборони, накладені на власника."><svg class="svg svg_i16_info"><use xlink:href="https://auto.ria.com/uk/auto_mercedes_benz_c_class_33401387.html#i16_info"></use></svg></span></span></dd><dd><svg class="svg svg-match blue"><use xlink:href="https://auto.ria.com/uk/auto_mercedes_benz_c_class_33401387.html#i16_check"></use></svg><span class="label">Тип обтяження</span> <span class="argument"><span>не виявлено</span></span></dd><dd><svg class="svg svg-match blue"><use xlink:href="https://auto.ria.com/uk/auto_mercedes_benz_c_class_33401387.html#i16_check"></use></svg><span class="label">Обмеження відчуження</span> <span class="argument">дозволено відчужувати</span></dd></dl></div><div class="mb-10"><dl class="unstyle"><dd> <span class="bold">Перевірено AUTO.RIA</span> <span class="i-block special-tooltip"><span class="bold">по страховим базам</span> <span data-tooltip="Дата останньої перевірки 06.12.2022 AUTO.RIA перевірив страхові випадки, пов’язані з авто, за базами провідних страхових компаній України.
"><svg class="svg svg_i16_info"><use xlink:href="https://auto.ria.com/uk/auto_mercedes_benz_c_class_33401387.html#i16_info"></use></svg></span></span></dd><dd><svg class="svg svg-match blue"><use xlink:href="https://auto.ria.com/uk/auto_mercedes_benz_c_class_33401387.html#i16_check"></use></svg><span class="label">Наявність страхового випадку</span> <span class="argument">не знайдено</span></dd></dl></div> <span class="bold">Перевірено AUTO.RIA за 15 базами даних</span> <span class="tooltip-vin_code relative"><svg class="svg svg_i16_info" focusable="false"><use xlink:href="https://auto.ria.com/uk/auto_mercedes_benz_c_class_33401387.html#i16_info"></use></svg> <span class="tooltip-view"><span class="boxed">Дата останньої перевірки 07.11.2022</span> <span class="i-block bold mar-bot-10">AUTO.RIA звірив дані по VIN-коду від продавця:</span> <span class="boxed bold">Пробіг</span> <span class="i-block mar-bot-10">Останній пробіг, зафіксований на СТО при сервісному центрі, дилерському центрі, при ремонті чи технічному огляді.</span><span class="boxed bold">ДТП</span> <span class="i-block">Відображаються тільки офіційно зафіксовані випадки ДТП. За відкритими базами даних України, країн Євросоюзу, СНД, США та Канади.</span></span></span></dd><dd><div class="hide">Carvin race report</div><svg class="svg svg-match blue" focusable="false"><use xlink:href="https://auto.ria.com/uk/auto_mercedes_benz_c_class_33401387.html#i16_check"></use></svg> <span class="label">Пробіг перевірено</span> <span class="argument">141 тис.км <span class="point">•</span> 4 роки, 9 міс. тому <span class="size13 boxed">останній зафіксований від 02.04.2018<br>джерело фіксації — архівні дані з офіційного аукціону Copart в США</span></span></dd><dd> <span class="label">Пробіг від продавця</span> <span class="argument">202 тис.км</span></dd><dd><svg class="svg svg-match blue" focusable="false"><use xlink:href="https://auto.ria.com/uk/auto_mercedes_benz_c_class_33401387.html#i16_check"></use></svg><span class="label">ДТП</span> <span class="argument">Зафіксовано ДТП <input class="checked_details" type="checkbox" value="1" name="auction" id="carvin-dtp-info"> <label for="carvin-dtp-info" class="btn-more link open">Деталі</label> <label for="carvin-dtp-info" class="btn-more link close">Закрити</label><br> <span class="i-block text_details">на території США в 2018 році із пошкодженням зовнішнього інтерфейсу</span></span></dd></dl>
"""

all_data = []


def make_df(data_list):
    # TODO save to csv file

    df = pd.DataFrame(data_list, columns=['Car name', 'Car price', 'Miles'])
    df.to_csv('out.csv',index=False)          #dataframe to csv
    print(df)



def parse_one_page(link):
    data2 = requests.get(link)
    soup2 = BeautifulSoup(data2.text, 'html.parser')
    try:

        car_name = soup2.find('h1', {"class": "head"}).text
        car_price = soup2.find('strong', {"class": ""}).text
        miles = soup2.find('span', {'class': 'label'},
                           text='Пробіг перевірено').next_element.next_element.next_element.text
        miles = miles[0:10]
        print(car_name, car_price, miles, sep='||||')
        all_data.append([car_name, car_price, miles])
        return all_data
        # make_df(car_name,car_price,miles)
    except Exception as e:
        print("Exception", e)


start_time = time.time()

for link in links_list:
    parse_one_page(link)

print(make_df(all_data))
print("--- %s seconds ---" % (time.time() - start_time))
# print(test[13].text)        #  Пробіг перевірено Даних про пробіг не виявлено інформація відсутня в базах даних



class Links():
    @classmethod
    def find_links(cls):                 #find our links
        for i in range(len(mylinks)):
            first_id = str(mylinks[i]).find('https')  # found elements to further slice
            second_id = str(mylinks[i]).find('">')  # found elements to further slice
            test = str(mylinks[i])
            links_list.append(test[first_id:second_id])
            return links_list
            # TODO rewrite smartly  -->> links_list.append(mylinks[i]) how, why is this looks like shit?

class Parsing():
    def __init__(self,link):
        self.link=link

    def parse_one_page(self):
        data2 = requests.get(self.link)
        soup2 = BeautifulSoup(data2.text, 'html.parser')
        try:

            car_name = soup2.find('h1', {"class": "head"}).text
            car_price = soup2.find('strong', {"class": ""}).text
            miles = soup2.find('span', {'class': 'label'},
                               text='Пробіг перевірено').next_element.next_element.next_element.text
            miles = miles[0:10]
            print(car_name, car_price, miles, sep='||||')
            all_data.append([car_name, car_price, miles])
            return all_data
            # make_df(car_name,car_price,miles)
        except Exception as e:
            print("Exception", e)


example=Parsing(Links.find_links())

for link in Links.find_links():
    example.parse_one_page()



'''
мало практики - більше практикуватись(статті, гуглити інформацію, дивитись відео, шукати нові бібліотеки, напрямок вибрати)4
більше коментів
погана планіровка коду
погано переглядаю документації
'мєтаюсь'

дз
1) функціонал коду(2-3 фічи
2) закоментити код, переглянути і перед уроком погратись
3) засунути в ооп
4)
'''
