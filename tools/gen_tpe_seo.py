#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comparatifs TPE déclinés SEO (moins cher, gratuit, sans abonnement, restaurant...)."""
import html, os, json
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'

ACT={
 "flatpay":dict(name="Flatpay",score="9,2",price="1,29%",go="/go/flatpay",dom="flatpay.com",
   desc="TPE et caisse à commission fixe 1,29%, même taux toutes cartes, sans abonnement.",
   pts=["Commission fixe 1,29%","TPE offert dès 2 000 €/mois","Toutes cartes, même taux","Sans abonnement"]),
 "sumup":dict(name="SumUp",score="8,8",price="1,75%",go="/go/sumup",dom="sumup.fr",
   desc="Le TPE mobile le plus populaire, sans engagement ni abonnement.",
   pts=["Sans engagement","TPE dès ~29 €","Sans abonnement","Idéal petits volumes"]),
 "zettle":dict(name="Zettle (PayPal)",score="8,6",price="1,75%",go="/go/zettle",dom="zettle.com",
   desc="Le terminal de PayPal, simple et sans engagement.",
   pts=["Sans engagement","Écosystème PayPal","Application simple","Achat du TPE"]),
 "mypos":dict(name="myPOS",score="8,4",price="dès 1,10%",go="/go/mypos",dom="mypos.com",
   desc="TPE avec compte et IBAN pro intégrés, fonds disponibles instantanément.",
   pts=["IBAN pro inclus","Fonds en instantané","Sans engagement","Carte business"]),
 "square":dict(name="Square",score="8,6",price="1,65%",go="/go/square",dom="squareup.com",
   desc="Écosystème complet TPE + caisse + gestion, sans engagement.",
   pts=["Caisse complète","Logiciels gratuits","Sans engagement","Évolutif"]),
 "viva-wallet":dict(name="Viva Wallet",score="8,4",price="dès 1,20%",go="/go/viva-wallet",dom="vivawallet.com",
   desc="Néobanque pro européenne avec Tap to Pay sur smartphone.",
   pts=["Tap to Pay sans TPE","Compte pro inclus","Tarifs dégressifs","Européen"]),
 "payplug":dict(name="PayPlug",score="8,2",price="sur devis",go="/go/payplug",dom="payplug.com",
   desc="Solution 100% française (groupe BPCE), en ligne et en magasin.",
   pts=["100% français (BPCE)","En ligne + magasin","Support FR","Anti-fraude avancé"]),
 "stripe":dict(name="Stripe Terminal",score="8,8",price="1,4% + 0,25€",go="/go/stripe",dom="stripe.com",
   desc="Terminal pour e-commerçants et acteurs omnicanaux, très flexible.",
   pts=["Online + magasin","API flexible","Sans engagement","Pour profils tech"]),
}

PAGES=[
 ("meilleur-tpe-pas-cher","Meilleur TPE pas cher 2026 : le top 4 des terminaux les moins chers",
  "Quel est le TPE le moins cher en 2026 ? Notre top 4 des terminaux de paiement au meilleur coût : commission, abonnement, terminal. Flatpay, SumUp, Viva, myPOS comparés.",
  "Meilleur TPE pas cher : le top 4 en 2026",
  "Entre commission, abonnement et prix du terminal, le « moins cher » dépend de votre volume. Voici notre classement des TPE au meilleur coût réel.",
  ["flatpay","sumup","viva-wallet","mypos"]),
 ("tpe-gratuit","TPE gratuit 2026 : top 4 des terminaux sans frais fixes",
  "TPE gratuit en 2026 : quels terminaux sans abonnement ni frais fixes ? Notre top 4 (Flatpay terminal offert, SumUp, Zettle, Viva) et la vérité sur le « gratuit ».",
  "TPE gratuit : le top 4 en 2026",
  "Aucun TPE n'est 100% gratuit (il reste une commission), mais certains suppriment l'abonnement et offrent le terminal. Voici les meilleures options « sans frais fixes ».",
  ["flatpay","sumup","zettle","viva-wallet"]),
 ("tpe-sans-abonnement","TPE sans abonnement 2026 : top 4 des terminaux sans frais mensuels",
  "Meilleur TPE sans abonnement en 2026 : payez uniquement à la transaction. Top 4 (Flatpay, SumUp, Zettle, Square) comparés sur la commission et les conditions.",
  "TPE sans abonnement : le top 4 en 2026",
  "Pas de frais mensuels fixes : vous ne payez qu'une commission sur vos encaissements. Voici les meilleurs TPE sans abonnement.",
  ["flatpay","sumup","zettle","square"]),
 ("tpe-sans-engagement","TPE sans engagement 2026 : top 4 des terminaux libres",
  "Meilleur TPE sans engagement en 2026 : résiliez quand vous voulez. Top 4 (SumUp, Zettle, myPOS, Square). Comparatif des terminaux les plus flexibles.",
  "TPE sans engagement : le top 4 en 2026",
  "Vous voulez pouvoir arrêter quand vous voulez ? Ces TPE fonctionnent sans engagement de durée (à la différence de Flatpay, engagé sur 36 mois).",
  ["sumup","zettle","mypos","square"]),
 ("meilleur-tpe-restaurant","Meilleur TPE pour restaurant 2026 : top 4",
  "Quel TPE pour un restaurant en 2026 ? Top 4 des terminaux et caisses adaptés à la restauration : pourboire, partage d'addition, caisse. Flatpay, Square, myPOS, SumUp.",
  "Meilleur TPE pour restaurant : le top 4 en 2026",
  "Restauration : pourboire, partage d'addition, caisse connectée et fiabilité comptent. Voici les meilleurs TPE et caisses pour restaurants.",
  ["flatpay","square","mypos","sumup"]),
 ("meilleur-tpe-mobile","Meilleur TPE mobile 2026 : top 4 des terminaux portables",
  "Meilleur TPE mobile / portable en 2026 : encaissez partout. Top 4 (SumUp, Viva Tap to Pay, Zettle, Flatpay). Comparatif des terminaux nomades.",
  "Meilleur TPE mobile : le top 4 en 2026",
  "Marchés, food-trucks, livraison, artisans : un TPE portable (ou le paiement sur smartphone) est indispensable. Voici les meilleurs.",
  ["sumup","viva-wallet","zettle","flatpay"]),
 ("meilleur-tpe-auto-entrepreneur","Meilleur TPE auto-entrepreneur 2026 : top 4",
  "Quel TPE pour auto-entrepreneur en 2026 ? Top 4 des terminaux simples et économiques pour micro-entreprise. SumUp, Flatpay, Zettle, Viva comparés.",
  "Meilleur TPE pour auto-entrepreneur : le top 4 en 2026",
  "En micro-entreprise, on veut un TPE simple, sans frais fixes et sans paperasse. Voici les meilleurs choix pour auto-entrepreneurs.",
  ["sumup","flatpay","zettle","viva-wallet"]),
 ("meilleur-tpe-francais","Meilleur TPE français 2026 : top 4 avec support en France",
  "Meilleur TPE français ou avec support en France en 2026 : PayPlug (BPCE), Flatpay, SumUp. Top 4 des solutions avec accompagnement local.",
  "Meilleur TPE français : le top 4 en 2026",
  "Pour un interlocuteur en France et un accompagnement local, certaines solutions se démarquent — dont PayPlug, 100% français (groupe BPCE).",
  ["payplug","flatpay","sumup","square"]),
]

def head(title,desc,url,extra):
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<meta name="twitter:card" content="summary">{extra}
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/comparatifs/terminaux-paiement.html" class="btn-primary">Comparatif TPE →</a></div>
</div></div></header>'''

def topcard(slug):
    a=ACT[slug]; avis=f"/avis/{slug}.html" if os.path.exists(f"avis/{slug}.html") else a['go']
    pts="".join(f"<li>{html.escape(p)}</li>" for p in a['pts'])
    return f'''<div class="offer-card top-pick">
        <div class="tp-rank">1</div>
        <div class="tp-logo"><img src="/assets/logos/{slug}.png" alt="{html.escape(a['name'])}" loading="lazy"></div>
        <div class="tp-main"><div class="tp-name">{html.escape(a['name'].split(' (')[0])}</div>
          <div class="tp-tagline">{html.escape(a['desc'])}</div>
          <ul class="tp-checklist">{pts}</ul>
          <a class="tp-more" href="{avis}">En savoir plus →</a></div>
        <div class="tp-side"><div class="tp-score"><b>{a['score']}</b><span>/10</span><small>Note Selectum</small></div>
          <div class="tp-price">{html.escape(a['price'])}</div>
          <a class="btn-green tp-cta" href="{a['go']}" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a>
          <a class="tp-gosite" href="{a['go']}" target="_blank" rel="sponsored nofollow noopener">Aller sur {a['dom']} →</a></div>
      </div>'''

def card(slug,rank):
    a=ACT[slug]
    tags="".join(f'<span class="offer-tag">{html.escape(p)}</span>' for p in a['pts'][:3])
    return f'''<div class="offer-card">
        <div class="offer-rank">{rank}</div>
        <div class="offer-logo brand"><img src="/assets/logos/{slug}.png" alt="{html.escape(a['name'])}" loading="lazy"></div>
        <div class="offer-info"><div class="offer-name">{html.escape(a['name'])}</div>
          <div class="offer-desc">{html.escape(a['desc'])}</div>
          <div class="offer-tags">{tags}</div></div>
        <div class="offer-score-mini"><b>{a['score']}</b><span>/10</span></div>
        <div class="offer-price">{html.escape(a['price'])}<span>par transaction</span></div>
        <a href="{a['go']}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a>
      </div>'''

def page(slug,title,desc,h1,intro,order):
    url=f"https://selectum.fr/comparatifs/{slug}.html"
    rows="".join(f"<tr><td><strong>{html.escape(ACT[s]['name'])}</strong></td><td>{html.escape(ACT[s]['price'])}</td><td>{ACT[s]['score']}/10</td></tr>" for s in order)
    cards=topcard(order[0])+"".join(card(s,i+2) for i,s in enumerate(order[1:]))
    items=[(f"Quel est le meilleur {h1.split(':')[0].strip().lower()} ?",f"Notre n°1 est {ACT[order[0]]['name']}. Le choix dépend de votre volume d'encaissement, de votre besoin de flexibilité et de votre secteur."),
           ("Comment sont classés ces TPE ?","Nous comparons la commission, l'abonnement, l'engagement, le matériel et le service. Le classement reflète le meilleur rapport global pour l'intention de recherche de cette page.")]
    ld_item=json.dumps({"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":ACT[s]['name']} for i,s in enumerate(order)]},ensure_ascii=False)
    ld_faq=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]},ensure_ascii=False)
    extra=f'\n<script type="application/ld+json">{ld_item}</script>\n<script type="application/ld+json">{ld_faq}</script>'
    faqhtml='<div class="faq"><h2>❓ Questions fréquentes</h2>'+''.join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in items)+'</div>'
    return f'''{head(title,desc,url,extra)}
<div class="article-header"><div class="container-article">
<div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/comparatifs/terminaux-paiement.html">Terminaux de paiement</a><span>/</span>{html.escape(h1.split(':')[0].strip())}</div>
<h1>{html.escape(h1)}</h1><p class="updated">🗓️ Mis à jour le 11 juin 2026 — Analysé par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-layout" style="grid-template-columns:1fr 300px;"><main class="article-body">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
<div class="intro-box"><p>{html.escape(intro)}</p></div>
<h2 id="classement">🏆 Notre classement</h2>
<div class="offer-cards">{cards}</div>
<h2 id="tableau">Tableau comparatif</h2>
<div class="comparison-table-wrap"><table class="comparison-table"><thead><tr><th>Solution</th><th>Commission</th><th>Note</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2 id="choisir">Comment choisir ?</h2>
<p>Pour bien choisir, évaluez votre <strong>volume mensuel d'encaissement</strong>, votre besoin de <strong>flexibilité</strong> (engagement ou non), votre <strong>secteur</strong> (restauration, mobilité, boutique) et la <strong>qualité du support</strong>. Les commissions affichées sont les taux standards ; vérifiez les conditions à jour avant de souscrire.</p>
{faqhtml}
<p style="margin-top:20px;">À lire aussi : <a href="/comparatifs/terminaux-paiement.html">comparatif complet des TPE</a> · <a href="/avis/flatpay.html">avis Flatpay</a> · <a href="/guides/flatpay-tarifs.html">tarifs Flatpay</a></p>
</main>
<aside class="sidebar">
<div class="sidebar-cta"><h4>🥇 Notre n°1</h4><p>{html.escape(ACT[order[0]]['name'])} — {html.escape(ACT[order[0]]['desc'])}</p><a href="{ACT[order[0]]['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
<div class="sidebar-card"><h4>🔗 Autres classements TPE</h4><ul class="sidebar-toc">
<li><a href="/comparatifs/tpe-gratuit.html">TPE gratuit →</a></li>
<li><a href="/comparatifs/tpe-sans-abonnement.html">TPE sans abonnement →</a></li>
<li><a href="/comparatifs/meilleur-tpe-pas-cher.html">TPE pas cher →</a></li>
<li><a href="/comparatifs/meilleur-tpe-restaurant.html">TPE restaurant →</a></li>
</ul></div>
</aside>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

n=0
for slug,title,desc,h1,intro,order in PAGES:
    open(f"comparatifs/{slug}.html","w").write(page(slug,title,desc,h1,intro,order)); n+=1
print("comparatifs TPE SEO générés:",n)
