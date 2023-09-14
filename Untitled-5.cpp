#include <bits/stdc++.h>
using namespace std;
class Geeks {

public:
    string geekname;
	void printname() { cout << "Geekname is:" << geekname; }
};
int main()
{
	Geeks obj1;
    obj1.geekname = "Abhi";
	obj1.printname();
	return 0;
}
