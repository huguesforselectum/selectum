#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html, os, json
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
ACT={
 "coinbase":dict(name="Coinbase",go="/go/coinbase",score="8,0",price="jusqu'à 3,99%",
   desc="La plateforme crypto la plus grand public : simple, rassurante et cotée en bourse aux États-Unis.",
   pts=["Très simple à utiliser","Coté en bourse (US)","Large choix de cryptos","Idéal grand public"]),
 "bitpanda":dict(name="Bitpanda",go="/go/bitpanda",score="9,2",price="1,49%",
   desc="Plateforme européenne régulée, idéale pour débuter (crypto + actions + ETF).",pts=["Régulé en Europe","Dès 1€","Crypto + actions + ETF","Bonus de bienvenue"]),
 "kraken":dict(name="Kraken",go="/go/kraken",score="8,4",price="dès 0,25%",
   desc="L'exchange le plus sécurisé, avec Kraken Pro et des frais bas.",pts=["Sécurité de référence","Frais bas sur Pro","Paires en euros","Virement SEPA"]),
 "binance":dict(name="Binance",go="/go/binance",score="8,2",price="0,10%",
   desc="Le plus gros exchange mondial, frais minimes et 350+ cryptos.",pts=["Frais les plus bas","350+ cryptos","Outils avancés","Très complet"]),
 "coinhouse":dict(name="Coinhouse",go="/go/coinhouse",score="7,8",price="dès 0,99%",
   desc="La plateforme française régulée AMF, avec accompagnement en français.",pts=["Français régulé AMF","Accompagnement","Support FR","Simplicité fiscale"]),
 "crypto-com":dict(name="Crypto.com",go="/go/crypto-com",score="8,0",price="frais variables",
   desc="L'app tout-en-un avec carte Visa, cashback et staking.",pts=["Carte Visa cashback","Staking","Régulé PSAN","App complète"]),
}
def col(slug,win):
    a=ACT[slug]; badge='<span class="best-badge">Notre choix</span>' if win else ''
    pts="".join(f"<li>{html.escape(p)}</li>" for p in a['pts'])
    return f'''<div class="vs-col{' vs-win' if win else ''}">
      <div class="vs-logo"><img src="/assets/logos/{slug}.png" alt="{html.escape(a['name'])}"></div>
      <h2>{html.escape(a['name'])} {badge}</h2>
      <div class="tp-score" style="max-width:150px;margin:6px auto 10px;"><b>{a['score']}</b><span>/10</span><small>Note Selectum</small></div>
      <ul class="tp-checklist" style="grid-template-columns:1fr;text-align:left;max-width:230px;margin:0 auto 12px;">{pts}</ul>
      <div class="vs-price">{html.escape(a['price'])}<span style="display:block;font-size:.7rem;color:var(--gray-500);font-weight:600;">par transaction</span></div>
      <a href="{a['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir {html.escape(a['name'])} →</a>
    </div>'''
def fn(x):
    try: return float(x.replace(',','.'))
    except: return 0
n=0
for slug in ["bitpanda","kraken","binance","coinhouse","crypto-com"]:
    if os.path.exists(f"comparatifs/coinbase-vs-{slug}.html") or os.path.exists(f"comparatifs/{slug}-vs-coinbase.html"): 
        # supprime la version inversée pour garder coinbase-first
        rev=f"comparatifs/{slug}-vs-coinbase.html"
        if os.path.exists(rev): os.remove(rev)
    cb=ACT['coinbase']; c=ACT[slug]; cn=html.escape(c['name'])
    win_cb = fn(cb['score'])>=fn(c['score'])
    url=f"https://selectum.fr/comparatifs/coinbase-vs-{slug}.html"
    title=f"Coinbase ou {c['name']} ? Comparatif crypto 2026 | Selectum"
    desc=f"Coinbase vs {c['name']} : frais, simplicité, sécurité et régulation. Comparatif 2026 pour choisir la meilleure plateforme crypto. Investir comporte un risque de perte en capital."
    verdict=(f"<strong>Coinbase</strong> mise tout sur la simplicité et la confiance (société cotée), idéale pour débuter, mais ses frais ({cb['price']}) sont parmi les plus élevés. <strong>{cn}</strong> ({html.escape(c['desc'])}) l'emporte sur {('les frais' if slug in ('binance','kraken') else 'la régulation et le rapport global')}. Pour un grand débutant qui veut le maximum de simplicité, Coinbase reste pertinent ; sinon {cn} offre un meilleur rapport global.")
    qa=[(f"Coinbase ou {c['name']} : lequel choisir ?",f"Coinbase est le plus simple et rassurant pour débuter, mais plus cher. {cn} : {html.escape(c['desc'])} Le choix dépend de votre priorité : simplicité (Coinbase) ou frais/régulation ({cn})."),
        ("Lequel a les frais les plus bas ?",f"{cn} ({c['price']}) est généralement moins cher que Coinbase (jusqu'à 3,99% par carte). Pensez à utiliser les modes d'achat les moins coûteux."),
        ("Sont-ils sûrs et régulés ?","Les deux appliquent des standards de sécurité élevés. Investir en crypto comporte toutefois un risque de perte en capital.")]
    qx=[(html.escape(q),html.escape(a)) for q,a in qa]
    ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qx]},ensure_ascii=False)
    pg=f'''<!DOCTYPE html>
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
<nav class="nav"></nav><div class="header-cta"><a href="/comparatifs/crypto.html" class="btn-primary">Comparatif crypto →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
<div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/comparatifs/crypto.html">Crypto</a><span>/</span>Coinbase vs {cn}</div>
<h1>Coinbase ou {cn} ? Le comparatif crypto 2026</h1>
<p class="updated">🗓️ Mis à jour le 11 juin 2026 — Analysé par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:920px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Investir comporte un risque de perte en capital.</div>
<p>Vous hésitez entre <strong>Coinbase</strong> et <strong>{cn}</strong> pour acheter vos cryptos ? Voici notre comparatif en face-à-face.</p>
<div class="vs-grid">{col('coinbase',win_cb)}<div class="vs-or">VS</div>{col(slug,not win_cb)}</div>
<h2>Coinbase vs {cn} : le verdict</h2>
<p>{verdict}</p>
<div class="comparison-table-wrap"><table class="comparison-table">
<thead><tr><th>Critère</th><th>Coinbase</th><th>{cn}</th></tr></thead><tbody>
<tr><td>Frais</td><td>{html.escape(cb['price'])}</td><td>{html.escape(c['price'])}</td></tr>
<tr><td>Simplicité</td><td>Excellente</td><td>{'Excellente' if slug in ('bitpanda','coinhouse','crypto-com') else 'Bonne'}</td></tr>
<tr><td>Note Selectum</td><td>{cb['score']}/10</td><td>{c['score']}/10</td></tr>
</tbody></table></div>
<div class="highlight-box"><p>💡 <strong>Notre conseil :</strong> pour démarrer en toute simplicité avec une marque rassurante, Coinbase est un bon point d'entrée. Pour optimiser les frais ou la régulation, regardez {cn} et notre <a href="/comparatifs/crypto.html">comparatif crypto complet</a>.</p></div>
<div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qx)+f'''</div>
<p style="margin-top:22px;">À lire aussi : <a href="/avis/coinbase.html">Avis Coinbase</a> · <a href="/comparatifs/crypto.html">Comparatif des plateformes crypto</a></p>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''
    open(f"comparatifs/coinbase-vs-{slug}.html","w").write(pg); n+=1
print("pages coinbase-vs générées:",n)
