# Angela Chang
# A computationally generated flower, where a 
# letters on each petal spell out "Processing 2021" 
# and the number "20" is in the center. 
# Look's like a notebook sketch.
# Written in python. Source available at
# Happy 20th Birthday Processing!  Oct. 01, 2021
# Github: anjchang, Twitter: anjchang
# anjchang@gmail.com
anjstr="PROCESSING 2021 "
cnt = 0
def setup():
    global font,font2
    size(2250,3000)
    background(255)
    smooth()
    strokeWeight(1)
    textMode(CENTER)
def draw():
    global cnt,anjstr
    for i in range(0,width,100):
        for j in range(0,height,100):
            stroke(25)
            rect(i,j,width-i,height-i)
    translate(width/2,height/2)
    scale(9)
    stroke(200)
    pushMatrix()
    fill(255)
    for i in range(0,len(anjstr)):
        ellipse(0,-75,50,75)
        fill(0)
        text(anjstr[cnt],-6,-92)
        cnt = (cnt+1)%len(anjstr)
        rotate(TWO_PI/len(anjstr)) 
        fill(255)   
    popMatrix()
    arc(0,-75,50,75,HALF_PI,PI+QUARTER_PI)
    fill(125,125,125,20)
    for i in range(0,15):
        rotate(radians(360/15))
        ellipse(0,-25,50,50)
    fill(255)
    ellipse(0,0,25,25) #center
    stroke(0)
    fill(255,0,0)
    fill(0)
    text("2",-8,5)
    text("0",0,5) 
    saveFrame("Processing20.tif")
    exit()   
    
    
    
    
