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
koh,kob,kobs,kohs=0,0,0,0
start=False
Clock.max_iteration = 100
treset=0
fc,rfc=0,1
radb,radh,radp=0,0,0
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
#m.play()
switchm=1

pbt,pbh,pbb,pbd,wh,wb,wg,wd=False,0,0,0,0,0,0,0
bh,bb,bg,bd,hh,hb,hg,hd=0,0,0,0,0,0,0,0
fpav=0
sch,scb=0,0
vpavy=0.5
vpavx=0.5
mh,mb,mp=76,76,50
xmax,ymax=Window.size[0],Window.size[1]
mx,my=xmax/30,ymax/40#margexy
pavx,pavy=int(xmax/2),int(ymax/2)
test=0
gagnant=0
vxh,vxb,vyh,vyb,fh,fb=0,0,0,0,0,0
yh=ymax/3*2
yb=ymax/3
xh=xmax/2
xb=xmax/2
jhcoul,jbcoul,jbc,jhc=0,0,0,0
engo=True
#anime va et vient vvtic 10 à 100 et multvv 1-1
vv,mvv,vv1,mvv1,vv2,mvv2,vv3,mvv3=1,1,1,1,1,1,1,1
#m=SoundLoader.load('m.wav')
#reb.play()
choixidh,choixidb=0,0
#fh fb force h b xylistes ih ib index listes
timeappuh,timeappub,timelacheh,timelacheb=0,0,0,0
def vvincrem(self):
	global vv,mvv,vv1,mvv1,vv2,mvv2,vv3,mvv3
	
	vv+=1*mvv
	if vv>50 or vv<1:
		self.c.source='anim/c'+str(vv1)+'.png'
		mvv*=-1
		vv1+=1*mvv1
		if vv1>8 or vv1<2:
			mvv1*=-1
			vv2+=1*mvv2
			if vv2>9 or vv2<1:
				mvv2*=-1
	
def coul(self,ou,scr,**kwargs):
	pts = "changecoul"+ou
	self.canvas.before.remove_group(pts)
	if ou=="g":
		x,y=xmax/4-90,ymax/2-90
	if ou=="d":
		x,y=xmax/4*3-90,ymax/2-90
	if ou=="md":
		x,y=xmax-10-180,ymax/2-90
	if ou=="mg":
		x,y=10,ymax/2-90
	if ou=="dhg":
		x,y=10,ymax-180-10
	if ou=="dbg":
		x,y=10,10
	if ou=="dhd":
		x,y=xmax-10-180,ymax-180-10
	if ou=="dbd":
		x,y=xmax-10-180,10
		
	
	#self.canvas.clear('pts')
	#self.canvas.remove(group='pts')	
	with self.canvas.before:
		Color(0.26, 0.26, 0.26,group=pts)
		el1=Ellipse(pos=(x,y), size=(180,180),group=pts)
		Color(1, 0, 1,group=pts)
		el2=Ellipse(pos=(x,y), size=(180,180),angle_end=(0.001 if scr == 0 else 1/300*scr*360),group=pts)
		Color(1, 1, 1,group=pts)
		el3=Ellipse(pos=(x+3,y+3), size=(180-6,180-6),group=pts)
		#fin coul
	
def scr(self,qui,scr,**kwargs):
	
	pts = "pts"+qui
	self.canvas.before.remove_group(pts)
	if qui=="b":
		x,y=xmax/2-90,ymax/3*2-90
	if qui=="h":
		x,y=xmax/2-90,ymax/3-90
	
	#self.canvas.clear('pts')
	#self.canvas.remove(group='pts')	
	with self.canvas.before:
		Color(0.26, 0.26, 0.26,group=pts)
		el1=Ellipse(pos=(x,y), size=(180,180),group=pts)
		Color(0, 1, 0,group=pts)
		el2=Ellipse(pos=(x,y), size=(180,180),angle_end=(0.001 if scr == 0 else 1/10*scr*360),group=pts)
		Color(1, 1, 1,group=pts)
		el3=Ellipse(pos=(x+10,y+10), size=(180-20,180-20),group=pts)



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
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,xb0,yb0,xh0,yh0,accb,acch
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
         

        ##insert((
        ud = touch.ud
        it=float(100*time.time())
        if choixidh==0 and int(touch.id)+1!=choixidb and touch.y>ymax/2:
        	choixidh=int(touch.id)+1
        if choixidb==0 and int(touch.id)+1!=choixidh and touch.y<ymax/2:
        	choixidb=int(touch.id)+1
        if touch.y>ymax/2 and int(touch.id)+1==choixidh:
        	#ih+=1
        	fh=0
        	#xh0,yh0=xh,yh
        	xh,yh=float(touch.x),float(touch.y)
        	#h[ih*10+int(touch.id)+1]=xh,yh,it
        	#h[ih]=xh,yh,it
        	#if ih>3:
        		#a,b,e=h[(ih-1)*10+int(touch.id)+1]
        		#c,d,f=h[ih*10+int(touch.id)+1]
        		#fh=force(a,b,e,c,d,f)
        if touch.y<ymax/2 and int(touch.id)+1==choixidh:
        	ih=ih
        	
        		
        if touch.y<ymax/2 and int(touch.id)+1==choixidb:
        	#ib+=1
        	fb=0
        	
        		
        	#xb0,yb0=xb,yb
        	xb,yb=float(touch.x),float(touch.y)
        	#b[ib*10+int(touch.id)+1]=xb,yb,it
        	#b[ib]=xb,yb,it
        	#if ib>3:
        		#ibm=ib-1
        		#g,h,i=b[ibm]
        		#j,k,l=b[ib]
        		#g,h,i=b[(ib-1)*10+int(touch.id)+1]
        		#j,k,l=b[ib*10+int(touch.id)+1]
        		#fb=force(g,h,j,k,i,l)
        if touch.y<ymax/2 and int(touch.id)+1==choixidb:
        	
        	ib=ib

        ##insert))
        ud['label'] = Label(size_hint=(None, None),color=[105, 106, 188, 1])
        #self.update_touch_label(ud['label'], touch)
        #self.add_widget(ud['label'])
        #<<<<<<<<  add  <<<<<<<<≤<<<<<<<<<<<<<<∆
        touch.grab(self)
        return True

    def on_touch_move(self, touch):
        global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,xb0,yb0,xh0,yh0,accb,acch
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
    	global xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,fh,fb,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test,pavx,paxy,vpavx,vpavy,fpav,mh,mb,vv,mvv,vv1,mvv1,vv2,mvv2
    	
    	super(jah, self).__init__(**kwargs)
    	with self.canvas.before:
    		Color(1, 1, 1)
    		self.fond=Rectangle(source='table.png',pos=(0,0), size=(xmax,ymax))
    	
    		
    		#self.down=Rectangle(source=str(scb)+'.png',pos=(xmax/2+300,ymax/2+100),size=(100,100))
    		#Color(0.26, 0.26, 0.26)
    		#self.down=Ellipse(pos=(xmax/2+200,ymax/2+100),size=(200,200))
    		#Color(1, 1, 1)
    		#self.up=Rectangle(source=str(sch)+'.png',pos=(xmax/2-400,ymax/2-400),size=(100,100))
    		ps=121
    		hs=161
    		
    	with self.canvas:
    		self.pavé=Rectangle(source='pavé120.png',pos=(pavx,pavy),size=(ps,ps))
    		self.jh=Rectangle(source='jh0.png',pos=(xh-mh,yh-mh),size=(hs,hs))
    		self.jb=Rectangle(source='jb0.png',pos=(xb-mb,yb-mb),size=(hs,hs))
    		self.gagn=Rectangle(source='goi.png',pos=(-5100,-5000),size=(400,200))
    		self.win=Rectangle(source='winp.png',pos=(-5100,-5000),size=(300,600))
    		self.help=Rectangle(source='help.png',pos=(0,0), size=(xmax,ymax))
    	scr(self,"h",0)
    	scr(self,"b",0)
    	with self.canvas:
    		self.cadre=Rectangle(source='cadre.png',pos=(0,0), size=(xmax,ymax))
    		self.c=Rectangle(source='anim/c'+str(vv1)+'.png',pos=(xmax-200,ymax-200), size=(150,150))
    	

    		
    def screen_up(self,time_passed,**kwargs):
    	global test,pavx,xh,pavy,yh,xmax,ymax,xh,yh,xb,yb,h,b,ih,ib,timeappuh,timeappub,timelacheh,timelacheb,choixidh,choixidb,test,pavx,pavy,vpavx,vpavy,fpav,mp,vxh,vxb,vyh,vyb,fh,fb,pbt,pbh,pbb,pbd,wh,wb,wg,wd,bh,bb,bg,bd,hh,hb,hg,hd,sch,scb,gagnant,fc,count,rfc,treset,stoph,stopb,start,switchm,engo,fb0,fh0,acch,accb,pavx0,pavy0,xh0,yh0,xb0,yb0,treset0,jhcoul,jbcoul,jbc,jhc,radb,radh,radp,koh,kob,kobs,kohs,mx,my,vv,mvv,vv1,mvv1,vv2,mvv2
    	#fc frame count
    	#passby true? trou haut bas deux pbb pbh pbd walls haut b g d  puis score en 10 sch et scb
    	#self.canvas.remove_group('pts')
    	#mask de dist pour pavé et haut bas handle betwin et config
    	mdpav,mdhb,mdconf=60-1,80-1,70
    	mdbe=mdhb+mdpav
    	vvincrem(self)
    	#kobeth koh,kob,kobs,kohs s pour save
    	if kob>0:
    		kob-=1
    		if kob<1:
    			kob=0
    			choixidb=0
    	if kob<1:
    		kov=0
    	
    	if koh>0:
    		koh-=1
    		if koh<1:
    			koh=0
    			choixidh=0
    	if koh<1:
    		koh=0
    		
    		
    	#mdbe=(mdpav*2+mdhb*2)/4
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
    	if pavx>xmax-mp-mx and wd==0:
    		wd=1
    		reb2.play()
    		vpavx*=-1
    		pavx=xmax-mp*1.3-mx
    	else:
    		wd=0
    	if pavx<0+mp+mx and wg==0:
    		wg=1
    		pavx=mp*1.3+mx
    		reb2.play()
    		vpavx*=-1
    	else:
    		wg=0
    	if pavy>ymax-mp-my and not pbt and engo and wh==0:
    		wh=1
    		pavy=ymax-mp*1.3-my
    		reb2.play()
    		if pbt==False:
    			vpavy*=-1
    		
    	else:
    		wh=0
    	if pavy<0+mp+my and not pbt and engo and wb==0:
    		wb=1
    		reb2.play()
    		pavy=mp*1.3+my
    		if pbt==False:
    			vpavy*=-1
    	else:
    		wb=0
    	if pavy<0 and engo and pbt and gagnant==0:
    		scb+=1
    		tombe.play()
    		
    		engo=False
    		if scb>9:
    			scb=10
    			gagnant=1
    			tamb.play()
    		pavx,pavy=int(xmax/2),int(ymax/2)
    		scr(self,'b',scb)
    		self.gagn.source='go.png'
    		self.win.source='winpi.png'
    		#self.down.source=str(scb)+'.png'
    		fpav,fh,fb=0,0,0
    	if pavy>ymax and engo and pbt and gagnant==0:
    		engo=False
    		tombe.play()
    		sch+=1
    		if sch>9:
    			sch=10
    			gagnant=2
    			tamb.play()
    		pavx,pavy=int(xmax/2),int(ymax/2)
    		#self.up.source=str(sch)+'.png'
    		scr(self,'h',sch)
    		self.gagn.source='goi.png'
    		self.win.source='winp.png'
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
    	antici=0.4#_------------,<  antici sur acc
    	#anticif pour un max
    	anticif=25
    	af=0
    	#anticife pour se substituer à fh ou fb
    	it=float(100*time.time())
    	if choixidh<1:
    		fh-=0.5
    		if fh<1:
    			fh=0
    		xh0,yh0=xh,yh
    		#ih+=1
    		xh,yh=xh-vxh*fh,yh-vyh*fh
    		ih=0
    		acch=0
    		#h[ih]=xh,yh,it
    	else:
    			if acch>0:
    				#af=fh+acch*acch*antici
    				
    				if af>anticif:
    					af=anticif
    				#ih+=1
    				#xh0,yh0=xh,yh
    				#xh,yh=xh-vxh*af,yh-vyh*af
    				#h[ih]=xh,yh,it
    				
    	if choixidb<1:
    		fb-=0.5
    		if fb<1:
    			fb=0
    		xb0,yb0=xb,yb
    		#ib+=1
    		xb,yb=xb-vxb*fb,yb-vyb*fb
    		#b[ib]=xb,yb,it
    		ib=0
    		accb=0
    	else:
    		if accb>0:
    			#af=fb+accb*accb*antici
    			
    			if af>anticif:
    					af=anticif
    			#ib+=1
    			#xb0,yb0=xb,yb
    			#xb,yb=xb-vxb*af,yb-vyb*af
    			#b[ib]=xb,yb,it
    		
    		## h et b dans la  limites de la table
    	if accb<1:
    		accb=0
    	if acch<1:
    		acch=0
    	if xh>xmax-mh-mx and hd==0 and choixidh<1:
    		xh=xmax-1.3*mh-mx
    		reb3.play()
    		hd=1
    		vxh*=-1
    	else:
    		hd=0
    	if xh<0+mh+mx and choixidh<1 and hg==0:
    		xh=0+1.3*mh+mx
    		reb3.play()
    		hg=1
    		vxh*=-1
    	else:
    		hg=0
    	if yh>ymax-mh-my and choixidh<1 and hh==0:
    		yh=ymax-1.3*mh-my
    		reb3.play()
    		hh=1
    		vyh*=-1
    	else:
    		hh=0
    	if yh<0+mh+my and choixidh<1 and hb==0:
    		reb3.play()
    		yh=0+1.3*mh+my
    		hb=1
    		vyh*=-1
    	else:
    		hb=0
    	if xb>xmax-mb and choixidb<1 and bd==0:## h et b dans la  limites de la table:
    		xb=xmax-1.3*mb
    		reb3.play()
    		bd=1
    		vxb*=-1
    	else:
    		bd=0
    	if xb<0+mb and choixidb<1 and bg==0:
    		xb=0+1.3*mb
    		reb3.play()
    		bg=1
    		vxb*=-1
    	else:
    		bg=0
    	if yb>ymax-mb and choixidb<1 and bh==0:
    		yb=ymax-1.3*mb
    		reb3.play()
    		bh=1
    		vyb*=-1
    	else:
    		bh=0
    	if yb<0+mb and choixidb<1and bb==0:
    		yb=0+1.3*mb
    		reb3.play()
    		bb=1
    		vyb*=-1
    	else:
    		bb=0
    	###vecteurs de forces h et b et def des rad
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

#####m
######:
	######:

    		

    	radh,radb,radp=radc(vxh,vyh),radc(vxb,vyb),radc(vpavx,vpavy)
    	stopsens=3.5#div 2
    	if collide(pavx,pavy,xh,yh,mdbe/stopsens) and ih<2 and choixidh>0:
    		fpav=0
    		stoph=1
    	if collide(pavx,pavy,xh,yh,mdbe)and stoph==0 and not collide(xh,yh,xb,yb,mdbe) and pbh==0:## test collide:
    		for i in range(0,10):
    			if fh!=0 or fpav!=0:
    				ifb=fh/100
    				ifpav=fpav/100
    				ixb,iyb=xh0+vxh*ifb*i,yh0+vyh*ifb*i
    				ipavx,ipavy=pavx0+ifpav*i*vpavx,pavy0+ifpav*i*vpavy
    				if collide(ipavx,ipavy,ixb,iyb,mdbe):
    					pavx,pavy,xh,yh=float(ipavx),float(ipavy),float(ixb),float(iyb)
    					i=10
    		vpavx,vpavy=vectoriser(pavx,pavy,xh,yh)
    		fpav=ralent(fpav)
    		
    		pbh+=1

    		if fpav<6 and fh<6 and choixidh>0:
    			stoph=1
    		if fpav>19:
    			reb.play()
    		if fh>fpav:
    			fpav=abs(raddif(radh,radp))*verifdif(fh,fpav)+fh*collidedif(pavx,pavy,xh,yh,mdbe)
    		else:
    			fpav+=fh*collidedif(pavx,pavy,xh,yh,mdbe)
    			#fpav=fh
    			#vpavx,vpavy=vectoriser(xh,yh,pavx,pavy)
    		#
    		pavx0,pavy0=pavx,pavy
    		mult=2
    		pavx,pavy=pavx+vpavx*fpav*mult,pavy+vpavy*fpav*mult
    		
    		#
    	treset0=treset
    	if not engo:
    		srs=mdconf
    		if collide(xh,yh,xmax/2,ymax/3*2,srs) and collide(xb,yb,xmax/2,ymax/3,srs):
    			pavx,pavy=int(xmax/2),int(ymax/2)
    			mil.play()
    			engo=True
    			pavx,pavy=int(xmax/2),int(ymax/2)
    	if gagnant!=0:
    		
    		if (collide(xh,yh,xmax/2,ymax/3*2,srs) and collide(xb,yb,xmax/2,ymax/3,srs)):
    			restart(self)
    	srs=100
    	if collide(xh,yh,xmax-50,ymax-50,srs) and collide(xb,yb,50,50,srs):
    		treset+=1
    		coul(self,'dhd',treset)
    		coul(self,'dbg',treset)
    		if treset>300:
    			restart(self)
    			engo=True
    			fpav=0
    		
    	srs=mdpav
    	if (collide(xh,yh,50,ymax/2,srs) and collide(xb,yb,xmax-50,ymax/2,srs)) or (collide(xb,yb,50,ymax/2,srs) and collide(xh,yh,xmax-50,ymax/2,srs)):
    		coul(self,'mg',treset)
    		coul(self,'md',treset)
    		treset+=1
    		if treset>300:	
    			treset=0
    			if switchm>0:
    				m.stop()
    				m.play()
    				switchm*=-1
    			else:
    				switchm*=-1
    				m.stop()
    			
    			#self.pavé.pos=(pavx-mp,pavy-mp)
    			
    	if collide(xh,yh,xmax/4+50,ymax/2,80) or collide(xh,yh,xmax/4*3+50,ymax/2,80):
    		treset+=1
    		if collide(xh,yh,xmax/4+50,ymax/2,80):
    			coul(self,'g',treset)
    		else:
    			coul(self,'d',treset)
    			
    		if treset>300:	
    			treset=0
    			jhcoul+=1
    			if jhcoul>10:
    				jhcoul=0
    			if jhcoul==10:
    				self.jh.source="jh"+str(jhcoul-3)+'.png'
    			else:
    				self.jh.source="jh"+str(jhcoul)+'.png'
    	if jhcoul==10:
    			jhc+=1
    			if jhc>99:
    				jhc=0
    			self.jh.source="jh"+str(int(jhc/10))+'.png'
    			#<<<<<<<<   coul
    	if collide(xb,yb,xmax/4+50,ymax/2,mdpav) or collide(xb,yb,xmax/4*3+50,ymax/2,mdpav):
    		treset+=1
    		if collide(xb,yb,xmax/4+50,ymax/2,mdpav):
    			coul(self,'g',treset)
    		else:
    			coul(self,'d',treset)
    			
    		if treset>300:	
    			treset=0
    			jbcoul+=1
    			if jbcoul>10:
    				jbcoul=0
    			#<<<<<<<<<<     coul
    			if jbcoul==10:
    				self.jb.source="jb"+str(jbcoul-2)+'.png'
    			else:
    				self.jb.source="jb"+str(jbcoul)+'.png'
    	if jbcoul==10:
    			jbc+=1
    			if jbc>99:
    				jbc=0
    			self.jb.source="jb"+str(int(jbc/10))+'.png'
 
    			#pavx,pavy=int(xmax/2),int(ymax/2)
    			#self.pavé.pos=(pavx-mp,pavy-mp)
    			
    	if collide(xh,yh,50,ymax-50,srs) and collide(xb,yb,xmax-50,50,srs):
    		treset+=1
    		coul(self,'dhg',treset)
    		coul(self,'dbd',treset)
    		if treset>300:	
    			treset=0
    			engo=True
    			fpav=0
    			pavx,pavy=int(xmax/2),int(ymax/2)
    			self.pavé.pos=(pavx-mp,pavy-mp)
    			
    			
    	self.pavé.pos=(pavx-mp,pavy-mp)
    	
    			
    			#####>>>>>  xb
    			
    	if collide(pavx,pavy,xb,yb,mdbe/stopsens) and ih<3 and choixidb>0:
    		fpav=0
    		stopb=1
    	if collide(pavx,pavy,xb,yb,mdbe) and stopb==0 and not collide(xh,yh,xb,yb,mdbe) and pbb==0:
    		##
    		for i in range(0,10):
    			if fb!=0 or fpav!=0:
    				ifb=fb/100
    				ifpav=fpav/100
    				ixb,iyb=xb0+vxb*ifb*i,yb0+vyb*ifb*i
    				ipavx,ipavy=pavx0+ifpav*i*vpavx,pavy0+ifpav*i*vpavy
    				if collide(ipavx,ipavy,ixb,iyb,mdbe):
    					pavx,pavy,xb,yb=float(ipavx),float(ipavy),float(ixb),float(iyb)
    					i=100
    		##
    		fpav=ralent(fpav)
    		
    		if fpav>10:
    			reb.play()
    		pbb=pbb+1
    		vpavx,vpavy=vectoriser(pavx,pavy,xb,yb)
    		if fpav<6 and fb<6 and choixidb>0:
    			stopb=1
    		if fb>fpav:
    			#fpav=fb+accb/10
    			fpav=fb*collidedif(pavx,pavy,xb,yb,mdbe)+abs(raddif(radb,radp))*verifdif(fb,fpav)
    		else:
    			fpav+=fh*collidedif(pavx,pavy,xb,yb,mdbe)
    			#fpav=fb
    		pavx0,pavy0=pavx,pavy
    		mult=2
    		pavx,pavy=pavx+vpavx*fpav*mult,pavy+vpavy*fpav*mult
    	if pbb!=0:
    		pbb+=1
    		if collide(pavx,pavy,xb,yb,mdbe):
    		
    			
    			
    			
    			fpav+=fb*collidedif(pavx,pavy,xb,yb,mdbe)
    			pbb=1
    			#pavx,pavy+=vpavx*fpav,vpavy*fpav
    		if pbb>3:
    			pbb=0
    	if pbh!=0:
    		pbh+=1
    		if collide(pavx,pavy,xh,yh,mdbe):
    			#
    			
    			
    			
    			fpav+=fh*collidedif(pavx,pavy,xh,yh,mdbe)
    			#
    			pbh=1
    		if pbh>3:
    			pbh=0
    	if pbd!=0:
    		pbd+=1
    		if collide(xb,yb,xh,yh,mdhb*2):
    			pbd=1
    			#
    			vxh,vyh=vectoriser(xb,yb,xh,yh)
    			vxb,vyb=vectoriser(xh,yh,xb,yb)
    			if fb>fh:
    				fh=0.95*fb
    				fb=fh*0.85
    			else:
    				fb=fh*0.95
    				fh=fb*0.85
    			if fb<1:
    				fb=1
    			if fh<1:
    				fh=1
    			#
    		
    		if pbd>3:
    			pbd=0
    
    	##                   !eatch over collide and ko		
    	if collide(xh,yh,xb,yb,mdhb*2-2) and pbd==0:
    		kob,koh,kobs,kohs=5,5,5,5
    		choixidb=-400
    		choixidh=-500
    		ib,ih=0,0
    		if fb>fh:
    			#kobs+=fb-fh
    			#kohs=50
    			kobs,kohs=10,10
    		else:
    			#kohs+=(fh-fb)*3
    			#kobs=50
    			kohs,kobs=10,10
    		
    		#koh+=int(kobs*1)+5
    		#kob+=int(kohs*1)+5
    		if choixidh>0 or choixidb>0:
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
    		if fb<10:
    			fb=10
    		if fh<10:
    			fh=10
    			
    	
    	
    	
    	if stopb==1:
    		pavx,pavy=xb,yb
    		if fb*fb*fb>90 or choixidb<1:
    			stopb=0
    			fpav,vpavx,vpavy,pbb=fb*1.5,-vxb,-vyb,1
    			pavx,pavy=pavx+vpavx*fpav,pavy+vpavy*fpav
    			pavx0,pavy0=pavx,pavy
    	if stoph==1:
    		pavx,pavy,fpav=xh,yh,fh*1.5
    		if fh*fh*fh>90 or choixidh<1:
    			stoph=0
    			fpav,vpavx,vpavy,pbh=fh*1.5,-vxh,-vyh,1
    			pavx,pavy=pavx+4*vpavx*fpav,pavy+4*vpavy*fpav
    			pavx0,pavy0=pavx,pavy
    	if treset0==treset:
    		treset=0
    		cleanchangecoul(self)

    		
    	self.pavé.pos=(pavx-mdpav,pavy-mdpav)
    	self.jh.pos=(xh-mdhb,yh-mdhb)
    	self.jb.pos=(xb-mdhb,yb-mdhb)
    	
def verifdif(f1,f2):
	if f1==0 or f2 ==0:
		return 0
	if f1>f2:
		if f1/f2>1:
			return 0
		else: 
			return 1
		return 1 
def cleanchangecoul(self):
    self.canvas.before.remove_group('changecould')
    self.canvas.before.remove_group('changecoulg')
    self.canvas.before.remove_group('changecoulmg')
    self.canvas.before.remove_group('changecoulmd')
    self.canvas.before.remove_group('changecouldhd')
    self.canvas.before.remove_group('changecouldhg')
    self.canvas.before.remove_group('changecouldbd')
    self.canvas.before.remove_group('changecouldbg')
    
def radc(vx,vy):
    va=(vx+1)/2
    vb=(vy+1)/2
    return ((va+vb*-1)/2)*1000#360
def raddif(rada,radb):
    if rada>radb:
    	return rada-radb
    else:
    	return (radb-rada)*-1
    	
def ralent(fp):
	fp-=(fp*fp*fp)*0.000004
	if fp<1:
		fp=0
	return fp
	
def result(f1,f2):
	if f1>f2:
	  	return -1
def collide(x1,y1,x2,y2,sensi):#dif sur tan
	a,b=abs(x1-x2),abs(y1-y2)
	ac,bc=a*a,b*b
	result=sqrt(ac+bc)
	if result<sensi:
		return True
	return False
	
def collidedif(x1,y1,x2,y2,sensi):#ecart diftan
	a,b=abs(x1-x2),abs(y1-y2)
	ac,bc=a*a,b*b
	result=sqrt(ac+bc)
	if result<1:
		return 0
	if result<sensi:
		return abs(1/(sensi/result))
	return 0
	
def tantemps(x1,y1,x2,y2,temps):#test tan
	a,b=abs(x1-x2),abs(y1-y2)
	ac,bc=a*a,b*b
	result=sqrt(ac+bc)
	return abs(result/temps)
		

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
class mainApp(App):

    title = 'Test'
    def on_start(self):
    	Clock.max_iteration = 60
    	Clock.schedule_interval(self.root.screen_up, 0.001)   		

    def build(self):
        return jah()

    def on_pause(self):
        return True

choixidh,choixidb=0,0

if __name__ in ('__main__', '__android__'):
    mainApp().run()