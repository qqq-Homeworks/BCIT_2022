import requests
import matplotlib.pyplot as plt


def main():
    n = 50
    r = requests.get('http://127.0.0.1:5000/' + n.__str__())
    listq = list(r.json())
    print(listq)
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()


if __name__ == "__main__":
    main()
