#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;

int main() {
    //Le a imagem
    cv::Mat image,redimensionada;
    image = cv::imread("len_std.png");
    //Mostra a imagem na janela
    cv::namedWindow("Imagem 256x256"); // define a janela
    cv::imshow("Imagem 256x256", image);

    cv::resize(image,redimensionada,Size(128,128));

    //Mostra a imagem na janela
    cv::namedWindow("Imagem 128x128"); // define a janela
    cv::imshow("Imagem 128x128", redimensionada);

    cv::imwrite("lena128x128.png",redimensionada);

    cv::waitKey(0);

    return 1;
}


