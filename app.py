# importing libraries 
import cv2 
import numpy as np 

# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('6.mp4') 

# Check if camera opened successfully 
if (cap.isOpened()== False): 
    print("Error opening video file") 

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
# With webcam get(CV_CAP_PROP_FPS) does not work.
# Let's see for ourselves.
fps = 0
if int(major_ver)  < 3 :
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else :
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

days = 0
hrs = 0
mins = 0
sec = 0
period = '00:00:00:00'

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.
out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))


# Read until video is completed 
while(cap.isOpened()): 
        
    # Capture frame-by-frame 
    ret, frame = cap.read() 
    if ret == True: 

        cfn = cap.get(1)
        if int(cfn)%int(fps)==0:
            if sec > 59:
                sec = 0
                mins = mins+1

            if mins > 59:
                mins = 0
                hrs = hrs+1

            if hrs > 23:
                hrs = 0
                days = days+1

            period = "{:02d}:{:02d}:{:02d}:{:02d}".format(days,hrs,mins,sec)
            sec = sec + 1

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,period,(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
        out.write(frame)
        # Display the resulting frame 
        cv2.imshow('Frame', frame) 

        # Press Q on keyboard to exit 
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break

    # Break the loop 
    else: 
        break

# When everything done, release 
# the video capture object 
cap.release() 
out.release()

# Closes all the frames 
cv2.destroyAllWindows() 
