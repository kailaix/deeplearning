import arcade
import time
import random

GRAVITY = 0
BONUS_RATE = 0.1

class Rect(arcade.Sprite):
    def __init__(self,cx):
        super().__init__('rec.jpg',image_height=5,image_width=100,center_x=cx,center_y=0)
        self.change_y = 1

class Bonus(arcade.Sprite):
    def __init__(self,cx,cy):
        super().__init__('bonus.png', image_height=10, image_width=10, center_x=cx, center_y=cy+5)
        self.change_y = 1


class DGame(arcade.Window):
    def __init__(self):
        super().__init__(500,500,'DeepLearning Demo')

        self.person = arcade.Sprite('person.png',scale=0.1)
        self.person.center_x = 250
        self.person.center_y = 500

        self.rects = arcade.SpriteList()
        self.bonus = arcade.SpriteList()

        self.score = 0
        self.chances = 3
        self.status = 0



    def on_draw(self):
        arcade.set_background_color(arcade.color.AERO_BLUE)
        arcade.start_render()
        self.person.draw()
        self.rects.draw()
        self.bonus.draw()
        self._panel()
        if self.status==1:
            self.status = 0
            arcade.draw_text("Start Again", 200, 400, arcade.color.RED, 14)
        elif self.status==-1:
            arcade.draw_text("Game Over", 200, 400, arcade.color.RED, 14)




    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            pass
            # self.person.change_x = 0
            # self.person.change_y = 0
        if key==arcade.key.DOWN:
            pass
            # self.person.change_x = 0
            # self.person.change_y = -1
        if key==arcade.key.LEFT:
            self.person.change_x = -1
        if key==arcade.key.RIGHT:
            self.person.change_x = 1

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.person.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.person.change_x = 0



    def animate(self,deltatime=1):
        if self.chances==0:
            while 1:
                time.sleep(1)

        if self.person.center_x == 250 and self.person.center_y == 500:
            time.sleep(1)

        if self._lowerest():
            cx = random.randrange(50,450)
            nr = Rect(cx)
            self.rects.append(nr)
            if random.random()<BONUS_RATE:
                cx = random.randrange(nr.center_x-50,nr.center_x+50)
                cy = nr.center_y+3
                self.bonus.append(Bonus(cx,cy))

        collide_list = arcade.check_for_collision_with_list(self.person,self.rects)


        if (len(collide_list)>0) and (self.person.center_y - 8 >= collide_list[0].center_y):
            self.person.change_y = 1
        else:
            if self.person.change_y < 0:
                self.person.change_y -= GRAVITY
            else:
                self.person.change_y = -1

        self._check_bonus()


        self.score += 1


        self.person.update()
        self.rects.update()
        self.bonus.update()

        if not self.valid_check():
            if self.chances >= 1:
                self.chances -= 1
                self.person.center_x = 250
                self.person.center_y = 500
                self._removetop()
                self.status = 1
            else:

                self.chances -= 1
                self.status = -1


    def _lowerest(self):
        if len(self.rects)==0:
            return True
        t = []
        for rec in self.rects:
            t.append(rec.center_y)
        if min(t)>80:
            return True

    def valid_check(self):
        # delete those rectangles who are out of range
        for rec in self.rects:
            if rec.center_y>500:
                rec.kill()

        if self.person.center_x <5:
            self.person.center_x = 5
        if self.person.center_x > 495:
            self.person.center_x = 495


        if self.person.center_y < 0 or self.person.center_y>500:
            return False

        return True

    def _panel(self):
        arcade.draw_text("Score:{}".format(self.score),\
                         400,470,color=arcade.color.BLACK,align="left")
        arcade.draw_text("Chances:{}".format(self.chances),\
                         400,450,color=arcade.color.BLACK,align="left")

    def _removetop(self):
        collide_list = arcade.check_for_collision_with_list(self.person, self.rects)
        if len(collide_list)>0:
            for c in collide_list:
                self._remove_bonus(c)
                self.rects.remove(c)
        for c in self.rects:
            if abs(c.center_x-250)<100 and c.center_y>250:
                self._remove_bonus(c)
                c.kill()

    def _check_bonus(self):
        collide_list = arcade.check_for_collision_with_list(self.person, self.bonus)
        if len(collide_list)>0:
            collide_list[0].kill()
            self.chances += 1

    def _remove_bonus(self,c):
        for b in self.bonus:
            if abs(c.center_y-b.center_y)<50:
                b.kill()



if __name__=='__main__':
    DGame()
    arcade.run()

