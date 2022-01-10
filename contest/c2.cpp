#include <bits/stdc++.h>
#include <algorithm>
#define len(a) a.size()
#define pb push_back
#define mkp make_pair
#define F first
#define S second
#define all(a) a.begin(), a.end()
using namespace std;
typedef long long int ll;
#define newline cout<<"\n";
#define fine cout<<"FINE"; newline
#define debug(x) cout<<"x: "<<x;newline
#define rep(i,a,b) for (ll i=a; i<b; i++)
typedef vector<vector<ll>> vvi;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<ll> vi;
typedef vector<pair<ll, ll>> vp;
typedef pair<ll, ll> pll;
ll inf = 100000000000000000;
ll mod = 1000000007;
void printvi(vi v){for (auto x: v)  cout<<x<<" ";newline}
void printvb(vb v){for (auto x: v)  cout<<x<<" ";newline}
void printvvi(vvi v){for (auto x: v){for (auto y:x)  cout<<y<<" ";newline}}
void printvs(vs v){for (auto x: v)  cout<<x<<" ";newline}
void printvp(vp v){for (auto &x: v) {cout<<x.F<<" "<<x.S;newline}}
ll D;
bool sortcol(const vi &v1, const vi &v2){ return (v1[1]/D<v2[1]/D) or (v1[1]/D == v2[1]/D and v1[2]<v2[2]);}

//==========================================================================
int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
	//------------------------------------------------------

            int x = 4, z = 3;
            int y = !((x<<3)+(~z)-(++x));
            printf(" %d\n", y);

    return 0;
}
