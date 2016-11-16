from dgame import DGame
import sys
import _pickle as pickle
import arcade
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print(''' Error PyOpenGL not installed properly!!''')
  sys.exit(  )
from matplotlib import pyplot as plt


# Untility function: change .save to image
# pickle recommended
def data2img(filename):
    with open(filename,'rb') as fp:
        data  = pickle.load(fp)['info'].img
    plt.imshow(data)
    plt.savefig(os.path.splitext(filename)[0]+'.png')
    plt.close()

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

class DGameAPI(DGame):
    def __init__(self):
        super().__init__()
        self.info = None
    def animate(self,deltatime=1):
        self.info = get_info(0,self.info)
        self.person.change_x = stdin_input()
        super().animate()

def get_info(d: DGameAPI):
    isDead = d.chances
    x,y = d.person.center_x,d.person.center_y
    change_y = d.person.change_y
    score = d.score
    chances = d.chances
    xs = []
    ys = []
    for r in d.rects:
        xs.append(r.center_x)
        ys.append(r.center_y)
    img = glReadPixels(0, 0, 500, 500, GL_RGB, GL_UNSIGNED_BYTE, outputType=None)
    info = {
        'isDead':isDead,
        'x':x,'y':y,
        'change_y':change_y,
        'score':score,
        'chances':chances,
        'xs':xs,'ys':ys,
        'img':img
    }
    return info

def main():
    DGameAPI()
    arcade.run()

if __name__=="__main__":
    main()



