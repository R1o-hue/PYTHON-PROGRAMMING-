#include <iostream>
#include <string>

std::string gradeScore(int score) {
    if (score >= 90) {
        return "A";
    } else if (score >= 80) {
        return "B";
    } else if (score >= 70) {
        return "C";
    } else if (score >= 60) {
        return "D";
    } else {
        return "F";
    }
}

int main() {
    int score = 59;
    std::cout << "Your grade is: " << gradeScore(score) << std::endl;
    return 0;
}