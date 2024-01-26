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
        global choixidh,choixidb,ymax
        if choixidh!=0 and touch.id==choixidh and touch.y>ymax/2:
        	choixidh=touch.id+1
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
                Point(points=(touch.x, touch.y), source='pavé120.png',
                      pointsize=pointsize, group=g)]

        ud['label'] = Label(size_hint=(None, None),color=[105, 106, 188, 1])
        self.update_touch_label(ud['label'], touch)
        self.add_widget(ud['label'])
        touch.grab(self)
        return True

    def on_touch_move(self, touch):
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb
        
        if touch.grab_current is not self:
            return
        ud = touch.ud
        if touch.y>ymax/2 and touch.id==choixidh:
        	ih+=1
        	xh,yh=touch.x,touch.y
        	h[ih*10+touch.id]=xh,yh,int(100*time.time())
        	if ih>2:
        		a,b,e=h[(ih-1)*10+touch.id]
        		c,d,f=h[ih*10+touch.id]
        		fh=force(a,b,e,c,d,f)
        		
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
        t = int(time.time())
        if t not in ud:
            ud[t] = 1
        else:
            ud[t] += 1
        self.update_touch_label(ud['label'], touch)

    def on_touch_up(self, touch,**kwargs):
        global choixidh,choixidb,ih,ib
        if choixidh!=0 and touch.id==choixidh:
        	choixidh,ih=0,0
        if touch.grab_current is not self:
            return
        touch.ungrab(self)
        ud = touch.ud
        #self.canvas.remove_group(ud['group'])
        #self.remove_widget(ud['label'])

    def update_touch_label(self, label, touch):
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb
        label.text = 'ID: %s\joueurh et force (%d,%d,%d)\time %d /nPos: (%d, %d)\nClass: %s' % (
            touch.id, xh,yh,fh,0,touch.x, touch.y, touch.__class__.__name__)
        label.texture_update()
        label.pos = touch.pos
        label.size = label.texture_size[0] + 20, label.texture_size[1] + 20
        
    def __init__(self, **kwargs):
    	global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb
    	xh,yh,xb,yb,fh,fb=0,0,0,0,0,0
    	h,b,ih,ib={},{},0,0
    	choixidh,choixidb=0,0
    	#fh fb force h b xylistes ih ib index listes
    	timeappuh,timeappub,timelacheh,timelacheb=0,0,0,0
    	xmax,ymax=Window.size[0],Window.size[1]
    	super(jah, self).__init__(**kwargs)
    	with self.canvas:
    		Color(1, 1, 1)
    		Rectangle(source='table.png',pos=(0,0), size=(xmax,ymax))
    		Rectangle(source='pavé120.png',pos=(xmax/2-58.5,ymax/2-58.5))
    		
def force(a,b,e,c,d,f):
	vx,vy,t=a-c,b-d,f-e
	if t==0:
		f=0
		return f
	f=int(((abs(vx)+abs(vy))/2)/t)
	return f

def vectoriser(a,b,c,d):
	#forme xya xyb
	

	vvectx,vvecty=a-c,b-d
	absx,absy=abs(vvectx),abs(vvecty)
	totdif=absx+absy
	#les signes pos ou neg de x et y vect
	if vvectx<absx:
		ssignex=-1
	else:
		ssignex=1
	if vvecty<absy:
		ssigney=-1
	else:
		ssigney=1
	#si x ou y au dessus de 99%tot alors donner val à 99% et 1% sinon calculer.
	if absx>0.99*totdif:
		vvectx=0.99
		vvecty=0.01
	if absy>0.99*totdif:
		vvecty=0.99
		vvectx=0.01
	if (vvectx!=0.99 and vvecty!=0.01) or (vvecty!=0.99 and vvectx!=0.01):
		vvectx=absx/totdif*ssignex
		vvecty=absy/totdif*ssigney

	return vvectx,vvecty  	
def rr(p):


	tval=time.time()


	tval=tval-int(tval)


	tval=tval*10000


	tval=tval-int(tval)


	q= tval*p


	return q	
class jahApp(App):
    title = 'Test'
    

    def build(self):
        return jah()

    def on_pause(self):
        return True

choixidh,choixidb=0,0
if __name__ == '__main__':
    jahApp().run()
