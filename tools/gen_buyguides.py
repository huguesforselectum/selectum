#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère guide-achat/<slug>.html : guide d'achat 'comment choisir <catégorie>' par comparatif."""
import glob, os, re, html, json
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
LABELS={
 "banque-en-ligne":"une banque en ligne","crypto":"une plateforme crypto","trading-bourse":"un courtier en bourse",
 "hebergement-web":"un hébergeur web","vpn":"un VPN","assurance-auto":"une assurance auto",
 "assurance-habitation":"une assurance habitation","mutuelle-sante":"une mutuelle santé","assurance-vie":"une assurance-vie",
 "logiciels-comptabilite":"un logiciel de comptabilité","logiciels-crm":"un logiciel CRM","facturation":"un logiciel de facturation",
 "box-internet":"une box internet","box-abonnement":"une box par abonnement","credit-conso":"un crédit conso",
 "rachat-credit":"un rachat de crédit","courtage-immobilier":"un courtier immobilier","assurance-emprunteur":"une assurance emprunteur",
 "comptes-pro":"un compte pro","cartes-famille":"une carte pour ado/famille","transfert-argent":"un service de transfert d'argent",
 "change-multidevises":"un compte multi-devises","epargne-pilotee":"une épargne pilotée","per-retraite":"un PER",
 "formation":"une plateforme de formation","terminaux-paiement":"un terminal de paiement"}
RISK={"crypto","trading-bourse","assurance-vie","epargne-pilotee","per-retraite"}
CRIT={
 "default":["Les frais et tarifs (le critère n°1)","La qualité du service client et le support en français","La simplicité d'utilisation (app, interface)","La réputation et les avis clients","Les conditions et la flexibilité (sans engagement, résiliation)"],
}

def topbrands(slug):
    s=open(f"comparatifs/{slug}.html").read()
    out=[]
    for c in re.findall(r'<div class="offer-card.*?(?:</a>|offer-cta">.*?</div>)\s*</div>', s, re.S):
        lm=re.search(r'/assets/logos/([a-z0-9-]+)\.png', c); nm=re.search(r'offer-name">([^<]+)<', c)
        if lm and nm:
            name=re.split(r'\s+[—–-]\s+', nm.group(1))[0].split(' (')[0].strip()
            a=lm.group(1)
            if not any(x[0]==a for x in out): out.append((a,name))
    return out[:3]

def page(slug,cl):
    url=f"https://selectum.fr/guide-achat/{slug}.html"
    risk=" Investir comporte un risque de perte en capital." if slug in RISK else ""
    catword=cl
    title=f"Comment choisir {cl} en 2026 ? Guide d'achat | Selectum"
    desc=f"Comment choisir {cl} en 2026 : les critères à comparer, les pièges à éviter et notre sélection. Guide d'achat indépendant Selectum."
    crit="".join(f"<li>{html.escape(c)}</li>" for c in CRIT["default"])
    tops=topbrands(slug)
    topli="".join(f'<li><a href="/avis/{a}.html">{html.escape(n)}</a> — voir notre avis</li>' for a,n in tops if os.path.exists(f"avis/{a}.html"))
    qa=[(f"Comment bien choisir {cl} ?",f"Comparez d'abord les frais, puis le service client, la simplicité d'usage et la réputation. Notre comparatif classe les meilleures options selon ces critères."),
        (f"Quel est le meilleur choix en 2026 ?", "Notre n°1 actuel figure en tête de notre comparatif. Le meilleur choix dépend toutefois de votre profil et de vos besoins."),
        (f"Peut-on changer facilement ?","Oui, la plupart des offres sont sans engagement ou résiliables. Pensez à vérifier les conditions avant de souscrire.")]
    qatxt=[(html.escape(q),html.escape(a)) for q,a in qa]
    ld_faq=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]},ensure_ascii=False)
    ld_art=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-11","dateModified":"2026-06-11","mainEntityOfPage":url},ensure_ascii=False)
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
<script type="application/ld+json">{ld_art}</script>
<script type="application/ld+json">{ld_faq}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/comparatifs/{slug}.html" class="btn-primary">Voir le comparatif →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
<div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span>Guide d'achat<span>/</span>Comment choisir {html.escape(cl)}</div>
<h1>Comment choisir {html.escape(cl)} en 2026 ?</h1>
<p class="updated">🗓️ Mis à jour le 11 juin 2026</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
<div class="intro-box"><p>Choisir {html.escape(cl)} peut vite devenir compliqué tant les offres se ressemblent. Ce guide vous donne les <strong>critères qui comptent vraiment</strong>, les pièges à éviter, et vous oriente vers notre sélection.{risk}</p></div>
<h2 id="criteres">Les critères à comparer en priorité</h2>
<ul>{crit}</ul>
<h2 id="pieges">Les pièges à éviter</h2>
<p>Méfiez-vous des prix d'appel trop beaux pour être vrais (vérifiez le tarif après la 1ʳᵉ année), des frais cachés (tenue de compte, retrait, change), et des engagements longue durée difficiles à résilier. Lisez toujours les conditions avant de signer.</p>
<h2 id="selection">Notre sélection</h2>
<p>Après comparaison, voici les options qui ressortent en tête :</p>
<ul>{topli or '<li>Voir notre classement complet ci-dessous.</li>'}</ul>
<div class="highlight-box"><p>👉 Pour le classement détaillé avec notes, frais et offres, consultez notre <a href="/comparatifs/{slug}.html"><strong>comparatif complet</strong></a>.</p></div>
<div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qatxt)+f'''</div>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

n=0
for slug,cl in LABELS.items():
    if os.path.exists(f"comparatifs/{slug}.html"):
        open(f"guide-achat/{slug}.html","w").write(page(slug,cl)); n+=1
print("guides d'achat générés:",n)
