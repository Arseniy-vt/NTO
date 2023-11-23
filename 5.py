#include <iostream>
#include <vector>

using namespace std;

vector <vector <int> > g;
vector <int> col;
bool fl=0;

bool dfs(int s)
{
col[s]=1;
for(int i=0;i<g[s].size();i++)
{
if(col[g[s][i]]==0)
{
if(dfs(g[s][i]))
{
return true;
}
}
if(col[g[s][i]]==1)
{
return true;
}
}
col[s]=2;
return false;
}

signed main()
{
int t; cin>>t;
for(int z=0;z<t;z++)
{
int n; cin>>n;
g.resize(n); 
col.resize(n, 0);
for(int i=0;i<n;i++)
{
int k; cin>>k;
for(int j=0;j<k;j++)
{
int a; cin>>a; a--;
g[i].push_back(a);
}
}
bool fl=0;
for(int i=0;i<col.size();i++)
{
if(col[i]==0)
{
if(dfs(i))
{
fl=1;
break; 
} 
}
}
if(fl) cout<<"No"<<endl;
else cout<<"Yes"<<endl;
g.clear(); 
col.clear();
}
return 0;
}
