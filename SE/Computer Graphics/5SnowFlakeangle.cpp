#include<iostream>
    #include<graphics.h>
    #include<math.h>
    using namespace std;

    class snow
    {
       int x,y;
      public:
            int x1,y1,x2,y2,x3,y3,x4,y4;
             void snowflake(int,int,int ,int,int iter);
             void dda(float,float,float,float);
             void draw();
    };

    void snow::snowflake(int x1,int y1,int x2,int y2,int iter)
    {
     float angle = 60*M_PI/180;
     int x3 = (2*x1+x2)/3;
     int y3 = (2*y1+y2)/3;
     
     int x4 = (x1+2*x2)/3;
     int y4 = (y1+2*y2)/3;
     
     int x = x3 + (x4-x3)*cos(angle)+(y4-y3)*sin(angle);
     int y = y3 - (x4-x3)*sin(angle)+(y4-y3)*cos(angle);
     
     if(iter>0)
       {  
        snowflake(x1,y1,x3,y3,iter-1);
        snowflake(x3,y3,x,y,iter-1);
        snowflake(x,y,x4,y4,iter-1);
        snowflake(x4,y4,x2,y2,iter-1);
       }
     
    	else
    	{
    	line(x1,y1,x3,y3);
        	line(x3,y3,x,y);
        	line(x,y,x4,y4);
        	line(x4,y4,x2,y2);
    	}
    }
     
     
    int main()
    {
     
     int gd=DETECT,gm;
     initgraph(&gd,&gm,NULL);
     
     int x1 = 100, y1 = 100, x2 = 400, y2 = 400;
     int x3 = 150, y3= 150, x4 = 450, y4 = 450;
      snow s;
     
      s.snowflake(x1, y1, x2, y2, 4);
      s.snowflake(x2, y2, x3, y3, 4);
      s.snowflake(x1, y1, x2, y2, 4);
      s.snowflake(x4, y4, x2, y2, 4);
      delay(50000);
      closegraph();
      return 0;
}
