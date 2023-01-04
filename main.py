sex = input("Введите ваш пол: ")
weigth = int(input("Введите свой вес в кг: "))
heigth = int(input("Введите свой рост в см: "))
age = int(input("Введите свой возраст: "))
if sex == "женский":
    result_w = round((weigth*10) + (6.25*heigth) + (age*5) - 161)
    print("Ваша норма ", result_w, "ккал")
else:
    result_m = round((weigth*10) + (6.25*heigth) + (age*5) + 5)
    print("Ваша норма ", result_m, "ккал")


