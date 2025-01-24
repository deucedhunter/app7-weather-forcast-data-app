import requests
API_KEY = "d0b9bf2ee14fafbe3a3ccc4e3e66a46d"
def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    nr_values = 8 * forecast_days
    filter_data = filter_data[:nr_values]
    return filter_data


if __name__=="__main__":
    print(get_data(place="Tokyo", forecast_days=3))