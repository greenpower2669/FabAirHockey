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
import math
h,b={},{}
xh,yh,xb,yb,fh,fb=0.1,0.1,0.1,0.1,0.1,0.1
h[1]=0.1,0.1,0.1
b[1]=0.1,0.1,0.1
ih=1
ib=1
#test passby

pbt,pbh,pbb,pbd,wh,wb,wg,wd=False,0,0,0,0,0,0,0
bh,bb,bg,bd,hh,hb,hg,hd=0,0,0,0,0,0,0,0
fpav=0
sch,scb=0,0
vpavy=0.5
vpavx=0.5
mh,mb,mp=76,76,50
xmax,ymax=Window.size[0],Window.size[1]
pavx,pavy=int(xmax/2-50),int(ymax/2-50)
test=0
vxh,vxb,vyh,vyb,fh,fb=0,0,0,0,0,0
#m=SoundLoader.load('m.wav')
#m.play()
choixidh,choixidb=0,0
#fh fb force h b xylistes ih ib index listes
timeappuh,timeappub,timelacheh,timelacheb=0,0,0,0


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
            Color(0, 0, 0,0,mode='rgba', group=g)
            ud['lines'] = [
                #Rectangle(pos=(touch.x, 0), size=(1, win.height), group=g),
                #Rectangle(pos=(0, touch.y), size=(win.width, 1), group=g),
                Point(points=(touch.x, touch.y), 
                      pointsize=0, group=g)]

        ud['label'] = Label(size_hint=(None, None),color=[105, 106, 188, 1])
        self.update_touch_label(ud['label'], touch)
        #self.add_widget(ud['label'])
        touch.grab(self)
        return True

    def on_touch_move(self, touch):
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb
        #time.sleep(0.001)
        
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
        #ud['lines'][0].pos = touch.x, 0
        #ud['lines'][1].pos = 0, touch.y

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
                #g = ud['group']
                pointsize = (touch.pressure * 100000) ** 2
                #with self.canvas:
                    #Color(ud['color'], 1, 8, mode='hsv', group=g)
                    #ud['lines'].append(
                        #Point(points=(), source='pavé120.gif',
                              #pointsize=pointsize, group=g))

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
        #self.update_touch_label(ud['label'], touch)

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
    	global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test,pavx,paxy,vpavx,vpavy,fpav,mh,mb
    	
    	super(jah, self).__init__(**kwargs)
    	with self.canvas:
    		#Color(1, 1, 1)
    		self.fond=Rectangle(source='table.png',pos=(0,0), size=(xmax,ymax))
    		self.pavé=Rectangle(source='pavé120.png',pos=(pavx,pavy),size=(100,100))
    		self.jh=Rectangle(source='jh120.png',pos=(xh-mh,yh-mh),size=(150,150))
    		self.jb=Rectangle(source='jb120.png',pos=(xb-mb,yb-mb),size=(150,150))
    		
    def screen_up(self,time_passed,**kwargs):
    	global test,pavx,xh,pavy,yh,xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test,pavx,pavy,vpavx,vpavy,fpav,mp,vxh,vxb,vyh,vyb,fh,fb,pbt,pbh,pbb,pbd,wh,wb,wg,wd,bh,bb,bg,bd,hh,hb,hg,hd
    	#passby true? trou haut bas deux pbb pbh pbd walls haut b g d  puis score en 10 sch et scb
    	
    	if xmax!=Window.size[0]:
    		xmax,ymax=Window.size[0],Window.size[1]
    		self.canvas.clear()
    		with self.canvas:
    			#Color(1, 1, 1)
    			self.fond=Rectangle(source='table.png',pos=(0,0), size=(xmax,ymax))
    			self.pavé=Rectangle(source='pavé120.png',pos=(pavx,pavy),size=(100,100))
    			self.jh=Rectangle(source='jh120.png',pos=(50,50),size=(150,150))
    			self.jb=Rectangle(source='jb120.png',pos=(50,50),size=(150,150))
    	pavx+=vpavx*fpav
    	pavy+=vpavy*fpav
    	fpav=fpav-0.1
    	if fpav<1:#limites de la table pour le pavé
    		fpav=0
    	if pavx>xmax-mp and wd==0:
    		wd=1
    		vpavx*=-1
    	else:
    		wd=0
    	if pavx<0+mp and wg==0:
    		wg=1
    		vpavx*=-1
    	else:
    		wg=0
    	if pavy>ymax-mp and wh==0:
    		wh=1
    		vpavy*=-1
    	else:
    		wh=0
    	if pavy<0+mp and wb==0:
    		wb=1
    		vpavy*=-1
    	else:
    		wb=0
    	if ib>1000:#### reset du rec b et h
    		ib=0
    	if ih>1000:
    		ih=0
    	##### mouvement d'' inertie des poignées
    	if choixidh==0:
    		fh-=0.5
    		if fh<1:
    			fh=0
    		xh,yh=xh-vxh*fh,yh-vyh*fh
    	if choixidb==0:
    		fb-=0.5
    		if fb<1:
    			fb=0
    		xb,yb=xb-vxb*fb,yb-vyb*fb
    		## h et b dans la  limites de la table
    	if xh>xmax-mh and hd==0:
    		hd=1
    		vxh*=-1
    	else:
    		hd=0
    	if xh<0+mh and hg==0:
    		hg=1
    		vxh*=-1
    	else:
    		hg=0
    	if yh>ymax-mh and hh==0:
    		hh=1
    		vyh*=-1
    	else:
    		hh=0
    	if yh<0+mh and hb==0:
    		hb=1
    		vyh*=-1
    	else:
    		hb=0
    	if xb>xmax-mb and bd==0:## h et b dans la  limites de la table:
    		xb=xmax-mb
    		bd=1
    		vxb*=-1
    	else:
    		bd=0
    	if xb<0+mb and bg==0:
    		xb=0+mb
    		bg=1
    		vxb*=-1
    	else:
    		bg=0
    	if yb>ymax-mb and bh==0:
    		yb=ymax-mb
    		bh=1
    		vyb*=-1
    	else:
    		bh=0
    	if yb<0+mb and bb==0:
    		yb=0+mb
    		bb=1
    		vyb*=-1
    	else:
    		bb=0
    	###vecteurs de forces h et b
    	if ih>4:
        	aa,bb,ee=h[ih-2]
        	cc,dd,ff=h[ih]
        	fh=force(aa,bb,ee,cc,dd,ff)*1.5
        	vxh,vyh=vectoriser(aa,bb,cc,dd)
		#########
    	###vecteurs de forces h et b
    	if ib>4:
        	aa,bb,ee=b[ib-2]
        	cc,dd,ff=b[ib]
        	fb=force(aa,bb,ee,cc,dd,ff)*1.5
        	vxb,vyb=vectoriser(aa,bb,cc,dd)
		#########
		#7#77
		## pass bye  collides#

    	if collide(pavx,pavy,xh,yh,100) and pbh==0:## test collide:
    		vpavx,vpavy=vectoriser(pavx,pavy,xh,yh)
    		fpav=fpav-0.1
    		pbh+=1
    		if fh>fpav:
    			fpav+=fh
    		if fpav==0:
    			fpav=fh
    			vpavx,vpavy=vectoriser(xh,yh,pavx,pavy)
    	if collide(pavx,pavy,xb,yb,100) and pbb==0:
    		fpav=fpav-0.1
    		pbb=pbb+1
    		vpavx,vpavy=vectoriser(pavx,pavy,xb,yb)
    		if fb>fpav:
    			fpav+=fb
    		if fpav==0:
    			fpav=fb
    			#vpavx,vpavy=vectoriser(pavx,pavy,xb,yb)
    	if pbb!=0:
    		pbb+=1
    		if pbb>10:
    			pbb=0
    	if pbh!=0:
    		pbh+=1
    		if pbh>10:
    			pbh=0
    	if pbd!=0:
    		pbd+=1
    		if pbd>10:
    			pbd=0
    			
    	if collide(xh,yh,xb,yb,100) and pbd==0:
    		fb-=0.1
    		fh-=0.1
    		vxh,vxb=vectoriser(xh,yh,xb,yb)
    		vxh,vxb=vectoriser(xb,yb,xh,yh)
    		pbd+=1
    		if fb>fh:
    			fh=fb
    		else:
    			fb=fh
    		
    	self.pavé.pos=(pavx-mp,pavy-mp)
    	self.jh.pos=(xh-mh,yh-mh)
    	self.jb.pos=(xb-mb,yb-mb)
def result(f1,f2):
	if f1>f2:
	  	return -1
   	
def collide(x1,y1,x2,y2,sensi): ### comparaison des pts milieux plus marge
	if abs(x1-x2) <sensi and abs(y1-y2)<sensi:
		return True
	False
	
def force(a,b,e,c,d,f):### Force par deux coo par le temps
	vx,vy,t=a-c,b-d,f-e
	if t==0:
		vf=0
		return vf
	vf=int(((abs(vx)+abs(vy))/2)/t)
	return vf

def vectoriser(a,b,c,d):####   Vectorisation sur 2 tuple
	#forme xya xyb
	vvectx,vvecty=a-c,b-d
	absx,absy=abs(vvectx),abs(vvecty)
	totdif=absx+absy
	#les signes pos ou neg de x et y vect
	if a==c or b==d:
		return 0,0
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

    	Clock.schedule_interval(self.root.screen_up, 0.0005)   		

    def build(self):
        return jah()

    def on_pause(self):
        return True

choixidh,choixidb=0,0
if __name__ == '__main__':
    jahApp().run()
