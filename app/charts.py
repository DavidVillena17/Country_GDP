import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, country):
    fig, ax = plt.subplots()
    plt.title(country+"'s GDP")
    #plt.axis(['2014','2023',0,107000000000000])
    plt.xlabel('Years')
    plt.ylabel('Million of dollars')
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['a','b','c']
    values = [1,2,3]