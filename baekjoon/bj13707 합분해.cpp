// DP 사용 이항계수 X

#include <bits/stdc++.h>

using namespace std;

int main () {
    int n=0,k=0;
    cin>>n>>k;
    int dp[k][n+1];
    for (int i=0; i<k; i++){
        dp[i][0] = 1;
    }
    for (int j=0; j<=n; j++){
        dp[0][j] = 1;
    }
    
    for (int i=1; i<k; i++){
        for (int j=1; j<=n; j++){
            dp[i][j] = dp[i][j-1] + dp[i-1][j];
            dp[i][j] %= 1000000000;
        }
    }
    cout << dp[k-1][n];
    return 0;
}