#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les hubs index : /guides-marques.html et /actualites.html (listent guides & actu)."""
import glob, os, re, html
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'

def name_from(path, prefix):
    s=open(path).read()
    m=re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    t=re.sub(r'<[^>]+>','',m.group(1)).strip() if m else os.path.basename(path)[:-5]
    return t

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
<div class="hero" style="padding:56px 0 48px;"><div class="container"><div class="hero-content">
<h1>{html.escape(h1)}</h1><p>{html.escape(sub)}</p>
</div></div></div>
<section class="section"><div class="container">{inner}</div></section>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

# Hub guides marques
gfiles=sorted(glob.glob("guides/*.html"))
# garde uniquement les guides "marque" (présents dans assets/logos)
items=""
for f in gfiles:
    slug=os.path.basename(f)[:-5]
    if not os.path.exists(f"assets/logos/{slug}.png"): continue
    nm=name_from(f,'guides')
    items+=f'<a href="/guides/{slug}.html" class="hub-item"><img src="/assets/logos/{slug}.png" alt="" style="height:22px;max-width:80px;object-fit:contain;vertical-align:middle;margin-right:8px;">{html.escape(nm)}</a>\n'
inner=f'<div class="section-title"><div class="eyebrow">Guides par marque</div><h2>Tous nos guides</h2></div><div class="hub-grid">{items}</div>'
open("guides-marques.html","w").write(shell("Guides par marque : comment ça marche ? | Selectum",
  "Tous nos guides par marque : comment fonctionne chaque service, comment ouvrir un compte, frais et sécurité.",
  "https://selectum.fr/guides-marques.html","Guides par marque","Comprendre chaque service et savoir comment s'y inscrire.",inner))

# Hub actualités
afiles=sorted(glob.glob("actualites/*.html"))
items=""
for f in afiles:
    slug=os.path.basename(f)[:-5]; nm=name_from(f,'actualites')
    items+=f'<a href="/actualites/{slug}.html" class="hub-item">{html.escape(nm)}</a>\n'
inner=f'<div class="section-title"><div class="eyebrow">Actualités & promotions</div><h2>Les offres du moment</h2></div><div class="hub-grid">{items}</div>'
open("actualites.html","w").write(shell("Actualités & promotions : meilleures offres 2026 | Selectum",
  "Toutes les promotions et offres du moment par catégorie : banque, crypto, bourse, VPN, hébergement, assurance, logiciels.",
  "https://selectum.fr/actualites.html","Actualités & promotions","Les meilleures offres du moment, mises à jour régulièrement.",inner))
print("hubs créés: guides-marques.html + actualites.html")
