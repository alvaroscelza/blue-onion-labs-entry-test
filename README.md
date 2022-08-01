# BlueOnionLabs entry test
[Tasks](https://github.com/BlueOnionLabs/api-spacex-backend)

- I implemented a postgres database with docker-compose, just run `docker-compose up` to start it in port 5432.
Remember: you have to have Docker running on background (Docker-Desktop for windows and mac).
You can connect to it (it's called 'docker') with user 'docker' and password 'docker' through localhost.
- All requirements are set in the requirements.txt file.
- I didn't use Gitflow because I'm the only developer, and it's a small project, but I use it on all my actual projects.
- Some ids were duplicated (like 5eed7714096e59000698563c), therefore I set a new field name for that called launch_id 
which is not unique.
- The data is gathered from your repository json using internet. So, in order for this to work, you need to be connected
to the internet. I use requests package for this.
- Sequent runs of the program will fetch the data and insert it into the database multiple times.

## Assumptions
- Handling all that data in memory is not an issue, nor is performance.
- Data is always correctly formatted, no correctness checks are made.

## Effort Registry

The entire project took TODO minutes in total, to be completed.

## Technology Stack

- Python 3.8
- Docker Desktop 4.9 (mac)

## Installation and running

- Create virtual environment and activate it. Example: `virtualenv venv`
- Enter environment: Example: `venv\Scripts\activate`
- Install requirements: `pip install -r requirements.txt`
- Run `docker-compose up` to start database.
- Run `python main.py` to run the code.
