import json
import sys

import requests as requests
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from satellite_position import SatellitePosition


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


def insert_positions_into_database(positions_relevant_data):
    engine = create_engine("postgresql+psycopg2://docker:docker@localhost:5432/docker")
    SatellitePosition.metadata.create_all(engine)
    with Session(engine) as session:
        for position_data in positions_relevant_data:
            launch = SatellitePosition(
                satellite_id=position_data['id'],
                creation_date=position_data['creation_date'],
                longitude=position_data['longitude'],
                latitude=position_data['latitude']
            )
            session.add_all([launch])
            session.commit()


def get_satellite_last_known_position(satellite_id, time):
    engine = create_engine("postgresql+psycopg2://docker:docker@localhost:5432/docker")
    with Session(engine) as session:
        return session.execute(select(SatellitePosition)
                               .where(SatellitePosition.satellite_id == satellite_id)
                               .where(SatellitePosition.creation_date == time)).first()


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
        positions = json.loads(response.text)
        positions_relevant_data = get_relevant_data(positions)
        insert_positions_into_database(positions_relevant_data)
    satellite_id = arguments[1]
    time = arguments[2]
    last_known_position = get_satellite_last_known_position(satellite_id, time)
    print(last_known_position)


if __name__ == '__main__':
    main()
