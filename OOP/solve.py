#3) Создай класс человек. Добавь поля: имя string, оптимальная температура float, коэффициент недовольства float
#4) Добавь в этот класс метод calc_displeasure_value, которая принимает текущую температуру воздуха float и возвращает
#уровень недовольства float. уровень недовольства считается по формуле |оптим. темп. - текущая темп.| *
#коэф. недовольства, где | | - это модуль числа

class Human :
    def __init__(self,name:str, temp: float, disp_level: float):
        self.name = name
        self.temp = temp
        self.disp_level = disp_level


    def calc_disp_value(self, current_temp: float) -> float:
        diff = self.temp - current_temp
        if diff < 0:
            diff = -diff

        return diff * self.disp_level



human1 = Human("Anna", 22.0, 1.5)
human2 = Human("John", 18.0, 0.5)
human3 = Human("Kane", 20.0, 1.2)
human4 = Human("Jeff", 19.5, 1.11)
human5 = Human("Greg", 22.0, 1.5)

#5.1) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает минимальный
#    уровень недовольства среди этих людей

def minimal_disp_level(humans: list[Human], current_temp: float) -> float:
    minimal = None
    for human in humans:
       disp_value = human.calc_disp_value(current_temp)
       if minimal is None or disp_value < minimal:
           minimal = disp_value

    return minimal




#5.2) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает имя человека
#     с минимальным уровнем недовольства
def minimal_disp_name(humans: list[Human], current_temp: float) -> str:
    minimal = None
    minimal_name = None

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value
            minimal_name = human.name

    return minimal_name



#5.3) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает имя человека
#    с минимальным уровнем недовольства и его уровень недовольства
def name_n_disp_lvl(humans: list[Human], current_temp: float) -> tuple[str, float]:
    minimal = None
    minimal_name = None
    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value
            minimal_name = human.name

    return minimal_name, minimal

#print(name_n_disp_lvl(humans= [human1, human2, human3, human4, human5],current_temp=27.0))

#5.4) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает имя человека
#     с минимальным уровнем недовольства. Если таких несколько, вернуть первого встретившегося

def first_minimal_name(humans:list[Human], current_temp: float) -> str:
    minimal = None
    minimal_name = ''
    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value
            minimal_name = human.name
    return minimal_name

print(first_minimal_name(humans = [human1, human2, human3, human4, human5],current_temp=23.0))


#    5.5) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает имя человека
#    с минимальным уровнем недовольства. Если таких несколько, вернуть последнего встретившегося

def last_minimal_name(humans:list[Human], current_temp: float) -> str:
    minimal = None
    minimal_name = None
    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value <= minimal:
            minimal = disp_value
            minimal_name = human.name

    return minimal_name

#print(last_minimal_name(humans= [human1, human2, human3, human4, human5],current_temp=23.0))

#    5.6) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает минимальный
#    уровень недовольства. Если людей с таким уровнем недовольства несколько, то вернуть минимальный уровень недовольства
#   и количество людей с таким уровнем недовольства

def minimal_level_n_count(humans: list[Human], current_temp: float) -> tuple[float| int, float|int]:
    minimal = None
    count = 0
    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value
            count = 1
        elif disp_value == minimal:
            count += 1

    return minimal, count

#print(minimal_level_n_count(humans= [human1, human2, human3, human4, human5],current_temp=23.0))

#5.7) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и удаляет из него людей
#    с максимальным и минимальным уровнем недовольства. Если их несколько, то удалить всех с максимальным и минимальным
#    уровнем недовольства

def delete_minimal_maximal(humans: list[Human], current_temp: float) -> list[Human]:
    minimal = None
    maximal = None

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value

        if maximal is None or disp_value > maximal:
            maximal = disp_value

    result = []
    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if disp_value != minimal and disp_value != maximal:
            result.append(human)
    return result

print(delete_minimal_maximal([human1, human2, human3, human4, human5],current_temp=23.0))
