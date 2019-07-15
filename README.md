# Game of Drones
A simple scissors paper rock game.

## Getting Started
### Install and dependencies
1. Clone this repo `git clone https://github.com/jacastillol/game-of-drones.git` and `cd game-of-drones`.
1. Build the container `docker-compose build`.
1. Build database command `docker-compose run --rm app sh -c "python manage.py makemigrations"`
1. Build database `docker-compose run --rm app sh -c "python manage.py migreate"`
1. Run the app from your local machine with `docker-compose up"`

