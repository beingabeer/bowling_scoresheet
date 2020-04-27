### 10 Pin Bowling Game  (WIP)
A 10 pin bowling game built using Python/Django with a Rest API support

![](https://github.com/beingabeer/bowling_scoresheet/blob/master/app/screens/bowling.png)


## Running application with Docker

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

## How does it work?

Simply register a player name, create a game and click on the "Play" button. After which the player is directed to the game detail screen.

![](https://github.com/beingabeer/bowling_scoresheet/blob/master/app/screens/game-detail.png)




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
