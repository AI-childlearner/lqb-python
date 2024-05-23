#include<bits/stdc++.h>
using namespace std;
inline void rd(int &x){
    int s=0,f=1; char c=getchar();
    while(c<'0'||c>'9'){if(c=='-')f=0; c=getchar();}
    while(c>='0'&&c<='9'){s=s*10+c-48; c=getchar();}
    x=f? s:-s;
}
const int N=1e5+10, M=N<<1; int LOGM;
struct edge{int to,nt;} e[M]; int hd[N],ect;
inline void ade(int u,int v){e[++ect]={v,hd[u]}; hd[u]=ect;}

int n,m,rot,in[N],fa[N][22],dep[N];
void pre(int u,int f){
    fa[u][0]=f; dep[u]=dep[f]+1;
    for(int i=1;i<=LOGM;i++) fa[u][i]=fa[fa[u][i-1]][i-1];
    for(int i=hd[u];i;i=e[i].nt) pre(e[i].to,u);
}
bool fg[N];
inline int calc(int x){
    for(int i=LOGM;~i;i--){
        if(fa[x][i] && fg[fa[x][i]]==0) x=fa[x][i];
    }
    return x;
}

signed main(){
    rd(n); rd(m); LOGM=log2(n);
    for(int i=1,u,v;i<n;i++){
        rd(u); rd(v); in[v]++; ade(u,v);
    }
    for(int i=1;i<=n;i++) if(!in[i]){rot=i; break;}
    pre(rot,0); fg[rot]=1;
    for(int i=1;i<=m;i++){
        char c=getchar(); int x;
        while(c!='P'&&c!='Q') c=getchar();
        rd(x);
        if(c=='P'){
            if(fg[x]){
                for(int j=hd[x];j;j=e[j].nt) fg[e[j].to]=1;
                puts("0");
                continue;
            }
            int top=calc(x); top=fa[top][0];
            printf("%d\n",dep[x]-dep[top]);
            for(;;x=fa[x][0]){
                fg[x]=1;
                for(int j=hd[x];j;j=e[j].nt) fg[e[j].to]=1;
                if(x==top) break;
            }
        }
        else{
            if(fg[x]){
                puts("0"); continue;
            }
            int top=calc(x); top=fa[top][0];
            printf("%d\n",dep[x]-dep[top]);
        }
    }
    return 0;
}