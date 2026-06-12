#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages code-promo + parrainage RICHES (SEO) pour les marques à liens d'affiliation.
Cible 'code promo X', 'parrainage X', 'avis X'. Honnête (pas de code/montant inventé)."""
import os, html, json

FONT = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D = "12 juin 2026"
ORG = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Selectum","url":"https://selectum.fr/","logo":"https://selectum.fr/assets/selectum-logo.png","description":"Comparatifs et avis indépendants : banque, bourse, crypto, assurance, crédit, énergie et logiciels."}</script>'
WS = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"Selectum","url":"https://selectum.fr/","inLanguage":"fr-FR"}</script>'

# slug, name, cat(breadcrumb), compar_url, compar_label, bonus_kind, alts[slug], risk, guide(bool)
BR = [
 ("xtb","XTB","Bourse","/comparatifs/trading-bourse.html","comparatif bourse",
  "offre de bienvenue (dont 0 % de commission sur les actions jusqu'à un certain seuil)",
  ["trade-republic","degiro","trading-212"],True,True),
 ("n26","N26","Banque","/comparatifs/banque-en-ligne.html","comparatif banque en ligne",
  "offre de bienvenue à l'ouverture du compte",["revolut","bunq","monabanq"],False,True),
 ("kraken","Kraken","Crypto","/comparatifs/crypto.html","comparatif crypto",
  "offre de bienvenue à l'inscription",["bitpanda","coinhouse","coinbase"],True,True),
 ("linxea","Linxea","Épargne","/comparatifs/assurance-vie.html","comparatif assurance-vie",
  "avantage à la souscription (0 % de frais d'entrée et offre éventuelle)",["nalo","yomoni","placement-direct"],True,True),
 ("sumup","SumUp","Paiement","/comparatifs/terminaux-paiement.html","comparatif des terminaux de paiement",
  "offre sur le lecteur de carte et l'inscription",["zettle","mypos","flatpay"],False,True),
 ("flatpay","Flatpay","Paiement","/comparatifs/terminaux-paiement.html","comparatif des terminaux de paiement",
  "offre sur l'abonnement et le matériel",["sumup","zettle","mypos"],False,True),
 ("expressvpn","ExpressVPN","Tech","/comparatifs/vpn.html","comparatif VPN",
  "réduction sur l'abonnement (mois offerts via le lien)",["nordvpn","surfshark","cyberghost"],False,True),
 ("adguard","AdGuard","Tech","/comparatifs/bloqueur-de-pub.html","comparatif bloqueur de pub",
  "réduction sur la licence AdGuard",["expressvpn","nordvpn","surfshark"],False,True),
 ("shopify","Shopify","E-commerce","/comparatifs/creer-boutique-en-ligne.html","comparatif création de boutique en ligne",
  "essai gratuit et offre de lancement",["bigcommerce","squarespace","wix"],False,True),
 ("santevet","SantéVet","Assurance","/comparatifs/assurance-animaux.html","comparatif assurance animaux",
  "offre de bienvenue (mois offert éventuel)",["dalma","assuropoil","lassie"],False,False),
 ("airwallex","Airwallex","Pro","/comparatifs/comptes-pro.html","comparatif comptes pro",
  "offre de bienvenue sur le compte pro",["qonto","shine","finom"],False,False),
 ("wallester","Wallester","Pro","/comparatifs/comptes-pro.html","comparatif comptes pro",
  "offre de bienvenue sur les cartes et le compte",["qonto","finom","blank"],False,False),
]

def head(url, title, desc, leaf, extra=""):
    t, d = html.escape(title), html.escape(desc)
    bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
        {"@type":"ListItem","position":2,"name":leaf.split(" — ")[0],"item":"https://selectum.fr/index.html"},
        {"@type":"ListItem","position":3,"name":leaf,"item":url}]},ensure_ascii=False)
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title><meta name="description" content="{d}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="article"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<meta name="twitter:card" content="summary">
{ORG}
{WS}
<script type="application/ld+json">{bc}</script>
{extra}</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="{{COMPAR}}" class="btn-primary">{{COMPARCTA}} →</a></div>
</div></div></header>'''

FOOT = '''<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a> · <a href="/methodologie.html" style="color:var(--gray-500)">Méthodologie</a></p>
</div></div></footer>
<script src="/assets/site.js" defer></script>
</body></html>'''

def faq_ld(faq):
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)

def alts_html(alts, kind):
    out=[]
    for a in alts:
        if os.path.exists(f"{kind}/{a}.html"):
            label = a.replace("-"," ").title()
            out.append(f'<li><a href="/{kind}/{a}.html">{"Code promo" if kind=="code-promo" else "Parrainage"} {html.escape(label)}</a></li>')
    return "".join(out)

def risk_box(risk):
    return ('<div class="affiliate-notice" style="margin-top:14px;">⚠️ <strong>Risques :</strong> investir comporte un risque de perte en capital. Les performances passées ne préjugent pas des performances futures.</div>') if risk else ""

def gen_codepromo(slug,name,cat,compar,compar_label,bonus,alts,risk,has_guide):
    n=html.escape(name); url=f"https://selectum.fr/code-promo/{slug}.html"
    title=f"Code promo {name} 2026 : offre de bienvenue & parrainage (vérifié)"
    desc=f"Code promo {name} 2026 : existe-t-il un code de réduction ? Comment activer l'offre de bienvenue et le parrainage {name}, étape par étape. Vérifié par Selectum."
    guide_link=f'<a href="/guides/{slug}.html">guide {n}</a>' if has_guide else f'<a href="/avis/{slug}.html">avis {n}</a>'
    faq=[(f"Existe-t-il un code promo {name} en 2026 ?", f"{name} fonctionne surtout par une {bonus}, activée via un lien plutôt qu'un code à recopier. Le détail évolue : seules les conditions officielles {name} font foi."),
         (f"Comment obtenir l'offre {name} ?", f"Accédez à l'offre via le lien, créez votre compte {name}, puis suivez les étapes (vérification, première action éventuelle). L'avantage est appliqué selon les conditions en vigueur."),
         (f"Le code promo {name} est-il gratuit ?", f"Oui, activer l'offre {name} est gratuit. Vous ne réglez que les éventuels frais habituels du service {name}."),
         (f"Faut-il un code de parrainage {name} ?", f"Le parrainage {name} s'active en général via un lien dédié plutôt qu'un code à saisir. Voir notre page parrainage {name}."),
         (f"L'offre {name} est-elle limitée dans le temps ?", f"Oui, les offres évoluent selon les périodes. L'offre présentée a été vérifiée le {D} ; vérifiez les conditions à jour sur le site {name}.")]
    art=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
        "author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},
        "datePublished":"2026-01-15","dateModified":"2026-06-12","mainEntityOfPage":url},ensure_ascii=False)
    howto=json.dumps({"@context":"https://schema.org","@type":"HowTo","name":f"Comment obtenir l'offre {name}","step":[
        {"@type":"HowToStep","position":1,"name":"Ouvrir l'offre","text":f"Cliquez sur « Révéler l'offre {name} » pour accéder à l'offre en cours."},
        {"@type":"HowToStep","position":2,"name":"Créer son compte","text":f"Inscrivez-vous sur {name} et finalisez la vérification demandée."},
        {"@type":"HowToStep","position":3,"name":"Remplir la condition","text":"Réalisez l'action éventuellement requise par l'offre (premier achat, dépôt, abonnement…)."},
        {"@type":"HowToStep","position":4,"name":"Recevoir l'avantage","text":f"L'avantage est appliqué selon les conditions {name} en vigueur."}]},ensure_ascii=False)
    extra=f'<script type="application/ld+json">{art}</script>\n<script type="application/ld+json">{howto}</script>\n<script type="application/ld+json">{faq_ld(faq)}</script>\n'
    h=head(url,title,desc,f"Code promo {name}",extra).replace("{COMPAR}",compar).replace("{COMPARCTA}",html.escape(compar_label.capitalize()))
    altl=alts_html(alts,"code-promo")
    faqh="".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)
    body=f'''<div class="brand-hero"><div class="container-article">
  <div class="brand-hero-logo"><img src="/assets/logos/{slug}.png" alt="{n}" width="96" height="96" style="max-width:100%;max-height:100%;object-fit:contain;"></div>
  <div class="brand-hero-text">
    <div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / <a href="{compar}" style="color:rgba(255,255,255,.8)">{html.escape(cat)}</a> / Code promo {n}</div>
    <h1>Code promo {n} 2026 : offre de bienvenue &amp; parrainage</h1>
    <p class="subtitle">Existe-t-il un code promo {n} ? Comment activer l'offre, étape par étape — vérifié ce mois-ci.</p>
    <p class="updated">🗓️ Mis à jour le {D} — vérifié par notre équipe</p>
  </div></div></div>
<div class="container-article"><div class="article-layout" style="grid-template-columns: 1fr 300px;"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
  <div class="intro-box"><p>Vous cherchez un <strong>code promo {n}</strong> ? Soyons clairs : {n} fonctionne surtout par une <strong>{html.escape(bonus)}</strong> qui s'active via un lien, le plus souvent <strong>sans code à recopier</strong>. On vous explique exactement ce qui existe et comment en profiter.</p></div>
  <div class="promo-box"><span class="promo-badge">🎁 Offre {n}</span>
    <h3>L'offre {n} du moment</h3>
    <p>Profitez de l'offre {n} en passant par notre lien : elle s'applique automatiquement.</p>
    <div class="promo-reveal"><div class="promo-code">OFFRE EN COURS</div>
    <a href="/go/{slug}" class="promo-btn" target="_blank" rel="sponsored nofollow noopener">Révéler l'offre {n}</a></div>
    <p class="promo-note">Offre soumise aux conditions {n}, variable selon les périodes — vérifiée le {D}.</p>
  </div>
  <h2 id="existe">Existe-t-il vraiment un code promo {n} ?</h2>
  <p>La réponse honnête : {n} ne distribue pas de « code de réduction » classique à coller dans un champ. L'avantage prend la forme d'une <strong>{html.escape(bonus)}</strong>, activée via un lien. Méfiez-vous des sites qui promettent un code {n} avec un montant garanti : les conditions évoluent et <strong>seul le site officiel fait foi</strong>.</p>
  <h2 id="obtenir">Comment activer l'offre {n} (étape par étape)</h2>
  <ol>
    <li><strong>Ouvrez l'offre</strong> en cliquant sur « Révéler l'offre {n} » ci-dessus.</li>
    <li><strong>Créez votre compte</strong> {n} et finalisez la vérification demandée.</li>
    <li><strong>Remplissez la condition</strong> éventuelle (premier achat, dépôt, abonnement…), si elle est requise.</li>
    <li><strong>Recevez l'avantage</strong>, appliqué selon les conditions {n} en vigueur.</li>
  </ol>
  <div class="highlight-box"><p>💡 Pensez aussi au <a href="/parrainage/{slug}.html">parrainage {n}</a> et lisez notre {guide_link} et notre <a href="/avis/{slug}.html">avis {n}</a> avant de souscrire.</p></div>
  <h2 id="alternatives">Code promo {n} : les alternatives à comparer</h2>
  <p>Avant de choisir, comparez l'offre {n} avec les autres acteurs :</p>
  <ul>{altl}<li><a href="{compar}">{html.escape(compar_label.capitalize())}</a></li></ul>
  {risk_box(risk)}
  <div class="faq"><h2>❓ Questions fréquentes sur le code promo {n}</h2>{faqh}</div>
  <div class="rel-links"><h2>À lire aussi sur {n}</h2><div class="rel-list"><a href="/avis/{slug}.html" class="rel-chip">Avis {n} →</a><a href="/parrainage/{slug}.html" class="rel-chip">Parrainage {n} →</a>{('<a href="/guides/'+slug+'.html" class="rel-chip">Guide '+n+' →</a>') if has_guide else ''}<a href="{compar}" class="rel-chip">{html.escape(compar_label.capitalize())} →</a></div></div>
</main>
<aside class="sidebar">
  <div class="sidebar-cta"><h4>👉 {n}</h4><p>Activez l'offre {n} du moment.</p><a href="/go/{slug}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
  <div class="sidebar-card"><h4>🔗 Sur {n}</h4><ul class="sidebar-toc"><li><a href="/avis/{slug}.html">Avis {n} →</a></li><li><a href="/parrainage/{slug}.html">Parrainage {n} →</a></li>{('<li><a href="/guides/'+slug+'.html">Guide '+n+' →</a></li>') if has_guide else ''}<li><a href="{compar}">{html.escape(compar_label.capitalize())} →</a></li></ul></div>
</aside></div></div>'''
    open(f"code-promo/{slug}.html","w",encoding="utf-8").write(h+body+FOOT)

def gen_parrainage(slug,name,cat,compar,compar_label,bonus,alts,risk,has_guide):
    n=html.escape(name); url=f"https://selectum.fr/parrainage/{slug}.html"
    title=f"Parrainage {name} 2026 : prime, lien et conditions (vérifié)"
    desc=f"Parrainage {name} 2026 : comment être parrainé, prime de bienvenue, lien et conditions. Le guide complet du parrainage {name}, vérifié par Selectum."
    faq=[(f"Comment fonctionne le parrainage {name} ?", f"Le filleul s'inscrit via un lien de parrainage {name} et réalise l'action demandée ; le parrain et le filleul peuvent recevoir un avantage selon les conditions {name}."),
         (f"Quelle prime de parrainage chez {name} ?", f"Le montant évolue régulièrement. La voie la plus simple est l'{bonus} accessible via notre lien ; vérifiez les conditions à jour sur le site {name}."),
         (f"Faut-il un code de parrainage {name} ?", f"En général, le parrainage {name} s'active via un lien dédié plutôt qu'un code à saisir."),
         (f"Le parrainage {name} est-il cumulable avec une autre offre ?", f"Les règles de cumul dépendent de {name} ; consultez les conditions officielles avant de souscrire.")]
    art=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
        "author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},
        "datePublished":"2026-01-15","dateModified":"2026-06-12","mainEntityOfPage":url},ensure_ascii=False)
    extra=f'<script type="application/ld+json">{art}</script>\n<script type="application/ld+json">{faq_ld(faq)}</script>\n'
    h=head(url,title,desc,f"Parrainage {name}",extra).replace("{COMPAR}",compar).replace("{COMPARCTA}",html.escape(compar_label.capitalize()))
    altl=alts_html(alts,"parrainage")
    faqh="".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)
    body=f'''<div class="brand-hero"><div class="container-article">
  <div class="brand-hero-logo"><img src="/assets/logos/{slug}.png" alt="{n}" width="96" height="96" style="max-width:100%;max-height:100%;object-fit:contain;"></div>
  <div class="brand-hero-text">
    <div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / <a href="{compar}" style="color:rgba(255,255,255,.8)">{html.escape(cat)}</a> / Parrainage {n}</div>
    <h1>Parrainage {n} 2026 : prime, lien &amp; conditions</h1>
    <p class="subtitle">Comment être parrainé chez {n} et profiter de l'offre de bienvenue — vérifié ce mois-ci.</p>
    <p class="updated">🗓️ Mis à jour le {D} — vérifié par notre équipe</p>
  </div></div></div>
<div class="container-article"><div class="article-layout" style="grid-template-columns: 1fr 300px;"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
  <div class="intro-box"><p>Vous cherchez un <strong>parrainage {n}</strong> pour profiter de l'offre de bienvenue ? Voici comment ça marche et comment l'activer simplement, sans forcément de code à recopier.</p></div>
  <div class="promo-box"><span class="promo-badge">🎁 Offre de bienvenue {n}</span>
    <h3>Être parrainé chez {n}</h3>
    <p>La façon la plus simple de profiter de l'avantage de bienvenue est de passer par l'offre en cours :</p>
    <div class="promo-reveal"><div class="promo-code">OFFRE EN COURS</div>
    <a href="/go/{slug}" class="promo-btn" target="_blank" rel="sponsored nofollow noopener">Révéler l'offre {n}</a></div>
    <p class="promo-note">Conditions {n} susceptibles d'évoluer — vérifiées le {D}.</p>
  </div>
  <h2 id="fonctionnement">Comment fonctionne le parrainage {n} ?</h2>
  <p>Le principe : un <strong>filleul</strong> s'inscrit via un lien de parrainage {n} et réalise l'action demandée. Le <strong>parrain</strong> et le <strong>filleul</strong> peuvent alors recevoir un avantage, selon les conditions {n} en vigueur. Le plus souvent, tout se joue via le lien — <strong>sans code à saisir</strong>.</p>
  <h2 id="etapes">Profiter du parrainage {n} en 3 étapes</h2>
  <ol>
    <li><strong>Ouvrez l'offre</strong> via « Révéler l'offre {n} » ci-dessus.</li>
    <li><strong>Inscrivez-vous</strong> sur {n} et finalisez la vérification.</li>
    <li><strong>Réalisez la condition</strong> (premier achat, dépôt, abonnement…) pour débloquer l'avantage.</li>
  </ol>
  <div class="highlight-box"><p>💡 Voir aussi le <a href="/code-promo/{slug}.html">code promo {n}</a> et notre <a href="/avis/{slug}.html">avis {n}</a>.</p></div>
  <h2 id="alternatives">Parrainage {n} : les alternatives</h2>
  <ul>{altl}<li><a href="{compar}">{html.escape(compar_label.capitalize())}</a></li></ul>
  {risk_box(risk)}
  <div class="faq"><h2>❓ Questions fréquentes sur le parrainage {n}</h2>{faqh}</div>
  <div class="rel-links"><h2>À lire aussi sur {n}</h2><div class="rel-list"><a href="/code-promo/{slug}.html" class="rel-chip">Code promo {n} →</a><a href="/avis/{slug}.html" class="rel-chip">Avis {n} →</a>{('<a href="/guides/'+slug+'.html" class="rel-chip">Guide '+n+' →</a>') if has_guide else ''}<a href="{compar}" class="rel-chip">{html.escape(compar_label.capitalize())} →</a></div></div>
</main>
<aside class="sidebar">
  <div class="sidebar-cta"><h4>👉 {n}</h4><p>Profitez de l'offre {n} du moment.</p><a href="/go/{slug}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
  <div class="sidebar-card"><h4>🔗 Sur {n}</h4><ul class="sidebar-toc"><li><a href="/code-promo/{slug}.html">Code promo {n} →</a></li><li><a href="/avis/{slug}.html">Avis {n} →</a></li>{('<li><a href="/guides/'+slug+'.html">Guide '+n+' →</a></li>') if has_guide else ''}<li><a href="{compar}">{html.escape(compar_label.capitalize())} →</a></li></ul></div>
</aside></div></div>'''
    open(f"parrainage/{slug}.html","w",encoding="utf-8").write(h+body+FOOT)

for slug,name,cat,compar,compar_label,bonus,alts,risk,has_guide in BR:
    gen_codepromo(slug,name,cat,compar,compar_label,bonus,alts,risk,has_guide)
    gen_parrainage(slug,name,cat,compar,compar_label,bonus,alts,risk,has_guide)
print("pages riches générées :", len(BR)*2, "(code-promo + parrainage pour", len(BR), "marques affiliées)")
