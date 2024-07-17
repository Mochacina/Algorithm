#include <bits/stdc++.h>

using namespace std;

int main(){
    map<int, int> m;
    while (1) {
        int n;
        cin >> n;
        if (!n) break;

        if (n==1){
            int k,p;
            cin >> k >> p;
            m.insert({k,p});
        }
        else if (n==2)
        {
            if (!m.empty()) {
                auto it = m.begin();
                m.erase(it);
            }
        }
        else if (n==3)
        {
            if (!m.empty()) {
                auto it = m.rbegin();
                m.erase(next(it).base());
            }
        }
        
    }

    return 0;
}