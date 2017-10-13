#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

void saltPepperNoise(cv::Mat &image, int n, int tipo);

int main() {
    //Le a imagem
    cv::Mat image;
    image = cv::imread("len_std.png");

    //Mostra a imagem na janela
    cv::namedWindow("Imagem Original"); // define the window
    cv::imshow("Imagem Original", image);
    //Mostra o tamanho da imagem
    std::cout << "Tamanho: " << image.size().height << "x" << image.size().width << std::endl;

    saltPepperNoise(image,1000,0);
    saltPepperNoise(image,1000,255);

    cv::namedWindow("Imagem de saida 2"); // define the window
    cv::imshow("Imagem de saida 2",image);

    cv::imwrite("ImagemRuido.png",image);
    //Espera uma tecla por 5000ms
    cv::waitKey(0);

    return 1;
}

void saltPepperNoise(cv::Mat &image, int n, int tipo) {
    for (int k=0; k<n; k++) {
        // rand() is the MFC random number generator
        // try qrand() with Qt
        int i= rand()%image.cols;
        int j= rand()%image.rows;
        if (image.channels() == 1) { // gray-level image
            image.at<uchar>(j,i)= tipo;
        } else if (image.channels() == 3) { // color image
            image.at<cv::Vec3b>(j,i)[0]= tipo;
            image.at<cv::Vec3b>(j,i)[1]= tipo;
            image.at<cv::Vec3b>(j,i)[2]= tipo;
        }
    }
}
