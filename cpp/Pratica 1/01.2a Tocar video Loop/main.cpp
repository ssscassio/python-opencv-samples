#include "opencv2/highgui/highgui.hpp"
#include <opencv2/opencv.hpp>

#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char* argv[])
{
    VideoCapture cap("Megamind.avi"); // Open the video file for reading

    if ( !cap.isOpened() )  { // If not success, exit program
        cout << "Cannot open the video file" << endl;
        return -1;
    }

    double fps = cap.get(CV_CAP_PROP_FPS); // Get the frames per seconds of the video
    cout << "Frame per seconds : " << fps << endl;
    namedWindow("MyVideo", WINDOW_AUTOSIZE); // Create a window called "MyVideo"

    Mat frame;
    int frame_counter=0;

    while(1) {
         cap >> frame; // Get a new frame from camera
         frame_counter++; // Increments the frame count

         // Check if frame is the last one
         if (frame_counter == cap.get(CV_CAP_PROP_FRAME_COUNT)){
             frame_counter = 0;
             cap.set(CV_CAP_PROP_POS_FRAMES, 0); // Set de video frame back to 0
        }
        if(frame.empty()==0) {
            imshow("MyVideo", frame); //show the frame in "MyVideo" window
        }
        if (waitKey(30) == 27){
            break;
        }
    }
    cap.release();
    return 0;
}
