#include <iostream>
#include <cmath>

using namespace std;

int roots(double a, double b, double c, double& x1, double& x2) {
    double discriminant = b * b - 4 * a * c;

    if (discriminant < 0) {
        return -1;
    }

    x1 = (-b + sqrt(discriminant)) / (2 * a);
    x2 = (-b - sqrt(discriminant)) / (2 * a);

    if (discriminant == 0) {
        return 0;
    }

    return 1;
}

int main() {
    double a, b, c, x1, x2;

    cout << "Enter coefficients a, b, c: ";
    cin >> a >> b >> c;

    int result = roots(a, b, c, x1, x2);

    if (result == -1) {
        cout << "No real roots" << endl;
    }
    else if (result == 0) {
        cout << "Single root x1 = x2 = " << x1 << endl;
    }
    else {
        cout << "Roots: x1 = " << x1 << ", x2 = " << x2 << endl;
    }

    return 0;
}