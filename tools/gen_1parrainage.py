#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Curation 1parrainage (verticales Selectum) : avis + code-promo + parrainage
par marque, + 6 comparateurs de niche. Liens /go non trackés (à brancher ensuite)."""
import os, html, json, urllib.request, subprocess

FONT = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D = "12 juin 2026"
ORG = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Organization", "name": "Selectum", "url": "https://selectum.fr/", "logo": "https://selectum.fr/assets/selectum-logo.png", "description": "Comparatifs et avis indépendants : banque, bourse, crypto, assurance, crédit, énergie et logiciels."}</script>'
WS = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "WebSite", "name": "Selectum", "url": "https://selectum.fr/", "inLanguage": "fr-FR"}</script>'

# vertical -> (label, comparatif_url, comparatif_label, risk, pros[], cons[], pour_qui)
VERT = {
 "neobank": ("néobanque", "/comparatifs/banque-en-ligne.html", "comparatif banque en ligne", False,
   ["Compte et carte gérés depuis une application mobile soignée", "Ouverture rapide en ligne", "Frais souvent réduits par rapport aux banques traditionnelles"],
   ["Réseau d'agences inexistant", "Dépôt d'espèces limité ou impossible"],
   "particuliers à l'aise avec le 100 % mobile et cherchant à réduire leurs frais"),
 "pro-bank": ("compte pro", "/comparatifs/comptes-pro.html", "comparatif comptes pro", False,
   ["Ouverture rapide, IBAN dédié", "Outils de gestion (cartes, dépenses, parfois facturation)", "Tarifs lisibles"],
   ["Pas toujours de découvert ou de crédit", "Dépôt d'espèces limité"],
   "indépendants, TPE et sociétés cherchant un compte professionnel en ligne"),
 "crypto": ("plateforme crypto", "/comparatifs/crypto.html", "comparatif crypto", True,
   ["Achat et vente de cryptomonnaies", "Application et parcours d'inscription modernes", "Mesures de sécurité (2FA, stockage à froid selon l'acteur)"],
   ["Frais variables selon la méthode de paiement", "Marché volatil"],
   "investisseurs souhaitant acheter ou gérer des crypto-actifs"),
 "bourse": ("courtier en bourse", "/comparatifs/trading-bourse.html", "comparatif bourse", True,
   ["Accès aux marchés actions, ETF ou produits dérivés", "Frais d'ordre souvent compétitifs", "Plateforme web et mobile"],
   ["Fiscalité à gérer selon l'enveloppe (CTO, PEA…)", "Risque de perte en capital"],
   "investisseurs autonomes souhaitant placer en bourse"),
 "epargne": ("épargne & placement", "/comparatifs/assurance-vie.html", "comparatif assurance-vie", True,
   ["Solutions d'épargne et de placement en ligne", "Frais réduits par rapport aux réseaux classiques", "Souscription dématérialisée"],
   ["Disponibilité et fiscalité selon le support", "Risque de perte sur les unités de compte"],
   "épargnants cherchant à faire fructifier leur argent sur le long terme"),
 "p2p": ("crowdlending / P2P", "/comparatifs/crowdlending-p2p.html", "comparatif crowdlending", True,
   ["Rendement potentiel supérieur aux livrets", "Diversification du patrimoine", "Tickets d'entrée souvent accessibles"],
   ["Risque de perte en capital et de défaut", "Liquidité limitée"],
   "investisseurs avertis cherchant du rendement via le prêt participatif"),
 "assurance": ("assurance", "/comparatifs/assurance-auto.html", "comparatif assurance", False,
   ["Souscription et gestion 100 % en ligne", "Tarifs compétitifs", "Parcours simplifié"],
   ["Garanties à comparer poste par poste", "Gestion des sinistres variable"],
   "assurés cherchant à réduire le coût de leurs contrats"),
 "assurance-animaux": ("assurance animaux", "/comparatifs/assurance-animaux.html", "comparatif assurance animaux", False,
   ["Remboursement des frais vétérinaires", "Souscription rapide en ligne", "Formules adaptées chien et chat"],
   ["Délais de carence et exclusions à vérifier", "Plafonds annuels de remboursement"],
   "propriétaires de chien ou chat voulant anticiper les frais vétérinaires"),
 "energie": ("fournisseur d'énergie", "/comparatifs/fournisseur-energie.html", "comparatif fournisseurs d'énergie", False,
   ["Offres d'électricité et/ou de gaz souvent moins chères que le tarif réglementé", "Souscription en ligne en quelques minutes", "Options vertes disponibles"],
   ["Prix indexés pouvant varier", "Service client variable selon l'acteur"],
   "particuliers cherchant à réduire leur facture d'énergie ou à passer au vert"),
 "solaire": ("kit solaire", "/comparatifs/kit-solaire-autoconsommation.html", "comparatif kits solaires", False,
   ["Autoconsommation et baisse de la facture d'électricité", "Installation simplifiée (kits plug-and-play)", "Amortissement sur la durée"],
   ["Investissement initial à prévoir", "Production dépendante de l'ensoleillement"],
   "particuliers souhaitant produire une partie de leur électricité"),
 "telecom": ("forfait mobile", "/comparatifs/forfait-mobile.html", "comparatif forfaits mobiles", False,
   ["Forfaits souvent sans engagement", "Data généreuse à petit prix", "Souscription en ligne"],
   ["Réseau dépendant de l'opérateur hôte", "Hausses de prix possibles après la promo"],
   "utilisateurs cherchant un forfait mobile au meilleur prix"),
 "esim": ("eSIM voyage", "/comparatifs/esim-voyage.html", "comparatif eSIM voyage", False,
   ["Data à l'étranger sans carte SIM physique", "Activation immédiate", "Tarifs au pays ou par zone"],
   ["Compatibilité eSIM requise sur le téléphone", "Appels/SMS souvent non inclus"],
   "voyageurs voulant rester connectés à l'étranger sans frais d'itinérance"),
 "vpn": ("VPN / cybersécurité", "/comparatifs/vpn.html", "comparatif VPN", False,
   ["Protection de la vie privée en ligne", "Chiffrement de la connexion", "Outils annexes (gestionnaire de mots de passe, antivirus…)"],
   ["Abonnement nécessaire pour un usage sérieux", "Vitesse variable selon les serveurs"],
   "internautes soucieux de leur vie privée et de leur sécurité en ligne"),
 "saas": ("logiciel / SaaS pro", "/comparatifs/logiciels-crm.html", "comparatifs logiciels pro", False,
   ["Outil en ligne sans installation", "Gain de temps sur la gestion", "Tarifs par abonnement"],
   ["Coût récurrent", "Courbe de prise en main selon l'outil"],
   "indépendants et entreprises cherchant à digitaliser leur gestion"),
 "compta": ("comptabilité / facturation", "/comparatifs/logiciels-comptabilite.html", "comparatif logiciels de comptabilité", False,
   ["Facturation conforme et compta simplifiée", "Déclarations facilitées (Urssaf, TVA)", "Pensé pour indépendants et TPE"],
   ["Abonnement mensuel", "Accompagnement humain variable"],
   "indépendants et TPE voulant simplifier leur gestion administrative"),
 "transfert": ("transfert d'argent", "/comparatifs/transfert-argent.html", "comparatif transfert d'argent", False,
   ["Envoi d'argent à l'international à frais réduits", "Taux de change souvent avantageux", "Réception rapide"],
   ["Frais et délais variables selon le pays", "Plafonds selon le profil"],
   "personnes envoyant de l'argent à l'étranger régulièrement"),
 "paiement": ("solution de paiement", "/comparatifs/terminaux-paiement.html", "comparatif des terminaux de paiement", False,
   ["Encaissement par carte en ligne et/ou en boutique", "Mise en place rapide", "Tarifs lisibles à la transaction"],
   ["Commissions à comparer selon le volume", "Matériel parfois à acheter"],
   "commerçants, indépendants et e-commerçants qui veulent encaisser la carte"),
 "shopping": ("shopping & cashback", "/autres-comparatifs.html", "tous nos comparatifs", False,
   ["Bons plans, cashback ou produits à prix réduits", "Souscription gratuite", "Économies sur les achats du quotidien"],
   ["Conditions de cashback à vérifier", "Délais de versement variables"],
   "consommateurs qui veulent payer moins cher leurs achats"),
 "jeux": ("jeux & paris en ligne", "/autres-comparatifs.html", "tous nos comparatifs", False,
   ["Offre de bienvenue à l'inscription", "Application et parcours 100 % en ligne", "Opérateur agréé en France (ANJ)"],
   ["Jouer comporte un risque d'addiction et de pertes", "Réservé aux personnes majeures"],
   "joueurs majeurs cherchant une offre de bienvenue"),
 "streaming": ("streaming & TV", "/autres-comparatifs.html", "tous nos comparatifs", False,
   ["Catalogue de contenus (sport, cinéma, séries)", "Souscription en ligne", "Offres groupées possibles"],
   ["Abonnement mensuel", "Engagement éventuel selon la formule"],
   "amateurs de TV, sport et cinéma"),
 "maison": ("maison & équipement", "/autres-comparatifs.html", "tous nos comparatifs", False,
   ["Produits et services pour la maison", "Commande en ligne", "Promotions régulières"],
   ["Délais de livraison variables", "Conditions de retour à vérifier"],
   "particuliers qui équipent ou entretiennent leur logement"),
 "food": ("food & livraison", "/autres-comparatifs.html", "tous nos comparatifs", False,
   ["Repas ou produits livrés à domicile", "Première commande souvent à prix réduit", "Souscription flexible"],
   ["Coût récurrent selon la formule", "Zones de livraison limitées"],
   "particuliers qui veulent se faire livrer repas ou courses"),
 "sante": ("santé & bien-être", "/autres-comparatifs.html", "tous nos comparatifs", False,
   ["Service ou dispositif accessible en ligne", "Accompagnement à distance", "Souscription simple"],
   ["Coût à vérifier selon la prise en charge", "Ne remplace pas un avis médical"],
   "particuliers cherchant un service de santé ou de bien-être"),
 "services": ("services du quotidien", "/autres-comparatifs.html", "tous nos comparatifs", False,
   ["Mise en relation ou service en ligne", "Inscription gratuite", "Gain de temps au quotidien"],
   ["Disponibilité selon la zone", "Conditions variables selon le prestataire"],
   "particuliers et pros cherchant un service du quotidien"),
}

# slug, Nom, url, vertical, description courte
BRANDS = [
 # néobanques
 ("bforbank","BforBank","https://www.bforbank.com/","neobank","La banque en ligne du groupe Crédit Agricole, comptes et placements."),
 ("monese","Monese","https://monese.com/fr/","neobank","Le compte courant mobile accessible sans condition de revenus."),
 ("lydia","Lydia","https://lydia-app.com/","neobank","L'application de paiement et compte mobile populaire en France."),
 ("onlyone","OnlyOne","https://www.onlyonecard.eu/","neobank","La néobanque engagée pour une consommation plus responsable."),
 ("helios","Helios","https://www.helios.do/","neobank","Le compte courant qui finance la transition écologique."),
 ("greengot","Green-Got","https://www.green-got.com/","neobank","Le compte bancaire qui oriente l'épargne vers des projets verts."),
 ("anytime","Anytime","https://www.anytime.eu/","neobank","Le compte pour particuliers et pros avec cartes et gestion en ligne."),
 ("vivid","Vivid","https://vivid.money/fr-fr/","neobank","Le compte mobile avec cashback et fonctionnalités d'investissement."),
 ("sogexia","Sogexia","https://www.sogexia.com/","neobank","Le compte en ligne rapide à ouvrir, sans condition de revenus."),
 ("blackcatcard","Blackcatcard","https://blackcatcard.com/","neobank","Le compte et la carte Mastercard avec cashback, ouverture express."),
 # pro
 ("propulse-by-ca","Propulse by CA","https://www.propulsebyca.fr/","pro-bank","Le compte pro tout-en-un du Crédit Agricole pour indépendants."),
 ("airwallex","Airwallex","https://www.airwallex.com/fr","pro-bank","La plateforme de comptes multidevises et paiements internationaux pour entreprises."),
 # crypto
 ("bitget","Bitget","https://www.bitget.com/fr","crypto","Plateforme crypto connue pour le copy-trading et les dérivés."),
 ("bybit","Bybit","https://www.bybit.com/fr-FR/","crypto","Exchange crypto avec large offre de trading et de produits."),
 ("okx","OKX","https://www.okx.com/fr","crypto","Plateforme crypto mondiale : achat, trading et wallet Web3."),
 ("kucoin","KuCoin","https://www.kucoin.com/","crypto","Exchange crypto au très large choix d'altcoins."),
 ("gate-io","Gate.io","https://www.gate.io/fr","crypto","Plateforme crypto historique avec des milliers d'actifs."),
 ("bitstamp","Bitstamp","https://www.bitstamp.net/","crypto","L'un des plus anciens exchanges crypto, axé fiabilité."),
 ("bitvavo","Bitvavo","https://bitvavo.com/fr","crypto","Plateforme crypto européenne aux frais réduits."),
 ("swissborg","SwissBorg","https://swissborg.com/fr","crypto","L'app crypto européenne pour investir, échanger et générer du rendement."),
 ("bitstack","Bitstack","https://bitstack.com/","crypto","L'app française pour épargner en Bitcoin automatiquement."),
 ("gemini","Gemini","https://www.gemini.com/","crypto","Exchange crypto régulé, axé sécurité et conformité."),
 ("nexo","Nexo","https://nexo.com/fr","crypto","Plateforme crypto de prêts et de comptes rémunérés."),
 ("ledger","Ledger","https://www.ledger.com/fr","crypto","Le leader français des portefeuilles physiques (cold wallets)."),
 ("zengo","Zengo","https://zengo.com/","crypto","Le wallet crypto sans phrase secrète, axé sécurité."),
 ("young-platform","Young Platform","https://youngplatform.com/fr/","crypto","Exchange crypto européen pensé pour les débutants."),
 ("stackinsat","StackinSat","https://stackinsat.com/","crypto","La plateforme française d'épargne programmée en Bitcoin."),
 ("uphold","Uphold","https://uphold.com/fr-fr","crypto","Plateforme multi-actifs : crypto, métaux et devises."),
 ("mt-pelerin","Mt Pelerin","https://www.mtpelerin.com/fr","crypto","La passerelle suisse entre euros et cryptomonnaies, sans compte."),
 ("paymium","Paymium","https://www.paymium.com/","crypto","L'exchange Bitcoin français, l'un des plus anciens d'Europe."),
 ("bingx","BingX","https://bingx.com/fr-fr/","crypto","Plateforme crypto axée copy-trading et dérivés."),
 ("mexc","MEXC","https://www.mexc.com/fr-FR","crypto","Exchange crypto au très large catalogue d'altcoins."),
 ("tangem","Tangem","https://tangem.com/fr/","crypto","Le portefeuille crypto sous forme de carte NFC."),
 ("safepal","SafePal","https://www.safepal.com/","crypto","Wallet crypto matériel et logiciel à petit prix."),
 ("bit2me","Bit2Me","https://bit2me.com/fr","crypto","Plateforme crypto espagnole tout-en-un, régulée en Europe."),
 ("gnosis-pay","Gnosis Pay","https://gnosispay.com/","crypto","La carte de paiement adossée à un wallet crypto auto-hébergé."),
 # bourse / invest
 ("trading-212","Trading 212","https://www.trading212.com/","bourse","Courtier proposant actions et ETF sans commission."),
 ("scalable-capital","Scalable Capital","https://fr.scalable.capital/","bourse","Courtier et plans d'investissement programmés sur ETF."),
 ("saxo","Saxo","https://www.home.saxo/fr-fr","bourse","Courtier premium avec accès à de très nombreux marchés."),
 ("swissquote","Swissquote","https://www.swissquote.com/fr","bourse","La banque en ligne suisse spécialiste du trading."),
 ("interactive-brokers","Interactive Brokers","https://www.interactivebrokers.fr/","bourse","Le courtier de référence des investisseurs actifs et expérimentés."),
 ("bourse-direct","Bourse Direct","https://www.boursedirect.fr/","bourse","Le courtier français à frais réduits, PEA et CTO."),
 ("freedom24","Freedom24","https://freedom24.com/","bourse","Courtier européen avec actions, ETF et comptes rémunérés."),
 ("avatrade","AvaTrade","https://www.avatrade.fr/","bourse","Courtier CFD et forex régulé, plateformes multiples."),
 ("finary","Finary","https://finary.com/fr","bourse","Le suivi de patrimoine en temps réel et l'investissement."),
 ("moning","Moning","https://moning.co/","bourse","L'app française pour investir en bourse et suivre ses dividendes."),
 ("mon-petit-placement","Mon Petit Placement","https://www.monpetitplacement.fr/","epargne","L'investissement accompagné, accessible dès quelques centaines d'euros."),
 ("wesave","WeSave","https://www.wesave.fr/","epargne","La gestion pilotée en assurance-vie par des experts."),
 ("altaprofits","Altaprofits","https://www.altaprofits.com/","epargne","Le courtier en assurance-vie et placements en ligne."),
 ("linxo","Linxo","https://www.linxo.com/","saas","L'agrégateur de comptes pour piloter son budget."),
 ("bankin","Bankin'","https://bankin.com/","saas","L'application de gestion de budget et d'agrégation de comptes."),
 ("corum","Corum","https://www.corum.fr/","epargne","La gestion d'épargne spécialisée en SCPI immobilières."),
 ("moniwan","Moniwan","https://www.moniwan.fr/","epargne","La plateforme d'investissement en SCPI du groupe La Française."),
 ("mes-placements","Mes Placements","https://www.mes-placements.fr/","epargne","Le courtier en ligne en assurance-vie, PER et SCPI."),
 # p2p / crowdlending
 ("mintos","Mintos","https://www.mintos.com/fr/","p2p","La plus grande marketplace européenne de prêts P2P."),
 ("peerberry","PeerBerry","https://peerberry.com/","p2p","Plateforme de prêt entre particuliers à court terme."),
 ("bondora","Bondora","https://www.bondora.com/fr","p2p","Plateforme P2P estonienne, dont l'offre Go & Grow."),
 ("robocash","Robocash","https://robo.cash/","p2p","Plateforme de crowdlending automatisée à haut rendement."),
 ("swaper","Swaper","https://swaper.com/","p2p","Plateforme de prêt P2P avec rachat garanti."),
 ("esketit","Esketit","https://esketit.com/","p2p","Plateforme de crowdlending adossée à un groupe de crédit."),
 ("viainvest","VIAINVEST","https://viainvest.com/","p2p","Plateforme P2P régulée investissant dans le crédit conso."),
 ("crowdestor","Crowdestor","https://crowdestor.com/","p2p","Financement participatif de projets immobiliers et business."),
 ("estateguru","EstateGuru","https://estateguru.co/","p2p","Plateforme paneuropéenne de prêts immobiliers garantis."),
 ("raizers","Raizers","https://www.raizers.com/","p2p","Plateforme française de crowdfunding immobilier et entreprises."),
 ("lendopolis","Lendopolis","https://www.lendopolis.com/","p2p","Le financement participatif des énergies renouvelables (groupe La Banque Postale)."),
 ("lendosphere","Lendosphere","https://www.lendosphere.com/","p2p","Le crowdfunding dédié aux projets de transition écologique."),
 ("look-and-fin","Look&Fin","https://www.lookandfin.com/","p2p","Plateforme de prêt aux PME françaises et belges."),
 ("homunity","Homunity","https://www.homunity.com/","p2p","Le crowdfunding immobilier pour investir dès 1 000 €."),
 ("clubfunding","ClubFunding","https://www.clubfunding.fr/","p2p","Plateforme leader du financement participatif immobilier."),
 ("la-premiere-brique","La Première Brique","https://lapremierebrique.fr/","p2p","Le crowdfunding immobilier accessible dès 1 €."),
 ("enerfip","Enerfip","https://enerfip.fr/","p2p","Le financement participatif des énergies renouvelables."),
 ("miimosa","MiiMOSA","https://www.miimosa.com/fr","p2p","Le financement participatif de l'agriculture et de l'alimentation."),
 ("wiseed","WiSEED","https://www.wiseed.com/","p2p","Pionnier français du crowdfunding immobilier et startups."),
 ("october","October","https://fr.october.eu/","p2p","Le prêt aux PME européennes financé par les particuliers."),
 ("pretup","PretUp","https://www.pretup.fr/","p2p","Plateforme de prêt aux PME françaises."),
 ("baltis","Baltis","https://www.baltis.fr/","p2p","Le crowdfunding immobilier locatif accessible."),
 ("bricks","Bricks","https://bricks.co/","p2p","L'investissement immobilier fractionné dès quelques euros."),
 # assurance
 ("getsafe","Getsafe","https://www.hellogetsafe.com/fr","assurance","L'assurance 100 % digitale (habitation, responsabilité civile…)."),
 ("acheel","Acheel","https://www.acheel.com/","assurance","L'assurtech française multi-produits à tarifs compétitifs."),
 ("lovys","Lovys","https://www.lovys.fr/","assurance","L'assurance mensualisée et modulable, tout en ligne."),
 ("eurofil","Eurofil","https://www.eurofil.com/","assurance","L'assurance auto et habitation en direct, sans intermédiaire."),
 ("acommeassure","A comme Assure","https://www.acommeassure.com/","assurance","Le courtier en assurance auto, moto et habitation en ligne."),
 ("april","April","https://www.april.fr/","assurance","Le courtier grossiste : santé, emprunteur, auto, habitation."),
 ("qare","Qare","https://www.qare.fr/","assurance","La téléconsultation médicale en ligne avec des médecins."),
 ("l-olivier","L'olivier Assurance","https://www.lolivier.fr/","assurance","L'assurance auto et habitation au prix au kilomètre près."),
 # assurance animaux
 ("dalma","Dalma","https://www.dalma.co/","assurance-animaux","L'assurance santé pour chien et chat, gestion 100 % mobile."),
 ("santevet","SantéVet","https://www.santevet.com/","assurance-animaux","Le spécialiste historique de l'assurance santé animale."),
 ("assuropoil","Assuropoil","https://www.assuropoil.fr/","assurance-animaux","L'assurance chien et chat aux formules complètes."),
 ("barkibu","Barkibu","https://www.barkibu.com/fr","assurance-animaux","L'assurance animale avec vétérinaires en ligne inclus."),
 ("bulle-bleue","Bulle Bleue","https://www.bullebleue.fr/","assurance-animaux","La mutuelle santé pour chien et chat, sur-mesure."),
 ("kozoo","Kozoo","https://kozoo.eu/","assurance-animaux","L'assurance santé animale rapide et 100 % en ligne."),
 # énergie
 ("edf","EDF","https://www.edf.fr/","energie","Le fournisseur historique d'électricité et de gaz."),
 ("octopus-energy","Octopus Energy","https://octopusenergy.fr/","energie","Le fournisseur d'électricité verte au service client salué."),
 ("mint-energie","Mint Énergie","https://www.mint-energie.com/","energie","Le fournisseur d'électricité verte à prix bas, 100 % en ligne."),
 ("alpiq","Alpiq","https://www.alpiq.fr/","energie","Le fournisseur d'électricité et gaz à prix indexés."),
 ("enercoop","Enercoop","https://www.enercoop.fr/","energie","Le fournisseur coopératif d'électricité 100 % renouvelable."),
 ("ilek","ilek","https://www.ilek.fr/","energie","L'énergie verte de producteurs locaux français."),
 ("elmy","Elmy","https://www.elmy.fr/","energie","Le fournisseur d'électricité verte à prix coûtant."),
 ("wekiwi","Wekiwi","https://www.wekiwi.fr/","energie","Le fournisseur d'énergie au forfait avec gestion en ligne."),
 ("mega-energie","Méga Énergie","https://www.mega-energie.fr/","energie","Le fournisseur d'électricité et gaz à prix réduits."),
 ("sowee","Sowee","https://www.sowee.fr/","energie","Le fournisseur d'énergie connecté du groupe EDF."),
 ("plenitude","Plénitude","https://www.plenitude.com/fr","energie","Le fournisseur d'électricité et gaz du groupe Eni."),
 ("primeo-energie","Primeo Énergie","https://www.primeo-energie.fr/","energie","Le fournisseur d'électricité verte à prix compétitifs."),
 ("la-bellenergie","La Bellénergie","https://www.labellenergie.fr/","energie","Le fournisseur d'électricité verte indépendant et local."),
 ("hello-watt","Hello Watt","https://www.hellowatt.fr/","energie","Le service gratuit de conseil et de suivi de la conso d'énergie."),
 ("selectra","Selectra","https://selectra.info/","energie","Le comparateur et service de souscription énergie/télécom."),
 # solaire
 ("otovo","Otovo","https://www.otovo.fr/","solaire","L'installation de panneaux solaires clé en main."),
 ("beem-energy","Beem Energy","https://www.beemenergy.fr/","solaire","Le kit solaire plug-and-play à brancher soi-même."),
 ("sunology","Sunology","https://sunology.eu/","solaire","La station solaire prête à poser pour autoconsommer."),
 ("edf-enr","EDF ENR","https://www.edfenr.com/","solaire","L'installation de panneaux solaires par une filiale d'EDF."),
 # telecom
 ("sosh","Sosh","https://www.sosh.fr/","telecom","La marque mobile et box sans engagement d'Orange."),
 ("prixtel","Prixtel","https://www.prixtel.com/","telecom","Le forfait mobile ajustable selon la conso, sur réseau SFR/Orange."),
 ("youprice","YouPrice","https://www.youprice.co/","telecom","Le forfait mobile au choix du réseau (Orange ou SFR)."),
 ("lebara","Lebara","https://www.lebara.fr/","telecom","Les forfaits mobiles économiques tournés vers l'international."),
 ("lycamobile","Lycamobile","https://www.lycamobile.fr/","telecom","Les forfaits mobiles sans engagement avec appels internationaux."),
 ("nrj-mobile","NRJ Mobile","https://www.nrjmobile.fr/","telecom","Les forfaits mobiles à petits prix sur réseaux Orange/SFR."),
 ("coriolis","Coriolis","https://www.coriolis.com/","telecom","Les forfaits mobiles et box de l'opérateur Coriolis Telecom."),
 ("syma-mobile","Syma Mobile","https://www.symamobile.com/","telecom","Le forfait mobile tourné international, sans engagement."),
 ("auchan-telecom","Auchan Telecom","https://www.auchantelecom.fr/","telecom","Les forfaits mobiles low-cost de l'enseigne Auchan."),
 ("starlink-france","Starlink","https://www.starlink.com/","telecom","L'internet par satellite haut débit, partout en France."),
 ("nordnet","Nordnet","https://www.nordnet.com/","telecom","L'internet par satellite, fibre et 4G du groupe Orange."),
 # esim
 ("airalo","Airalo","https://www.airalo.com/fr","esim","La marketplace d'eSIM de voyage la plus connue."),
 ("holafly","Holafly","https://esim.holafly.com/fr/","esim","L'eSIM voyage avec data illimitée dans de nombreux pays."),
 ("ubigi","Ubigi","https://www.ubigi.com/fr/","esim","L'eSIM data mondiale du groupe Transatel (NTT)."),
 ("saily","Saily","https://saily.com/","esim","L'eSIM voyage des créateurs de NordVPN."),
 ("kolet","Kolet","https://www.kolet.com/","esim","L'eSIM voyage française simple et économique."),
 ("nomad-esim","Nomad","https://www.getnomad.app/","esim","L'eSIM data à la carte pour voyager connecté."),
 # vpn / privacy
 ("windscribe","Windscribe","https://windscribe.com/","vpn","Le VPN avec une offre gratuite généreuse et des outils anti-pub."),
 ("incogni","Incogni","https://incogni.com/","vpn","Le service qui supprime vos données chez les data brokers."),
 ("nordpass","NordPass","https://nordpass.com/fr/","vpn","Le gestionnaire de mots de passe de l'équipe NordVPN."),
 ("dashlane","Dashlane","https://www.dashlane.com/fr","vpn","Le gestionnaire de mots de passe avec VPN intégré."),
 ("bitdefender","Bitdefender","https://www.bitdefender.fr/","vpn","La suite antivirus et cybersécurité de référence."),
 ("avast","Avast","https://www.avast.com/fr-fr/","vpn","L'antivirus grand public avec VPN et outils de confidentialité."),
 ("internxt","Internxt","https://internxt.com/fr","vpn","Le cloud chiffré open source, alternative à Google Drive."),
 ("pcloud","pCloud","https://www.pcloud.com/fr/","vpn","Le stockage cloud sécurisé avec licence à vie possible."),
 ("protonmail","Proton Mail","https://proton.me/fr/mail","vpn","La messagerie chiffrée suisse, alternative privée à Gmail."),
 # saas / compta
 ("dougs","Dougs","https://www.dougs.fr/","compta","L'expertise comptable en ligne pour indépendants et TPE."),
 ("keobiz","Keobiz","https://www.keobiz.fr/","compta","L'expert-comptable en ligne à tarif maîtrisé."),
 ("abby","Abby","https://abby.fr/","compta","L'app de gestion et facturation pour auto-entrepreneurs."),
 ("freebe","Freebe","https://www.freebe.me/","compta","L'outil de gestion tout-en-un pour freelances."),
 ("decla","Decla","https://www.decla.fr/","compta","L'assistant de déclaration et gestion pour micro-entrepreneurs."),
 ("zervant","Zervant","https://www.zervant.com/fr/","compta","Le logiciel de facturation simple pour petites entreprises."),
 ("legalplace","LegalPlace","https://www.legalplace.fr/","saas","La création et la gestion juridique d'entreprise en ligne."),
 ("captain-contrat","Captain Contrat","https://www.captaincontrat.com/","saas","L'accompagnement juridique en ligne pour créer son entreprise."),
 ("malt","Malt","https://www.malt.fr/","saas","La plateforme qui connecte freelances et entreprises."),
 ("comeup","ComeUp","https://comeup.com/fr/","saas","La marketplace de microservices freelance (ex-5euros)."),
 ("systemeio","Systeme.io","https://systeme.io/fr","saas","L'outil tout-en-un de marketing et de vente en ligne."),
 ("gandi","Gandi","https://www.gandi.net/fr","saas","Le registrar français de noms de domaine et hébergement."),
 ("lws","LWS","https://www.lws.fr/","saas","L'hébergeur web français à petits prix."),
 ("amen","Amen","https://www.amen.fr/","saas","L'hébergeur et registrar pour sites et emails pro."),
 ("planethoster","PlanetHoster","https://www.planethoster.com/fr/","saas","L'hébergement web performant, France et Canada."),
 ("gocardless","GoCardless","https://gocardless.com/fr-fr/","saas","La solution de prélèvement automatique pour entreprises."),
 # transfert
 ("western-union","Western Union","https://www.westernunion.com/fr/fr/home.html","transfert","Le réseau mondial historique de transfert d'argent."),
 ("moneygram","MoneyGram","https://www.moneygram.com/","transfert","Le transfert d'argent international, en ligne et en agence."),
 ("paysend","Paysend","https://paysend.com/fr-fr","transfert","Le transfert d'argent de carte à carte à frais fixes."),
 ("taptap-send","TapTap Send","https://www.taptapsend.com/","transfert","L'app de transfert d'argent à frais réduits vers l'Afrique et l'Asie."),
 ("worldremit","WorldRemit","https://www.worldremit.com/fr","transfert","Le transfert d'argent en ligne vers 130+ pays."),
 ("xoom","Xoom","https://www.xoom.com/fr","transfert","Le service de transfert international de PayPal."),
 ("sendwave","Sendwave","https://www.sendwave.com/","transfert","Le transfert d'argent mobile sans frais vers l'Afrique."),
 ("instarem","Instarem","https://www.instarem.com/fr-fr/","transfert","Le transfert international avec taux de change réel."),
 ("ria","Ria","https://www.riamoneytransfer.com/","transfert","L'un des plus grands réseaux mondiaux de transfert d'argent."),
 ("currencyfair","CurrencyFair","https://www.currencyfair.com/","transfert","La place de marché des changes de devises peer-to-peer."),
 ("lemfi","LemFi","https://www.lemfi.com/fr","transfert","Le transfert d'argent dédié aux diasporas, à frais réduits."),
 ("transfergo","TransferGo","https://www.transfergo.com/fr","transfert","Le transfert d'argent rapide en Europe et au-delà."),
 ("xe","XE","https://www.xe.com/fr/","transfert","Le spécialiste du change et des transferts internationaux."),
 # marques 1parrainage déjà branchées (logo+redirect) à doter de leurs pages
 ("nirio","Nirio","https://www.nirio.fr/","neobank","Le compte et les services de paiement de proximité (groupe Fnac Darty / BNP)."),
 ("nickel","Nickel","https://nickel.eu/fr","neobank","Le compte sans condition de revenus, ouvrable chez le buraliste."),
 ("distingo","Distingo Bank","https://www.distingo.fr/","epargne","La banque d'épargne en ligne : livret et comptes à terme."),
 ("lendermarket","Lendermarket","https://lendermarket.com/","p2p","Plateforme de prêt P2P adossée à un groupe de crédit."),
 ("youhodler","YouHodler","https://www.youhodler.com/","crypto","Plateforme crypto de prêts et d'épargne rémunérée sur cryptoactifs."),
 ("leocare","Leocare","https://www.leocare.eu/","assurance","L'assurance 100 % mobile : auto, habitation, moto et smartphone."),
 ("hiscox","Hiscox","https://www.hiscox.fr/","assurance","L'assurance des professionnels et indépendants (RC Pro, multirisque)."),
 ("lassie","Lassie","https://www.lassie.co/fr","assurance-animaux","L'assurance santé pour chien et chat, axée prévention."),
 ("engie","Engie","https://particuliers.engie.fr/","energie","Le fournisseur d'électricité et de gaz, offres vertes et services."),
 ("totalenergies","TotalEnergies","https://www.totalenergies.fr/particuliers","energie","Électricité et gaz à tarifs compétitifs, dont des offres vertes."),
 ("vattenfall","Vattenfall","https://www.vattenfall.fr/","energie","Fournisseur d'électricité et de gaz d'origine renouvelable."),
 ("ekwateur","ekWateur","https://ekwateur.fr/","energie","Fournisseur d'énergie verte : électricité et gaz renouvelables."),
 ("ohm-energie","OHM Énergie","https://www.ohm-energie.com/","energie","Fournisseur d'électricité avec offres indexées et heures creuses."),
 ("monkitsolaire","MonKitSolaire","https://www.monkitsolaire.fr/","solaire","Kits de panneaux solaires en autoconsommation à monter soi-même."),
 ("materfrance","Materfrance","https://www.materfrance.fr/","solaire","Kits solaires plug-and-play et autoconsommation pour particuliers."),
 ("red-by-sfr","RED by SFR","https://www.red-by-sfr.fr/","telecom","Forfaits mobiles et box sans engagement sur réseau SFR."),
 ("laposte-mobile","La Poste Mobile","https://www.lapostemobile.fr/","telecom","Forfaits mobiles de La Poste, sur le réseau SFR."),
 # marques restantes à doter de leurs pages (paiement + divers)
 ("payplug","PayPlug","https://www.payplug.com/","paiement","La solution de paiement en ligne et TPE pensée pour les PME françaises."),
 ("square","Square","https://squareup.com/fr/fr","paiement","Le terminal et l'écosystème d'encaissement tout-en-un pour commerçants."),
 ("stripe","Stripe","https://stripe.com/fr","paiement","La référence du paiement en ligne pour sites web et applications."),
 ("viva-wallet","Viva.com","https://www.viva.com/fr-fr/","paiement","La solution d'encaissement et de paiement professionnelle 100 % digitale."),
 ("back-market","Back Market","https://www.backmarket.fr/","shopping","La marketplace de référence du reconditionné garanti."),
 ("rakuten","Rakuten","https://fr.shopping.rakuten.com/","shopping","La marketplace avec programme de cashback (ex-PriceMinister)."),
 ("coupon-network","Coupon Network","https://www.couponnetwork.fr/","shopping","Bons de réduction et coupons sur les produits du quotidien."),
 ("betsson","Betsson","https://www.betsson.fr/","jeux","Paris sportifs et casino en ligne, opérateur agréé."),
 ("pmu","PMU","https://www.pmu.fr/","jeux","Paris hippiques, paris sportifs et poker en ligne."),
 ("canal-plus","Canal+","https://www.canalplus.com/","streaming","Chaînes premium : sport, cinéma, séries et plateformes incluses."),
 ("emma","Emma","https://www.emma-matelas.fr/","maison","Matelas en mousse et literie, leader européen de la vente en ligne."),
 ("ninja-kitchen","Ninja","https://www.ninjakitchen.fr/","maison","Appareils de cuisine : friteuses sans huile, blenders, multicuiseurs."),
 ("engie-home-services","Engie Home Services","https://www.engie-homeservices.fr/","maison","Entretien et dépannage chauffage, chaudière et climatisation."),
 ("quitoque","Quitoque","https://www.quitoque.fr/","food","Paniers-repas avec ingrédients et recettes livrés à domicile."),
 ("kiwiiz","Kiwiiz","https://www.kiwiiz.fr/","services","Location de matériel et services entre particuliers et professionnels."),
 ("poppins","Poppins","https://poppins.io/","sante","Dispositif médical numérique d'aide à la lecture pour enfants dyslexiques."),
]

def faq_ld(faq):
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)

def head(url, title, desc, leaf, extra=""):
    t, d = html.escape(title), html.escape(desc)
    bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
        {"@type":"ListItem","position":2,"name":leaf,"item":url}]},ensure_ascii=False)
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

def logo_chip(slug, name, big=False):
    s = "96" if big else "72"
    return f'<img src="/assets/logos/{slug}.png" alt="{html.escape(name)}" width="{s}" height="{s}" loading="lazy" style="max-width:100%;max-height:100%;object-fit:contain;">'

def siblings(brand_slug, vert, k=3):
    sibs = [(s,n) for s,n,u,v,d in BRANDS if v==vert and s!=brand_slug]
    return sibs[:k]

def gen_avis(slug, name, url, vert, desc):
    n = html.escape(name)
    label, comp_url, comp_label, risk, pros, cons, pour_qui = VERT[vert]
    out = f"avis/{slug}.html"
    if os.path.exists(out): return False
    page_url = f"https://selectum.fr/avis/{slug}.html"
    title = f"Avis {name} 2026 : présentation, offres et alternatives | Selectum"
    d = f"Avis {name} 2026 : {desc} Présentation, fonctionnement, pour qui, alternatives et offres en cours, par l'équipe Selectum."
    art = json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":d,
        "author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum",
        "logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},
        "datePublished":"2026-06-12","dateModified":"2026-06-12","mainEntityOfPage":page_url},ensure_ascii=False)
    faq = [(f"{name} est-il fiable ?", f"{name} est un acteur de la catégorie {label}. Nous présentons son offre et ses limites sur cette page ; vérifiez toujours les conditions à jour sur le site officiel."),
           (f"Comment profiter de l'offre {name} ?", f"Consultez notre page code promo {name} et notre page parrainage {name} pour les offres de bienvenue en cours."),
           (f"Quelles alternatives à {name} ?", f"Comparez {name} aux autres acteurs dans notre {comp_label}.")]
    pros_h = "".join(f"<li>{html.escape(p)}</li>" for p in pros)
    cons_h = "".join(f"<li>{html.escape(c)}</li>" for c in cons)
    sib = siblings(slug, vert)
    sib_links = "".join(f'<a href="/avis/{s}.html" class="rel-chip">Avis {html.escape(nm)} →</a>' for s,nm in sib)
    risk_box = ('<div class="affiliate-notice" style="margin-top:14px;">⚠️ <strong>Risques :</strong> ce produit comporte un risque de perte en capital. Les performances passées ne préjugent pas des performances futures. N\'investissez que ce que vous pouvez vous permettre de perdre.</div>') if risk else ""
    body = f'''<div class="brand-hero"><div class="container-article">
  <div class="brand-hero-logo">{logo_chip(slug,name,big=True)}</div>
  <div class="brand-hero-text">
    <div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / <a href="{comp_url}" style="color:rgba(255,255,255,.8)">{html.escape(label.capitalize())}</a> / {n}</div>
    <h1>Avis {n} : présentation et alternatives</h1>
    <p class="subtitle">{html.escape(desc)}</p>
    <p class="updated">🗓️ Publié le {D} — par l'équipe Selectum</p>
  </div></div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Voir notre <a href="/methodologie.html">méthodologie</a>.</div>
  <div class="intro-box"><p>{n} est un acteur de la catégorie <strong>{html.escape(label)}</strong>. {html.escape(desc)} Voici notre présentation, ses points forts et ses limites, et vers qui vous tourner si {n} ne vous convient pas.</p></div>
  <h2 id="presentation">Que propose {n} ?</h2>
  <p>{n} s'adresse aux {html.escape(pour_qui)}. Cette page est une présentation éditoriale ; pour le détail chiffré et à jour (tarifs, conditions), reportez-vous au site officiel et à nos comparatifs.</p>
  <div class="pros-cons"><div class="pros"><h4>✅ Points forts</h4><ul>{pros_h}</ul></div><div class="cons"><h4>❌ Points d'attention</h4><ul>{cons_h}</ul></div></div>
  <h2 id="pour-qui">Pour qui {n} est-il fait ?</h2>
  <p>{n} conviendra surtout aux <strong>{html.escape(pour_qui)}</strong>. Pour vérifier que c'est le meilleur choix pour votre situation, comparez-le à ses concurrents dans notre <a href="{comp_url}">{html.escape(comp_label)}</a>.</p>
  <h3>Alternatives directes</h3>
  <p>Si {n} ne correspond pas à votre besoin, regardez les autres acteurs de notre <a href="{comp_url}">{html.escape(comp_label)}</a>.</p>
  {risk_box}
  <div class="highlight-box"><p>💡 <strong>Offres {n} :</strong> consultez le <a href="/code-promo/{slug}.html">code promo {n}</a> et le <a href="/parrainage/{slug}.html">parrainage {n}</a> pour les bonus de bienvenue en cours.</p></div>
  <h2 id="auteur">Méthodologie & auteur</h2>
  <ul><li><strong>Auteur :</strong> équipe éditoriale Selectum (HALBC SAS) — contact@selectum.fr</li><li><strong>Méthodologie :</strong> <a href="/methodologie.html">comment nous évaluons les marques</a></li><li><strong>Indépendance :</strong> l'affiliation n'influence ni la présentation ni le classement.</li></ul>
  <div class="faq"><h2>❓ Questions fréquentes</h2>{"".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)}</div>
  <div class="rel-links"><h2>À lire aussi</h2><div class="rel-list"><a href="{comp_url}" class="rel-chip">{html.escape(comp_label.capitalize())} →</a><a href="/code-promo/{slug}.html" class="rel-chip">Code promo {n} →</a><a href="/parrainage/{slug}.html" class="rel-chip">Parrainage {n} →</a>{sib_links}</div></div>
</div></div>'''
    open(out,"w",encoding="utf-8").write(head(page_url,title,d,f"Avis {name}",'<script type="application/ld+json">'+art+'</script>\n<script type="application/ld+json">'+faq_ld(faq)+'</script>\n')+body+FOOT)
    return True

def gen_codepromo(slug, name, url, vert, desc):
    n = html.escape(name)
    label, comp_url, comp_label, risk, *_ = VERT[vert]
    out = f"code-promo/{slug}.html"
    if os.path.exists(out): return False
    page_url = f"https://selectum.fr/code-promo/{slug}.html"
    title = f"Code promo {name} 2026 : offre de bienvenue en cours | Selectum"
    d = f"Code promo et offre de bienvenue {name} 2026, vérifiés ce mois-ci. {desc} Profitez de l'offre du moment via Selectum."
    faq = [(f"Y a-t-il un code promo {name} ?", f"L'offre de bienvenue {name} s'active généralement via notre lien, sans code à saisir. Les promotions ponctuelles sont indiquées sur cette page."),
           (f"L'offre {name} est-elle vérifiée ?", f"Oui, l'offre affichée a été vérifiée le {D}. Les conditions peuvent évoluer : le site officiel fait foi."),
           (f"Comment utiliser l'offre {name} ?", "Cliquez sur « Révéler l'offre », vous êtes redirigé vers le site partenaire où l'offre s'applique.")]
    art = json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":d,
        "author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum",
        "logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},
        "datePublished":"2026-06-12","dateModified":"2026-06-12","mainEntityOfPage":page_url},ensure_ascii=False)
    body = f'''<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span>Code promo<span>/</span>{n}</div>
  <h1>Code promo {n} : l'offre du moment</h1>
  <p class="updated">🗓️ Vérifié le {D} par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
  <div class="promo-box"><span class="promo-badge">🎁 Offre en cours</span>
    <h3>Offre de bienvenue {n}</h3>
    <p>{html.escape(desc)} Découvrez l'offre du moment en cliquant ci-dessous.</p>
    <div class="promo-reveal"><div class="promo-code">OFFRE EN COURS</div>
    <a href="/go/{slug}" class="promo-btn" target="_blank" rel="sponsored nofollow noopener">Révéler l'offre</a></div>
    <p class="promo-note">Offre susceptible d'évoluer — vérifiée le {D}. Voir conditions sur le site {n}.</p>
  </div>
  <h2>Comment profiter de l'offre {n}</h2>
  <ol><li>Cliquez sur « Révéler l'offre » ci-dessus</li><li>Vous êtes redirigé vers le site officiel {n}</li><li>Finalisez votre inscription : l'offre de bienvenue s'applique</li></ol>
  <div class="highlight-box"><p>💡 Avant de souscrire, lisez notre <a href="/avis/{slug}.html">avis {n}</a> et comparez dans notre <a href="{comp_url}">{html.escape(comp_label)}</a>.</p></div>
  <div class="faq"><h2>❓ Questions fréquentes</h2>{"".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)}</div>
  <div class="rel-links"><h2>À lire aussi</h2><div class="rel-list"><a href="/avis/{slug}.html" class="rel-chip">Avis {n} →</a><a href="/parrainage/{slug}.html" class="rel-chip">Parrainage {n} →</a><a href="{comp_url}" class="rel-chip">{html.escape(comp_label.capitalize())} →</a></div></div>
</div></div>'''
    open(out,"w",encoding="utf-8").write(head(page_url,title,d,f"Code promo {name}",'<script type="application/ld+json">'+art+'</script>\n<script type="application/ld+json">'+faq_ld(faq)+'</script>\n')+body+FOOT)
    return True

def gen_parrainage(slug, name, url, vert, desc):
    n = html.escape(name)
    label, comp_url, comp_label, risk, *_ = VERT[vert]
    out = f"parrainage/{slug}.html"
    if os.path.exists(out): return False
    page_url = f"https://selectum.fr/parrainage/{slug}.html"
    title = f"Parrainage {name} 2026 : prime et conditions | Selectum"
    d = f"Parrainage {name} 2026 : comment ça marche, prime de bienvenue et conditions. {desc}"
    faq = [(f"Comment fonctionne le parrainage {name} ?", f"Le principe : un filleul s'inscrit via une offre dédiée et les deux parties reçoivent une prime, selon les conditions {name} en vigueur."),
           (f"Quelle prime de parrainage chez {name} ?", f"Le montant évolue régulièrement. L'offre de bienvenue accessible via notre lien est la voie la plus simple ; vérifiez les conditions à jour sur le site {name}."),
           (f"Le parrainage {name} est-il cumulable ?", "Les règles de cumul dépendent de chaque marque ; consultez les conditions officielles avant de souscrire.")]
    art = json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":d,
        "author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum",
        "logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},
        "datePublished":"2026-06-12","dateModified":"2026-06-12","mainEntityOfPage":page_url},ensure_ascii=False)
    body = f'''<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span>Parrainage<span>/</span>{n}</div>
  <h1>Parrainage {n} : prime et conditions</h1>
  <p class="updated">🗓️ Mis à jour le {D} par notre équipe</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
  <div class="intro-box"><p>Vous cherchez une <strong>offre de parrainage {n}</strong> ? {html.escape(desc)} Voici comment en profiter, vérifié le {D}.</p></div>
  <h2>Comment être parrainé chez {n}</h2>
  <p>La façon la plus simple de bénéficier de l'avantage de bienvenue est de passer par l'offre en cours :</p>
  <div class="promo-box"><span class="promo-badge">🎁 Offre de bienvenue</span>
    <h3>Profitez de l'offre {n}</h3>
    <div class="promo-reveal"><div class="promo-code">OFFRE EN COURS</div>
    <a href="/go/{slug}" class="promo-btn" target="_blank" rel="sponsored nofollow noopener">Révéler l'offre</a></div>
    <p class="promo-note">Conditions susceptibles d'évoluer — vérifiées le {D}.</p>
  </div>
  <div class="highlight-box"><p>💡 Voir aussi notre <a href="/avis/{slug}.html">avis {n}</a>, le <a href="/code-promo/{slug}.html">code promo {n}</a> et notre <a href="{comp_url}">{html.escape(comp_label)}</a>.</p></div>
  <div class="faq"><h2>❓ Questions fréquentes</h2>{"".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)}</div>
  <div class="rel-links"><h2>À lire aussi</h2><div class="rel-list"><a href="/avis/{slug}.html" class="rel-chip">Avis {n} →</a><a href="/code-promo/{slug}.html" class="rel-chip">Code promo {n} →</a><a href="{comp_url}" class="rel-chip">{html.escape(comp_label.capitalize())} →</a></div></div>
</div></div>'''
    open(out,"w",encoding="utf-8").write(head(page_url,title,d,f"Parrainage {name}",'<script type="application/ld+json">'+art+'</script>\n<script type="application/ld+json">'+faq_ld(faq)+'</script>\n')+body+FOOT)
    return True

def fetch_logo(slug, url):
    p = f"assets/logos/{slug}.png"
    if os.path.exists(p) and os.path.getsize(p) >= 800: return "exists"
    dom = url.split("//")[-1].split("/")[0].replace("www.","")
    for src in [f"https://www.google.com/s2/favicons?domain={dom}&sz=256", f"https://icons.duckduckgo.com/ip3/{dom}.ico"]:
        try:
            req = urllib.request.Request(src, headers={"User-Agent":"Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=15).read()
            if len(data) < 300: continue
            open("/tmp/lg.img","wb").write(data)
            if data[:4] == b"\x89PNG":
                open(p,"wb").write(data)
            else:
                subprocess.run(["sips","-s","format","png","/tmp/lg.img","--out",p], capture_output=True)
            if os.path.exists(p) and open(p,"rb").read(4) == b"\x89PNG":
                return "ok"
        except Exception:
            continue
    return "fail"

def main():
    os.makedirs("avis", exist_ok=True); os.makedirs("code-promo", exist_ok=True); os.makedirs("parrainage", exist_ok=True)
    na=nc=np=0; lo_ok=lo_fail=0; redirects=[]
    existing_go = open("_redirects").read()
    for slug,name,url,vert,desc in BRANDS:
        r = fetch_logo(slug, url)
        if r in ("ok","exists"): lo_ok+=1
        else: lo_fail+=1; print("logo FAIL:", slug)
        if gen_avis(slug,name,url,vert,desc): na+=1
        if gen_codepromo(slug,name,url,vert,desc): nc+=1
        if gen_parrainage(slug,name,url,vert,desc): np+=1
        if f"/go/{slug} " not in existing_go and f"/go/{slug}\t" not in existing_go and f"\n/go/{slug}" not in existing_go:
            redirects.append(f"/go/{slug}".ljust(22) + f" {url} 302")
    if redirects:
        with open("_redirects","a",encoding="utf-8") as f:
            f.write("\n# Curation 1parrainage — verticales Selectum (liens à brancher)\n" + "\n".join(redirects) + "\n")
    print(f"avis:{na} code-promo:{nc} parrainage:{np} | logos ok:{lo_ok} fail:{lo_fail} | redirects ajoutés:{len(redirects)}")

if __name__ == "__main__":
    main()
