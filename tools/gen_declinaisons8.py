#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comparatifs déclinés (long-tail) pour les 8 top catégories.
Réutilise les offres du comparatif parent, angle + FAQ spécifiques."""
import re, os, html, json

FONT = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D = "11 juin 2026"

def find(s, pat, d=""):
    m = re.search(pat, s, re.S); return m.group(1).strip() if m else d

def parse(path):
    s = open(path, encoding="utf-8").read()
    offers = []
    # top-pick
    tp = re.search(r'tp-logo"><img src="/assets/logos/([a-z0-9-]+)\.png"[^>]*>.*?tp-name">([^<]+)<.*?tp-tagline">([^<]+)<.*?tp-score"><b>([0-9,\.]+)</b>.*?tp-price">([^<]*)<.*?href="(/go/[a-z0-9-]+)"', s, re.S)
    if tp:
        offers.append(dict(slug=tp.group(1), name=tp.group(2), desc=tp.group(3), score=tp.group(4), price=tp.group(5), go=tp.group(6)))
    chunks = re.split(r'<div class="offer-card">', s)[1:]
    for c in chunks:
        c = c.split('<div class="offer-card', 1)[0]
        slug = find(c, r'/assets/logos/([a-z0-9-]+)\.png')
        name = find(c, r'offer-name">([^<]+)<')
        desc = find(c, r'offer-desc">([^<]+)<')
        score = find(c, r'offer-score-mini"><b>([0-9,\.]+)</b>')
        go = find(c, r'href="(/go/[a-z0-9-]+)"')
        price = find(c, r'offer-price-cap">([^<]*)<')
        if slug and name and go and not any(o["slug"] == slug for o in offers):
            offers.append(dict(slug=slug, name=name, desc=desc, score=score or "8,0", price=price, go=go))
    return offers

# (catégorie parent, [ (slug, h1, angle_intro, [(q,a)...]) ])
CFG = {
 "comptes-pro": ("compte pro", [
  ("meilleur-compte-pro", "Meilleur compte pro 2026 : le classement",
   "Quel est le meilleur compte professionnel en 2026 ? Nous avons classé les acteurs selon les tarifs, l'application, les outils de gestion et le support.",
   [("Quel est le meilleur compte pro en 2026 ?","Qonto domine notre classement pour sa complétude (facturation, compta, équipes). Shine et Finom sont les meilleurs choix gratuits pour démarrer."),
    ("Compte pro en ligne ou banque traditionnelle ?","Pour un indépendant ou une TPE, un compte pro en ligne est en général 2 à 4 fois moins cher et s'ouvre en quelques minutes.")]),
  ("compte-pro-auto-entrepreneur", "Compte pro auto-entrepreneur : lequel choisir en 2026 ?",
   "Auto-entrepreneur, vous devez séparer vos flux professionnels au-delà de 10 000 € de CA annuel (2 ans de suite). Voici les comptes les plus adaptés : simples, peu chers, avec facturation intégrée.",
   [("Un auto-entrepreneur doit-il avoir un compte pro ?","Un compte dédié à l'activité est obligatoire au-delà de 10 000 € de CA annuel deux années de suite. Un compte pro n'est pas imposé, mais un compte séparé l'est."),
    ("Quel compte pour un auto-entrepreneur qui démarre ?","Shine ou Finom en offre gratuite : 0 €/mois avec IBAN français ou européen et facturation incluse.")]),
  ("compte-pro-sasu", "Compte pro pour SASU : le comparatif 2026",
   "En SASU, le compte professionnel est indispensable dès la création : il sert au dépôt du capital social et à l'obtention du certificat de dépôt exigé pour l'immatriculation.",
   [("Une SASU doit-elle avoir un compte pro ?","Oui. Le dépôt du capital social exige un compte au nom de la société, et le certificat de dépôt est requis pour l'immatriculation."),
    ("Quel compte pro accepte le dépôt de capital pour une SASU ?","Qonto, Shine et Blank proposent le dépôt de capital en ligne avec certificat sous quelques jours.")]),
  ("compte-pro-sas", "Compte pro pour SAS : le comparatif 2026",
   "Pour une SAS, il faut un compte professionnel capable de gérer plusieurs associés, le dépôt de capital et les accès multi-utilisateurs. Voici notre sélection.",
   [("Quel compte pro pour une SAS avec plusieurs associés ?","Qonto est le plus adapté : gestion multi-utilisateurs, cartes d'équipe et permissions fines. Ses formules Smart et Premium ciblent les équipes."),
    ("Le dépôt de capital d'une SAS peut-il se faire en ligne ?","Oui, plusieurs comptes pro en ligne gèrent le dépôt de capital et délivrent le certificat nécessaire à l'immatriculation.")]),
  ("banque-pro-en-ligne", "Banque pro en ligne : le comparatif 2026",
   "Les « banques pro en ligne » (établissements de paiement et néobanques B2B) ont remplacé l'agence par une application efficace et des tarifs nets. Comparatif des meilleures offres.",
   [("Quelle est la meilleure banque pro en ligne ?","Qonto pour la complétude, Shine pour les indépendants, Finom pour le rapport qualité-prix, Blank pour les artisans."),
    ("Ces banques pro sont-elles fiables ?","Ce sont des établissements agréés : les fonds sont cantonnés auprès de banques partenaires et protégés.")])]),
 "terminaux-paiement": ("terminal de paiement", [
  ("terminal-paiement", "Terminal de paiement : comparatif 2026",
   "Quel terminal de paiement choisir en 2026 ? Lecteurs mobiles sans abonnement, TPE fixes, tarifs au volume : notre comparatif complet.",
   [("Quel terminal de paiement choisir ?","SumUp pour les petits volumes sans abonnement, myPOS pour le versement instantané, Flatpay pour un coût fixe prévisible."),
    ("Combien coûte un terminal de paiement ?","De ~29 € à l'achat pour un lecteur mobile, plus une commission par transaction (souvent autour de 1,75 %). Utilisez notre calculateur pour votre cas précis.")]),
  ("terminal-paiement-sans-abonnement", "Terminal de paiement sans abonnement : le comparatif 2026",
   "Pas envie d'un engagement mensuel ? Les lecteurs sans abonnement ne facturent qu'une commission à la transaction. Idéal pour les volumes modestes ou saisonniers.",
   [("Quel TPE sans abonnement choisir ?","SumUp et Zettle sont les références : matériel à petit prix, aucune mensualité, commission fixe par transaction."),
    ("Un TPE sans abonnement est-il rentable à fort volume ?","Au-delà de quelques milliers d'euros de CA carte mensuel, une offre à abonnement avec commission réduite devient souvent plus économique.")]),
  ("terminal-paiement-restaurant", "Terminal de paiement pour restaurant : comparatif 2026",
   "Service en salle, addition partagée, pourboires, encaissement rapide au comptoir : le TPE d'un restaurant a des exigences spécifiques. Notre sélection.",
   [("Quel TPE pour un restaurant ?","Un terminal mobile avec bonne autonomie pour encaisser en salle. Zettle (caisse incluse) et myPOS (versement instantané) sont bien adaptés."),
    ("Peut-on gérer les pourboires sur ces terminaux ?","Oui, la plupart des TPE modernes proposent une fonction pourboire à activer dans les réglages.")]),
  ("terminal-paiement-auto-entrepreneur", "Terminal de paiement auto-entrepreneur : comparatif 2026",
   "Pour un auto-entrepreneur, le bon TPE est sans abonnement, sans engagement et au matériel bon marché : on ne paie que lorsqu'on encaisse.",
   [("Quel TPE pour un auto-entrepreneur ?","SumUp est notre choix n°1 : lecteur à petit prix, zéro abonnement, commission unique par transaction."),
    ("Y a-t-il un minimum de chiffre d'affaires ?","Non, les lecteurs sans abonnement n'imposent aucun volume minimum : parfait pour une activité qui démarre.")])]),
 "banque-en-ligne": ("néobanque", [
  ("meilleure-banque-en-ligne", "Meilleure banque en ligne 2026 : le classement",
   "Cartes gratuites, applications soignées, frais réduits à l'étranger : notre classement des meilleures banques en ligne et néobanques en 2026.",
   [("Quelle est la meilleure banque en ligne en 2026 ?","Notre classement privilégie les frais réels, l'application et le support. Le détail complet est dans le classement ci-dessous."),
    ("Les néobanques sont-elles sûres ?","Les acteurs agréés cantonnent ou garantissent les dépôts selon leur statut (établissement de crédit ou de paiement).")]),
  ("banque-en-ligne-sans-frais", "Banque en ligne sans frais : le comparatif 2026",
   "Zéro frais de tenue de compte, carte gratuite, paiements à l'étranger sans surcoût : voici les banques en ligne réellement gratuites au quotidien.",
   [("Quelle banque en ligne est vraiment gratuite ?","Les offres d'entrée des néobanques sont gratuites au quotidien ; les frais apparaissent sur les retraits ou options premium."),
    ("Quels frais cachés vérifier ?","Retraits aux distributeurs, paiements hors zone euro, cartes de remplacement et virements instantanés.")]),
  ("banque-en-ligne-voyage", "Meilleure banque pour voyager : comparatif 2026",
   "Paiements hors zone euro, retraits à l'étranger, taux de change réel : les néobanques ont changé la donne pour les voyageurs. Notre sélection.",
   [("Quelle carte pour payer à l'étranger sans frais ?","Les néobanques type N26 ou Revolut offrent des paiements hors zone euro au taux réel, contre 2-3 % de frais dans une banque classique."),
    ("Les retraits à l'étranger sont-ils gratuits ?","Souvent dans une limite mensuelle, au-delà de laquelle un petit pourcentage s'applique selon la formule.")])]),
 "crypto": ("plateforme crypto", [
  ("meilleure-plateforme-crypto", "Meilleure plateforme crypto 2026 : le classement",
   "Frais, régulation PSAN, sécurité, simplicité : notre classement des meilleures plateformes pour acheter des cryptomonnaies en 2026.",
   [("Quelle est la meilleure plateforme crypto en 2026 ?","Notre classement croise frais réels, régulation, sécurité et expérience : le détail est ci-dessous."),
    ("Faut-il choisir une plateforme enregistrée PSAN ?","Oui, l'enregistrement PSAN auprès de l'AMF est le socle réglementaire pour un public français.")]),
  ("plateforme-crypto-securisee", "Plateforme crypto la plus sécurisée : comparatif 2026",
   "Cold storage, preuve de réserves, 2FA, historique sans piratage majeur : la sécurité doit primer dans le choix d'une plateforme crypto.",
   [("Quelle plateforme crypto est la plus sûre ?","Kraken et Coinbase font référence : preuve de réserves, majorité des fonds en cold storage et historique solide."),
    ("Comment sécuriser son compte crypto ?","Activez la double authentification (2FA), utilisez un mot de passe unique et envisagez un portefeuille externe pour les gros montants.")]),
  ("acheter-crypto-carte-bancaire", "Acheter des cryptos par carte bancaire : comparatif 2026",
   "L'achat par carte est immédiat mais plus cher que le virement. Voici les plateformes qui l'acceptent et comment limiter les frais.",
   [("Peut-on acheter des cryptos par carte bancaire ?","Oui sur la plupart des plateformes, avec des frais supérieurs au virement SEPA (souvent 1,5 à 4 %)."),
    ("Comment payer moins cher ?","Alimentez votre compte par virement SEPA puis achetez via l'interface avancée : c'est presque toujours plus économique que l'achat carte instantané.")])]),
 "assurance-vie": ("assurance-vie", [
  ("meilleure-assurance-vie", "Meilleure assurance-vie 2026 : le classement",
   "0 % de frais d'entrée, fonds euros performants, ETF et SCPI accessibles : notre classement des meilleures assurances-vie en ligne en 2026.",
   [("Quelle est la meilleure assurance-vie en 2026 ?","Les contrats en ligne dominent : 0 % de frais d'entrée et frais de gestion réduits. Le classement détaillé est ci-dessous."),
    ("Quels frais regarder en priorité ?","Frais d'entrée (0 % impératif), frais de gestion des unités de compte et frais d'arbitrage.")]),
  ("assurance-vie-etf", "Assurance-vie pour investir en ETF : comparatif 2026",
   "Loger des ETF dans une assurance-vie combine frais bas et fiscalité douce après 8 ans. Voici les contrats avec les meilleures gammes de trackers.",
   [("Quelle assurance-vie pour les ETF ?","Les contrats type Linxea Spirit 2 offrent une large gamme d'ETF à frais réduits, idéale pour la gestion passive."),
    ("Pourquoi des ETF en assurance-vie plutôt qu'en CTO ?","Pour l'abattement fiscal après 8 ans et l'absence d'imposition tant qu'on ne retire pas.")]),
  ("assurance-vie-scpi", "Assurance-vie pour investir en SCPI : comparatif 2026",
   "Accéder à l'immobilier via des SCPI logées en assurance-vie : frais d'entrée réduits et fiscalité avantageuse. Les meilleurs contrats pour le faire.",
   [("Quelle assurance-vie pour les SCPI ?","Les contrats Linxea sont réputés pour leur choix de SCPI et des conditions de retrait avantageuses."),
    ("Les SCPI en assurance-vie sont-elles garanties ?","Non : capital et revenus ne sont pas garantis. C'est un placement immobilier de long terme.")])]),
 "trading-bourse": ("courtier en bourse", [
  ("meilleur-courtier-bourse", "Meilleur courtier en bourse 2026 : le classement",
   "Frais d'ordre, choix de marchés, PEA ou CTO, qualité de la plateforme : notre classement des meilleurs courtiers pour investir en bourse en 2026.",
   [("Quel est le meilleur courtier en bourse en 2026 ?","Selon le profil : frais minimaux pour les investisseurs actifs, simplicité pour les débutants. Voir le classement ci-dessous."),
    ("Courtier étranger ou français ?","Les courtiers européens régulés sont accessibles ; vérifiez la fiscalité déclarative et l'absence de PEA chez certains.")]),
  ("courtier-bourse-debutant", "Meilleur courtier en bourse pour débutant : comparatif 2026",
   "Pour débuter en bourse : une interface claire, des montants minimums faibles, des frais lisibles et de la pédagogie. Notre sélection pour bien commencer.",
   [("Quel courtier pour débuter en bourse ?","Une plateforme simple avec achat fractionné et frais lisibles. eToro et XTB sont pensés pour les débutants."),
    ("Combien faut-il pour commencer ?","Quelques dizaines d'euros suffisent grâce aux fractions d'actions et aux ETF.")]),
  ("courtier-etf", "Meilleur courtier pour ETF : comparatif 2026",
   "Investir en ETF à moindre coût : courtiers avec ETF sans commission, plans d'investissement programmés et large choix de trackers.",
   [("Quel courtier pour acheter des ETF ?","Privilégiez les courtiers à commission nulle ou réduite sur ETF avec investissement programmé."),
    ("Vaut-il mieux des ETF au PEA ou au CTO ?","Le PEA offre un cadre fiscal avantageux après 5 ans pour les ETF éligibles ; le CTO donne accès à tout le marché.")])]),
 "hebergement-web": ("hébergeur web", [
  ("meilleur-hebergement-web", "Meilleur hébergement web 2026 : le classement",
   "Performances, prix au renouvellement, support en français : notre classement des meilleurs hébergeurs web en 2026.",
   [("Quel est le meilleur hébergeur web en 2026 ?","o2switch pour l'offre unique tout illimité, Hostinger pour les petits prix, Infomaniak pour l'éthique suisse."),
    ("Quel piège éviter en choisissant ?","Le prix de renouvellement : les promos de première année peuvent doubler ou tripler ensuite.")]),
  ("hebergement-wordpress", "Meilleur hébergement WordPress : comparatif 2026",
   "WordPress propulse plus de 40 % du web : voici les hébergeurs les plus rapides et les plus simples pour un site WordPress en 2026.",
   [("Quel hébergeur pour WordPress ?","Un hébergeur avec installation en un clic, cache serveur et PHP récent : o2switch et Hostinger excellent sur ce terrain."),
    ("Faut-il un hébergement WordPress « managé » ?","Pour la plupart des sites, un bon mutualisé suffit ; le managé se justifie pour les gros trafics.")]),
  ("hebergement-pas-cher", "Hébergement web pas cher : comparatif 2026",
   "Héberger un site pour quelques euros par mois sans sacrifier la fiabilité : les meilleures offres économiques, prix de renouvellement inclus.",
   [("Quel est l'hébergeur le moins cher ?","Hostinger affiche les prix d'appel les plus bas ; comparez toujours le prix de renouvellement."),
    ("Un hébergement pas cher est-il fiable ?","Oui chez les acteurs établis : la différence se joue sur les ressources allouées et le support.")])]),
 "vpn": ("VPN", [
  ("meilleur-vpn", "Meilleur VPN 2026 : le classement",
   "Vitesse, confidentialité, streaming, prix : notre classement des meilleurs VPN en 2026, testés en conditions réelles.",
   [("Quel est le meilleur VPN en 2026 ?","NordVPN et ExpressVPN dominent pour la vitesse et la fiabilité ; Surfshark gagne sur le prix en connexions illimitées."),
    ("Un VPN gratuit suffit-il ?","Pour un usage sérieux, non : limites de données, vitesses bridées et politique de confidentialité souvent floue.")]),
  ("vpn-streaming", "Meilleur VPN pour le streaming : comparatif 2026",
   "Accéder à vos catalogues en voyage et éviter les blocages : les VPN les plus efficaces pour le streaming en 2026.",
   [("Quel VPN fonctionne avec les plateformes de streaming ?","ExpressVPN et NordVPN maintiennent les meilleurs taux de compatibilité avec les principales plateformes."),
    ("Le streaming via VPN est-il légal ?","Utiliser un VPN est légal en France ; respectez les conditions d'utilisation des plateformes.")]),
  ("vpn-pas-cher", "VPN pas cher : comparatif 2026",
   "Protéger toute sa famille pour quelques euros par mois : les VPN au meilleur rapport qualité-prix, engagements longs inclus.",
   [("Quel est le VPN le moins cher ?","Surfshark sur les abonnements longs, avec connexions simultanées illimitées."),
    ("Les VPN pas chers sont-ils fiables ?","Oui pour les acteurs reconnus : l'écart de prix vient de la durée d'engagement, pas de la sécurité.")])]),
}

def page(cat, cat_label, offers, slug, h1, intro, faq):
    url = f"https://selectum.fr/comparatifs/{slug}.html"
    title = f"{h1} | Selectum"
    desc = (intro[:150] + "…") if len(intro) > 150 else intro
    t, d = html.escape(title), html.escape(desc)
    items = json.dumps({"@context":"https://schema.org","@type":"ItemList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":o["name"]} for i,o in enumerate(offers)]},ensure_ascii=False)
    fq = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)
    bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
        {"@type":"ListItem","position":2,"name":"Comparatifs","item":"https://selectum.fr/autres-comparatifs.html"},
        {"@type":"ListItem","position":3,"name":h1,"item":url}]},ensure_ascii=False)
    cards = ""
    for i, o in enumerate(offers):
        n, ds = html.escape(o["name"]), html.escape(o["desc"])
        price = html.escape(o["price"]) if o["price"] else "Voir le site"
        avis = f'<a class="tp-more" href="/avis/{o["slug"]}.html">Lire notre avis {n} →</a>' if os.path.exists(f'avis/{o["slug"]}.html') else ""
        if i == 0:
            cards += f'''<div class="offer-card top-pick">
  <div class="tp-rank">1</div>
  <div class="tp-logo"><img src="/assets/logos/{o["slug"]}.png" alt="{n}" width="120" height="60" loading="lazy"></div>
  <div class="tp-main"><div class="tp-name">{n}</div><div class="tp-tagline">{ds}</div>{avis}</div>
  <div class="tp-side"><div class="tp-score"><b>{o["score"]}</b><span>/10</span><small>Note Selectum</small></div>
  <div class="tp-price">{price}</div>
  <a class="btn-green tp-cta" href="{o["go"]}" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
</div>'''
        else:
            cards += f'''<div class="offer-card">
  <div class="offer-rank">{i+1}</div>
  <div class="offer-logo brand"><img src="/assets/logos/{o["slug"]}.png" alt="{n}" width="104" height="60" loading="lazy"></div>
  <div class="offer-info"><div class="offer-name">{n}</div><div class="offer-desc">{ds}</div></div>
  <div class="offer-score-mini"><b>{o["score"]}</b><span>/10</span></div>
  <div class="offer-buy"><a href="{o["go"]}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a><div class="offer-price-cap">{price}</div></div>
</div>'''
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
<script type="application/ld+json">{items}</script>
<script type="application/ld+json">{fq}</script>
<script type="application/ld+json">{bc}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/comparatifs/{cat}.html" class="btn-primary">Comparatif complet →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/comparatifs/{cat}.html">{html.escape(cat_label.capitalize())}</a><span>/</span>{html.escape(h1)}</div>
  <h1>{html.escape(h1)}</h1>
  <p class="updated">🗓️ Mis à jour le {D} — Vérifié par notre équipe selon notre <a href="/methodologie.html" style="color:rgba(255,255,255,.8)">méthodologie</a></p>
</div></div>
<div class="container-article"><div class="article-solo"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Cela n'influence pas notre classement.</div>
  <div class="intro-box"><p>{intro}</p></div>
  <h2 id="classement">🏆 Notre classement</h2>
  <div class="offers-list">{cards}</div>
  <p style="margin-top:18px;">👉 Pour l'analyse complète et le tableau détaillé, consultez notre <a href="/comparatifs/{cat}.html">comparatif {html.escape(cat_label)}</a>.</p>
  {faqh}
  <div class="rel-links"><h2>À lire aussi</h2><div class="rel-list"><a href="/comparatifs/{cat}.html" class="rel-chip">Comparatif {html.escape(cat_label)} complet →</a><a href="/methodologie.html" class="rel-chip">Notre méthodologie de notation →</a><a href="/outils.html" class="rel-chip">Nos outils gratuits →</a></div></div>
</main></div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

def main():
    made = 0
    for cat, (label, variants) in CFG.items():
        parent = f"comparatifs/{cat}.html"
        if not os.path.exists(parent):
            print("parent absent:", parent); continue
        offers = parse(parent)
        if len(offers) < 2:
            print("offres insuffisantes:", parent, len(offers)); continue
        for slug, h1, intro, faq in variants:
            out = f"comparatifs/{slug}.html"
            if os.path.exists(out): continue
            open(out, "w", encoding="utf-8").write(page(cat, label, offers, slug, h1, intro, faq))
            made += 1
    print("déclinaisons créées:", made)

if __name__ == "__main__":
    main()
