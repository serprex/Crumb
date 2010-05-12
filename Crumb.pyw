#!/usr/bin/env python
__import__("pyglet").options["debug_gl"]=__import__("pyglet").clock.set_fps_limit(60)
from pyglet.gl import GLfloat as F,glBegin as G,glEnd,glLineWidth as N,glVertex2f as V,glColor3f as O,glReadPixels as P,glClear as C,glRecti as R
W=__import__("pyglet").window.Window(600,600,style="borderless")
(lambda f:f(f))(lambda f:globals().update(A=-6,B=-6,Z=(((Z<<2)-6,4)for Z in xrange(2147483647)),_=C(16384),r=f,U=globals().update))
W.on_mouse_drag=W.on_mouse_motion=lambda x,y,z,Z,b=N(2),m=W.set_mouse_cursor(W.get_system_mouse_cursor("crosshair")),R=(F*3)():A or(L.extend((x,y))or len(L)>3 and any(((P(x,y+(x-L[-2])*(L[-3]-L[-1])/(L[-4]-L[-2]),1,1,6407,5126,R),any(R[:2]))[1]for x in xrange(x,L[-4],cmp(*L[-4::2])or x))if abs(L[-3]-L[-1])<abs(L[-4]-L[-2])else((P(x+(y-L[-1])*(L[-4]-L[-2])/(L[-3]-L[-1]),y,1,1,6407,5126,R),any(R[:2]))[1]for y in xrange(y,L[-3],cmp(*L[-3::2])or y)))and(r(r)if R[1]else U(A=X,B=Y)))
W.on_draw=U(A=U((x,__import__("random").randint(100,500))for x in"XY"),L=[V(*a)for a,b in zip(Z,(G(1),O(0,1,1)))][glEnd():O(0,0,0):R(A+9,B+9,A-9,B-9)][R(X+9,Y+9,X-9,Y-9):O(1,0,0):R(X+4,Y+4,X-4,Y-4)]*0)if A else[V(*(L.pop(0),L.pop(0))if a>2 else L[O(1,1,1):2])for a in xrange(len(L)-12,G(3)or-1,-2)][U(A=glEnd()):]
__import__("pyglet").app.run()
