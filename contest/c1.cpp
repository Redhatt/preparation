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
typedef long long int ll;
#define rep(i,a,b) for (ll i=a; i<b; i++)
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef pair<ll, ll> pll;
typedef vector<pll> vp;
long long int inf = 100000000000000000;
ll mod = 1000000007;
void printvi(vi v){for (auto x: v)  cout<<x<<" ";newline}
void printvb(vb v){for (auto x: v)  cout<<x<<" ";newline}
void printvvi(vvi v){for (auto x: v){for (auto y:x)  cout<<y<<" ";newline}}
void printvs(vs v){for (auto x: v)  cout<<x<<" ";newline}
void printvp(vp v){for (auto &x: v) {cout<<x.F<<" "<<x.S;newline}}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
	// Code here ------------------------
	
	int arr[] = {3,2,1};
	sort(arr, arr+3);
	cout<<arr[0]<<" "<<arr[1]<<" "<<arr[2]<<endl;
	cout<<pow(2, 10);


	cout<<"working";

	// ----------------------------------
	return 0;
}