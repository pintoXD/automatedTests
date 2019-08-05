import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from get_batlvl import *
import time
import statistics
import numpy as np

def tiraMedia():
    aux = []
    # aux = [getBatVoltage()]
    # print(aux)

    for i in range(100):
        print("I = ", i)

        aux = aux + [getBatVoltage()]
        time.sleep(0.2)


    print("Media is: ", statistics.mean(aux))
    print("Standard deviation: ", statistics.stdev(aux))

    print("Rounded Media is: ", round(statistics.mean(aux), 3))
    print("Rounded Standard deviation: ", round(statistics.stdev(aux), 3))

def polinomio():

    # np.random.seed(0)
    # x = 2 - 3 * np.random.normal(0, 1, 20)
    # y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)


    x = [2220, 2251, 2281, 2312, 2344, 2374, 2405, 2436, 2466]
    y = [3.6, 3.65, 3.7, 3.75, 3.8, 3.85, 3.9, 3.95, 4]

    # transforming the data to include another axis
    # x = x[:, np.newaxis]
    # y = y[:, np.newaxis]

    # model = LinearRegression()
    # model.fit(x, y)
    # y_pred = model.predict(x)

    plt.scatter(x, y, s=10)
    plt.plot(x, y, color='r')
    plt.show()



def main():
    tiraMedia()
    # polinomio()




if __name__ == "__main__":
  main()
