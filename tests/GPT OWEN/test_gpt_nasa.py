import allure
import pytest
import requests


@allure.id("1")
@allure.feature("NASA API")
@allure.label("API test")
@allure.title("Проверка наличия транспортного средства в OSDR API")
@allure.description("Тест проверяет существует ли указанное транспортное средство в API")
@pytest.mark.gpt_nasa_tests
class TestVehicleExistence:
    BASE_URL = "https://osdr.nasa.gov/geode-py/ws/api/vehicles"
    TIMEOUT = 10

    @allure.step("Получить список всех транспортных средств")
    def get_all_vehicles(self):
        """Получает список всех доступных транспортных средств"""
        response = requests.get(self.BASE_URL, timeout=self.TIMEOUT)
        response.raise_for_status()
        return response.json()

    @allure.step("Проверить наличие транспортного средства: {vehicle_name}")
    def check_vehicle_exists(self, vehicles_data, vehicle_name):
        """Проверяет是否存在 указанное транспортное средство"""
        if isinstance(vehicles_data, list):
            return any(
                vehicle.get('name', '').lower() == vehicle_name.lower()
                for vehicle in vehicles_data
            )
        elif isinstance(vehicles_data, dict):
            return vehicles_data.get('name', '').lower() == vehicle_name.lower()
        return False

    def test_vehicle_discovery_exists(self):
        """Тест: транспортное средство Discovery должно существовать"""
        with allure.step("Запрос к API транспортных средств"):
            vehicles = self.get_all_vehicles()

        with allure.step("Проверка наличия Discovery"):
            exists = self.check_vehicle_exists(vehicles, "Discovery")

        with allure.step("Валидация результата"):
            assert exists, "Транспортное средство 'Discovery' не найдено в API"
            allure.attach.body(
                f"Найдено транспортных средств: {len(vehicles) if isinstance(vehicles, list) else 1}",
                name="Статистика",
                attachment_type=allure.attachment_type.TEXT
            )

    @pytest.mark.parametrize("vehicle_name,should_exist", [
        ("Discovery", True),
        ("Endeavour", True),
        ("NonExistentVehicle123", False),
    ])
    def test_vehicle_existence_parametrized(self, vehicle_name, should_exist):
        """Параметризированный тест для проверки разных транспортных средств"""
        vehicles = self.get_all_vehicles()
        exists = self.check_vehicle_exists(vehicles, vehicle_name)

        if should_exist:
            assert exists, f"Транспортное средство '{vehicle_name}' должно существовать"
        else:
            assert not exists, f"Транспортное средство '{vehicle_name}' не должно существовать"

    def test_api_response_structure(self):
        """Тест: проверка структуры ответа API"""
        response = requests.get(self.BASE_URL, timeout=self.TIMEOUT)

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

        with allure.step("Проверка формата ответа"):
            data = response.json()
            assert data is not None, "Ответ API не должен быть пустым"
            assert isinstance(data, (list, dict)), "Ответ должен быть списком или объектом"


# Дополнительно: фикстуры для переиспользования
@pytest.fixture(scope="module")
def nasa_vehicles_data():
    """Фикстура для получения данных о транспортных средствах"""
    response = requests.get(
        "https://osdr.nasa.gov/geode-py/ws/api/vehicles",
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def test_with_fixture(nasa_vehicles_data):
    """Пример использования фикстуры"""
    assert nasa_vehicles_data is not None