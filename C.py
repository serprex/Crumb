from random import*
from pyglet import*
from pyglet.gl import*
run,o,n,g,i,i.on_draw=lambda:glClear(g(r=1,c=1,_=iter(range(16384)))or 16384),glColor3f,glRecti,globals().update,window.Window(599,599),lambda:g(r=g(p=randint(99,512),e=randint(99,512)),l=(o(0,1,1),n(next(_)*4-6,2,next(_)*4-6,4),o(0,0,0),n(r+9,c+9,r-9,c-9),n(p+9,e+9,p-9,e-9),o(1,0,0),n(p+4,e+4,p-4,e-4))and[])if r else(glBegin(3),o(1,1,1))and[glVertex2f(l.pop(0),l.pop(0))for a in range(len(l)/2-6)]and glVertex2f(*l[:2])or g(r=glEnd())
i.on_mouse_drag=i.on_mouse_motion=lambda a,o,m,_=run(),b=glLineWidth(2),i=i.set_mouse_cursor (i.get_system_mouse_cursor ("crosshair")),n=(GLint*3)():r or(l.extend((a,o))or len(l)>3and((lambda e:any(glReadPixels(*(((a,o)[e]+(p-l[-1-e])*(l[e-4]-l[e-2])/(l[-3-e]-l[-1-e]),p)[::1-e-e]+(1,1,6407,5122,n)))or n[0]for p in range((o,a)[e],l[-3-e],cmp(*l[-3-e::2]))))(abs(l[-4]-l[-2])>abs(l[-3]-l[-1])))and(g(r=p,c=e)or n[1])and run())
app.run()