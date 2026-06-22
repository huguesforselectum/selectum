#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 7 : long-tail supplementaire (crypto, banque, bourse, epargne, compte-pro, vpn)."""
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
 "banque":[("/comparatifs/banque-en-ligne.html","Comparatif des banques en ligne"),("/code-promo/n26.html","Code promo N26"),("/code-promo/revolut.html","Offres Revolut"),("/code-promo/boursobank.html","Code promo BoursoBank")],
 "bourse":[("/comparatifs/trading-bourse.html","Comparatif des courtiers en bourse"),("/code-promo/xtb.html","Code promo XTB"),("/code-promo/trade-republic.html","Offres Trade Republic"),("/code-promo/etoro.html","Code promo eToro")],
 "epargne":[("/comparatifs/assurance-vie.html","Comparatif assurance-vie"),("/comparatifs/per-retraite.html","Comparatif PER"),("/code-promo/linxea.html","Code promo Linxea"),("/code-promo/yomoni.html","Offres Yomoni")],
 "compte-pro":[("/comparatifs/comptes-pro.html","Comparatif des comptes pro"),("/comparatifs/facturation.html","Logiciels de facturation"),("/code-promo/qonto.html","Code promo Qonto"),("/code-promo/shine.html","Offres Shine")],
 "vpn":[("/comparatifs/vpn.html","Comparatif des VPN"),("/code-promo/expressvpn.html","Code promo ExpressVPN"),("/code-promo/nordvpn.html","Offres NordVPN"),("/code-promo/surfshark.html","Code promo Surfshark")],
}
CATLABEL={"crypto":"Crypto","banque":"Banque","bourse":"Bourse","epargne":"Épargne","compte-pro":"Compte pro","vpn":"Tech"}
G=[]
def add(**k): G.append(k)

add(slug="comment-stocker-ses-cryptos",cat="crypto",
 title="Comment stocker ses cryptomonnaies en sécurité en 2026 ?",
 desc="Comment stocker ses cryptos en 2026 : wallet d'exchange, hot wallet, cold wallet (Ledger), phrase de récupération. Le guide clair pour sécuriser ses cryptomonnaies.",
 h1="Comment stocker ses cryptomonnaies en sécurité ?",
 lead="Acheter des cryptos, c'est facile ; bien les conserver l'est moins. Voici les options et les règles de sécurité essentielles.",
 body=H2("options","Les façons de stocker ses cryptos")
  +UL(["<strong>Sur l'application crypto</strong> (custodial) : simple, mais vous ne détenez pas les clés.",
       "<strong>Hot wallet</strong> (portefeuille logiciel) : vous gardez les clés, connecté à internet.",
       "<strong>Cold wallet</strong> (Ledger, Trezor) : clés hors ligne, sécurité maximale."])
  +H2("phrase","La phrase de récupération")
  +P("Votre <strong>seed phrase</strong> (12 ou 24 mots) est la clé de tout. Notez-la sur papier, jamais en photo ni en ligne. Quiconque la possède contrôle vos fonds.")
  +H2("regles","Les règles d'or")
  +UL(["Activez la <strong>2FA</strong> partout.","Ne partagez jamais vos clés privées.","Méfiez-vous du <strong>phishing</strong> et des fausses applications.","Pour de gros montants, privilégiez le <strong>cold wallet</strong>."])
  +BOX("💡 Voir <a href=\"/guides/hot-wallet-ou-cold-wallet.html\">hot wallet ou cold wallet</a> et notre <a href=\"/comparatifs/crypto.html\">comparatif des applications crypto</a>."),
 faq=[("Où stocker ses cryptos en sécurité ?","Pour de petits montants, l'application crypto suffit ; pour de gros montants, un cold wallet (Ledger) hors ligne est le plus sûr."),
      ("Qu'est-ce qu'une phrase de récupération ?","Une suite de 12 ou 24 mots qui permet de restaurer votre portefeuille. À conserver hors ligne et à ne jamais partager."),
      ("Faut-il un Ledger pour débuter ?","Pas indispensable au début, mais recommandé dès que vous détenez des sommes importantes en crypto.")]),

add(slug="bitcoin-halving-comment-ca-marche",cat="crypto",
 title="Le halving du Bitcoin : comment ça marche en 2026 ?",
 desc="Le halving du Bitcoin en 2026 : principe, calendrier, effet sur l'offre et le prix. Le guide clair pour comprendre cet événement clé du Bitcoin.",
 h1="Le halving du Bitcoin : comment ça marche ?",
 lead="Le halving est un événement programmé qui réduit l'émission de nouveaux bitcoins. Voici son mécanisme et ce qu'il faut en penser.",
 body=H2("principe","Le principe")
  +P("Environ tous les <strong>quatre ans</strong>, la récompense versée aux mineurs de Bitcoin est <strong>divisée par deux</strong>. Cela ralentit la création de nouveaux bitcoins et renforce la rareté programmée (21 millions au total).")
  +H2("effet","Quel effet sur le prix ?")
  +P("Historiquement, le halving a précédé des phases de hausse, car l'offre nouvelle diminue. Mais <strong>rien n'est garanti</strong> : le prix dépend de nombreux facteurs et reste très volatil.")
  +H2("retenir","À retenir")
  +UL(["Le halving réduit l'émission, pas le nombre de bitcoins existants.","Les performances passées ne préjugent pas du futur.","C'est un élément de contexte, pas un signal d'achat."])
  +BOX("⚠️ Investir dans le Bitcoin comporte un risque de perte en capital. Voir notre <a href=\"/comparatifs/crypto.html\">comparatif des applications crypto</a>."),
 faq=[("C'est quoi le halving du Bitcoin ?","Un événement programmé qui divise par deux la récompense des mineurs, tous les ~4 ans, ralentissant la création de nouveaux bitcoins."),
      ("Le halving fait-il monter le prix ?","Il a historiquement précédé des hausses, mais sans aucune garantie : le prix du Bitcoin reste très volatil."),
      ("Quand a lieu le prochain halving ?","Le halving survient environ tous les quatre ans ; le dernier a eu lieu en 2024.")]),

add(slug="comment-payer-moins-frais-bancaires",cat="banque",
 title="Comment payer moins de frais bancaires en 2026 ?",
 desc="Comment réduire ses frais bancaires en 2026 : frais à traquer, banques en ligne, négociation, paiements à l'étranger. Le guide concret pour économiser sur sa banque.",
 h1="Comment payer moins de frais bancaires ?",
 lead="Les frais bancaires grignotent votre budget souvent sans que vous le remarquiez. Voici comment les réduire fortement.",
 body=H2("traquer","Les frais à traquer")
  +UL(["<strong>Cotisation carte</strong> et tenue de compte.",
       "<strong>Frais à l'étranger</strong> (paiements et retraits hors zone euro).",
       "<strong>Commissions d'intervention</strong> et incidents.",
       "<strong>Virements</strong> instantanés ou internationaux."])
  +H2("solutions","Comment économiser")
  +UL(["Passer à une <strong>banque en ligne</strong> (souvent gratuite sous conditions).",
       "Utiliser une <strong>néobanque</strong> pour les paiements à l'étranger sans surcoût.",
       "<strong>Négocier</strong> ou faire jouer la concurrence chaque année.",
       "Surveiller son relevé pour repérer les frais évitables."])
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a> et voir <a href=\"/guides/comment-changer-de-banque.html\">comment changer de banque</a>."),
 faq=[("Comment réduire ses frais bancaires ?","Passer à une banque en ligne, utiliser une néobanque pour l'étranger, négocier chaque année et surveiller les frais sur ses relevés."),
      ("Les banques en ligne sont-elles vraiment gratuites ?","La carte est souvent gratuite sous condition d'usage ou de revenus, et beaucoup de frais classiques disparaissent."),
      ("Comment éviter les frais à l'étranger ?","Une néobanque (N26, Revolut) permet de payer hors zone euro sans surcoût, contrairement à beaucoup de banques classiques.")]),

add(slug="carte-virtuelle-comment-ca-marche",cat="banque",
 title="Carte bancaire virtuelle : comment ça marche en 2026 ?",
 desc="La carte bancaire virtuelle en 2026 : principe, sécurité des achats en ligne, cartes éphémères, banques qui la proposent. Le guide pour payer plus sûr sur internet.",
 h1="Carte bancaire virtuelle : comment ça marche ?",
 lead="La carte virtuelle protège vos achats en ligne en masquant votre vraie carte. Voici son fonctionnement et son intérêt.",
 body=H2("principe","Le principe")
  +P("Une <strong>carte virtuelle</strong> est un numéro de carte généré pour payer en ligne, sans exposer votre carte physique. Certaines sont <strong>éphémères</strong> (à usage unique) ou plafonnées.")
  +H2("avantages","Pourquoi l'utiliser")
  +UL(["<strong>Sécurité</strong> : en cas de fuite, votre vraie carte reste protégée.",
       "<strong>Contrôle</strong> : plafonds et cartes à usage unique.",
       "Idéal pour les <strong>abonnements</strong> et sites peu connus."])
  +H2("ou","Où en obtenir ?")
  +P("De nombreuses néobanques et banques en ligne (Revolut, N26…) proposent des cartes virtuelles directement depuis l'application.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a>."),
 faq=[("À quoi sert une carte bancaire virtuelle ?","À payer en ligne sans exposer votre vraie carte : en cas de fuite de données, votre carte physique reste protégée."),
      ("La carte virtuelle est-elle gratuite ?","Elle est souvent incluse dans les offres des néobanques et banques en ligne, parfois selon le plan."),
      ("Peut-on utiliser une carte virtuelle en magasin ?","Surtout en ligne ; certaines s'ajoutent au paiement mobile pour régler en magasin via le téléphone.")]),

add(slug="etf-msci-world-comment-investir",cat="bourse",
 title="ETF MSCI World : comment investir en 2026 ?",
 desc="Investir dans un ETF MSCI World en 2026 : principe, diversification mondiale, où l'acheter (PEA, CTO, assurance-vie), frais. Le guide pour débuter simplement en bourse.",
 h1="ETF MSCI World : comment investir ?",
 lead="L'ETF MSCI World est l'un des placements préférés des investisseurs long terme. Voici pourquoi et comment y investir.",
 body=H2("principe","Qu'est-ce que le MSCI World ?")
  +P("Le <strong>MSCI World</strong> regroupe des centaines de grandes entreprises des pays développés. Un <strong>ETF</strong> qui le réplique permet d'investir d'un coup dans cette diversification mondiale, à frais réduits.")
  +H2("ou","Où l'acheter ?")
  +UL(["<strong>PEA</strong> : via un ETF éligible, fiscalité avantageuse après 5 ans.",
       "<strong>Compte-titres (CTO)</strong> : plus large, sans plafond.",
       "<strong>Assurance-vie</strong> : selon les unités de compte proposées."])
  +H2("conseils","Bonnes pratiques")
  +UL(["Investir <strong>régulièrement</strong> (versements programmés).",
       "Viser le <strong>long terme</strong> et ignorer le bruit de court terme.",
       "Comparer les <strong>frais</strong> de l'ETF et du support."])
  +BOX("⚠️ Investir comporte un risque de perte en capital. Voir <a href=\"/guides/comment-choisir-un-etf.html\">comment choisir un ETF</a> et le <a href=\"/comparatifs/trading-bourse.html\">comparatif des courtiers</a>."),
 faq=[("Le MSCI World, c'est quoi ?","Un indice de centaines de grandes entreprises des pays développés. Un ETF MSCI World permet d'investir dans cette diversification mondiale."),
      ("Où acheter un ETF MSCI World ?","Via un PEA (fiscalité douce), un compte-titres ou une assurance-vie, selon les supports disponibles."),
      ("Est-ce risqué ?","Comme tout placement actions, il comporte un risque de perte en capital ; il se conçoit sur le long terme.")]),

add(slug="dividendes-comment-ca-marche",cat="bourse",
 title="Les dividendes en bourse : comment ça marche en 2026 ?",
 desc="Les dividendes en 2026 : principe, date de détachement, fiscalité (flat tax), réinvestissement. Le guide clair pour comprendre les dividendes d'actions.",
 h1="Les dividendes en bourse : comment ça marche ?",
 lead="Les dividendes sont une part des bénéfices reversée aux actionnaires. Voici leur fonctionnement et leur fiscalité.",
 body=H2("principe","Le principe")
  +P("Quand une entreprise réalise des bénéfices, elle peut en reverser une partie sous forme de <strong>dividende</strong> à ses actionnaires. Toutes les sociétés n'en versent pas ; certaines réinvestissent tout.")
  +H2("date","Date de détachement")
  +P("Pour toucher le dividende, il faut détenir l'action avant la <strong>date de détachement</strong>. Le cours baisse mécaniquement du montant du dividende ce jour-là.")
  +H2("fiscalite","Fiscalité")
  +P("Hors enveloppes spécifiques, les dividendes sont soumis à la <strong>flat tax</strong> (prélèvement forfaitaire unique). Dans un <strong>PEA</strong>, ils profitent d'un cadre plus favorable.")
  +BOX("⚠️ Investir comporte un risque de perte en capital. Voir <a href=\"/guides/comment-ouvrir-un-pea.html\">comment ouvrir un PEA</a> et le <a href=\"/comparatifs/trading-bourse.html\">comparatif des courtiers</a>."),
 faq=[("Qu'est-ce qu'un dividende ?","Une part des bénéfices qu'une entreprise reverse à ses actionnaires. Toutes les sociétés n'en versent pas."),
      ("Comment sont imposés les dividendes ?","En général via la flat tax (prélèvement forfaitaire unique) ; le PEA offre un cadre plus avantageux sous conditions."),
      ("Faut-il réinvestir ses dividendes ?","Sur le long terme, réinvestir les dividendes accélère l'effet des intérêts composés.")]),

add(slug="comment-cloturer-un-pea",cat="bourse",
 title="Comment clôturer un PEA en 2026 (et les conséquences) ?",
 desc="Clôturer un PEA en 2026 : procédure, conséquences fiscales selon l'âge du plan, transfert plutôt que clôture. Le guide clair avant de fermer son PEA.",
 h1="Comment clôturer un PEA ?",
 lead="Clôturer un PEA n'est pas anodin : l'âge du plan change tout côté fiscalité. Voici ce qu'il faut savoir avant d'agir.",
 body=H2("age","L'âge du plan change tout")
  +UL(["<strong>Avant 5 ans</strong> : tout retrait entraîne en principe la clôture et une fiscalité moins favorable.",
       "<strong>Après 5 ans</strong> : les gains bénéficient d'une fiscalité allégée, et un retrait ne ferme plus le plan."])
  +H2("transfert","Transférer plutôt que clôturer")
  +P("Si vous changez d'établissement, préférez le <strong>transfert de PEA</strong> : vous conservez l'antériorité fiscale, ce qui est bien plus avantageux qu'une clôture suivie d'une réouverture.")
  +H2("etapes","Les étapes")
  +OL(["Vendre ou transférer les titres.","Demander la clôture à votre établissement.","Vérifier l'imposition des gains selon l'âge du plan."])
  +BOX("💡 Voir <a href=\"/guides/comment-ouvrir-un-pea.html\">comment ouvrir un PEA</a> et le <a href=\"/comparatifs/trading-bourse.html\">comparatif des courtiers</a>."),
 faq=[("Clôturer un PEA avant 5 ans, quelles conséquences ?","Un retrait avant 5 ans entraîne en principe la clôture et une fiscalité moins favorable sur les gains."),
      ("Vaut-il mieux transférer ou clôturer son PEA ?","Le transfert conserve l'antériorité fiscale du plan : c'est presque toujours préférable à une clôture-réouverture."),
      ("Un retrait après 5 ans ferme-t-il le PEA ?","Non, depuis la réforme, un retrait après 5 ans ne ferme plus le plan et vous pouvez continuer à verser.")]),

add(slug="meilleur-livret-epargne",cat="epargne",
 title="Meilleur livret d'épargne en 2026 : lequel choisir ?",
 desc="Meilleur livret d'épargne en 2026 : Livret A, LDDS, LEP, livrets boostés. Plafonds, taux, disponibilité. Le guide pour placer son épargne de précaution sans risque.",
 h1="Meilleur livret d'épargne : lequel choisir ?",
 lead="Pour l'épargne de précaution, le bon livret dépend de votre situation. Voici comment les comparer simplement.",
 body=H2("reglementes","Les livrets réglementés")
  +UL(["<strong>Livret A</strong> et <strong>LDDS</strong> : disponibles, défiscalisés, plafonnés.",
       "<strong>LEP</strong> : taux plus élevé, réservé sous conditions de revenus — à privilégier si vous y êtes éligible."])
  +H2("boostes","Les livrets bancaires boostés")
  +P("Certaines banques proposent des <strong>taux promotionnels</strong> temporaires sur leurs livrets. Attention : le taux de base après la promo est souvent bas, et les intérêts sont fiscalisés.")
  +H2("choisir","Comment choisir ?")
  +P("Remplissez d'abord les <strong>livrets réglementés</strong> (surtout le LEP si éligible), puis envisagez un livret boosté pour l'excédent. Au-delà de l'épargne de précaution, l'<strong>assurance-vie</strong> prend le relais pour le long terme.")
  +BOX("💡 Voir <a href=\"/guides/comment-epargner-chaque-mois.html\">comment épargner chaque mois</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Quel est le meilleur livret d'épargne ?","Le LEP si vous y êtes éligible (taux le plus élevé), sinon le Livret A et le LDDS pour une épargne disponible et défiscalisée."),
      ("Les livrets boostés valent-ils le coup ?","Pour placer un excédent à court terme, oui, mais le taux promotionnel est temporaire et les intérêts sont fiscalisés."),
      ("Que faire quand le Livret A est plein ?","Compléter avec le LDDS/LEP, puis se tourner vers l'assurance-vie pour le long terme.")]),

add(slug="comment-investir-petit-budget",cat="epargne",
 title="Comment investir avec un petit budget en 2026 ?",
 desc="Comment investir avec un petit budget en 2026 : versements programmés, ETF, assurance-vie, crypto raisonnée. Le guide pour commencer à investir même avec peu.",
 h1="Comment investir avec un petit budget ?",
 lead="Pas besoin de gros capital pour commencer : la régularité compte plus que le montant. Voici comment débuter avec peu.",
 body=H2("regularite","La régularité avant le montant")
  +P("Investir <strong>un peu chaque mois</strong> (versements programmés) lisse les prix et fait jouer les intérêts composés. Mieux vaut 50 €/mois régulièrement qu'attendre d'avoir une grosse somme.")
  +H2("ou","Où investir avec peu ?")
  +UL(["<strong>ETF</strong> via un PEA ou un compte-titres : diversification mondiale à faible coût.",
       "<strong>Assurance-vie</strong> en gestion pilotée : accessible dès quelques dizaines d'euros.",
       "<strong>Crypto raisonnée</strong> : une petite part seulement, en connaissant les risques."])
  +H2("eviter","À éviter")
  +UL(["Les frais élevés qui grignotent un petit capital.","Les placements que vous ne comprenez pas.","Investir l'argent dont vous avez besoin à court terme."])
  +BOX("⚠️ Investir comporte un risque de perte en capital. Voir <a href=\"/guides/comment-placer-10000-euros.html\">comment placer son épargne</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Peut-on investir avec un petit budget ?","Oui : des versements programmés de quelques dizaines d'euros suffisent pour débuter en ETF ou en assurance-vie."),
      ("Combien faut-il pour commencer ?","On peut commencer avec très peu ; l'important est la régularité et le long terme, pas le montant de départ."),
      ("Faut-il garder une épargne de précaution ?","Oui : constituez d'abord une réserve sur livret avant d'investir l'argent dont vous n'avez pas besoin à court terme.")]),

add(slug="comment-facturer-en-freelance",cat="compte-pro",
 title="Comment facturer en freelance en 2026 (mentions obligatoires) ?",
 desc="Comment facturer en freelance en 2026 : mentions obligatoires, numérotation, TVA, délais de paiement, logiciel de facturation. Le guide pratique pour des factures conformes.",
 h1="Comment facturer en freelance ?",
 lead="Une facture conforme protège votre activité et accélère les paiements. Voici les règles essentielles pour bien facturer.",
 body=H2("mentions","Les mentions obligatoires")
  +UL(["Identité et coordonnées (vous et le client), numéro SIREN.",
       "<strong>Numéro de facture</strong> unique et séquentiel.",
       "Date, description des prestations, quantités et prix.",
       "<strong>TVA</strong> (ou mention « TVA non applicable, art. 293 B du CGI » si franchise).",
       "Conditions et <strong>délais de paiement</strong>, pénalités de retard."])
  +H2("outils","Un logiciel pour gagner du temps")
  +P("Un <strong>logiciel de facturation</strong> garantit la numérotation, calcule la TVA et conserve l'historique — utile aussi pour la <strong>facturation électronique</strong> qui se généralise.")
  +H2("paiement","Se faire payer")
  +P("Indiquez clairement le délai, relancez sans tarder, et envisagez un acompte pour les grosses missions. Un <strong>compte pro</strong> séparé facilite le suivi.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/facturation.html\">comparatif des logiciels de facturation</a> et le <a href=\"/comparatifs/comptes-pro.html\">comparatif des comptes pro</a>."),
 faq=[("Quelles mentions obligatoires sur une facture ?","Identités, SIREN, numéro de facture unique, date, détail des prestations, TVA (ou mention de franchise), et conditions de paiement."),
      ("Faut-il un logiciel de facturation ?","Ce n'est pas obligatoire mais fortement recommandé : numérotation fiable, TVA, archivage et conformité à la facturation électronique."),
      ("Un freelance doit-il facturer la TVA ?","Cela dépend du régime : en franchise en base, on facture sans TVA avec la mention légale ; au-delà des seuils, la TVA s'applique.")]),

add(slug="micro-entreprise-plafonds-2026",cat="compte-pro",
 title="Micro-entreprise : plafonds et seuils 2026",
 desc="Plafonds de la micro-entreprise en 2026 : seuils de chiffre d'affaires, TVA, conséquences d'un dépassement. Le guide clair pour rester dans le régime micro.",
 h1="Micro-entreprise : plafonds et seuils 2026",
 lead="Le régime micro est simple mais plafonné. Voici comment fonctionnent les seuils et ce qui se passe en cas de dépassement.",
 body=H2("seuils","Deux types de seuils")
  +UL(["Un <strong>plafond de chiffre d'affaires</strong> selon l'activité (vente de marchandises vs prestations de services).",
       "Un <strong>seuil de TVA</strong> (franchise en base) à partir duquel vous devez facturer la TVA."])
  +P("Les montants exacts sont fixés par l'administration et peuvent évoluer : vérifiez les seuils en vigueur sur les sources officielles avant de vous baser dessus.")
  +H2("depassement","En cas de dépassement")
  +P("Un dépassement du plafond de CA peut vous faire <strong>basculer hors du régime micro</strong> (selon la durée du dépassement). Le franchissement du seuil de TVA vous oblige à la <strong>facturer</strong>.")
  +H2("anticiper","Anticiper")
  +P("Suivez votre CA en continu, mettez de côté pour les cotisations et la TVA éventuelle, et envisagez un changement de statut si votre activité grossit durablement.")
  +BOX("💡 Voir <a href=\"/guides/comment-devenir-auto-entrepreneur.html\">devenir auto-entrepreneur</a> et le <a href=\"/comparatifs/comptes-pro.html\">comparatif des comptes pro</a>."),
 faq=[("Quels sont les plafonds de la micro-entreprise ?","Il existe un plafond de CA distinct pour la vente et pour les services, plus un seuil de franchise de TVA. Vérifiez les montants en vigueur sur les sources officielles."),
      ("Que se passe-t-il si je dépasse le plafond ?","Un dépassement durable du plafond de CA peut entraîner la sortie du régime micro ; le seuil de TVA franchi oblige à facturer la TVA."),
      ("La micro-entreprise facture-t-elle la TVA ?","Pas tant que vous êtes sous le seuil de franchise ; au-delà, vous devez facturer et reverser la TVA.")]),

add(slug="vpn-pour-streaming",cat="vpn",
 title="Quel VPN pour le streaming en 2026 ?",
 desc="Quel VPN choisir pour le streaming en 2026 : vitesse, déblocage de catalogues, légalité, critères. Le guide pour choisir un VPN adapté au streaming.",
 h1="Quel VPN pour le streaming ?",
 lead="Tous les VPN ne se valent pas pour le streaming : vitesse et fiabilité font la différence. Voici comment choisir.",
 body=H2("criteres","Ce qui compte pour le streaming")
  +UL(["<strong>Vitesse</strong> élevée et stable pour la HD/4K.",
       "<strong>Nombre de serveurs</strong> et de pays disponibles.",
       "<strong>Fiabilité</strong> du déblocage des catalogues.",
       "<strong>Applications</strong> pour TV, mobile et box."])
  +H2("legal","Est-ce légal ?")
  +P("Utiliser un VPN est <strong>légal</strong> en France. En revanche, contourner des restrictions géographiques peut enfreindre les <strong>conditions d'utilisation</strong> de certains services : restez vigilant.")
  +H2("choisir","Notre approche")
  +P("Privilégiez un VPN reconnu pour sa vitesse et son réseau de serveurs, avec une politique <strong>no-log</strong> sérieuse. Comparez les offres sur l'engagement long, souvent le moins cher.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/vpn.html\">comparatif des VPN</a> et voir <a href=\"/guides/meilleur-vpn-pas-cher.html\">le meilleur VPN pas cher</a>."),
 faq=[("Quel est le meilleur VPN pour le streaming ?","Celui qui offre vitesse, large réseau de serveurs et applications pour tous vos écrans, avec une politique no-log sérieuse."),
      ("Utiliser un VPN pour le streaming est-il légal ?","Le VPN est légal en France ; contourner des restrictions géographiques peut toutefois enfreindre les conditions d'utilisation de certains services."),
      ("Un VPN ralentit-il le streaming ?","Un bon VPN limite la perte de vitesse ; choisissez un service réputé rapide pour la HD/4K.")])

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
print("batch 7 guides créés :", len(G))
