#include<iostream>
#include<opencv.hpp>
using namespace cv;
using namespace std;
void DFT(Mat&);
int main()
{
	Mat in = imread("1.jpg", CV_LOAD_IMAGE_GRAYSCALE);
	if (in.empty())
		cout << "good";
	DFT(in);
}
void DFT(Mat& I)
{
	Mat O;
	imshow("原始", I);
	waitKey(-1);
	//填充成合适尺寸的图像，便于进行dft
	int m = getOptimalDFTSize(I.rows);//合适行数
	int n = getOptimalDFTSize(I.cols);//合适列数
	copyMakeBorder(I, O, 0, m - I.rows, 0, n - I.cols, BORDER_CONSTANT, Scalar::all(0));//填充
	//增加通道，储存复数
	Mat planes[] = { Mat_<float>(O),Mat::zeros(O.size(),CV_32F) };
	Mat complex;
	merge(planes, 2, complex);
	//dft计算
	dft(complex, complex);
	split(complex, planes);//拆分通道，planes[0]=RE(dft(I)),planes[1]=IM(dft(I))
	magnitude(planes[0], planes[1], planes[0]);//计算功率谱，并输出到planes[0]
	Mat out = planes[0];
	out += Scalar::all(1);
	log(out, out);
	normalize(out, out, 0, 1, CV_MINMAX);
	imshow("未中心化", out);
	waitKey(-1);
	//功率谱图像中心显示
	out = out(Rect(0, 0, out.cols & -2, out.rows & -2));
	int cx = out.cols / 2;
	int cy = out.rows / 2;
	Mat q1 = out(Range(0, cy), Range(0, cx));
	Mat q2 = out(Range(0, cy), Range(cx, out.cols));
	Mat q3 = out(Range(cy, out.rows), Range(0, cx));
	Mat q4 = out(Range(cy, out.rows), Range(cx, out.cols));
	Mat tem;
	q1.copyTo(tem);
	q4.copyTo(q1);
	tem.copyTo(q4);
	q2.copyTo(tem);
	q3.copyTo(q2);
	tem.copyTo(q3);
	imshow("中心化", out);
	waitKey(-1);
}
