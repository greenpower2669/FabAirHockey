__version__ = '1.0'

import kivy
kivy.require('1.0.6')
from kivy.core.window import Window
from kivy.core.window import WindowBase
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Point, GraphicException
from random import random
from math import sqrt
import time


def calculate_points(x1, y1, x2, y2, steps=5):
    dx = x2 - x1
    dy = y2 - y1
    dist = sqrt(dx * dx + dy * dy)
    if dist < steps:
        return
    o = []
    m = dist / steps
    for i in range(1, int(m)):
        mi = i / m
        lastx = x1 + dx * mi
        lasty = y1 + dy * mi
        o.extend([lastx, lasty])
    return o


class jah(FloatLayout):

    def on_touch_down(self, touch):
        win = self.get_parent_window()
        ud = touch.ud
        ud['group'] = g = str(touch.uid)
        pointsize = 5
        if 'pressure' in touch.profile:
            ud['pressure'] = touch.pressure
            pointsize = (touch.pressure * 100000) ** 2
        ud['color'] = random()

        with self.canvas:
            Color(1, 1, 1, mode='hsv', group=g)
            ud['lines'] = [
                Rectangle(pos=(touch.x, 0), size=(1, win.height), group=g),
                Rectangle(pos=(0, touch.y), size=(win.width, 1), group=g),
                Point(points=(touch.x+50, touch.y+50), source='pavé120.png',
                      pointsize=pointsize, group=g)]

        ud['label'] = Label(size_hint=(None, None),color=[105, 106, 188, 1])
        self.update_touch_label(ud['label'], touch)
        self.add_widget(ud['label'])
        touch.grab(self)
        return True

    def on_touch_move(self, touch):
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappua,timeappub,timelachea,timelacheb
        
        if touch.grab_current is not self:
            return
        ud = touch.ud
        if touch.y>ymax/2:
        	xh,yh=int(touch.x),int(touch.y)
        else:
        	xb,yb=touch.x,touch.y
        ud['lines'][0].pos = touch.x, 0
        ud['lines'][1].pos = 0, touch.y

        index = -1

        while True:
            try:
                points = ud['lines'][index].points
                oldx, oldy = points[-2], points[-1]
                break
            except:
                index -= 1

        points = calculate_points(oldx, oldy, touch.x, touch.y)

        # if pressure changed create a new point instruction
        if 'pressure' in ud:
            if not .95 < (touch.pressure / ud['pressure']) < 1.05:
                g = ud['group']
                pointsize = (touch.pressure * 100000) ** 2
                with self.canvas:
                    Color(ud['color'], 1, 1, mode='hsv', group=g)
                    ud['lines'].append(
                        Point(points=(), source='pavé120.gif',
                              pointsize=pointsize, group=g))

        if points:
            try:
                lp = ud['lines'][-1].add_point
                for idx in range(0, len(points), 2):
                    lp(points[idx], points[idx + 1])
            except GraphicException:
                pass

        ud['label'].pos = touch.pos
        import time
        t = int(time.time())
        if t not in ud:
            ud[t] = 1
        else:
            ud[t] += 1
        self.update_touch_label(ud['label'], touch)

    def on_touch_up(self, touch):
        if touch.grab_current is not self:
            return
        touch.ungrab(self)
        ud = touch.ud
        #self.canvas.remove_group(ud['group'])
        #self.remove_widget(ud['label'])

    def update_touch_label(self, label, touch):
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappua,timeappub,timelachea,timelacheb
        label.text = 'ID: %s\joueurh et force (%d,%d,%d\nPos: (%d, %d)\nClass: %s' % (
            touch.id, xh,yh,fh,touch.x, touch.y, touch.__class__.__name__)
        label.texture_update()
        label.pos = touch.pos
        label.size = label.texture_size[0] + 20, label.texture_size[1] + 20
    def __init__(self, **kwargs):
    	global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappua,timeappub,timelachea,timelacheb
    	xh,yh,xb,yb,fh,fb=0,0,0,0,0,0
    	h,b,ih,ib={},{},0,0
    	#fh fb force h b xylistes ih ib index listes
    	timeappua,timeappub,timelachea,timelacheb=0,0,0,0
    	xmax,ymax=Window.size[0],Window.size[1]
    	super(jah, self).__init__(**kwargs)
    	with self.canvas:
    		Color(1, 1, 1)
    		Rectangle(source='table.png',pos=(0,0), size=(xmax,ymax))
    		Rectangle(source='pavé120.png',pos=(xmax/2-58.5,ymax/2-58.5))
    		

class jahApp(App):
    title = 'Test'
    

    def build(self):
        return jah()

    def on_pause(self):
        return True


if __name__ == '__main__':
    jahApp().run()
