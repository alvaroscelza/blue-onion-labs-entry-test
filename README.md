# BlueOnionLabs entry test
[Tasks](https://github.com/BlueOnionLabs/api-spacex-backend)

- I implemented a postgres database with docker-compose, just run `docker-compose up` to start it in port 5432.
Remember: you have to have Docker running on background (Docker-Desktop for windows and mac).
You can connect to it (it's called 'docker') with user 'docker' and password 'docker' through localhost.
- All requirements are set in the requirements.txt file.
- I didn't use Gitflow because I'm the only developer, and it's a small project, but I use it on all my actual projects.

## Assumptions
None.

## Effort Registry

The entire project took TODO minutes in total, to be completed.

## Technology Stack

- Python 3.8
- Docker Desktop 4.9 (mac)

## Installation and running

### Without Docker

- Create virtual environment and activate it. Example: `virtualenv venv`
- Enter environment: Example: `venv\Scripts\activate`
- Install requirements: `pip install -r requirements.txt`
- Run `docker-compose up` to start database.
