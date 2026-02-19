import requests

url = "https://osdr.nasa.gov/geode-py/ws/api/subjects"


def test_get_subject():
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Не смогли получить объекты, ошибка {e}")
        raise
    my_json = response.json()
    subjects = my_json.get('data')
    for subj in subjects:
        val = 'https://osdr.nasa.gov/geode-py/ws/api/subject/195'
        if subj.get("subject") == val:
            subj_response = requests.get(val)
            print(subj_response.json())
            print(subj_response.status_code)
            assert subj_response.status_code != 500
    print(response.status_code)
    assert response.status_code == 200