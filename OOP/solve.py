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

#print(first_minimal_name(humans = [human1, human2, human3, human4, human5],current_temp=23.0))


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

#print(delete_minimal_maximal([human1, human2, human3, human4, human5],current_temp=23.0))


#5.8) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает уровень
#    недовольства, который является минимальным без учета текущего мин. уровня недовольства (текущих минимальных уровней
#   недовольства, если их несколько)

def minimal_wo_current(humans: list[Human], current_temp: float) -> float|int:
    minimal = None
    next_minimal = None

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if disp_value != minimal:
            if next_minimal is None or disp_value < next_minimal:
                next_minimal = disp_value

    return next_minimal

print(minimal_wo_current([human1, human2, human3, human4, human5],current_temp=23.0))

#    5.9) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает суммарный
#    уровень недовольства, без учета минимального (минимальных если их несколько)

def sum_wo_minimal(humans: list[Human], current_temp: float) -> float|int:
    total = 0
    minimal = None

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if disp_value != minimal:
            total += disp_value

    return total

print(sum_wo_minimal([human1, human2, human3, human4, human5],current_temp=23.0))


#5.10) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает среднее
#    значение уровня недовольства, без учета максимального и минимального (максимальных и минимальных, если их несколько)

def avg_disp(humans: list[Human], current_temp: float) -> float|int:
    minimal = None
    maximal = None
    total = 0
    count = 0

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value

        if maximal is None or disp_value > maximal:
            maximal = disp_value

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if disp_value != minimal and disp_value != maximal:
            total += disp_value
            count += 1

    if count == 0:
        return 0.0

    return total / count

print(avg_disp([human1, human2, human3, human4, human5],current_temp=23.0))

#5.11) написать функцию, которая принимает массив людей и текущую температуру воздуха (float) и возвращает
#     имя человека, уровень недовольства которого ближе всего к среднему. Если таких несколько, вернуть индекс
#    первого встретившегося

def closest_to_avg(humans: list[Human], current_temp: float) -> str:
    total = 0
    count = 0

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        total += disp_value
        count += 1
    avg = total / count
    best_diff = 0
    best_name = ''
    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        diff = disp_value - avg
        if diff < 0:
            diff = -diff
        if diff < best_diff:
            best_diff = diff
            best_name = human.name

    return best_name


print(closest_to_avg([human1, human2, human3, human4, human5],current_temp=23.0))
