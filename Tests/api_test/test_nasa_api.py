import allure
import pytest
import requests
# import framework.helpers import some_help
a = 2

@allure.id("1")
@allure.feature("NASA API")
@allure.label("API test")
@allure.title("Получение эксперимента от nasa_api")
@allure.description("Тест проверяет что в ручке экспериментом приходят эксперименты")
@allure.testcase("some_test_case_url")
@pytest.mark.nasa_tests
# @pytest.mark.skipif(a = 2, reason='Пропустить тест если переменная a = 2')
# @pytest.mark.skip(reason="Метод получение экспериментов не работает.")
# @pytest.mark.parametrize("language", ["eng", "uz", "kz"])


def test_get_experiment():
    url = "https://osdr.nasa.gov/geode-py/ws/api/vehicles"
    Vehicle = {
        "id": 4,
        "name": "Discovery",
        "status": "available"
    }


    response = requests.get("https://osdr.nasa.gov/geode-py/ws/api/vehicle/Discovery")
    print (response.status_code)  # 200
    print (response.json())#["name"] == "Discovery"
    try:
        response = requests.get("https://osdr.nasa.gov/geode-py/ws/api/vehicle/Discovery", timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", e)

    with allure.step("Step 1"):
        pass