#include <GL/glfw.h>
#define P glfwGetMousePos(&a,&b)
#define C(x,y)glColor3f(x,y,y)
int main(){glfwInit();glfwOpenWindow(599,599,0,0,0,0,0,0,GLFW_WINDOW);glOrtho(0,599,599,0,1,-1);glLineWidth(2);srand(glfwGetTime());i:glClear(16384);int s=0,x,y,a,b,c,d,e,f;s:P;e=c=a;f=d=b;C(0,0);glRecti(x-9,y-9,x+9,y+9);while((x=rand()&511)<99);while((y=rand()&511)<99);glRecti(x-9,y-9,x+9,y+9);C(1,0);glRecti(x-4,y-4,x+4,y+4);C(0,1);glRecti(s*6-4,595,s*6,597);s++;C(1,1);do{if((c-a)*(c-a)+(d-b)*(d-b)>63&&a>-1&&b>-1&&a<600&&b<600){int i=0,j=0,k=abs(c-a)>abs(d-b);for(;k?i<abs(c-a):j<abs(d-b);k?i++:j++){if(k)j=d==b?0:i*abs(d-b)/abs(c-a);else i=c==a?0:j*abs(c-a)/abs(d-b);unsigned char g;glReadPixels((c<a?c:a)+i,599-(d<b?d:b)-j,1,1,6407,32818,&g);if(g==255)goto i;if(g==224)goto s;}glBegin(1);glVertex2i(e,f);glVertex2i(e=c,f=d);glEnd();c=a;d=b;}glfwSwapBuffers();P;}while(!glfwGetKey(GLFW_KEY_ESC));}