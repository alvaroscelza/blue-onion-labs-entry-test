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

## Assumptions
- Handling all that data in memory is not an issue, nor is performance.
- Data is always correctly formatted, no correctness checks are made.
- Task 3 is confusing: not sure if you want to have the last know position of a satellite, or that satellite position 
given a time T (and returning None in case we don't have a position for that satellite at that time T). I'm assuming 
you wanted the last case.

## Effort Registry

The entire project took an hour and a half to be completed.

## Technology Stack

- Python 3.8
- Docker Desktop 4.9 (mac)

## Installation

- Create virtual environment and activate it. Example: `virtualenv venv`
- Enter environment: Example: `venv\Scripts\activate`
- Install requirements: `pip install -r requirements.txt`
- Run `docker-compose up` to start database.

## Usage
- Example: `python main.py 5eed7714096e59000698563c 2020-08-29T04:46:09 --populate-data`
- Refer to the main.py script code for deeper documentation.
