import allure
import pytest
import requests
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
@pytest.mark.parametrize("language", ["eng", "uz", "kz"])
def test_get_experiment(language):
    pass


    with allure.step("Step 1"):
        pass