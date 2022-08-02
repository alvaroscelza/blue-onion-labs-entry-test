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
                satellite_id=launch_data['id'],
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
                                              .where(Launch.satellite_id == satellite_id)
                                              .where(Launch.creation_date == time)).first()
        return satellite_positions


def main():
    """
    Allows to populate the database with data from
    https://raw.githubusercontent.com/BlueOnionLabs/api-spacex-backend/master/starlink_historical_data.json.
    Allows to print a satellite position given its id and a specific time. If no position is found for that satellite at
    that time, then 'None' is printed.
    Command to run: `python main.py <satellite_id> <datetime> [--populate-data]`
    Example populating data: `python main.py 5eed770f096e59000698560d 2020-10-13T04:16:08 --populate-data`
    Example without populating data: `python main.py 5eed770f096e59000698560d 2020-10-13T04:16:08`

    :param satellite_id: the id of the wanted satellite.
    :param datetime: the specific datetime at which we want the satellite position.
    :param --populate-data: (optional) this enables data population of the database. It is necessary to have a working
    internet connection for this. Data is fetched from the data url, processed (only certain parameters are used) and
    stored in database. this is required the first time you run the app or your database will be empty (without data
    or tables), and the program will crash.

    :return: void.

    No parameters checks were programmed, if one or both of the required params is missing, the program will crash.
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
