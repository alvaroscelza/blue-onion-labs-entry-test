import sys

from haversine import haversine
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from satellite_position import SatellitePosition


def get_all_satellite_positions(time):
    engine = create_engine("postgresql+psycopg2://docker:docker@localhost:5432/docker")
    SatellitePosition.metadata.create_all(engine)
    with Session(engine) as session:
        return session.execute(select(SatellitePosition).where(SatellitePosition.creation_date == time)).all()


def get_closest_satellite(time, latitude, longitude):
    best_distance = float('inf')
    closest_satellite_position = None
    desired_position = (latitude, longitude)
    all_satellites_positions = get_all_satellite_positions(time)
    for satellite_position_row in all_satellites_positions:
        satellite_position = dict(satellite_position_row)['SatellitePosition']
        distance = haversine(desired_position, (satellite_position.latitude, satellite_position.longitude))
        if distance < best_distance:
            best_distance = distance
            closest_satellite_position = satellite_position_row
    return closest_satellite_position


def main():
    """
    Allows to print the closest satellite position information (including its ID) given a specific time and position
    (lat, long). If no position is found for that specific time, then 'None' is printed.
    Command to run: `python closest_satellite.py <datetime> <latitude> <longitude>`
    Example: `python closest_satellite.py 2021-01-26T14:26:10 25 20`

    :param datetime: the specific datetime at which we want to search.
    :param latitude: the specific latitude for which we want the closest position.
    :param longitude: the specific longitude for which we want the closest position.

    :return: void.

    No parameters checks were programmed. This feature also requires that you populate the database previously using
    the main.py feature (refer to the main function inside the main.py file to see how).
    """
    arguments = sys.argv
    time = arguments[1]
    latitude = float(arguments[2])
    longitude = float(arguments[3])
    closest_satellite = get_closest_satellite(time, latitude, longitude)
    print(closest_satellite)


if __name__ == '__main__':
    main()
