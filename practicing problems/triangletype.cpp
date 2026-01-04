#include <iostream>
using namespace std;

int main() {
    // update your code here
    int a,b,c;
    cin>>a>>b>>c;
    if (a==b and b==c) cout<<"Equilateral";
    else if (a!=b and b!=c and c!=a) cout<<"Scalene";
    else cout<<"Isosceles";

    return 0;
}