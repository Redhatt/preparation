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

struct Node{ll data;Node * next = NULL;};
Node * newNode(ll data){struct Node *node = new Node;node->data = data;return node;}
void copy_llist(Node* head, vi &list){Node *temp = head;while (temp){list.pb(temp->data);temp = temp->next;}}
void printll(Node *head){while (head){cout<<head->data<<" ";head = head->next;}newline}
vi primeUpto(ll n){
	ll f, j;
	vi primes;
	rep(i, 2, n+1){
		f = 1; j = 2;
		while (j*j <= i){
			if (i%j == 0){
				f = 0;
				break;
			}
			j++;
		}
		if (f)
			primes.pb(i);
	}
	return primes;
}

vi primeFactors(ll n, vi primes){
	vi factors;
	ll i = 0; ll size = len(primes);
	ll d;
	while (i<size){
		d = primes[i];
		while (n%d == 0){
			n = n/d;
			factors.pb(d);
		}
		i+=1;
	}
	if (n != 1)
		factors.pb(n);
	return factors;
}

ll cal(ll a, ll b){
	if (a == 1) return 1;
	if (b <= 0) return 1;
	ll ans = 1;
	ll c = 0;
	while (ans<=mod and c<b){
		ans = ans*a;
		c++;
	}
	ans = ans%mod;
	if (c == b) return ans;
	ll r = b%c;
	ll q = b/c;
	return ((cal(a,r)%mod)*(cal(ans, q)%mod))%mod;
}

int main() {
	clock_t start, end;
	start = clock();
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
	//----------------------------------------------
	multiset <ll> car;
	car.insert(12);
	car.insert(12);
	car.insert(12);
	for (auto x: car) cout<<x<<" ";
	//----------------------------------------------
	end = clock();
	double time_taken = double(end - start) / double(CLOCKS_PER_SEC/1000); 
    cout << "||Time = " << fixed<< time_taken << setprecision(5); 
    cout << "ms||" << endl; 
    return 0; 
}