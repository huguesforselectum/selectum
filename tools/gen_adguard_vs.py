#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html, os, json
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
exec(open("tools/gen_adguard.py").read().split("CAT=")[0])  # ACT
VERDICT={
 "ublock":"<strong>AdGuard</strong> agit au niveau du système : il bloque pubs et traceurs dans <em>toutes</em> vos apps (pas seulement le navigateur), moyennant une licence. <strong>uBlock Origin</strong> est gratuit, open-source et redoutablement efficace, mais limité au navigateur. uBlock suffit pour surfer ; AdGuard protège tout l'appareil.",
 "brave":"<strong>AdGuard</strong> s'ajoute au navigateur que vous utilisez déjà (et à vos apps). <strong>Brave</strong> est un navigateur complet avec blocage intégré : excellent si vous acceptez de changer de navigateur. Les deux se complètent même très bien.",
 "ghostery":"<strong>AdGuard</strong> bloque à la fois la publicité et le pistage, partout sur l'appareil. <strong>Ghostery</strong> est spécialisé dans l'anti-traçage avec un tableau de bord détaillé. Pour une protection complète pub+traceurs, AdGuard est plus large.",
 "adblockplus":"<strong>AdGuard</strong> est plus complet et plus strict. <strong>AdBlock Plus</strong> est le plus populaire et le plus simple, mais autorise par défaut des « publicités acceptables » — à désactiver pour un blocage total.",
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
ag=ACT['adguard']; n=0
for slug in ["ublock","brave","ghostery","adblockplus"]:
    c=ACT[slug]; cn=html.escape(c['name']); url=f"https://selectum.fr/comparatifs/adguard-vs-{slug}.html"
    title=f"AdGuard ou {c['name']} ? Comparatif bloqueur de pub 2026 | Selectum"
    desc=f"AdGuard vs {c['name']} : efficacité, prix, navigateur ou système. Comparatif 2026 pour choisir le meilleur bloqueur de publicité."
    qa=[(f"AdGuard ou {c['name']} : lequel choisir ?",f"AdGuard bloque pubs et traceurs au niveau système (toutes apps). {c['name']} : {html.escape(c['desc'])} Le choix dépend de si vous voulez une protection navigateur ou globale."),
        (f"AdGuard est-il meilleur que {c['name']} ?",f"AdGuard est plus complet (système entier). {c['name']} a ses atouts ({html.escape(c['pts'][0])}). Pour bloquer la pub partout, AdGuard prend l'avantage."),
        (f"{c['name']} est-il gratuit ?",f"{c['name']} : {html.escape(c['price'])}. AdGuard propose une version d'essai et une licence (à vie possible, ~40 €).")]
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
<meta name="twitter:card" content="summary"><script type="application/ld+json">{ld}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/avis/adguard.html" class="btn-primary">Avis AdGuard →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
<div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/comparatifs/bloqueur-de-pub.html">Bloqueur de pub</a><span>/</span>AdGuard vs {cn}</div>
<h1>AdGuard ou {cn} ? Le comparatif 2026</h1>
<p class="updated">🗓️ Mis à jour le 11 juin 2026 — Analysé par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:920px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
<p>Vous hésitez entre <strong>AdGuard</strong> et <strong>{cn}</strong> pour bloquer la publicité ? Voici notre comparatif en face-à-face.</p>
<div class="vs-grid">{col(ag,'adguard',True)}<div class="vs-or">VS</div>{col(c,slug,False)}</div>
<h2>AdGuard vs {cn} : le verdict</h2>
<p>{VERDICT[slug]}</p>
<div class="comparison-table-wrap"><table class="comparison-table">
<thead><tr><th>Critère</th><th>AdGuard</th><th>{cn}</th></tr></thead><tbody>
<tr><td>Portée</td><td>Tout le système (toutes apps)</td><td>{html.escape(c['pts'][-1])}</td></tr>
<tr><td>Prix</td><td>Licence à vie ~40 €</td><td>{html.escape(c['price'])}</td></tr>
<tr><td>Anti-traçage</td><td>Oui</td><td>{'Oui' if slug in ('ghostery','brave','ublock') else 'Partiel'}</td></tr>
<tr><td>Plateformes</td><td>Windows, Mac, Android, iOS, navigateurs</td><td>{'Navigateur' if slug in ('ublock','adblockplus','ghostery') else 'Navigateur dédié'}</td></tr>
</tbody></table></div>
<div class="highlight-box"><p>💡 <strong>Notre conseil :</strong> pour bloquer la pub partout (apps incluses) et sur tous vos appareils, <strong>AdGuard</strong> est le plus complet. {cn} reste un excellent choix {('gratuit pour le navigateur' if slug in ('ublock','adblockplus') else 'selon votre usage')}.</p></div>
<div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qatxt)+f'''</div>
<p style="margin-top:22px;">Pour aller plus loin : <a href="/avis/adguard.html">Avis AdGuard</a> · <a href="/comparatifs/bloqueur-de-pub.html">Comparatif des bloqueurs de pub</a></p>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''
    open(f"comparatifs/adguard-vs-{slug}.html","w").write(page); n+=1
print("pages adguard-vs:",n)
