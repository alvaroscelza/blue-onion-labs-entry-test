import requests as requests


def get_relevant_data(launches):
    relevant_data = []
    for launch in launches:
        new_launch = {
            'creation_date': launch['spaceTrack']['CREATION_DATE'],
            'longitude': launch['longitude'],
            'latitude': launch['latitude'],
            'id': launch['id']
        }
        relevant_data.append(new_launch)
    return relevant_data


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/BlueOnionLabs/api-spacex-backend/master/starlink_historical_data.json'
    response = requests.get(url)
    launches = response.text
    launches_relevant_data = get_relevant_data(launches)
