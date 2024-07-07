import sys


def circle_array(m:int , n:int) -> list:
    """Calculate circle length path

    Args:
        m (int): length of array
        n (int): length of step

    Returns:
        int: iteration count
    """

    array = [i for i in range(1,m+1)]
    if n > len(array):
        print("Длинна шага не может быть больше длинны массива")
        return None
    if n == len(array):
        
        return ["1"]
    current = 0
    path = []
    while True :
        path.append(str(array[current]))
        current = (current + n - 1) % m
       
        if current == 0:
            break
    return path


if __name__ == "__main__":
    if len(sys.argv) !=  3:
        print('Недостаточно аргументов. необходимое кол-во аргументов 2')
        sys.exit(0)
    else:
        result  = circle_array(int(sys.argv[1]),int(sys.argv[2]))
        print(f"Полученный путь: {''.join(result)}")
    


    

