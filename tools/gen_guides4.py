#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 4 : long-tail supplementaire toutes verticales."""
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
 "epargne":[("/comparatifs/assurance-vie.html","Comparatif assurance-vie"),("/comparatifs/per-retraite.html","Comparatif PER"),("/code-promo/linxea.html","Code promo Linxea"),("/code-promo/yomoni.html","Offres Yomoni")],
 "vpn":[("/comparatifs/vpn.html","Comparatif des VPN"),("/code-promo/expressvpn.html","Code promo ExpressVPN"),("/code-promo/nordvpn.html","Offres NordVPN"),("/code-promo/surfshark.html","Code promo Surfshark")],
 "assurance":[("/comparatifs/assurance-auto.html","Comparatif assurance auto"),("/comparatifs/assurance-habitation.html","Assurance habitation"),("/comparatifs/mutuelle-sante.html","Mutuelle santé")],
}
CATLABEL={"crypto":"Crypto","bourse":"Bourse","banque":"Banque","compte-pro":"Compte pro","epargne":"Épargne","vpn":"Tech","assurance":"Assurance"}
G=[]
def add(**k): G.append(k)

add(slug="meilleure-assurance-jeune-conducteur",cat="assurance",
 title="Meilleure assurance auto jeune conducteur en 2026",
 desc="Quelle est la meilleure assurance auto pour un jeune conducteur en 2026 ? Surprime, astuces pour payer moins, garanties. Le guide pour assurer un jeune permis pas cher.",
 h1="Meilleure assurance auto pour jeune conducteur",
 lead="Les jeunes conducteurs paient cher leur assurance à cause de la surprime. Voici comment réduire la facture sans sacrifier la couverture.",
 body=H2("surprime","Pourquoi c'est plus cher")
  +P("Un jeune conducteur (permis de moins de 3 ans) subit une <strong>surprime</strong> qui dégresse chaque année sans sinistre. C'est statistique : les profils récents ont plus d'accidents.")
  +H2("astuces","Astuces pour payer moins")
  +UL(["Choisir une <strong>petite voiture</strong> peu puissante.",
       "Opter pour la <strong>conduite accompagnée</strong> réduit la surprime.",
       "Être <strong>second conducteur</strong> sur le contrat d'un parent (avec prudence sur les règles).",
       "Comparer chaque année et privilégier les <strong>formules au kilomètre</strong> si vous roulez peu."])
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/assurance-auto.html\">comparatif assurance auto</a>."),
 faq=[("Comment baisser son assurance jeune conducteur ?","Petite voiture, conduite accompagnée, formules au km, et surtout comparer chaque année. La surprime baisse sans sinistre."),
      ("Combien de temps dure la surprime ?","Elle dégresse en général sur 3 ans sans sinistre responsable."),
      ("Tiers ou tous risques pour un jeune ?","Au tiers pour une voiture d'occasion peu chère ; tous risques si le véhicule a de la valeur.")]),

add(slug="compte-pro-gratuit",cat="compte-pro",
 title="Compte pro gratuit en 2026 : existe-t-il vraiment ?",
 desc="Compte pro gratuit en 2026 : quelles offres sans frais, leurs limites et pour qui c'est suffisant. Le guide honnête sur les comptes professionnels gratuits.",
 h1="Compte pro gratuit : existe-t-il vraiment ?",
 lead="Oui, des comptes pros à 0 €/mois existent — mais avec des limites. Voici ce qu'ils valent et pour qui ils suffisent.",
 body=H2("offres","Les offres gratuites")
  +P("Plusieurs acteurs proposent un <strong>plan d'entrée à 0 €/mois</strong> (Shine, Finom…). Ils incluent un IBAN, une carte et des virements, mais avec des <strong>quotas limités</strong>.")
  +H2("limites","Les limites à connaître")
  +UL(["Nombre de <strong>virements/encaissements</strong> limité, facturé au-delà.",
       "Carte parfois virtuelle ou à fonctionnalités réduites.",
       "Fonctions avancées (compta, sous-comptes) payantes."])
  +H2("pour-qui","Pour qui c'est suffisant ?")
  +P("Pour un <strong>indépendant qui démarre</strong> avec peu de flux, un compte gratuit suffit souvent. Dès que l'activité grossit, un plan payant devient plus rentable que les frais hors forfait.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/comptes-pro.html\">comparatif des comptes pro</a>."),
 faq=[("Existe-t-il un compte pro 100 % gratuit ?","Des offres d'entrée à 0 €/mois existent (Shine, Finom), avec des quotas limités. Au-delà, des frais s'appliquent."),
      ("Un compte gratuit suffit-il pour une société ?","Souvent oui pour démarrer, mais vérifiez le dépôt de capital et les quotas. Les sociétés ont besoin d'un compte dédié."),
      ("Quand passer à un plan payant ?","Quand les frais hors forfait (virements, encaissements) dépassent le coût d'un abonnement.")]),

add(slug="per-ou-assurance-vie",cat="epargne",
 title="PER ou assurance-vie : lequel choisir en 2026 ?",
 desc="PER ou assurance-vie en 2026 : avantage fiscal, disponibilité, succession, fiscalité de sortie. Comparatif clair pour choisir entre PER et assurance-vie selon votre projet.",
 h1="PER ou assurance-vie : lequel choisir ?",
 lead="Les deux servent à épargner sur le long terme, mais leur logique fiscale diffère. Souvent, ils se complètent.",
 body=H2("per","Le PER")
  +UL(["<strong>Avantage fiscal à l'entrée</strong> : versements déductibles du revenu imposable.",
       "<strong>Bloqué jusqu'à la retraite</strong> (hors déblocages anticipés, dont résidence principale).",
       "Idéal pour les <strong>contribuables fortement imposés</strong>."])
  +H2("av","L'assurance-vie")
  +UL(["<strong>Disponible à tout moment</strong>, fiscalité douce après 8 ans.",
       "Atout <strong>succession</strong> majeur.",
       "Plus souple pour des projets à moyen terme."])
  +H2("choisir","Lequel choisir ?")
  +P("Le <strong>PER</strong> si vous êtes fortement imposé et visez la retraite ; l'<strong>assurance-vie</strong> si vous voulez de la souplesse et garder l'argent disponible. Beaucoup combinent les deux.")
  +BOX("💡 Voir notre <a href=\"/guides/per-comment-preparer-retraite.html\">guide PER</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("PER ou assurance-vie en priorité ?","PER si vous êtes fortement imposé et visez la retraite ; assurance-vie pour la souplesse et la disponibilité. Ils sont complémentaires."),
      ("Le PER est-il bloqué ?","Oui, jusqu'à la retraite, sauf cas de déblocage anticipé (achat de la résidence principale notamment)."),
      ("Quelle enveloppe pour la succession ?","L'assurance-vie offre un cadre successoral particulièrement avantageux.")]),

add(slug="scpi-ou-immobilier-locatif",cat="epargne",
 title="SCPI ou immobilier locatif : que choisir en 2026 ?",
 desc="SCPI ou investissement locatif en direct en 2026 : rendement, gestion, ticket d'entrée, risque, liquidité. Comparatif clair pour choisir comment investir dans l'immobilier.",
 h1="SCPI ou immobilier locatif : que choisir ?",
 lead="Investir dans l'immobilier peut se faire en direct (acheter un bien) ou en SCPI (pierre-papier). Deux approches très différentes.",
 body=H2("scpi","La SCPI (pierre-papier)")
  +UL(["<strong>Aucune gestion</strong> : vous percevez des loyers au prorata de vos parts.",
       "<strong>Ticket d'entrée faible</strong> et diversification immédiate.",
       "Accessible aussi <strong>via l'assurance-vie</strong> (frais réduits)."])
  +H2("direct","L'immobilier locatif en direct")
  +UL(["<strong>Effet de levier du crédit</strong> et contrôle total du bien.",
       "Mais <strong>gestion chronophage</strong> (locataires, travaux, vacance).",
       "Ticket d'entrée élevé et risque concentré sur un seul bien."])
  +H2("choisir","Lequel choisir ?")
  +P("La <strong>SCPI</strong> pour investir sans contrainte et diversifier dès quelques centaines d'euros ; l'<strong>immobilier en direct</strong> si vous voulez utiliser le levier du crédit et gérer vous-même.")
  +BOX("💡 Voir notre <a href=\"/guides/linxea-scpi.html\">guide SCPI</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>. La valeur des parts et les loyers ne sont pas garantis."),
 faq=[("SCPI ou locatif en direct ?","La SCPI pour investir sans gestion et diversifier facilement ; le direct pour le levier du crédit et le contrôle, au prix de la gestion."),
      ("Quel rendement pour une SCPI ?","Variable selon les SCPI et le marché ; les performances passées ne préjugent pas du futur."),
      ("Peut-on acheter des SCPI à crédit ?","Oui, certaines SCPI s'achètent à crédit, mais les conditions diffèrent de l'immobilier en direct.")]),

add(slug="meilleur-antivirus",cat="vpn",
 title="Meilleur antivirus en 2026 : comment bien se protéger",
 desc="Quel est le meilleur antivirus en 2026 ? Protection, VPN intégré, prix, gratuit ou payant. Critères et sélection pour sécuriser ses appareils efficacement.",
 h1="Meilleur antivirus : comment bien se protéger",
 lead="Un bon antivirus protège contre virus, phishing et ransomwares. Voici comment choisir, et si le gratuit suffit.",
 body=H2("criteres","Les critères d'un bon antivirus")
  +UL(["<strong>Détection</strong> efficace (résultats des laboratoires indépendants).",
       "<strong>Impact léger</strong> sur les performances.",
       "Outils annexes utiles : <strong>VPN, gestionnaire de mots de passe</strong>, protection web.",
       "Bon rapport qualité/prix sur les licences multi-appareils."])
  +H2("gratuit","Gratuit ou payant ?")
  +P("Les antivirus <strong>gratuits</strong> couvrent l'essentiel pour un usage basique. Les versions <strong>payantes</strong> ajoutent protection web avancée, VPN, contrôle parental et support — utile pour une famille ou un usage intensif.")
  +H2("selection","Les références")
  +P("Bitdefender et Avast figurent parmi les références. Pour la confidentialité, couplez avec un VPN — voir notre <a href=\"/comparatifs/vpn.html\">comparatif des VPN</a> et notre guide <a href=\"/guides/a-quoi-sert-un-vpn.html\">à quoi sert un VPN</a>."),
 faq=[("L'antivirus gratuit suffit-il ?","Pour un usage basique, oui. Pour une protection web avancée, un VPN intégré ou une famille, la version payante est préférable."),
      ("Faut-il un antivirus sur Mac ?","Les Mac sont moins ciblés mais pas invulnérables ; un antivirus reste utile, surtout contre le phishing."),
      ("Antivirus et VPN, est-ce la même chose ?","Non : l'antivirus protège des logiciels malveillants, le VPN chiffre la connexion et masque l'IP. Ils sont complémentaires.")]),

add(slug="meilleure-banque-jeune-actif",cat="banque",
 title="Meilleure banque pour un jeune actif en 2026",
 desc="Quelle est la meilleure banque pour un jeune actif en 2026 ? Frais réduits, appli, épargne, crédit. Critères et sélection pour le premier compte d'un jeune salarié.",
 h1="Meilleure banque pour un jeune actif",
 lead="Premier salaire, premiers projets : un jeune actif a besoin d'une banque peu chère, mobile, et qui accompagne l'épargne et les futurs crédits.",
 body=H2("criteres","Les critères pour un jeune actif")
  +UL(["<strong>Frais réduits</strong> et carte gratuite.",
       "<strong>Appli</strong> moderne avec suivi et sous-comptes.",
       "Accès à l'<strong>épargne</strong> (livrets, assurance-vie) et, à terme, au crédit.",
       "<strong>Prime de bienvenue</strong> appréciable à l'ouverture."])
  +H2("selection","Notre sélection")
  +UL(["<strong>BoursoBank</strong> : banque en ligne complète avec prime de bienvenue.",
       "<strong>N26</strong> / <strong>Revolut</strong> : pour le 100 % mobile et l'international.",
       "Combiner néobanque (au quotidien) et banque en ligne complète (épargne/crédit) est souvent malin."])
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a>."),
 faq=[("Quelle banque pour un premier salaire ?","Une banque en ligne complète (BoursoBank) ou une néobanque (N26, Revolut). Le bon choix dépend de vos besoins d'épargne et de crédit."),
      ("Faut-il quitter sa banque traditionnelle ?","Pas forcément : beaucoup combinent une banque en ligne (frais bas) et gardent l'ancienne pour le crédit immo."),
      ("Les primes de bienvenue valent-elles le coup ?","Elles sont un plus, mais comparez surtout les frais et services sur la durée.")]),

add(slug="comment-resilier-assurance-habitation",cat="assurance",
 title="Comment résilier son assurance habitation en 2026 ?",
 desc="Comment résilier son assurance habitation en 2026 : loi Hamon, déménagement, échéance, démarches. Le guide simple pour changer d'assurance habitation sans stress.",
 h1="Comment résilier son assurance habitation ?",
 lead="Résilier son assurance habitation est simple, surtout après un an grâce à la loi Hamon. Voici les cas et les démarches.",
 body=H2("hamon","Résiliation après un an (loi Hamon)")
  +P("Après la première année, vous pouvez résilier <strong>à tout moment</strong>, sans frais ni justificatif. Le nouvel assureur s'occupe des démarches.")
  +H2("motifs","Résilier en cours d'année")
  +UL(["<strong>Déménagement</strong> ou changement de situation.",
       "<strong>Augmentation de tarif</strong> injustifiée (selon conditions).",
       "Vente du logement."])
  +H2("etapes","Les étapes")
  +OL(["Comparez les offres à garanties équivalentes.",
       "Souscrivez le nouveau contrat.",
       "Le nouvel assureur résilie l'ancien (loi Hamon) ou envoyez votre demande.",
       "Vérifiez la continuité de couverture."])
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/assurance-habitation.html\">comparatif assurance habitation</a>."),
 faq=[("Quand peut-on résilier son assurance habitation ?","À tout moment après un an (loi Hamon), ou en cours d'année pour un motif légitime (déménagement, hausse de tarif…)."),
      ("Qui résilie l'ancien contrat ?","Après un an, le nouvel assureur s'en charge. Sinon, vous envoyez une demande de résiliation."),
      ("L'assurance habitation est-elle obligatoire ?","Elle est obligatoire pour les locataires et en copropriété ; vivement conseillée pour les propriétaires.")]),

add(slug="comment-ouvrir-un-pea",cat="bourse",
 title="Comment ouvrir un PEA en 2026 : étapes et conseils",
 desc="Comment ouvrir un PEA en 2026 : conditions, choix du courtier, versement, premiers ETF. Le guide pas à pas pour ouvrir son plan d'épargne en actions.",
 h1="Comment ouvrir un PEA en 2026",
 lead="Le PEA est l'enveloppe idéale pour investir en actions/ETF européens avec un avantage fiscal. Voici comment l'ouvrir simplement.",
 body=H2("conditions","Les conditions")
  +UL(["Être <strong>majeur et résident fiscal français</strong>.",
       "<strong>Un seul PEA par personne</strong> (plafond 150 000 €).",
       "Investissement limité aux <strong>actions et ETF européens</strong> éligibles."])
  +H2("etapes","Ouvrir un PEA en 4 étapes")
  +OL(["<strong>Choisissez un courtier</strong> ou une banque en ligne (comparez les frais d'ordre).",
       "<strong>Ouvrez le PEA</strong> en ligne (justificatifs d'identité et de domicile).",
       "<strong>Versez</strong> un premier montant (prenez date dès que possible).",
       "<strong>Investissez</strong> progressivement, par exemple sur un ETF World éligible."])
  +H2("date","Pourquoi prendre date tôt")
  +P("L'avantage fiscal du PEA (exonération d'IR sur les gains) s'obtient <strong>après 5 ans</strong>. Ouvrir tôt, même avec un petit versement, lance le compteur.")
  +BOX("💡 Voir <a href=\"/guides/meilleur-courtier-pea.html\">meilleur courtier PEA</a> et <a href=\"/guides/pea-ou-compte-titres.html\">PEA ou compte-titres</a>. Investir comporte un risque de perte en capital."),
 faq=[("Qui peut ouvrir un PEA ?","Toute personne majeure résidente fiscale française, à raison d'un seul PEA par personne."),
      ("Quel montant pour ouvrir un PEA ?","Souvent quelques dizaines d'euros suffisent. L'important est de prendre date tôt pour l'avantage fiscal."),
      ("Quand le PEA devient-il avantageux ?","Après 5 ans, les gains sont exonérés d'impôt sur le revenu (hors prélèvements sociaux).")]),

add(slug="comment-devenir-auto-entrepreneur",cat="compte-pro",
 title="Comment devenir auto-entrepreneur en 2026 : guide complet",
 desc="Comment devenir auto-entrepreneur en 2026 : démarches d'inscription, cotisations, compte dédié, facturation, TVA. Le guide pas à pas pour se lancer en micro-entreprise.",
 h1="Comment devenir auto-entrepreneur en 2026",
 lead="La micro-entreprise est le statut le plus simple pour se lancer. Voici les étapes, des démarches à la gestion au quotidien.",
 body=H2("etapes","S'inscrire en micro-entreprise")
  +OL(["<strong>Vérifiez</strong> que votre activité est éligible au régime.",
       "<strong>Déclarez l'activité</strong> sur le guichet unique de l'INPI.",
       "Obtenez votre <strong>SIRET</strong> et choisissez vos options fiscales (versement libératoire, TVA…).",
       "Ouvrez un <strong>compte dédié</strong> (obligatoire au-delà de 10 000 € de CA pendant 2 ans)."])
  +H2("gestion","La gestion au quotidien")
  +UL(["Émettre des <strong>factures conformes</strong> (mentions légales).",
       "Déclarer son <strong>chiffre d'affaires</strong> à l'URSSAF (mensuel ou trimestriel).",
       "Suivre les <strong>seuils de TVA</strong> et de CA.",
       "Provisionner cotisations et impôt."])
  +BOX("💡 Voir notre <a href=\"/guides/compte-pro-obligatoire-micro-entreprise.html\">guide compte pro micro-entreprise</a>, notre <a href=\"/comparatifs/comptes-pro.html\">comparatif comptes pro</a> et nos <a href=\"/outils/checklist-independant.html\">outils pour indépendants</a>."),
 faq=[("Comment s'inscrire en auto-entrepreneur ?","Via le guichet unique de l'INPI. L'inscription est gratuite et 100 % en ligne."),
      ("Faut-il un compte pro en micro-entreprise ?","Un compte dédié devient obligatoire au-delà de 10 000 € de CA pendant deux ans, mais pas forcément un compte « pro » payant."),
      ("Quelles charges paie un auto-entrepreneur ?","Des cotisations sociales calculées en % du chiffre d'affaires, plus l'impôt (barème ou versement libératoire).")]),

add(slug="comment-acheter-ethereum",cat="crypto",
 title="Comment acheter de l'Ethereum (ETH) en 2026 : guide débutant",
 desc="Comment acheter de l'Ethereum (ETH) en 2026 : choisir une application, créer un compte, premier achat, frais, staking et sécurité. Le guide pas à pas pour acheter de l'ETH.",
 h1="Comment acheter de l'Ethereum (ETH) en 2026",
 lead="L'Ethereum est la 2e cryptomonnaie et la plus utilisée pour les applications décentralisées. Voici comment en acheter simplement.",
 body=H2("etapes","Acheter de l'ETH en 5 étapes")
  +OL(["<strong>Choisissez une application crypto</strong> régulée (voir notre comparatif).",
       "<strong>Créez un compte</strong> et validez votre identité (KYC).",
       "<strong>Déposez des euros</strong> par virement SEPA (moins cher que la carte).",
       "Achetez l'<strong>ETH</strong> via l'interface pro pour réduire les frais.",
       "<strong>Sécurisez</strong> (2FA, voire portefeuille externe)."])
  +H2("staking","Le staking d'Ethereum")
  +P("L'ETH peut être <strong>staké</strong> pour percevoir une récompense (preuve d'enjeu). Le rendement n'est pas garanti et des conditions de déblocage s'appliquent.")
  +H2("frais","Réduire les frais")
  +P("Comme pour le Bitcoin, privilégiez l'interface pro et le virement SEPA. Voir notre <a href=\"/etudes/barometre-frais-crypto.html\">baromètre des frais crypto</a>.")
  +BOX("⚠️ Investir dans les crypto-actifs comporte un risque de perte en capital. Voir aussi <a href=\"/guides/bitcoin-vs-ethereum.html\">Bitcoin ou Ethereum</a>."),
 faq=[("Quel est le minimum pour acheter de l'ETH ?","Très faible : vous pouvez acheter une fraction d'Ethereum et commencer avec quelques euros."),
      ("Peut-on staker son Ethereum ?","Oui, l'ETH fonctionne en preuve d'enjeu et peut être staké. Le rendement est variable et des conditions s'appliquent."),
      ("Où acheter de l'Ethereum au meilleur prix ?","Privilégiez l'interface pro et le virement SEPA. Comparez les frais dans notre baromètre et notre comparatif crypto.")]),

add(slug="comment-resilier-mutuelle",cat="assurance",
 title="Comment résilier sa mutuelle santé en 2026 ?",
 desc="Comment résilier sa mutuelle santé en 2026 : résiliation infra-annuelle après un an, démarches, changement. Le guide simple pour changer de complémentaire santé.",
 h1="Comment résilier sa mutuelle santé ?",
 lead="Depuis la résiliation infra-annuelle, changer de mutuelle après un an est simple et gratuit. Voici comment procéder.",
 body=H2("regle","Résiliation après un an")
  +P("Après <strong>un an d'adhésion</strong>, vous pouvez résilier votre mutuelle <strong>à tout moment</strong>, sans frais ni justificatif. La nouvelle mutuelle peut s'occuper des démarches.")
  +H2("etapes","Les étapes")
  +OL(["Comparez les offres adaptées à vos besoins.",
       "Souscrivez la nouvelle mutuelle.",
       "Demandez la résiliation de l'ancienne (ou laissez la nouvelle le faire).",
       "Vérifiez la date d'effet pour éviter tout trou de couverture."])
  +H2("conseil","Le bon réflexe")
  +P("Profitez du changement pour <strong>réajuster vos garanties</strong> à vos besoins réels (optique, dentaire, hospitalisation), c'est là que se font les économies.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/mutuelle-sante.html\">comparatif mutuelle santé</a> et voir <a href=\"/guides/comment-choisir-mutuelle-sante.html\">comment choisir sa mutuelle</a>."),
 faq=[("Quand peut-on résilier sa mutuelle ?","À tout moment après un an d'adhésion, grâce à la résiliation infra-annuelle, sans frais."),
      ("Qui s'occupe de la résiliation ?","La nouvelle mutuelle peut prendre en charge la résiliation de l'ancienne."),
      ("Peut-on résilier une mutuelle d'entreprise ?","La mutuelle d'entreprise obligatoire suit des règles spécifiques ; la résiliation libre concerne surtout les contrats individuels.")]),

add(slug="meilleur-courtier-debutant",cat="bourse",
 title="Meilleur courtier en bourse pour débutant en 2026",
 desc="Quel est le meilleur courtier en bourse pour un débutant en 2026 ? Frais bas, simplicité, PEA, ETF. Critères et sélection pour bien choisir où débuter en bourse.",
 h1="Meilleur courtier en bourse pour débutant",
 lead="Pour débuter, l'idéal est un courtier simple, peu cher et qui propose le PEA et les ETF. Voici comment choisir.",
 body=H2("criteres","Les critères pour un débutant")
  +UL(["<strong>Frais d'ordre bas</strong> et pas de droits de garde.",
       "<strong>Application simple</strong> et pédagogique.",
       "<strong>Éligibilité PEA</strong> et accès aux ETF.",
       "Possibilité de <strong>versements programmés</strong>."])
  +H2("selection","Notre sélection")
  +UL(["<strong>Trade Republic</strong> : plans d'épargne automatiques en ETF, très simple.",
       "<strong>XTB</strong> : 0 % de commission actions (jusqu'à un seuil), plateforme complète.",
       "<strong>DEGIRO</strong> : low-cost avec un large choix."])
  +BOX("💡 Voir <a href=\"/guides/comment-investir-en-bourse-debutant.html\">comment investir en bourse</a> et le <a href=\"/comparatifs/trading-bourse.html\">comparatif des courtiers</a>. Investir comporte un risque de perte en capital."),
 faq=[("Quel courtier pour débuter en bourse ?","Trade Republic pour la simplicité et les plans d'épargne, XTB pour le 0 % commission, DEGIRO pour le low-cost. Comparez selon vos besoins."),
      ("Faut-il choisir un courtier avec PEA ?","Oui si vous visez les actions/ETF européens : le PEA offre un avantage fiscal après 5 ans."),
      ("Combien faut-il pour commencer ?","Quelques dizaines d'euros suffisent grâce aux ETF et aux courtiers sans minimum élevé.")])

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
print("batch 4 guides créés :", len(G))
