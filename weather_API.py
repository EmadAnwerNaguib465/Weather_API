import requests
def display_weather(data_dic):
    for key, value in data_dic.items():
        print(f'{key.title()} : {value}')

def get_weather_data(city):
    my_key = 'aa536c18d1f33acb84dae64136ec3c35'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={my_key}'
    response = requests.get(url)
    try:
        assert response.status_code == 200
    except:
        print('Error')

    else:
        data = response.json()
        print(f'## Weather in {data["name"]} ##')
        return display_weather(data['main'])

def main():
    while True:
        city = input('Enter city name : ')
        get_weather_data(city)
        again = input('Do you want to check another city? (y/n) : ')
        if again.lower() == 'n':
            print('Bye!')
            break
        


if __name__ == '__main__':
    main()