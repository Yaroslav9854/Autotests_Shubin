import requests

url = "https://osdr.nasa.gov/geode-py/ws/api/missions"

def test_get_mission():
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Не смогли получить никаких объектов, возможно ошибка {e}")
        raise
    new_json = response.json()
    missions = new_json.get('data')
    print(missions)
    for mis in missions:
        a = mis.get("mission")
        val = 'https://osdr.nasa.gov/geode-py/ws/api/mission/27'
        if mis.get("mission") == val:
            mis_response = requests.get(val)
            print(mis_response.json())
            print(mis_response.status_code)
            assert mis_response.status_code != 500
    print(response.status_code)
    assert response.status_code == 200