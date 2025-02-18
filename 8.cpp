#include <iostream>
#include <string>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <climits>
using namespace std;
class Solution {
public:
    int myAtoi(string s) {
        long long res = 0;
        int len = s.length();
        int i = 0;
        while(s[i] == ' '){
            ++i;
        }
        int flag = 1;
        if(s[i] == '-'){
            flag = -1;
            ++i;
        }
        else if(s[i] == '+')++i;
        while(s[i] == '0')++i;
        for(; i < len; ++ i){
            if(!isdigit(s[i]))break;
            if(flag == 1)res = res * 10 + (s[i] - '0');
            else res = res * 10 -(s[i] - '0');
            if(res >= pow(2, 31) - 1)return INT_MAX;
            else if(res <= -pow(2, 31))return INT_MIN;
        }
        return res;
    }
};
int main() {
    Solution sol;
    string str = "  +b12102370352";
    cout << sol.myAtoi(str) << endl; 
    return 0;
}