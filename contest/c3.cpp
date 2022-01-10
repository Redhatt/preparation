#include <bits/stdc++.h>
#define len(a) a.size()
#define pb push_back
#define mkp make_pair
#define F first
#define S second
#define all(a) a.begin(), a.end()
using namespace std;
#define newline cout<<"\n";
#define fine cout<<"FINE"; newline
#define debug(x) cout<<"x: "<<x;newline
#define rep(i,a,b) for (long long int i=a; i<b; i++)
typedef long long int ll;
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

int main() {
	// #ifndef ONLINE_JUDGE
	// freopen("input.txt", "r", stdin);
	// freopen("output.txt", "w", stdout);
	// #endif
	ll n, m, q;
	cin>>n>>m>>q;
	vector<vector<ll>> graph(n, vector<ll>(n, inf));
	ll a,b,c;
	rep(i, 0, m){
		cin>>a>>b>>c;
		graph[a-1][b-1] = min(graph[a-1][b-1], c);
		graph[b-1][a-1] = min(graph[b-1][a-1], c);
	}
	rep(k, 0, n){
		rep(i, 0, n){
			rep(j, 0, n) 
			if (graph[i][k] < inf and graph[k][j] < inf) graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j]);
		}
	}
	rep(i, 0, q){
		cin>>a>>b;
		c = (graph[a-1][b-1] == inf) ? -1 : graph[a-1][b-1];
		cout<<c;
		newline
	}
    return 0;
}	