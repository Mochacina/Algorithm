#include <bits/stdc++.h>

using namespace std;

int main(){
    set<pair<int,int>> m;
    while (1) {
        int n;
        cin >> n;
        if (!n) break;

        if (n==1){
            int k,p;
            cin >> k >> p;
            m.insert({p,k});
        }
        else if (n==2)
        {
            if (!m.empty()) {
                auto it = m.begin();
                printf("%d\n", it->second);
                m.erase(it);
            }
        }
        else if (n==3)
        {
            if (!m.empty()) {
                auto it = m.rbegin();
                printf("%d\n", it->second);
                m.erase(--m.end());
            }
        }
        
    }

    return 0;
}