import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C"]
    Values = [20, 30, 50]

    fig, ax = plt.subplots()
    ax.pie(Values, labels=labels)
    plt.savefig("pie.png")
    plt.close()







