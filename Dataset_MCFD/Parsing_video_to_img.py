# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam_angle = 8
chute = ['02','05','09','12','18','21']
#chute = ['21']

for scene in chute:
    for angle in range(1,cam_angle+1):
        vid = cv2.VideoCapture("./dataset/chute" + str(scene) + "/cam" + str(angle) + ".avi")

        length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
        print(length)

        try:

            # creating a folder named image
            if not os.path.exists('image'):
                os.makedirs('image')

        # if not created then raise error
        except OSError:
            print('Error: Creating directory of image')

        # frame
        currentframe = 1

        while (True):

            if vid.isOpened():

                # reading from frame
                ret, frame = vid.read()

                if ret:
                    # if video is still left continue creating images
                    name = './image/chute' + str(scene) + '/cam' + str(angle) +\
                            '/chute'+str(scene)+'cam0' + str(angle) + '_'+ str(currentframe) + '.jpg'
                    #print('Creating...' + name)

                    # writing the extracted images
                    cv2.imwrite(name, frame)

                else:
                    break

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1

        # Release all space and windows once done
        vid.release()
        cv2.destroyAllWindows()