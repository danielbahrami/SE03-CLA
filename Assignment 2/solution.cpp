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

double gradientDescent(double x, double e = 0.000001, double iterMax = 10000, double a = 0.000001) {
    double count = 0;
    while (centralDifferences(x) > e && count < iterMax) {
        x = x - a * centralDifferences(x);
        count++;
    }
    return x;
}

int main() {
    cout << gradientDescent(1) << endl;
    return 0;
}
