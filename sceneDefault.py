import scenery as sin

sin.rectangle(sin.x_lower, sin.y_lower, sin.y_upper-sin.y_lower, sin.x_upper-sin.x_lower, -1)
print("Default scenery: ")

#hut
sin.top_semi_ellipse(39,58,22,15,1)
sin.top_semi_ellipse(39,73,5,6,1)
sin.rectangle(21,41,17,36,1)
sin.rectangle(35,41,12,8,1)
sin.rectangle(23,48,5,10,1)
sin.rectangle(45,48,5,10,1)

#hill 1
sin.line(0,50,21,50,2)
sin.line(57,50,71,50,2)
sin.line(0,80,24,69,2)
sin.line(57,55,71,50,2)

#hill 2
sin.line(71,50,80,50,3)
sin.line(104,50,150,50,3)
sin.line(64,53,76,59,3)
sin.line(106,74,109,76,4)
sin.line(109,76,150,58,3)

#tree
sin.ellipse(92,62,15,20,4)
sin.line(90,62,90,55,4)
sin.line(90,51,90,0,4)
sin.line(90,51,82,60,4)
sin.line(90,55,82,64,4)
sin.line(94,48,94,0,4)
sin.line(82,60,82,64,4)
sin.line(94,52,94,62,4)
sin.line(92,58,90,62,4)
sin.line(92,58,94,62,4)
sin.line(100,56,94,48,4)
sin.line(94,52,100,60,4)
sin.line(100,56,100,60,4)

#pond
sin.left_semi_ellipse(150,20,50,18,5)

#sun
sin.circle(64,80,8,6)

#road
sin.line(35,41,10,0,7)
sin.line(43,41,70,0,7)

#clouds
sin.ellipse(114,88,30,4,8)
sin.ellipse(26,92,15,3,9)

#bush
sin.top_semi_ellipse(63,32,10,5,10)
sin.top_semi_ellipse(75,23,7,7,11)
sin.top_semi_ellipse(12,26,10,10,12)
sin.top_semi_ellipse(115,40,12,8,12)

#colors
sin.color_fill(40,65,"#CB9D06")     #hut roof
sin.color_fill(39,75,"#CB9D06")     #hut roof
sin.color_fill(39,55,"#D3D3D3")     #hut wall
sin.color_fill(38,47,"#7F2B0A")     #hut door
sin.color_fill(28,50,"#7F2B0A")     #hut window
sin.color_fill(49,50,"#7F2B0A")     #hut window
sin.color_fill(10,62,"#CC8899")     #hill 1
sin.color_fill(60,52,"#CC8899")     #hill 1
sin.color_fill(73,53,"#FF6700")     #hill 2
sin.color_fill(121,58,"#FF6700")    #hill 2
sin.color_fill(93,69,"#3A5F0B")     #tree leaves
sin.color_fill(92,51,"#140D07")     #tree branches
sin.color_fill(91,21,"#140D07")     #tree bark
sin.color_fill(40,18,"#616161")     #road
sin.color_fill(10,18,"#97DC21")     #meadows
sin.color_fill(78,14,"#97DC21")     #meadows
sin.color_fill(101,33,"#97DC21")    #meadows
sin.color_fill(11,31,"#013220")     #bush 1
sin.color_fill(62,34,"#013220")     #bush 2
sin.color_fill(75,26,"#013220")     #bush 3
sin.color_fill(114,43,"#013220")    #bush 4
sin.color_fill(128,20,"#03FDFC")    #pond water
sin.color_fill(47,85,"#00BFFF")     #sky
sin.color_fill(64,80,"#FFCC33")     #sun

sin.display()
exit(0)
