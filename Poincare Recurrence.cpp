#include <iostream>
#include <set>
#include <iterator>
#include <algorithm>
#include <random>

using namespace std;

int main() {
	random_device rd;
	mt19937_64 mt(rd());

	set<int>urn1, urn2 = {};
	int n;

	cout << "How many numbers to start with: ";
	cin >> n;

	for (int i = 0; i < n; i++)
		urn1.insert(i);

	cout << "\nurn1 contains...\n";
	for (set<int>::iterator it = urn1.begin(); it != urn1.end(); it++)
		cout << *it << " ";

	uniform_int_distribution<int> dist(1, n);
	int num_in_urn2 = dist(mt);
	cout << "\nNumber of items to put in urn2 = " << num_in_urn2;
	
	int steps = 0;

	if (num_in_urn2 == 0) {
		cout << "\nurn1 contains...\n";
		for (set<int>::iterator it = urn1.begin(); it != urn1.end(); it++)
			cout << *it << " ";
		cout << "\nurn2 contains...\n";
		for (set<int>::iterator it = urn2.begin(); it != urn2.end(); it++)
			cout << *it << " ";
	}
	else {
		while (urn2.size() != num_in_urn2) {
			int x = rand() % n;
			urn1.erase(x);
			urn2.insert(x);
		}
	}

	cout << "\nurn1 contains...\n";
	for (set<int>::iterator it = urn1.begin(); it != urn1.end(); it++)
		cout << *it << " ";
	cout << "\nurn2 contains...\n";
	for (set<int>::iterator it = urn2.begin(); it != urn2.end(); it++)
		cout << *it << " ";

	while (urn2.size() != 0) {
		int x = dist(mt);
		if (urn1.find(x) != urn1.end()) {
			//x is in urn1
			urn1.erase(x);
			urn2.insert(x);
			steps++;
		}
		else if (urn2.find(x) != urn2.end()) {
			//x is in urn 2
			urn2.erase(x);
			urn1.insert(x);
			steps++;
		}
	}

	cout << "\nurn1 contains...\n";
	for (set<int>::iterator it = urn1.begin(); it != urn1.end(); it++)
		cout << *it << " ";
	cout << "\nurn2 contains...\n";
	for (set<int>::iterator it = urn2.begin(); it != urn2.end(); it++)
		cout << *it << " ";
	cout << "\n\nSteps taken = " << steps;
	return 0;
}