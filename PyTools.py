ó
®X]c           @   s5  d  d l  Z  d  d l Z d  d l Z d  d l Z d Z d Z d Z d Z d Z d Z	 d Z
 d	 Z d Z d
 Z d Z d Z d Z e d e d e d Z d   Z d   Z e  j d  e e  d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z d   Z e d k r1e   n  d S(   iÿÿÿÿNs   [96;1ms   [34;1ms   [33;1ms   [32;1ms   [0;1ms   [31;1ms   [36;1ms   [34ms   [32ms   [31msÀ       ____       ______            __
   / __ \__  _/_  __/___  ____  / /____
  / /_/ / / / // / / __ \/ __ \/ / ___/
 / ____/ /_/ // / / /_/ / /_/ / (__  )
/_/    \__, //_/  \____/\____/_/____/s    V1.0s   
      /____/
c           C   sA   t  t d t d t d t d  t j d  t j   d  S(   Nt   [t   !t   ]s    Exiting ...i   (   t   jalant   Ct   Rt   RRt   timet   sleept   syst   exit(    (    (    s   /sdcard/dataWCT/p.pyt   keluar   s    &c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R	   t   stdoutt   writet   flushR   R   (   t   zt   e(    (    s   /sdcard/dataWCT/p.pyR      s    t   clearc           C   sæ  t  j d  t GHd GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHt d t d t d t d	 t d t d t d GHt d t d t d t d t d t d t d GHHt d t d
 t d t d GHt d t d t d t d GHt d t d t d t d GHt d t d t d t d GHt d t d t d t d GHHt   d  S(   NR   t    R    R   R   s/   ===============================================s/    Author : Bl4ck Dr460n                         s/    Type   : python v2                            s/    Note   : Tools ini masih tahap pengembangan   t   1s   ].s    Show Tools Spammert   2s    Show All Toolst   3s    Update Toolst   4s    Chat Admint   0s    Exit The Program(	   t   ost   systemt   bannerR   t   Yt   GR   t   Wt   pil(    (    (    s   /sdcard/dataWCT/p.pyt   menu(   s     99999!!!!!c          C   s÷   t  t d t  }  |  d k rK t d t d t d t d GHt   n¨ |  d k ra t   n |  d k rw t   n| |  d	 k r t	   nf |  d
 k rµ d GHt
 j d  t   n> |  d k rË t   n( t d t d t d t d GHt   d  S(   Ns	   Choose > R   R    R   R   s    Wrong InputR   R   R   R   s7   Maaf Tools Masih Tahap Pengembangan Pilih Yang Lain Ajai   R   (   t	   raw_inputR   R   R   R   R   R   t   spamt   toolst   updateR   R   R   (   t   bil(    (    s   /sdcard/dataWCT/p.pyR   :   s$    !





!c           C   s  t  j d  t GHd GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHHt d t d t d	 t d
 GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHHt   d  S(   NR   R   R    R   R   s   ===============================s    Author : Bl4ck Dr460n         R   s   ].s
    TokopediaR   s
    BukalapakR   s    GrabR   s
    Telkomselt   5s    Email SpamR   s    Back(	   R   R   R   R   R   R   R   R   t   spampil(    (    (    s   /sdcard/dataWCT/p.pyR!   O   s    999!!!!!!c          C   s  t  t d t  }  |  d k rK t d t d t d t d GHt   nH|  d k rÃ t j d  t	 GHt j d	  t j d
  t j d  t j d  t j d  Ht  t d  t
   nÐ|  d k r;t j d  t	 GHt j d	  t j d
  t j d  t j d  t j d  Ht  t d  t
   nX|  d k r¦t j d  t	 GHt j d	  t j d  t j d  t j d  Ht  t d  t
   ní |  d k rt j d  t	 GHt j d  t j d  t j d  Ht  t d  t
   n |  d k rUt j d  t	 GHt j d  t j d  Ht  t d  t
   n> |  d k rkt   n( t d t d t d t d GHt   d  S(   Ns	   Choose > t    R    R   R   s    Wrong InputR   R   s   pkg update -ys   pkg upgrade -ys    pkg install git php curl wget -ys3   git clone https://github.com/nee48/BomTelpSmsTokpeds   mv BomTelpSmsTokped $HOMEs    Enter To ReturnR   s    pkg install php wget curl git -ys;   git clone https://github.com/mukhlisakbr/spam-otp-bukalapaks   mv spam-otp-bukalapak $HOMER   s    pkg install php gut curl wget -ys:    git clone https://github.com/WattanaGaming/Spammer-Grab-1s   mv Spammer-Grab-1 $HOMER   sC   pkg update -y && pkg upgrade -y && pkg install php curl wget git -ys6   git clone https://github.com/ilhamhax0r/TSEL-Spam-Codes   mv TSEL-Spam-Code $HOMER%   sZ   pkg install git php curl wget -y && git clone https://github.com/Juniorn1003/Email-Spammers   mv Email-Spammer $HOMER   (   R    R   R   R   R   R   R&   R   R   R   R!   R   (   t   pilspam(    (    s   /sdcard/dataWCT/p.pyR&   `   sr    !






!c           C   sS  t  j d  t GHd GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHHt d t d t d	 t d
 GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHHt   d  S(   NR   R   R    R   R   s   ===============================s    Author : Bl4ck Dr460n         R   s   ].s    Information GatheringR   s    Password AttacksR   s    Web HackingR   s    Back(	   R   R   R   R   R   R   R   R   t   piltools(    (    (    s   /sdcard/dataWCT/p.pyR"      s    999!!!!c          C   sÏ   t  t d t  }  |  d k rK t d t d t d t d GHt   n  |  d k ra t   nj |  d k rw t   nT |  d	 k r t	   n> |  d
 k r£ t
   n( t d t d t d t d GHt   d  S(   Ns	   Choose > R'   R    R   R   s    Wrong InputR   R   R   R   (   R    R   R   R   R   R   R)   t   InGt   PassAttackst
   WebHackingR   (   t   tpil(    (    s   /sdcard/dataWCT/p.pyR)   ª   s    !




!c           C   st  t  j d  t GHd GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHHt d t d t d	 t d
 GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHHt   d  S(   NR   R   R    R   R   s   ===============================s    Author : Bl4ck Dr460n         R   s   ].s    NmapR   s    Black HydraR   s    SqlmapR   s	    Red HawkR   s    Back(	   R   R   R   R   R   R   R   R   t   InGPil(    (    (    s   /sdcard/dataWCT/p.pyR*   »   s    999!!!!!c          C   s×  t  t d t  }  |  d k rK t d t d t d t d GHt   n|  d k r t j d  t j d	  Ht  t d
  t	   nI|  d k rã t j d  t j d  t j d  t j d  Ht  t d
  t	   nð |  d k r<t j d  t j d  t j d  t j d  Ht  t d
  t	   n |  d k rt j d  t j d  t j d  t j d  Ht  t d
  t	   n> |  d k r«t
   n( t d t d t d t d GHt   d  S(   Ns
   Choose >  R'   R    R   R   s    Wrong InputR   s   pkg install nmap -ys   pkg update -y && pkg upgrade -ys    Enter To ReturnR   s   apt update && apt upgrades   apt install hydra git python2s1   git clone https://github.com/Gameye98/Black-Hydras   mv Black-Hydra ~R   s   apt install git python2s1   git clone https://github.com/sqlmapproject/sqlmaps   mv sqlmap ~R   s   apt install git phps2   git clone https://github.com/Tuhinshubhra/RED_HAWKs   mv RED_HAWK ~R   (   R    R   R   R   R   R   R.   R   R   R*   R"   (   t   piling(    (    s   /sdcard/dataWCT/p.pyR.   Ë   sL    !





!c           C   s[  t  j d  t GHd GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHt d t d t d t d t d t d t d GHHt d t d t d	 t d
 GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHt d t d t d	 t d GHHt   d  S(   NR   R   R    R   R   s   ===============================s    Author : Bl4ck Dr460n         R   s   ].s    CuppR   s    Indonesian WordlistR   s    ASUR   s    Dark FbR%   t   6t   7t   8t   9t   10t   11t   00(	   R   R   R   R   R   R   R   R   t   passpil(    (    (    s   /sdcard/dataWCT/p.pyR+   ó   s*    999!!!!!!!!!!!!c          C   sM  t  t d t  }  |  d k rK t d t d t d t d GHt   nþ t d k r¤ t j	 d  t j	 d	  t j	 d
  t j	 d  Ht  t d  t
   n¥ t d k rý t j	 d  t j	 d  t j	 d  t j	 d  Ht  t d  t
   nL t d k rIt j	 d  t j	 d  t j	 d  Ht  t d  t
   n  d  S(   Ns
   Choose >  R'   R    R   R   s    Wrong InputR   s   apt update && apt upgrades   apt install python2 gits'   git clone https://github.com/Mebus/cupps	   mv cupp ~s    Enter To ReturnR   s   apt install gits8   git clone https://github.com/geovedi/indonesian-wordlists   mv indonesian-wordlist $HOMER   sl   pkg update -y && pkg upgrade -y && pkg install python2 python curl wget git -y && pip2 install bs4 mechanizes(   git clone https://github.com/LOoLzeC/ASUs   mv ASU $HOME(   R    R   R   R   R   R   R7   t   pilpsaaR   R   R+   (   t   pilpass(    (    s   /sdcard/dataWCT/p.pyR7   
  s6    !


t   __main__(    R   R	   R   t   requestst   GLt   BBt   YYt   GGt   WWR   t   CCt   BR   R   R   R   R   R   R   R   R   R   R   R!   R&   R"   R)   R*   R.   R+   R7   t   __name__(    (    (    s   /sdcard/dataWCT/p.pyt   <module>   s>   0		
				;				(		!