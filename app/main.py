import charts
import utils
import read_csv

#Use your path of data
path = '/Users/DavidVillena/Documents/Personal/Proyectos/Mis proyectos/Country_GDP/data_gdp.csv'

def run ():
    data = read_csv.read_csv(path)
    country = entity = input('Type country --> ')
    result = utils.gdp_by_country(data, country)

    if len(result)>0:
        country = result[0]
        labels, values = utils.get_entity(country)
        charts.generate_bar_chart(labels, values, entity)


if __name__ == '__main__':
    run()
