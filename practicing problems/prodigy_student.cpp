#include <iostream>
using namespace std;
int main() {
    string s1,s2;
    cin>> s1>> s2;
    double p1,p2;
    cin>> p1>> p2;
    if(p1>p2)
    cout<<s1;
    else if(p2>p1)
    cout<<s2;
    else
    cout<<"equal";
    return 0;
}