#include <iostream>
#include <cmath>

using namespace std;

double f(double x) {
    return -20 * pow(M_E, -(pow(x, 2) / 8)) - pow(M_E, (0.5 * cos(2 * M_PI * x))) + 20 + M_E;
}

double centralDifferences(double x) {
    double h = 0.0001;
    return (f(x + h) - f(x - h)) / (2 * h);
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
    cout << gradientDescent(1) << endl;
    return 0;
}
