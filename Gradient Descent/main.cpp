#include <iostream>
#include <cmath>

double f(double x) {
    return -20 * pow(M_E, -(pow(x, 2) / 8)) - pow(M_E, (0.5 * cos(2 * M_PI * x))) + 20 + M_E;
}

double firstDerivative(double x) {
    double h = 0.0001;
    return (f(x + h) - f(x - h)) / (2 * h);
}

double secondDerivative(double x) {
    double h = 0.0001;
    return (f(x + 2 * h) - (2 * f(x)) + (f(x - 2 * h))) / (4 * pow(h, 2));
}

void extremum(double x) {
    if (secondDerivative(x) > 0) {
        std::cout << "Minimum" << std::endl;
    } else if (secondDerivative(x) < 0) {
        std::cout << "Maximum" << std::endl;
    }
}

double gradientDescent(double x) {
    double e = 0.0001;
    double count = 0;
    double iterMax = 10000;
    while (fabs(firstDerivative(x)) > e && count < iterMax) {
        x = x - (1 / secondDerivative(x)) * firstDerivative(x);
        count++;
    }
    return x;
}

int main() {
    std::cout << std::fixed << gradientDescent(1) << std::endl;
    extremum(gradientDescent(1));
    std::cout << std::fixed << gradientDescent(2) << std::endl;
    extremum(gradientDescent(2));
    std::cout << std::fixed << gradientDescent(3) << std::endl;
    extremum(gradientDescent(3));
    return 0;
}
