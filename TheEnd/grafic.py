import matplotlib.pyplot as plt

potato_price = [45, 35,35,45,40,35,40,40,40]
cabbage_price = [50,30,30,45,40,35,40,40,40]
onion_price = [70,50,45,60,50,45,60,50,60]
year = ["02.11.2016","02.11.2016","02.11.2016", "14.11.2016","14.11.2016","14.11.2016","22.11.2016","22.11.2016","22.11.2016" ]

plt.plot(year,potato_price,label = "Картопля")
plt.plot(year,cabbage_price,label = "капуста")
plt.plot(year,onion_price,label = "Цибуля")
plt.xlabel("Дата")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

def showplot():
    plt.show()