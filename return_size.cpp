#include <iostream>
using namespace std;
int main() {
    int x = 2;
    double y = 3.5;
    char z = 'g';
    int a = sizeof(x);
    int b = sizeof(y);
    int c = sizeof(z);
    cout << a << " " << b << " " << c << endl;
    return 0;
}