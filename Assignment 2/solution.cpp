#include <iostream>
#include <cmath>

using namespace std;

double f(double x) {
    double e = 2.71828;
    return pow(-20 * e, -(pow(x, 2) / 8)) - (pow(e, (0.5 * cos(2 * M_PI * x))) + 20 + e);
}

double centralDifferences(double x, double h = 0.000001) {
    return (f(x + h) - f(x - h)) / 2 * h;
}

void gradientDescent(double x, double epsilon = 0.000001, double iterMax = 10000, double alpha = 0.000001) {
    double count = 0;
    while (centralDifferences(x) > epsilon && count < iterMax) {
        x = x - alpha * centralDifferences(x);
        count = count + 1;
    }
}

int main() {
    return 0;
}
