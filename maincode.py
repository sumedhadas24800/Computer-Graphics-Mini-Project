import scenery as sin

fig_list = []
sin.rectangle(sin.x_lower, sin.y_lower, sin.y_upper-sin.y_lower, sin.x_upper-sin.x_lower, -1)
print("Let's draw some thing!")
c = 'y'
while (c == 'y' or c == 'Y'):
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
    i = int(input("Enter your option: "))
    print(" ")
    print("No point must be negative.")
    if i == 1:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x1 = int(input("Enter x coordinate of the first point: "))
        y1 = int(input("Enter y coordinate of the first point: "))
        x2 = int(input("Enter x coordinate of the second point: "))
        y2 = int(input("Enter y coordinate of the second point: "))
        if x1 > sin.x_upper or y1 > sin.y_upper or x2 > sin.x_upper or y2 > sin.y_upper or x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
            print("Enter correct input!!!")
        else:
            sin.line(x1, y1, x2, y2, fig_no)
    elif i == 2:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x = int(input("Enter x coordinate of the bottom left corner of the rectangle: "))
        y = int(input("Enter y coordinate of the bottom left corner of the rectangle: "))
        h = int(input("Enter the height (vertical length): "))
        w = int(input("Enter the width (horizontal length): "))
        if x > sin.x_upper or y > sin.y_upper or x + w > sin.x_upper or y + h > sin.y_upper or x < 0 or y < 0:
            print("Enter correct input!!!")
        else:
            sin.rectangle(x, y, h, w, fig_no)
    elif i == 3:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the circle centre: "))
        y_centre = int(input("Enter y coordinate of the circle centre: "))
        radius = int(input("Enter the radius of the circle: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or x_centre + radius > sin.x_upper or y_centre + radius > sin.y_upper or x_centre < 0 or y_centre < 0 or x_centre - radius < 0 or y_centre - radius < 0:
            print("Enter correct input!!!")
        else:
            sin.circle(x_centre, y_centre, radius, fig_no)
    elif i == 4:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the circle centre: "))
        y_centre = int(input("Enter y coordinate of the circle centre: "))
        radius = int(input("Enter the radius of the circle: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or x_centre + radius > sin.x_upper or y_centre + radius > sin.y_upper or x_centre < 0 or y_centre < 0 or x_centre - radius < 0:
            print("Enter correct input!!!")
        else:
            sin.top_semi_ellipse(x_centre, y_centre, radius, radius, fig_no)
    elif i == 5:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the circle centre: "))
        y_centre = int(input("Enter y coordinate of the circle centre: "))
        radius = int(input("Enter the radius of the circle: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or x_centre + radius > sin.x_upper or x_centre < 0 or y_centre < 0 or x_centre - radius < 0 or y_centre - radius < 0:
            print("Enter correct input!!!")
        else:
            sin.down_semi_ellipse(x_centre, y_centre, radius, radius, fig_no)
    elif i == 6:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the circle centre: "))
        y_centre = int(input("Enter y coordinate of the circle centre: "))
        radius = int(input("Enter the radius of the circle: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or x_centre + radius > sin.x_upper or y_centre + radius > sin.y_upper or y_centre - radius < 0 or y_centre < 0 or x_centre < 0:
            print("Enter correct input!!!")
        else:
            sin.right_semi_ellipse(x_centre, y_centre, radius, radius, fig_no)
    elif i == 7:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the circle centre: "))
        y_centre = int(input("Enter y coordinate of the circle centre: "))
        radius = int(input("Enter the radius of the circle: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or y_centre + radius > sin.y_upper or y_centre < 0 or x_centre < 0 or y_centre - radius < 0 or x_centre - radius < 0:
            print("Enter correct input!!!")
        else:
            sin.left_semi_ellipse(x_centre, y_centre, radius, radius, fig_no)
    elif i == 8:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the ellipse centre: "))
        y_centre = int(input("Enter y coordinate of the ellipse centre: "))
        rx = int(input("Enter the value of a of the ellipse: "))
        ry = int(input("Enter the value of b of the ellipse: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or x_centre + rx > sin.x_upper or y_centre + ry > sin.y_upper or x_centre < 0 or y_centre < 0 or x_centre - rx < 0 or y_centre - ry < 0:
            print("Enter correct input!!!")
        else:
            sin.ellipse(x_centre, y_centre, rx, ry, fig_no)
    elif i == 9:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the ellipse centre: "))
        y_centre = int(input("Enter y coordinate of the ellipse centre: "))
        rx = int(input("Enter the value of a of the ellipse: "))
        ry = int(input("Enter the value of b of the ellipse: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or x_centre + rx > sin.x_upper or y_centre + ry > sin.y_upper or x_centre < 0 or y_centre < 0 or x_centre - rx < 0:
            print("Enter correct input!!!")
        else:
            sin.top_semi_ellipse(x_centre, y_centre, rx, ry, fig_no)
    elif i == 10:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the ellipse centre: "))
        y_centre = int(input("Enter y coordinate of the ellipse centre: "))
        rx = int(input("Enter the value of a of the ellipse: "))
        ry = int(input("Enter the value of b of the ellipse: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or x_centre + rx > sin.x_upper or x_centre < 0 or y_centre < 0 or y_centre - ry < 0 or x_centre - rx < 0:
            print("Enter correct input!!!")
        else:
            sin.down_semi_ellipse(x_centre, y_centre, rx, ry, fig_no)
    elif i == 11:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the ellipse centre: "))
        y_centre = int(input("Enter y coordinate of the ellipse centre: "))
        rx = int(input("Enter the value of a of the ellipse: "))
        ry = int(input("Enter the value of b of the ellipse: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or x_centre + rx > sin.x_upper or y_centre + ry > sin.y_upper or x_centre < 0 or y_centre < 0 or y_centre - ry < 0:
            print("Enter correct input!!!")
        else:
            sin.right_semi_ellipse(x_centre, y_centre, rx, ry, fig_no)
    elif i == 12:
        print(" ")
        fig_no = int(input("Enter figure no: "))
        if fig_no not in fig_list:
            fig_list.append(fig_no)
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x_centre = int(input("Enter x coordinate of the ellipse centre: "))
        y_centre = int(input("Enter y coordinate of the ellipse centre: "))
        rx = int(input("Enter the value of a of the ellipse: "))
        ry = int(input("Enter the value of b of the ellipse: "))
        if x_centre > sin.x_upper or y_centre > sin.y_upper or y_centre + ry > sin.y_upper or x_centre < 0 or y_centre < 0 or x_centre - rx < 0 or y_centre - ry < 0:
            print("Enter correct input!!!")
        else:
            sin.left_semi_ellipse(x_centre, y_centre, rx, ry, fig_no)
    elif i == 13:
        print(" ")
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x = int(input("Enter x coordinate of the point: "))
        y = int(input("Enter y coordinate of the point: "))
        fig = int(input("Enter the figure number: "))
        if fig not in fig_list:
            print("Enter correct figure number!!!")
        elif x > sin.x_upper or y > sin.y_upper or x < 0 or y < 0:
            print("Enter correct input!!!")
        else:
            j = sin.inside_outside_test(x, y, fig)
            if j == 0:
                print("The point is present inside the figure ", fig)
            else:
                print("The point is present outside the figure ", fig)
    elif i == 14:
        print(" ")
        print("No point must cross coordinate by x:"+str(sin.x_upper)+"y:"+str(sin.y_upper))
        print(" ")
        x = int(input("Enter x coordinate of an interior point: "))
        y = int(input("Enter y coordinate of an interior point: "))
        if x > sin.x_upper or y > sin.y_upper or x < 0 or y < 0:
            print("Enter correct input!!!")
        else:
            print("1. Red")
            print("2. Yellow")
            print("3. Light Blue")
            print("4. Dark Blue")
            print("5. Orange")
            print("6. Light Green")
            print("7. Dark Green")
            print("8. Violet")
            print("9. Brown")
            print("10.Pink")
            print("11.White")
            print("12.Black")
            print("13.Gray")
            print("14.Custom color")
            j = int(input("Enter choice: "))
            if j > 0 and j < 15:
                if j == 1:
                    c = "#FF0000"
                elif j == 2:
                    c = "#FFFF00"
                elif j == 3:
                    c = "#00BFFF"
                elif j == 4:
                    c = "#000080"
                elif j == 5:
                    c = "#FFA500"
                elif j == 6:
                    c = "#4DEE07"
                elif j == 7:
                    c = "#257303"
                elif j == 8:
                    c = "#8F00FF"
                elif j == 9:
                    c = "#A52A2A"
                elif j == 10:
                    c = "#FFC0CB"
                elif j == 11:
                    c = "#FFFFFF"
                elif j == 12:
                    c = "#000000"
                elif j == 13:
                    c = "#808080"
                elif j == 14:
                    c = input("Enter the hex code of the custom color: ")
                sin.color_fill(x, y, c)
            else:
                print("Enter correct choice!!!")

    c = input("Want to insert another figure or fill color (y/n): ")
sin.display()
