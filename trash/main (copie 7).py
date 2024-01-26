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
from time import sleep
from kivy.core.audio import SoundLoader
from kivy.clock import Clock


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
        it=float(100*time.time())
        if choixidh==0 and int(touch.id)+1!=choixidb and touch.y>ymax/2:
        	choixidh=int(touch.id)+1
        if choixidb==0 and int(touch.id)+1!=choixidh and touch.y<ymax/2:
        	choixidb=int(touch.id)+1
        if touch.y>ymax/2 and int(touch.id)+1==choixidh:
        	ih+=1
        	xh,yh=float(touch.x),float(touch.y)
        	#h[ih*10+int(touch.id)+1]=xh,yh,it
        	h[ih]=xh,yh,it
        	#if ih>3:
        		#a,b,e=h[(ih-1)*10+int(touch.id)+1]
        		#c,d,f=h[ih*10+int(touch.id)+1]
        		#fh=force(a,b,e,c,d,f)
        if touch.y<ymax/2 and int(touch.id)+1==choixidh:
        	ih=ih
        		
        if touch.y<ymax/2 and int(touch.id)+1==choixidb:
        	ib+=1
        	xb,yb=float(touch.x),float(touch.y)
        	#b[ib*10+int(touch.id)+1]=xb,yb,it
        	b[ib]=xb,yb,it
        	#if ib>3:
        		#ibm=ib-1
        		#g,h,i=b[ibm]
        		#j,k,l=b[ib]
        		#g,h,i=b[(ib-1)*10+int(touch.id)+1]
        		#j,k,l=b[ib*10+int(touch.id)+1]
        		#fb=force(g,h,j,k,i,l)
        if touch.y<ymax/2 and int(touch.id)+1==choixidb:
        	ib=ib
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

    def on_touch_up(self, touch):
        global choixidh,choixidb,ih,ib
        if choixidh!=0 and int(touch.id)+1==choixidh and int(touch.id)+1!=choixidb:
        	choixidh,ih=0,0
        if choixidb!=0 and int(touch.id)+1==choixidb and choixidh!=int(touch.id)+1:
        	choixidb,ib=0,0
        if touch.grab_current is not self:
            return
        touch.ungrab(self)
        ud = touch.ud
        self.canvas.remove_group(ud['group'])
        self.remove_widget(ud['label'])

    def update_touch_label(self, label, touch):
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test
        label.text = 'ID: %s\joueurh et force (%d,%d,%d)\n choix h et b (%d,%d) %d /nPos: (%d, %d)\nClass: %s' % (
            touch.id, xh,yh,fh,choixidh,choixidb,test,touch.x, touch.y, touch.__class__.__name__)
        label.texture_update()
        label.pos = touch.pos
        label.size = label.texture_size[0] + 20, label.texture_size[1] + 20

        
    def __init__(self, **kwargs):
    	global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test,pavx,paxy
    	h,b={},{}
    	xh,yh,xb,yb,fh,fb=0.1,0.1,0.1,0.1,0.1,0.1
    	h[1]=0.1,0.1,0.1
    	b[1]=0.1,0.1,0.1
    	ih=1
    	ib=1
    	xmax,ymax=Window.size[0],Window.size[1]
    	pavx,pavy=xmax/2-58.5,ymax/2-58.5
    	test=0
    	#m=SoundLoader.load('m.wav')
    	#m.play()
    	choixidh,choixidb=0,0
    	#fh fb force h b xylistes ih ib index listes
    	timeappuh,timeappub,timelacheh,timelacheb=0,0,0,0
    	
    	super(jah, self).__init__(**kwargs)
    	with self.canvas:
    		Color(1, 1, 1)
    		Rectangle(source='table.png',pos=(0,0), size=(xmax,ymax))
    		self.pavé=Rectangle(source='pavé120.png',pos=(pavx,pavy))
    def screen_up(self,time_passed):
    	global test,pavx,xh,pavy,yh
    	test+=1
    	pavx=xh
    	pavy=yh
    	self.pavé.pos=(pavx,pavy)
    	

def force(a,b,e,c,d,f):
	vx,vy,t=a-c,b-d,f-e
	if t==0:
		g=0
		return g
	f=int(((abs(vx)+abs(vy))/2)/t)
	return g

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
    def on_start(self):
    	Clock.schedule_interval(self.root.screen_up, 0.01)   		

    def build(self):
        return jah()

    def on_pause(self):
        return True

choixidh,choixidb=0,0
if __name__ == '__main__':
    jahApp().run()
