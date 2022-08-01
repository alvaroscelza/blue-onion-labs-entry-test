import json
import sys

import requests as requests
from sqlalchemy import create_engine, select
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


def get_satellite_last_known_position(satellite_id, time):
    engine = create_engine("postgresql+psycopg2://docker:docker@localhost:5432/docker")
    with Session(engine) as session:
        satellite_positions = session.execute(select(Launch)
                                              .where(Launch.launch_id == satellite_id)
                                              .where(Launch.creation_date == time)).first()
        return satellite_positions


def main():
    """
    - Run `python main.py` to run the code.
    - Pass the satellite id and a time T as parameters: `python main.py 5eed7714096e59000698563c 2020-08-29T04:46:09`. Be
    mindful: I didn't program any checks on these parameters, if you miss one, both or change their order the program will
    crash.
    - Use the argument '--populate-data' to fetch data from your json file and insert it into the database, this is required
    the first time you run the app or your database will be empty (without data or tables), and the program will crash.
    This parameter must always be at the end of the command, or the program will crash:
    `python main.py 5eed7714096e59000698563c 2020-08-29T04:46:09 --populate-data`
    """
    arguments = sys.argv
    if '--populate-data' in arguments:
        url = 'https://raw.githubusercontent.com/BlueOnionLabs/api-spacex-backend/master/starlink_historical_data.json'
        response = requests.get(url)
        launches = json.loads(response.text)
        launches_relevant_data = get_relevant_data(launches)
        insert_launches_into_database(launches_relevant_data)
    satellite_id = arguments[1]
    time = arguments[2]
    last_known_position = get_satellite_last_known_position(satellite_id, time)
    print(last_known_position)


if __name__ == '__main__':
    main()
