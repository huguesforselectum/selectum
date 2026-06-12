#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""6 comparateurs de niche : crowdlending P2P, assurance animaux, fournisseur d'énergie,
kit solaire, eSIM voyage, forfait mobile. Sélection éditoriale (sans note chiffrée inventée)."""
import os, html, json, importlib.util

spec = importlib.util.spec_from_file_location("g1", "tools/gen_1parrainage.py")
g1 = importlib.util.module_from_spec(spec)
# on ne lance pas main(); on importe juste BRANDS
import types, re
src = open("tools/gen_1parrainage.py").read()
ns = {}
exec(src.split("def main(")[0], ns)
BRANDS = ns["BRANDS"]
BYSLUG = {b[0]: b for b in BRANDS}

FONT = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D = "12 juin 2026"
ORG = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Organization", "name": "Selectum", "url": "https://selectum.fr/", "logo": "https://selectum.fr/assets/selectum-logo.png", "description": "Comparatifs et avis indépendants : banque, bourse, crypto, assurance, crédit, énergie et logiciels."}</script>'
WS = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "WebSite", "name": "Selectum", "url": "https://selectum.fr/", "inLanguage": "fr-FR"}</script>'

# Marques existantes à inclure (desc courte)
EXTRA = {
 "lendermarket": "Plateforme de prêt P2P adossée à un groupe de crédit.",
 "lassie": "L'assurance santé pour chien et chat, axée prévention.",
 "engie": "Le fournisseur d'électricité et de gaz, offres vertes et services.",
 "totalenergies": "Électricité et gaz à tarifs compétitifs, offres vertes.",
 "vattenfall": "Fournisseur d'électricité et de gaz d'origine renouvelable.",
 "ekwateur": "Fournisseur d'énergie verte : électricité et gaz renouvelables.",
 "ohm-energie": "Fournisseur d'électricité avec offres indexées et heures creuses.",
 "monkitsolaire": "Kits de panneaux solaires en autoconsommation à monter soi-même.",
 "materfrance": "Kits solaires plug-and-play et autoconsommation pour particuliers.",
 "red-by-sfr": "Forfaits mobiles et box sans engagement sur réseau SFR.",
 "laposte-mobile": "Forfaits mobiles de La Poste, sur le réseau SFR.",
}
def desc_of(slug):
    if slug in BYSLUG: return BYSLUG[slug][3-1] if False else BYSLUG[slug][4]
    return EXTRA.get(slug, "")
def name_of(slug):
    if slug in BYSLUG: return BYSLUG[slug][1]
    return {"lendermarket":"Lendermarket","lassie":"Lassie","engie":"Engie","totalenergies":"TotalEnergies",
            "vattenfall":"Vattenfall","ekwateur":"ekWateur","ohm-energie":"OHM Énergie","monkitsolaire":"MonKitSolaire",
            "materfrance":"Materfrance","red-by-sfr":"RED by SFR","laposte-mobile":"La Poste Mobile"}.get(slug, slug)

# slug_page, h1, intro, risk, members[], faq[]
COMPARS = [
 ("crowdlending-p2p", "Meilleures plateformes de crowdlending / P2P 2026", True,
  "Le crowdlending (prêt participatif) permet de viser un rendement supérieur aux livrets en prêtant aux entreprises ou en finançant l'immobilier. Voici notre sélection des plateformes les plus reconnues — à utiliser en connaissance du risque.",
  ["mintos","lendermarket","peerberry","bondora","robocash","swaper","esketit","viainvest","crowdestor","estateguru","raizers","lendopolis","lendosphere","look-and-fin","homunity","clubfunding","la-premiere-brique","enerfip","miimosa","wiseed","october","pretup","baltis","bricks"],
  [("Le crowdlending est-il risqué ?","Oui : il existe un risque de perte en capital et de défaut de l'emprunteur, et la liquidité est limitée. Diversifiez et n'investissez qu'une part mesurée de votre épargne."),
   ("Quel rendement espérer en P2P ?","Les rendements annoncés vont souvent de 5 % à plus de 12 %, sans garantie. Le rendement réel dépend des défauts et de la qualité de la plateforme."),
   ("Comment choisir une plateforme de crowdlending ?","Regardez l'ancienneté, la régulation, le type de prêts (conso, immobilier, entreprises), les garanties de rachat et l'historique de défauts.")]),
 ("assurance-animaux", "Meilleure assurance pour animaux (chien & chat) 2026", False,
  "Une mutuelle pour animaux rembourse une partie des frais vétérinaires (consultations, chirurgie, médicaments). Voici les principaux acteurs pour assurer votre chien ou votre chat.",
  ["dalma","santevet","assuropoil","barkibu","bulle-bleue","kozoo","lassie"],
  [("L'assurance animaux est-elle utile ?","Elle protège des grosses dépenses vétérinaires imprévues. L'intérêt dépend de l'âge et de la race de l'animal, et des plafonds de remboursement."),
   ("Combien coûte une assurance pour chien ou chat ?","Les cotisations vont généralement de quelques euros à plus de 50 €/mois selon la formule, l'espèce, la race et l'âge."),
   ("Y a-t-il un délai de carence ?","Oui, la plupart des contrats appliquent un délai de carence avant la prise en charge ; vérifiez-le ainsi que les exclusions.")]),
 ("fournisseur-energie", "Meilleur fournisseur d'énergie (électricité & gaz) 2026", False,
  "Depuis l'ouverture du marché, de nombreux fournisseurs proposent des offres d'électricité et de gaz souvent moins chères que le tarif réglementé, dont des offres vertes. Voici les principaux acteurs.",
  ["edf","engie","totalenergies","octopus-energy","mint-energie","vattenfall","ekwateur","ohm-energie","alpiq","enercoop","ilek","elmy","wekiwi","mega-energie","sowee","plenitude","primeo-energie","la-bellenergie"],
  [("Quel est le fournisseur d'énergie le moins cher ?","Cela dépend de votre consommation et du type d'offre (prix fixe, indexé, vert). Comparez le prix du kWh et de l'abonnement pour votre profil."),
   ("Changer de fournisseur d'énergie est-il risqué ?","Non : c'est gratuit, sans coupure et sans engagement. Vous pouvez revenir au tarif réglementé ou changer à tout moment."),
   ("Les offres vertes sont-elles plus chères ?","Pas forcément. Certaines offres d'électricité verte sont parmi les moins chères du marché.")]),
 ("kit-solaire-autoconsommation", "Meilleur kit solaire en autoconsommation 2026", False,
  "Les kits solaires plug-and-play permettent de produire une partie de son électricité et de réduire sa facture, sans gros chantier. Voici les acteurs de référence en autoconsommation.",
  ["beem-energy","sunology","monkitsolaire","materfrance","otovo","edf-enr"],
  [("Un kit solaire est-il rentable ?","La rentabilité dépend de votre consommation, de l'ensoleillement et du prix de l'électricité. L'amortissement se compte généralement en années."),
   ("Faut-il une autorisation pour un kit solaire ?","Une déclaration préalable en mairie et auprès du gestionnaire de réseau est souvent nécessaire ; les kits plug-and-play simplifient les démarches."),
   ("Quelle puissance choisir ?","Cela dépend de votre consommation en journée. Commencez par estimer votre talon de consommation pour dimensionner le kit.")]),
 ("esim-voyage", "Meilleure eSIM voyage 2026 : rester connecté à l'étranger", False,
  "Une eSIM de voyage permet d'avoir de la data à l'étranger sans changer de carte SIM ni subir les frais d'itinérance. Voici les meilleures applications d'eSIM voyage.",
  ["airalo","holafly","ubigi","saily","kolet","nomad-esim"],
  [("Comment fonctionne une eSIM de voyage ?","Vous achetez un forfait data pour un pays ou une zone, puis activez l'eSIM en scannant un QR code — sans carte physique."),
   ("Mon téléphone est-il compatible eSIM ?","La plupart des smartphones récents le sont (iPhone XS et +, Pixel, Galaxy récents). Vérifiez dans les réglages réseau."),
   ("L'eSIM inclut-elle les appels ?","La plupart des offres ne comprennent que la data ; les appels passent par des applications (WhatsApp, etc.).")]),
 ("forfait-mobile", "Meilleur forfait mobile pas cher 2026", False,
  "Forfaits sans engagement, grosses enveloppes de data à petit prix : les opérateurs et marques low-cost se livrent une vraie bataille. Voici les acteurs à comparer.",
  ["sosh","red-by-sfr","prixtel","youprice","lebara","lycamobile","nrj-mobile","coriolis","syma-mobile","auchan-telecom","laposte-mobile"],
  [("Quel est le forfait mobile le moins cher ?","Les offres low-cost démarrent à quelques euros par mois. Le bon choix dépend de votre besoin en data et de la couverture réseau."),
   ("Forfait avec ou sans engagement ?","La plupart des forfaits récents sont sans engagement : vous pouvez changer à tout moment, idéal pour profiter des promotions."),
   ("Peut-on garder son numéro ?","Oui, grâce à la portabilité via votre code RIO ; le nouvel opérateur s'occupe de la résiliation de l'ancien.")]),
]

def head(url, title, desc, leaf, extra=""):
    t,d=html.escape(title),html.escape(desc)
    bc=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
        {"@type":"ListItem","position":2,"name":"Comparatifs","item":"https://selectum.fr/autres-comparatifs.html"},
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
<nav class="nav"></nav><div class="header-cta"><a href="/autres-comparatifs.html" class="btn-primary">Voir les comparatifs →</a></div>
</div></div></header>'''

FOOT = '''<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a> · <a href="/methodologie.html" style="color:var(--gray-500)">Méthodologie</a></p>
</div></div></footer>
<script src="/assets/site.js" defer></script>
</body></html>'''

def card(i, slug):
    n = html.escape(name_of(slug)); ds = html.escape(desc_of(slug))
    avis = f'<a href="/avis/{slug}.html">Lire notre avis</a>' if os.path.exists(f"avis/{slug}.html") else ""
    return f'''<div class="offer-card">
  <div class="offer-rank">{i}</div>
  <div class="offer-logo brand"><img src="/assets/logos/{slug}.png" alt="{n}" width="104" height="60" loading="lazy"></div>
  <div class="offer-info"><div class="offer-name">{n}</div><div class="offer-desc">{ds}</div><div style="font-size:.8rem;margin-top:4px;">{avis}</div></div>
  <div class="offer-buy"><a href="/go/{slug}" class="btn-green" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
</div>'''

def build():
    made = 0
    for slug_page, h1, risk, intro, members, faq in COMPARS:
        out = f"comparatifs/{slug_page}.html"
        members = [m for m in members if os.path.exists(f"assets/logos/{m}.png")]
        url = f"https://selectum.fr/comparatifs/{slug_page}.html"
        title = f"{h1} | Selectum"
        desc = (intro[:150] + "…") if len(intro) > 153 else intro
        items = json.dumps({"@context":"https://schema.org","@type":"ItemList","itemListElement":[
            {"@type":"ListItem","position":i+1,"name":name_of(m)} for i,m in enumerate(members)]},ensure_ascii=False)
        fq = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)
        cards = "".join(card(i+1, m) for i,m in enumerate(members))
        faqh = '<div class="faq"><h2>❓ Questions fréquentes</h2>' + "".join(
            f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq) + "</div>"
        risk_box = ('<div class="affiliate-notice" style="margin-top:14px;">⚠️ <strong>Risques :</strong> investir comporte un risque de perte en capital. Les performances passées ne préjugent pas des performances futures.</div>') if risk else ""
        body = f'''<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/autres-comparatifs.html">Comparatifs</a><span>/</span>{html.escape(h1)}</div>
  <h1>{html.escape(h1)}</h1>
  <p class="updated">🗓️ Mis à jour le {D} — sélection éditoriale, selon notre <a href="/methodologie.html" style="color:rgba(255,255,255,.8)">méthodologie</a></p>
</div></div>
<div class="container-article"><div class="article-solo"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Cela n'influence pas notre sélection.</div>
  <div class="intro-box"><p>{html.escape(intro)}</p></div>
  {risk_box}
  <h2 id="selection">🏆 Notre sélection</h2>
  <div class="offers-list">{cards}</div>
  {faqh}
  <div class="rel-links"><h2>À lire aussi</h2><div class="rel-list"><a href="/autres-comparatifs.html" class="rel-chip">Tous nos comparatifs →</a><a href="/methodologie.html" class="rel-chip">Notre méthodologie →</a><a href="/outils.html" class="rel-chip">Nos outils gratuits →</a></div></div>
</main></div></div>'''
        open(out,"w",encoding="utf-8").write(head(url,title,desc,h1,
            f'<script type="application/ld+json">{items}</script>\n<script type="application/ld+json">{fq}</script>\n')+body+FOOT)
        made += 1
        print(f"  {out} ({len(members)} acteurs)")
    print("comparateurs créés:", made)

if __name__ == "__main__":
    build()
