#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

int main() {
    //Le a imagem
    cv::Mat image;

    image = cv::imread("len_std.png",1);
    //Mostra a imagem na janela
    cv::namedWindow("Imagem Original"); // define a janela
    cv::imshow("Imagem Original", image);
    //Mostra o tamanho da imagem
    std::cout << "Tamanho: " << image.size().height << "x" << image.size().width << std::endl;

    cv::waitKey(0);

    return 1;
}


