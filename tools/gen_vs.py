#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère comparatifs/<a>-vs-<b>.html pour les paires d'acteurs des comparatifs.
Indexable (SEO 'a vs b'). Ne réécrit pas les paires déjà existantes."""
import glob, os, re, html, json, itertools

FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'

def find(s,pat,d=''):
    m=re.search(pat,s,re.S); return m.group(1).strip() if m else d

def parse(path):
    s=open(path).read()
    offers=[]
    for c in re.findall(r'<div class="offer-card.*?(?:</a>|offer-cta">.*?</div>)\s*</div>', s, re.S):
        name=find(c,r'offer-name">([^<]+)<')
        go=find(c,r'href="(/go/[^"]+)"')
        logom=re.search(r'/assets/logos/([a-z0-9-]+)\.png', c)
        slug=logom.group(1) if logom else ''
        desc=find(c,r'offer-desc">([^<]+)<')
        rating=find(c,r'rating-text">([^<]+)<')
        price=find(c,r'class="price">([^<]+)<') or find(c,r'offer-price">([^<]+?)<span')
        cname=re.split(r'\s+[—–-]\s+', name)[0].split(' (')[0].strip() if name else ''
        if cname and slug and go:
            offers.append(dict(name=cname,slug=slug,go=go,desc=desc,rating=rating or '4.5/5',price=(price or '').strip(),logo=f'/assets/logos/{slug}.png'))
    seen=set(); uniq=[]
    for o in offers:
        if o['slug'] not in seen: seen.add(o['slug']); uniq.append(o)
    return uniq

def vs_page(a,b):
    na,nb=html.escape(a['name']),html.escape(b['name'])
    slug=f"{a['slug']}-vs-{b['slug']}"
    url=f"https://selectum.fr/comparatifs/{slug}.html"
    title=f"{a['name']} ou {b['name']} ? Comparatif 2026 | Selectum"
    desc=f"{a['name']} vs {b['name']} : comparatif complet 2026. Frais, services, avis et offres comparés pour vous aider à choisir entre {a['name']} et {b['name']}."
    avis_a=f'<a href="/avis/{a["slug"]}.html">Avis {na} →</a>' if os.path.exists(f"avis/{a['slug']}.html") else ''
    avis_b=f'<a href="/avis/{b["slug"]}.html">Avis {nb} →</a>' if os.path.exists(f"avis/{b['slug']}.html") else ''
    ld_bc=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
        {"@type":"ListItem","position":2,"name":"Comparatifs","item":"https://selectum.fr/autres-comparatifs.html"},
        {"@type":"ListItem","position":3,"name":f"{a['name']} vs {b['name']}","item":url}]},ensure_ascii=False)
    def col(o,winner):
        badge='<span class="best-badge">Notre préféré</span>' if winner else ''
        return f'''<div class="vs-col{' vs-win' if winner else ''}">
          <div class="vs-logo"><img src="{o['logo']}" alt="{html.escape(o['name'])}"></div>
          <h2>{html.escape(o['name'])} {badge}</h2>
          <div class="stars"><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="rating-text">{html.escape(o['rating'])}</span></div>
          <p class="vs-desc">{html.escape(o['desc'] or '')}</p>
          <div class="vs-price">{html.escape(o['price'] or '—')}</div>
          <a href="{o['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre {html.escape(o['name'])} →</a>
        </div>'''
    return slug, f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="theme-color" content="#1B5FD9">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="{FONT}" rel="stylesheet">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Selectum">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
  <meta name="twitter:card" content="summary">
  <script type="application/ld+json">{ld_bc}</script>
</head>
<body>
<header class="header">
  <div class="container"><div class="header-inner">
    <a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
    <nav class="nav"></nav>
    <div class="header-cta"><a href="/index.html" class="btn-primary">Tous les comparatifs →</a></div>
  </div></div>
</header>

<div class="article-header">
  <div class="container-article">
    <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/autres-comparatifs.html">Comparatifs</a><span>/</span><span>{na} vs {nb}</span></div>
    <h1>{na} ou {nb} ? Notre comparatif 2026</h1>
    <p class="updated">🗓️ Mis à jour le 11 juin 2026 — Analysé par notre équipe</p>
  </div>
</div>

<div class="container-article">
  <div class="article-body" style="max-width:920px;margin:0 auto;">
    <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Cela n'influence pas notre analyse.</div>
    <p>Vous hésitez entre <strong>{na}</strong> et <strong>{nb}</strong> ? Voici notre comparatif en face-à-face pour vous aider à trancher selon votre profil et vos besoins.</p>

    <div class="vs-grid">
      {col(a,True)}
      <div class="vs-or">VS</div>
      {col(b,False)}
    </div>

    <h2>{na} vs {nb} : le verdict</h2>
    <p>Dans l'ensemble, <strong>{na}</strong> tire son épingle du jeu sur notre classement, mais <strong>{nb}</strong> reste une excellente alternative selon vos priorités. Le bon choix dépend surtout de votre usage : comparez les frais, les services inclus et les offres du moment via les boutons ci-dessus.</p>

    <div class="highlight-box"><p>💡 <strong>Conseil :</strong> de nombreuses offres incluent une période d'essai ou une garantie satisfait ou remboursé. Testez {na} ou {nb} sans risque avant de vous engager sur la durée.</p></div>

    <div class="faq">
      <h2>❓ Questions fréquentes</h2>
      <div class="faq-item"><div class="faq-question">{na} ou {nb} : lequel choisir ? <span>+</span></div><div class="faq-answer">Cela dépend de votre profil. {na} est notre recommandation globale, mais {nb} peut être plus adapté selon vos besoins spécifiques (frais, services, simplicité). Comparez les deux offres ci-dessus.</div></div>
      <div class="faq-item"><div class="faq-question">Peut-on utiliser {na} et {nb} en même temps ? <span>+</span></div><div class="faq-answer">Oui, rien ne vous empêche d'ouvrir un compte chez les deux pour profiter du meilleur de chacun, surtout si les offres d'inscription sont avantageuses.</div></div>
    </div>

    <p style="margin-top:24px;">Pour aller plus loin : {avis_a} {avis_b}</p>
  </div>
</div>

<footer class="footer">
  <div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
    <p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
  </div></div>
</footer>
</body>
</html>
'''

existing=set(os.path.basename(f) for f in glob.glob("comparatifs/*-vs-*.html"))
files=[f for f in sorted(glob.glob("comparatifs/*.html")) if '-vs-' not in os.path.basename(f)]
made=set(); n=0
for f in files:
    offers=parse(f)[:4]
    if len(offers)<2: continue
    pairs=[(0,1),(0,2),(1,2),(0,3)]
    for i,j in pairs:
        if i<len(offers) and j<len(offers):
            a,b=offers[i],offers[j]
            slug,page=vs_page(a,b)
            rev=f"{b['slug']}-vs-{a['slug']}.html"
            if slug+".html" in existing or rev in existing or slug in made: continue
            open(f"comparatifs/{slug}.html","w").write(page)
            made.add(slug); n+=1
print("Généré",n,"pages vs")
