# calling camera function
# calling face/noface function -- if noface, return to camera
# calling identify function

camera()

face = isface()


def stateloop(self):
    print("state: " + str(self.state))
    
    #starts the state machine
    self.state = 0
    
    #camera 
    if self.state == 0:
        #take a picture!
    
    #isface?
    elif self.state == 1:
        # face will return (face_img, self.state)
        if face_img == False:
            self.state = 0
        else self.state = 2  
    
    #if face is too far -- step 1.1
    elif self.state == 1.1:
        print("too far")
        
    #isme?   
    elif self.state == 2:
        #if it is joseph
        if isme:
            print("hello, joseph")
        #if it is not joseph
        else:
            print ("hi! I don't know you")
        
    
    elif self.state == 3:
        
    else:
        print("how the fuck did you get here?")
