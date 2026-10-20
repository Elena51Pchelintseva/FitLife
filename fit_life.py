WATER_PER_KG = 30
ML_IN_LITER = 1000
user_name = input('Как вас зовут?')
# Приветствие
print(f'Привет, {user_name}!')
user_age = int(input('Сколько Вам лет?'))

user_weight = float(input('Сколько вы весите? (кг)'))
user_height = float(input(
    'Ваш рост? (м)(Введите ваш рост в метрах, используя точку)'))

bmi = user_weight / (user_height ** 2)  # Расчёт ИМT
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITER

# Вывод красивого результата
print(f'Отчёт для пользователя: {user_name}({user_age} г.)')
print(f'Ваш индекс массы тела: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {round(water_l, 1)}л. в день')

print("Расчет окончен. Будьте здоровы!")
