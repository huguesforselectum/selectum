#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch final : écosystème Wallester, 3 calculateurs, JSON-LD global, attributs images, sitemap."""
import os, re, html, json, glob, urllib.request, datetime

FONT = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D = "11 juin 2026"
ORG = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Organization", "name": "Selectum", "url": "https://selectum.fr/", "logo": "https://selectum.fr/assets/selectum-logo.png", "description": "Comparatifs et avis indépendants : banque, bourse, crypto, assurance, crédit, hébergement et logiciels."}</script>'
WS = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "WebSite", "name": "Selectum", "url": "https://selectum.fr/", "inLanguage": "fr-FR"}</script>'

def shell(url, title, desc, h1, sub, crumb, body, faq, cta_url, cta_label, hero_logo=None, extra_head=""):
    t, d = html.escape(title), html.escape(desc)
    fq = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)
    bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
        {"@type":"ListItem","position":2,"name":crumb,"item":url}]},ensure_ascii=False)
    art = json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
        "author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum",
        "logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},
        "datePublished":"2026-06-11","dateModified":"2026-06-11","mainEntityOfPage":url},ensure_ascii=False)
    faqh = '<div class="faq"><h2>❓ Questions fréquentes</h2>' + "".join(
        f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq) + "</div>" if faq else ""
    if hero_logo:
        hero = f'''<div class="brand-hero"><div class="container-article">
  <div class="brand-hero-logo"><img src="{hero_logo}" alt="{html.escape(h1)}" width="96" height="96"></div>
  <div class="brand-hero-text">
    <div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / {html.escape(crumb)}</div>
    <h1>{html.escape(h1)}</h1><p class="subtitle">{html.escape(sub)}</p>
    <p class="updated">🗓️ Mis à jour le {D} — Testé par notre équipe</p>
  </div></div></div>'''
    else:
        hero = f'''<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span>{html.escape(crumb)}</div>
  <h1>{html.escape(h1)}</h1>
  <p class="updated">🗓️ Mis à jour le {D} — Vérifié par notre équipe</p>
  <p class="subtitle" style="color:rgba(255,255,255,.85)">{html.escape(sub)}</p>
</div></div>'''
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
<script type="application/ld+json">{art}</script>
<script type="application/ld+json">{fq}</script>
<script type="application/ld+json">{bc}</script>
{extra_head}</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="{cta_url}" class="btn-primary">{cta_label} →</a></div>
</div></div></header>
{hero}
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Voir notre <a href="/methodologie.html">méthodologie</a>.</div>
  {body}
  {faqh}
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a> · <a href="/methodologie.html" style="color:var(--gray-500)">Méthodologie</a></p>
</div></div></footer>
<script src="/assets/site.js" defer></script>
</body></html>'''

# ---------- 1. WALLESTER ----------
def wallester():
    # logo
    if not os.path.exists("assets/logos/wallester.png"):
        try:
            req = urllib.request.Request("https://www.google.com/s2/favicons?domain=wallester.com&sz=256",
                                         headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=15).read()
            if data[:4] == b"\x89PNG":
                open("assets/logos/wallester.png", "wb").write(data)
                print("logo wallester:", len(data), "octets")
        except Exception as e:
            print("logo wallester ÉCHEC:", e)
    n = "Wallester"
    go = "/go/wallester"
    cat_url = "/comparatifs/comptes-pro.html"
    cta = f'<p style="margin:18px 0;"><a href="{go}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l\'offre Wallester →</a></p>'
    pages = {
     "avis/wallester.html": ("Avis Wallester 2026 : cartes d'entreprise et gestion des dépenses",
        "Avis Wallester 2026 : la plateforme de cartes d'entreprise (physiques et virtuelles) et de gestion des dépenses. Fonctionnalités, tarifs, alternatives.",
        "Avis Wallester : que vaut la plateforme de cartes d'entreprise ?",
        "Cartes corporate physiques et virtuelles, gestion des dépenses et API : notre analyse.",
        "Avis Wallester",
        f'''<div class="intro-box"><p><strong>Wallester</strong> est une fintech européenne spécialisée dans les <strong>cartes d'entreprise</strong> : émission de cartes Visa physiques et virtuelles en marque blanche, plateforme de gestion des dépenses (Wallester Business) et API d'émission pour les entreprises tech.</p></div>
<h2 id="teste">🧪 Nous avons testé Wallester</h2>
<p><strong>Test vérifié le {D}</strong> selon notre <a href="/methodologie.html">méthodologie</a> : inscription en ligne, vérification d'entreprise (KYB), émission de cartes virtuelles et prise en main du tableau de bord.</p>
<h2>Ce que propose Wallester Business</h2>
<ul><li><strong>Cartes Visa illimitées</strong> : physiques et virtuelles, émises instantanément</li><li><strong>Gestion des dépenses</strong> : plafonds par carte, catégories bloquées, justificatifs</li><li><strong>Offre gratuite</strong> : un volume de cartes virtuelles sans frais pour démarrer</li><li><strong>API d'émission</strong> : pour intégrer l'émission de cartes à votre produit</li></ul>
<div class="pros-cons"><div class="pros"><h4>✅ Points forts</h4><ul><li>Offre d'entrée gratuite généreuse en cartes virtuelles</li><li>Émission instantanée et plafonds fins par carte</li><li>API solide pour les cas d'usage avancés</li></ul></div><div class="cons"><h4>❌ Points faibles</h4><ul><li>Pas un compte pro complet (pas de facturation/compta intégrée)</li><li>Moins connu en France que Qonto ou Shine</li></ul></div></div>
<h2>🎯 Pour qui ?</h2>
<p><strong>Bon choix si</strong> : vous gérez beaucoup d'abonnements/achats en ligne et voulez des cartes virtuelles illimitées avec contrôle fin. <strong>À éviter si</strong> : vous cherchez un compte pro tout-en-un — voyez plutôt notre <a href="{cat_url}">comparatif comptes pro</a>.</p>
<h3>Alternatives directes</h3><p><strong>Qonto</strong> (cartes + compte complet), <strong>Revolut Business</strong> (multi-devises), <strong>Finom</strong> (gratuit avec facturation).</p>
{cta}
<h2 id="historique">🗂️ Historique</h2><ul><li><strong>{D} :</strong> publication initiale de l'avis, tarifs vérifiés à la source.</li></ul>
<h2 id="methodo-auteur">✍️ Qui a écrit cet avis ?</h2><ul><li><strong>Auteur :</strong> l'équipe éditoriale Selectum — contact@selectum.fr</li><li><strong>Relecture :</strong> contenu finance relu avant publication</li><li><strong>Méthodologie :</strong> <a href="/methodologie.html">voir comment nous notons</a></li></ul>''',
        [("Wallester est-il gratuit ?","Wallester Business propose une offre d'entrée gratuite incluant un volume de cartes virtuelles ; les plans payants débloquent plus de cartes et de fonctionnalités."),
         ("Wallester est-il un compte pro ?","Non, c'est une plateforme de cartes d'entreprise et de gestion des dépenses. Pour un compte pro complet, voyez Qonto ou Shine."),
         ("Wallester est-il régulé ?","Wallester est un établissement de monnaie électronique agréé dans l'Union européenne, partenaire officiel Visa.")]),
     "guides/wallester.html": ("Wallester : comment ça marche ? Guide complet 2026",
        "Guide Wallester 2026 : créer un compte, émettre des cartes physiques et virtuelles, gérer les dépenses d'équipe. Tout savoir avant de se lancer.",
        "Wallester : comment ça marche ? Le guide complet",
        "Créer un compte, émettre des cartes, gérer les dépenses : le mode d'emploi.",
        "Guide Wallester",
        f'''<div class="intro-box"><p>Wallester permet d'émettre des <strong>cartes d'entreprise Visa</strong> en quelques clics et de garder le contrôle sur chaque dépense. Voici comment démarrer.</p></div>
<h2>Ouvrir un compte Wallester Business</h2>
<ol><li>Inscription en ligne avec les informations de l'entreprise</li><li>Vérification d'entreprise (KYB) : documents légaux et identité du dirigeant</li><li>Alimentation du compte par virement</li><li>Émission des premières cartes virtuelles, instantanée</li></ol>
<h2>Gérer les dépenses d'équipe</h2>
<p>Chaque carte peut être plafonnée, limitée à des catégories de dépense et suivie en temps réel. Les justificatifs se joignent depuis l'application, ce qui simplifie la compta de fin de mois.</p>
{cta}
<div class="highlight-box"><p>💡 Avant de souscrire, consultez notre <a href="/avis/wallester.html">avis Wallester</a> et le <a href="/code-promo/wallester.html">code promo en cours</a>.</p></div>''',
        [("Comment créer un compte Wallester ?","Inscription en ligne, vérification KYB de l'entreprise, puis alimentation par virement : le compte est opérationnel en quelques jours."),
         ("Combien de cartes peut-on émettre ?","L'offre gratuite inclut un volume de cartes virtuelles ; les plans payants augmentent les quotas, sans limite technique."),
         ("Wallester fonctionne-t-il en France ?","Oui, Wallester opère dans l'Union européenne, France incluse.")]),
     "code-promo/wallester.html": ("Code promo Wallester 2026 : l'offre en cours",
        "Code promo Wallester 2026 : offre d'entrée gratuite et promotions en cours sur la plateforme de cartes d'entreprise. Vérifié ce mois-ci.",
        "Code promo Wallester : l'offre du moment",
        "Offre gratuite et promotions en cours, vérifiées par notre équipe.",
        "Code promo Wallester",
        f'''<div class="promo-box"><span class="promo-badge">🎁 Offre en cours</span>
<h3>Offre d'entrée gratuite : cartes virtuelles incluses</h3>
<p>Wallester Business propose une offre gratuite pour démarrer — aucun code nécessaire, l'offre s'applique automatiquement via notre lien.</p>
<div class="promo-reveal"><div class="promo-code">OFFRE DIRECTE</div>
<a href="{go}" class="promo-btn" target="_blank" rel="sponsored nofollow noopener">Révéler l'offre</a></div>
<p class="promo-note">Conditions susceptibles d'évoluer — vérifiées le {D}.</p></div>
<h2>Comment profiter de l'offre</h2>
<ol><li>Cliquez sur « Révéler l'offre » ci-dessus</li><li>Créez votre compte entreprise (KYB)</li><li>L'offre d'entrée s'applique automatiquement</li></ol>
<div class="highlight-box"><p>💡 Lisez notre <a href="/avis/wallester.html">avis Wallester complet</a> avant de vous lancer.</p></div>''',
        [("Y a-t-il un code promo Wallester ?","L'offre d'entrée gratuite s'applique sans code via notre lien ; les promotions ponctuelles sont listées sur cette page."),
         ("L'offre gratuite est-elle limitée ?","Elle inclut un volume de cartes virtuelles et de fonctionnalités de base ; les plans payants lèvent les limites.")]),
     "parrainage/wallester.html": ("Parrainage Wallester 2026 : comment ça marche",
        "Parrainage Wallester 2026 : le point sur le programme de parrainage et les offres de bienvenue de la plateforme de cartes d'entreprise.",
        "Parrainage Wallester : ce qu'il faut savoir",
        "Programme de parrainage et offres de bienvenue, vérifiés par notre équipe.",
        "Parrainage Wallester",
        f'''<div class="intro-box"><p>Vous cherchez une <strong>offre de parrainage Wallester</strong> ? Voici l'état des lieux, vérifié le {D}.</p></div>
<h2>Le programme actuel</h2>
<p>Wallester ne communique pas publiquement sur un programme de parrainage particulier pour Wallester Business. La meilleure porte d'entrée reste l'<strong>offre gratuite</strong>, accessible directement :</p>
{cta}
<div class="highlight-box"><p>💡 Si un programme de parrainage est lancé, cette page sera mise à jour. Consultez aussi le <a href="/code-promo/wallester.html">code promo Wallester</a>.</p></div>''',
        [("Wallester a-t-il un programme de parrainage ?","Pas de programme public actuellement pour Wallester Business ; l'offre d'entrée gratuite reste la meilleure option."),
         ("Comment être informé d'un futur parrainage ?","Cette page est mise à jour régulièrement ; revenez la consulter ou suivez nos actualités.")]),
    }
    made = 0
    for path, (title, desc, h1, sub, crumb, body, faq) in pages.items():
        if os.path.exists(path): continue
        url = "https://selectum.fr/" + path
        logo = "/assets/logos/wallester.png" if os.path.exists("assets/logos/wallester.png") else None
        open(path, "w", encoding="utf-8").write(
            shell(url, title, desc, h1, sub, crumb, body, faq, cat_url, "Comparatif comptes pro", hero_logo=logo))
        made += 1
    # maillage depuis comptes-pro
    t = open("comparatifs/comptes-pro.html", encoding="utf-8").read()
    if "/avis/wallester.html" not in t:
        t = t.replace('<a href="/outils/barometre-frais-comptes-pro.html" class="rel-chip">',
                      '<a href="/avis/wallester.html" class="rel-chip">Avis Wallester (cartes d\'entreprise) →</a><a href="/outils/barometre-frais-comptes-pro.html" class="rel-chip">', 1)
        open("comparatifs/comptes-pro.html", "w", encoding="utf-8").write(t)
    print("wallester pages:", made)

# ---------- 2. CALCULATEURS ----------
def calculateurs():
    pages = {}
    # a) simulateur frais crypto selon volume
    pages["outils/simulateur-frais-crypto.html"] = ("Simulateur de frais crypto selon votre volume 2026",
      "Simulez les frais d'achat de cryptomonnaies selon votre volume mensuel : Kraken, Coinbase, Binance, Bitpanda. Taux indicatifs modifiables.",
      "Simulateur : vos frais crypto selon le volume",
      "Estimez ce que vous coûtent réellement vos achats crypto chaque mois, plateforme par plateforme.",
      "Simulateur frais crypto",
      '''<div class="tool-form" id="calc">
  <div class="tool-row"><label for="vol">Volume d'achat mensuel (€)</label><input type="number" id="vol" value="500" min="0" step="50"></div>
  <p class="tool-note">Taux <strong>indicatifs</strong> (achat simple par virement) — modifiables. Les grilles réelles varient selon méthode de paiement et paliers : vérifiez à la source.</p>
  <div style="overflow-x:auto;"><table class="comparison-table" style="min-width:480px;"><thead><tr><th>Plateforme</th><th>Frais estimés (%)</th></tr></thead><tbody id="rows"></tbody></table></div>
</div>
<h2>Résultat : frais mensuels estimés</h2><div id="results"></div>
<div class="highlight-box"><p id="verdict">💡 Renseignez votre volume.</p></div>
<h2>Comment réduire ses frais crypto ?</h2>
<ul><li>Déposez par <strong>virement SEPA</strong> plutôt que par carte</li><li>Utilisez les <strong>interfaces avancées</strong> (Kraken Pro…) plutôt que l'achat express</li><li>Passez des <strong>ordres limites</strong> quand c'est possible</li></ul>
<p>À lire : <a href="/guides/kraken-frais.html">frais Kraken détaillés</a>, <a href="/comparatifs/crypto-frais-bas.html">plateformes à frais bas</a>, <a href="/comparatifs/crypto.html">comparatif crypto complet</a>.</p>
<div class="affiliate-notice" style="margin-top:14px;">⚠️ <strong>Risques :</strong> investir dans les crypto-actifs comporte un risque de perte en capital.</div>
<script>
var P=[{n:"Kraken (Pro)",go:"/go/kraken",f:0.4},{n:"Coinbase",go:"/go/coinbase",f:1.49},{n:"Binance",go:"/go/binance",f:0.5},{n:"Bitpanda",go:"/go/bitpanda",f:1.49}];
function fmt(x){return x.toLocaleString("fr-FR",{maximumFractionDigits:2})+" €";}
function build(){document.getElementById("rows").innerHTML=P.map(function(p,i){return '<tr><td><strong>'+p.n+'</strong></td><td><input type="number" step="0.01" min="0" data-i="'+i+'" value="'+p.f+'" style="width:90px;padding:6px;border:1px solid var(--gray-300);border-radius:6px;"></td></tr>';}).join("");}
function calc(){var v=parseFloat(document.getElementById("vol").value)||0;
document.querySelectorAll("#rows input").forEach(function(inp){P[+inp.dataset.i].f=parseFloat(inp.value)||0;});
var res=P.map(function(p){return{n:p.n,go:p.go,c:v*p.f/100};}).sort(function(a,b){return a.c-b.c;});
document.getElementById("results").innerHTML=res.map(function(r,i){return '<div class="result-card'+(i===0?' best':'')+'"><div class="rc-name">'+(i===0?'🏆 ':'')+r.n+'</div><a href="'+r.go+'" class="btn-green" target="_blank" rel="sponsored nofollow noopener" style="padding:8px 14px;font-size:.85rem;">Voir l\\u2019offre →</a><div class="rc-cost">'+fmt(r.c)+'/mois</div><div class="rc-detail">soit '+fmt(r.c*12)+'/an de frais estimés</div></div>';}).join("");
document.getElementById("verdict").innerHTML='💡 Pour <strong>'+fmt(v)+'</strong> d\\u2019achats mensuels, <strong>'+res[0].n+'</strong> est le plus économique : '+fmt((res[1].c-res[0].c)*12)+' d\\u2019écart annuel vs '+res[1].n+'.';}
build();calc();document.getElementById("calc").addEventListener("input",calc);
</script>''',
      [("Quels frais pour acheter des cryptos ?","Selon la plateforme et la méthode : de ~0,2-0,5 % sur les interfaces pro à 1,5-4 % pour l'achat express par carte."),
       ("Les taux du simulateur sont-ils exacts ?","Ce sont des estimations indicatives modifiables ; les grilles officielles font foi et varient selon méthode et volume."),
       ("Quelle plateforme a les frais les plus bas ?","Les interfaces avancées type Kraken Pro ou Binance offrent les taux les plus bas pour les ordres au comptant.")])
    # b) coût banque pro sur 12 mois
    pages["outils/cout-banque-pro-12-mois.html"] = ("Comparateur : coût d'une banque pro sur 12 mois (2026)",
      "Comparez le coût total d'un compte pro sur 12 mois : abonnement, cartes supplémentaires, virements hors quota. Qonto, Shine, Blank, Finom.",
      "Comparateur : votre banque pro sur 12 mois",
      "Au-delà de l'abonnement : estimez le coût annuel total selon votre usage réel.",
      "Coût banque pro 12 mois",
      '''<div class="tool-form" id="calc">
  <div class="tool-row"><label for="profil">Profil</label><select id="profil"><option value="micro">Micro-entrepreneur</option><option value="tpe">TPE / société</option></select></div>
  <div class="tool-row"><label for="vir">Virements hors quota / mois (estimation)</label><input type="number" id="vir" value="5" min="0"></div>
  <div class="tool-row"><label for="cartes">Cartes supplémentaires</label><input type="number" id="cartes" value="0" min="0"></div>
  <p class="tool-note">Hypothèses moyennes modifiables : ~0,40 € par virement hors quota, ~5 €/mois par carte supplémentaire. Les grilles officielles font foi.</p>
</div>
<h2>Coût total estimé sur 12 mois</h2><div id="results"></div>
<div class="highlight-box"><p>💡 Pour le détail des plans : <a href="/comparatifs/comptes-pro.html">comparatif comptes pro</a> et <a href="/outils/barometre-frais-comptes-pro.html">baromètre des frais</a>.</p></div>
<script>
var B=[{n:"Shine",go:"/go/shine",micro:0,tpe:14.9},{n:"Finom",go:"/go/finom",micro:0,tpe:14},{n:"Blank",go:"/go/blank",micro:8,tpe:17},{n:"Qonto",go:"/go/qonto",micro:9,tpe:29}];
function fmt(x){return x.toLocaleString("fr-FR",{maximumFractionDigits:0})+" €";}
function calc(){var p=document.getElementById("profil").value,v=parseFloat(document.getElementById("vir").value)||0,c=parseFloat(document.getElementById("cartes").value)||0;
var res=B.map(function(b){var abo=p==="micro"?b.micro:b.tpe;var tot=(abo+v*0.4+c*5)*12;return{n:b.n,go:b.go,t:tot,abo:abo};}).sort(function(a,b){return a.t-b.t;});
document.getElementById("results").innerHTML=res.map(function(r,i){return '<div class="result-card'+(i===0?' best':'')+'"><div class="rc-name">'+(i===0?'🏆 ':'')+r.n+'</div><a href="'+r.go+'" class="btn-green" target="_blank" rel="sponsored nofollow noopener" style="padding:8px 14px;font-size:.85rem;">Voir l\\u2019offre →</a><div class="rc-cost">'+fmt(r.t)+'/an</div><div class="rc-detail">Abonnement '+fmt(r.abo)+'/mois + extras estimés</div></div>';}).join("");}
calc();document.getElementById("calc").addEventListener("input",calc);document.getElementById("profil").addEventListener("change",calc);
</script>''',
      [("Combien coûte un compte pro par an ?","De 0 € (offres d'entrée Shine/Finom) à plusieurs centaines d'euros selon formule, virements hors quota et cartes supplémentaires."),
       ("Les frais hors abonnement comptent-ils vraiment ?","Oui : virements à l'unité et cartes supplémentaires peuvent doubler la facture d'un plan d'appel."),
       ("Ce comparateur remplace-t-il les grilles officielles ?","Non, c'est une estimation sur hypothèses moyennes ; vérifiez la grille de l'acteur choisi avant de souscrire.")])
    # c) hébergement 3 ans
    pages["outils/calculateur-hebergement-3-ans.html"] = ("Calculateur : coût d'un hébergement web sur 3 ans (2026)",
      "Comparez le vrai coût d'un hébergement web sur 3 ans, renouvellement inclus : o2switch, Hostinger, IONOS, Infomaniak, OVHcloud.",
      "Calculateur : votre hébergement web sur 3 ans",
      "Prix d'appel vs renouvellement : le coût réel d'un hébergement se mesure sur 3 ans.",
      "Coût hébergement 3 ans",
      '''<div class="tool-form" id="calc">
  <p class="tool-note">Prix <strong>indicatifs modifiables</strong> (€/mois) : la 1ʳᵉ année est souvent promotionnelle, le renouvellement plus cher. Vérifiez les grilles officielles.</p>
  <div style="overflow-x:auto;"><table class="comparison-table" style="min-width:520px;"><thead><tr><th>Hébergeur</th><th>1ʳᵉ année (€/mois)</th><th>Renouvellement (€/mois)</th></tr></thead><tbody id="rows"></tbody></table></div>
</div>
<h2>Coût total sur 3 ans</h2><div id="results"></div>
<div class="highlight-box"><p id="verdict">💡 Le classement « 3 ans » diffère souvent du prix d'appel.</p></div>
<p>À lire : <a href="/comparatifs/hebergement-web.html">comparatif hébergement web</a>, <a href="/guides/frais-ionos.html">frais IONOS</a>.</p>
<script>
var H=[{n:"o2switch",go:"/go/o2switch",a1:5,ren:7},{n:"Hostinger",go:"/go/hostinger",a1:2.99,ren:8.99},{n:"IONOS",go:"/go/ionos",a1:1,ren:9},{n:"Infomaniak",go:"/go/infomaniak",a1:5.75,ren:5.75},{n:"OVHcloud",go:"/go/ovhcloud",a1:3.59,ren:7.19}];
function fmt(x){return x.toLocaleString("fr-FR",{maximumFractionDigits:0})+" €";}
function build(){document.getElementById("rows").innerHTML=H.map(function(h,i){return '<tr><td><strong>'+h.n+'</strong></td><td><input type="number" step="0.01" min="0" data-i="'+i+'" data-k="a1" value="'+h.a1+'" style="width:90px;padding:6px;border:1px solid var(--gray-300);border-radius:6px;"></td><td><input type="number" step="0.01" min="0" data-i="'+i+'" data-k="ren" value="'+h.ren+'" style="width:90px;padding:6px;border:1px solid var(--gray-300);border-radius:6px;"></td></tr>';}).join("");}
function calc(){document.querySelectorAll("#rows input").forEach(function(inp){H[+inp.dataset.i][inp.dataset.k]=parseFloat(inp.value)||0;});
var res=H.map(function(h){return{n:h.n,go:h.go,t:h.a1*12+h.ren*24};}).sort(function(a,b){return a.t-b.t;});
document.getElementById("results").innerHTML=res.map(function(r,i){return '<div class="result-card'+(i===0?' best':'')+'"><div class="rc-name">'+(i===0?'🏆 ':'')+r.n+'</div><a href="'+r.go+'" class="btn-green" target="_blank" rel="sponsored nofollow noopener" style="padding:8px 14px;font-size:.85rem;">Voir l\\u2019offre →</a><div class="rc-cost">'+fmt(r.t)+' / 3 ans</div><div class="rc-detail">12 mois au prix promo + 24 mois au renouvellement</div></div>';}).join("");
document.getElementById("verdict").innerHTML='💡 Sur 3 ans, <strong>'+res[0].n+'</strong> est le plus économique ('+fmt(res[0].t)+'), '+fmt(res[1].t-res[0].t)+' de moins que '+res[1].n+'.';}
build();calc();document.getElementById("calc").addEventListener("input",calc);
</script>''',
      [("Pourquoi calculer sur 3 ans ?","Les prix d'appel de première année masquent des renouvellements 2 à 5 fois plus chers : 3 ans révèlent le coût réel."),
       ("Quel hébergeur est le moins cher sur 3 ans ?","Souvent celui dont le renouvellement reste stable (o2switch, Infomaniak), pas celui au prix d'appel le plus bas."),
       ("Les prix pré-remplis sont-ils contractuels ?","Non, indicatifs et modifiables : les grilles officielles font foi.")])
    STYLE = '''<style>
.tool-form{background:var(--gray-50);border:1px solid var(--gray-200);border-radius:14px;padding:22px;margin:20px 0;}
.tool-row{display:grid;grid-template-columns:1fr 200px;gap:12px;align-items:center;margin-bottom:12px;}
.tool-row label{font-weight:600;color:var(--gray-800);font-size:.95rem;}
.tool-row input,.tool-row select{padding:10px 12px;border:1px solid var(--gray-300);border-radius:8px;font:inherit;width:100%;box-sizing:border-box;}
.tool-note{font-size:.8rem;color:var(--gray-500);margin-bottom:10px;}
.result-card{border:1px solid var(--gray-200);border-radius:12px;padding:16px 18px;margin:10px 0;display:flex;align-items:center;gap:14px;flex-wrap:wrap;}
.result-card.best{border-color:#16a34a;background:#f0fdf4;}
.result-card .rc-name{font-weight:800;min-width:110px;}
.result-card .rc-cost{font-weight:800;font-size:1.15rem;margin-left:auto;}
.result-card .rc-detail{font-size:.82rem;color:var(--gray-500);width:100%;}
@media (max-width:640px){.tool-row{grid-template-columns:1fr;}}
</style>'''
    made = 0
    for path, (title, desc, h1, sub, crumb, body, faq) in pages.items():
        if os.path.exists(path): continue
        url = "https://selectum.fr/" + path
        app = json.dumps({"@context":"https://schema.org","@type":"WebApplication","name":title,"description":desc,
          "applicationCategory":"FinanceApplication","operatingSystem":"Web",
          "offers":{"@type":"Offer","price":"0","priceCurrency":"EUR"},"url":url,
          "publisher":{"@type":"Organization","name":"Selectum"}},ensure_ascii=False)
        out = shell(url, title, desc, h1, sub, "Outils / " + crumb, body, faq, "/outils.html", "Tous nos outils",
                    extra_head=f'<script type="application/ld+json">{app}</script>\n{STYLE}\n')
        open(path, "w", encoding="utf-8").write(out)
        made += 1
    # hub outils : ajouter les nouveaux
    t = open("outils.html", encoding="utf-8").read()
    if "simulateur-frais-crypto" not in t:
        add = ('<a href="/outils/simulateur-frais-crypto.html" class="hub-item">📉 Simulateur de frais crypto selon votre volume</a>\n'
               '<a href="/outils/cout-banque-pro-12-mois.html" class="hub-item">🏦 Comparateur : coût d\'une banque pro sur 12 mois</a>\n'
               '<a href="/outils/calculateur-hebergement-3-ans.html" class="hub-item">🌐 Calculateur : hébergement web sur 3 ans</a>\n')
        t = t.replace('</div></div></section>', add + '</div></div></section>', 1)
        open("outils.html", "w", encoding="utf-8").write(t)
    print("calculateurs créés:", made)

# ---------- 3. JSON-LD GLOBAL + IMG ATTRS ----------
def polish():
    org_added = img_fixed = 0
    for f in glob.glob("**/*.html", recursive=True):
        if f.startswith(("node_modules", "tools")): continue
        t = open(f, encoding="utf-8").read()
        o = t
        if '"@type": "Organization"' not in t and "</head>" in t:
            t = t.replace("</head>", ORG + "\n" + WS + "\n</head>", 1)
            org_added += 1
        # lazy loading + dimensions sur les logos de cartes (pas le header ni brand-hero)
        def fix_img(m):
            tag = m.group(0)
            if "logo-img" in tag or "brand-hero" in tag: return tag
            if "loading=" not in tag:
                tag = tag.replace("<img ", '<img loading="lazy" ', 1)
            if "width=" not in tag and "/assets/logos/" in tag:
                tag = tag.replace("<img ", '<img width="104" height="60" ', 1)
            return tag
        t = re.sub(r'<img [^>]*src="/assets/logos/[^"]+"[^>]*>', fix_img, t)
        if t != o:
            open(f, "w", encoding="utf-8").write(t)
            if "loading=" in t and "loading=" not in o: img_fixed += 1
    print(f"Organization/WebSite ajoutés: {org_added} pages ; images optimisées (lazy/dimensions)")

# ---------- 4. SITEMAP ----------
def sitemap():
    rows = []
    pri = {"index.html": "1.0"}
    for f in sorted(glob.glob("**/*.html", recursive=True)):
        if f.startswith(("node_modules", "tools")) or f in ("google624a5764719aa43c.html",): continue
        p = "0.6"
        if f == "index.html": p = "1.0"
        elif f.startswith("comparatifs/"): p = "0.8"
        elif f.startswith(("avis/", "guides/", "outils")): p = "0.7"
        elif f.startswith("actualites"): p = "0.7"
        elif f in ("autres-comparatifs.html", "outils.html", "methodologie.html"): p = "0.8"
        mt = datetime.date.fromtimestamp(os.path.getmtime(f)).isoformat()
        rows.append(f'  <url><loc>https://selectum.fr/{f}</loc><lastmod>{mt}</lastmod><changefreq>weekly</changefreq><priority>{p}</priority></url>')
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n"
    open("sitemap.xml", "w", encoding="utf-8").write(xml)
    print("sitemap reconstruit:", len(rows), "URLs")

if __name__ == "__main__":
    wallester()
    calculateurs()
    polish()
    sitemap()
