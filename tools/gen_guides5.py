#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 5 : long-tail supplementaire."""
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
 "compte-pro":[("/comparatifs/comptes-pro.html","Comparatif des comptes pro"),("/comparatifs/facturation.html","Logiciels de facturation"),("/code-promo/qonto.html","Code promo Qonto"),("/code-promo/shine.html","Offres Shine")],
 "epargne":[("/comparatifs/assurance-vie.html","Comparatif assurance-vie"),("/comparatifs/per-retraite.html","Comparatif PER"),("/code-promo/linxea.html","Code promo Linxea"),("/code-promo/yomoni.html","Offres Yomoni")],
 "credit":[("/comparatifs/credit-conso.html","Comparatif crédit conso"),("/comparatifs/rachat-credit.html","Rachat de crédit"),("/comparatifs/courtage-immobilier.html","Courtage immobilier"),("/comparatifs/assurance-emprunteur.html","Assurance emprunteur")],
 "energie":[("/comparatifs/fournisseur-energie.html","Comparatif fournisseurs d'énergie"),("/comparatifs/kit-solaire-autoconsommation.html","Kit solaire")],
}
CATLABEL={"crypto":"Crypto","bourse":"Bourse","banque":"Banque","compte-pro":"Compte pro","epargne":"Épargne","credit":"Crédit","energie":"Énergie"}
G=[]
def add(**k): G.append(k)

add(slug="staking-crypto-comment-ca-marche",cat="crypto",
 title="Le staking crypto : comment ça marche en 2026 ?",
 desc="Le staking crypto en 2026 : principe, rendement, cryptos éligibles, risques et fiscalité. Le guide clair pour comprendre comment faire travailler ses cryptoactifs.",
 h1="Le staking crypto : comment ça marche ?",
 lead="Le staking permet de générer un rendement avec ses cryptos, sans les vendre. Voici son fonctionnement et ses limites.",
 body=H2("principe","Le principe du staking")
  +P("Le <strong>staking</strong> consiste à immobiliser des cryptos en preuve d'enjeu pour participer à la sécurisation d'un réseau et percevoir une <strong>récompense</strong>. C'est une forme de rendement, mais pas sans risque.")
  +H2("cryptos","Quelles cryptos peut-on staker ?")
  +P("Principalement des actifs en preuve d'enjeu : <strong>Ethereum, Solana, Cardano, Polkadot…</strong> Le rendement annuel estimé varie selon l'actif et le réseau.")
  +H2("risques","Les risques")
  +UL(["Le <strong>rendement n'est pas garanti</strong>.","Certaines cryptos imposent une <strong>période de déblocage</strong>.","La <strong>valeur de l'actif</strong> peut baisser.","Les récompenses sont <strong>imposables</strong>."])
  +BOX("⚠️ Investir comporte un risque de perte en capital. Voir notre <a href=\"/comparatifs/crypto.html\">comparatif crypto</a> et <a href=\"/guides/declarer-cryptomonnaies-impots.html\">la fiscalité crypto</a>."),
 faq=[("Le staking est-il sans risque ?","Non : rendement non garanti, possible blocage des fonds et risque de marché. Le staking ne supprime pas la volatilité."),
      ("Quel rendement espérer ?","Cela dépend de la crypto et du réseau ; les taux affichés sont des estimations variables, jamais des promesses."),
      ("Peut-on staker le Bitcoin ?","Non, le Bitcoin n'est pas en preuve d'enjeu. Le staking concerne Ethereum, Solana et d'autres.")]),

add(slug="compte-sans-banque",cat="banque",
 title="Compte sans banque en 2026 : comment en ouvrir un ?",
 desc="Compte sans banque en 2026 : solutions accessibles sans conditions de revenus ni découvert, pour interdit bancaire ou ouverture rapide. Le guide des comptes alternatifs.",
 h1="Compte sans banque : comment en ouvrir un ?",
 lead="Besoin d'un compte rapide, sans conditions de revenus ni risque de refus ? Des solutions existent, notamment pour les interdits bancaires.",
 body=H2("solutions","Les solutions de compte sans banque")
  +UL(["<strong>Comptes ouvrables chez le buraliste</strong> (type Nickel) : sans condition de revenus.",
       "<strong>Néobanques</strong> à ouverture simplifiée (N26, Revolut, Sogexia…).",
       "Ces comptes offrent un IBAN, une carte et des paiements, sans découvert ni crédit."])
  +H2("interdit","Pour un interdit bancaire")
  +P("Même en cas d'<strong>interdiction bancaire</strong> (fichage Banque de France), ces comptes restent souvent accessibles car ils ne proposent ni découvert ni chéquier. Le <strong>droit au compte</strong> garantit aussi un accès à un compte de base.")
  +H2("limites","Les limites")
  +P("Pas de découvert autorisé, pas de crédit, dépôt d'espèces parfois limité. Pour ces besoins, une banque classique reste nécessaire.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a>."),
 faq=[("Peut-on avoir un compte en étant interdit bancaire ?","Oui : les comptes sans découvert (Nickel, certaines néobanques) restent accessibles, et le droit au compte garantit un compte de base."),
      ("Un compte sans banque a-t-il un IBAN ?","Oui, ces comptes fournissent un IBAN pour recevoir un salaire et payer."),
      ("Y a-t-il des conditions de revenus ?","Non pour la plupart de ces comptes, qui s'ouvrent sans justificatif de revenus.")]),

add(slug="meilleure-assurance-moto",cat="credit",
 title="Meilleure assurance moto en 2026 : comment bien choisir",
 desc="Quelle est la meilleure assurance moto en 2026 ? Formules (tiers, tous risques), garanties, équipement, économies. Le guide pour assurer sa moto au meilleur prix.",
 h1="Meilleure assurance moto : comment bien choisir",
 lead="Assurer sa moto au bon prix demande de choisir la bonne formule et les bonnes garanties selon l'usage et la valeur du véhicule.",
 body=H2("formules","Tiers ou tous risques ?")
  +UL(["<strong>Au tiers</strong> : minimum légal, adapté aux motos anciennes ou peu chères.",
       "<strong>Intermédiaire</strong> : tiers + vol, incendie, bris de glace.",
       "<strong>Tous risques</strong> : couverture maximale, pour une moto récente ou de valeur."])
  +H2("garanties","Les garanties à regarder")
  +UL(["Garantie <strong>équipement du pilote</strong> (casque, blouson).",
       "<strong>Assistance</strong> et prêt de véhicule.",
       "Franchises et plafonds."])
  +H2("economiser","Payer moins cher")
  +P("Comparez chaque année, adaptez la formule à la valeur réelle de la moto, et profitez du <strong>bonus-malus</strong>. Une moto bien protégée (antivol) peut réduire la prime.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/assurance-auto.html\">comparatif assurance</a>."),
 faq=[("Tiers ou tous risques pour une moto ?","Au tiers pour une moto ancienne ou de faible valeur ; tous risques pour une moto récente ou chère."),
      ("L'assurance moto est-elle obligatoire ?","Oui, au minimum la responsabilité civile (au tiers) est obligatoire pour circuler."),
      ("Comment payer moins cher son assurance moto ?","Adapter la formule, comparer chaque année, sécuriser la moto (antivol) et soigner son bonus.")]),

add(slug="meilleur-logiciel-facturation-auto-entrepreneur",cat="compte-pro",
 title="Meilleur logiciel de facturation pour auto-entrepreneur (2026)",
 desc="Quel est le meilleur logiciel de facturation pour auto-entrepreneur en 2026 ? Devis, factures conformes, suivi URSSAF, prix. Critères et sélection pour bien gérer.",
 h1="Meilleur logiciel de facturation pour auto-entrepreneur",
 lead="Un bon logiciel de facturation fait gagner du temps et garantit des factures conformes. Voici comment choisir selon vos besoins.",
 body=H2("criteres","Les critères de choix")
  +UL(["<strong>Factures conformes</strong> (mentions légales obligatoires).",
       "<strong>Devis, relances</strong> et suivi des paiements.",
       "<strong>Suivi du chiffre d'affaires</strong> et aide à la déclaration URSSAF.",
       "Prix adapté (certaines apps de compte pro l'incluent gratuitement)."])
  +H2("selection","Nos pistes")
  +P("Des outils dédiés (Abby, Freebe, Tiime…) et certains comptes pros (Shine, Qonto) intègrent la facturation. Pour de la compta complète, voir notre <a href=\"/comparatifs/logiciels-comptabilite.html\">comparatif comptabilité</a> et notre <a href=\"/comparatifs/facturation.html\">comparatif facturation</a>.")
  +BOX("💡 Voir aussi notre <a href=\"/guides/comment-devenir-auto-entrepreneur.html\">guide auto-entrepreneur</a> et notre <a href=\"/outils/checklist-independant.html\">checklist indépendant</a>."),
 faq=[("Quel logiciel de facturation pour auto-entrepreneur ?","Des outils dédiés (Abby, Freebe, Tiime) ou un compte pro avec facturation intégrée (Shine, Qonto). Le choix dépend de vos besoins."),
      ("La facturation conforme est-elle obligatoire ?","Oui, vos factures doivent comporter les mentions légales obligatoires. Un logiciel les génère automatiquement."),
      ("Existe-t-il des logiciels gratuits ?","Certains comptes pros incluent la facturation gratuitement ; des outils proposent aussi des formules gratuites limitées.")]),

add(slug="comment-changer-assurance-emprunteur",cat="credit",
 title="Comment changer d'assurance emprunteur en 2026 (loi Lemoine) ?",
 desc="Comment changer d'assurance emprunteur en 2026 : loi Lemoine, résiliation à tout moment, économies sur le crédit immobilier. Le guide pour faire baisser le coût de son prêt.",
 h1="Comment changer d'assurance emprunteur (loi Lemoine) ?",
 lead="Changer l'assurance de son prêt immobilier peut faire économiser plusieurs milliers d'euros. La loi Lemoine a tout simplifié.",
 body=H2("lemoine","La loi Lemoine en bref")
  +P("Depuis la <strong>loi Lemoine</strong>, vous pouvez <strong>changer d'assurance emprunteur à tout moment</strong>, sans frais ni attendre une date anniversaire. La nouvelle assurance doit offrir des garanties équivalentes.")
  +H2("economie","Pourquoi c'est rentable")
  +P("L'assurance emprunteur représente une part importante du coût d'un crédit immobilier. La déléguer à un assureur moins cher (à garanties égales) peut faire <strong>économiser plusieurs milliers d'euros</strong> sur la durée du prêt.")
  +H2("etapes","Les étapes")
  +OL(["Comparez les offres à <strong>garanties équivalentes</strong>.",
       "Souscrivez la nouvelle assurance.",
       "Envoyez la demande de substitution à votre banque.",
       "La banque doit accepter si l'équivalence des garanties est respectée."])
  +BOX("💡 Voir notre <a href=\"/comparatifs/assurance-emprunteur.html\">comparatif assurance emprunteur</a> et notre <a href=\"/comparatifs/courtage-immobilier.html\">comparatif courtage immobilier</a>."),
 faq=[("Quand changer d'assurance emprunteur ?","À tout moment grâce à la loi Lemoine, sans frais, tant que les garanties restent équivalentes."),
      ("Combien peut-on économiser ?","Souvent plusieurs milliers d'euros sur la durée du prêt en déléguant à un assureur moins cher à garanties égales."),
      ("La banque peut-elle refuser ?","Seulement si les garanties ne sont pas équivalentes. Sinon, elle doit accepter la substitution.")]),

add(slug="comment-investir-dans-immobilier",cat="epargne",
 title="Comment investir dans l'immobilier en 2026 : les options",
 desc="Comment investir dans l'immobilier en 2026 : locatif en direct, SCPI, crowdfunding immobilier, SCI. Le guide clair pour choisir la meilleure façon d'investir dans la pierre.",
 h1="Comment investir dans l'immobilier en 2026 ?",
 lead="Investir dans l'immobilier ne se résume pas à acheter un appartement. Voici les principales options selon votre budget et votre temps.",
 body=H2("options","Les façons d'investir")
  +UL(["<strong>Locatif en direct</strong> : effet de levier du crédit, mais gestion chronophage.",
       "<strong>SCPI</strong> : pierre-papier, sans gestion, dès quelques centaines d'euros.",
       "<strong>Crowdfunding immobilier</strong> : financer des projets à court terme (risqué).",
       "<strong>SCI</strong> : structurer un investissement à plusieurs ou transmettre."])
  +H2("choisir","Comment choisir")
  +P("Tout dépend de votre <strong>budget</strong>, votre <strong>temps disponible</strong> et votre <strong>tolérance au risque</strong>. La SCPI est la plus accessible et passive ; le locatif en direct offre le levier du crédit.")
  +BOX("💡 Voir <a href=\"/guides/scpi-ou-immobilier-locatif.html\">SCPI ou locatif</a> et notre <a href=\"/comparatifs/crowdlending-p2p.html\">comparatif crowdfunding</a>. La valeur des biens et les revenus ne sont pas garantis."),
 faq=[("Quelle est la façon la plus simple d'investir dans l'immobilier ?","La SCPI : accessible dès quelques centaines d'euros, sans gestion, et diversifiée."),
      ("Peut-on investir dans l'immobilier avec peu d'argent ?","Oui, via les SCPI ou le crowdfunding immobilier, accessibles avec de petits montants."),
      ("L'immobilier est-il sans risque ?","Non : la valeur des biens, les loyers et la liquidité ne sont pas garantis, surtout sur le crowdfunding.")]),

add(slug="comment-reduire-facture-energie",cat="energie",
 title="Comment réduire sa facture d'énergie en 2026 ?",
 desc="Comment réduire sa facture d'électricité et de gaz en 2026 : changer de fournisseur, écogestes, heures creuses, isolation. Le guide concret pour payer moins cher l'énergie.",
 h1="Comment réduire sa facture d'énergie ?",
 lead="Entre le choix du fournisseur et quelques bons réflexes, on peut réduire sensiblement sa facture d'énergie. Voici comment.",
 body=H2("fournisseur","1. Changer de fournisseur")
  +P("Le geste le plus rapide : <strong>comparer et changer de fournisseur</strong>, gratuitement et sans coupure. Certaines offres (dont des vertes) sont bien moins chères que le tarif réglementé.")
  +H2("ecogestes","2. Les écogestes qui comptent")
  +UL(["Chauffer à la bonne température (1 °C de moins = économies notables).",
       "Profiter des <strong>heures creuses</strong> pour les gros appareils.",
       "Traquer les <strong>appareils en veille</strong>.",
       "Entretenir chaudière et radiateurs."])
  +H2("long-terme","3. Les investissements rentables")
  +P("L'<strong>isolation</strong>, un thermostat connecté ou des panneaux solaires en autoconsommation réduisent durablement la facture.")
  +BOX("💡 Comparez les fournisseurs dans notre <a href=\"/comparatifs/fournisseur-energie.html\">comparatif</a> et voir <a href=\"/guides/comment-changer-fournisseur-energie.html\">comment changer de fournisseur</a>."),
 faq=[("Comment baisser rapidement sa facture d'énergie ?","Changer de fournisseur (gratuit, sans coupure) est le geste le plus rapide, complété par quelques écogestes."),
      ("Les offres vertes sont-elles plus chères ?","Pas forcément : certaines offres d'électricité verte sont parmi les moins chères du marché."),
      ("L'autoconsommation solaire est-elle rentable ?","Sur la durée, oui selon votre consommation et l'ensoleillement, avec un investissement initial à amortir.")]),

add(slug="hot-wallet-ou-cold-wallet",cat="crypto",
 title="Hot wallet ou cold wallet : quel portefeuille crypto choisir ?",
 desc="Hot wallet ou cold wallet en 2026 : différences, sécurité, usages. Le guide clair pour choisir où stocker ses cryptomonnaies en sécurité selon vos montants.",
 h1="Hot wallet ou cold wallet : que choisir ?",
 lead="Où stocker ses cryptos ? Entre le portefeuille connecté (hot) et le portefeuille hors ligne (cold), le choix dépend surtout des montants.",
 body=H2("hot","Le hot wallet (connecté)")
  +UL(["Application ou wallet en ligne, <strong>pratique au quotidien</strong>.",
       "Idéal pour de <strong>petits montants</strong> et des transactions fréquentes.",
       "Plus exposé aux piratages car connecté à Internet."])
  +H2("cold","Le cold wallet (hors ligne)")
  +UL(["Portefeuille physique (hardware), <strong>déconnecté d'Internet</strong>.",
       "<strong>Sécurité maximale</strong> pour conserver de gros montants sur le long terme.",
       "Moins pratique pour les transactions fréquentes."])
  +H2("choisir","La règle simple")
  +P("Petits montants et usage courant : <strong>hot wallet</strong> (ou la plateforme). Gros montants conservés longtemps : <strong>cold wallet</strong>. Ne partagez jamais votre phrase de récupération.")
  +BOX("💡 Voir notre <a href=\"/comparatifs/crypto.html\">comparatif des applications crypto</a> et <a href=\"/guides/comment-acheter-cryptomonnaies.html\">comment acheter des cryptos</a>."),
 faq=[("Hot ou cold wallet, lequel est plus sûr ?","Le cold wallet (hors ligne) est plus sûr pour de gros montants. Le hot wallet est plus pratique pour le quotidien."),
      ("Faut-il un hardware wallet ?","Recommandé dès que vous conservez des montants importants sur le long terme."),
      ("Mes cryptos sont-elles en sécurité sur une plateforme ?","Les bonnes plateformes sécurisent les fonds, mais pour de gros montants, un portefeuille personnel offre plus de contrôle.")]),

add(slug="meilleur-per",cat="epargne",
 title="Meilleur PER en 2026 : comment choisir son plan d'épargne retraite",
 desc="Quel est le meilleur PER en 2026 ? Frais d'entrée, gestion, supports (ETF, fonds euros), fiscalité. Critères et sélection pour bien choisir son plan d'épargne retraite.",
 h1="Meilleur PER : comment choisir",
 lead="Un bon PER, c'est zéro frais d'entrée, des frais de gestion bas et de bons supports. Voici comment choisir.",
 body=H2("criteres","Les critères d'un bon PER")
  +UL(["<strong>0 % de frais d'entrée</strong> et de versement.",
       "<strong>Frais de gestion bas</strong> sur les unités de compte.",
       "Bon <strong>fonds euros</strong> et large choix d'<strong>ETF</strong>.",
       "Gestion <strong>libre ou pilotée</strong> selon votre profil."])
  +H2("selection","Nos pistes")
  +P("Les PER des acteurs en ligne (Linxea, Yomoni, Nalo…) se distinguent par des frais bas. Le bon choix dépend de votre fiscalité et de votre horizon. Voir notre <a href=\"/comparatifs/per-retraite.html\">comparatif PER</a>.")
  +H2("rappel","L'avantage fiscal")
  +P("Les versements sont <strong>déductibles du revenu imposable</strong> (dans certaines limites). Le PER est surtout gagnant si votre tranche d'imposition baisse à la retraite.")
  +BOX("💡 Voir notre <a href=\"/guides/per-comment-preparer-retraite.html\">guide PER</a> et <a href=\"/guides/per-ou-assurance-vie.html\">PER ou assurance-vie</a>."),
 faq=[("Quel est le meilleur PER ?","Celui à 0 % de frais d'entrée, frais de gestion bas et bons supports. Les PER en ligne (Linxea, Yomoni, Nalo) sont compétitifs."),
      ("Le PER est-il intéressant pour tout le monde ?","Surtout pour les contribuables fortement imposés. Moins intéressant si votre tranche est faible."),
      ("Peut-on transférer un ancien PER ?","Oui, les anciens contrats retraite peuvent généralement être transférés vers un PER, parfois avec des frais.")]),

add(slug="comment-reduire-ses-impots",cat="epargne",
 title="Comment réduire ses impôts en 2026 : les placements à connaître",
 desc="Comment réduire ses impôts en 2026 : PER, déficit foncier, dispositifs de défiscalisation, dons. Le guide clair des leviers légaux pour payer moins d'impôt.",
 h1="Comment réduire ses impôts en 2026 ?",
 lead="Plusieurs dispositifs légaux permettent de réduire son impôt. Voici les principaux leviers, à adapter à votre situation.",
 body=H2("per","Le PER : déduction à l'entrée")
  +P("Les versements sur un <strong>PER</strong> sont déductibles du revenu imposable (dans certaines limites) : l'un des leviers les plus simples pour les contribuables imposés.")
  +H2("autres","Les autres dispositifs")
  +UL(["<strong>Investissement locatif</strong> et déficit foncier.",
       "<strong>Dons</strong> à des associations (réduction d'impôt).",
       "Dispositifs de défiscalisation (à étudier avec prudence et selon l'actualité fiscale).",
       "Emploi à domicile (crédit d'impôt)."])
  +H2("attention","Le bon réflexe")
  +P("Ne défiscalisez jamais pour la seule réduction d'impôt : un placement doit d'abord être <strong>bon en soi</strong>. L'avantage fiscal est un bonus, pas un objectif.")
  +BOX("💡 Information générale, pas un conseil personnalisé. Voir notre <a href=\"/comparatifs/per-retraite.html\">comparatif PER</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Quel est le moyen le plus simple de réduire ses impôts ?","Le PER, dont les versements sont déductibles du revenu imposable, est l'un des leviers les plus accessibles pour les contribuables imposés."),
      ("Faut-il défiscaliser à tout prix ?","Non : un placement doit être bon en soi. L'avantage fiscal ne doit pas être la seule motivation."),
      ("L'assurance-vie réduit-elle l'impôt ?","Elle n'offre pas de déduction à l'entrée, mais une fiscalité avantageuse sur les gains après 8 ans.")]),

add(slug="meilleur-taux-credit-immobilier",cat="credit",
 title="Comment obtenir le meilleur taux pour un crédit immobilier (2026) ?",
 desc="Comment obtenir le meilleur taux pour un crédit immobilier en 2026 : apport, profil, courtier, négociation, assurance emprunteur. Le guide pour emprunter au meilleur coût.",
 h1="Comment obtenir le meilleur taux immobilier ?",
 lead="Le taux n'est qu'une partie du coût d'un crédit immobilier. Voici comment optimiser l'ensemble pour emprunter au meilleur prix.",
 body=H2("profil","Soigner son profil")
  +UL(["Un <strong>apport</strong> conséquent rassure la banque.",
       "Des <strong>finances saines</strong> (pas de découverts, taux d'endettement maîtrisé).",
       "Une <strong>situation stable</strong>."])
  +H2("courtier","Faire jouer la concurrence")
  +P("Mettre les banques en concurrence, directement ou via un <strong>courtier</strong>, permet souvent d'obtenir un meilleur taux. Le courtier négocie aussi les frais annexes.")
  +H2("assurance","Ne pas négliger l'assurance")
  +P("L'<strong>assurance emprunteur</strong> pèse lourd dans le coût total. La déléguer (loi Lemoine) à garanties égales peut faire économiser des milliers d'euros — voir <a href=\"/guides/comment-changer-assurance-emprunteur.html\">notre guide</a>.")
  +BOX("💡 Voir notre <a href=\"/comparatifs/courtage-immobilier.html\">comparatif courtage immobilier</a> et le <a href=\"/comparatifs/assurance-emprunteur.html\">comparatif assurance emprunteur</a>."),
 faq=[("Comment négocier son taux immobilier ?","Soignez votre profil (apport, finances saines), mettez les banques en concurrence et passez éventuellement par un courtier."),
      ("Le taux est-il le seul critère ?","Non : l'assurance emprunteur et les frais annexes pèsent aussi lourd. Comparez le coût total."),
      ("Un courtier est-il utile ?","Souvent oui : il met les banques en concurrence et peut obtenir de meilleures conditions, y compris sur l'assurance.")]),

add(slug="comment-choisir-un-etf",cat="bourse",
 title="Comment choisir un ETF en 2026 : le guide pour bien débuter",
 desc="Comment choisir un ETF en 2026 : indice, frais (TER), réplication, capitalisant ou distribuant, éligibilité PEA. Le guide clair pour sélectionner ses trackers.",
 h1="Comment choisir un ETF en 2026 ?",
 lead="Tous les ETF ne se valent pas. Voici les critères qui comptent vraiment pour bien choisir ses trackers.",
 body=H2("criteres","Les critères essentiels")
  +UL(["<strong>L'indice répliqué</strong> (MSCI World, S&amp;P 500, CAC 40…) : c'est l'exposition.",
       "<strong>Les frais (TER)</strong> : plus ils sont bas, mieux c'est.",
       "<strong>Capitalisant ou distribuant</strong> : réinvestit les dividendes ou les verse.",
       "<strong>Éligibilité PEA</strong> si vous investissez dans cette enveloppe.",
       "La <strong>taille de l'ETF</strong> (encours) et la qualité de l'émetteur."])
  +H2("debuter","Pour débuter simplement")
  +P("Un <strong>ETF World</strong> (type MSCI World) capitalisant et à frais bas est l'option la plus simple pour une exposition diversifiée mondiale, en cœur de portefeuille.")
  +BOX("💡 Voir <a href=\"/guides/etf-vs-actions.html\">ETF ou actions</a>, <a href=\"/guides/comment-investir-en-bourse-debutant.html\">comment investir en bourse</a> et le <a href=\"/comparatifs/courtier-etf.html\">comparatif courtier ETF</a>. Investir comporte un risque de perte en capital."),
 faq=[("Quel ETF choisir pour débuter ?","Un ETF World capitalisant à frais bas, pour une exposition mondiale diversifiée en cœur de portefeuille."),
      ("Capitalisant ou distribuant ?","Capitalisant pour faire croître le capital sans gérer les dividendes ; distribuant si vous voulez percevoir un revenu."),
      ("Comment savoir si un ETF est éligible au PEA ?","L'éligibilité PEA est indiquée par l'émetteur ; privilégiez les ETF éligibles si vous investissez via un PEA.")])

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
print("batch 5 guides créés :", len(G))
