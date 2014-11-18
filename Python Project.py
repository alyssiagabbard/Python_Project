# Hello world

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_rectangle(390,580,410,600, fill="light blue")
rocket1 = drawpad.create_rectangle(400,585,405,590)
player2= drawpad.create_rectangle(390,10,410,30, fill="black")
enemy = drawpad.create_rectangle(50,300,100,310, fill="red")
direction = 5


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
        
        def animate(self):
            global drawpad
            global enemy
            global direction
            global rocket
            global rocket1Fired
            didWeHit = self.collisionDetect()
            x1,y1,x2,y2 = drawpad.coords(enemy)
            px1,py1,px2,py2 = drawpad.coords(player)
            rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)

            if x2 > 800:
                direction = - 5
            elif x1 < 0:
                direction = 5
            elif didWeHit == True:
                drawpad.delete(enemy)
            elif rocket1Fired == True:
                drawpad.move(rocket1,0,-5)
            
                if ry2<-5:
                    drawpad.move(rocket1,px1-rx1+6,py1-ry1+6)
                    rocket1Fired = False
                
        
            drawpad.move(enemy, direction, 0)
            drawpad.after(5,self.animate)
        
        
    def key(self,event):
        global player
        global rocket1Fired
        global drawpad
        
        px1,py1,px2,py2 = drawpad.coords(player)
        if event.char == "w" and py1>0: #and didWeHit==False:
            drawpad.move(player,0,-4)
            if rocket1Fired == False:                
                drawpad.move(rocket1,0,-4)
        elif event.char == "a" and px1>=0: #and didWeHit==False:
            drawpad.move(player,-4,0)
            if rocket1Fired == False:
                drawpad.move(rocket1,-4,0)
        elif event.char == "s" and py2<600: #and didWeHit==False
            drawpad.move(player,0,4)
            if rocket1Fired == False:
                drawpad.move(rocket1,0,4)
        elif event.char == "d" and px2<=800: #and didWeHit==False:
            drawpad.move(player,4,0)
            if rocket1Fired == False:
                drawpad.move(rocket1,4,0)
        elif event.char == " ":
            rocket1Fired=True
            self.rockets = self.rockets - 1
            self.rocketsTxt.configure(text=self.rockets)
            
            
app = myApp(root)
root.mainloop()