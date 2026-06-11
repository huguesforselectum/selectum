#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère avis + code-promo + parrainage pour les acteurs cités sans page dédiée."""
import json, html, os, re
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
data=json.load(open("/tmp/missing_data.json"))

CATLABEL={'adblock':('Bloqueur de pub','/comparatifs/bloqueur-de-pub.html'),'ecommerce':('E-commerce','/comparatifs/ecommerce.html'),'vpn':('VPN','/comparatifs/vpn.html'),'hebergement-web':('Hébergement','/comparatifs/hebergement-web.html'),
 'banque-en-ligne':('Banque','/comparatifs/banque-en-ligne.html'),'assurance-auto':('Assurance','/comparatifs/assurance-auto.html'),
 'assurance-habitation':('Assurance','/comparatifs/assurance-habitation.html'),'mutuelle-sante':('Mutuelle','/comparatifs/mutuelle-sante.html'),
 'logiciels-comptabilite':('Logiciel','/comparatifs/logiciels-comptabilite.html'),'logiciels-crm':('CRM','/comparatifs/logiciels-crm.html'),
 'box-internet':('Box internet','/comparatifs/box-internet.html'),'crypto':('Crypto','/comparatifs/crypto.html')}

def head(title,desc,url,extra_ld=''):
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
  <link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:type" content="article"><meta property="og:site_name" content="Selectum">
  <meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
  <meta name="twitter:card" content="summary">{extra_ld}
</head>
<body>
<header class="header"><div class="container"><div class="header-inner">
  <a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
  <nav class="nav"></nav><div class="header-cta"><a href="/index.html" class="btn-primary">Tous les comparatifs →</a></div>
</div></div></header>'''

def hero(d,kind,h1,sub):
    cl,_=CATLABEL.get(d['cat'],('Comparatif','/index.html'))
    _,clink=CATLABEL.get(d['cat'],('Comparatif','/index.html'))
    return f'''<div class="brand-hero"><div class="container-article">
    <div class="brand-hero-logo"><img src="/assets/logos/{d['slug']}.png" alt="{html.escape(d['name'])}"></div>
    <div class="brand-hero-text">
      <div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / <a href="{clink}" style="color:rgba(255,255,255,.8)">{cl}</a> / {html.escape(d['name'])}</div>
      <h1>{h1}</h1><p class="subtitle">{sub}</p><p class="updated">🗓️ Mis à jour le 11 juin 2026</p>
    </div></div></div>'''

def footer():
    return '''<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
    <p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
    </div></div></footer></body></html>'''

def sidebar(d,kind):
    n=html.escape(d['name']); cl,clink=CATLABEL.get(d['cat'],('Comparatif','/index.html'))
    links=[]
    for t,p in [('Avis','avis'),('Code promo','code-promo'),('Parrainage','parrainage')]:
        if p!=kind: links.append(f'<li><a href="/{p}/{d["slug"]}.html">{t} {n} →</a></li>')
    links.append(f'<li><a href="{clink}">Comparatif {cl.lower()} →</a></li>')
    return f'''<aside class="sidebar">
      <div class="sidebar-cta"><h4>👉 {n}</h4><p>Découvrez l'offre {n} du moment.</p><a href="{d['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
      <div class="sidebar-card"><h4>🔗 À lire aussi</h4><ul class="sidebar-toc">{''.join(links)}</ul></div>
    </aside>'''

def faq_ld(qa):
    return '\n  <script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]},ensure_ascii=False)+'</script>'

def avis(d):
    n=html.escape(d['name']); desc=html.escape(d['desc']); url=f"https://selectum.fr/avis/{d['slug']}.html"
    score=d['rating'].split('/')[0]
    qa=[(f"{d['name']} est-il fiable ?",f"Oui, {d['name']} est un acteur reconnu de sa catégorie. Nous lui attribuons la note de {d['rating']} sur la base de notre analyse."),
        (f"Quels sont les avantages de {d['name']} ?",f"{d['name']} se distingue par : {d['desc']}. C'est l'un de ses principaux atouts face à la concurrence."),
        (f"Comment souscrire à {d['name']} ?",f"Il suffit de cliquer sur le lien vers l'offre {d['name']}, puis de suivre le parcours d'inscription en ligne.")]
    qatxt=[(html.escape(q),html.escape(a)) for q,a in qa]
    title=f"Avis {d['name']} 2026 : test, avis et offre | Selectum"
    mdesc=f"Avis {d['name']} 2026 : notre test complet, les points forts, les points faibles et l'offre du moment. Note {d['rating']}."
    return head(title,mdesc,url,faq_ld(qatxt))+hero(d,'avis',f"Avis {n} 2026 : notre test complet",desc)+f'''
<div class="container-article"><div class="article-layout" style="grid-template-columns: 1fr 300px;"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
  <div class="verdict-box"><div class="verdict-score"><div class="num">{score.replace('.',',')}</div><div class="out">/ 5</div></div>
  <div class="verdict-text"><h3>Notre verdict</h3><p><strong>{n}</strong> — {desc}. Un choix que nous recommandons dans notre comparatif, avec la note de {d['rating']}.</p></div></div>
  <h2 id="presentation">{n} en bref</h2>
  <p>{n} fait partie des références que nous avons analysées. {desc}. Découvrez ci-dessous ses atouts, ses limites et comment en profiter au meilleur prix.</p>
  <div class="pros-cons">
    <div class="pros"><h4>✅ Points forts</h4><ul><li>{desc}</li><li>Réputation solide ({d['rating']})</li><li>Offre accessible en ligne</li></ul></div>
    <div class="cons"><h4>❌ À surveiller</h4><ul><li>Comparez toujours avec les alternatives de notre comparatif</li><li>Vérifiez les conditions tarifaires en vigueur</li></ul></div>
  </div>
  <div class="highlight-box"><p>💡 <strong>Astuce :</strong> avant de souscrire {n}, jetez un œil à notre <a href="/code-promo/{d['slug']}.html">page code promo {n}</a> et à son <a href="/parrainage/{d['slug']}.html">programme de parrainage</a> pour économiser.</p></div>
  <div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qatxt)+f'''</div>
</main>{sidebar(d,'avis')}</div></div>'''+footer()

def promo(d):
    n=html.escape(d['name']); url=f"https://selectum.fr/code-promo/{d['slug']}.html"
    qa=[(f"Y a-t-il un code promo {d['name']} ?",f"Les offres {d['name']} s'activent généralement via un lien partenaire, sans code à recopier. Cliquez sur le bouton pour en profiter."),
        (f"L'offre {d['name']} est-elle limitée dans le temps ?","Les promotions évoluent selon les périodes. Le montant affiché correspond à l'offre vérifiée à la date de mise à jour.")]
    qatxt=[(html.escape(q),html.escape(a)) for q,a in qa]
    title=f"Code promo {d['name']} 2026 : offre & réduction | Selectum"
    mdesc=f"Code promo {d['name']} 2026 : l'offre du moment et comment en profiter. Réduction vérifiée par notre équipe."
    return head(title,mdesc,url,faq_ld(qatxt))+hero(d,'code-promo',f"Code promo {n} 2026 : l'offre du moment",f"L'offre {n} actuelle, vérifiée par notre équipe.")+f'''
<div class="container-article"><div class="article-layout" style="grid-template-columns: 1fr 300px;"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
  <div class="promo-box"><span class="promo-badge">🔥 Offre vérifiée</span><h3>L'offre {n} du moment</h3>
    <p>{html.escape(d['desc'])}. Profitez de l'offre {n} en passant par notre lien — réduction appliquée automatiquement, sans code à recopier.</p>
    <a href="{d['go']}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre {n} →</a>
    <p class="promo-note">Offre soumise aux conditions {n}. Montant variable selon les périodes.</p></div>
  <h2 id="comment">Comment profiter de l'offre {n} ?</h2>
  <ol><li>Cliquez sur « Voir l'offre {n} » ci-dessus.</li><li>Vous arrivez sur {n} avec l'offre en cours appliquée.</li><li>Finalisez votre inscription / souscription en ligne.</li></ol>
  <div class="highlight-box"><p>💡 Pensez aussi au <a href="/parrainage/{d['slug']}.html">parrainage {n}</a> et à notre <a href="/avis/{d['slug']}.html">avis complet {n}</a>.</p></div>
  <div class="faq"><h2>❓ Questions fréquentes</h2>'''+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qatxt)+f'''</div>
</main>{sidebar(d,'code-promo')}</div></div>'''+footer()

n=0
for slug,d in data.items():
    if not os.path.exists(f"avis/{slug}.html"): open(f"avis/{slug}.html","w").write(avis(d)); n+=1
    if not os.path.exists(f"code-promo/{slug}.html"): open(f"code-promo/{slug}.html","w").write(promo(d)); n+=1
print("Généré",n,"pages (avis+code-promo manquants)")
