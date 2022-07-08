#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> graph;
vector<int> in, out, flat, bit, value;
int N, n, q;


void dfs(int node, int parent, int& timer)
{
    timer++;
    in[node] = timer;
    flat[timer] = node;

    for (int nbr: graph[node]) {
        if (nbr == parent) continue;
        dfs(nbr, node, timer);
    }
    timer++;
    out[node] = timer;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    clock_t start, end;
    start = clock();
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif


    // Code here ------------------------
    int i, a, b;
    cin>>n>>q;

    N = n + 1;
    graph.resize(N);
    in.assign(N, 0);
    out.assign(N, 0);
    value.assign(N, 0);
    flat.assign(3*N, 0);
    bit.assign(3*N + 1, 0);

    for (i=0; i<n; i++)
        cin>>value[i];

    for (i=0; i<n-1; i++) {
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int timer = 0;
    dfs(1, -1, timer);

    for (int x: flat)
        cout<<x<<" ";

    // ----------------------------------

    end = clock();
    double time_taken = double(end - start) / double(CLOCKS_PER_SEC/1000); 
    cout << "\n||Time = " << fixed << time_taken << setprecision(5); 
    cout << "ms||" << endl; 
    return 0;
}