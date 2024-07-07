import json
import sys


def get_data_from_file(path:str)-> dict:
    """Получение json данных из файла

    Args:
        path (str): Путь до файла с данными

    Returns:
        dict: Словарь с полученными данными
    """
    with open(path,"r",encoding="utf-8") as file:
        return json.load(file)


def make_report(tests:dict,values:dict,path:str)-> None:
    """генерация отчета на основании входных данных

    Args:
        tests (dict): Данные тестов
        values (dict): данные о прохождении тестов
        path (str): путь до файла с отчетами
    """

    for test in tests["tests"]:
        if  get_test_result(test["id"],values):
            test["value"] = get_test_result(test["id"],values)
        if  "values"  in test.keys(): 
            parse_json_data(test,values)


    if not path.endswith(".json"):
        path = path+"/report.json"

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(tests, file, ensure_ascii=False, indent=4)


def parse_json_data(tests_data:dict,values)->None:
    """Функция разбора json

    Args:
        tests_data (dict): Словарь тестов
        values (dict): данные о прохождении тестов
    """
    for test in tests_data["values"]:
        if get_test_result(test["id"],values):
            test["value"] = get_test_result(test["id"],values)
        if "values" in test.keys():
            parse_json_data(test,values)


def get_test_result(id:str,results:dict)->str:
    """Получение результата теста по ID

    Args:
        id (str): id теста
        results (dict): данные о результатах тестирования

    Returns:
        str: результат тестирования
    """

    for result in results["values"]:
        if result["id"] == id:
            return result["value"]
    return 0
                

    


if __name__ == "__main__":
    if len(sys.argv) !=  4:
        print('Недостаточно аргументов. необходимое кол-во аргументов 3')
        sys.exit(0)
    else:
        try:
            test_data = get_data_from_file(sys.argv[1])
            values_data  = get_data_from_file(sys.argv[2])
            path = sys.argv[3]
            make_report(test_data,values_data,path)
        except FileNotFoundError as e:
            print(f"не удалось прочитать фаил -> {e}")
