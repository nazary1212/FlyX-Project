import os
import numpy as np
import cv2

def create_dir(path): #creates a directory at a specific path
    try: #allows to catch exceptions
        if not os.path.exists(path):
            os.makedirs(path) #creates a directory if it does not already exist
    except OSError: #catches errors
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_path, save_dir, gap=10):
    name = video_path.split("/")[-1].split(".")[0] #extracts base name of the file, removes / and .  [-1] takes the last element ie the video name 
    save_path = os.path.join(save_dir, name) #constructs the path where the extracted frames will be saved
    create_dir(save_path) #creates the path with folder name

    cap = cv2.VideoCapture(video_path) #reads frames video file 
    idx = 0 # frame index intializer

    while True:
        ret, frame = cap.read() #ret is boolean, confirms if succesfully read
                                #frame is actual frame data
        if ret == False:
            cap.release()
            break

        if idx == 0: #writes first frame into an image file 
            cv2.imwrite(f"{save_path}/{idx}.png", frame) #cv2 function
        else:
            if idx % gap == 0: #rest of frames into an image file 
                cv2.imwrite(f"{save_path}/{idx}.png", frame)

        idx += 1

if __name__ == "__main__":
    # Specify the path to your video file
    video_path = "/Users/ny/Documents/FLYX_PROJECT/Converted_Recordings/test2.mp4" #change final /to recording name

    # Specify the directory where you want to save the extracted frames
    save_dir = "/Users/ny/Documents/FLYX_PROJECT/Extracted_Frames"

    #function call 
    save_frame(video_path, save_dir, gap=390) #gap is how many frames to skip before saving png 
    #FPS : 60 and approx least time between value changes is 6.7 and rounded down to 6.5 seconds to be safe 
    #60*6.5 = 390, value seems to work however could be changed to 400 if needed

    #TO RUN THIS CODE GO INTO MAC TERMINAL 
    # cd /Users/ny/Documents/FLYX_PROJECT   - gets into the folder
    # python VideoToFrame.py - runs the file 

