import scenery as sin
fig_list=[]
print("Let's draw some thing!")
c='y'
while(c=='y' or c=='Y'):
	print(" ")
	print("1. Draw a line")
	print("2. Draw a rectangle")
	print("3. Draw a circle")
	print("4. Draw a top semi circle")
	print("5. Draw a bottom semi circle")
	print("6. Draw a right semi circle")
	print("7. Draw a left semi circle")
	print("8. Draw an ellipse")
	print("9. Draw a top semi ellipse")
	print("10.Draw a bottom semi ellipse")
	print("11.Draw a right semi ellipse")
	print("12.Draw a left semi ellipse")
	print("13.Inside Outside Test")
	print("14.Fill color")
	print(" ")
	i=int(input("Enter your option: "))
	print(" ")
	print("No point must be negative!!!")
	if i==1:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x1=int(input("Enter first point x coordinate: "))
		y1=int(input("Enter first point y coordinate: "))
		x2=int(input("Enter second point x coordinate: "))
		y2=int(input("Enter second point y coordinate: "))
		if x1>150 or y1>150 or x2>150 or y2>150 or x1<0 or x2<0 or y1<0 or y2<0:
			print("Enter correct input!!!")
		else:
			sin.line(x1,y1,x2,y2,fig_no)
	elif i==2:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x=int(input("Enter the x coordinate of the bottom left corner of the rectangle: "))
		y=int(input("Enter the y coordinate of the bottom left corner of the rectangle: "))
		h=int(input("Enter the height (vertical length): "))
		w=int(input("Enter the width (horizontal length): "))
		if x>150 or y>150 or x+w>150 or y+h>150 or x<0 or y<0:
			print("Enter correct input!!!")
		else:
			sin.rectangle(x,y,h,w,fig_no)
	elif i==3:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of circle centre: "))
		y_centre=int(input("Enter y coordinate of circle centre: "))
		radius=int(input("Enter the radius of circle: "))
		if x_centre>150 or y_centre>150 or x_centre+radius>150 or y_centre+radius>150 or x_centre<0 or y_centre<0 or x_centre-radius<0 or y_centre-radius<0:
			print("Enter correct input!!!")
		else:
			sin.circle(x_centre,y_centre,radius,fig_no)
	elif i==4:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of circle centre: "))
		y_centre=int(input("Enter y coordinate of circle centre: "))
		radius=int(input("Enter the radius of circle: "))
		if x_centre>150 or y_centre>150 or x_centre+radius>150 or y_centre+radius>150 or x_centre<0 or y_centre<0 or x_centre-radius<0:
			print("Enter correct input!!!")
		else:
			sin.top_semi_ellipse(x_centre,y_centre,radius,radius,fig_no)
	elif i==5:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of circle centre: "))
		y_centre=int(input("Enter y coordinate of circle centre: "))
		radius=int(input("Enter the radius of circle: "))
		if x_centre>150 or y_centre>150 or x_centre+radius>150 or x_centre<0 or y_centre<0 or x_centre-radius<0 or y_centre-radius<0:
			print("Enter correct input!!!")
		else:
			sin.down_semi_ellipse(x_centre,y_centre,radius,radius,fig_no)
	elif i==6:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of circle centre: "))
		y_centre=int(input("Enter y coordinate of circle centre: "))
		radius=int(input("Enter the radius of circle: "))
		if x_centre>150 or y_centre>150 or x_centre+radius>150 or y_centre+radius>150 or y_centre-radius<0 or y_centre<0 or x_centre<0:
			print("Enter correct input!!!")
		else:
			sin.right_semi_ellipse(x_centre,y_centre,radius,radius,fig_no)
	elif i==7:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of circle centre: "))
		y_centre=int(input("Enter y coordinate of circle centre: "))
		radius=int(input("Enter the radius of circle: "))
		if x_centre>150 or y_centre>150 or y_centre+radius>150 or y_centre<0 or x_centre<0 or y_centre-radius<0 or x_centre-radius<0 :
			print("Enter correct input!!!")
		else:
			sin.left_semi_ellipse(x_centre,y_centre,radius,radius,fig_no)
	elif i==8:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of circle centre: "))
		y_centre=int(input("Enter y coordinate of circle centre: "))
		rx=int(input("Enter the major axis of the ellipse: "))
		ry=int(input("Enter the minor axis of the ellipse: "))
		if x_centre>150 or y_centre>150 or x_centre+rx>150 or y_centre+ry>150 or x_centre<0 or y_centre<0 or x_centre-rx<0 or y_centre-ry<0:
			print("Enter correct input!!!")
		else:
			sin.ellipse(x_centre,y_centre,rx,ry,fig_no)
	elif i==9:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of ellipse centre: "))
		y_centre=int(input("Enter y coordinate of ellipse centre: "))
		rx=int(input("Enter the major axis of the ellipse: "))
		ry=int(input("Enter the minor axis of the ellipse: "))
		if x_centre>150 or y_centre>150 or x_centre+rx>150 or y_centre+ry>150 or x_centre<0 or y_centre<0 or x_centre-rx<0:
			print("Enter correct input!!!")
		else:
			sin.top_semi_ellipse(x_centre,y_centre,rx,ry,fig_no)
	elif i==10:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of ellipse centre: "))
		y_centre=int(input("Enter y coordinate of ellipse centre: "))
		rx=int(input("Enter the major axis of the ellipse: "))
		ry=int(input("Enter the minor axis of the ellipse: "))
		if x_centre>150 or y_centre>150 or x_centre+rx>150 or x_centre<0 or y_centre<0 or y_centre-ry<0 or x_centre-rx<0:
			print("Enter correct input!!!")
		else:
			sin.down_semi_ellipse(x_centre,y_centre,rx,ry,fig_no)
	elif i==11:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of ellipse centre: "))
		y_centre=int(input("Enter y coordinate of ellipse centre: "))
		rx=int(input("Enter the major axis of the ellipse: "))
		ry=int(input("Enter the minor axis of the ellipse: "))
		if x_centre>150 or y_centre>150 or x_centre+rx>150 or y_centre+ry>150 or x_centre<0 or y_centre<0 or y_centre-ry<0:
			print("Enter correct input!!!")
		else:
			sin.right_semi_ellipse(x_centre,y_centre,rx,ry,fig_no)
	elif i==12:
		print(" ")
		fig_no=int(input("Enter figure no: "))
		if fig_no not in fig_list:
			fig_list.append(fig_no)
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x_centre=int(input("Enter x coordinate of ellipse centre: "))
		y_centre=int(input("Enter y coordinate of ellipse centre: "))
		rx=int(input("Enter the major axis of the ellipse: "))
		ry=int(input("Enter the minor axis of the ellipse: "))
		if x_centre>150 or y_centre>150 or y_centre+ry>150 or x_centre<0 or y_centre<0 or x_centre-rx<0 or y_centre-ry<0:
			print("Enter correct input!!!")
		else:
			sin.left_semi_ellipse(x_centre,y_centre,rx,ry,fig_no)
	elif i==13:
		print(" ")
		print("No point must cross coordinate by x:150 y:150")
		print(" ")
		x=int(input("Enter x coordinate: "))
		y=int(input("Enter y coordinate: "))
		fig=int(input("Enter the figure number: "))
		if fig not in fig_list:
			print("Enter correct figure number!!!")
		elif x>150 or y>150 or x<0 or y<0:
			print("Enter correct input!!!")
		else:
			j=sin.inside_outside_test(x,y,fig)
			if j==0:
				print("The point is present inside the figure ",fig)
			else:
				print("The point is present outside the figure ",fig)
	elif i==14:
		print(" ")
		print("Point must cross coordinate by x:150 y:150")
		print(" ")
		x=int(input("Enter x coordinate of interior point: "))
		y=int(input("Enter y coordinate of interior point: "))
		if x>150 or y>150 or x<0 or y<0:
			print("Enter correct input!!!")
		else:
			print("1. Sky Blue")
			print("2. Prussian Blue")
			print("3. Light Green")
			print("4. Deep Green")
			print("5. Red")
			print("6. Yellow")
			print("7. Brown")
			print("8. Pink")
			print("9. Orange")
			print("10.Black")
			j=int(input("Enter color number: "))
			if j>0 and j<11:
				if j==1:
					c="#1CE7D8"
				elif j==2:
					c="#0A5279"
				elif j==3:
					c="#4DEE07"
				elif j==4:
					c="#257303"
				elif j==5:
					c="#F90404"
				elif j==6:
					c="#F9F504"
				elif j==7:
					c="#A52A2A"
				elif j==8:
					c="#FFC0CB"
				elif j==9:
					c="#FFA500"
				elif j==10:
					c="#000000"
				sin.color_fill(x,y,c)
			else:
				print("Enter correct color number!!!")
		
	c=input("Want to insert another figure or fill color (y/n): ")
sin.display()
