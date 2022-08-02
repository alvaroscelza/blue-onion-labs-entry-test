# BlueOnionLabs entry test
[Tasks](https://github.com/BlueOnionLabs/api-spacex-backend)

## Important Notes
- I implemented a postgres database with docker-compose, just run `docker-compose up` to start it in port 5432.
Remember: you have to have Docker running on background (Docker-Desktop for windows and mac).
You can connect to it with user 'docker' and password 'docker' through localhost, database is also called 'docker'.
- All requirements are set in the requirements.txt file.
- I didn't use Gitflow because I'm the only developer, and it's a small project, but I use it on all my actual projects.
For this case though, the branch 'master' was enough.
- Some data ids were duplicated (like 5eed7714096e59000698563c), therefore I set a new field name for that called
launch_id which is not unique.
- The data is gathered from your repository json using internet. So, in order for this to work, you need to be connected
to the internet. I use requests package for this.
- Some provided data don't have latitude (it's null), so you will see 'None' in the latitude of the printed
result for those.

## Assumptions
- Handling all that data in memory is not an issue, otherwise we would have to explore how to download it by chunks.
- Data is always correctly formatted, no correctness checks are made.
- Task 3 is confusing: not sure if you want to have the last know position of a satellite, or that satellite position 
given a time T (and returning None in case we don't have a position for that satellite at that time T). I'm assuming 
you wanted the last case.

## Effort Registry

The entire project took 3 hours to be completed.

## Technology Stack

- Python 3.8
- Docker Desktop 4.9 (mac)

## Installation

- Create virtual environment and activate it. Example: `virtualenv venv`
- Enter environment: Example: `venv\Scripts\activate`
- Install requirements: `pip install -r requirements.txt`
- Run `docker-compose up` to start database.

## Usage
- Get satellite position at time Example: `python main.py 5eed770f096e59000698560d 2020-10-13T04:16:08 --populate-data`
- Refer to the main function in [main.py](main.py) file for deeper documentation.
- Get the closest satellite at given time-position: `python closest_satellite.py 2021-01-26T14:26:10 25 20` (answer
for this case (63 positions with that time), should be the satellite with id `5eed7714096e5900069856a0`).
- Refer to the main function in [closest_satellite.py](closest_satellite.py) file for deeper documentation.
