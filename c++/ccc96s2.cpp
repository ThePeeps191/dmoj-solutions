#include <bits/stdc++.h>

using namespace std;

int main() {
	int N;
	cin >> N;
	for (int n = 0; n < N; n++) {
		int i;
		cin >> i;
		int orig = i;
		cout << i << endl;
		while (to_string(i).length() > 2) {
			int d = to_string(i).back();
			i = stoi(to_string(i).substr(0, to_string(i).size()-1));
			i -= d;
			cout << i << endl;
		}
		if (i % 11 == 0) {
			cout << "The number " << orig << " is divisible by 11." << endl;
		} else {
			cout << "The number " << orig << " is not divisible by 11." << endl;
		}

		if (n != N - 1) {
			cout << endl;
		}
	}
}