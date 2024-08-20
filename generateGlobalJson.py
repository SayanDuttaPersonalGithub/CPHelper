TEMPLATE = '''
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>  
#pragma GCC optimize("O3,unroll-loops")
using namespace std;
using namespace chrono;
 
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> p64;
typedef pair<double,double> pdd;
typedef vector<ll> v64;
typedef vector<vector<ll> > vv64;
typedef vector<vector<p64> > vvp64;
typedef vector<p64> vp64;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i,e) for(ll i = 0; i < e; i++)
#define ln "\n"
#define pb push_back
#define ppb pop_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())
#define print(x) cout<<x<<ln
 
#ifndef ONLINE_JUDGE
#define dbg(x) cerr << #x <<" "; _print(x); cerr << endl;
#else
#define dbg(x)
#endif
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
void _print(ll t) {cerr << t;}
void _print(int t) {cerr << t;}
void _print(string t) {cerr << t;}
void _print(char t) {cerr << t;}
void _print(lld t) {cerr << t;}
void _print(double t) {cerr << t;}
void _print(ull t) {cerr << t;}
 
template <class T, class V> void _print(pair <T, V> p);
template <class T> void _print(vector <T> v);
template <class T> void _print(set <T> v);
template <class T, class V> void _print(map <T, V> v);
template <class T> void _print(multiset <T> v);
 template <class T, class V> void _print(pair <T, V> p) {cerr << "{"; _print(p.fi); cerr << ","; _print(p.se); cerr << "}"<<ln;}
template <class T> void _print(vector <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
 template <class T> void _print(set <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(multiset <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T, class V> void _print(map <T, V> v) {cerr << "[ "; for (auto i : v) {_print(i); cerr << " ";} cerr << "]";}
 
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void solve(){
}
int main()
{
#ifndef ONLINE_JUDGE
freopen("Error.txt", "w", stderr); 
#endif 
	fast_cin();
	ll t=1;
	cin >> t;
	for(int it=1;it<=t;it++) {
		solve();
	}
	return 0;
}'''

import json

D = {}
D['template'] = TEMPLATE
D['inputTxtPath'] = "C:\Users\SAYAN\AppData\Roaming\Sublime Text\Packages\User\input.txt"
D['dashCount'] = 50
D['baseContestPath'] = "C:\Users\SAYAN\AppData\Roaming\Sublime Text\Packages\User"
D['author'] = 'Sayan'
D['teamName'] = 'BlundersPride'

with open('globals.json' , 'wb') as glob:
	glob.write(json.dumps(D).encode())
