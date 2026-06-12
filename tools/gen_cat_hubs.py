#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hubs code-promo par catégorie : /code-promo-<cat>.html (cibles backlinks + maillage)."""
import os, re, glob, html, json
FONT="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D="12 juin 2026"
noindex=set(open("/tmp/noindex_slugs.txt").read().split()) if os.path.exists("/tmp/noindex_slugs.txt") else set()
AFF={"airwallex","coinbase","expressvpn","flatpay","kraken","linxea","n26","santevet","shopify","sumup","wallester","xtb"}

def members_from(comparatifs):
    out=[]
    for c in comparatifs:
        f=f"comparatifs/{c}.html"
        if not os.path.exists(f): continue
        for m in re.finditer(r'/go/([a-z0-9-]+)', open(f).read()):
            s=m.group(1)
            if os.path.exists(f"code-promo/{s}.html") and s not in out:
                out.append(s)
    return out

def name_of(slug):
    t=open(f"code-promo/{slug}.html",encoding="utf-8").read()
    m=re.search(r'<h1>(?:Code promo|Promo)\s+(.+?)(?:\s+2026|\s*:|\s*</h1>)',t)
    return m.group(1).strip() if m else slug.replace("-"," ").title()

# slug, h1, intro, comparatif_url, comparatif_label, source comparatifs
HUBS=[
 ("crypto","Codes promo crypto 2026 : toutes les offres des applications crypto",
  "Vous cherchez un code promo pour une application crypto ? Voici les offres de bienvenue vérifiées des principaux acteurs (Coinbase, Kraken, Bitpanda…), et comment en profiter — sans code à recopier le plus souvent.",
  "/comparatifs/crypto.html","comparatif des applications crypto",["crypto","crypto-debutant","crypto-frais-bas"]),
 ("banque","Codes promo banque en ligne 2026 : primes de bienvenue",
  "Les banques en ligne et néobanques proposent régulièrement des primes de bienvenue à l'ouverture d'un compte. Retrouvez les offres vérifiées (N26, Revolut, BoursoBank…) et les conditions.",
  "/comparatifs/banque-en-ligne.html","comparatif des banques en ligne",["banque-en-ligne","cartes-famille"]),
 ("bourse","Codes promo courtiers en bourse 2026 : offres de bienvenue",
  "Les courtiers en bourse offrent souvent un avantage à l'inscription ou des frais réduits. Comparez les offres (XTB, Trade Republic, DEGIRO…) avant d'ouvrir un PEA ou un compte-titres.",
  "/comparatifs/trading-bourse.html","comparatif des courtiers en bourse",["trading-bourse"]),
 ("compte-pro","Codes promo comptes pro 2026 : offres pour entreprises",
  "Ouvrir un compte professionnel avec une offre de bienvenue : retrouvez les promotions vérifiées des comptes pros (Qonto, Shine, Finom…) pour indépendants, TPE et sociétés.",
  "/comparatifs/comptes-pro.html","comparatif des comptes pro",["comptes-pro"]),
 ("paiement","Codes promo terminaux de paiement 2026 : offres TPE",
  "Vous équipez votre commerce d'un terminal de paiement ? Comparez les offres des solutions d'encaissement (SumUp, Zettle, Flatpay…) et leurs conditions.",
  "/comparatifs/terminaux-paiement.html","comparatif des terminaux de paiement",["terminaux-paiement"]),
 ("vpn","Codes promo VPN 2026 : réductions et abonnements",
  "Les VPN sont parmi les services qui proposent les plus grosses réductions à l'abonnement annuel. Comparez les offres (ExpressVPN, NordVPN, Surfshark…) et les mois offerts.",
  "/comparatifs/vpn.html","comparatif des VPN",["vpn","bloqueur-de-pub"]),
 ("epargne","Codes promo épargne & assurance-vie 2026",
  "Assurance-vie, gestion pilotée, SCPI : retrouvez les avantages de souscription (souvent 0 % de frais d'entrée plutôt qu'un code) des acteurs de l'épargne en ligne (Linxea, Nalo, Yomoni…).",
  "/comparatifs/assurance-vie.html","comparatif assurance-vie",["assurance-vie","epargne-pilotee","per-retraite"]),
 ("assurance","Codes promo assurance 2026 : auto, santé, animaux",
  "Les assureurs en ligne proposent des offres de bienvenue et des réductions. Retrouvez les promotions vérifiées (assurance animaux, auto, habitation…) et nos comparatifs.",
  "/comparatifs/assurance-animaux.html","comparatif assurance animaux",["assurance-animaux","assurance-auto","mutuelle-sante"]),
 ("ecommerce","Codes promo création de site e-commerce 2026",
  "Lancer une boutique en ligne avec un essai gratuit ou une offre de lancement : comparez Shopify et ses alternatives pour créer votre site e-commerce.",
  "/comparatifs/creer-boutique-en-ligne.html","comparatif création de boutique en ligne",["creer-boutique-en-ligne","ecommerce"]),
 ("hebergement","Codes promo hébergement web 2026 : les meilleures offres",
  "L'hébergement web est l'un des secteurs où les prix d'appel sont les plus agressifs. Retrouvez les offres vérifiées (IONOS, Hostinger, OVHcloud, o2switch…) pour héberger votre site moins cher.",
  "/comparatifs/hebergement-web.html","comparatif des hébergeurs web",["hebergement-web"]),
]

def build(slug,h1,intro,comp,complab,sources):
    members=[s for s in members_from(sources) if s not in noindex or s in AFF]
    # priorité aux affiliés en tête
    members=sorted(members,key=lambda s:(s not in AFF, name_of(s).lower()))
    url=f"https://selectum.fr/code-promo-{slug}.html"
    cards=""
    for s in members:
        nm=html.escape(name_of(s))
        logo=f'<img src="/assets/logos/{s}.png" alt="" width="104" height="60" loading="lazy" style="height:22px;max-width:74px;object-fit:contain;vertical-align:middle;margin-right:8px;">' if os.path.exists(f"assets/logos/{s}.png") else ""
        badge=' <span style="color:#16a34a;font-size:.7rem;font-weight:700;">★</span>' if s in AFF else ''
        cards+=f'<a href="/code-promo/{s}.html" class="hub-item">{logo}Code promo {nm}{badge}</a>\n'
    bc=json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":h1,"url":url,"description":intro[:155]},ensure_ascii=False)
    org='{"@context":"https://schema.org","@type":"Organization","name":"Selectum","url":"https://selectum.fr/","logo":"https://selectum.fr/assets/selectum-logo.png"}'
    page=f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(h1)} | Selectum</title><meta name="description" content="{html.escape(intro[:155])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{html.escape(h1)}"><meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<script type="application/ld+json">{bc}</script>
<script type="application/ld+json">{org}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="{comp}" class="btn-primary">{html.escape(complab.capitalize())} →</a></div>
</div></div></header>
<div class="hero" style="padding:52px 0 36px;"><div class="container"><div class="hero-content"><h1>{html.escape(h1)}</h1></div></div></div>
<div class="container-article"><div class="article-body" style="max-width:920px;margin:0 auto;">
<div class="intro-box"><p>{html.escape(intro)}</p></div>
<p style="color:var(--gray-600);">Les offres ci-dessous sont vérifiées et mises à jour régulièrement (dernière vérification : {D}). Le ★ signale nos partenaires avec offre suivie de près.</p>
<h2>Toutes les offres {html.escape(slug.replace('-',' '))}</h2>
<div class="hub-grid">{cards}</div>
<div class="highlight-box"><p>💡 Pour choisir, consultez aussi notre <a href="{comp}">{html.escape(complab)}</a> et tous nos <a href="/code-promo.html">codes promo</a>.</p></div>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/code-promo.html" style="color:var(--gray-500)">Codes promo</a> · <a href="/methodologie.html" style="color:var(--gray-500)">Méthodologie</a></p>
</div></div></footer></body></html>'''
    open(f"code-promo-{slug}.html","w",encoding="utf-8").write(page)
    return len(members)

tot=0
for h in HUBS:
    n=build(*h); print(f"code-promo-{h[0]}.html : {n} offres"); tot+=n
print("hubs catégorie créés:",len(HUBS))
