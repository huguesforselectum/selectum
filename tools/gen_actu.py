#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère actualites/<slug>.html : page 'Promotions & nouveautés <catégorie>' par top comparatif."""
import re, os, json, html
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
TOP={"banque-en-ligne":"banque en ligne","crypto":"plateformes crypto","trading-bourse":"courtiers en bourse","hebergement-web":"hébergement web","vpn":"VPN","assurance-auto":"assurance auto","mutuelle-sante":"mutuelle santé","logiciels-comptabilite":"logiciels de comptabilité"}
RISK={"crypto","trading-bourse"}

def parse(slug):
    s=open(f"comparatifs/{slug}.html").read()
    offers=[]
    for c in re.findall(r'<div class="offer-card.*?(?:</a>|offer-cta">.*?</div>)\s*</div>', s, re.S):
        lm=re.search(r'/assets/logos/([a-z0-9-]+)\.png', c); nm=re.search(r'offer-name">([^<]+)<', c)
        go=re.search(r'href="(/go/[^"]+)"', c); d=re.search(r'offer-desc">([^<]+)<', c)
        pr=re.search(r'class="price">([^<]+)<', c) or re.search(r'offer-price">([^<]+?)<span', c)
        if not(lm and nm): continue
        a=lm.group(1)
        if any(o['slug']==a for o in offers): continue
        name=re.split(r'\s+[—–-]\s+', nm.group(1))[0].split(' (')[0].strip()
        offers.append(dict(slug=a,name=name,go=(go.group(1) if go else f"/go/{a}"),desc=(d.group(1).strip() if d else ''),price=(pr.group(1).strip() if pr else '')))
    return offers

def page(slug,cl):
    offers=parse(slug); url=f"https://selectum.fr/actualites/{slug}.html"
    risk=" Investir comporte un risque de perte en capital." if slug in RISK else ""
    title=f"Promotions {cl} : les meilleures offres de juin 2026 | Selectum"
    desc=f"Toutes les promotions et nouveautés {cl} en juin 2026 : offres, bonus et codes promo du moment, vérifiés par notre équipe Selectum."
    rows=""
    for i,o in enumerate(offers,1):
        n=html.escape(o['name'])
        rows+=f'''<div class="actu-item">
          <div class="actu-logo"><img src="/assets/logos/{o['slug']}.png" alt="{n}"></div>
          <div class="actu-body"><h3>{n}{' — '+html.escape(o['price']) if o['price'] else ''}</h3><p>{html.escape(o['desc'])}</p>
          <div class="actu-links"><a href="/code-promo/{o['slug']}.html">Code promo</a> · <a href="/avis/{o['slug']}.html">Avis</a> · <a href="/guides/{o['slug']}.html">Guide</a></div></div>
          <a href="{o['go']}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a>
        </div>''' if os.path.exists(f"guides/{o['slug']}.html") else f'''<div class="actu-item">
          <div class="actu-logo"><img src="/assets/logos/{o['slug']}.png" alt="{n}"></div>
          <div class="actu-body"><h3>{n}{' — '+html.escape(o['price']) if o['price'] else ''}</h3><p>{html.escape(o['desc'])}</p>
          <div class="actu-links"><a href="/code-promo/{o['slug']}.html">Code promo</a> · <a href="/avis/{o['slug']}.html">Avis</a></div></div>
          <a href="{o['go']}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a>
        </div>'''
    ld=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-01","dateModified":"2026-06-11","mainEntityOfPage":url},ensure_ascii=False)
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="article"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<meta name="twitter:card" content="summary"><script type="application/ld+json">{ld}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/comparatifs/{slug}.html" class="btn-primary">Voir le comparatif →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span>Actualités<span>/</span>Promotions {cl}</div>
  <h1>Promotions {cl} : les meilleures offres de juin 2026</h1>
  <p class="updated">🗓️ Mis à jour le 11 juin 2026 — vérifié par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.{risk}</div>
  <p>Voici les <strong>offres et promotions {cl} du moment</strong>, mises à jour en juin 2026. Pour chaque acteur, retrouvez l'offre en cours et nos pages détaillées (avis, code promo, guide).</p>
  <div class="actu-list">{rows}</div>
  <p style="margin-top:24px;">👉 Pour le classement complet, consultez notre <a href="/comparatifs/{slug}.html">comparatif {cl}</a>.</p>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

n=0
for slug,cl in TOP.items():
    open(f"actualites/{slug}.html","w").write(page(slug,cl)); n+=1
print("Généré",n,"pages actualités")
