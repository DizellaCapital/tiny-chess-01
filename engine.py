import json,os,urllib.request
V=[0,100,320,330,500,900,0]
KN=[-33,-31,-18,-14,14,18,31,33]
KG=[-17,-16,-15,-1,1,15,16,17]
DG=[-17,-15,15,17,-16,-1,1,16]
DQ=[-17,-15,15,17]
DO=[-16,-1,1,16]
C2=[0,1,2,3,3,2,1,0]
AD=[0,0,5,10,18,30,50,0]
KF=[10,14,4,0,0,4,14,10]
def _pv(t,r,f,g):
 c=C2[f]+C2[r]
 if t==1: return AD[r]+2*C2[f]
 if t==2: return 8*c-(25 if not g else 15)
 if t==3: return 5*c-(10 if not g else 5)
 if t==4: return 2*c+((12 if not g else 10) if r==6 else 0)
 if t==5: return (2 if not g else 3)*c-5
 return (KF[f] if r==0 else -12*r) if not g else 8*c-20
PM=[[0]*128 for _ in range(7)]
PE=[[0]*128 for _ in range(7)]
for _t in range(1,7):
 for _q in range(128):
  if _q&136: continue
  PM[_t][_q]=_pv(_t,_q>>4,_q&7,0)
  PE[_t][_q]=_pv(_t,_q>>4,_q&7,1)
CM=[[V[t]+PM[t][q] for q in range(128)] for t in range(7)]
CE=[[V[t]+PE[t][q] for q in range(128)] for t in range(7)]
_z=88172645463325252;M=(1<<64)-1
def _rn():
 global _z
 _z=(_z*6364136223846793005+1442695040888963407)&M
 return _z
ZP=[[_rn() for _ in range(128)] for _ in range(12)]
ZS=_rn();ZC=[_rn() for _ in range(16)];ZE=[_rn() for _ in range(8)]
def zi(p): return (abs(p)-1)*2+(p<0)
B=[0]*128;SD=1;CR=0;EP=-1;HM=0;KEY=0;KP=[4,116]
WL=[];BL=[];IX=[-1]*128;NPC=[7,7]
ST=[];HS=set();PR={}
TT={};KL=[[0,0] for _ in range(128)];HI=[[0]*128 for _ in range(7)]
NN=0;NB=100000
INF=1000000;MT=100000
class SE(Exception): pass
def atk(s,by):
 for o in (s-15*by,s-17*by):
  if not(o&136) and B[o]==by: return 1
 for d in KN:
  o=s+d
  if not(o&136) and B[o]==2*by: return 1
 for d in KG:
  o=s+d
  if not(o&136) and B[o]==6*by: return 1
 for d in DQ:
  o=s+d
  while not(o&136):
   p=B[o]
   if p:
    if p==3*by or p==5*by: return 1
    break
   o+=d
 for d in DO:
  o=s+d
  while not(o&136):
   p=B[o]
   if p:
    if p==4*by or p==5*by: return 1
    break
   o+=d
 return 0
def gen(cp):
 ms=[];us=SD;L=WL if us>0 else BL
 for s in L:
  p=B[s];t=p*us
  if t==1:
   d=16*us;o=s+d
   if not(o&136) and not B[o] and not cp:
    lr=7 if us>0 else 0
    if (o>>4)==lr:
     for pr in (5,4,3,2): ms.append(s|(o<<7)|(pr<<14))
    else:
     ms.append(s|(o<<7))
     if (s>>4)==(1 if us>0 else 6) and not B[s+2*d]: ms.append(s|((o+d)<<7)|(1<<17))
   for df in (-1,1):
    o=s+d+df
    if o&136: continue
    q=B[o]
    if q and (q>0)!=(us>0):
     if (o>>4)==(7 if us>0 else 0):
      for pr in (5,4,3,2): ms.append(s|(o<<7)|(pr<<14))
     else: ms.append(s|(o<<7))
    elif o==EP: ms.append(s|(o<<7)|(2<<17))
  elif t==2 or t==6:
   for d in (KN if t==2 else KG):
    o=s+d
    if o&136: continue
    q=B[o]
    if not q:
     if not cp: ms.append(s|(o<<7))
    elif (q>0)!=(us>0): ms.append(s|(o<<7))
   if t==6 and not cp:
    for sg in (1,-1):
     kt=s+2*sg;rf=s+3*sg if sg>0 else s-4;rt=s+sg
     rb=(1 if sg>0 else 2) if us>0 else (4 if sg>0 else 8)
     if CR&rb and B[rf]==4*us and not B[rt] and not B[kt] and (sg>0 or not B[s-3]) and not atk(s,-us) and not atk(rt,-us) and not atk(kt,-us): ms.append(s|(kt<<7)|((4 if sg>0 else 8)<<17))
  else:
   for d in (DQ if t==3 else DO if t==4 else DG):
    o=s+d
    while not(o&136):
     q=B[o]
     if not q:
      if not cp: ms.append(s|(o<<7))
     else:
      if (q>0)!=(us>0): ms.append(s|(o<<7))
      break
     o+=d
 return ms
def make(m):
 global SD,CR,EP,HM,KEY
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;fl=m>>17
 us=SD;pc=B[f];cp=B[t];cs=t
 if fl&2:
  cs=t-16*us;cp=B[cs];B[cs]=0
 L=WL if us>0 else BL;VL=BL if us>0 else WL
 vi=-1;sw=-1
 if cp:
  vi=IX[cs];last=VL.pop()
  if vi<len(VL): VL[vi]=last;IX[last]=vi;sw=last
  else: sw=-1
  IX[cs]=-1
  if abs(cp)>1: NPC[cp<0]-=1
 L[IX[f]]=t;IX[t]=IX[f];IX[f]=-1
 np=pr*us if pr else pc
 B[t]=np;B[f]=0
 rs=-1
 if fl&12:
  rs=t+1 if fl&4 else t-2;rt=t-1 if fl&4 else t+1
  L[IX[rs]]=rt;IX[rt]=IX[rs];IX[rs]=-1
  B[rt]=4*us;B[rs]=0
 if abs(pc)==6: KP[0 if us>0 else 1]=t
 ncr=CR
 if pc==6: ncr&=~3
 elif pc==-6: ncr&=~12
 if f==0 or t==0: ncr&=~2
 if f==7 or t==7: ncr&=~1
 if f==112 or t==112: ncr&=~8
 if f==119 or t==119: ncr&=~4
 nep=(f+t)//2 if fl&1 else -1
 k=KEY
 k^=ZP[zi(pc)][f]
 if cp: k^=ZP[zi(cp)][cs]
 k^=ZP[zi(np)][t]
 if rs>=0:
  k^=ZP[zi(4*us)][rs];k^=ZP[zi(4*us)][t-1 if fl&4 else t+1]
 k^=ZC[CR];k^=ZC[ncr]
 if EP>=0: k^=ZE[EP&7]
 if nep>=0: k^=ZE[nep&7]
 k^=ZS
 if pr: NPC[us<0]+=1
 ST.append((m,cp,cs,sw,vi,CR,EP,HM,KEY))
 CR=ncr;EP=nep
 HM=0 if abs(pc)==1 or cp else HM+1
 KEY=k;SD=-us
 rep=(k in PR) or (k in HS)
 PR[k]=PR.get(k,0)+1
 return rep
def unmake():
 global SD,CR,EP,HM,KEY
 m,cp,cs,sw,vi,cr0,ep0,hm0,k0=ST.pop()
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;fl=m>>17
 us=-SD;pc=us if pr else B[t]
 n=PR.get(KEY,0)
 if n<=1: PR.pop(KEY,None)
 else: PR[KEY]=n-1
 L=WL if us>0 else BL;VL=BL if us>0 else WL
 B[f]=pc;B[t]=0
 if cp: B[cs]=cp
 if fl&12:
  rs=t+1 if fl&4 else t-2;rt=t-1 if fl&4 else t+1
  L[IX[rt]]=rs;IX[rs]=IX[rt];IX[rt]=-1
  B[rs]=4*us;B[rt]=0
 L[IX[t]]=f;IX[f]=IX[t];IX[t]=-1
 if cp:
  if sw>=0:
   VL.append(sw);VL[vi]=cs;IX[cs]=vi;IX[sw]=len(VL)-1
  else:
   VL.append(cs);IX[cs]=len(VL)-1
  if abs(cp)>1: NPC[cp<0]+=1
 if pr: NPC[us<0]-=1
 if abs(pc)==6: KP[0 if us>0 else 1]=f
 CR,EP,HM,KEY=cr0,ep0,hm0,k0
 SD=us
def mknull():
 global SD,EP,KEY
 ST.append((0,0,-1,-1,-1,CR,EP,HM,KEY))
 k=KEY^ZS^(ZE[EP&7] if EP>=0 else 0)
 rep=(k in PR) or (k in HS)
 PR[k]=PR.get(k,0)+1
 KEY=k;EP=-1;SD=-SD
 return rep
def unnull():
 global SD,EP,KEY,CR,HM
 m,cp,cs,sw,vi,cr0,ep0,hm0,k0=ST.pop()
 n=PR.get(KEY,0)
 if n<=1: PR.pop(KEY,None)
 else: PR[KEY]=n-1
 CR,EP,HM,KEY=cr0,ep0,hm0,k0
 SD=-SD
def bad():
 us=-SD
 return atk(KP[0 if us>0 else 1],SD)
def setup(mv):
 global B,SD,CR,EP,HM,KEY
 B=[0]*128;WL.clear();BL.clear()
 bk=[4,2,3,5,6,3,2,4]
 for i,p in enumerate(bk):
  B[i]=p;B[i+112]=-p;B[i+16]=1;B[i+96]=-1
 for q in range(128):
  if q&136: continue
  p=B[q]
  if p>0: WL.append(q);IX[q]=len(WL)-1
  elif p<0: BL.append(q);IX[q]=len(BL)-1
 SD=1;CR=15;EP=-1;HM=0;KP[0]=4;KP[1]=116;NPC[0]=7;NPC[1]=7
 KEY=0
 for q in range(128):
  if q&136: continue
  p=B[q]
  if p: KEY^=ZP[zi(p)][q]
 KEY^=ZC[CR]
 HS.clear();PR.clear();ST.clear()
 for s in mv:
  HS.add(KEY)
  make(puc(s))
 HS.add(KEY);PR.clear();ST.clear()
def puc(s):
 f=(ord(s[1])-49)*16+ord(s[0])-97
 t=(ord(s[3])-49)*16+ord(s[2])-97
 pc=B[f];fl=0;pr=0
 if len(s)>4: pr="nbrq".index(s[4])+2
 if abs(pc)==1:
  if t==EP: fl=2
  elif abs(t-f)==32: fl=1
 elif abs(pc)==6 and abs(t-f)==2:
  fl=4 if t>f else 8
 return f|(t<<7)|(pr<<14)|(fl<<17)
def sq(x): return chr(97+(x&7))+str(1+(x>>4))
def uci(m):
 pr=(m>>14)&7
 return sq(m&127)+sq((m>>7)&127)+("nbrq"[pr-2] if pr else "")
PADV=[0,4,8,14,24,40,60,0]
def evl():
 mg=0;eg=0;mt=0;nb=0;bb=0
 wx=[-1]*8;wn=[8]*8;bx=[-1]*8;bn=[8]*8
 for q in WL:
  t=B[q]
  if t==6:
   mg+=CM[6][q];eg+=CE[6][q];continue
  mg+=CM[t][q];eg+=CE[t][q]
  if t==1:
   f=q&7;r=q>>4
   if r>wx[f]: wx[f]=r
   if r<wn[f]: wn[f]=r
  elif t==3: nb+=1;mt+=V[3]
  elif t==4: mt+=V[4]
  else: mt+=V[t]
 for q in BL:
  t=-B[q];mq=q^112
  if t==6:
   mg-=CM[6][mq];eg-=CE[6][mq];continue
  mg-=CM[t][mq];eg-=CE[t][mq]
  if t==1:
   f=q&7;r=q>>4
   if r>bx[f]: bx[f]=r
   if r<bn[f]: bn[f]=r
  elif t==3: bb+=1;mt+=V[3]
  elif t==4: mt+=V[4]
  else: mt+=V[t]
 if nb>1: mg+=25;eg+=25
 if bb>1: mg-=25;eg-=25
 for f in range(8):
  if wx[f]>=0:
   b0=bx[f-1] if f>0 else -1;b1=bx[f];b2=bx[f+1] if f<7 else -1
   if b0<=wx[f] and b1<=wx[f] and b2<=wx[f]: mg+=PADV[wx[f]];eg+=PADV[wx[f]]
  if bn[f]<=7:
   w0=wn[f-1] if f>0 else 8;w1=wn[f];w2=wn[f+1] if f<7 else 8
   if w0>=bn[f] and w1>=bn[f] and w2>=bn[f]: mg-=PADV[7-bn[f]];eg-=PADV[7-bn[f]]
 ph=mt
 if ph>6200: ph=6200
 s=(mg*ph+eg*(6200-ph))//6200
 return s if SD>0 else -s
def order(ms,tt,pl):
 k=KL[pl] if pl<128 else KL[127]
 sc=[]
 for m in ms:
  if m==tt: s=1000000
  else:
   f=m&127;t=(m>>7)&127;v=B[t]
   if v: s=V[abs(v)]*10-V[abs(B[f])]//10+10000
   elif (m>>17)&2: s=1000
   elif m==k[0]: s=9000
   elif m==k[1]: s=8000
   else: s=HI[abs(B[f])][t]
  sc.append((-s,m))
 sc.sort()
 return [m for _,m in sc]
def qsr(a,b,pl):
 global NN
 NN+=1
 if NN>NB: raise SE
 kc=KP[0 if SD>0 else 1]
 chk=atk(kc,-SD)
 if chk:
  lg=0
  for m in order(gen(False),0,pl):
   make(m)
   if bad():
    unmake();continue
   lg+=1
   v=-qsr(-b,-a,pl+1)
   unmake()
   if v>=b: return b
   if v>a: a=v
  if not lg: return -MT+pl
  return a
 st=evl()
 if st>=b: return b
 if st>a: a=st
 for m in order(gen(True),0,pl):
  make(m)
  if bad():
   unmake();continue
  v=-qsr(-b,-a,pl+1)
  unmake()
  if v>=b: return b
  if v>a: a=v
 return a
def srch(a,b,d,pl):
 global NN
 NN+=1
 if NN>NB: raise SE
 if HM>=100: return 0
 if d<=0: return qsr(a,b,pl)
 kc=KP[0 if SD>0 else 1]
 chk=atk(kc,-SD)
 e=TT.get(KEY)
 tt=0
 if e:
  if e[0]>=d:
   v=e[2]
   if v>MT-1000: v-=pl
   elif v<-MT+1000: v+=pl
   if e[1]==0: return v
   if e[1]==1 and v>=b: return v
   if e[1]==2 and v<=a: return v
  tt=e[3]
 if d>=3 and not chk and NPC[0 if SD>0 else 1]>0:
  ev=evl()
  if ev>=b:
   mknull()
   v=-srch(-b,-b+1,d-3,pl+1)
   unnull()
   if v>=b: return b
 ms=order(gen(False),tt,pl)
 if not ms: return -MT+pl if chk else 0
 ao=a;bv=-INF;bm=0;fst=True;rb=False
 for i,m in enumerate(ms):
  t2=(m>>7)&127;cap=bool(B[t2]) or bool((m>>17)&2)
  rep=make(m)
  if bad():
   unmake();continue
  if rep: v=25 if evl()>0 else -25 if evl()<0 else 0
  elif fst:
   v=-srch(-b,-a,d-1,pl+1);fst=False
  else:
   rd=d-1
   if d>=3 and i>3 and not cap and not chk: rd=d-2
   v=-srch(-a-1,-a,rd,pl+1)
   if v>a:
    if rd<d-1: v=-srch(-a-1,-a,d-1,pl+1)
    if v>a and v<b: v=-srch(-b,-a,d-1,pl+1)
  unmake()
  if v>bv: bv=v;bm=m;rb=rep
  if v>=b:
   if not cap:
    kp=KL[pl] if pl<128 else KL[127]
    if m!=kp[0]: kp[1]=kp[0];kp[0]=m
    HI[abs(B[m&127])][t2]+=d*d
   break
  if v>a: a=v
 if not bm: return -MT+pl if chk else 0
 if len(TT)>250000: TT.clear()
 if rb: return bv
 sv=bv
 if sv>MT-1000: sv+=pl
 elif sv<-MT+1000: sv-=pl
 TT[KEY]=(d,1 if bv>=b else 2 if bv<=ao else 0,sv,bm)
 return bv
def rsearch(d):
 e=TT.get(KEY);tt=e[3] if e else 0
 ms=order(gen(False),tt,0)
 a=-INF;best=ms[0];bv=-INF
 for m in ms:
  rep=make(m)
  if bad():
   unmake();continue
  if rep: v=0
  else: v=-srch(-INF,-a,d-1,1)
  unmake()
  if v>bv: bv=v;best=m
  if v>a: a=v
 return bv,best
def think():
 global NN
 PR.clear();PR[KEY]=1
 best=0
 for m in gen(False):
  make(m)
  if not bad(): best=m;unmake();break
  unmake()
 NN=0
 for d in range(1,17):
  try: v,bm=rsearch(d)
  except SE: break
  best=bm
  if v>=MT-100: break
 return best
def choose(g):
 setup(g["moves"])
 return uci(think())
U=os.environ.get("MAKEFUN_ENV_URL","http://127.0.0.1:8901")
def call(p,d):
 return json.loads(urllib.request.urlopen(U+p,json.dumps(d).encode()).read())
if __name__=="__main__":
 while True:
  g=call("/game",{})
  if g.get("status")=="done": break
  if g.get("status")!="your_move": continue
  call("/move",{"game":g["game"],"move":choose(g)})
