#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages 'meilleures offres [categorie]' : selection editoriale qui pousse les code-promo Tier 1."""
import os, html, json
FONT="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D="12 juin 2026"

def head(url,title,desc,extra=""):
    org='{"@context":"https://schema.org","@type":"Organization","name":"Selectum","url":"https://selectum.fr/","logo":"https://selectum.fr/assets/selectum-logo.png"}'
    ws='{"@context":"https://schema.org","@type":"WebSite","name":"Selectum","url":"https://selectum.fr/","inLanguage":"fr-FR"}'
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="article"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<script type="application/ld+json">{org}</script>
<script type="application/ld+json">{ws}</script>
{extra}</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/code-promo.html" class="btn-primary">Tous les codes promo →</a></div>
</div></div></header>'''

FOOT='''<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a> · <a href="/code-promo.html" style="color:var(--gray-500)">Codes promo</a> · <a href="/methodologie.html" style="color:var(--gray-500)">Méthodologie</a></p>
</div></div></footer></body></html>'''

# slug, h1, intro, comparatif_url, comparatif_label, hub_url, offers[(brand_slug, name, why)], faq
PAGES=[
 ("meilleures-offres-crypto","Meilleures offres crypto 2026 : bonus et codes promo",
  "Quelles sont les meilleures offres de bienvenue crypto en 2026 ? Notre sélection des bonus et avantages à l'inscription sur les applications crypto, vérifiée ce mois-ci.",
  "/comparatifs/crypto.html","comparatif des applications crypto","/code-promo-crypto.html",
  [("coinbase","Coinbase","L'application la plus simple pour débuter, offre de bienvenue régulière."),
   ("bitpanda","Bitpanda","Acteur européen tout-en-un (crypto, actions, métaux), avantage à l'inscription."),
   ("kraken","Kraken","La référence sécurité avec Kraken Pro pour des frais réduits."),
   ("binance","Binance","Le plus grand choix de cryptos et des frais parmi les plus bas."),
   ("etoro","eToro","Crypto + actions/ETF et copy-trading, compte démo gratuit.")],
  [("Quelle est la meilleure offre crypto en 2026 ?","Cela dépend de votre profil : Coinbase/Bitpanda pour débuter simplement, Kraken/Binance pour des frais bas. L'offre de bienvenue compte moins que les frais sur la durée."),
   ("Les bonus crypto sont-ils garantis ?","Non, les offres évoluent et dépendent de conditions (premier achat, montant…). Vérifiez les conditions officielles avant de souscrire."),
   ("Comment profiter d'une offre crypto ?","Passez par le lien de l'offre, créez votre compte, validez votre identité et réalisez l'action demandée. L'avantage est crédité selon les conditions.")]),
 ("meilleures-offres-banque","Meilleures offres banque en ligne 2026 : primes de bienvenue",
  "Les meilleures primes de bienvenue des banques en ligne et néobanques en 2026 : notre sélection des offres à l'ouverture d'un compte, vérifiée ce mois-ci.",
  "/comparatifs/banque-en-ligne.html","comparatif des banques en ligne","/code-promo-banque.html",
  [("boursobank","BoursoBank","Une vraie banque en ligne complète avec prime de bienvenue récurrente."),
   ("n26","N26","La banque 100 % mobile sans frais de tenue de compte."),
   ("revolut","Revolut","Le multidevises et le change avantageux, mois Premium parfois offerts."),
   ("monabanq","Monabanq","Banque en ligne au service client salué, offre d'ouverture régulière.")],
  [("Quelle banque en ligne offre la meilleure prime ?","BoursoBank propose régulièrement l'une des primes les plus élevées. Mais comparez aussi les frais et services, pas seulement le bonus."),
   ("La prime de bienvenue est-elle imposable ?","Une prime bancaire de bienvenue peut être soumise à fiscalité selon sa nature ; renseignez-vous sur votre situation."),
   ("Comment toucher la prime ?","Ouvrez le compte via l'offre et remplissez les conditions (premier versement, domiciliation…) ; la prime est versée ensuite selon les délais de la banque.")]),
 ("meilleures-offres-compte-pro","Meilleures offres compte pro 2026 : bonus pour entreprises",
  "Les meilleures offres de bienvenue des comptes professionnels en 2026 pour indépendants, TPE et sociétés : notre sélection vérifiée ce mois-ci.",
  "/comparatifs/comptes-pro.html","comparatif des comptes pro","/code-promo-compte-pro.html",
  [("qonto","Qonto","La référence du compte pro : complet, fiable, offre de bienvenue régulière."),
   ("shine","Shine","Pensé pour les indépendants avec outils administratifs intégrés."),
   ("finom","Finom","Plan gratuit et cashback, idéal pour démarrer une petite structure."),
   ("wise","Wise","Imbattable sur le multidevises et les paiements internationaux.")],
  [("Quel compte pro offre le meilleur bonus ?","Qonto et Shine proposent des offres de bienvenue régulières. Le bon choix dépend surtout de vos besoins (cartes, virements, compta)."),
   ("Un compte pro est-il obligatoire ?","Pour les sociétés, oui. Pour la micro-entreprise, un compte dédié est requis au-delà d'un certain CA pendant deux ans."),
   ("Comment profiter de l'offre compte pro ?","Ouvrez le compte via l'offre et finalisez la vérification d'entreprise (KYB) ; l'avantage s'applique selon les conditions.")]),
 ("meilleures-offres-hebergement","Meilleures offres hébergement web 2026 : promos et réductions",
  "Les meilleures offres d'hébergement web en 2026 : notre sélection des promotions et prix d'appel les plus agressifs (IONOS, Hostinger, OVHcloud, o2switch), vérifiée ce mois-ci.",
  "/comparatifs/hebergement-web.html","comparatif des hébergeurs web","/code-promo-hebergement.html",
  [("hostinger","Hostinger","Souvent le moins cher à l'entrée sur les engagements longs."),
   ("ionos","IONOS","Prix d'appel très agressifs la première année, offre complète."),
   ("ovhcloud","OVHcloud","L'acteur français, fort sur le VPS et le cloud."),
   ("o2switch","o2switch","Offre unique tout compris, sans hausse au renouvellement.")],
  [("Quel est le meilleur prix pour héberger un site ?","Les prix d'appel démarrent autour de 1-3 €/mois (IONOS, Hostinger). Attention au prix de renouvellement, souvent plus élevé — voir notre classement des hébergeurs les moins chers."),
   ("Le prix d'appel est-il le vrai prix ?","Pas toujours : beaucoup d'hébergeurs renouvellent plus cher. o2switch propose un tarif unique stable."),
   ("Comment profiter d'une promo hébergement ?","Choisissez l'offre via le lien et engagez-vous sur la durée la plus longue pour bloquer le tarif d'appel.")]),
 ("meilleures-offres-bourse","Meilleures offres bourse 2026 : courtiers et bonus",
  "Les meilleures offres des courtiers en bourse en 2026 : bonus de bienvenue, 0 % de commission et frais réduits (XTB, Trade Republic, DEGIRO, eToro), notre sélection vérifiée.",
  "/comparatifs/trading-bourse.html","comparatif des courtiers en bourse","/code-promo-bourse.html",
  [("xtb","XTB","0 % de commission sur les actions jusqu'à un seuil, plateforme complète."),
   ("trade-republic","Trade Republic","Plans d'épargne automatiques en ETF à 1 €/ordre, liquidités rémunérées."),
   ("etoro","eToro","Actions, ETF et crypto avec copy-trading, compte démo."),
   ("degiro","DEGIRO","Courtier low-cost avec un très large choix de places.")],
  [("Quel courtier offre le meilleur bonus en 2026 ?","Les offres varient ; XTB et Trade Republic sont parmi les plus attractifs sur les frais. Investir comporte un risque de perte en capital."),
   ("PEA ou compte-titres pour profiter d'une offre ?","Cela dépend de votre fiscalité et de votre horizon. Le PEA offre un avantage fiscal après 5 ans ; le CTO est plus flexible."),
   ("Comment profiter d'une offre de courtier ?","Ouvrez le compte via l'offre, validez votre identité et effectuez le dépôt ou l'action requise selon les conditions.")]),
]

def build(slug,h1,intro,comp,complab,hub,offers,faq):
    url=f"https://selectum.fr/{slug}.html"
    art=json.dumps({"@context":"https://schema.org","@type":"Article","headline":h1,"description":intro[:155],"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-12","dateModified":"2026-06-12","mainEntityOfPage":url},ensure_ascii=False)
    il=json.dumps({"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":nm} for i,(s,nm,w) in enumerate(offers)]},ensure_ascii=False)
    fld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)
    bc=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},{"@type":"ListItem","position":2,"name":"Codes promo","item":"https://selectum.fr/code-promo.html"},{"@type":"ListItem","position":3,"name":h1,"item":url}]},ensure_ascii=False)
    cards=""
    for i,(s,nm,why) in enumerate(offers):
        logo=f'<img src="/assets/logos/{s}.png" alt="{html.escape(nm)}" width="104" height="60" loading="lazy">' if os.path.exists(f"assets/logos/{s}.png") else ""
        cards+=f'''<div class="offer-card">
  <div class="offer-rank">{i+1}</div>
  <div class="offer-logo brand">{logo}</div>
  <div class="offer-info"><div class="offer-name">{html.escape(nm)}</div><div class="offer-desc">{html.escape(why)}</div>
    <div style="font-size:.82rem;margin-top:4px;"><a href="/code-promo/{s}.html">Code promo {html.escape(nm)}</a> · <a href="/avis/{s}.html">Avis {html.escape(nm)}</a></div></div>
  <div class="offer-buy"><a href="/go/{s}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
</div>'''
    faqh="".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)
    body=f'''<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/code-promo.html">Codes promo</a><span>/</span>{html.escape(h1.split(":")[0].strip())}</div>
  <h1>{html.escape(h1)}</h1>
  <p class="updated">🗓️ Mis à jour le {D} — sélection vérifiée par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-solo"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires (<code>rel="sponsored nofollow"</code>), sans surcoût pour vous.</div>
  <div class="intro-box"><p>{html.escape(intro)}</p></div>
  <h2 id="selection">🏆 Notre sélection des meilleures offres</h2>
  <div class="offers-list">{cards}</div>
  <div class="highlight-box"><p>💡 Voir aussi : <a href="{hub}">tous les codes promo {html.escape(complab.split("des ")[-1].split("comparatif")[-1].strip() or slug)}</a> et notre <a href="{comp}">{html.escape(complab)}</a>.</p></div>
  <div class="faq"><h2>❓ Questions fréquentes</h2>{faqh}</div>
  <div class="rel-links"><h2>À lire aussi</h2><div class="rel-list"><a href="{comp}" class="rel-chip">{html.escape(complab.capitalize())} →</a><a href="{hub}" class="rel-chip">Codes promo de la catégorie →</a><a href="/code-promo.html" class="rel-chip">Tous les codes promo →</a></div></div>
</main></div></div>'''
    open(f"{slug}.html","w",encoding="utf-8").write(head(url,h1+" | Selectum",intro[:155],
        f'<script type="application/ld+json">{art}</script>\n<script type="application/ld+json">{il}</script>\n<script type="application/ld+json">{fld}</script>\n<script type="application/ld+json">{bc}</script>\n')+body+FOOT)

for p in PAGES: build(*p)
print("pages 'meilleures offres' créées :", len(PAGES))
