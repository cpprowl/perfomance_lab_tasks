import sys


def get_data_from_file(path:str)->list:
    """Чтение данных из файла

    Args:
        path (str): путь до файла

    Returns:
        list: данный из файла
    """
    with open(path, "r") as file:
        return file.readlines()


def calcultate_arithmetic_mean(digits:list)->int:
    """Подсчет среднего арифметического суммы чисел в списке

    Args:
        digits (list): список чисел

    Returns:
        int: среднее арифметическое
    """
    summ = 0
    for item in digits:
        summ+=abs(int(item))

    return summ // len(digits)


def calculate_steps(digits:list) -> int:
    """Подсчет шагов, необходимых для приведения всех элементов списка к одному числу

    Args:
        digits (list): список чисел

    Returns:
        int: Кол-во шагов
    """
    steps = 0
    a_m = calcultate_arithmetic_mean(digits)
    for item in digits:
        item = abs(int(item))
        if item == a_m:
            continue
        while item != a_m:
            if item > a_m:
                item-=1
                steps+=1
                continue
            if item < a_m:
                item+=1
                steps+=1
                continue
    return steps


if __name__ == "__main__":
    if len(sys.argv) !=  2:
        print('Недостаточно аргументов. Необходимое кол-во аргументов 1')
        sys.exit(0)
    else:
        try:
            file_data = get_data_from_file(sys.argv[1])
            print(f"Кол-во шагов {calculate_steps(file_data)}")
        except FileNotFoundError as e :
            print(f"не удалось прочитать фаил -> {e}")

      




