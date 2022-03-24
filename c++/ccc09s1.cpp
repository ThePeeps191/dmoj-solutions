#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b;
	cin >> a;
	cin >> b;
	int c = 0;
	double intpart;
	for(int n = a;n<=b;n++) {
		double result1 = sqrt(n);
		double result2 = cbrt(n);
		if(modf(result1, &intpart) == 0.0 and modf(result2, &intpart) == 0.0) {
			c++;
		}
	}
	cout << c << endl;
}