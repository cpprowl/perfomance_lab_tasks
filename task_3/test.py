import json
import os

from task_3.task_3 import get_data_from_file, make_report

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

values = {
  "values": [{
    "id": 2,
    "value": "passed"
  }, {
    "id": 41,
    "value": "passed"
  }, {
    "id": 73,
    "value": "passed"
  }, {
    "id": 110,
    "value": "failed"
  }, {
    "id": 122,
    "value": "failed"
  }, {
    "id": 234,
    "value": "passed"
  }, {
    "id": 238,
    "value": "passed"
  }, {
    "id": 345,
    "value": "passed"
  }, {
    "id": 653,
    "value": "passed"
  }, {
    "id": 690,
    "value": "failed"
  }, {
    "id": 5321,
    "value": "passed"
  }, {
    "id": 5322,
    "value": "failed"
  }]
}

report = {
    "tests": [
        {
            "id": 2,
            "title": "Smoke test",
            "value": "passed"
        },
        {
            "id": 41,
            "title": "Debug test",
            "value": "passed"
        },
        {
            "id": 73,
            "title": "Performance test",
            "value": "passed",
            "values": [
                {
                    "id": 345,
                    "title": "Maxperf",
                    "value": "passed",
                    "values": [
                        {
                            "id": 230,
                            "title": "Percent",
                            "values": [
                                {
                                    "id": 234,
                                    "title": "200",
                                    "value": "passed"
                                },
                                {
                                    "id": 653,
                                    "title": "300",
                                    "value": "passed"
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": 110,
                    "title": "Stability test",
                    "value": "failed",
                    "values": [
                        {
                            "id": 261,
                            "title": "Percent",
                            "values": [
                                {
                                    "id": 238,
                                    "title": "160",
                                    "value": "passed"
                                },
                                {
                                    "id": 690,
                                    "title": "240",
                                    "value": "failed"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "id": 122,
            "title": "Security test",
            "value": "failed",
            "values": [
                {
                    "id": 5321,
                    "title": "Confidentiality",
                    "value": "passed"
                },
                {
                    "id": 5322,
                    "title": "Integrity",
                    "value": "failed"
                }
            ]
        }
    ]
}

def test_get_data_from_file():
    """Проверка функции получения данных из файла"""
    assert get_data_from_file(os.path.join(BASE_DIR,"task_3/test_data/values.json")) == values


def test_make_report(tmp_path):
    """Проверка функции создания отчета"""
    test_data = get_data_from_file(os.path.join(BASE_DIR,"task_3/test_data/tests.json"))
    values_data  = get_data_from_file(os.path.join(BASE_DIR,"task_3/test_data/values.json"))
    path = tmp_path / "reports"
    path.mkdir()
    make_report(test_data,values_data,str(path))
    with open(os.path.join(path,"report.json"),"r",encoding="utf-8") as file:
        assert json.load(file) == report
