

import matplotlib.pyplot as plt

def barChart(labels:list, values:list):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def pieChart(labels:list, values:list):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.show()


