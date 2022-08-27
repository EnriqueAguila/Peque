from turtle import*
import colorsys
speed (0)
hue = 0.5
bgcolor("black")
for i in range(130):
   col=colorsys.hsv_to_rgb(hue,1,1)
   hue+=0.004
   fillcolor(col)
   begin_fill()
   circle(50-i,190)
   circle(50-i,190)
   rt(00)
   end_fill()