#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages 'Alternatives à X' (comparatifs/) et pages 'Frais X' (guides/)."""
import os, html, json

FONT = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D = "11 juin 2026"

def scaffold(url, title, desc, h1, sub, crumb, body, faq, cta_url, cta_label, extra_ld=""):
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
        f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq) + "</div>"
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
<script type="application/ld+json">{art}</script>
<script type="application/ld+json">{fq}</script>
<script type="application/ld+json">{bc}</script>
{extra_ld}</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="{cta_url}" class="btn-primary">{cta_label} →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span>{html.escape(crumb)}</div>
  <h1>{html.escape(h1)}</h1>
  <p class="updated">🗓️ Mis à jour le {D} — Vérifié par notre équipe</p>
  <p class="subtitle" style="color:rgba(255,255,255,.85)">{html.escape(sub)}</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Voir notre <a href="/methodologie.html">méthodologie</a>.</div>
  {body}
  {faqh}
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

def card(slug, name, why):
    n = html.escape(name)
    avis = f' · <a href="/avis/{slug}.html">notre avis</a>' if os.path.exists(f"avis/{slug}.html") else ""
    return f'''<div class="result-card" style="border:1px solid var(--gray-200);border-radius:12px;padding:16px 18px;margin:10px 0;display:flex;align-items:center;gap:14px;flex-wrap:wrap;">
<div style="width:88px;height:48px;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid var(--gray-200);border-radius:8px;padding:4px 8px;box-sizing:border-box;"><img src="/assets/logos/{slug}.png" alt="{n}" style="max-width:100%;max-height:100%;object-fit:contain;" width="72" height="40" loading="lazy"></div>
<div style="flex:1;min-width:200px;"><strong>{n}</strong><div style="font-size:.85rem;color:var(--gray-500);">{html.escape(why)}{avis}</div></div>
<a href="/go/{slug}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a>
</div>'''

# ---------- ALTERNATIVES ----------
ALTS = {
 "qonto": ("Qonto","compte pro","/comparatifs/comptes-pro.html",
   [("shine","Le compte pro des indépendants, offre d'entrée gratuite et aide administrative"),
    ("finom","Plan gratuit avec facturation intégrée et cashback sur les plans payants"),
    ("blank","Le compte pro tout-en-un adossé au Crédit Agricole, pensé pour les artisans"),
    ("revolut","Compte business multi-devises, fort à l'international")],
   "Qonto est la référence des comptes pro, mais son tarif (dès 9 €/mois HT) ou son positionnement ne conviennent pas à tout le monde."),
 "shine": ("Shine","compte pro","/comparatifs/comptes-pro.html",
   [("qonto","Plus complet pour les équipes : multi-utilisateurs, compta avancée"),
    ("finom","Alternative gratuite directe avec facturation et IBAN européen"),
    ("blank","Bon choix artisans/commerçants avec dépôt de capital en ligne")],
   "Shine séduit les indépendants, mais selon votre profil (équipe, international, budget zéro), d'autres comptes font mieux."),
 "sumup": ("SumUp","terminal de paiement","/comparatifs/terminaux-paiement.html",
   [("zettle","Le TPE de PayPal avec caisse enregistreuse incluse"),
    ("mypos","Versement instantané des encaissements et compte pro intégré"),
    ("flatpay","Tarif fixe prévisible, intéressant à fort volume")],
   "SumUp est notre n°1 des petits volumes, mais versement instantané, caisse intégrée ou gros volumes peuvent justifier une alternative."),
 "revolut-business": ("Revolut Business","compte pro","/comparatifs/comptes-pro.html",
   [("qonto","Le compte pro le plus complet pour les équipes françaises (IBAN FR)"),
    ("finom","IBAN européen, facturation incluse, plan gratuit"),
    ("wise","Référence des paiements internationaux au taux de change réel"),
    ("shine","Le plus simple pour un indépendant français")],
   "Revolut Business brille à l'international, mais pour un IBAN français, la facturation ou le support local, voici les meilleures alternatives."),
 "bitpanda": ("Bitpanda","plateforme crypto","/comparatifs/crypto.html",
   [("kraken","Référence sécurité : preuve de réserves, frais dégressifs sur Kraken Pro"),
    ("coinbase","La plateforme grand public la plus simple pour débuter"),
    ("binance","Le plus large choix de cryptos et des frais très bas"),
    ("coinhouse","L'acteur français avec accompagnement personnalisé")],
   "Bitpanda est simple et régulé, mais selon vos priorités (frais, choix, sécurité, accompagnement), d'autres plateformes peuvent mieux convenir."),
 "etoro": ("eToro","courtier","/comparatifs/trading-bourse.html",
   [("xtb","Courtier régulé avec actions et ETF sans commission (volumes courants)"),
    ("trade-republic","Le plan d'épargne en actions/ETF le plus simple, dès 1 €"),
    ("degiro","Courtier low-cost de référence pour les investisseurs autonomes")],
   "eToro a démocratisé le trading social, mais frais de retrait, spreads ou besoin d'un PEA peuvent motiver une alternative."),
 "ionos": ("IONOS","hébergeur web","/comparatifs/hebergement-web.html",
   [("o2switch","L'offre unique française tout illimité, support réputé"),
    ("hostinger","Les prix d'appel les plus agressifs du marché"),
    ("infomaniak","L'hébergeur suisse éthique et écologique"),
    ("ovhcloud","Le géant français, du mutualisé au dédié")],
   "IONOS est un poids lourd européen, mais selon votre budget et vos besoins (simplicité, écologie, performance), voici les alternatives crédibles."),
 "hostinger": ("Hostinger","hébergeur web","/comparatifs/hebergement-web.html",
   [("o2switch","Tout illimité à prix fixe, sans surprise au renouvellement"),
    ("infomaniak","Qualité suisse, données en Europe, énergie renouvelable"),
    ("ovhcloud","Large gamme et datacenters français"),
    ("ionos","Offres complètes avec domaine et email inclus")],
   "Hostinger casse les prix la première année, mais le renouvellement grimpe : ces alternatives offrent des prix plus stables ou des garanties différentes."),
}

def gen_alternatives():
    made = 0
    for slug, (name, cat_label, cat_url, alts, intro) in ALTS.items():
        out = f"comparatifs/alternative-{slug}.html"
        if os.path.exists(out): continue
        n = html.escape(name)
        NAMES = {"shine":"Shine","finom":"Finom","blank":"Blank","revolut":"Revolut Business","qonto":"Qonto",
                 "wise":"Wise","zettle":"Zettle","mypos":"myPOS","flatpay":"Flatpay","kraken":"Kraken",
                 "coinbase":"Coinbase","binance":"Binance","coinhouse":"Coinhouse","xtb":"XTB",
                 "trade-republic":"Trade Republic","degiro":"DEGIRO","o2switch":"o2switch",
                 "hostinger":"Hostinger","infomaniak":"Infomaniak","ovhcloud":"OVHcloud","ionos":"IONOS"}
        cards = "".join(card(s, NAMES.get(s, s.title()), why) for s, why in alts)
        body = f'''<div class="intro-box"><p>{html.escape(intro)} Voici les <strong>meilleures alternatives à {n}</strong> en 2026, sélectionnées selon notre <a href="/methodologie.html">méthodologie</a>.</p></div>
<h2>Les alternatives à {n} que nous recommandons</h2>
{cards}
<h2>Comment choisir ?</h2>
<p>Listez vos deux ou trois critères décisifs (prix, fonctionnalité clé, support), puis comparez uniquement sur ceux-là. Notre <a href="{cat_url}">comparatif {html.escape(cat_label)}</a> détaille chaque acteur selon les mêmes critères pondérés.</p>'''
        faq = [(f"Quelle est la meilleure alternative à {name} ?",
                f"{NAMES.get(alts[0][0], alts[0][0].title())} arrive en tête de notre sélection : {alts[0][1][0].lower()+alts[0][1][1:]}."),
               (f"Pourquoi quitter {name} ?",
                "Les motifs les plus fréquents : tarif inadapté au volume d'usage, fonctionnalité manquante ou besoin d'un support différent."),
               ("Ces alternatives sont-elles fiables ?",
                "Oui, toutes sont des acteurs établis que nous avons évalués selon la même grille de critères publique.")]
        url = f"https://selectum.fr/comparatifs/alternative-{slug}.html"
        title = f"Alternative à {name} : les meilleures options 2026"
        desc = f"Quelles alternatives à {name} en 2026 ? Notre sélection comparée selon les frais, les fonctionnalités et le support, avec avis détaillés."
        html_out = scaffold(url, title, desc, f"Alternative à {name} : que choisir en 2026 ?",
                            f"Les meilleurs concurrents de {name}, comparés selon nos critères publics.",
                            f"Alternatives à {name}", body, faq, cat_url, "Comparatif complet")
        open(out, "w", encoding="utf-8").write(html_out)
        made += 1
    print("pages alternatives créées:", made)

# ---------- FRAIS ----------
FRAIS = {
 "qonto": ("Qonto","compte pro","/comparatifs/comptes-pro.html","/avis/qonto.html",
   [("Abonnement","Formules de 9 € à 39 €/mois HT (Basic, Smart, Premium), Enterprise sur devis"),
    ("Cartes","Carte physique incluse selon formule ; cartes supplémentaires et virtuelles selon plan"),
    ("Virements","Quota mensuel inclus selon formule, facturation à l'unité au-delà"),
    ("Dépôt d'espèces","Limité et payant — Qonto vise un usage 100 % en ligne")]),
 "shine": ("Shine","compte pro","/comparatifs/comptes-pro.html","/avis/shine.html",
   [("Abonnement","Offre d'entrée gratuite ; plans payants pour les besoins avancés"),
    ("Cartes","Carte Mastercard incluse dès l'offre de base"),
    ("Virements","Quota inclus selon le plan, à l'unité au-delà"),
    ("Encaissements","Liens de paiement et outils d'encaissement selon formule")]),
 "revolut-business": ("Revolut Business","compte pro","/comparatifs/comptes-pro.html",None,
   [("Abonnement","Plan d'entrée gratuit, plans payants par paliers selon volume"),
    ("Change","Taux interbancaire jusqu'à un plafond mensuel, marge au-delà"),
    ("Virements","Virements locaux/internationaux inclus par quotas selon plan"),
    ("Cartes","Cartes physiques et virtuelles, plafonds selon formule")]),
 "sumup": ("SumUp","terminal de paiement","/comparatifs/terminaux-paiement.html","/avis/sumup.html",
   [("Commission","~1,75 % par transaction carte présente (taux indicatif)"),
    ("Matériel","Lecteur dès ~39 € (achat unique, pas de location)"),
    ("Abonnement","Aucun : on ne paie qu'à la transaction"),
    ("Versement","Sous 1 à 3 jours ouvrés selon la banque")]),
 "zettle": ("Zettle","terminal de paiement","/comparatifs/terminaux-paiement.html","/avis/zettle.html",
   [("Commission","Taux unique par transaction (voir grille officielle)"),
    ("Matériel","Lecteur à petit prix, caisse enregistreuse incluse dans l'app"),
    ("Abonnement","Aucun abonnement obligatoire"),
    ("Versement","Généralement sous 1 à 2 jours ouvrés")]),
 "bitpanda": ("Bitpanda","plateforme crypto","/comparatifs/crypto.html","/avis/bitpanda.html",
   [("Achat/vente crypto","Frais intégrés au prix affiché (spread) selon l'actif"),
    ("Dépôt","Virement SEPA généralement gratuit ; carte plus chère"),
    ("Retrait","Frais selon méthode ; retraits crypto aux frais de réseau"),
    ("Staking/produits","Commission sur les récompenses selon le produit")]),
 "etoro": ("eToro","courtier","/comparatifs/trading-bourse.html","/avis/etoro.html",
   [("Actions/ETF","0 % de commission sur les actions au comptant (conditions s'appliquent)"),
    ("Spreads","Écart achat/vente variable selon l'actif (crypto, CFD)"),
    ("Retrait","Frais fixe par retrait (voir grille officielle)"),
    ("Inactivité","Frais mensuel après une longue période d'inactivité")]),
 "ionos": ("IONOS","hébergeur web","/comparatifs/hebergement-web.html",None,
   [("Hébergement","Prix d'appel la 1ʳᵉ année, renouvellement plus élevé — à vérifier avant achat"),
    ("Domaine","Souvent offert la première année, payant ensuite"),
    ("Email pro","Inclus selon formule, extensions payantes"),
    ("Options","Sauvegardes, SSL avancé et performances en supplément selon plan")]),
}

def gen_frais():
    made = 0
    for slug, (name, cat_label, cat_url, avis_url, lignes) in FRAIS.items():
        out = f"guides/frais-{slug}.html"
        if os.path.exists(out): continue
        n = html.escape(name)
        rows = "".join(f"<tr><td><strong>{html.escape(k)}</strong></td><td>{html.escape(v)}</td></tr>" for k, v in lignes)
        avis_link = f' Lisez aussi <a href="{avis_url}">notre avis {n} complet</a>.' if avis_url else ""
        body = f'''<div class="intro-box"><p>Combien coûte vraiment <strong>{n}</strong> ? Voici la structure de ses frais, vérifiée le {D} sur la grille tarifaire officielle. Les montants exacts évoluent : la <a href="/go/{slug}" target="_blank" rel="sponsored nofollow noopener">page officielle des tarifs</a> fait foi.{avis_link}</p></div>
<h2>La structure des frais {n}</h2>
<div class="comparison-table-wrap"><table class="comparison-table"><thead><tr><th>Poste</th><th>Ce qu'il faut savoir</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>Comment payer moins cher chez {n}</h2>
<ul><li>Choisissez la formule alignée sur votre usage réel (quotas de virements, volume d'encaissement…)</li><li>Préférez les moyens de paiement/dépôt les moins facturés (virement plutôt que carte)</li><li>Surveillez les promotions de bienvenue — souvent 1 à 3 mois offerts</li><li>Réévaluez votre formule chaque année : les grilles évoluent</li></ul>
<div class="highlight-box"><p>💡 Comparez {n} avec ses concurrents dans notre <a href="{cat_url}">comparatif {html.escape(cat_label)}</a>, à grille de critères égale.</p></div>'''
        faq = [(f"Quels sont les frais de {name} ?",
                f"Les postes principaux : {', '.join(k.lower() for k, _ in lignes)}. Le détail chiffré à jour figure sur la grille officielle de {name}."),
               (f"Les tarifs {name} affichés ici sont-ils à jour ?",
                f"Ils ont été vérifiés le {D} sur la grille officielle. En cas d'écart, la page tarifs officielle fait foi — signalez-nous toute erreur à contact@selectum.fr."),
               (f"{name} a-t-il des frais cachés ?",
                "Les coûts à surveiller sont listés dans le tableau ci-dessus ; lisez toujours les conditions de la formule choisie avant de souscrire.")]
        url = f"https://selectum.fr/guides/frais-{slug}.html"
        title = f"Frais {name} 2026 : le détail complet, vérifié"
        desc = f"Frais {name} 2026 : {', '.join(k.lower() for k, _ in lignes[:3])}… Le détail vérifié à la source et nos conseils pour payer moins."
        html_out = scaffold(url, title, desc, f"Frais {name} : combien ça coûte vraiment ?",
                            f"La structure tarifaire de {name} décortiquée, vérifiée à la source.",
                            f"Frais {name}", body, faq, cat_url, "Voir le comparatif")
        open(out, "w", encoding="utf-8").write(html_out)
        made += 1
    print("pages frais créées:", made)

if __name__ == "__main__":
    gen_alternatives()
    gen_frais()
