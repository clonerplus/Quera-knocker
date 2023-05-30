// C program to illustrate the use of
// header file in C
#include <iostream>
#include <vector>
#include <string>

using namespace std;



class TextualMachine {
public:
    string input;
    vector<string> toBePrinted;

    explicit TextualMachine(const string& input){
        this->input = input;
    }

    void SHIFT_R(int N) {
        if (this->input == "") return;
        if (N > input.length()) N %= input.length();
        this->input = input.substr(input.length() - N) + input.substr(0, input.length() - N);
    }

    void SHIFT_L(int N) {
        if (this->input == "") return;
        if (N > input.length()) N %= input.length();
        this->input = input.substr(N, input.length()) + input.substr(0, N);
    }

    void EXTEND(const int N) {
        for (int i = 0; i < N; i++) {
            this->input += '*';
        }
    }

    void SHRINK(const int N) {
        if (N >= this->input.length()) {
            this->input = "";
            return;
        }
        this->input = input.substr(0, input.length() - N);
    }

    void REVERSE() {
        string reversed;
        for (int i = this->input.length() - 1; i >= 0; i--) {
            reversed += this->input[i];
        }
        this->input = reversed;
    }

    void PUT_I_C(const int N, const char C) {
        this->input[N-1] = C;
    }

    void PRINT() {
        toBePrinted.push_back(this->input);
    }

};

int main() {
    string input, control;
    getline(cin, input);

    TextualMachine machine(input);


    while (true){

        getline(cin, control);

        if (control.find("SHIFT-R") != string::npos) {
            int N = stoi(control.substr(8));
            machine.SHIFT_R(N);

        } else if (control.find("SHIFT-L") != string::npos) {
            int N = stoi(control.substr(8));
            machine.SHIFT_L(N);

        } else if (control.find("EXTEND") != string::npos) {
            int N = stoi(control.substr(7));
            machine.EXTEND(N);

        } else if (control.find("SHRINK") != string::npos) {
            int N = stoi(control.substr(7));
            machine.SHRINK(N);

        } else if (control == "REVERSE") {
            machine.REVERSE();

        } else if (control.find("PUT") != string::npos) {
            int N = stoi(control.substr(3, control.length() - 2));
            machine.PUT_I_C(N, control[control.length()-1]);

        } else if (control == "PRINT") {
            machine.PRINT();

        } else break;
    }


    for (const auto& i: machine.toBePrinted) {
        cout << i << endl;
    }
}

