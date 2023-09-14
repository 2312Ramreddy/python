
#include<iostream>
#include<string>
using namespace std;
class myclass{
    public:
    int mynum;
    string mystring;
};
int main(){
    myclass myobj;
    myobj.mynum=15;
    myobj.mystring="some text";
    cout<<myobj.mynum<<"\n";
    cout<<myobj.mystring;
    return 0;
}