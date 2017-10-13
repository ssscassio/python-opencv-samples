#include <iostream>
#include <vector>

#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>


void colorReduce(cv::Mat& entrada, cv::Mat& destino, int iBit=1){
    int nl = entrada.rows;                    // number of lines
    int nc = entrada.cols * entrada.channels(); // number of elements per line

    destino = entrada.clone();

    for (int j = 0; j < nl; j++) {
        // get the address of row j
        uchar* data = destino.ptr<uchar>(j);

        for (int i = 0; i < nc; i++) {
            // process each pixel
            data[i] = data[i] >> iBit;
        }
    }
   cv::normalize(destino, destino, 0, 255, CV_MINMAX );
}

int main(int argc, char* argv[])
{
    // Load input image (colored, 3-channel, BGR)
    cv::Mat img256 = cv::imread("len_std.png");

    if (img256.empty()) {
        std::cout << "!!! Failed imread()" << std::endl;
        return -1;
    }

    cv::Mat img128,img64,img32,img16,img8,img4,img2;

    cv::namedWindow("256 Tons",CV_WINDOW_AUTOSIZE);
    cv::normalize(img256, img256, 0, 255, CV_MINMAX );
    cv::imshow("256 Tons", img256);

    colorReduce(img256,img128,1);
    cv::namedWindow("128 Tons",CV_WINDOW_AUTOSIZE);
    cv::imshow("128 Tons", img128);

    colorReduce(img256,img64,2);
    cv::namedWindow("64 Tons",CV_WINDOW_AUTOSIZE);
    cv::imshow("64 Tons", img64);

    colorReduce(img256,img32,3);
    cv::namedWindow("32 Tons",CV_WINDOW_AUTOSIZE);
    cv::imshow("32 Tons", img32);

    colorReduce(img256,img16,4);
    cv::namedWindow("16 Tons",CV_WINDOW_AUTOSIZE);
    cv::imshow("16 Tons", img16);

    colorReduce(img256,img8,5);
    cv::namedWindow("8 Tons",CV_WINDOW_AUTOSIZE);
    cv::imshow("8 Tons", img8);

    colorReduce(img256,img4,6);
    cv::namedWindow("4 Tons",CV_WINDOW_AUTOSIZE);
    cv::imshow("4 Tons", img4);

    colorReduce(img256,img2,7);
    cv::namedWindow("2 Tons",CV_WINDOW_AUTOSIZE);
    cv::imshow("2 Tons", img2);

    cv::waitKey(0);

    return 0;
}
