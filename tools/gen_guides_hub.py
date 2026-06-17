#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hub /guides.html par categorie + cross-linking 'Guides lies' entre guides + liens home/footer."""
import glob, re, os, html, random
random.seed(42)

COMP2CAT={}
for b in ["crypto","crypto-debutant","crypto-frais-bas","acheter-bitcoin"]: COMP2CAT[b]="Crypto"
COMP2CAT["hebergement-web"]="Hébergement & web"; COMP2CAT["creer-boutique-en-ligne"]="Hébergement & web"; COMP2CAT["ecommerce"]="Hébergement & web"
for b in ["banque-en-ligne","cartes-famille"]: COMP2CAT[b]="Banque"
COMP2CAT["comptes-pro"]="Compte pro & indépendants"; COMP2CAT["facturation"]="Compte pro & indépendants"; COMP2CAT["logiciels-comptabilite"]="Compte pro & indépendants"
COMP2CAT["trading-bourse"]="Bourse"; COMP2CAT["courtier-etf"]="Bourse"
for b in ["assurance-vie","epargne-pilotee","per-retraite","crowdlending-p2p"]: COMP2CAT[b]="Épargne & investissement"
for b in ["assurance-animaux","mutuelle-sante","assurance-auto","assurance-habitation","assurance-emprunteur"]: COMP2CAT[b]="Assurance"
for b in ["credit-conso","rachat-credit","courtage-immobilier"]: COMP2CAT[b]="Crédit"
for b in ["vpn","bloqueur-de-pub"]: COMP2CAT[b]="Tech, VPN & sécurité"
for b in ["fournisseur-energie","kit-solaire-autoconsommation"]: COMP2CAT[b]="Énergie"
for b in ["transfert-argent","change-multidevises"]: COMP2CAT[b]="Transfert d'argent"
ORDER=["Crypto","Bourse","Banque","Compte pro & indépendants","Épargne & investissement","Assurance","Crédit","Hébergement & web","Énergie","Transfert d'argent","Tech, VPN & sécurité","Autres guides"]

def title_of(f):
    t=open(f,encoding="utf-8").read()
    m=re.search(r'<h1>(.+?)</h1>',t); return (re.sub(r'\s*\|\s*Selectum.*','',m.group(1)).strip() if m else os.path.basename(f)[:-5])
def cat_of(f):
    t=open(f,encoding="utf-8").read()
    for m in re.finditer(r'/comparatifs/([a-z0-9-]+)\.html',t):
        if m.group(1) in COMP2CAT: return COMP2CAT[m.group(1)]
    return "Autres guides"

guides=sorted(glob.glob("guides/*.html"))
info={f:(title_of(f),cat_of(f)) for f in guides}
bycat={}
for f in guides: bycat.setdefault(info[f][1],[]).append(f)

# 1) cross-linking 'Guides liés' dans chaque guide
inj=0
for f in guides:
    t=open(f,encoding="utf-8").read()
    if 'Guides liés' in t or '<footer' not in t: continue
    cat=info[f][1]; sibs=[g for g in bycat[cat] if g!=f]
    if len(sibs)<2: continue
    pick=random.sample(sibs, min(4,len(sibs)))
    chips="".join(f'<a href="/{g}" class="rel-chip">{html.escape(info[g][0][:54])} →</a>' for g in pick)
    block=f'<div class="container-article" style="max-width:880px;margin:0 auto;"><div class="rel-links"><h2>📚 Guides liés</h2><div class="rel-list">{chips}</div></div></div>\n'
    t=t.replace('<footer', block+'<footer',1)
    open(f,"w",encoding="utf-8").write(t); inj+=1
print("cross-linking 'Guides liés' injecté:",inj,"guides")

# 2) hub /guides.html
sections=""
for cat in ORDER+[c for c in bycat if c not in ORDER]:
    if cat not in bycat: continue
    items=sorted(bycat[cat], key=lambda f:info[f][0].lower())
    cards="".join(f'<a href="/{f}" class="hub-item">{html.escape(info[f][0])}</a>\n' for f in items)
    anchor=re.sub(r'[^a-z]+','-',cat.lower()).strip('-')
    sections+=f'<section class="section" style="padding:28px 0;"><div class="container"><div class="section-title" style="text-align:left;"><h2 id="{anchor}">{html.escape(cat)} <span style="color:var(--gray-400);font-weight:500;font-size:1rem;">({len(items)})</span></h2></div><div class="hub-grid">{cards}</div></div></section>\n'
nav=" · ".join(f'<a href="#{re.sub(chr(91)+"^a-z"+chr(93)+"+","-",c.lower()).strip("-")}">{html.escape(c)}</a>' for c in ORDER if c in bycat)
hub=f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Guides Selectum : tous nos guides finance, crypto, banque & assurance</title><meta name="description" content="Tous les guides Selectum : comment investir, choisir une banque, acheter des cryptos, assurer son véhicule, réduire ses impôts… {len(guides)} guides pratiques et indépendants.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="https://selectum.fr/guides.html"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Selectum"><meta property="og:title" content="Guides Selectum"><meta property="og:url" content="https://selectum.fr/guides.html"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"CollectionPage","name":"Guides Selectum","url":"https://selectum.fr/guides.html"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Selectum","url":"https://selectum.fr/","logo":"https://selectum.fr/assets/selectum-logo.png"}}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/autres-comparatifs.html" class="btn-primary">Comparatifs →</a></div>
</div></div></header>
<div class="hero" style="padding:52px 0 36px;"><div class="container"><div class="hero-content"><h1>Tous nos guides</h1><p>{len(guides)} guides pratiques et indépendants pour faire les bons choix : banque, bourse, crypto, assurance, crédit, épargne…</p></div></div></div>
<div class="container" style="padding:18px 20px 0;"><p style="color:var(--gray-600);">Accès rapide : {nav}.</p></div>
{sections}
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/code-promo.html" style="color:var(--gray-500)">Codes promo</a> · <a href="/etudes.html" style="color:var(--gray-500)">Études</a></p>
</div></div></footer></body></html>'''
open("guides.html","w",encoding="utf-8").write(hub)
print("hub /guides.html créé :", len(guides),"guides en", len([c for c in bycat]),"catégories")

# 3) lien /guides.html dans footer sitewide + home
add=' · <a href="/guides.html" style="color:var(--gray-500)">Guides</a>'
pat=re.compile(r'(<a href="(?:\.\./)?politique-confidentialite\.html"[^>]*>Confidentialité</a>(?:[^<]*<a href="/code-promo[^"]*"[^>]*>Codes promo</a>)?)')
n=0
for f in glob.glob("**/*.html",recursive=True):
    if f.startswith("node_modules") or f=="guides.html": continue
    t=open(f,encoding="utf-8").read()
    if '/guides.html"' in t: continue
    if '>Codes promo</a>' in t:
        t2=t.replace('>Codes promo</a>', '>Codes promo</a>'+add,1)
    elif 'politique-confidentialite.html"' in t:
        t2=re.sub(r'(>Confidentialité</a>)', r'\1'+add, t, count=1)
    else: continue
    if t2!=t: open(f,"w",encoding="utf-8").write(t2); n+=1
print("lien /guides.html ajouté au footer:",n,"pages")
