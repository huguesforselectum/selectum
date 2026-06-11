#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Déclinaisons SEO génériques pour plusieurs verticales (lit les données réelles des comparatifs)."""
import html, os, re, json
FONT='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'

def f1(s,pat,d=''):
    m=re.search(pat,s,re.S); return m.group(1).strip() if m else d

def load_actors(base):
    s=open(f"comparatifs/{base}.html").read()
    acts={}
    # découpe en cartes
    blocks=re.split(r'(?=<div class="offer-card)', s)
    for b in blocks:
        if 'offer-card' not in b[:30]: continue
        slug=f1(b,r'/assets/logos/([a-z0-9-]+)\.png')
        if not slug or slug in acts: continue
        name=f1(b,r'tp-name">([^<]+)<') or f1(b,r'offer-name">([^<]+)<')
        if not name: continue
        name=re.split(r'\s+[—–-]\s+', name)[0].split(' (')[0].strip()
        go=f1(b,r'href="(/go/[^"]+)"', f"/go/{slug}")
        score=f1(b,r'tp-score"><b>([^<]+)<') or f1(b,r'offer-score-mini"><b>([^<]+)<')
        if not score:
            rm=re.search(r'rating-text">([0-9.,]+)/5', b)
            score=("%.1f"%(float(rm.group(1).replace(',','.'))*2)).replace('.',',') if rm else "9,0"
        price=f1(b,r'tp-price">([^<]+)<') or f1(b,r'class="price">([^<]+)<') or f1(b,r'offer-price">([^<]+?)<')
        note=f1(b,r'offer-price">[^<]*<span>([^<]+)<')
        desc=f1(b,r'tp-tagline">([^<]+)<') or f1(b,r'offer-desc">([^<]+)<')
        pts=re.findall(r'<li>([^<]+)</li>', f1(b,r'tp-checklist">(.*?)</ul>')) or re.findall(r'offer-tag[^>]*>([^<]+)<', b)
        acts[slug]=dict(slug=slug,name=name,go=go,score=score,price=(price or '').strip(),note=(note or '').strip(),desc=(desc or '').strip(),pts=[p.strip() for p in pts][:4])
    return acts

def head(title,desc,url,extra,cta_link):
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
<nav class="nav"></nav><div class="header-cta"><a href="{cta_link}" class="btn-primary">Voir le comparatif →</a></div>
</div></div></header>'''

def topcard(a):
    avis=f"/avis/{a['slug']}.html" if os.path.exists(f"avis/{a['slug']}.html") else a['go']
    pts="".join(f"<li>{html.escape(p)}</li>" for p in a['pts'])
    pricebox=f'<div class="tp-price">{html.escape(a["price"])}</div>' if a['price'] else ''
    return f'''<div class="offer-card top-pick">
        <div class="tp-rank">1</div>
        <div class="tp-logo"><img src="/assets/logos/{a['slug']}.png" alt="{html.escape(a['name'])}" loading="lazy"></div>
        <div class="tp-main"><div class="tp-name">{html.escape(a['name'])}</div>
          <div class="tp-tagline">{html.escape(a['desc'])}</div>
          <ul class="tp-checklist">{pts}</ul>
          <a class="tp-more" href="{avis}">En savoir plus →</a></div>
        <div class="tp-side"><div class="tp-score"><b>{a['score']}</b><span>/10</span><small>Note Selectum</small></div>
          {pricebox}
          <a class="btn-green tp-cta" href="{a['go']}" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
      </div>'''

def card(a,rank):
    tags="".join(f'<span class="offer-tag">{html.escape(p)}</span>' for p in a['pts'][:3])
    note=f'<span>{html.escape(a["note"])}</span>' if a['note'] else ''
    return f'''<div class="offer-card">
        <div class="offer-rank">{rank}</div>
        <div class="offer-logo brand"><img src="/assets/logos/{a['slug']}.png" alt="{html.escape(a['name'])}" loading="lazy"></div>
        <div class="offer-info"><div class="offer-name">{html.escape(a['name'])}</div>
          <div class="offer-desc">{html.escape(a['desc'])}</div><div class="offer-tags">{tags}</div></div>
        <div class="offer-score-mini"><b>{a['score']}</b><span>/10</span></div>
        <div class="offer-price">{html.escape(a['price'])}{note}</div>
        <a href="{a['go']}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a>
      </div>'''

def build(slug,title,desc,h1,intro,order,ACT,cat_label,cat_link,related):
    url=f"https://selectum.fr/comparatifs/{slug}.html"
    order=[s for s in order if s in ACT]
    if len(order)<2: return False
    cards=topcard(ACT[order[0]])+"".join(card(ACT[s],i+2) for i,s in enumerate(order[1:]))
    rows="".join(f"<tr><td><strong>{html.escape(ACT[s]['name'])}</strong></td><td>{html.escape(ACT[s]['price'])}</td><td>{ACT[s]['score']}/10</td></tr>" for s in order)
    qa=[(f"Quel est le meilleur choix pour « {h1.split(':')[0].strip().lower()} » ?",f"Notre n°1 est {ACT[order[0]]['name']}. Le bon choix dépend de votre profil et de vos besoins ; comparez les critères ci-dessus."),
        ("Comment avons-nous classé ces offres ?","Nous comparons le prix, les services, les conditions et les avis. Le classement reflète le meilleur rapport global pour cette recherche précise.")]
    ld_item=json.dumps({"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":ACT[s]['name']} for i,s in enumerate(order)]},ensure_ascii=False)
    ld_faq=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qa]},ensure_ascii=False)
    extra=f'\n<script type="application/ld+json">{ld_item}</script>\n<script type="application/ld+json">{ld_faq}</script>'
    faqhtml='<div class="faq"><h2>❓ Questions fréquentes</h2>'+''.join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in qa)+'</div>'
    rel="".join(f'<li><a href="{u}">{html.escape(t)} →</a></li>' for t,u in related)
    pagehtml=f'''{head(title,desc,url,extra,cat_link)}
<div class="article-header"><div class="container-article">
<div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="{cat_link}">{html.escape(cat_label)}</a><span>/</span>{html.escape(h1.split(':')[0].strip())}</div>
<h1>{html.escape(h1)}</h1><p class="updated">🗓️ Mis à jour le 11 juin 2026 — Analysé par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-layout" style="grid-template-columns:1fr 300px;"><main class="article-body">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
<div class="intro-box"><p>{html.escape(intro)}</p></div>
<h2 id="classement">🏆 Notre classement</h2>
<div class="offer-cards">{cards}</div>
<h2 id="tableau">Tableau comparatif</h2>
<div class="comparison-table-wrap"><table class="comparison-table"><thead><tr><th>Offre</th><th>Prix</th><th>Note</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2 id="choisir">Comment choisir ?</h2>
<p>Évaluez le prix, les services inclus, les conditions et la qualité du service client. Les tarifs affichés peuvent évoluer — vérifiez l'offre en cours avant de souscrire.</p>
{faqhtml}
<p style="margin-top:20px;">À lire aussi : <a href="{cat_link}">comparatif complet</a>.</p>
</main>
<aside class="sidebar">
<div class="sidebar-cta"><h4>🥇 Notre n°1</h4><p>{html.escape(ACT[order[0]]['name'])} — {html.escape(ACT[order[0]]['desc'])}</p><a href="{ACT[order[0]]['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
<div class="sidebar-card"><h4>🔗 Autres classements</h4><ul class="sidebar-toc">{rel}</ul></div>
</aside>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''
    open(f"comparatifs/{slug}.html","w").write(pagehtml); return True

print("lib verticals chargée")
