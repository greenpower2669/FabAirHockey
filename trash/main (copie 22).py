b__version__ = '1.0'

import kivy
kivy.require('1.0.6')
from kivy.core.window import Window
from kivy.core.window import WindowBase
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Ellipse,Color, Rectangle, Point, GraphicException
from random import random
from math import sqrt
import time
from time import sleep
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import math
start=False
Clock.max_iteration = 500
treset=0
fc,rfc=0,1
count=0
h,b={},{}
xh,yh,xb,yb,fh,fb=0.1,0.1,0.1,0.1,0.1,0.1
h[1]=0.1,0.1,0.1
b[1]=0.1,0.1,0.1
fb0,fh0,acch,accb=0,0,0,0
ih=1
ib=1
#test passby
stoph,stopb=0,0
m = SoundLoader.load('m.wav')
reb = SoundLoader.load('reb.wav')
reb2 = SoundLoader.load('reb2.wav')
reb3= SoundLoader.load('reb3.wav')
tombe= SoundLoader.load('tombe.wav')
tamb= SoundLoader.load('tamb.wav')
eng= SoundLoader.load('engo.wav')
mil= SoundLoader.load('mil.wav')
treset0=0
musict=time.time()
m.play()
switchm=1

pbt,pbh,pbb,pbd,wh,wb,wg,wd=False,0,0,0,0,0,0,0
bh,bb,bg,bd,hh,hb,hg,hd=0,0,0,0,0,0,0,0
fpav=0
sch,scb=0,0
vpavy=0.5
vpavx=0.5
mh,mb,mp=76,76,50
xmax,ymax=Window.size[0],Window.size[1]
pavx,pavy=int(xmax/2),int(ymax/2)
test=0
gagnant=0
vxh,vxb,vyh,vyb,fh,fb=0,0,0,0,0,0
yh=ymax/3*2
yb=ymax/3
xh=xmax/2
xb=xmax/2
engo=True
#m=SoundLoader.load('m.wav')
#reb.play()
choixidh,choixidb=0,0
#fh fb force h b xylistes ih ib index listes
timeappuh,timeappub,timelacheh,timelacheb=0,0,0,0

def scr(self,qui,scr,**kwargs):
	
	pts = "pts"+qui
	if qui=="b":
		x,y=xmax/2-90,ymax/3*2-90
	if qui=="h":
		x,y=xmax/2-90,ymax/3-90
	self.canvas.before.remove_group(pts)
	#self.canvas.clear('pts')
	#self.canvas.remove(group='pts')	
	with self.canvas.before:
		pts='pts'
		Color(0.26, 0.26, 0.26,group=pts)
		el1=Ellipse(pos=(x,y), size=(180,180),group=pts)
		Color(0, 1, 0,group=pts)
		el2=Ellipse(pos=(x,y), size=(180,180),angle_end=(0.001 if scr == 0 else 1/10*scr*360),group=pts)
		Color(1, 1, 1,group=pts)
		el3=Ellipse(pos=(x+5,y+5), size=(180-10,180-10),group=pts)



def restart(self):
	global gagnant,scb,sch,treset,xmax,ymax,mp,pavx,pavy
	gagnant,scb,sch=0,0,0
	treset=0
	eng.play()
	mil.play()
	self.gagn.pos=(-5000,-5000)
	self.win.pos=(-5000,-5000)
	scr(self,'h',0)
	scr(self,'b',0)
	#self.down.source=str(scb)+'.png'
	#self.up.source=str(sch)+'.png'
	
	pavx,pavy=int(xmax/2),int(ymax/2)
	self.pavé.pos=(pavx-mp,pavy-mp)

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
        #self.update_touch_label(ud['label'], touch)
        #self.add_widget(ud['label'])
        #<<<<<<<<  add  <<<<<<<<≤<<<<<<<<<<<<<<∆
        touch.grab(self)
        return True

    def on_touch_move(self, touch):
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,xb0,yb0,xh0,yh0
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
        	xh0,yh0=xh,yh
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
        	xb0,yb0=xb,yb
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
        #update≤<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<∆

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
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test,pbt,fc,treset
        label.text ='' #'ID: %s\joueurh et force (%d,%d,%d)\n choix h et b (%d,%d) milieu?%d /nPos: (%d, %d)\nClass: %s >fc %d' % (
            #touch.id, xh,yh,fh,choixidh,choixidb,pbt,touch.x, touch.y, touch.__class__.__name__,fc)
        #srs=50
        #infoh=collide(xh,yh,xmax-50,ymax-50,srs) 
        #infob= collide(xb,yb,50,50,srs)
        #infohb= infoh and infob
        #label.text = '>>>>> info en haut à droite? %s \n >>>>>info en bas à gauche? %s >>> les deux ? %s  %d \nh coo (%d  :  %d)\nb coo (%d  : %d)' % (
            #infoh,infob,infohb,treset,xh,yh,xb,yb)
        label.texture_update()
        label.pos = touch.pos
        label.size = label.texture_size[0] + 20, label.texture_size[1] + 20

        
    def __init__(self, **kwargs):
    	global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test,pavx,paxy,vpavx,vpavy,fpav,mh,mb
    	
    	super(jah, self).__init__(**kwargs)
    	with self.canvas.before:
    		Color(1, 1, 1)
    		self.fond=Rectangle(source='table.png',pos=(0,0), size=(xmax,ymax))
    		
    		#self.down=Rectangle(source=str(scb)+'.png',pos=(xmax/2+300,ymax/2+100),size=(100,100))
    		#Color(0.26, 0.26, 0.26)
    		#self.down=Ellipse(pos=(xmax/2+200,ymax/2+100),size=(200,200))
    		#Color(1, 1, 1)
    		#self.up=Rectangle(source=str(sch)+'.png',pos=(xmax/2-400,ymax/2-400),size=(100,100))
    	with self.canvas:
    		self.pavé=Rectangle(source='pavé120.png',pos=(pavx,pavy),size=(101,101))
    		self.jh=Rectangle(source='jh120.png',pos=(xh-mh,yh-mh),size=(151,151))
    		self.jb=Rectangle(source='jb120.png',pos=(xb-mb,yb-mb),size=(151,151))
    		self.gagn=Rectangle(source='go.png',pos=(-5100,-5000),size=(400,200))
    		self.win=Rectangle(source='winp.png',pos=(-5100,-5000),size=(300,600))
    		self.help=Rectangle(source='help.png',pos=(0,0), size=(xmax,ymax))
    	scr(self,"h",0)
    	scr(self,"b",0)
    	

    		
    def screen_up(self,time_passed,**kwargs):
    	global test,pavx,xh,pavy,yh,xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test,pavx,pavy,vpavx,vpavy,fpav,mp,vxh,vxb,vyh,vyb,fh,fb,pbt,pbh,pbb,pbd,wh,wb,wg,wd,bh,bb,bg,bd,hh,hb,hg,hd,sch,scb,gagnant,fc,count,rfc,treset,stoph,stopb,start,switchm,engo,fb0,fh0,acch,accb,pavx0,pavy0,xh0,yh0,xb0,yb0,treset0
    	#fc frame count
    	#passby true? trou haut bas deux pbb pbh pbd walls haut b g d  puis score en 10 sch et scb
    	self.canvas.remove_group('pts')
    	
    	if xmax!=Window.size[0]:
    		xmax,ymax=Window.size[0],Window.size[1]
    		self.fond.size=(xmax,ymax)
    		scr(self,'h',sch)
    		scr(self,'b',scb)
    	pavx0,pavy0=pavx,pavy		
    	pavx+=vpavx*fpav
    	pavy+=vpavy*fpav
    	fpav=ralent(fpav)
    	count+=-1
    	fc+=rfc
    	
    	if start!=True and (choixidb>0 or choixidh>0):
    		start=True
    		self.help.pos=(-6000,-6000)
    	if fc>1000 or fc<1:
    		rfc*=-1
    	#upscr= Label(size_hint=(40, 40),color=[105, 106, 188, 1])
    	#upscr.text = 'Joueur 1:%d     Joueur2:%d' % (sch,scb)
    	#upscr.texture_update()
        #<<<<<<<<  add
    	if pavx<(xmax/3)*2 and pavx>xmax/3:
    		pbt=True
    	else:
    		pbt=False
    	if fpav<1:#limites de la table pour le pavé
    		fpav=0
    	if pavx>xmax-mp and wd==0:
    		wd=1
    		reb2.play()
    		vpavx*=-1
    		pavx=xmax-mp*1.3
    	else:
    		wd=0
    	if pavx<0+mp and wg==0:
    		wg=1
    		pavx=mp*1.3
    		reb2.play()
    		vpavx*=-1
    	else:
    		wg=0
    	if pavy>ymax-mp and not pbt and engo and wh==0:
    		wh=1
    		pavy=ymax-mp*1.3
    		reb2.play()
    		if pbt==False:
    			vpavy*=-1
    		
    	else:
    		wh=0
    	if pavy<0+mp and not pbt and engo and wb==0:
    		wb=1
    		reb2.play()
    		pavy=mp*1.3
    		if pbt==False:
    			vpavy*=-1
    	else:
    		wb=0
    	if pavy<0 and engo and pbt and gagnant==0:
    		scb+=1
    		tombe.play()
    		
    		engo=False
    		if scb>9:
    			scb=9
    			gagnant=1
    			tamb.play()
    		pavx,pavy=int(xmax/2),int(ymax/2)
    		scr(self,'b',scb)
    		#self.down.source=str(scb)+'.png'
    		fpav,fh,fb=0,0,0
    	if pavy>ymax and engo and pbt and gagnant==0:
    		engo=False
    		tombe.play()
    		sch+=1
    		if sch>9:
    			sch=9
    			gagnant=2
    			tamb.play()
    		pavx,pavy=int(xmax/2),int(ymax/2)
    		#self.up.source=str(sch)+'.png'
    		scr(self,'h',sch)
    		fpav,fh,fb=0,0,0
    		#self.up.source=str(scb)+'.png'
    	#gagnant=1#test position win
    	if gagnant!=0:
    		self.gagn.pos=(xmax/2-230,ymax/2-800+gagnant*500)
    		self.win.pos=(xmax/2-140-250+int(fc/2),ymax/2+500-gagnant*500)
    	if not engo:
    		fpav=0
    		pavx,pavy=xmax/2,-8000
    	if ib>1000:#### reset du rec b et h
    		ib=0
    	if ih>1000:
    		ih=0
    	##### mouvement d'' inertie des poignées
    	if choixidh==0:
    		fh-=0.5
    		if fh<1:
    			fh=0
    		xh0,yh0=xh,yh
    		xh,yh=xh-vxh*fh,yh-vyh*fh
    	if choixidb==0:
    		fb-=0.5
    		if fb<1:
    			fb=0
    		xb0,yb0=xb,yb
    		xb,yb=xb-vxb*fb,yb-vyb*fb
    		## h et b dans la  limites de la table
    	if xh>xmax-mh and hd==0 and choixidh<1:
    		xh=xmax-1.3*mh
    		reb3.play()
    		hd=1
    		vxh*=-1
    	else:
    		hd=0
    	if xh<0+mh and choixidh==0 and hg==0:
    		xh=0+1.3*mh
    		reb3.play()
    		hg=1
    		vxh*=-1
    	else:
    		hg=0
    	if yh>ymax-mh and choixidh==0 and hh==0:
    		yh=ymax-1.3*mh
    		reb3.play()
    		hh=1
    		vyh*=-1
    	else:
    		hh=0
    	if yh<0+mh and choixidh==0 and hb==0:
    		reb3.play()
    		yh=0+1.3*mh
    		hb=1
    		vyh*=-1
    	else:
    		hb=0
    	if xb>xmax-mb and choixidb==0 and bd==0:## h et b dans la  limites de la table:
    		xb=xmax-1.3*mb
    		reb3.play()
    		bd=1
    		vxb*=-1
    	else:
    		bd=0
    	if xb<0+mb and choixidb==0 and bg==0:
    		xb=0+1.3*mb
    		reb3.play()
    		bg=1
    		vxb*=-1
    	else:
    		bg=0
    	if yb>ymax-mb and choixidb==0 and bh==0:
    		yb=ymax-1.3*mb
    		reb3.play()
    		bh=1
    		vyb*=-1
    	else:
    		bh=0
    	if yb<0+mb and choixidb==0 and bb==0:
    		yb=0+1.3*mb
    		reb3.play()
    		bb=1
    		vyb*=-1
    	else:
    		bb=0
    	###vecteurs de forces h et b
    	if ih>4:
        	aa,bb,ee=h[ih-2]
        	cc,dd,ff=h[ih]
        	#fh=force(aa,bb,ee,cc,dd,ff)*1.5
        	fh0=fh
        	fh=tantemps(aa,bb,cc,dd,ff-ee)
        	if fh>60:
        		fh=60
        	acch=fh-fh0
        	if acch>fh:
        		acch=fh
        	vxh,vyh=vectoriser(aa,bb,cc,dd)
		#########
    	###vecteurs de forces h et b
    	if ib>4:
        	aa,bb,ee=b[ib-2]
        	cc,dd,ff=b[ib]
        	#fb=force(aa,bb,ee,cc,dd,ff)*1.5
        	fb0=fb
        	fb=tantemps(aa,bb,cc,dd,ff-ee)
        	if fb>60:
        		fb=60
        	accb=fb-fb0
        	if accb>fb:
        		accb=fb
        	vxb,vyb=vectoriser(aa,bb,cc,dd)
			#########
			#7#77
			## pass bye  collides#
			
			
			
			######>>>>>>  xh
		

    	if collide(pavx,pavy,xh,yh,100)and stoph==0 and not collide(xh,yh,xb,yb,100) and pbh==0:## test collide:
    		for i in range(0,10):
    			if fh!=0 or fpav!=0:
    				ifb=fh/100
    				ifpav=fpav/100
    				ixb,iyb=xh0+vxh*ifb*i,yh0+vyh*ifb*i
    				ipavx,ipavy=pavx0+ifpav*i*vpavx,pavy0+ifpav*i*vpavy
    				if collide(ipavx,ipavy,ixb,iyb,100):
    					pavx,pavy,xh,yh=float(ipavx),float(ipavy),float(ixb),float(iyb)
    					i=100
    		vpavx,vpavy=vectoriser(pavx,pavy,xh,yh)
    		fpav=ralent(fpav)
    		
    		pbh+=1
    		if fh>fpav:
    			fpav=fh+acch/10
    		if fpav<20 and choixidh!=0:
    			stoph=1
    		if fpav>19:
    			reb.play()
    			#fpav=fh
    			#vpavx,vpavy=vectoriser(xh,yh,pavx,pavy)
    	treset0=treset
    	if not engo:
    		srs=100
    		if (collide(xh,yh,xmax/2,ymax/3*2,srs) and collide(xb,yb,xmax/2,ymax/3,srs)):
    			pavx,pavy=int(xmax/2),int(ymax/2)
    			mil.play()
    			engo=True
    	if gagnant!=0:
    		srs=100
    		if (collide(xh,yh,xmax/2,ymax/3*2,srs) and collide(xb,yb,xmax/2,ymax/3,srs)):
    			restart(self)
    	srs=100
    	if collide(xh,yh,xmax-50,ymax-50,srs) and collide(xb,yb,50,50,srs):
    		treset+=1
    		if treset>300:
    			restart(self)
    	srs=100
    	if (collide(xh,yh,50,ymax/2,srs) and collide(xb,yb,xmax-50,ymax/2,srs)) or (collide(xb,yb,50,ymax/2,srs) and collide(xh,yh,xmax-50,ymax/2,srs)):
    		treset+=1
    		if treset>300:	
    			treset=0
    			if switchm>0:
    				m.stop()
    				switchm*=-1
    			else:
    				switchm*=-1
    				m.stop()
    				m.play()
    			pavx,pavy=int(xmax/2),int(ymax/2)
    			self.pavé.pos=(pavx-mp,pavy-mp)
    	if collide(xh,yh,50,ymax-50,srs) and collide(xb,yb,xmax-50,50,srs):
    		treset+=1
    		if treset>300:	
    			treset=0
    			engo=True
    			pavx,pavy=int(xmax/2),int(ymax/2)
    			self.pavé.pos=(pavx-mp,pavy-mp)
    			
    			#####>>>>>  xb
    			
    	if collide(pavx,pavy,xb,yb,100) and stopb==0 and not collide(xh,yh,xb,yb,100) and pbb==0:
    		##
    		for i in range(0,10):
    			if fb!=0 or fpav!=0:
    				ifb=fb/100
    				ifpav=fpav/100
    				ixb,iyb=xb0+vxb*ifb*i,yb0+vyb*ifb*i
    				ipavx,ipavy=pavx0+ifpav*i*vpavx,pavy0+ifpav*i*vpavy
    				if collide(ipavx,ipavy,ixb,iyb,100):
    					pavx,pavy,xb,yb=float(ipavx),float(ipavy),float(ixb),float(iyb)
    					i=100
    		##
    		fpav=ralent(fpav)
    		
    		if fpav>19:
    			reb.play()
    		pbb=pbb+1
    		vpavx,vpavy=vectoriser(pavx,pavy,xb,yb)
    		if fb>fpav:
    			fpav=fb+accb/10
    		if fpav<10 and choixidb!=0:
    			stopb=1
    			#fpav=fb
    			#vpavx,vpavy=vectoriser(pavx,pavy,xb,yb)
    	if pbb!=0:
    		pbb+=1
    		if collide(pavx,pavy,xb,yb,100):
    			fpav+=fpav/10
    			pbb=1
    			#pavx,pavy+=vpavx*fpav,vpavy*fpav
    		if pbb>5:
    			pbb=0
    	if pbh!=0:
    		pbh+=1
    		if collide(pavx,pavy,xh,yh,100):
    			fpav+=fpav/5
    			pbh=1
    		if pbh>5:
    			pbh=0
    	if pbd!=0:
    		pbd+=1
    		if collide(pavx,pavy,xb,yb,100):
    			fpav+=fpav/5
    			pbb=1
    		if pbd>5:
    			pbd=0
    			
    	if collide(xh,yh,xb,yb,130) and pbd==0:
    		if choixidh==0 or choixidb==0:
    			if fb>4 or fh>4:
    				reb3.play()
    		vxh,vyh=vectoriser(xb,yb,xh,yh)
    		vxb,vyb=vectoriser(xh,yh,xb,yb)
    		pbd+=1
    		if fb>fh:
    			fh=0.95*fb
    			fb=fh*0.85
    		else:
    			fb=fh*0.95
    			fh=fb*0.85
    		
    	if stopb==1:
    		pavx,pavy,fpav=xb,yb,fb
    		if fpav>30 or choixidb==0:
    			stopb=0
    			fpav,vpavx,vpavy,pbb=fb*1.5,-vxb,-vyb,1
    	if stoph==1:
    		pavx,pavy,fpav=xh,yh,fh
    		if fpav>30 or choixidh==0:
    			stoph=0
    			fpav,vpavx,vpavy,pbh=fh*1.5,-vxh,-vyh,1
    	if treset0==treset:
    		treset=0
    	self.pavé.pos=(pavx-mp,pavy-mp)
    	self.jh.pos=(xh-mh,yh-mh)
    	self.jb.pos=(xb-mb,yb-mb)
def ralent(fp):
	fp-=(fp*fp)*0.0001
	if fp<1:
		fp=0
	return fp
	
def result(f1,f2):
	if f1>f2:
	  	return -1
def collide(x1,y1,x2,y2,sensi):#test tan
	a,b=abs(x1-x2),abs(y1-y2)
	ac,bc=a*a,b*b
	result=sqrt(ac+bc)
	if result<sensi:
		return True
def tantemps(x1,y1,x2,y2,temps):#test tan
	a,b=abs(x1-x2),abs(y1-y2)
	ac,bc=a*a,b*b
	result=sqrt(ac+bc)
	return result/temps
		
def collideanc(x1,y1,x2,y2,sensi): ### comparaison des pts milieux plus marge
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
    	Clock.max_iteration = 50
    	Clock.schedule_interval(self.root.screen_up, 0.001)   		

    def build(self):
        return jah()

    def on_pause(self):
        return True

choixidh,choixidb=0,0
if __name__ == '__main__':
    jahApp().run()
