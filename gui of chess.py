import pygame as p  
import chessengine as ce
images={}

def load_image():
    piece=["wP","wR","wN","wB","wK","wQ","bp","br","bn","bb","bk","bq","wp"]
    for i in piece:
       images[i]=p.transform.scale(p.image.load("image/" + i + ".png"),(64,64))

def main():
    p.init()
    screen=p.display.set_mode((512,512))
    clock=p.time.Clock()
    screen.fill(p.Color("white"))
    gs=ce.Game_State()
    p.display.set_caption("CHESS GAME")
    Icon=p.transform.scale(p.image.load("image/chess.png"),(100,100))
    p.display.set_icon(Icon)
    load_image()    
    running=True
    while running:
        for i in p.event.get():
            if i.type==p.QUIT:
                running=False
        drawgamestate(screen,gs)
        clock.tick(15)
        p.display.flip()

def drawgamestate(screen,gs):
    drawboard(screen)
    drawpiece(screen,gs.chessboard)

def drawboard(screen):
    colors=[p.Color("white"), p.Color("gray")]    
    for i in range(8):
        for j in range(8):
            color=colors[((i+j)%2)]
            p.draw.rect(screen,color,p.Rect(j*64,i*64,64,64))

def drawpiece(screen,board):
    for i in range(8):
        for j in range(8):
            piece=board[i][j]
            if piece!="--":
                screen.blit(images[piece],p.Rect(j*64,i*64,64,64))

if __name__=="__main__":
    main()