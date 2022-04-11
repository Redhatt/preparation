#include <bits/stdc++.h>

using namespace  std;
int K, N;
vector<vector<int>> graph, up;
vector<int> in, out, level;


bool isAncestor(int u, int v)
{
    if ((u == -1) or (v == -1)) return true;
    return (in[u]<=in[v]) and (out[u]>=out[v]);
}

int LCA(int u, int v)
{
    if (isAncestor(u, v))
        return u;

    if (isAncestor(v, u))
        return v;

    for (int k=K-1; k>=0; k--)
    {
        if (!isAncestor(up[u][k], v))
            u = up[u][k];
    }

    return up[u][0];
}

int getDis(int u, int v)
{
    int ancestor = LCA(u, v);
    return abs(level[ancestor] - level[u]) + abs(level[ancestor] - level[v]);
}

void dfs(int node, int parent, int &time, int depth)
{
    in[node] = ++time;
    up[node][0] = parent;
    level[node] = depth;

    for (int k=1; k<K;k++)
    {
        if (up[node][k-1] == -1) break;
        up[node][k] = up[up[node][k-1]][k-1];
    }

    for (int nbr: graph[node])
    {
        if (nbr == parent) continue;
        dfs(nbr, node, time, depth+1);
    }
    out[node] = ++time;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    clock_t start, end;
    start = clock();
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int n, q, a, b, u, v, i;
    cin>>n>>q;

    N = n + 1;
    K = 1 + (int) ceil(log2(N));
    up.assign(N, vector<int>(K, -1));
    graph.resize(N);
    in.resize(N, 0);
    out.resize(N, 0);
    level.resize(N, 0);

    for (i=0; i<n-1; i++)
    {
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int time = 0;
    dfs(1, -1, time, 0);

    for (i=0; i<q; i++)
    {
        cin>>u>>v;
        cout<<getDis(u, v)<<endl;
    }    

    // end = clock();
    // double time_taken = double(end - start) / double(CLOCKS_PER_SEC/1000); 
    // cout << "\n||Time = " << fixed<< time_taken << setprecision(5); 
    // cout << "ms||" << endl; 
    return 0;
}