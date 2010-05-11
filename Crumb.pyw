#!/usr/bin/env python
from pyglet import options as R
from pyglet.clock import set_fps_limit as W,tick
R["debug_gl"]=W(60)
from pyglet.gl import GLfloat,glBegin,glEnd,glLineWidth,glVertex2f,glVertex2fv,glColor3f,glReadPixels,glClear,glRecti
from pyglet.window import Window as W
from random import randint as R
W=W(600,600,style="borderless")
(lambda f:f(f))(lambda f:globals().update(A=-6,B=-6,Z=((GLfloat*2)((Z<<2)-6,4)for Z in xrange(2147483647)),_=glClear(16384),r=f))
W.event("on_mouse_drag")(W.event("on_mouse_motion")(lambda x,y,z,Z,b=glLineWidth(2),m=W.set_mouse_cursor(W.get_system_mouse_cursor("crosshair")),R=(GLfloat*3)():A or(L.extend((x,y))or len(L)>3 and any(((glReadPixels(x,y+(x-L[-2])*(L[-3]-L[-1])/(L[-4]-L[-2]),1,1,6407,5126,R),any(R[:2]))[1]for x in xrange(x,L[-4],cmp(*L[-4::2])or x))if abs(L[-3]-L[-1])<abs(L[-4]-L[-2])else((glReadPixels(x+(y-L[-1])*(L[-4]-L[-2])/(L[-3]-L[-1]),y,1,1,6407,5126,R),any(R[:2]))[1]for y in xrange(y,L[-3],cmp(*L[-3::2])or y)))and(r(r)if R[1]else globals().update(A=X,B=Y)))))
while not W.has_exit:
	tick(W.dispatch_events())
	if A:
		globals().update((x,R(100,500))for x in"XY")
		glColor3f(0,0,0)
		glRecti(A+9,B+9,A-9,B-9)
		for A,B in(0,9),(1,4):
			glRecti(X+B,Y+B,X-B,Y-B)
			glColor3f(1-A,A,A)
		for A,L in zip(Z,(glBegin(1),[])):glVertex2fv(A)
		A=glColor3f(1,1,1)
	elif len(L)>12:
		glBegin(3)
		for A in xrange(len(L)-12,-1,-2):glVertex2f(*(L.pop(0),L.pop(0))if A>2 else L[:2])
	glEnd()
	W.flip()
W.close()
