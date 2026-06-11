#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html, os, json
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
exec(open("tools/gen_ecommerce.py").read().split("CAT=")[0])  # ACT

VERDICT={
 "woocommerce":"<strong>Shopify</strong> est une solution tout-en-un hébergée : on se lance vite, sans technique, contre un abonnement mensuel. <strong>WooCommerce</strong> est open-source et gratuit, mais nécessite un hébergement WordPress et un peu de technique — imbattable sur la flexibilité, le SEO et le coût sur la durée.",
 "wix":"<strong>Shopify</strong> est taillé pour l'e-commerce sérieux et évolutif. <strong>Wix</strong> est plus simple et polyvalent, parfait pour une vitrine ou une petite boutique, mais montre ses limites quand le catalogue et le chiffre d'affaires grandissent.",
 "prestashop":"<strong>Shopify</strong> est clé-en-main et sans maintenance. <strong>PrestaShop</strong> est open-source, français et très puissant pour les gros catalogues, mais demande de l'hébergement et des compétences techniques.",
 "squarespace":"<strong>Shopify</strong> offre l'écosystème e-commerce le plus complet. <strong>Squarespace</strong> brille par son design premium, idéal pour les créateurs et marques visuelles avec un catalogue modéré.",
 "bigcommerce":"<strong>Shopify</strong> dispose du plus grand écosystème d'applications. <strong>BigCommerce</strong> séduit par l'absence de frais de transaction et sa robustesse pour les boutiques à fort volume.",
}
def col(a,slug,win):
    badge='<span class="best-badge">Notre choix</span>' if win else ''
    pts="".join(f"<li>{html.escape(p)}</li>" for p in a['pts'])
    return f'''<div class="vs-col{' vs-win' if win else ''}">
      <div class="vs-logo"><img src="/assets/logos/{slug}.png" alt="{html.escape(a['name'])}"></div>
      <h2>{html.escape(a['name'])} {badge}</h2>
      <div class="tp-score" style="max-width:150px;margin:6px auto 10px;"><b>{a['score']}</b><span>/10</span><small>Note Selectum</small></div>
      <ul class="tp-checklist" style="grid-template-columns:1fr;text-align:left;max-width:230px;margin:0 auto 12px;">{pts}</ul>
      <div class="vs-price">{html.escape(a['price'])}</div>
      <a href="{a['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir {html.escape(a['name'])} →</a>
    </div>'''
sh=ACT['shopify']
n=0
for slug in ["woocommerce","wix","prestashop","squarespace","bigcommerce"]:
    c=ACT[slug]; cn=html.escape(c['name']); url=f"https://selectum.fr/comparatifs/shopify-vs-{slug}.html"
    title=f"Shopify ou {c['name']} ? Comparatif e-commerce 2026 | Selectum"
    desc=f"Shopify vs {c['name']} : prix, simplicité, SEO, évolutivité. Comparatif 2026 pour choisir la meilleure plateforme pour créer votre boutique en ligne."
    qa=[(f"Shopify ou {c['name']} : lequel choisir ?",f"Shopify est idéal pour se lancer vite sans technique (abonnement tout-en-un). {c['name']} : {html.escape(c['desc'])} Le choix dépend de votre budget, de vos compétences techniques et de vos ambitions."),
        (f"Shopify est-il mieux que {c['name']} pour le SEO ?",f"Shopify offre un bon SEO clé-en-main ; {c['name']} peut aller plus loin selon la configuration. Pour un SEO très poussé, les solutions open-source ont l'avantage."),
        (f"Quel est le moins cher entre Shopify et {c['name']} ?",f"Shopify coûte dès 33 €/mois tout compris. {c['name']} affiche {html.escape(c['price'])}. Pensez à intégrer l'hébergement et les extensions dans le coût total.")]
    qatxt=[(html.escape(q),html.escape(a)) for q,a in qa]
    ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qatxt]},ensure_ascii=False)
    page=f'''<!DOCTYPE html>
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
<script type="application/ld+json">{ld}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/avis/shopify.html" class="btn-primary">Avis Shopify →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
<div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/comparatifs/ecommerce.html">E-commerce</a><span>/</span>Shopify vs {cn}</div>
<h1>Shopify ou {cn} ? Le comparatif e-commerce 2026</h1>
<p class="updated">🗓️ Mis à jour le 11 juin 2026 — Analysé par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:920px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
<p>Vous hésitez entre <strong>Shopify</strong> et <strong>{cn}</strong> pour créer votre boutique en ligne ? Voici notre comparatif en face-à-face.</p>
<div class="vs-grid">{col(sh,'shopify',True)}<div class="vs-or">VS</div>{col(c,slug,False)}</div>
<h2>Shopify vs {cn} : le verdict</h2>
<p>{VERDICT[slug]}</p>
<div class="comparison-table-wrap"><table class="comparison-table">
<thead><tr><th>Critère</th><th>Shopify</th><th>{cn}</th></tr></thead><tbody>
<tr><td>Modèle</td><td>SaaS tout-en-un hébergé</td><td>{html.escape(c['pts'][0])}</td></tr>
<tr><td>Prix</td><td>dès 33 €/mois</td><td>{html.escape(c['price'])}</td></tr>
<tr><td>Technique requise</td><td>Faible</td><td>{'Élevée' if slug in ('woocommerce','prestashop') else 'Faible'}</td></tr>
<tr><td>Évolutivité</td><td>Très élevée</td><td>{'Élevée' if slug in ('woocommerce','prestashop','bigcommerce') else 'Moyenne'}</td></tr>
<tr><td>Idéal pour</td><td>Se lancer vite, vendre sérieusement</td><td>{html.escape(c['pts'][-1])}</td></tr>
</tbody></table></div>
<div class="highlight-box"><p>💡 <strong>Notre conseil :</strong> pour démarrer rapidement et vendre sans contrainte technique, <strong>Shopify</strong> est le plus simple et le plus complet. {cn} reste pertinent si {('vous avez des compétences techniques et un budget serré' if slug in ('woocommerce','prestashop') else 'votre projet correspond à son point fort')}.</p></div>
<div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qatxt)+f'''</div>
<p style="margin-top:22px;">Pour aller plus loin : <a href="/avis/shopify.html">Avis Shopify</a> · <a href="/comparatifs/ecommerce.html">Comparatif des plateformes e-commerce</a></p>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''
    open(f"comparatifs/shopify-vs-{slug}.html","w").write(page); n+=1
print("pages shopify-vs générées:",n)
