#include <GL/glfw.h>
#define D;glfwGetMousePos(&a,&b)
#define U(x,y)glColor3f(x,y,y)
#define B(z)glRecti(x-z,y-z,x+z,y+z)
#define É(x);while((x=rand()&511)<99);
main(){glfwInit();glfwOpenWindow(599,599,0,0,0,0,0,0,65537);gluOrtho2D(0,599,599,0);glLineWidth(2);srand(glfwGetTime());i:glClear(16384);int s=0,x,y,a,b,c,d,e,f,g[3];s:U(0,0)D;e=c=a;f=d=b;B(9)É(x)É(y)B(9);U(1,0);B(4);U(0,1);glRecti(s*6-4,595,s*6,597);s++;U(1,1);do{int p=abs(c-a),q=abs(d-b),i=0,j=0,k=p>q;if(p*p+q*q>9&&a>0&&b>0&&a<600&&b<600){while(k?(j=d==b?:i*q/p,i++<p):(i=c==a?:j*p/q,j++<q)){glReadPixels((c<a?c:a)+i,599-(d<b?d:b)-j,1,1,6407,5122,g);if(g[1])goto i;if(g[0])goto s;}glBegin(1);glVertex2i(e,f);glVertex2i(e=c,f=d);glEnd();c=a;d=b;}glfwSwapBuffers()D;}while(!glfwGetKey(257));}