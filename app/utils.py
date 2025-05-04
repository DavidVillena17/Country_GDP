
def get_entity(country_dic):
    entity_dic = {
        '2015' : country_dic['2015'],
        '2016' : country_dic['2016'],
        '2017' : country_dic['2017'],
        '2018' : country_dic['2018'],
        '2019' : country_dic['2019'],
        '2020' : country_dic['2020'],
        '2021' : country_dic['2021'],
        '2022' : country_dic['2022'],
        '2023' : country_dic['2023'],
    }
    labels = entity_dic.keys()
    values = entity_dic.values()
    return labels, values

def gdp_by_country(data, country):
    result = list(filter(lambda item: item['Country Name'] == country, data))
    return result
