#include <bits/stdc++.h>

using namespace  std;
int K, N;
vector<vector<int>>graph, up;
vector<int> in, out, value, ans;


bool isAnscetor(int u, int v)
{
    if ((u == -1) or (v == -1))
        return true;

    return (in[u]<=in[v]) and (out[u]>=out[v]);
}

int LCA(int u, int v)
{
    if (isAnscetor(u, v))
        return u;

    if (isAnscetor(v, u))
        return v;

    for (int k=K-1; k>=0; k--) {
        if (!isAnscetor(up[u][k], v))
            u = up[u][k];
    }

    return up[u][0];
}

void dfs(int node, int parent, int& time)
{
    in[node] = ++time;
    up[node][0] = parent;

    for (int k=1; k<K; k++) {
        if (up[node][k-1] == -1) break;
        up[node][k] = up[up[node][k-1]][k-1];
    }

    for (int nbr: graph[node]) {
        if (nbr == parent) continue;
        dfs(nbr, node, time);
    }

    out[node] = ++time;
}

void ansDfs(int node, int parent, vector<int>& ans)
{
    ans[node] = value[node];

    for (int nbr: graph[node]) {
        if (nbr == parent) continue;
        ansDfs(nbr, node, ans);
        ans[node] += ans[nbr];
    }
}

int main()
{
    int n, q, a, b, lca, p;
    cin>>n>>q;
    N = n + 1;
    K = 1 + (int) ceil(log2(N));
    up.assign(N, vector<int>(K, -1));
    graph.resize(N);
    in.resize(N, 0);
    out.resize(N, 0);
    value.resize(N, 0);
    ans.resize(N, 0);

    for (int i=0; i<n-1; i++) {
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int time = 0;
    dfs(1, -1, time);

    // concept of difference array.
    for (int i=0; i<q; i++) {
        cin>>a>>b;
        lca = LCA(a, b);
        p = up[lca][0];
        value[a]++;
        value[b]++;
        value[lca]--;
        if (p != -1)
            value[p]--;
    }

    ansDfs(1, -1, ans);

    for (int i=1; i<ans.size(); i++)
        cout<<ans[i]<<" ";

    return 0;
}