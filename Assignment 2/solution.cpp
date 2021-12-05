#include <iostream>
#include <cmath>

double f(double x) {
    return -20 * pow(M_E, -(pow(x, 2) / 8)) - pow(M_E, (0.5 * cos(2 * M_PI * x))) + 20 + M_E;
}

double centralDifferences(double x) {
    double h = 0.0001;
    return (f(x + h) - f(x - h)) / (2 * h);
}

std::string secondDerivative(double x) {
    double h = 0.0001;
    double extrema = (f(x + 2 * h) - (2 * f(x)) + (f(x - 2 * h))) / (4 * pow(h, 2));
    if (extrema > 0) {
        std::cout << extrema << std::endl;
        return "Minimum";
    } else if (extrema < 0) {
        std::cout << extrema << std::endl;
        return "Maximum";
    }
    return "";
}

double gradientDescent(double x) {
    double a = 0.0001;
    double e = 0.0001;
    double iterMax = 100000;
    double count = 0;
    while (fabs(centralDifferences(x)) > e && count < iterMax) {
        x = x - a * centralDifferences(x);
        count++;
    }
    return x;
}

int main() {
    std::cout << secondDerivative(1) << std::endl;
    std::cout << std::fixed << gradientDescent(1) << std::endl;
    return 0;
}
