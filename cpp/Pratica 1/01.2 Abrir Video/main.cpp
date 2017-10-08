#include "opencv2/highgui/highgui.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char* argv[])
{
    VideoCapture cap("Megamind.avi"); // open the video file for reading

    if ( !cap.isOpened() )  { // if not success, exit program
        cout << "Cannot open the video file" << endl;
        return -1;
    }

    double fps = cap.get(CV_CAP_PROP_FPS); //get the frames per seconds of the video
    cout << "Frame per seconds : " << fps << endl;
    namedWindow("MyVideo", WINDOW_AUTOSIZE); //create a window called "MyVideo"

    Mat frame;

    while(1) {
         cap >> frame; // get a new frame from camera
         if(frame.empty()==0) {
            imshow("MyVideo", frame); //show the frame in "MyVideo" window
         }

        if(waitKey(30) == 27) { //wait for 'esc' key press for 30 ms. If 'esc' key is pressed, break loop
            cout << "esc key is pressed by user" << endl;
            break;
        }
    }
    return 0;
}
