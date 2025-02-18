class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0)return false;
        int a[20];
        int i = 0;
        while(x != 0){
            a[i++] = x % 10;
            x /= 10;
        }
        --i;
        int j = 0;
        while(i != j && i != j - 1){
            if(a[i] != a[j])return false;
            --i;++j;
        }
        return true;
    }
};