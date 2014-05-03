#include <GLFW/glfw3.h>
#include <time.h>
#define D;glfwPollEvents();glfwGetCursorPos(w,&a,&b);
#define U(x,y)glColor3f(x,y,y);
#define B(z)glRecti(x-z,y-z,x+z,y+z);
main(){glfwInit();GLFWwindow*w=glfwCreateWindow(599,599,"",0,0);glfwMakeContextCurrent(w);glOrtho(0,599,599,0,0,1);glLineWidth(2);srand(time(0));i:glClear(16384);double a,b;int s=0,x,y,c,d,e,f,g[3];s:U(0,0)D e=c=a;f=d=b;B(9)while((x=rand()&511)<99||(y=rand()&511)<99);B(9)U(1,0)B(4)U(0,1)glRecti(s*6-4,595,s*6,597);s++;U(1,1)while(!glfwGetKey(w,257)&&!glfwWindowShouldClose(w)){int p=abs(c-a),q=abs(d-b),i=0,j=0;if(p*p+q*q>9&&a>0&&b>0&&a<599&&b<599){while(p>q?(j=d==b?:i*q/p,i++<p):(i=c==a?:j*p/q,j++<q)){glReadPixels((c<a?c:a)+i,599-(d<b?d:b)-j,1,1,6407,5122,g);if(g[1])goto i;if(g[0])goto s;}glBegin(1);glVertex2i(e,f);glVertex2i(e=c,f=d);glEnd();c=a;d=b;}glfwSwapBuffers(w);D}}