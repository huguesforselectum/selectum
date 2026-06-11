#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html, os, json, itertools
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
exec(open("tools/gen_tpe_seo.py").read().split("\nn=0")[0])  # ACT, page (ACT has slug data)

# enrich ACT with go/dom for vs
DOM={"sumup":"sumup.fr","zettle":"zettle.com","mypos":"mypos.com","square":"squareup.com","viva-wallet":"vivawallet.com","stripe":"stripe.com","payplug":"payplug.com","flatpay":"flatpay.com"}

def col(slug,win):
    a=ACT[slug]; badge='<span class="best-badge">Notre choix</span>' if win else ''
    # ACT (gen_tpe_seo) has: name, score, price, go, desc, pts
    pts="".join(f"<li>{html.escape(p)}</li>" for p in a['pts'])
    return f'''<div class="vs-col{' vs-win' if win else ''}">
      <div class="vs-logo"><img src="/assets/logos/{slug}.png" alt="{html.escape(a['name'])}"></div>
      <h2>{html.escape(a['name'])} {badge}</h2>
      <div class="tp-score" style="max-width:150px;margin:6px auto 10px;"><b>{a['score']}</b><span>/10</span><small>Note Selectum</small></div>
      <ul class="tp-checklist" style="grid-template-columns:1fr;text-align:left;max-width:230px;margin:0 auto 12px;">{pts}</ul>
      <div class="vs-price">{html.escape(a['price'])}<span style="display:block;font-size:.7rem;color:var(--gray-500);font-weight:600;">par transaction</span></div>
      <a href="{a['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir {html.escape(a['name'])} →</a>
    </div>'''

PAIRS=[("sumup","zettle"),("sumup","mypos"),("sumup","square"),("sumup","viva-wallet"),
       ("zettle","mypos"),("zettle","square"),("mypos","square"),("mypos","viva-wallet"),
       ("square","viva-wallet"),("stripe","sumup"),("payplug","sumup")]
def fnum(x): 
    try: return float(x.replace(',','.'))
    except: return 0
n=0
for x,y in PAIRS:
    # winner = meilleure note
    a,b=(x,y) if fnum(ACT[x]['score'])>=fnum(ACT[y]['score']) else (y,x)
    if os.path.exists(f"comparatifs/{a}-vs-{b}.html") or os.path.exists(f"comparatifs/{b}-vs-{a}.html"): continue
    na,nb=html.escape(ACT[a]['name']),html.escape(ACT[b]['name'])
    slug=f"{a}-vs-{b}"; url=f"https://selectum.fr/comparatifs/{slug}.html"
    title=f"{ACT[a]['name']} ou {ACT[b]['name']} ? Comparatif TPE 2026 | Selectum"
    desc=f"{ACT[a]['name']} vs {ACT[b]['name']} : commission, engagement, matériel. Comparatif 2026 pour choisir le meilleur terminal de paiement."
    qa=[(f"{ACT[a]['name']} ou {ACT[b]['name']} : lequel choisir ?",f"{ACT[a]['name']} ({ACT[a]['price']}) et {ACT[b]['name']} ({ACT[b]['price']}) sont deux excellents TPE sans engagement. Le choix dépend de votre volume, de vos besoins (IBAN, caisse) et de votre budget matériel."),
        ("Lequel a la commission la plus basse ?",f"{ACT[a]['name']} affiche {ACT[a]['price']} contre {ACT[b]['price']} pour {ACT[b]['name']}. Comparez aussi le prix du terminal et l'absence d'abonnement."),
        ("Y a-t-il un engagement ?","Ces deux solutions fonctionnent généralement sans engagement, avec achat du terminal. Idéal pour tester sans risque.")]
    qatxt=[(html.escape(q),html.escape(a2)) for q,a2 in qa]
    ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a2}} for q,a2 in qatxt]},ensure_ascii=False)
    page_html=f'''<!DOCTYPE html>
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
<nav class="nav"></nav><div class="header-cta"><a href="/comparatifs/terminaux-paiement.html" class="btn-primary">Comparatif TPE →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
<div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/comparatifs/terminaux-paiement.html">Terminaux de paiement</a><span>/</span>{na} vs {nb}</div>
<h1>{na} ou {nb} ? Le comparatif TPE 2026</h1>
<p class="updated">🗓️ Mis à jour le 11 juin 2026 — Analysé par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:920px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
<p>Vous hésitez entre <strong>{na}</strong> et <strong>{nb}</strong> pour encaisser les paiements de votre commerce ? Voici notre comparatif en face-à-face.</p>
<div class="vs-grid">{col(a,True)}<div class="vs-or">VS</div>{col(b,False)}</div>
<h2>{na} vs {nb} : le verdict</h2>
<p><strong>{na}</strong> ({html.escape(ACT[a]['desc'])}) garde l'avantage dans notre classement, mais <strong>{nb}</strong> ({html.escape(ACT[b]['desc'])}) reste une excellente alternative selon vos priorités. Comparez la commission, le prix du terminal et les services inclus.</p>
<div class="comparison-table-wrap"><table class="comparison-table">
<thead><tr><th>Critère</th><th>{na}</th><th>{nb}</th></tr></thead><tbody>
<tr><td>Commission</td><td>{html.escape(ACT[a]['price'])}</td><td>{html.escape(ACT[b]['price'])}</td></tr>
<tr><td>Engagement</td><td>Sans engagement</td><td>Sans engagement</td></tr>
<tr><td>Note Selectum</td><td>{ACT[a]['score']}/10</td><td>{ACT[b]['score']}/10</td></tr>
</tbody></table></div>
<div class="highlight-box"><p>💡 <strong>Notre conseil :</strong> départagez selon votre volume et vos besoins annexes (IBAN pro, logiciel de caisse, fonds instantanés). Pour un volume régulier et une commission fixe basse, regardez aussi <a href="/comparatifs/terminaux-paiement.html">notre comparatif complet</a>.</p></div>
<div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a2}</div></div>' for q,a2 in qatxt)+f'''</div>
<p style="margin-top:22px;">À lire aussi : <a href="/comparatifs/terminaux-paiement.html">comparatif des TPE</a> · <a href="/comparatifs/flatpay-vs-{a}.html">Flatpay vs {na}</a></p>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''
    open(f"comparatifs/{slug}.html","w").write(page_html); n+=1
print("comparaisons TPE concurrents générées:",n)
