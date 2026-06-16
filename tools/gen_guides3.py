#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 3 : long-tail 'meilleur X pour [cas]' + comparaisons de concepts 'X vs Y'."""
import os, html, json
FONT="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D="15 juin 2026"
def P(*x): return "".join(f"<p>{p}</p>" for p in x)
def H2(i,t): return f'<h2 id="{i}">{t}</h2>'
def UL(x): return "<ul>"+"".join(f"<li>{i}</li>" for i in x)+"</ul>"
def OL(x): return "<ol>"+"".join(f"<li>{i}</li>" for i in x)+"</ol>"
def BOX(t): return f'<div class="highlight-box"><p>{t}</p></div>'

SILO={
 "crypto":[("/comparatifs/crypto.html","Comparatif des applications crypto"),("/code-promo/coinbase.html","Code promo Coinbase"),("/code-promo/bitpanda.html","Offres Bitpanda"),("/code-promo/kraken.html","Code promo Kraken")],
 "bourse":[("/comparatifs/trading-bourse.html","Comparatif des courtiers en bourse"),("/code-promo/xtb.html","Code promo XTB"),("/code-promo/trade-republic.html","Offres Trade Republic"),("/code-promo/etoro.html","Code promo eToro")],
 "banque":[("/comparatifs/banque-en-ligne.html","Comparatif des banques en ligne"),("/code-promo/n26.html","Code promo N26"),("/code-promo/revolut.html","Offres Revolut"),("/code-promo/boursobank.html","Code promo BoursoBank")],
 "compte-pro":[("/comparatifs/comptes-pro.html","Comparatif des comptes pro"),("/code-promo/qonto.html","Code promo Qonto"),("/code-promo/shine.html","Offres Shine"),("/code-promo/finom.html","Code promo Finom")],
 "hebergement":[("/comparatifs/hebergement-web.html","Comparatif des hébergeurs web"),("/code-promo/ionos.html","Code promo IONOS"),("/code-promo/hostinger.html","Offres Hostinger"),("/code-promo/o2switch.html","Code promo o2switch")],
 "epargne":[("/comparatifs/assurance-vie.html","Comparatif assurance-vie"),("/code-promo/linxea.html","Code promo Linxea"),("/code-promo/nalo.html","Offres Nalo"),("/code-promo/yomoni.html","Code promo Yomoni")],
 "vpn":[("/comparatifs/vpn.html","Comparatif des VPN"),("/code-promo/expressvpn.html","Code promo ExpressVPN"),("/code-promo/nordvpn.html","Offres NordVPN"),("/code-promo/surfshark.html","Code promo Surfshark")],
 "assurance":[("/comparatifs/assurance-auto.html","Comparatif assurance auto"),("/comparatifs/assurance-habitation.html","Assurance habitation"),("/comparatifs/mutuelle-sante.html","Mutuelle santé")],
}
CATLABEL={"crypto":"Crypto","bourse":"Bourse","banque":"Banque","compte-pro":"Compte pro","hebergement":"Hébergement","epargne":"Épargne","vpn":"Tech","assurance":"Assurance"}

G=[]
def add(**k): G.append(k)

add(slug="meilleure-neobanque-etudiant",cat="banque",
 title="Meilleure néobanque pour étudiant en 2026",
 desc="Quelle est la meilleure néobanque pour un étudiant en 2026 ? Carte gratuite, paiements à l'étranger, sans frais. Critères et sélection pour bien choisir.",
 h1="Meilleure néobanque pour étudiant",
 lead="Pour un étudiant, l'idéal est une néobanque gratuite, simple et sans frais à l'étranger (Erasmus, voyages). Voici comment choisir.",
 body=H2("criteres","Ce qui compte pour un étudiant")
  +UL(["<strong>Carte gratuite</strong> et aucun frais de tenue de compte.",
       "<strong>Paiements et retraits à l'étranger</strong> sans surcoût (séjours, Erasmus).",
       "<strong>Appli simple</strong> avec suivi des dépenses et sous-comptes.",
       "Ouverture rapide, souvent dès 18 ans (offres ado pour les mineurs)."])
  +H2("selection","Notre sélection")
  +UL(["<strong>N26</strong> et <strong>Revolut</strong> : gratuites, parfaites à l'étranger.",
       "Les offres ado/jeunes (Pixpay, Kard) pour les mineurs.",
       "Une banque en ligne complète (BoursoBank) si besoin d'un compte plus complet."])
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a> et notre <a href=\"/comparatifs/cartes-famille.html\">sélection cartes ados &amp; famille</a>."),
 faq=[("Quelle néobanque gratuite pour étudiant ?","N26 et Revolut proposent une carte gratuite et sont idéales à l'étranger. Pour les mineurs, regardez les offres ado."),
      ("Peut-on ouvrir une néobanque à 16 ans ?","Oui via des offres dédiées aux ados (avec accord parental). Les comptes adultes s'ouvrent en général à 18 ans."),
      ("Une néobanque suffit-elle pour un étudiant ?","Oui pour la plupart des usages : carte, paiements, virements. Vérifiez juste le dépôt d'espèces si nécessaire.")]),

add(slug="meilleure-assurance-vie-debutant",cat="epargne",
 title="Meilleure assurance-vie pour débuter en 2026",
 desc="Quelle est la meilleure assurance-vie pour débuter en 2026 ? Frais d'entrée, fonds euros, ETF, gestion pilotée. Critères et sélection pour bien démarrer.",
 h1="Meilleure assurance-vie pour débuter",
 lead="Pour une première assurance-vie, l'essentiel est simple : zéro frais d'entrée, des frais de gestion bas, et le choix entre gérer soi-même ou être accompagné.",
 body=H2("criteres","Les critères pour débuter")
  +UL(["<strong>0 % de frais d'entrée</strong> et de versement (non négociable).",
       "<strong>Frais de gestion bas</strong> sur les unités de compte.",
       "Un <strong>fonds euros</strong> de qualité pour la partie sécurisée.",
       "Le choix entre <strong>gestion libre</strong> (autonomie) et <strong>gestion pilotée</strong> (accompagnée)."])
  +H2("selection","Notre sélection")
  +UL(["<strong>Linxea</strong> : référence en gestion libre, frais bas, large choix (ETF, SCPI).",
       "<strong>Nalo</strong> et <strong>Yomoni</strong> : gestion pilotée en ETF, idéal si vous voulez être accompagné.",
       "<strong>Prendre date tôt</strong> : l'antériorité fiscale court dès l'ouverture."])
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a> et lisez <a href=\"/guides/comment-placer-10000-euros.html\">comment placer 10 000 €</a>. L'assurance-vie comporte un risque de perte sur les unités de compte."),
 faq=[("Quelle assurance-vie choisir pour débuter ?","Une à 0 % de frais d'entrée et frais de gestion bas : Linxea en gestion libre, Nalo/Yomoni en gestion pilotée."),
      ("Faut-il prendre date sur une assurance-vie ?","Oui : l'antériorité fiscale court dès l'ouverture. Ouvrir tôt, même avec peu, lance le compteur des 8 ans."),
      ("Gestion libre ou pilotée pour débuter ?","Pilotée si vous voulez être accompagné, libre si vous êtes à l'aise pour choisir vos supports (ETF…).")]),

add(slug="meilleur-vpn-pas-cher",cat="vpn",
 title="Meilleur VPN pas cher en 2026 : le bon rapport qualité/prix",
 desc="Quel est le meilleur VPN pas cher en 2026 ? Réductions sur les engagements longs, appareils illimités, vitesse. Sélection pour un VPN fiable sans se ruiner.",
 h1="Meilleur VPN pas cher : le bon rapport qualité/prix",
 lead="Un bon VPN ne coûte pas cher si on s'engage sur la durée. Voici comment obtenir un service fiable au meilleur prix.",
 body=H2("prix","Comment payer son VPN moins cher")
  +UL(["Les <strong>engagements longs (1-2 ans)</strong> offrent les plus grosses réductions.",
       "Méfiez-vous du <strong>prix de renouvellement</strong>, souvent plus élevé.",
       "Les VPN gratuits financent souvent leur service par la revente de données : à éviter."])
  +H2("selection","Le meilleur rapport qualité/prix")
  +UL(["<strong>Surfshark</strong> : appareils illimités et tarifs bas sur les engagements longs — souvent le meilleur deal.",
       "<strong>NordVPN</strong> : complet et rapide, fortes promos sur 2 ans.",
       "<strong>CyberGhost</strong> : simple et économique, orienté streaming."])
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/vpn.html\">comparatif des VPN</a>."),
 faq=[("Quel est le VPN le moins cher et fiable ?","Surfshark offre souvent le meilleur rapport qualité/prix (appareils illimités). NordVPN et CyberGhost ont aussi de fortes promos sur les engagements longs."),
      ("Un VPN gratuit est-il une bonne idée ?","Rarement pour un usage sérieux : beaucoup se financent par la revente de données ou bridant le service."),
      ("Pourquoi le prix augmente au renouvellement ?","Les tarifs bas concernent la première période d'engagement ; le renouvellement est souvent plus cher. Pensez coût total.")]),

add(slug="meilleure-carte-crypto",cat="crypto",
 title="Meilleure carte crypto en 2026 : payer en cryptomonnaies",
 desc="Quelle est la meilleure carte crypto en 2026 ? Payer en cryptos, cashback, frais et fiscalité. Critères et sélection pour choisir une carte adossée à ses cryptoactifs.",
 h1="Meilleure carte crypto : payer en cryptomonnaies",
 lead="Une carte crypto permet de dépenser ses cryptoactifs comme une carte classique. Pratique, mais attention aux frais et à la fiscalité.",
 body=H2("principe","Comment fonctionne une carte crypto")
  +P("Une <strong>carte crypto</strong> convertit vos cryptos en euros au moment du paiement (ou s'adosse à un solde). Vous payez en magasin comme avec une carte normale, certaines offrant du <strong>cashback en crypto</strong>.")
  +H2("attention","Les points d'attention")
  +UL(["Chaque dépense peut déclencher une <strong>cession imposable</strong> (conversion crypto → euros).",
       "Des <strong>frais de conversion</strong> peuvent s'appliquer.",
       "Vérifiez la régulation de l'émetteur et les plafonds."])
  +H2("selection","Les acteurs")
  +P("Plusieurs plateformes crypto proposent une carte adossée à leur application. Comparez les frais et le cashback dans notre <a href=\"/comparatifs/crypto.html\">comparatif des applications crypto</a>.")
  +BOX("⚠️ Payer en crypto peut être un fait générateur d'imposition. Voir notre <a href=\"/guides/declarer-cryptomonnaies-impots.html\">guide fiscalité crypto</a>."),
 faq=[("Une carte crypto est-elle intéressante ?","Pratique pour dépenser ses cryptos et profiter de cashback, mais attention aux frais de conversion et à la fiscalité de chaque dépense."),
      ("Payer en crypto est-il imposable ?","Oui, une dépense via conversion crypto → euros peut constituer une cession imposable. Conservez l'historique."),
      ("Quelle carte crypto choisir ?","Comparez le cashback, les frais de conversion et la régulation de l'émetteur dans notre comparatif crypto.")]),

add(slug="meilleur-hebergement-ecommerce",cat="hebergement",
 title="Meilleur hébergement pour un site e-commerce en 2026",
 desc="Quel est le meilleur hébergement pour un site e-commerce en 2026 ? Performance, sécurité, WooCommerce ou solution dédiée. Critères et sélection pour vendre en ligne.",
 h1="Meilleur hébergement pour un site e-commerce",
 lead="Un site e-commerce exige plus qu'un hébergement basique : performance, sécurité et capacité à encaisser les pics de trafic. Voici comment choisir.",
 body=H2("criteres","Les critères pour l'e-commerce")
  +UL(["<strong>Performance</strong> (temps de chargement) : crucial pour le taux de conversion.",
       "<strong>Sécurité</strong> : SSL, sauvegardes, protection contre les attaques.",
       "<strong>Scalabilité</strong> pour absorber les pics (soldes, campagnes).",
       "Compatibilité <strong>WooCommerce</strong> ou solution e-commerce dédiée (Shopify)."])
  +H2("voie","Deux approches")
  +UL(["<strong>WordPress + WooCommerce</strong> sur un bon hébergement : flexible et économique.",
       "<strong>Shopify</strong> : tout-en-un hébergé, plus simple pour vendre vite."])
  +H2("selection","Les bons choix")
  +P("Pour WooCommerce, un hébergement performant (o2switch, Hostinger, IONOS) suffit pour démarrer. Pour une solution clé en main, voir notre <a href=\"/comparatifs/creer-boutique-en-ligne.html\">comparatif création de boutique en ligne</a> et le <a href=\"/comparatifs/hebergement-web.html\">comparatif hébergeurs</a>.")
  +BOX("💡 Voir aussi notre <a href=\"/etudes/classement-hebergeurs-moins-chers.html\">classement des hébergeurs les moins chers</a>."),
 faq=[("Quel hébergement pour un site e-commerce ?","Pour WooCommerce, un hébergement performant (o2switch, Hostinger, IONOS). Pour une solution clé en main, Shopify."),
      ("WooCommerce ou Shopify ?","WooCommerce pour la flexibilité et l'économie ; Shopify pour la simplicité tout-en-un."),
      ("Un mutualisé suffit-il pour vendre en ligne ?","Pour démarrer avec un trafic modéré, oui. Pour un gros volume, envisagez un VPS ou un hébergement infogéré.")]),

add(slug="meilleur-compte-pro-sasu",cat="compte-pro",
 title="Meilleur compte pro pour une SASU en 2026",
 desc="Quel est le meilleur compte pro pour une SASU en 2026 ? Dépôt de capital, fonctionnalités, prix. Critères et sélection pour ouvrir le compte de votre société.",
 h1="Meilleur compte pro pour une SASU",
 lead="Une SASU doit obligatoirement avoir un compte professionnel. Voici comment choisir, du dépôt de capital à la gestion au quotidien.",
 body=H2("obligation","Compte pro obligatoire pour une SASU")
  +P("Contrairement à la micro-entreprise, une <strong>société (SASU, EURL, SAS…) doit ouvrir un compte professionnel dédié</strong> dès sa création, notamment pour le <strong>dépôt du capital social</strong>.")
  +H2("criteres","Les critères de choix")
  +UL(["<strong>Dépôt de capital</strong> et attestation rapides.",
       "<strong>Outils de gestion</strong> : cartes, dépenses, parfois facturation et compta.",
       "<strong>Prix</strong> adapté à votre volume.",
       "Qualité du <strong>support</strong>."])
  +H2("selection","Notre sélection")
  +UL(["<strong>Qonto</strong> : la référence, complet et fiable, dépôt de capital fluide.",
       "<strong>Shine</strong> et <strong>Finom</strong> : alternatives plus économiques pour démarrer."])
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/comptes-pro.html\">comparatif des comptes pro</a> et notre <a href=\"/comparatifs/compte-pro-sasu.html\">sélection SASU</a>."),
 faq=[("Un compte pro est-il obligatoire pour une SASU ?","Oui : une société doit ouvrir un compte professionnel dédié dès sa création, notamment pour déposer le capital social."),
      ("Quel compte pro pour déposer le capital d'une SASU ?","Qonto, Shine et Finom permettent le dépôt de capital en ligne avec attestation. Comparez les délais et tarifs."),
      ("Combien coûte un compte pro pour SASU ?","De quelques euros à une trentaine d'euros par mois selon les fonctionnalités et le volume.")]),

# ---------- "X vs Y" concept ----------
add(slug="etf-vs-actions",cat="bourse",
 title="ETF ou actions : que choisir pour investir en bourse (2026) ?",
 desc="ETF ou actions en 2026 : diversification, risque, frais, temps de gestion. Comparatif clair pour choisir entre trackers et actions individuelles selon votre profil.",
 h1="ETF ou actions : que choisir ?",
 lead="Faut-il acheter des actions individuelles ou des ETF ? Pour la grande majorité des investisseurs, la réponse est plus simple qu'on ne le pense.",
 body=H2("etf","Les ETF en bref")
  +UL(["<strong>Diversification immédiate</strong> : un ETF World contient des centaines d'entreprises.",
       "<strong>Frais très bas</strong> et gestion passive.",
       "Idéal pour investir sans suivre les marchés au quotidien."])
  +H2("actions","Les actions individuelles en bref")
  +UL(["<strong>Potentiel de surperformance</strong>… mais risque concentré.",
       "Demande du <strong>temps</strong> et des connaissances pour analyser les entreprises.",
       "Plus de volatilité sur un seul titre."])
  +H2("verdict","Le verdict pour la plupart")
  +P("Pour un investisseur particulier, un <strong>ETF World en cœur de portefeuille</strong> est l'approche la plus simple, diversifiée et performante sur le long terme. Les actions individuelles peuvent compléter, en pleine conscience du risque.")
  +BOX("💡 Voir <a href=\"/guides/comment-investir-en-bourse-debutant.html\">comment investir en bourse</a> et notre <a href=\"/comparatifs/courtier-etf.html\">comparatif courtier ETF</a>. Investir comporte un risque de perte en capital."),
 faq=[("Vaut-il mieux acheter des ETF ou des actions ?","Pour la plupart des particuliers, un ETF diversifié (type World) est plus simple et performant sur le long terme que de choisir des actions individuelles."),
      ("Les ETF sont-ils risqués ?","Ils restent soumis au risque de marché, mais la diversification réduit le risque par rapport à une action unique."),
      ("Peut-on mélanger ETF et actions ?","Oui : beaucoup utilisent un ETF en cœur de portefeuille et quelques actions en complément.")]),

add(slug="fonds-euros-vs-unites-de-compte",cat="epargne",
 title="Fonds euros ou unités de compte : que choisir en assurance-vie ?",
 desc="Fonds euros ou unités de compte en 2026 : garantie, rendement, risque, fiscalité. Comparatif clair pour répartir son assurance-vie selon son horizon et son profil.",
 h1="Fonds euros ou unités de compte : que choisir ?",
 lead="En assurance-vie, vous répartissez entre fonds euros (sécurisé) et unités de compte (potentiel supérieur). Voici comment doser selon votre profil.",
 body=H2("fonds-euros","Le fonds euros")
  +UL(["<strong>Capital garanti</strong> et intérêts définitivement acquis (effet cliquet).",
       "Rendement modéré mais <strong>reparti à la hausse</strong> avec la remontée des taux.",
       "Idéal pour la <strong>part prudente</strong> et les horizons courts."])
  +H2("uc","Les unités de compte (UC)")
  +UL(["<strong>Potentiel de rendement supérieur</strong> (ETF, SCPI, actions…).",
       "<strong>Risque de perte en capital</strong> : la valeur fluctue.",
       "Pour la part <strong>long terme</strong> du portefeuille."])
  +H2("doser","Comment doser ?")
  +P("Plus votre <strong>horizon est long</strong> et votre tolérance au risque élevée, plus la part d'UC peut être importante. Un profil prudent privilégiera le fonds euros. Il n'y a pas de réponse unique.")
  +BOX("💡 Comparez les contrats dans notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Fonds euros ou unités de compte ?","Le fonds euros sécurise, les UC visent plus de rendement avec un risque. L'idéal est souvent un mix selon votre horizon."),
      ("Le fonds euros est-il garanti ?","Oui, le capital placé sur un fonds euros est garanti et les intérêts annuels sont définitivement acquis."),
      ("Les unités de compte sont-elles risquées ?","Oui, leur valeur fluctue et il existe un risque de perte en capital. Elles visent un rendement supérieur sur le long terme.")]),

add(slug="assurance-vie-ou-pea",cat="bourse",
 title="Assurance-vie ou PEA : lequel choisir en 2026 ?",
 desc="Assurance-vie ou PEA en 2026 : fiscalité, souplesse, supports, succession. Comparatif clair pour choisir la bonne enveloppe selon votre projet d'épargne.",
 h1="Assurance-vie ou PEA : lequel choisir ?",
 lead="Deux enveloppes phares de l'épargne française, deux logiques différentes. Souvent, le mieux est de combiner les deux.",
 body=H2("av","L'assurance-vie")
  +UL(["Très <strong>souple</strong> : fonds euros, ETF, SCPI, gestion pilotée…",
       "Fiscalité avantageuse après <strong>8 ans</strong> (abattement annuel).",
       "Atout <strong>succession</strong> majeur."])
  +H2("pea","Le PEA")
  +UL(["Dédié aux <strong>actions et ETF européens</strong>.",
       "Fiscalité très avantageuse après <strong>5 ans</strong> (gains exonérés d'IR).",
       "Plafond de 150 000 €."])
  +H2("choisir","Lequel choisir ?")
  +P("Le <strong>PEA</strong> pour investir en actions/ETF européens avec la meilleure fiscalité ; l'<strong>assurance-vie</strong> pour la souplesse, la diversification (fonds euros, SCPI) et la succession. Beaucoup d'épargnants ont les deux.")
  +BOX("💡 Voir <a href=\"/guides/pea-ou-compte-titres.html\">PEA ou compte-titres</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Assurance-vie ou PEA en premier ?","Le PEA pour les actions/ETF européens (fiscalité après 5 ans) ; l'assurance-vie pour la souplesse et la succession. Les deux sont complémentaires."),
      ("Peut-on avoir un PEA et une assurance-vie ?","Oui, c'est même recommandé : ils répondent à des objectifs différents."),
      ("Quelle enveloppe pour la succession ?","L'assurance-vie offre un cadre successoral particulièrement avantageux, contrairement au PEA.")]),

add(slug="bitcoin-vs-ethereum",cat="crypto",
 title="Bitcoin ou Ethereum : quelles différences et lequel choisir (2026) ?",
 desc="Bitcoin ou Ethereum en 2026 : différences, usages, risques. Comparatif clair pour comprendre les deux principales cryptomonnaies et faire son choix.",
 h1="Bitcoin ou Ethereum : quelles différences ?",
 lead="Les deux plus grandes cryptomonnaies ont des rôles différents. Comprendre leurs spécificités aide à faire un choix éclairé.",
 body=H2("btc","Bitcoin (BTC) : la réserve de valeur")
  +UL(["La <strong>première cryptomonnaie</strong>, la plus connue et la plus capitalisée.",
       "Souvent vu comme un <strong>« or numérique »</strong> et une réserve de valeur.",
       "Offre limitée à 21 millions d'unités."])
  +H2("eth","Ethereum (ETH) : la plateforme")
  +UL(["Une <strong>plateforme de contrats intelligents</strong> (applications décentralisées, NFT, DeFi).",
       "ETH sert à payer les frais du réseau.",
       "Permet le <strong>staking</strong> (preuve d'enjeu)."])
  +H2("choisir","Lequel choisir ?")
  +P("Ce n'est pas l'un <em>contre</em> l'autre : beaucoup détiennent les deux. Bitcoin pour la réserve de valeur, Ethereum pour l'exposition à l'écosystème applicatif. Dans tous les cas, n'investissez que ce que vous pouvez vous permettre de perdre.")
  +BOX("⚠️ Investir dans les crypto-actifs comporte un risque de perte en capital. Voir <a href=\"/guides/comment-acheter-cryptomonnaies.html\">comment acheter des cryptomonnaies</a>."),
 faq=[("Faut-il acheter du Bitcoin ou de l'Ethereum ?","Les deux ont des rôles différents (réserve de valeur vs plateforme). Beaucoup d'investisseurs détiennent les deux."),
      ("Lequel est le moins risqué ?","Aucune crypto n'est sans risque. Bitcoin est le plus établi ; Ethereum est plus exposé aux usages applicatifs. Tous deux sont volatils."),
      ("Peut-on staker le Bitcoin ?","Non, le Bitcoin ne fonctionne pas en preuve d'enjeu. Le staking concerne Ethereum et d'autres cryptos.")])

def page(d):
    url=f"https://selectum.fr/guides/{d['slug']}.html"
    title=f"{d['title']} | Selectum"
    art=json.dumps({"@context":"https://schema.org","@type":"Article","headline":d['title'],"description":d['desc'],"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-15","dateModified":"2026-06-15","mainEntityOfPage":url},ensure_ascii=False)
    fld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in d['faq']]},ensure_ascii=False)
    bc=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},{"@type":"ListItem","position":2,"name":"Guides","item":"https://selectum.fr/guides/"},{"@type":"ListItem","position":3,"name":d['title'],"item":url}]},ensure_ascii=False)
    org='{"@context":"https://schema.org","@type":"Organization","name":"Selectum","url":"https://selectum.fr/","logo":"https://selectum.fr/assets/selectum-logo.png"}'
    silo=SILO[d['cat']]
    faqh="".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in d['faq'])
    pop="".join(f'<a href="{u}" class="rel-chip">{html.escape(a)} →</a>' for u,a in silo)
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(d['desc'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="article"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(d['desc'])}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<script type="application/ld+json">{art}</script>
<script type="application/ld+json">{fld}</script>
<script type="application/ld+json">{bc}</script>
<script type="application/ld+json">{org}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="{silo[0][0]}" class="btn-primary">{html.escape(silo[0][1])} →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/guides/">Guides</a><span>/</span>{html.escape(CATLABEL[d['cat']])}</div>
  <h1>{html.escape(d['h1'])}</h1>
  <p class="updated">🗓️ Mis à jour le {D} — par l'équipe Selectum</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Voir notre <a href="/methodologie.html">méthodologie</a>.</div>
  <p class="intro" style="font-size:1.12rem;color:var(--gray-700);">{html.escape(d['lead'])}</p>
  {d['body']}
  <div class="faq"><h2>❓ Questions fréquentes</h2>{faqh}</div>
  <div class="rel-links"><h2>💡 À lire aussi en {html.escape(CATLABEL[d['cat']].lower())}</h2><div class="rel-list">{pop}</div></div>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a> · <a href="/code-promo.html" style="color:var(--gray-500)">Codes promo</a> · <a href="/etudes.html" style="color:var(--gray-500)">Études</a></p>
</div></div></footer></body></html>'''

os.makedirs("guides",exist_ok=True)
for d in G:
    open(f"guides/{d['slug']}.html","w",encoding="utf-8").write(page(d))
print("batch 3 guides créés :", len(G))
for d in G: print("  guides/"+d['slug']+".html ("+d['cat']+")")
