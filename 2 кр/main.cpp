#include <iostream>
#include <locale.h>
#include <stdbool.h>
#include <Windows.h>
#include <string> 
#include <vector>
#include <time.h>
#include <fstream>
#define userChoice '1'
#define randomChoice '2'

using namespace std;

int checkData() {
	int forCheck;
	cin >> forCheck;
	while (cin.fail()) {
		while (getchar() != '\n');
		cout << "�������� �����������. ������� ����� ������������� ��������: ";
		cin.clear();
		cin >> forCheck;
	}
	forCheck *= 10000;
	forCheck = (double)(int)forCheck;
	forCheck /= 10000;
	
	return forCheck;
}

double verification() {
	double checking;
	cin >> checking;
	while (cin.fail()) {
		while (getchar() != '\n');
		cout << "�������� �����������. ������� ����� �������� ��� ������(��� ������������ ����� ���������� �����): ";
		cin.clear();
		cin >> checking;
	}

	checking *= 10000;
	checking = (double)(int)checking;
	checking /= 10000;
	return checking;
}
void selectionSort(double* l, double* r) {
	for (double* i = l; i < r; i++) {
		double minz = *i, *ind = i;
		for (double* j = i + 1; j < r; j++) {
			if (*j < minz) minz = *j, ind = j;
		}
		swap(*i, *ind);
	}
}

void print(double massiv[], int num) {

	for (int j = 0; j < num; j++) {
		cout << massiv[j] << " ";
	}
}


int main(){
	srand(time(NULL));
	setlocale(LC_ALL, "RU");
	char choice;
	int size;
	double  *getArray;
	cout << "�����������\n������ ��������� ��������� 435 ������:\n�������� ����\n������ �����";
	
	while (true){
		cout << "\n1 - ������ ���� ������������������\n2 - �������� ������������ ������������������\n����� ������ ������� - �����" << endl;
		cin >> choice;
		while (getchar() != '\n');
		
		if (choice == userChoice) {
			cout << "������� ������ �������(������ ������������� �����): ";
			size = checkData();
			cout << "������ �������: " << size << endl;
			while (getchar() != '\n');
			getArray = new double[size];
			for (int h = 0; h < size; h++) {
				cout << "\n������� �������� ��� ������ " << h + 1 << " (��� ������������ ����� ���������� �����) : ";
				getArray[h] = verification();
				while (getchar() != '\n');
				cout << "h =  " << getArray[h];
			}
			cout << "\n�������� ������: " << endl;
			print(getArray, size);

			
			cout << "\n��������������� ������: " << endl;

			for (int g = 0; g < size; g++) {
				selectionSort(&getArray[g], &getArray[size - g]);
			}
			print(getArray, size);
			
			delete[] getArray;

		}

		else if (choice == randomChoice) {
			cout << "������� ������ �������(������ ������������� �����): ";
			size = checkData();
			cout << "������ �������: " << size << endl;
			while (getchar() != '\n');
			getArray = new double[size];
			for (int h = 0; h < size; h++) {
				getArray[h] = -100 + (double)rand() / RAND_MAX * (897.8 + 100);
			}
			cout << "\n�������� ������: " << endl;
			print(getArray, size);

			cout << "\n��������������� ������: " << endl;

			for (int g = 0; g < size; g++) {
				selectionSort(&getArray[g], &getArray[size - g]);
			}
			print(getArray, size);

			delete[] getArray;
		}

		else {
			break;
		}
	}
	
}