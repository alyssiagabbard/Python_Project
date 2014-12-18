 # Hello world = $wag mon3y

from Tkinter import *
root = Tk()
import random


drawpad = Canvas(root, width=800,height=600, background='light blue')
player2Side = drawpad.create_rectangle(850,650,0,300, fill='light pink')
box1 = drawpad.create_rectangle(-100,-100, 100, 100, fill = 'light pink')
box2 = drawpad.create_rectangle(850,-100,700,100, fill = 'light pink')
box3 = drawpad.create_rectangle(-100,650,100,500, fill = 'light blue')
box4 = drawpad.create_rectangle(700,500,900,700, fill = 'light blue' )
#Player 1
player = drawpad.create_rectangle(390,570,410,590, fill="black")
rocket1 = drawpad.create_rectangle(400,585,405,590 , fill= "black")
rocket1Fired = False
#Player 2
player2= drawpad.create_rectangle(390,10,410,30, fill="black")
rocket2 = drawpad.create_rectangle(400,15,405,20, fill="black")
rocket2Fired = False 
#Enemies
enemy = drawpad.create_rectangle(50,200,100,210, fill="red")
enemy2 = drawpad.create_rectangle(700,295,770,305, fill = "red")
enemy3 = drawpad.create_rectangle(50,375,100,385, fill = "red")
direction = random.randint(5,10)
direction2= random.randint(-10,-5)
playersSpeed = 20

#ScoreKeeping

    
class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        #Lable
        self.player1Score = 0
        self.player2Score = 0
        self.prompt = "Player 1 Score : " + str(self.player1Score) + "                                    Player 2 Score : " + str(self.player2Score)
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='light green') 
        self.label1.pack()
		
	
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
            global drawpad
            global enemy
            global direction
            global rocket1  
            global rocket2
            global rocket1Fired 
            global rocket2Fired
            global enemy2
            global enemy3
            global direction2
            global player1Score
            global player2Score
            x1,y1,x2,y2 = drawpad.coords(enemy)
            ex1,ey1,ex2,ey2 = drawpad.coords(enemy2)
            eex1,eey1,eex2,eey2 = drawpad.coords(enemy3)
            px1,py1,px2,py2 = drawpad.coords(player)
            rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
            ppx1,ppy1,ppx2,ppy2 = drawpad.coords(player2)
            rrx1,rry1,rrx2,rry2 = drawpad.coords(rocket2)
            
            #Player Score
            player1ScoreAdd = self.rocket1PlayerHit()
            if player1ScoreAdd == True:
                self.player1Score = self.player1Score + 1 
                self.prompt = "Player 1 Score : " + str(self.player1Score) + "                                    Player 2 Score : " + str(self.player2Score)
                self.label1.configure(text=self.prompt)
                
                player1ScoreAdd = False
                
            player2ScoreAdd = self.rocket2PlayerHit()
            if player2ScoreAdd == True:
                self.player2Score = self.player2Score + 1
                self.prompt = "Player 1 Score : " + str(self.player1Score) + "                                    Player 2 Score : " + str(self.player2Score)
                self.label1.configure(text=self.prompt)
                
                player2ScoreAdd = False
                
            if self.player1Score == 3 and self.player2Score == 2:
                self.player1Score = self.player1Score + 1
            player1ScoreAdd = self.rocket1PlayerHit()
            
            
            #Enemy1
            if x2 > 800:
                direction = -direction
            elif x1 < 0:
                direction = direction * -1
            #elif didWeHit == True:
                #drawpad.delete(enemy)
                
            #Enemy2
            elif ex2 >800:
                direction2 = -direction2
            elif ex1<0:
                direction2 = direction2 * -1
                
            #Enemy3
            elif eex2>800:
                direction = -direction
            elif eex1<0:
                direction = direction * -1
            #Rockets
            rocket1HitE = self.rocketHit()
            rocket2HitE = self.rocket2Hit()
            if rocket1Fired == True:
                drawpad.move(rocket1,0,-10)
                if ry2<-5:
                    drawpad.move(rocket1,px1-rx1+6,py1-ry1+10)
                    rocket1Fired = False
                    
                if rocket1HitE == True:
                    
                    drawpad.move(rocket1,px1-rx1+6,py1-ry1+10)
                    rocket1Fired = False
                      
            if rocket2Fired == True:
                drawpad.move(rocket2,0,10)
                if rry2>607:
                    drawpad.move(rocket2,ppx1-rrx1+6,ppy1-rry1-7)
                    rocket2Fired= False
                    
                if rocket2HitE == True:
                    
                    drawpad.move(rocket2,ppx1-rrx1+6,ppy1-rry1-7)
                    rocket2Fired = False
                    
                
            drawpad.move(enemy3, direction, 0)
            drawpad.move(enemy, direction, 0)
            drawpad.move(enemy2, direction2, 0)
            drawpad.after(5,self.animate)
        
        
    def key(self,event):                                                      
        global player
        global rocket1Fired                                                                                                                                                                 
        global drawpad
        global player2
        global rocket2Fired
        global playersSpeed
        px1,py1,px2,py2 = drawpad.coords(player)
        ppx1,ppy1,ppx2,ppy2 = drawpad.coords(player2)
        # Player 2
        if event.keysym == "Up" and ppy1>0:
            drawpad.move(player2, 0,-playersSpeed)
            if rocket2Fired == False:
                drawpad.move(rocket2, 0,-playersSpeed)
        elif event.keysym == "Down" and ppy2 <280:
            drawpad.move(player2, 0,playersSpeed)
            if rocket2Fired == False:
                    drawpad.move(rocket2, 0,playersSpeed)    
        elif event.keysym == "Right" and ppx2<=780:
            drawpad.move(player2, playersSpeed,0)
            if rocket2Fired == False:
                    drawpad.move(rocket2, playersSpeed,0)
        elif event.keysym  == "Left" and ppx1>=10:
            drawpad.move(player2,-playersSpeed,0)
            if rocket2Fired == False:
                    drawpad.move(rocket2, -playersSpeed,0)
        if event.char == "0":
            rocket2Fired = True
        # Player 1
        if event.char == "w" and py1>310: #and didWeHit==False:
            drawpad.move(player,0,-playersSpeed)
            if rocket1Fired == False:                
                drawpad.move(rocket1,0,-playersSpeed)
        elif event.char == "a" and px1>=0: #and didWeHit==False:
            drawpad.move(player,-playersSpeed,0)
            if rocket1Fired == False:
                drawpad.move(rocket1,-playersSpeed,0)
        elif event.char == "s" and py2<600: #and didWeHit==False
            drawpad.move(player,0,playersSpeed)
            if rocket1Fired == False:
                drawpad.move(rocket1,0,playersSpeed)
        elif event.char == "d" and px2<=800: #and didWeHit==False:
            drawpad.move(player,playersSpeed,0)
            if rocket1Fired == False:
                drawpad.move(rocket1,playersSpeed,0)
        if event.char == " ":
            rocket1Fired=True
        if self.player1Score >= 10:
            playersSpeed = 0
            self.label1.configure(text="Player 1 Wins!")
        if self.player2Score >= 10:
            playersSpeed = 0
            self.label1.configure(text="Player 2 Wins!")
            
            
    def rocketHit (self):
        global rocket1
        global enemy1 
        global enemy2 
        global enemy3
        x1,y1,x2,y2 = drawpad.coords(enemy)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy2)
        eex1,eey1,eex2,eey2 = drawpad.coords(enemy3)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        if rx1 > x1 and rx2 < x2:
            return True
        elif ry1 < y1 and ry2 > y2 :
            return True
        elif rx1 > ex1 and rx2 < ex2:
            return True 
        elif ry2 > ey2 and ry1 < ey1:
            return True
        elif rx1 > eex1 and rx2 < eex2:
            return True 
        elif ry2 > eey2 and ry1 < eey1:
            return True
        else:
            return False
            
            
    def rocket2Hit (self):
        global rocket2
        global enemy1 
        global enemy2 
        global enemy3
        x1,y1,x2,y2 = drawpad.coords(enemy)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy2)
        eex1,eey1,eex2,eey2 = drawpad.coords(enemy3)
        rrx1,rry1,rrx2,rry2 = drawpad.coords(rocket2)
        if rrx1 > x1 and rrx2 < x2:
            return True
        elif rry2 > y2 and rry1 < y1:
            return True
        elif rrx1 > ex1 and rrx2 < ex2:
            return True
        elif rry2 > ey2 and rry1 < ey1:
            return True
        elif rrx1 > eex1 and rrx2 < eex2:
            return True
        elif rry2 > eey2 and rry1 < eey1:
            return True
        else:
            return False
        
    
    #Player Score
    def rocket1PlayerHit (self):
        global rocket1
        global player2
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        ppx1,ppy1,ppx2,ppy2 = drawpad.coords(player2)
        if rx1 > ppx1 and rx2 < ppx2 and ry1 < ppy2 and ry2>ppy1:
            return True 
        else:
            return False 
    def rocket2PlayerHit (self):
        global rocket2
        global player 
        rrx1,rry1,rrx2,rry2 = drawpad.coords(rocket2)  
        px1,py1,px2,py2 = drawpad.coords(player)
        if rrx1 > px1 and rrx2 < px2 and rry1 < py2 and rry2 > py1:
            return True 
        else:
            return False         
            


app = myApp(root)
root.mainloop()