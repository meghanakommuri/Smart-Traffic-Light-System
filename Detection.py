from time import sleep
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Detection:

    max_lowThreshold = 100
    window_name = 'Edge Map'
    title_trackbar = 'Min Threshold:'
    ratio = 3
    kernel_size = 5



    @staticmethod
    def CannyThreshold(srcgray,img,sno):
        low_threshold = 100
        #img_blur = cv.blur(src_gray, (3,3))
        gausBlur = cv.GaussianBlur(srcgray, (5,5),0)
        detected_edges = cv.Canny(gausBlur, low_threshold, low_threshold*Detection.ratio, Detection.kernel_size)
        mask = detected_edges != 0
        dst = img * (mask[:,:,None].astype(img.dtype))
        #cv.imshow("image "+sno, dst)
        return dst

    @staticmethod
    def EdgeCount(edgecount):
        indices = np.where(edgecount != [0])
        count = 0
        for i in range(len(indices[0])):
                if(indices[0][i]!=0):
                        count += 1
        for i in range(len(indices[1])):
                if(indices[0][i]!=0):
                        count += 1
        #print("count: ", count)
        return count

    @staticmethod
    def ImageRead(image):
        max_lowThreshold = 100
        window_name = 'Edge Map'
        title_trackbar = 'Min Threshold:'
        ratio = 3
        kernel_size = 5

        ref_count=cap1_count=0
        src = cv.imread("road/ref.jpg")
        src1 = cv.imread(image)
        src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        src_gray1 = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)
        edges = Detection.CannyThreshold(src_gray,src,"1")
        edges1 = Detection.CannyThreshold(src_gray1,src1,"2")
        ref_count = Detection.EdgeCount(edges)
        cap1_count = Detection.EdgeCount(edges1)

        plt.subplot(1,2,1),plt.imshow(edges,cmap = 'gray')
        plt.title('Ref. Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(edges1,cmap = 'gray')
        plt.title('Cap. Edge'), plt.xticks([]), plt.yticks([])
        plt.show()

        per = (ref_count/cap1_count)*100
        #print("Percentage: "+"{:.2f}".format(per))
        #cv.waitKey(0)
        return per

    @staticmethod
    def process():
        f=open("tmp.txt","w")

        try:
            per = 0
            #l1=l2=l3=l4=0

            cond=True
            while cond:
                #led's switching
                per = Detection.ImageRead("road/cap1.jpg")
                f.write("Percentage: "+str(per)+"\n")
                if per<50 and per>0:
                    #line 1 turning on
                    f.write("Line 1 is turned ON for 30 sec \n")
                    sleep(3)
                elif per>51 and per<70:
                    f.write("Line 1 is turned ON for 20 sec \n")
                    sleep(2)
                elif per>71 and per<=100:
                    f.write("Line 1 is turned ON for 10 sec \n")
                    sleep(1)
                f.write("Line 1 is turned OFF \n")


                per = Detection.ImageRead("road/cap2.jpg")
                f.write("Percentage: " + str(per)+"\n")
                if per<50 and per>0:
                    #line 2 turning on
                    f.write("Line 2 is turned ON for 30 sec\n")
                    sleep(3)
                elif per>51 and per<70:
                    f.write("Line 2 is turned ON for 20 sec\n")
                    sleep(2)
                elif per>71 and per<=100:
                    f.write("Line 2 is turned ON for 10 sec\n")
                    sleep(1)
                f.write("Line 2 is turned OFF\n")
                per = Detection.ImageRead("road/cap3.jpg")
                f.write("Percentage: " + str(per)+"\n")
                if per<50 and per>0:
                    #line 3 turning on
                    f.write("Line 3 is turned ON for 30 sec\n")
                    sleep(3)
                elif per>51 and per<70:
                    f.write("Line 3 is turned ON for 20 sec\n")
                    sleep(2)
                elif per>71 and per<=100:
                    f.write("Line 3 is turned ON for 10 sec\n")
                    sleep(1)
                f.write("Line 3 is turned OFF\n")

                per = Detection.ImageRead("road/cap4.jpg")
                f.write("Percentage: " + str(per)+"\n")
                if per<50 and per>0:
                    #line 4 turning on
                    f.write("Line 4 is turned ON for 30 sec\n")
                    sleep(3)
                elif per>51 and per<70:
                    f.write("Line 4 is turned ON for 20 sec\n")
                    sleep(2)
                elif per>71 and per<=100:
                    f.write("Line 4 is turned ON for 10 sec\n")
                    sleep(1)
                f.write("Line 4 is turned OFF\n")
                cond=False

        except KeyboardInterrupt:

            print("Program Terminated")
            cv.destroyAllWindows()

if __name__=="__main__":
    Detection.process()

