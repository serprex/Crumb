#!/usr/bin/env python
from pyglet.clock import set_fps_limit as W,tick
__import__("pyglet").options["debug_gl"]=W(60)
from pyglet.gl import GLfloat as F,glBegin as G,glEnd,glLineWidth as N,glVertex2f as V,glColor3f as O,glReadPixels as P,glClear as C,glRecti as R
W=__import__("pyglet").window.Window(600,600,style="borderless")
(lambda f:f(f))(lambda f:globals().update(A=-6,B=-6,Z=(((Z<<2)-6,4)for Z in xrange(2147483647)),_=C(16384),r=f,U=globals().update))
W.on_mouse_drag=W.on_mouse_motion=lambda x,y,z,Z,b=N(2),m=W.set_mouse_cursor(W.get_system_mouse_cursor("crosshair")),R=(F*3)():A or(L.extend((x,y))or len(L)>3 and any(((P(x,y+(x-L[-2])*(L[-3]-L[-1])/(L[-4]-L[-2]),1,1,6407,5126,R),any(R[:2]))[1]for x in xrange(x,L[-4],cmp(*L[-4::2])or x))if abs(L[-3]-L[-1])<abs(L[-4]-L[-2])else((P(x+(y-L[-1])*(L[-4]-L[-2])/(L[-3]-L[-1]),y,1,1,6407,5126,R),any(R[:2]))[1]for y in xrange(y,L[-3],cmp(*L[-3::2])or y)))and(r(r)if R[1]else U(A=X,B=Y)))
while not W.has_exit or W.close():
	tick(W.dispatch_events())
	if A:
		U((x,__import__("random").randint(100,500))for x in"XY")
		O(0,0,0)
		R(A+9,B+9,A-9,B-9)
		for A,B in(0,9),(1,4):
			R(X+B,Y+B,X-B,Y-B)
			O(1-A,A,A)
		for A,L in zip(Z,(G(1),[])):V(*A)
		A=O(1,1,1)
	elif len(L)>12:
		G(3)
		for A in xrange(len(L)-12,-1,-2):V(*(L.pop(0),L.pop(0))if A>2 else L[:2])
	glEnd()
	W.flip()
