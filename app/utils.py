import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

path = 'data/new_data.csv' 

def get_data (country, init_year, final_year):
    df = pd.read_csv(path, index_col='Year')
    df = df.loc[init_year:final_year, country]
    return df/1000000000                        ##Billion Dollars

def generate_chart(country, init_year, final_year):
    gd = gridspec.GridSpec(2,2, height_ratios = [2,1], width_ratios = [1,2])  
    fig = plt.figure(figsize = (10,8))
    data = get_data(country, init_year, final_year)
    years = data.index.astype(str).tolist()
    values = data.values
    
    #Primer subplot 
    ax1 = fig.add_subplot(gd[0,:])
    ax1.bar(years, values, color='salmon', alpha = 0.6)
    ax1.set_xticks(years)
    ax1.set_xticklabels(years, rotation = 45)
    ax1.set_title(country+"'s GDP (Billion Dollars)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('GDP (Billion Dollars)')

    #Segundo subplot
    ax2 = fig.add_subplot(gd[1,:])
    ax2.plot(years, values, marker='o', linestyle='-', color='cyan', label='Anual GDP')
    ax2.set_xticks(years)
    ax2.set_xticklabels(years, rotation = 45)
    ax2.set_title(country+"'s Tendency (GDP - Billion Dollars)")
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Tendency')

    plt.tight_layout()

    plt.show()
    
