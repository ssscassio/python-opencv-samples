#include "opencv2/highgui/highgui.hpp"
#include <iostream>

using namespace cv;

int main(int, char**)
{
    VideoCapture capUm(0); // open the default camera
    capUm.set(CV_CAP_PROP_FRAME_WIDTH,640);
    capUm.set(CV_CAP_PROP_FRAME_HEIGHT,480);
    capUm.set(CV_CAP_PROP_FPS,15);

    if(!capUm.isOpened())  // check if we succeeded
        return -1;

    Mat frame;
    namedWindow("Frame",WINDOW_NORMAL);
    while(1){
        capUm >> frame; // get a new frame from camera
        if(frame.empty()==0) {
            imshow("Frame", frame);
            if (waitKey(30) == 27){
                break;
            }
        }
    }
    capUm.release();
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
