from ursina import *

# Create the app

app = Ursina()

# Set up your scene (sky, camera, lighting, etc.)
Sky()



app = Ursina()
Sky()
turn = ''
win = False   
class Box(Entity):
    def __init__(self, type=turn, model='cube', texture='base.png', position=(0,0,0), collider='box'):
        super().__init__(model=model, texture='base.png', position=position, collider=collider)
        self.type = type
        self.clicked = False

    def input(self, key):
        global turn
        if self.hovered and key == 'left mouse down' and not self.clicked:
         self.clicked = True

         if turn == 'x':
                self.texture = 'x.png'
                self.type = 'x'  # update type!
                turn = 'o'
         else:
             self.texture = 'o.png'
             self.type = 'o'  # update type!
             turn = 'x'


# Example player cube
player1 = Box(model='cube',texture='base.png',position=(1, 1, 0),collider='box')
player2 = Box(model='cube',texture='base.png',position=(0, 1, 0),collider='box')
player3 = Box(model='cube',texture='base.png',position=(-1, 1, 0),collider='box')
player4 = Box(model='cube',texture='base.png',position=(1, 0, 0),collider='box')
player5 = Box(model='cube',texture='base.png',position=(0, 0, 0),  collider='box')
player6 = Box(model='cube',texture='base.png',position=(-1, 0, 0),collider='box')
player7 = Box(model='cube',texture='base.png',position=(1, -1, 0), collider='box')
player8 = Box(model='cube',texture='base.png',position=(0,-1 , 0),collider='box')
player9 = Box(model='cube',texture='base.png',position=(-1, -1, 0),collider='box')
# Start the app


def update():
    global win
    # x win conditions
    if player1.type == 'x' and player2.type== 'x' and player3.type == 'x':
        win = True    
    if player1.type == 'x' and player5.type== 'x' and player9.type == 'x':
        win = True   
    if player1.type == 'x' and player4.type== 'x' and player7.type == 'x':
        win = True     
    if player4.type == 'x' and player5.type== 'x' and player6.type == 'x':
        win = True  
    if player3.type == 'x' and player5.type== 'x' and player7.type == 'x':
        win = True      
    if player3.type == 'x' and player6.type== 'x' and player9.type == 'x':
        win = True    
    if player2.type == 'x' and player4.type== 'x' and player6.type == 'x':
        win = True    
    if player7.type == 'x' and player8.type== 'x' and player9.type == 'x':
        win = True    

    # o win conditions     
    if player1.type == 'o' and player2.type== 'o' and player3.type == 'o':
        win = True    
    if player1.type == 'o' and player5.type== 'o' and player9.type == 'o':
        win = True   
    if player1.type == 'o' and player4.type== 'o' and player7.type == 'o':
        win = True     
    if player4.type == 'o' and player5.type== 'o' and player6.type == 'o':
        win = True  
    if player3.type == 'o' and player5.type== 'o' and player7.type == 'o':
        win = True      
    if player3.type == 'o' and player6.type== 'o' and player9.type == 'o':
        win = True    
    if player2.type == 'o' and player4.type== 'o' and player6.type == 'o':
        win = True    
    if player7.type == 'o' and player8.type== 'o' and player9.type == 'o':
        win = True    

    # Reset board when 'r' is pressed
    if held_keys['r']:
        boxes = [player1, player2, player3, player4, player5, player6, player7, player8, player9]
        for box in boxes:
            box.type = ''
            box.texture = 'base.png'
            box.clicked = False  # allow clicking again
        win = False

    
app.run()
