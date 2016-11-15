from dgame import DGame
from pprint import pprint

class DGameAPI(DGame):
    def cmd(self,i):
        self.person.change_x = i

    def animate(self,deltatime=1):
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
    info = {
        'isDead':isDead,
        'x':x,'y':y,
        'change_y':change_y,
        'score':score,
        'chances':chances,
        'xs':xs,'ys':ys
    }
    return info


def dapi(game,i):
    if i!=-1 and i!=0 and i!=1:
        raise Exception("Wrong input: should be -1,0,1")

    game.cmd(i)
    game.animate()
    info = get_info(game)
    return info

# game = DGameAPI()
#
# info = dapi(game,1)
# pprint(info)
#
# info = dapi(game,1)
# pprint(info)
#
# info = dapi(game,1)
# pprint(info)



