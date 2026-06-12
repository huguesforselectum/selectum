#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconstruit code-promo.html et parrainage.html : toutes les pages, groupées par catégorie."""
import os, re, glob, html

# verticales 1parrainage
src=open("tools/gen_1parrainage.py").read()
ns={}; exec(src.split("def faq_ld(")[0], ns)
VERT_OF={b[0]:b[3] for b in ns["BRANDS"]}

V2CAT={"neobank":"Banque & néobanque","pro-bank":"Compte pro & paiement","paiement":"Compte pro & paiement",
"compta":"Compte pro & paiement","transfert":"Compte pro & paiement","crypto":"Bourse & crypto","bourse":"Bourse & crypto",
"epargne":"Épargne & investissement","p2p":"Épargne & investissement","assurance":"Assurance","assurance-animaux":"Assurance",
"energie":"Énergie & maison","solaire":"Énergie & maison","maison":"Énergie & maison","telecom":"Télécom & internet",
"esim":"Télécom & internet","vpn":"Tech, VPN & web","saas":"Tech, VPN & web","shopping":"Shopping, food & divers",
"jeux":"Shopping, food & divers","streaming":"Shopping, food & divers","food":"Shopping, food & divers",
"sante":"Shopping, food & divers","services":"Shopping, food & divers"}

COMP2CAT={"banque-en-ligne":"Banque & néobanque","cartes-famille":"Banque & néobanque","comptes-pro":"Compte pro & paiement",
"terminaux-paiement":"Compte pro & paiement","transfert-argent":"Compte pro & paiement","change-multidevises":"Compte pro & paiement",
"logiciels-comptabilite":"Compte pro & paiement","facturation":"Compte pro & paiement","trading-bourse":"Bourse & crypto",
"crypto":"Bourse & crypto","assurance-vie":"Épargne & investissement","epargne-pilotee":"Épargne & investissement",
"per-retraite":"Épargne & investissement","crowdlending-p2p":"Épargne & investissement","mutuelle-sante":"Assurance",
"assurance-auto":"Assurance","assurance-habitation":"Assurance","assurance-emprunteur":"Assurance","assurance-animaux":"Assurance",
"credit-conso":"Crédit","rachat-credit":"Crédit","courtage-immobilier":"Crédit","vpn":"Tech, VPN & web",
"hebergement-web":"Tech, VPN & web","bloqueur-de-pub":"Tech, VPN & web","formation":"Tech, VPN & web","logiciels-crm":"Tech, VPN & web",
"creer-boutique-en-ligne":"Tech, VPN & web","ecommerce":"Tech, VPN & web","fournisseur-energie":"Énergie & maison",
"kit-solaire-autoconsommation":"Énergie & maison","forfait-mobile":"Télécom & internet","esim-voyage":"Télécom & internet",
"box-internet":"Télécom & internet"}

ORDER=["Banque & néobanque","Compte pro & paiement","Bourse & crypto","Épargne & investissement","Assurance","Crédit","Énergie & maison","Télécom & internet","Tech, VPN & web","Shopping, food & divers"]

# index comparatif par /go/<slug>
comp_of={}
for f in glob.glob("comparatifs/*.html"):
    base=os.path.basename(f)[:-5]
    if "-vs-" in base or base.startswith("alternative-"): continue
    for m in re.finditer(r'/go/([a-z0-9-]+)', open(f).read()):
        comp_of.setdefault(m.group(1), base)

def category(slug):
    if slug in VERT_OF: return V2CAT.get(VERT_OF[slug],"Shopping, food & divers")
    c=comp_of.get(slug)
    if c and c in COMP2CAT: return COMP2CAT[c]
    return "Shopping, food & divers"

def name_of(kind,slug):
    t=open(f"{kind}/{slug}.html",encoding="utf-8").read()
    m=re.search(r'<h1>(?:Code promo|Parrainage)\s+(.+?)(?:\s+2026|\s*:|\s*</h1>)', t)
    if m: return m.group(1).strip()
    return slug.replace("-"," ").title()

def build(kind, htitle, hdesc, word):
    slugs=sorted(os.path.basename(f)[:-5] for f in glob.glob(f"{kind}/*.html"))
    groups={c:[] for c in ORDER}
    for s in slugs:
        groups.setdefault(category(s),[]).append(s)
    total=len(slugs)
    sections=[]
    for cat in ORDER:
        items=sorted(groups.get(cat,[]), key=lambda s:name_of(kind,s).lower())
        if not items: continue
        cards=""
        for s in items:
            nm=html.escape(name_of(kind,s))
            logo=f'<img src="/assets/logos/{s}.png" alt="" width="104" height="60" loading="lazy" style="height:20px;max-width:70px;object-fit:contain;vertical-align:middle;margin-right:8px;">' if os.path.exists(f"assets/logos/{s}.png") else ""
            cards+=f'<a href="/{kind}/{s}.html" class="hub-item">{logo}{word} {nm}</a>\n'
        anchor=cat.lower().replace(" & ","-").replace(" ","-").replace(",","")
        sections.append(f'<section class="section" style="padding-top:32px;"><div class="container"><div class="section-title" style="text-align:left;"><h2 id="{anchor}">{word} {html.escape(cat.lower())}</h2></div><div class="hub-grid">{cards}</div></div></section>')
    intro_links=" · ".join(f'<a href="#{c.lower().replace(" & ","-").replace(" ","-").replace(",","")}">{html.escape(c)}</a>' for c in ORDER if groups.get(c))
    head=f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(htitle)}</title><meta name="description" content="{html.escape(hdesc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="https://selectum.fr/{kind}.html"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{html.escape(htitle)}"><meta property="og:description" content="{html.escape(hdesc)}">
<meta property="og:url" content="https://selectum.fr/{kind}.html"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"CollectionPage","name":"{html.escape(htitle)}","url":"https://selectum.fr/{kind}.html","description":"{html.escape(hdesc)}"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Selectum","url":"https://selectum.fr/","logo":"https://selectum.fr/assets/selectum-logo.png"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"Selectum","url":"https://selectum.fr/","inLanguage":"fr-FR"}}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/autres-comparatifs.html" class="btn-primary">Tous les comparatifs →</a></div>
</div></div></header>
<div class="hero" style="padding:56px 0 40px;"><div class="container"><div class="hero-content"><h1>{html.escape(htitle.split(" | ")[0])}</h1><p>{html.escape(word_intro)}</p></div></div></div>
<div class="container" style="padding:24px 20px 0;"><p style="color:var(--gray-600);">{word_para} <strong>{total} marques</strong> couvertes. Accès rapide : {intro_links}.</p></div>
'''
    foot='''<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a> · <a href="/methodologie.html" style="color:var(--gray-500)">Méthodologie</a></p>
</div></div></footer></body></html>'''
    open(f"{kind}.html","w",encoding="utf-8").write(head+"\n".join(sections)+foot)
    return total

word_intro="Toutes les offres de bienvenue et réductions du moment, vérifiées et classées par catégorie."
word_para="Retrouvez le code promo de chaque marque, vérifié ce mois-ci par notre équipe —"
t1=build("code-promo","Code promo 2026 : toutes les offres vérifiées par catégorie | Selectum",
 "Tous les codes promo et offres de bienvenue 2026, vérifiés et classés par catégorie : banque, crypto, bourse, assurance, énergie, télécom, pro…","Code promo")
word_intro="Tous les programmes de parrainage et offres de bienvenue du moment, classés par catégorie."
word_para="Retrouvez le parrainage de chaque marque, vérifié ce mois-ci par notre équipe —"
t2=build("parrainage","Parrainage 2026 : tous les programmes et primes par catégorie | Selectum",
 "Tous les programmes de parrainage 2026 et primes de bienvenue, classés par catégorie : banque, crypto, bourse, assurance, énergie, télécom, pro…","Parrainage")
print(f"code-promo.html: {t1} marques | parrainage.html: {t2} marques")
