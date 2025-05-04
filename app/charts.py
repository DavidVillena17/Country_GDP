import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, country):
    fig, ax = plt.subplots()
    plt.title(country+"'s GDP")
    plt.xlabel('Years')
    plt.ylabel('GDP (Dollars)')
    ax.bar(labels, values)
    plt.grid(True)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['a','b','c']
    values = [1,2,3]