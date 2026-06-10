#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère des hubs d'index pour avis/, code-promo/, parrainage/ (liste toutes les marques)."""
import glob, os, re, html
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'

def brand_name(slug):
    # nom depuis la page avis si dispo
    f=f"avis/{slug}.html"
    if os.path.exists(f):
        m=re.search(r'<title>Avis ([^—|:]+?)\s*(?:202\d|—|:|\|)', open(f).read())
        if m: return m.group(1).strip()
    return slug.replace('-',' ').title()

def shell(title,desc,canon,h1,sub,inner):
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{canon}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/index.html" class="btn-primary">Tous les comparatifs →</a></div>
</div></div></header>
<div class="hero" style="padding:56px 0 48px;"><div class="container"><div class="hero-content"><h1>{html.escape(h1)}</h1><p>{html.escape(sub)}</p></div></div></div>
<section class="section"><div class="container">{inner}</div></section>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

CFG=[
 ("avis","Avis","Tous nos avis : tests détaillés, notes et offres","Avis de marques","Nos tests et avis indépendants, marque par marque.","avis"),
 ("code-promo","Codes promo","Tous les codes promo et offres vérifiés","Codes promo & offres","Les meilleures offres et réductions du moment, vérifiées.","code-promo"),
 ("parrainage","Parrainages","Tous les programmes de parrainage & bonus","Parrainages & bonus","Les bonus de parrainage à connaître, marque par marque.","parrainage"),
]
out=[]
for folder,word,metadesc,h1,sub,fname in CFG:
    slugs=sorted(os.path.basename(f)[:-5] for f in glob.glob(f"{folder}/*.html"))
    items=""
    for s in slugs:
        logo=f'<img src="/assets/logos/{s}.png" alt="" style="height:20px;max-width:70px;object-fit:contain;vertical-align:middle;margin-right:8px;">' if os.path.exists(f"assets/logos/{s}.png") else ''
        items+=f'<a href="/{folder}/{s}.html" class="hub-item">{logo}{word} {html.escape(brand_name(s))}</a>\n'
    inner=f'<div class="section-title"><div class="eyebrow">{len(slugs)} marques</div><h2>{html.escape(h1)}</h2></div><div class="hub-grid">{items}</div>'
    title=f"{h1} 2026 | Selectum"
    canon=f"https://selectum.fr/{fname}.html"
    open(f"{fname}.html","w").write(shell(title,metadesc,canon,h1,sub,inner))
    out.append((f"{fname}.html",len(slugs)))
for o in out: print("créé:",o[0],"->",o[1],"liens")
