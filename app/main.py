import utils


def run ():
    print('Graph GDP values by country trough years \n Since 1960 - 2023')

    country = input('Type country: ')
    init_year = int(input('Type init year: '))
    final_year = int(input('Type final year: '))
    
    
    if 1960 <= init_year < final_year <= 2023:
        utils.generate_chart(country, init_year, final_year)
    else:
        print("Type valid values, try again")
        print('-*' * 50)
        run()
        


if __name__ == '__main__':
    run()


