#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages-études 'backlink bait' : baromètre frais crypto + classement hébergeurs.
Données indicatives publiques, relevées à date, avec disclaimers et bloc 'citer cette étude'."""
import os, html, json
FONT="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D="12 juin 2026"
os.makedirs("etudes", exist_ok=True)

def head(url,title,desc,extra=""):
    org='{"@context":"https://schema.org","@type":"Organization","name":"Selectum","url":"https://selectum.fr/","logo":"https://selectum.fr/assets/selectum-logo.png"}'
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
<style>
.chart{{margin:18px 0;display:flex;flex-direction:column;gap:10px;}}
.chart-row{{display:grid;grid-template-columns:130px 1fr 70px;align-items:center;gap:10px;font-size:.9rem;}}
.chart-bar{{height:22px;border-radius:6px;background:linear-gradient(90deg,#1B5FD9,#4F8BF0);min-width:2px;}}
.chart-bar.best{{background:linear-gradient(90deg,#16a34a,#4ade80);}}
.chart-val{{font-weight:700;text-align:right;}}
.cite-box{{background:var(--gray-50);border:1px solid var(--gray-200);border-radius:12px;padding:16px 18px;margin:20px 0;}}
.cite-box textarea{{width:100%;min-height:70px;font-family:monospace;font-size:.8rem;border:1px solid var(--gray-300);border-radius:8px;padding:10px;margin-top:8px;box-sizing:border-box;}}
.key-finding{{background:#eff6ff;border-left:4px solid #1B5FD9;border-radius:10px;padding:16px 18px;margin:18px 0;font-size:1.05rem;}}
@media(max-width:560px){{.chart-row{{grid-template-columns:96px 1fr 56px;font-size:.82rem;}}}}
</style>
<script type="application/ld+json">{org}</script>
{extra}</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/etudes.html" class="btn-primary">Nos études →</a></div>
</div></div></header>'''

FOOT='''<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/methodologie.html" style="color:var(--gray-500)">Méthodologie</a> · <a href="/etudes.html" style="color:var(--gray-500)">Études</a></p>
</div></div></footer></body></html>'''

def chart(rows, unit, lower_better=True):
    mx=max(v for _,v in rows) or 1
    best=min(rows,key=lambda r:r[1])[0] if lower_better else max(rows,key=lambda r:r[1])[0]
    out='<div class="chart">'
    for lab,v in rows:
        w=max(2,round(v/mx*100))
        cls=" best" if lab==best else ""
        out+=f'<div class="chart-row"><span>{html.escape(lab)}</span><div class="chart-bar{cls}" style="width:{w}%"></div><span class="chart-val">{v}{unit}</span></div>'
    return out+'</div>'

def cite(url,label):
    emb=f'Source : {label}, Selectum ({url}).'
    embhtml=html.escape(f'<a href="{url}">{label}</a> — Selectum')
    return (f'<div class="cite-box"><strong>📎 Citer cette étude</strong>'
        f'<p style="margin:6px 0 0;font-size:.9rem;color:var(--gray-600);">Vous pouvez reprendre ces données en citant la source :</p>'
        f'<p style="margin:8px 0 0;font-style:italic;">{html.escape(emb)}</p>'
        f'<textarea readonly onclick="this.select()">{embhtml}</textarea></div>')

def faqblock(faq):
    return '<div class="faq"><h2>❓ Questions fréquentes</h2>'+''.join(
        f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)+'</div>'

# ============ ÉTUDE 1 : Baromètre frais crypto ============
url1="https://selectum.fr/etudes/barometre-frais-crypto.html"
t1="Baromètre 2026 des frais des applications crypto"
d1="Baromètre 2026 des frais de trading des applications crypto (Binance, Kraken, Coinbase, Bitpanda…) : frais maker/taker indicatifs, dépôt et retrait, comparés par Selectum."
# frais taker indicatifs (interface pro / spot), en %, relevés juin 2026 — sources officielles
CRYPTO=[("Binance",0.10),("Bitget",0.10),("Kraken",0.26),("Coinbase",0.60),("Coinhouse",1.49),("Bitpanda",1.49)]
faq1=[("Quelle est l'application crypto la moins chère en 2026 ?","Sur les frais de trading affichés (spot/maker-taker), Binance et Bitget figurent parmi les plus bas (~0,10 %). Mais le coût réel dépend du mode d'achat : l'achat « simple/instantané » et le spread renchérissent la note."),
 ("Ces frais incluent-ils le spread ?","Non. Ce baromètre compare les frais de trading affichés. Le spread (écart achat/vente) et les frais de carte s'ajoutent au coût réel, et sont souvent le poste le plus cher sur l'achat simple."),
 ("Les chiffres sont-ils contractuels ?","Non, ce sont des valeurs indicatives relevées en juin 2026 à partir des grilles publiques. Les tarifs évoluent : la grille officielle de chaque acteur fait foi."),
 ("Comment réduire ses frais crypto ?","Utilisez l'interface « pro/advanced » plutôt que l'achat express, passez des ordres limites (maker), et déposez en euros par virement SEPA plutôt que par carte.")]
art1=json.dumps({"@context":"https://schema.org","@type":"Article","headline":t1,"description":d1,"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-12","dateModified":"2026-06-12","mainEntityOfPage":url1},ensure_ascii=False)
ds1=json.dumps({"@context":"https://schema.org","@type":"Dataset","name":t1,"description":d1,"url":url1,"creator":{"@type":"Organization","name":"Selectum"},"dateModified":"2026-06-12","license":"https://selectum.fr/mentions-legales.html"},ensure_ascii=False)
faqld1=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq1]},ensure_ascii=False)
rows1="".join(f'<tr><td><strong>{n}</strong></td><td>{v:.2f} %</td><td>{"Gratuit / faible" if n in("Binance","Kraken","Bitget") else "Variable"}</td><td><a href="/avis/{n.lower()}.html">Avis {n}</a></td></tr>' for n,v in CRYPTO)
body1=f'''<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/etudes.html">Études</a><span>/</span>Baromètre frais crypto</div>
  <h1>{t1}</h1>
  <p class="updated">🗓️ Relevé le {D} — méthodologie Selectum</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Méthodologie :</strong> frais de trading affichés (spot / maker-taker), relevés le {D} sur les grilles publiques des plateformes. Hors spread, hors frais de carte et hors promotions. Valeurs <strong>indicatives</strong> — la grille officielle de chaque acteur fait foi. Investir comporte un risque de perte en capital.</div>
<div class="key-finding">📊 <strong>Le chiffre clé :</strong> entre l'application la moins chère (~0,10 % de frais de trading) et l'achat « simple » des acteurs grand public (jusqu'à ~1,5 % + spread), le coût d'un même achat de crypto peut être <strong>multiplié par 15</strong>. Le poste qui pèse le plus n'est pas le bonus de bienvenue, mais le <strong>mode d'achat</strong>.</div>
<h2>Frais de trading indicatifs (interface pro, taker)</h2>
{chart([(n,v) for n,v in CRYPTO],' %')}
<div style="overflow-x:auto;"><table class="comparison-table" style="min-width:520px;"><thead><tr><th>Application</th><th>Frais trading (taker)*</th><th>Dépôt SEPA</th><th>Notre analyse</th></tr></thead><tbody>{rows1}</tbody></table></div>
<p style="font-size:.85rem;color:var(--gray-500);">* Frais affichés sur l'interface pro/advanced, relevés le {D}. L'achat « instantané » est généralement plus cher (spread inclus).</p>
{cite(url1,"Baromètre 2026 des frais des applications crypto")}
<h2>Comment lire ce baromètre</h2>
<p>Les <strong>frais de trading</strong> affichés ne sont qu'une partie du coût. Pour un achat ponctuel par carte, le <strong>spread</strong> et les frais de carte dominent. Pour de l'investissement régulier, ce sont les frais maker/taker qui comptent sur la durée. Notre conseil : privilégier l'interface pro/advanced, les ordres limites et le virement SEPA.</p>
<p>Pour aller plus loin : <a href="/comparatifs/crypto.html">comparatif des applications crypto</a>, <a href="/comparatifs/crypto-frais-bas.html">plateformes crypto à frais bas</a>, <a href="/guides/coinbase-frais.html">frais Coinbase</a>, <a href="/code-promo-crypto.html">codes promo crypto</a>.</p>
{faqblock(faq1)}
<div class="rel-links"><h2>À lire aussi</h2><div class="rel-list"><a href="/comparatifs/crypto.html" class="rel-chip">Comparatif crypto →</a><a href="/comparatifs/crypto-frais-bas.html" class="rel-chip">Crypto frais bas →</a><a href="/code-promo-crypto.html" class="rel-chip">Codes promo crypto →</a><a href="/etudes.html" class="rel-chip">Toutes nos études →</a></div></div>
</div></div>'''
open("etudes/barometre-frais-crypto.html","w",encoding="utf-8").write(
    head(url1,t1+" | Selectum",d1,f'<script type="application/ld+json">{art1}</script>\n<script type="application/ld+json">{ds1}</script>\n<script type="application/ld+json">{faqld1}</script>\n')+body1+FOOT)

# ============ ÉTUDE 2 : Classement hébergeurs les moins chers ============
url2="https://selectum.fr/etudes/classement-hebergeurs-moins-chers.html"
t2="Classement 2026 des hébergeurs web les moins chers"
d2="Classement 2026 des hébergeurs web les moins chers : prix d'appel mensuels indicatifs de Hostinger, IONOS, OVHcloud, o2switch, PlanetHoster, Infomaniak, comparés par Selectum."
# prix d'appel mensuel indicatif (mutualisé entrée, engagement long), en €, relevés juin 2026
HOST=[("Hostinger",2.99),("IONOS",1.00),("OVHcloud",3.59),("PlanetHoster",5.00),("Infomaniak",5.75),("o2switch",7.00)]
faq2=[("Quel est l'hébergeur web le moins cher en 2026 ?","Sur le prix d'appel, IONOS et Hostinger sont les plus agressifs (~1 à 3 €/mois sur engagement long). Mais attention au prix de renouvellement, souvent bien plus élevé."),
 ("Le prix d'appel est-il le vrai prix ?","Non. Beaucoup d'hébergeurs affichent un tarif promotionnel la 1re période, puis renouvellent plus cher. o2switch fait exception avec un tarif unique stable."),
 ("Ces prix sont-ils garantis ?","Non, ce sont des prix d'appel indicatifs relevés en juin 2026, hors promotions ponctuelles. La page tarifaire officielle de chaque hébergeur fait foi."),
 ("Faut-il choisir le moins cher ?","Pas seulement. Regardez aussi la performance, le support, le prix de renouvellement et les ressources incluses. Le moins cher à l'entrée n'est pas toujours le plus économique sur 3 ans.")]
art2=json.dumps({"@context":"https://schema.org","@type":"Article","headline":t2,"description":d2,"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-12","dateModified":"2026-06-12","mainEntityOfPage":url2},ensure_ascii=False)
ds2=json.dumps({"@context":"https://schema.org","@type":"Dataset","name":t2,"description":d2,"url":url2,"creator":{"@type":"Organization","name":"Selectum"},"dateModified":"2026-06-12"},ensure_ascii=False)
faqld2=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq2]},ensure_ascii=False)
HOSTSORT=sorted(HOST,key=lambda x:x[1])
rows2="".join(f'<tr><td><strong>{i+1}. {n}</strong></td><td>dès {v:.2f} €/mois*</td><td><a href="/avis/{("ovhcloud" if n=="OVHcloud" else n.lower())}.html">Avis {n}</a></td></tr>' for i,(n,v) in enumerate(HOSTSORT))
body2=f'''<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/etudes.html">Études</a><span>/</span>Hébergeurs les moins chers</div>
  <h1>{t2}</h1>
  <p class="updated">🗓️ Relevé le {D} — méthodologie Selectum</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Méthodologie :</strong> prix d'appel mensuels des offres mutualisées d'entrée de gamme (engagement long), relevés le {D} sur les sites officiels. Hors promotions ponctuelles. Valeurs <strong>indicatives</strong> — la page tarifaire de chaque hébergeur fait foi.</div>
<div class="key-finding">📊 <strong>Le chiffre clé :</strong> le prix d'appel d'un hébergement mutualisé va de <strong>~1 €/mois à ~7 €/mois</strong> selon l'acteur. Mais le vrai écart se joue au <strong>renouvellement</strong> : certains tarifs d'appel doublent voire triplent après la première période.</div>
<h2>Classement par prix d'appel mensuel</h2>
{chart([(n,v) for n,v in HOSTSORT],' €')}
<div style="overflow-x:auto;"><table class="comparison-table" style="min-width:480px;"><thead><tr><th>Hébergeur</th><th>Prix d'appel*</th><th>Notre avis</th></tr></thead><tbody>{rows2}</tbody></table></div>
<p style="font-size:.85rem;color:var(--gray-500);">* Offre mutualisée d'entrée de gamme, engagement long, hors promo ponctuelle, relevé le {D}. Attention au prix de renouvellement.</p>
{cite(url2,"Classement 2026 des hébergeurs web les moins chers")}
<h2>Le piège du prix d'appel</h2>
<p>La plupart des hébergeurs affichent un <strong>tarif promotionnel</strong> la première période, puis renouvellent bien plus cher. Pour comparer honnêtement, raisonnez en <strong>coût total sur 3 ans</strong> (prix d'appel + renouvellement). <strong>o2switch</strong> se distingue avec un tarif unique stable, sans hausse au renouvellement.</p>
<p>Pour choisir : <a href="/comparatifs/hebergement-web.html">comparatif des hébergeurs web</a>, <a href="/comparatifs/hostinger-vs-ionos.html">IONOS vs Hostinger</a>, <a href="/code-promo-hebergement.html">codes promo hébergement</a>.</p>
{faqblock(faq2)}
<div class="rel-links"><h2>À lire aussi</h2><div class="rel-list"><a href="/comparatifs/hebergement-web.html" class="rel-chip">Comparatif hébergeurs →</a><a href="/code-promo-hebergement.html" class="rel-chip">Codes promo hébergement →</a><a href="/code-promo/ionos.html" class="rel-chip">Code promo IONOS →</a><a href="/etudes.html" class="rel-chip">Toutes nos études →</a></div></div>
</div></div>'''
open("etudes/classement-hebergeurs-moins-chers.html","w",encoding="utf-8").write(
    head(url2,t2+" | Selectum",d2,f'<script type="application/ld+json">{art2}</script>\n<script type="application/ld+json">{ds2}</script>\n<script type="application/ld+json">{faqld2}</script>\n')+body2+FOOT)

# ============ Hub /etudes.html ============
hub=head("https://selectum.fr/etudes.html","Études & baromètres Selectum : données et classements 2026","Nos études et baromètres indépendants : frais des applications crypto, classement des hébergeurs web les moins chers, et plus. Données vérifiées, libres de citation.")
hub+=f'''<div class="hero" style="padding:52px 0 36px;"><div class="container"><div class="hero-content"><h1>Études & baromètres</h1><p>Des données indépendantes, vérifiées et libres de citation (avec lien).</p></div></div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
<div class="hub-grid">
<a href="/etudes/barometre-frais-crypto.html" class="hub-item">📊 Baromètre 2026 des frais des applications crypto</a>
<a href="/etudes/classement-hebergeurs-moins-chers.html" class="hub-item">🏆 Classement 2026 des hébergeurs web les moins chers</a>
</div>
<div class="highlight-box"><p>💡 Journalistes & blogueurs : ces données sont libres de reprise avec un lien vers la source. Contact : contact@selectum.fr</p></div>
</div></div>'''
hub+=FOOT
open("etudes.html","w",encoding="utf-8").write(hub)
print("études générées : barometre-frais-crypto, classement-hebergeurs-moins-chers + hub etudes.html")
