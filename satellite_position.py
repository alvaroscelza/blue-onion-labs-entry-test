from sqlalchemy import Column, String, DateTime, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SatellitePosition(Base):
    __tablename__ = 'launch'

    id = Column(Integer, primary_key=True)
    satellite_id = Column(String)
    creation_date = Column(DateTime())
    longitude = Column(Float)
    latitude = Column(Float)

    def __repr__(self):
        return 'Satellite id: {}, Datetime: {}, Longitude: {}, Latitude: {}'\
            .format(self.satellite_id, self.creation_date, self.longitude, self.latitude)
