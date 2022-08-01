import json

import requests as requests
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from launch import Launch


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


def insert_launches_into_database(launches_relevant_data):
    engine = create_engine("postgresql+psycopg2://docker:docker@localhost:5432/docker")
    Launch.metadata.create_all(engine)
    with Session(engine) as session:
        for launch_data in launches_relevant_data:
            launch = Launch(
                launch_id=launch_data['id'],
                creation_date=launch_data['creation_date'],
                longitude=launch_data['longitude'],
                latitude=launch_data['latitude']
            )
            session.add_all([launch])
            session.commit()


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/BlueOnionLabs/api-spacex-backend/master/starlink_historical_data.json'
    response = requests.get(url)
    launches = json.loads(response.text)
    launches_relevant_data = get_relevant_data(launches)
    insert_launches_into_database(launches_relevant_data)
