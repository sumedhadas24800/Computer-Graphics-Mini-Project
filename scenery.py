import matplotlib.pyplot as plt
                                                           #pre-requisite variables
x_lower=0                                                  #lower limit of x axis
x_upper=150                                                #upper limit of x axis
y_lower=0                                                  #lower limit of y axis
y_upper=150                                                #upper limit of y axis
x_axis=list(range(x_lower,x_upper+1))                      #list of markings for x axis
y_axis=list(range(y_lower,y_upper+1))                      #list of markings for y axis
fig_size=18                                                #figure size of the graph
r=max(x_upper-x_lower,y_upper-y_lower)                     #maximum range
pix=55.5*fig_size/r                                        #pixel size;factors figure size(f),maximum range(r);constant=55.5[calculated]
shape='s'                                                  #pixel shape
col='black'                                                #pixel color
plt.rcParams['figure.figsize'] = [fig_size,fig_size]
plt.xlim(x_lower,x_upper)
plt.ylim(y_lower,y_upper)
rows, cols = (160, 160)                                   
color_plot_list = [[0]*cols]*rows                          #1 if pixel color is black
color_plot_list = [ k.copy() for k in color_plot_list ]
fig_plot_list=[[0]*cols]*rows                              #tell occupying figure of a pixel
fig_plot_list=[ k.copy() for k in color_plot_list ]
                                                           #function to plot a pixel at a desired position
def pixel(x,y):
    plt.plot(x,y,marker=shape,ms=pix,color=col)
                                                           #bresenham_line_drawing_algo    
def line(x1,y1,x2,y2,fig_no):
    dx=x2-x1
    dy=y2-y1
    x=[x1]
    y=[y1]
    pixel(x1,y1)
    color_plot_list[x1][y1]=1
    if dx==0:
        for i in range(min(y1,y2),max(y1,y2)):
            x.append(x1)
            y1=y1+1
            y.append(y1)
            pixel(x1,y1)
            color_plot_list[x1][y1]=1
            fig_plot_list[x1][y1]=fig_no
    elif dy==0:
        for i in range(min(x1,x2),max(x1,x2)):
            x1=x1+1
            x.append(x1)
            y.append(y1)
            pixel(x1,y1)
            color_plot_list[x1][y1]=1
            fig_plot_list[x1][y1]=fig_no
    elif dy/dx>0 and dy/dx<=1:
        p=2*dy-dx
        for i in range(x1,x2):
            x1=x1+1
            x.append(x1)
            if p<0:
                p=p+2*dy
            else:
                p=p+2*dy-2*dx
                y1=y1+1
            y.append(y1)
            pixel(x1,y1)
            color_plot_list[x1][y1]=1
            fig_plot_list[x1][y1]=fig_no
    elif dy/dx>1:
        p=2*dx-dy
        for i in range(y1,y2):
            y1=y1+1
            y.append(y1)
            if p<0:
                p=p+2*dx
            else:
                p=p+2*dx-2*dy
                x1=x1+1
            x.append(x1)
            pixel(x1,y1)
            color_plot_list[x1][y1]=1
            fig_plot_list[x1][y1]=fig_no
    elif dy/dx<0:
        x=[x2]
        y=[y2]
        x2=x1+2*dx
        y2=y1
        x1=x[0]
        y1=y[0]
        if dy/dx>=-1:
            dy=y2-y1
            p=2*dy-dx
            for i in range(x1,x2):
                x1=x1+1
                x.append(2*x[0]-x1)
                if p<0:
                    p=p+2*dy
                else:
                    p=p+2*dy-2*dx
                    y1=y1+1
                y.append(y1)
                pixel(2*x[0]-x1,y1)
                zz=2*x[0]
                color_plot_list[zz][y1]=1
                fig_plot_list[zz][y1]=fig_no
        else:
            dx=x2-x1
            p=2*dx-dy
            for i in range(y1,y2):
                y1=y1+1
                y.append(y1)
                if p<0:
                    p=p+2*dx
                else:
                    p=p+2*dx-2*dy
                    x1=x1+1
                x.append(2*x[0]-x1)
                pixel(2*x[0]-x1,y1)
                zz=2*x[0]-x1
                color_plot_list[zz][y1]=1
                fig_plot_list[zz][y1]=fig_no

                                                                  #generating_rectangle
def rectangle(x,y,h,w,fig_no):
	line(x,y,x,y+h,fig_no)
	line(x,y+h,x+w,y+h,fig_no)
	line(x,y,x+w,y,fig_no)
	line(x+w,y,x+w,y+h,fig_no)  
  
                                                                  #generating circle
def circle(x_centre, y_centre, r,fig_no):
	xk=0
	yk=r
	pk=5/4-r
	pixel(xk+x_centre,yk+y_centre)
	color_plot_list[xk+x_centre][yk+y_centre]=1
	fig_plot_list=fig_no
	pixel(yk+x_centre,xk+y_centre)
	color_plot_list[yk+x_centre][xk+y_centre]=1
	fig_plot_list[yk+x_centre][xk+y_centre]=fig_no
	pixel(yk+x_centre,-xk+y_centre)
	color_plot_list[yk+x_centre][-xk+y_centre]=1
	fig_plot_list[yk+x_centre][-xk+y_centre]=fig_no
	pixel(xk+x_centre,-yk+y_centre)
	color_plot_list[xk+x_centre][-yk+y_centre]=1
	fig_plot_list[xk+x_centre][-yk+y_centre]=fig_no
	pixel(-xk+x_centre,-yk+y_centre)
	color_plot_list[-xk+x_centre][-yk+y_centre]=1
	fig_plot_list[-xk+x_centre][-yk+y_centre]=fig_no
	pixel(-yk+x_centre,-xk+y_centre)
	color_plot_list[-yk+x_centre][-xk+y_centre]=1
	fig_plot_list[-yk+x_centre][-xk+y_centre]=fig_no
	pixel(-yk+x_centre,xk+y_centre)
	color_plot_list[-yk+x_centre][xk+y_centre]=1
	fig_plot_list[-yk+x_centre][xk+y_centre]=fig_no
	pixel(-xk+x_centre,yk+y_centre)
	color_plot_list[-xk+x_centre][yk+y_centre]=1
	fig_plot_list[-xk+x_centre][yk+y_centre]=fig_no
	while xk<yk:
		xk=xk+1
		if pk<0:
			pk=pk+2*xk+1
		else:
			yk=yk-1
			pk=pk+2*xk-2*yk+1
	pixel(xk+x_centre,yk+y_centre)
	color_plot_list[xk+x_centre][yk+y_centre]=1
	fig_plot_list[xk+x_centre][yk+y_centre]=fig_no
	pixel(yk+x_centre,xk+y_centre)
	color_plot_list[yk+x_centre][xk+y_centre]=1
	fig_plot_list[yk+x_centre][xk+y_centre]=fig_no
	pixel(yk+x_centre,-xk+y_centre)
	color_plot_list[yk+x_centre][-xk+y_centre]=1
	fig_plot_list[yk+x_centre][-xk+y_centre]=fig_no
	pixel(xk+x_centre,-yk+y_centre)
	color_plot_list[xk+x_centre][-yk+y_centre]=1
	fig_plot_list[xk+x_centre][-yk+y_centre]=fig_no
	pixel(-xk+x_centre,-yk+y_centre)
	color_plot_list[-xk+x_centre][-yk+y_centre]=1
	fig_plot_list[-xk+x_centre][-yk+y_centre]=fig_no
	pixel(-yk+x_centre,-xk+y_centre)
	color_plot_list[-yk+x_centre][-xk+y_centre]=1
	fig_plot_list[-yk+x_centre][-xk+y_centre]=fig_no
	pixel(-yk+x_centre,xk+y_centre)
	color_plot_list[-yk+x_centre][xk+y_centre]=1
	fig_plot_list[-yk+x_centre][xk+y_centre]=fig_no
	pixel(-xk+x_centre,yk+y_centre)
	color_plot_list[-xk+x_centre][yk+y_centre]=1
	fig_plot_list[-xk+x_centre][yk+y_centre]=fig_no

                                                                         #generating ellipse
def ellipse(a,b,rx,ry,fig_no):
    x=0
    y=ry
    pk=ry*ry+0.25*rx*rx-rx*rx*y
    while 2*ry*ry*x<2*rx*rx*y:
        if pk<0:
            pk=pk+ry*ry*(1+2*(x+1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y+0
        else:
            pk=pk+ry*ry*(1+2*(x+1))+2*rx*rx*(1-y)
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y-1
    pk=ry*ry*(x+0.5)**2+rx*rx*(y-1)**2-rx*rx*ry*ry
    while 2*ry*ry*x>=2*rx*rx*y:
        if x==rx and y==0:
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            break
        elif pk<0:
            pk=pk+2*ry*ry*(x+1)+rx*rx*(1-2*(y-1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y-1
        else:
            pk=pk+rx*rx*(1-2*(y-1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+0
            y=y-1
                                                                       #generating_top_semi_ellipse
def top_semi_ellipse(a,b,rx,ry,fig_no):
    x=0
    y=ry
    pk=ry*ry+0.25*rx*rx-rx*rx*y
    while 2*ry*ry*x<2*rx*rx*y:
        if pk<0:
            pk=pk+ry*ry*(1+2*(x+1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            x=x+1
            y=y+0
        else:
            pk=pk+ry*ry*(1+2*(x+1))+2*rx*rx*(1-y)
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            x=x+1
            y=y-1
    pk=ry*ry*(x+0.5)**2+rx*rx*(y-1)**2-rx*rx*ry*ry
    while 2*ry*ry*x>=2*rx*rx*y:
        if x==rx and y==0:
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            break
        elif pk<0:
            pk=pk+2*ry*ry*(x+1)+rx*rx*(1-2*(y-1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            x=x+1
            y=y-1
        else:
            pk=pk+rx*rx*(1-2*(y-1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            x=x+0
            y=y-1
    for i in range(-rx+a,rx+a+1):
        pixel((i),(b))
        color_plot_list[i][b]=1
        fig_plot_list[i][b]=fig_no
                                                                        #generating_down_semi_ellipse
def down_semi_ellipse(a,b,rx,ry,fig_no):
    x=0
    y=ry
    pk=ry*ry+0.25*rx*rx-rx*rx*y
    while 2*ry*ry*x<2*rx*rx*y:
        if pk<0:
            pk=pk+ry*ry*(1+2*(x+1))
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y+0
        else:
            pk=pk+ry*ry*(1+2*(x+1))+2*rx*rx*(1-y)
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y-1
    pk=ry*ry*(x+0.5)**2+rx*rx*(y-1)**2-rx*rx*ry*ry
    while 2*ry*ry*x>=2*rx*rx*y:
        if x==rx and y==0:
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            break
        elif pk<0:
            pk=pk+2*ry*ry*(x+1)+rx*rx*(1-2*(y-1))
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y-1
        else:
            pk=pk+rx*rx*(1-2*(y-1))
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+0
            y=y-1
    for i in range(-rx+a,rx+a+1):
        pixel((i),(b))
        color_plot_list[i][b]=1
        fig_plot_list[i][b]=fig_no
                                                                         #generating_right_semi_ellipse
def right_semi_ellipse(a,b,rx,ry,fig_no):
    x=0
    y=ry
    pk=ry*ry+0.25*rx*rx-rx*rx*y
    while 2*ry*ry*x<2*rx*rx*y:
        if pk<0:
            pk=pk+ry*ry*(1+2*(x+1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            x=x+1
            y=y+0
        else:
            pk=pk+ry*ry*(1+2*(x+1))+2*rx*rx*(1-y)
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            x=x+1
            y=y-1
    pk=ry*ry*(x+0.5)**2+rx*rx*(y-1)**2-rx*rx*ry*ry
    while 2*ry*ry*x>=2*rx*rx*y:
        if x==rx and y==0:
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            break
        elif pk<0:
            pk=pk+2*ry*ry*(x+1)+rx*rx*(1-2*(y-1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            x=x+1
            y=y-1
        else:
            pk=pk+rx*rx*(1-2*(y-1))
            pixel((x+a),(y+b))
            color_plot_list[x+a][y+b]=1
            fig_plot_list[x+a][y+b]=fig_no
            pixel((x+a),(-y+b))
            color_plot_list[x+a][-y+b]=1
            fig_plot_list[x+a][-y+b]=fig_no
            x=x+0
            y=y-1
    for i in range(-ry+b,ry+b+1):
        pixel((a),(i))
        color_plot_list[a][i]=1
        fig_plot_list[a][i]=fig_no
                                                                            #generating_left_semi_ellipse
def left_semi_ellipse(a,b,rx,ry,fig_no):
    x=0
    y=ry
    pk=ry*ry+0.25*rx*rx-rx*rx*y
    while 2*ry*ry*x<2*rx*rx*y:
        if pk<0:
            pk=pk+ry*ry*(1+2*(x+1))
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y+0
        else:
            pk=pk+ry*ry*(1+2*(x+1))+2*rx*rx*(1-y)
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y-1
    pk=ry*ry*(x+0.5)**2+rx*rx*(y-1)**2-rx*rx*ry*ry
    while 2*ry*ry*x>=2*rx*rx*y:
        if x==rx and y==0:
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            break
        elif pk<0:
            pk=pk+2*ry*ry*(x+1)+rx*rx*(1-2*(y-1))
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+1
            y=y-1
        else:
            pk=pk+rx*rx*(1-2*(y-1))
            pixel((-x+a),(y+b))
            color_plot_list[-x+a][y+b]=1
            fig_plot_list[-x+a][y+b]=fig_no
            pixel((-x+a),(-y+b))
            color_plot_list[-x+a][-y+b]=1
            fig_plot_list[-x+a][-y+b]=fig_no
            x=x+0
            y=y-1
    for i in range(-ry+b,ry+b+1):
        pixel((a),(i))
        color_plot_list[a][i]=1
        fig_plot_list[a][i]=fig_no
                                                                               #color_filling_method
def color_fill(x,y,c):                         
    current=color_plot_list[x][y]
    if current!=1 and current!=2:
        plt.plot(x,y,marker=shape,ms=pix,color=c)
        color_plot_list[x][y]=2
        color_fill(x-1,y,c)
        color_fill(x+1,y,c)
        color_fill(x,y+1,c)
        color_fill(x,y-1,c)
                                                                               #inside_outside_test_method
def inside_outside_test(x,y,fig_no):
    c=0
    for i in range(x,x_upper):
        if fig_plot_list[i][y]==fig_no:
            c=c+1
    return c%2
                                                                               #displaying_picture
def display():
	plt.gca().set_aspect('equal',adjustable='box')
	plt.show()	
