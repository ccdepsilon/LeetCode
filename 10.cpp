#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;
        dp[0][1] = false;
        for(int i = 2; i < n + 1; ++ i){
            if(p[i - 1] == '*')dp[0][i] = dp[0][i - 2];
        }
        for(int i = 1; i < m + 1; ++ i){
            for(int j = 1; j < n + 1; ++ j){
                if(p[j - 1] == s[i - 1] || p[j - 1] == '.'){
                    dp[i][j] = dp[i - 1][j - 1];
                }
                else if(p[j - 1] == '*'){
                    if(p[j - 2] == s[i - 1] || p[j - 2] == '.'){
                        dp[i][j] = dp[i][j - 2] || dp[i][j - 1] || dp[i - 1][j];
                    }
                    else{
                        dp[i][j] = dp[i][j - 2];
                    }
                }
            }
        }
        return dp[m][n];
    }
};
int main()
{ 
    Solution s;
    cout << s.isMatch("aaa", "ab*ac*a") << endl;
    return 0;
}