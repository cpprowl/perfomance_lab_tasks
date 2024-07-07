import sys
from math import sqrt


def get_circle_data(path:str)->dict:
    """Получение данных об окружности из файла"""
    with open(path, "r") as file:
        circle = {}
        data = file.readlines()
        circle["center"] = data[0].rstrip()
        circle["radius"] = data[1].rstrip()
        return circle

def get_points_data(path:str)->list:
    """Получение точек из файла"""
    with open(path, "r") as file:
        points = []
        for point in file.readlines():
            points.append(point.rstrip())
        return points

def calculate_point_position(g:int, f:int, r:int,x:int,y:int) -> int:
    """Вычисление позиции точки отностительно окружности"""
    distanse = sqrt(abs(x-g)) + sqrt(abs(y-f))
    if sqrt(r) == distanse:
        return 0
    if sqrt(r) > distanse:
        return 1
    if sqrt(r) < distanse:
        return 2 
    




if __name__ == "__main__":
    circle_data = {}
    points = []
    if len(sys.argv) !=  3:
        print('Недостаточно аргументов. необходимое кол-во аргументов 2')
        sys.exit(0)
    else:
        try:
            circle_data = get_circle_data(sys.argv[1])
            points = get_points_data(sys.argv[2])
            gx = int(circle_data["center"].split(" ")[0])
            gy = int(circle_data["center"].split(" ")[1])
            r = int(circle_data["radius"])
            for point in points:
                x = int(point.split(" ")[0])
                y = int(point.split(" ")[1])
                print(f"{calculate_point_position(gx,gy,r,x,y)}")
        except (FileNotFoundError, IndexError) as e:
            print(f"Не удалось получить данные из файла -> {e}")



