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
* `img`: image data, `M*N*3`

## Interface

The function `stdin_input` is where deeplearning comes in. 

```
def stdin_input(last_info):
    # You will have the last step info -- last_info
    # Write Your Logic Here:
    # 1. Decide which direction to move(return value:0,1,2)
    # 2. Decide whether to save the info dictionary
    # 3. Other things you want to do

    # Example:
    s = input('Please input a number')
    if s=='-1':
        return -1
    if s=='1':
        return 1
    else:
        return 0
```

As denoted in the code, you should write your machine learning logistic here. You will get access to the last step `last_info`. 

You can also save the data in memory or in disk, so that you can get access to all the data you have. 

## Image Ultility

`data2img` is a function that convert pickle `.save` file to RGB image(`.png`). It is simple to use--read the raw code for reference.



