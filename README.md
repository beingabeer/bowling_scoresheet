## 10 Pin Bowling Game 
A 10 pin bowling game built using Python/Django with a Rest API support

![](https://github.com/beingabeer/bowling_scoresheet/blob/master/screens/bowl2.gif)

## Demo Link

<button name="button">https://bowling7.herokuapp.com/</button>

## Running application locally with Docker

Clone and add the following to a '.env.dev' file in the root directory:

```
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

Build the docker image and run the container:

```
docker-compose build
docker-compose up -d
```

then run the following commands:

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

to run tests:
```
docker-compose exec web pytest -n auto
```

## How does it work?

Simply register a player name, create a game and click on the "Play" button. After which the player is directed to the game detail screen. Select values for the rolls and click on the roll button to simulate a throw.

![](https://github.com/beingabeer/bowling_scoresheet/blob/master/screens/scoresheet1.gif)

## API 

[Documentation on Swagger](https://bowling7.herokuapp.com/swagger-docs/)

To start, make a `POST` request to `/player/create/` providing a player name

```
{
  "player_name": "Bob"
}
```
To create a game send a `POST` request to `/game/create/` passing in the player id. This will create a game with 10 frames attached to the game id.

For example -
```
curl -X POST "https://bowling7.herokuapp.com/api/v1/game/create/" -H  "Content-Type: application/json" -d '{  "player_id": 7}'
```

To get game details and score updates send a `GET` request to `/game/{game_id}/`. 

For example - 
```
curl -X GET "https://bowling7.herokuapp.com/api/v1/game/9/" -H  "accept: application/json"
```

```
{
  "game_id": 9,
  "cumulative_score": 0,
  "in_progress": true,
  "game_score": 0,
  "player_id": 25,
  "frames": [
    {
      "frame_no": 1,
      "roll_one": 0,
      "roll_two": 0,
      "roll_three": 0,
      "frame_is_active": true,
    },
    {
      "frame_no": 2,
      "roll_one": 0,
      "roll_two": 0,
      "roll_three": 0,
      "frame_is_active": false,
    },
    ..................
    {
      "frame_no": 9,
      "roll_one": 0,
      "roll_two": 0,
      "roll_three": 0,
      "frame_is_active": false,
    },
    {
      "frame_no": 10,
      "roll_one": 0,
      "roll_two": 0,
      "roll_three": 0,
      "frame_is_active": false,
    }
  ],
}

```

To simulate a Roll, send a `POST` request to `/game/{game_id}/roll/` passing in the `game id` and the roll data, where `roll_one` and `roll_two` values signify the number of pins knocked down for each individual frame. `roll_three` value is for the extra third throw that a player gets in frame 10 if there is a strike. By default, all roll values are 0. 

For example - 
```
curl -X POST "https://bowling7.herokuapp.com/api/v1/game/10/roll/" -H "Content-Type: application/json" -d '{  "roll_one": 0,  "roll_two": 0,  "roll_three": 0}'
```

If the roll is valid, it will be recorded and it may be immediately retrieved. 
A player may continue to roll until the game is over after the end of the 10th frame.
Any future attempts to make rolls will result in `400` response:
```
{
    "detail": "Game Over"
}
```
## Game Scoring rules summary

Each game, includes ten frames for the bowler.

* In each frame, the bowler gets up to two tries to knock down all the pins.
* If in two tries, the bowler fails to knock them all down, their score for that frame
is the total number of pins knocked down in their two tries.
* If in two tries the bowler knocks them all down, this is called a “spare” and their score for the
frame is ten plus the number of pins knocked down on their next throw (in their next turn).
* If on their first try in the frame the bowler knocks down all the pins, this is called a “strike”.
Their turn is over, and their score for the frame is ten plus the simple total of the pins knocked down in their next two rolls.
* If the bowler gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively.
These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat:
the bonus throws are only used to calculate the score of the final frame.
* The game score is the total of all frame scores.


## Technologies used

- Python
- Django
- Django Rest Framework
- Javascript
- Docker
- Black
- isort
- flake8
- Postgres
- Gunicorn
- HTML
- CSS
- pytest
- whitenoise
- Heroku
- Swagger
