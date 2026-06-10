#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconstruit la 1re carte (top-pick) en structure premium : rang|logo | checklist | [score/CTA/site]."""
import glob, os, re, html

DOMAINS={"bitpanda":"bitpanda.com","kraken":"kraken.com","coinhouse":"coinhouse.com","crypto-com":"crypto.com",
 "boursobank":"boursobank.com","fortuneo":"fortuneo.fr","hellobank":"hellobank.fr","monabanq":"monabanq.com",
 "trade-republic":"traderepublic.com","xtb":"xtb.com","degiro":"degiro.fr","etoro":"etoro.com",
 "o2switch":"o2switch.com","infomaniak":"infomaniak.com","hostinger":"hostinger.fr","ovhcloud":"ovhcloud.com","ionos":"ionos.fr",
 "nordvpn":"nordvpn.com","expressvpn":"expressvpn.com","surfshark":"surfshark.com","protonvpn":"protonvpn.com","cyberghost":"cyberghost.com",
 "maif":"maif.fr","alan":"alan.com","younited":"younited-credit.com","qonto":"qonto.com","shine":"shine.fr",
 "pennylane":"pennylane.com","wise":"wise.com","revolut":"revolut.com","n26":"n26.com"}

def field(s,pat,d=''):
    m=re.search(pat,s,re.S); return m.group(1).strip() if m else d

def upgrade(path):
    s=open(path).read()
    start=s.find('<div class="offer-card top-pick">')
    if start<0: return False,"no top-pick"
    nxt=s.find('<div class="offer-card', start+10)
    if nxt<0: return False,"single card"
    card=s[start:nxt]
    logo_m=re.search(r'/assets/logos/([a-z0-9-]+)\.png', card)
    slug=logo_m.group(1) if logo_m else ''
    name=field(card,r'offer-name">([^<]+)<')
    desc=field(card,r'offer-desc">([^<]+)<')
    rating=field(card,r'rating-text">([^<]+)<')  # ex 4.6/5
    go=field(card,r'href="(/go/[^"]+)"', f"/go/{slug}")
    tags=re.findall(r'offer-tag[^>]*>([^<]+)<', card)
    price=field(card,r'class="price">([^<]+)<') or field(card,r'offer-price">([^<]+?)<span')
    if not (slug and name and go): return False,"parse-fail"
    # score /10
    score="9,5"
    rm=re.match(r'([0-9]+[.,]?[0-9]*)\s*/\s*5', rating)
    if rm:
        try: score=("%.1f"%(float(rm.group(1).replace(',','.'))*2)).replace('.',',')
        except: pass
    # checklist = desc (1re puce) + tags
    items=[]
    if desc: items.append(desc)
    items += [t for t in tags if t.strip()]
    items=items[:5]
    checklist="".join(f"<li>{html.escape(i)}</li>" for i in items)
    avis = f"/avis/{slug}.html" if os.path.exists(f"avis/{slug}.html") else go
    dom = DOMAINS.get(slug)
    gosite = f'<a class="tp-gosite" href="{go}" target="_blank" rel="sponsored nofollow noopener">Aller sur {html.escape(dom)} →</a>' if dom else f'<a class="tp-gosite" href="{go}" target="_blank" rel="sponsored nofollow noopener">Aller sur le site →</a>'
    pricebox = f'<div class="tp-price">{html.escape(price)}</div>' if price else ''
    new=f'''<div class="offer-card top-pick">
          <div class="tp-rank">1</div>
          <div class="tp-logo"><img src="/assets/logos/{slug}.png" alt="{html.escape(name)}" loading="lazy"></div>
          <div class="tp-main">
            <div class="tp-name">{html.escape(name)}</div>
            <ul class="tp-checklist">{checklist}</ul>
            <a class="tp-more" href="{avis}">En savoir plus →</a>
          </div>
          <div class="tp-side">
            <div class="tp-score"><b>{score}</b><span>/10</span><small>Note Selectum</small></div>
            {pricebox}
            <a class="btn-green tp-cta" href="{go}" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a>
            {gosite}
          </div>
        </div>'''
    s2=s[:start]+new+s[nxt:]
    # garde le même nombre de cartes
    if s2.count('<div class="offer-card')!=s.count('<div class="offer-card'): return False,"count-mismatch"
    open(path,'w').write(s2)
    return True,slug

ok=0; skip=[]
for f in sorted(glob.glob("comparatifs/*.html")):
    if '-vs-' in f: continue
    r,info=upgrade(f)
    if r: ok+=1
    else: skip.append((os.path.basename(f),info))
print("top-pick reconstruites:",ok)
if skip: print("ignorées:",skip)
