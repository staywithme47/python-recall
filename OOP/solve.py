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
human5 = Human("Greg", 17.5, 0.75)

def minimal_disp_level(humans: list[Human], current_temp: float) -> float:
    minimal = None
    for human in humans:
       disp_value = human.calc_disp_value(current_temp)
       if minimal is None or disp_value < minimal:
           minimal = disp_value

    return minimal





def minimal_disp_name(humans: list[Human], current_temp: float) -> str:
    minimal = None
    minimal_name = None

    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value
            minimal_name = human.name

    return minimal_name




def name_n_disp_lvl(humans: list[Human], current_temp: float) -> tuple[str, float]:
    minimal = None
    minimal_name = None
    for human in humans:
        disp_value = human.calc_disp_value(current_temp)
        if minimal is None or disp_value < minimal:
            minimal = disp_value
            minimal_name = human.name

    return minimal_name, minimal

print(name_n_disp_lvl(humans= [human1, human2, human3, human4, human5],current_temp=27.0))

