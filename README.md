# DeepLearning Game

This game is created for deep learning course project purpose.

Users must first install [arcade](http://pythonhosted.org/arcade/index.html)(python3 version only).

```
pip install arcade
```

Then 

```
python dgame.py
```

You should be able to play the game. Notion: Python version only!

## Constant

`GRAVITY`: used to set gravity

`BONUS_RATE`: default bonus rate, it should be a number between 0 and 1.

## API

`api.py` is a command line API for modeling purpose. To use it, first create a `DGameAPI` object,

```
game = DGameAPI()
```

Then we can call the function `dapi(game,i)` to animate one step, where

* `i=1`: move right
* `i=-1`: move left
* `i=0`: stay

`dapi` will return a `info` dictionary:

* `isDead`: whether the game is over(`False` for game over)
* `x,y`: coordinate of the player
* `change_y`: the velocity of the player(negative number for falling)
* `score`: current score
* `chances`: remaining chances, `0` for dead
* `xs,ys`: the center of rectangles

