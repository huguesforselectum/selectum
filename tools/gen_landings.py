#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère une landing paid (lp/<slug>.html) pour chaque comparatif (hors *vs*).
Pages conversion-focused, noindex (ne pas concurrencer l'organique).
Réutilisable : relancer pour régénérer après ajout/modif de comparatifs."""
import re, glob, os, html

FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'

def txt(s): return re.sub(r'\s+',' ', re.sub(r'<[^>]+>','',s)).strip()
def find(s,pat,d=''):
    m=re.search(pat,s,re.S); return m.group(1).strip() if m else d

def parse(path):
    s=open(path).read()
    slug=os.path.basename(path)[:-5]
    title=txt(find(s,r'<title>(.*?)</title>'))
    desc=find(s,r'<meta name="description" content="([^"]*)"')
    h1=txt(find(s,r'<h1[^>]*>(.*?)</h1>'))
    # tous les offer-card dans l'ordre
    cards=re.findall(r'<div class="offer-card[^"]*">(.*?)(?=<div class="offer-card|</div>\s*</div>\s*<h2|<div class="offers-list"|$)', s, re.S)
    offers=[]
    for c in re.findall(r'<div class="offer-card.*?</a>\s*</div>|<div class="offer-card.*?offer-cta.*?</div>\s*</div>', s, re.S):
        name=find(c,r'offer-name">([^<]+)<')
        go=find(c,r'href="(/go/[^"]+)"')
        logo=find(c,r'offer-logo[^>]*><img src="([^"]+)"')
        d=find(c,r'offer-desc">([^<]+)<')
        rating=find(c,r'rating-text">([^<]+)<')
        price=find(c,r'class="price">([^<]+)<') or find(c,r'offer-price">([^<<]+?)<span')
        if name and go:
            cname=re.split(r'\s+[—–-]\s+', name)[0].split(' (')[0].strip()
            offers.append(dict(name=cname,go=go,logo=logo,desc=d,rating=rating,price=price.strip()))
    # dédoublonne par nom en gardant l'ordre
    seen=set(); uniq=[]
    for o in offers:
        if o['name'] not in seen: seen.add(o['name']); uniq.append(o)
    return dict(slug=slug,title=title,desc=desc,h1=h1,offers=uniq[:5])

def landing(d):
    if not d['offers']: return None
    top=d['offers'][0]
    others=d['offers'][1:4]
    short_h1 = re.sub(r'\s*:?\s*(le )?comparatif.*$','',d['h1'],flags=re.I).strip() or d['h1']
    logo = f'<img src="{top["logo"]}" alt="{html.escape(top["name"])}" class="lp-logo">' if top.get('logo') else ''
    rating = f'<div class="stars"><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="rating-text">{top["rating"] or "4.8/5"}</span></div>'
    others_html=''
    for i,o in enumerate(others,2):
        ol=f'<img src="{o["logo"]}" alt="{html.escape(o["name"])}">' if o.get("logo") else ''
        others_html+=f'''<div class="lp-alt">
          <span class="lp-alt-rank">{i}</span>
          <div class="lp-alt-logo">{ol}</div>
          <div class="lp-alt-info"><strong>{html.escape(o["name"])}</strong><span>{html.escape(o["desc"] or "")}</span></div>
          <a href="{o["go"]}" class="btn-secondary" target="_blank" rel="sponsored nofollow noopener">Voir →</a>
        </div>'''
    price_html=f'<div class="lp-price">{html.escape(top["price"])}</div>' if top.get('price') else ''
    title=f'{short_h1} — Notre n°1 : {top["name"]} | Selectum'
    desc=html.escape(d['desc'] or f"Découvrez notre sélection n°1 pour {short_h1.lower()} : {top['name']}. Comparez les meilleures offres et profitez de l'offre du moment.")
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="theme-color" content="#1B5FD9">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex, follow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONT}" rel="stylesheet">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body class="lp">
<header class="lp-header">
  <div class="container lp-header-in">
    <a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum" class="logo-img"></a>
    <span class="lp-trust">Comparatif indépendant · mis à jour en 2026</span>
  </div>
</header>

<section class="lp-hero">
  <div class="container-sm">
    <div class="lp-badge">★ Recommandé par Selectum</div>
    <h1>{html.escape(short_h1)}</h1>
    <p class="lp-sub">Notre équipe a comparé les meilleures offres. Voici notre <strong>n°1</strong> et les alternatives à connaître.</p>
    <div class="lp-card">
      <div class="lp-card-top">
        <div class="lp-card-logo">{logo}</div>
        <div class="lp-card-main">
          <div class="lp-rankpill">N°1</div>
          <h2>{html.escape(top["name"])}</h2>
          <p>{html.escape(top["desc"] or "")}</p>
          {rating}
        </div>
        {price_html}
      </div>
      <a href="{top["go"]}" class="btn-green lp-cta" target="_blank" rel="sponsored nofollow noopener">Voir l'offre {html.escape(top["name"])} →</a>
      <div class="lp-reassure">✓ Sans engagement &nbsp;·&nbsp; ✓ Offre vérifiée &nbsp;·&nbsp; ✓ 100% indépendant</div>
    </div>
  </div>
</section>

<section class="lp-section">
  <div class="container-sm">
    <h3 class="lp-h3">Les alternatives</h3>
    <div class="lp-alts">{others_html}</div>
  </div>
</section>

<section class="lp-section lp-why">
  <div class="container-sm">
    <h3 class="lp-h3">Pourquoi suivre notre recommandation ?</h3>
    <div class="lp-why-grid">
      <div><strong>Indépendant</strong><span>Nos classements reposent sur des critères objectifs, pas sur les commissions.</span></div>
      <div><strong>À jour</strong><span>Offres et tarifs vérifiés régulièrement pour refléter le marché réel.</span></div>
      <div><strong>Transparent</strong><span>On vous dit clairement ce que vaut chaque offre, sans bla-bla.</span></div>
    </div>
  </div>
</section>

<section class="lp-final">
  <div class="container-sm">
    <h3>Prêt à choisir {html.escape(top["name"])} ?</h3>
    <a href="{top["go"]}" class="btn-green lp-cta" target="_blank" rel="sponsored nofollow noopener">Profiter de l'offre →</a>
    <p class="lp-finalnote">Vous préférez tout comparer ? <a href="/comparatifs/{d['slug']}.html">Voir le comparatif complet</a></p>
  </div>
</section>

<footer class="lp-footer">
  <div class="container-sm">
    © 2026 Selectum — HALBC SAS · <a href="/mentions-legales.html">Mentions légales</a> · <a href="/politique-confidentialite.html">Confidentialité</a>
    <div class="lp-disclaimer">Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
  </div>
</footer>
</body>
</html>
'''

def main():
    files=[f for f in sorted(glob.glob("comparatifs/*.html")) if 'vs' not in os.path.basename(f)]
    n=0; skipped=[]
    for f in files:
        d=parse(f)
        page=landing(d)
        if not page: skipped.append(d['slug']); continue
        open(f"lp/{d['slug']}.html","w").write(page)
        n+=1
    print(f"Généré {n} landings dans lp/")
    if skipped: print("Ignorés (pas d'offres parsées):", skipped)

if __name__=="__main__":
    main()
