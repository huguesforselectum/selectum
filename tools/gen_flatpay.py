#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lot FlatPay : pages 'flatpay vs X' + articles dédiés (données réelles)."""
import html, os, json
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'

FP=dict(slug="flatpay",name="Flatpay",go="/go/flatpay",rating="4.6/5",score="9,2",price="1,29%",
  desc="TPE et caisse à <strong>commission fixe de 1,29%</strong>, même taux pour toutes les cartes, sans abonnement.",
  pts=["Commission fixe 1,29% (TPE)","Même taux toutes cartes (même Amex)","TPE offert dès 2 000 €/mois encaissés","Accompagnement physique à l'installation"])

COMP={
 "sumup":dict(name="SumUp",rating="4.4/5",score="8,8",price="1,75%",
   desc="Le TPE mobile le plus populaire en France, sans engagement et sans abonnement.",
   pts=["Sans engagement","Achat du TPE (dès ~29€)","Pas de volume minimum","Idéal petits volumes"]),
 "zettle":dict(name="Zettle (PayPal)",rating="4.3/5",score="8,6",price="1,75%",
   desc="Le terminal de PayPal, simple et sans engagement, intégré à l'écosystème PayPal.",
   pts=["Sans engagement","Lié à PayPal","Achat du TPE","Bon pour démarrer"]),
 "mypos":dict(name="myPOS",rating="4.2/5",score="8,4",price="dès 1,10%",
   desc="TPE avec compte et IBAN professionnel intégrés, encaissement instantané, sans engagement.",
   pts=["IBAN pro inclus","Fonds disponibles en instantané","Sans engagement","Achat du terminal"]),
 "square":dict(name="Square",rating="4.3/5",score="8,6",price="1,65%",
   desc="Écosystème complet TPE + caisse + outils de gestion, sans engagement.",
   pts=["Écosystème caisse complet","Sans engagement","Logiciels gratuits","Achat du TPE"]),
 "stripe":dict(name="Stripe Terminal",rating="4.4/5",score="8,8",price="1,4% + 0,25€",
   desc="Terminal pensé pour les développeurs et les acteurs du e-commerce omnicanal.",
   pts=["Idéal online + magasin","Très flexible (API)","Sans engagement","Plutôt pour les techs"]),
 "payplug":dict(name="PayPlug",rating="4.1/5",score="8,2",price="sur devis",
   desc="Solution française (groupe BPCE) combinant paiement en ligne et terminal en magasin.",
   pts=["100% français (BPCE)","En ligne + en magasin","Support FR","Tarif sur devis"]),
 "viva-wallet":dict(name="Viva Wallet",rating="4.2/5",score="8,4",price="dès 1,20%",
   desc="Néobanque professionnelle européenne avec Tap to Pay sur smartphone et compte intégré.",
   pts=["Tap to Pay (sans TPE)","Compte pro inclus","Européen","Tarifs dégressifs"]),
}

def headhtml(title,desc,url,extra=''):
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
<meta name="twitter:card" content="summary">{extra}
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/avis/flatpay.html" class="btn-primary">Avis Flatpay →</a></div>
</div></div></header>'''

def footer():
    return '''<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

def faq_ld(qa):
    return '\n<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]},ensure_ascii=False)+'</script>'

def col(d,slug,winner,go=None):
    badge='<span class="best-badge">Notre choix</span>' if winner else ''
    pts="".join(f"<li>{html.escape(p)}</li>" for p in d['pts'])
    link=go or f"/go/{slug}"
    return f'''<div class="vs-col{' vs-win' if winner else ''}">
      <div class="vs-logo"><img src="/assets/logos/{slug}.png" alt="{html.escape(d['name'])}"></div>
      <h2>{html.escape(d['name'])} {badge}</h2>
      <div class="tp-score" style="max-width:150px;margin:6px auto 10px;"><b>{d['score']}</b><span>/10</span><small>Note Selectum</small></div>
      <ul class="tp-checklist" style="grid-template-columns:1fr;text-align:left;max-width:230px;margin:0 auto 12px;">{pts}</ul>
      <div class="vs-price">{html.escape(d['price'])}<span style="display:block;font-size:.7rem;color:var(--gray-500);font-weight:600;">par transaction</span></div>
      <a href="{link}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir {html.escape(d['name'].split(' (')[0])} →</a>
    </div>'''

def vs_page(slug,c):
    cn=html.escape(c['name']); url=f"https://selectum.fr/comparatifs/flatpay-vs-{slug}.html"
    title=f"Flatpay ou {c['name']} ? Comparatif TPE 2026 | Selectum"
    desc=f"Flatpay vs {c['name']} : commission, engagement, terminal, services. Comparatif 2026 pour choisir le meilleur terminal de paiement pour votre commerce."
    qa=[(f"Flatpay ou {c['name']} : lequel choisir ?",f"Flatpay applique une commission fixe de 1,29% (toutes cartes) et offre le terminal dès 2 000 €/mois encaissés, mais impose un engagement de 36 mois. {c['name']} ({c['price']}) est généralement sans engagement. Le bon choix dépend de votre volume et de votre besoin de flexibilité."),
        (f"Flatpay est-il moins cher que {c['name']} ?",f"Sur la commission, Flatpay (1,29%) est souvent plus avantageux que {c['name']} ({c['price']}). En revanche, Flatpay demande un engagement de 36 mois, là où {c['name']} est sans engagement."),
        ("Y a-t-il un engagement ?",f"Flatpay impose un engagement de 36 mois. {c['name']} fonctionne en général sans engagement, avec achat du terminal.")]
    qatxt=[(html.escape(q),html.escape(a)) for q,a in qa]
    return f'''{headhtml(title,desc,url,faq_ld(qatxt))}
<div class="article-header"><div class="container-article">
<div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/comparatifs/terminaux-paiement.html">Terminaux de paiement</a><span>/</span>Flatpay vs {cn}</div>
<h1>Flatpay ou {cn} ? Le comparatif TPE 2026</h1>
<p class="updated">🗓️ Mis à jour le 11 juin 2026 — Analysé par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:920px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
<p>Vous hésitez entre <strong>Flatpay</strong> et <strong>{cn}</strong> pour encaisser les paiements de votre commerce ? Voici notre comparatif en face-à-face.</p>
<div class="vs-grid">{col(FP,'flatpay',True)}<div class="vs-or">VS</div>{col(c,slug,False)}</div>
<h2>Flatpay vs {cn} : le verdict</h2>
<p><strong>Flatpay</strong> se démarque par sa <strong>commission fixe de 1,29%</strong> identique pour toutes les cartes (y compris American Express et cartes hors zone euro), un terminal offert au-delà de 2 000 €/mois d'encaissement, et un accompagnement humain à l'installation. Son inconvénient principal : un <strong>engagement de 36 mois</strong>.</p>
<p><strong>{cn}</strong> ({c['price']}) mise plutôt sur la flexibilité : {html.escape(c['desc'])}</p>
<div class="comparison-table-wrap"><table class="comparison-table">
<thead><tr><th>Critère</th><th>Flatpay</th><th>{cn}</th></tr></thead>
<tbody>
<tr><td>Commission</td><td><strong>1,29%</strong> (fixe)</td><td>{html.escape(c['price'])}</td></tr>
<tr><td>Abonnement</td><td>Aucun</td><td>Variable</td></tr>
<tr><td>Engagement</td><td>36 mois</td><td>Généralement aucun</td></tr>
<tr><td>Terminal</td><td>Offert dès 2 000 €/mois</td><td>À l'achat</td></tr>
<tr><td>Idéal pour</td><td>Volume régulier &gt; 2 000 €/mois</td><td>Petits volumes / flexibilité</td></tr>
</tbody></table></div>
<div class="highlight-box"><p>💡 <strong>Notre conseil :</strong> si vous encaissez régulièrement plus de 2 000 €/mois et acceptez de vous engager, Flatpay est le plus rentable grâce à sa commission fixe basse. Pour un commerce saisonnier ou un faible volume sans engagement, {cn} est plus adapté.</p></div>
<div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qatxt)+f'''</div>
<p style="margin-top:22px;">Pour aller plus loin : <a href="/avis/flatpay.html">Avis Flatpay</a> · <a href="/comparatifs/terminaux-paiement.html">Comparatif des terminaux de paiement</a></p>
</div></div>{footer()}'''

n=0
for slug,c in COMP.items():
    if not os.path.exists(f"assets/logos/{slug}.png"): print("skip (no logo)",slug); continue
    open(f"comparatifs/flatpay-vs-{slug}.html","w").write(vs_page(slug,c)); n+=1
print("pages vs Flatpay générées:",n)
