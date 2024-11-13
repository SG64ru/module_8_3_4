class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)



    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        if isinstance(self.vin_number, int) == False:
            raise IncorrectVinNumber("Некорректный диапозон VIN номера")
        # if not 1000000 <= self.vin_number <= 9999999:# Способ 1
        if self.vin_number < 1000000 or self.vin_number > 9999999:# Способ 2
            raise IncorrectVinNumber("Неверный диапозон VIN номера")
        # if self.vin_number < 1000000:#Способ 3
        #     raise IncorrectVinNumber("Неверный диапозон VIN номера")#Способ 3
        # if self.vin_number > 9999999:#Способ 3
        #     raise IncorrectVinNumber("Неверный диапозон VIN номера")#Способ 3

        return True

    def __is_valid_numbers(self, __numbers):
        if isinstance(self.__numbers, str) == False:
            raise  IncorrectCarNumbers("Некорректный тип данных для номера номера")
        if len(__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, message, ):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message




try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')
#
try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')



