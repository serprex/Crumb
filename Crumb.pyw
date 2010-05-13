#!/usr/bin/env python
from pyglet.gl import GLfloat as F,glBegin as G,glEnd,glLineWidth as N,glVertex2f as V,glColor3f as O,glReadPixels as P,glClear as C,glRecti as R
(lambda r:r(r))(lambda r:globals().update(A=-6,B=-6,Z=iter(xrange(149)),r=r,U=globals().update,T=__import__("pyglet",C(16384)),Q=xrange))
T.options["debug_gl"],W=T.clock.set_fps_limit(60),T.window.Window(600,600)
W.on_mouse_drag=W.on_mouse_motion=lambda x,y,z,Z,b=N(2),m=W.set_mouse_cursor(W.get_system_mouse_cursor("crosshair")),R=(F*3)():A or(L.extend((x,y))or len(L)>3and any((P(x,y+(x-L[-2])*(L[-3]-L[-1])/(L[-4]-L[-2]),1,1,6407,5126,R)or any(R[:2])for x in Q(x,L[-4],cmp(*L[-4::2])or x))if abs(L[-3]-L[-1])<abs(L[-4]-L[-2])else(P(x+(y-L[-1])*(L[-4]-L[-2])/(L[-3]-L[-1]),y,1,1,6407,5126,R)or any(R[:2])for y in Q(y,L[-3],cmp(*L[-3::2])or y)))and(r(r)if R[1]else U(A=X,B=Y)))
W.on_draw=lambda:U(A=U((x,__import__("random").randint(100,500))for x in"XY"),L=[V(a*4-6,4)for a,a in zip((G(1),O(0,1,1)),Z)][glEnd():O(0,0,0):R(A+9,B+9,A-9,B-9)][R(X+9,Y+9,X-9,Y-9):O(1,0,0):R(X+4,Y+4,X-4,Y-4)]*0)if A else[V(*a>2and (L.pop(0),L.pop(0))or L[O(1,1,1):2])for a in Q(len(L)-12,G(3)or-1,-2)][U(A=glEnd()):]
T.app.run()
