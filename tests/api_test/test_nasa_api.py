import allure
import pytest
import requests


@allure.id("1")
@allure.feature("NASA API")
@allure.label("API test")
@allure.title("Получение эксперимента от nasa_api")
@allure.description("Тест проверяет что в ручке экспериментом приходят эксперименты")
@allure.testcase("some_test_case_url")
@pytest.mark.nasa_tests

class TestVehicleExistence:
    BASE_URL = "https://osdr.nasa.gov/geode-py/ws/api/vehicles"
    TIMEOUT = 10

    def test_get_experiment(self):

        response = requests.get("https://osdr.nasa.gov/geode-py/ws/api/vehicle/Foton")
        assert response.status_code == 200
        print (response.status_code)  # 200
        print (response.json())#["name"] == "Foton"
        try:
            response = requests.get("https://osdr.nasa.gov/geode-py/ws/api/vehicle/Foton", timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Ошибка запроса:", e)
            raise ValueError("Данный тест был прерван по причине неправильного написанного названия транспортного средства")

        with allure.step("Step 1"):
            pass

    def check_vehicle_exists(self, vehicles_data, vehicle_name):
        """Проверяет указанное транспортное средство"""
        if isinstance(vehicles_data, list):
            return any(
                vehicle.get('name', '').lower() == vehicle_name.lower()
                for vehicle in vehicles_data
            )
        elif isinstance(vehicles_data, dict):
            return vehicles_data.get('name', '').lower() == vehicle_name.lower()
        return False

