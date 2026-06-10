#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère guides/<slug>.html : article guide informationnel par marque (top comparatifs)."""
import json, html, os, re
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
data=json.load(open("/tmp/top_actors.json"))
CMP={"banque-en-ligne":"/comparatifs/banque-en-ligne.html","crypto":"/comparatifs/crypto.html","trading-bourse":"/comparatifs/trading-bourse.html","hebergement-web":"/comparatifs/hebergement-web.html","vpn":"/comparatifs/vpn.html","assurance-auto":"/comparatifs/assurance-auto.html","mutuelle-sante":"/comparatifs/mutuelle-sante.html","logiciels-comptabilite":"/comparatifs/logiciels-comptabilite.html"}
RISK={"crypto","trading-bourse"}
# verbe d'action selon catégorie
ACTION={"banque-en-ligne":"ouvrir un compte","crypto":"créer un compte","trading-bourse":"ouvrir un compte","hebergement-web":"souscrire un hébergement","vpn":"souscrire un abonnement","assurance-auto":"souscrire un contrat","mutuelle-sante":"souscrire une mutuelle","logiciels-comptabilite":"créer un compte"}

def page(d):
    n=html.escape(d['name']); cl=d['catlabel']; slug=d['slug']
    url=f"https://selectum.fr/guides/{slug}.html"
    action=ACTION[d['cat']]; cmp=CMP[d['cat']]
    risk = " Investir comporte un risque de perte en capital." if d['cat'] in RISK else ""
    title=f"{d['name']} : comment ça marche ? Guide complet 2026 | Selectum"
    desc=f"Guide {d['name']} 2026 : comment {action}, fonctionnement, frais, sécurité et conseils. Tout savoir sur {d['name']} ({cl}) avant de vous lancer."
    rel=[]
    for t,p in [("Avis","avis"),("Code promo","code-promo"),("Parrainage","parrainage")]:
        if os.path.exists(f"{p}/{slug}.html"): rel.append(f'<li><a href="/{p}/{slug}.html">{t} {n} →</a></li>')
    rel.append(f'<li><a href="{cmp}">Comparatif {cl} →</a></li>')
    qa=[(f"Comment {action} chez {d['name']} ?",f"Rendez-vous sur le site de {d['name']}, cliquez sur l'inscription, renseignez vos informations et validez votre identité. Le parcours est 100% en ligne et prend quelques minutes."),
        (f"{d['name']} est-il fiable ?",f"{d['name']} est un acteur établi de sa catégorie ({cl}). Nous l'analysons en détail dans notre avis dédié."),
        (f"Quels sont les frais de {d['name']} ?",f"Les conditions tarifaires de {d['name']} évoluent régulièrement. Consultez la page de l'offre et notre avis pour le détail à jour.")]
    qatxt=[(html.escape(q),html.escape(a)) for q,a in qa]
    ld_article=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-11","dateModified":"2026-06-11","mainEntityOfPage":url},ensure_ascii=False)
    ld_faq=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]},ensure_ascii=False)
    ld_bc=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},{"@type":"ListItem","position":2,"name":"Guides","item":"https://selectum.fr/guides/"},{"@type":"ListItem","position":3,"name":d['name'],"item":url}]},ensure_ascii=False)
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
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{ld_article}</script>
<script type="application/ld+json">{ld_faq}</script>
<script type="application/ld+json">{ld_bc}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="{cmp}" class="btn-primary">Voir le comparatif →</a></div>
</div></div></header>
<div class="brand-hero"><div class="container-article">
  <div class="brand-hero-logo"><img src="/assets/logos/{slug}.png" alt="{n}"></div>
  <div class="brand-hero-text">
    <div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / Guides / {n}</div>
    <h1>{n} : comment ça marche ? Le guide complet</h1>
    <p class="subtitle">Tout savoir sur {n} ({cl}) : fonctionnement, inscription, frais et sécurité.</p>
    <p class="updated">🗓️ Mis à jour le 11 juin 2026</p>
  </div></div></div>
<div class="container-article"><div class="article-layout" style="grid-template-columns: 1fr 300px;"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.{risk}</div>
  <div class="intro-box"><p>{n} est l'un des acteurs de référence côté <strong>{cl}</strong>. {html.escape(d['desc'])}. Dans ce guide, on vous explique simplement comment {action}, ce qu'il faut savoir sur les frais et la sécurité, et pour qui {n} est fait.</p></div>
  <h2 id="cest-quoi">{n}, c'est quoi ?</h2>
  <p>{n} se positionne sur le marché {cl}. {html.escape(d['desc'])}. C'est une option que nous retenons dans notre <a href="{cmp}">comparatif {cl}</a>.</p>
  <h2 id="ouvrir">Comment {action} chez {n} ?</h2>
  <ol>
    <li>Accédez à l'offre {n} et lancez l'inscription en ligne.</li>
    <li>Renseignez vos informations personnelles et créez vos identifiants.</li>
    <li>Validez votre identité (pièce justificative) — étape rapide et sécurisée.</li>
    <li>Finalisez : votre accès {n} est opérationnel en quelques minutes.</li>
  </ol>
  <h2 id="frais">Frais et tarifs {n}</h2>
  <p>Les tarifs {n} dépendent de la formule choisie et évoluent régulièrement. Pour le détail chiffré et à jour, consultez notre <a href="/avis/{slug}.html">avis {n}</a> ainsi que la page officielle de l'offre.</p>
  <h2 id="securite">{n} est-il fiable et sécurisé ?</h2>
  <p>{n} applique les standards de sécurité de son secteur. Nous détaillons sa fiabilité, ses garanties et les retours clients dans notre avis dédié.{(' '+risk.strip()) if risk else ''}</p>
  <div class="highlight-box"><p>💡 <strong>Astuce :</strong> avant de souscrire, vérifiez les offres en cours sur notre <a href="/code-promo/{slug}.html">page code promo {n}</a> et le <a href="/parrainage/{slug}.html">programme de parrainage {n}</a> pour économiser.</p></div>
  <div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qatxt)+f'''</div>
</main>
<aside class="sidebar">
  <div class="sidebar-cta"><h4>👉 {n}</h4><p>Découvrez l'offre {n} du moment.</p><a href="{d['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
  <div class="sidebar-card"><h4>🔗 À lire aussi</h4><ul class="sidebar-toc">{''.join(rel)}</ul></div>
</aside>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

n=0
for slug,d in data.items():
    open(f"guides/{slug}.html","w").write(page(d)); n+=1
print("Généré",n,"guides")
