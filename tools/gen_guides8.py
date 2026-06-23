#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 8 : long-tail supplementaire. Reutilise le template du batch 7."""
import os
from gen_guides7 import P,H2,UL,OL,BOX,SILO,CATLABEL,page

G=[]
def add(**k): G.append(k)

add(slug="comment-revendre-ses-cryptos",cat="crypto",
 title="Comment revendre ses cryptomonnaies en 2026 ?",
 desc="Comment revendre ses cryptos en 2026 : vendre contre euros, retrait SEPA, frais, fiscalité de la plus-value. Le guide clair pour encaisser ses cryptomonnaies.",
 h1="Comment revendre ses cryptomonnaies ?",
 lead="Revendre ses cryptos pour récupérer des euros est simple, mais quelques points méritent attention : frais, délais et fiscalité.",
 body=H2("etapes","Les étapes pour vendre")
  +OL(["Se connecter à son application crypto.",
       "Vendre la crypto <strong>contre des euros</strong> (idéalement via l'interface avancée pour réduire les frais).",
       "Demander un <strong>retrait SEPA</strong> vers son compte bancaire.",
       "Attendre le délai de virement (souvent quelques heures à 1-2 jours)."])
  +H2("frais","Frais et délais")
  +P("Vérifiez les <strong>frais de vente</strong> et de retrait. Un ordre limite coûte généralement moins cher qu'un achat/vente instantané. Le virement SEPA est le moyen de retrait le moins cher.")
  +H2("fiscalite","La fiscalité")
  +P("En France, la <strong>plus-value</strong> réalisée lors d'une conversion crypto → euros est imposable. Pensez à conserver l'historique pour votre déclaration.")
  +BOX("⚠️ Investir comporte un risque de perte en capital. Voir <a href=\"/guides/declarer-cryptomonnaies-impots.html\">déclarer ses cryptos aux impôts</a> et le <a href=\"/comparatifs/crypto.html\">comparatif des applications crypto</a>."),
 faq=[("Comment transformer ses cryptos en euros ?","On vend la crypto contre des euros sur son application, puis on demande un retrait SEPA vers son compte bancaire."),
      ("La revente de crypto est-elle imposable ?","Oui : la plus-value lors d'une conversion en euros est imposable en France. Conservez votre historique de transactions."),
      ("Combien de temps pour récupérer son argent ?","Le retrait SEPA prend généralement de quelques heures à un ou deux jours ouvrés selon le service.")]),

add(slug="erreurs-debutant-crypto",cat="crypto",
 title="Les erreurs à éviter quand on débute en crypto en 2026",
 desc="Débuter en crypto en 2026 : les erreurs classiques à éviter (FOMO, sécurité, frais, fiscalité) et les bons réflexes. Le guide pour bien commencer sans se faire piéger.",
 h1="Les erreurs à éviter quand on débute en crypto",
 lead="Beaucoup de débutants perdent de l'argent par manque de méthode plus que par malchance. Voici les pièges les plus courants.",
 body=H2("erreurs","Les erreurs fréquentes")
  +UL(["<strong>Acheter sous le coup de l'émotion</strong> (FOMO) après une forte hausse.",
       "<strong>Négliger la sécurité</strong> : pas de 2FA, clés mal protégées.",
       "<strong>Ignorer les frais</strong> qui grignotent les petits montants.",
       "<strong>Oublier la fiscalité</strong> et la conservation de l'historique.",
       "<strong>Investir plus que ce qu'on peut perdre</strong>."])
  +H2("reflexes","Les bons réflexes")
  +UL(["Se former avant d'investir.",
       "Commencer petit, avec une application régulée.",
       "Activer la 2FA et sécuriser sa phrase de récupération.",
       "Penser long terme et diversifier."])
  +BOX("⚠️ Investir comporte un risque de perte en capital. Voir <a href=\"/guides/comment-acheter-cryptomonnaies.html\">comment acheter des cryptos</a> et le <a href=\"/comparatifs/crypto.html\">comparatif</a>."),
 faq=[("Quelle est la principale erreur des débutants en crypto ?","Acheter sous le coup de l'émotion après une hausse, sans méthode ni gestion du risque."),
      ("Combien investir pour débuter ?","Seulement ce que vous pouvez vous permettre de perdre, en commençant petit avec une application régulée."),
      ("Faut-il se former avant d'acheter des cryptos ?","Oui : comprendre les frais, la sécurité et la fiscalité évite la plupart des erreurs coûteuses.")]),

add(slug="compte-joint-comment-ouvrir",cat="banque",
 title="Compte joint : comment l'ouvrir et comment ça marche en 2026 ?",
 desc="Compte joint en 2026 : fonctionnement, avantages, responsabilité solidaire, ouverture en banque en ligne. Le guide clair pour ouvrir un compte joint à deux.",
 h1="Compte joint : comment ça marche ?",
 lead="Le compte joint simplifie la gestion des dépenses communes, mais engage les deux titulaires. Voici l'essentiel à savoir.",
 body=H2("principe","Le principe")
  +P("Un <strong>compte joint</strong> appartient à plusieurs titulaires (« M. ou Mme ») qui peuvent le faire fonctionner indépendamment. Il sert souvent à gérer les <strong>dépenses communes</strong> (loyer, courses).")
  +H2("responsabilite","La responsabilité solidaire")
  +P("Attention : les titulaires sont <strong>solidairement responsables</strong>. En cas de découvert ou d'incident, chacun peut être tenu pour la totalité. La confiance est essentielle.")
  +H2("ouvrir","Comment l'ouvrir ?")
  +P("Les <strong>banques en ligne</strong> permettent d'ouvrir un compte joint rapidement. Il faut les pièces d'identité et justificatifs des deux titulaires.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a>."),
 faq=[("Comment fonctionne un compte joint ?","Plusieurs titulaires partagent un même compte qu'ils peuvent utiliser indépendamment, souvent pour gérer des dépenses communes."),
      ("Qui est responsable en cas de découvert ?","Les titulaires sont solidairement responsables : chacun peut être tenu pour la totalité du solde négatif."),
      ("Peut-on ouvrir un compte joint en ligne ?","Oui, les banques en ligne le permettent rapidement avec les pièces d'identité des deux titulaires.")]),

add(slug="virement-instantane-comment-ca-marche",cat="banque",
 title="Le virement instantané : comment ça marche en 2026 ?",
 desc="Le virement instantané en 2026 : délai, plafonds, frais, sécurité. Le guide clair pour envoyer de l'argent en quelques secondes en toute sécurité.",
 h1="Le virement instantané : comment ça marche ?",
 lead="Le virement instantané transfère de l'argent en quelques secondes, 24h/24. Voici son fonctionnement, ses limites et ses précautions.",
 body=H2("principe","Le principe")
  +P("Le <strong>virement instantané</strong> (SEPA Instant) crédite le compte du bénéficiaire en <strong>quelques secondes</strong>, y compris le week-end et la nuit, contrairement au virement classique.")
  +H2("frais","Frais et plafonds")
  +P("De plus en plus de banques le proposent <strong>gratuitement</strong>. Des <strong>plafonds</strong> par opération peuvent s'appliquer selon l'établissement.")
  +H2("securite","Sécurité : la vigilance reste de mise")
  +P("Comme il est <strong>irréversible et immédiat</strong>, vérifiez toujours le bénéficiaire avant de valider. C'est un canal prisé des fraudeurs : ne cédez jamais à la pression.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a> et voir <a href=\"/guides/comment-securiser-son-compte-en-ligne.html\">sécuriser ses comptes</a>."),
 faq=[("Combien de temps prend un virement instantané ?","Quelques secondes seulement, à toute heure et tous les jours, contrairement au virement classique (1-2 jours ouvrés)."),
      ("Le virement instantané est-il gratuit ?","De plus en plus de banques le proposent gratuitement ; certaines le facturent encore. Des plafonds peuvent s'appliquer."),
      ("Peut-on annuler un virement instantané ?","Non, il est immédiat et irréversible : vérifiez bien le bénéficiaire avant de valider.")]),

add(slug="types-ordres-bourse",cat="bourse",
 title="Les types d'ordres en bourse : lequel choisir en 2026 ?",
 desc="Les types d'ordres en bourse en 2026 : ordre au marché, à cours limité, à seuil de déclenchement. Le guide clair pour passer ses ordres au bon prix.",
 h1="Les types d'ordres en bourse : lequel choisir ?",
 lead="Bien choisir son type d'ordre permet de maîtriser le prix d'exécution et le risque. Voici les principaux ordres expliqués simplement.",
 body=H2("marche","L'ordre au marché")
  +P("Exécuté <strong>immédiatement au meilleur prix disponible</strong>. Simple et rapide, mais le prix exact n'est pas garanti, surtout sur les valeurs peu liquides.")
  +H2("limite","L'ordre à cours limité")
  +P("Vous fixez un <strong>prix maximum à l'achat</strong> (ou minimum à la vente). L'ordre ne s'exécute que si le marché atteint ce prix : vous maîtrisez le coût, mais l'exécution n'est pas garantie.")
  +H2("seuil","L'ordre à seuil de déclenchement")
  +P("Se déclenche quand le cours franchit un <strong>seuil</strong> défini. Utile pour limiter les pertes (stop) ou suivre une tendance.")
  +BOX("⚠️ Investir comporte un risque de perte en capital. Voir <a href=\"/guides/comment-investir-en-bourse-debutant.html\">investir en bourse débutant</a> et le <a href=\"/comparatifs/trading-bourse.html\">comparatif des courtiers</a>."),
 faq=[("Quel type d'ordre choisir en bourse ?","L'ordre à cours limité pour maîtriser le prix, l'ordre au marché pour une exécution immédiate, le seuil de déclenchement pour limiter les pertes."),
      ("L'ordre au marché est-il risqué ?","Il garantit l'exécution mais pas le prix exact, ce qui peut surprendre sur les valeurs peu liquides ou volatiles."),
      ("À quoi sert un ordre stop ?","À déclencher une vente (ou un achat) quand le cours franchit un seuil, par exemple pour limiter une perte.")]),

add(slug="pea-jeune-comment-ca-marche",cat="bourse",
 title="Le PEA jeune : comment ça marche en 2026 ?",
 desc="Le PEA jeune en 2026 : conditions d'âge, plafond, fonctionnement, intérêt pour les 18-25 ans rattachés au foyer fiscal. Le guide pour commencer à investir tôt.",
 h1="Le PEA jeune : comment ça marche ?",
 lead="Le PEA jeune permet aux 18-25 ans rattachés au foyer fiscal de leurs parents de commencer à investir tôt, avec un cadre fiscal avantageux.",
 body=H2("qui","Pour qui ?")
  +P("Le <strong>PEA jeune</strong> s'adresse aux <strong>18-25 ans</strong> encore <strong>rattachés au foyer fiscal</strong> de leurs parents. Il fonctionne comme un PEA classique, avec un plafond de versement réduit.")
  +H2("interet","Pourquoi commencer tôt ?")
  +UL(["Profiter des <strong>intérêts composés</strong> sur une longue durée.",
       "Acquérir l'<strong>antériorité fiscale</strong> (les 5 ans courent dès l'ouverture).",
       "Apprendre à investir avec de petits montants."])
  +H2("apres","Et après 25 ans ?")
  +P("À la fin du rattachement, le PEA jeune se transforme en <strong>PEA classique</strong>, en conservant son antériorité — un vrai atout.")
  +BOX("⚠️ Investir comporte un risque de perte en capital. Voir <a href=\"/guides/comment-ouvrir-un-pea.html\">comment ouvrir un PEA</a> et le <a href=\"/comparatifs/trading-bourse.html\">comparatif des courtiers</a>."),
 faq=[("Qui peut ouvrir un PEA jeune ?","Les 18-25 ans rattachés au foyer fiscal de leurs parents. Il fonctionne comme un PEA avec un plafond réduit."),
      ("Quel est l'intérêt du PEA jeune ?","Commencer tôt fait jouer les intérêts composés et lance le compteur des 5 ans pour la fiscalité avantageuse."),
      ("Que devient le PEA jeune à 25 ans ?","Il se transforme en PEA classique en conservant son antériorité fiscale.")]),

add(slug="interets-composes-comment-ca-marche",cat="epargne",
 title="Les intérêts composés : comment ça marche en 2026 ?",
 desc="Les intérêts composés en 2026 : principe, effet boule de neige, importance du temps et de la régularité. Le guide pour comprendre le moteur de l'épargne long terme.",
 h1="Les intérêts composés : comment ça marche ?",
 lead="Les intérêts composés sont le moteur de l'épargne long terme. Comprendre leur effet change votre façon d'épargner.",
 body=H2("principe","Le principe")
  +P("Avec les <strong>intérêts composés</strong>, vos gains génèrent eux-mêmes des gains. Année après année, l'effet « <strong>boule de neige</strong> » accélère la croissance de votre capital.")
  +H2("temps","Le temps est votre allié")
  +P("Plus la durée est longue, plus l'effet est puissant. <strong>Commencer tôt</strong>, même avec peu, bat souvent un effort plus important mais tardif.")
  +H2("regularite","La régularité")
  +P("Des <strong>versements réguliers</strong> combinés aux intérêts composés construisent un capital significatif sur le long terme, sans à-coups.")
  +BOX("💡 Voir <a href=\"/guides/comment-epargner-chaque-mois.html\">comment épargner chaque mois</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("C'est quoi les intérêts composés ?","Un mécanisme où vos gains génèrent à leur tour des gains, créant un effet boule de neige sur le long terme."),
      ("Pourquoi commencer à épargner tôt ?","Parce que le temps amplifie les intérêts composés : commencer tôt, même avec peu, est très avantageux."),
      ("Faut-il réinvestir ses gains ?","Oui : c'est précisément le réinvestissement des gains qui active la puissance des intérêts composés.")]),

add(slug="gestion-pilotee-ou-libre",cat="epargne",
 title="Gestion pilotée ou libre : que choisir pour son assurance-vie en 2026 ?",
 desc="Gestion pilotée ou gestion libre en 2026 : différences, frais, autonomie, pour qui. Le guide pour choisir le bon mode de gestion de son assurance-vie ou PER.",
 h1="Gestion pilotée ou libre : que choisir ?",
 lead="Le mode de gestion détermine qui pilote vos investissements. Voici comment choisir selon votre temps et vos connaissances.",
 body=H2("pilotee","La gestion pilotée")
  +UL(["Un <strong>professionnel gère</strong> votre allocation selon votre profil de risque.",
       "Idéale si vous <strong>manquez de temps ou de connaissances</strong>.",
       "Des <strong>frais de gestion</strong> supplémentaires s'appliquent."])
  +H2("libre","La gestion libre")
  +UL(["Vous <strong>choisissez vous-même</strong> vos supports (fonds euros, ETF…).",
       "<strong>Moins de frais</strong>, plus de contrôle.",
       "Demande du <strong>temps</strong> et un minimum de connaissances."])
  +H2("choisir","Lequel choisir ?")
  +P("La <strong>gestion pilotée</strong> pour déléguer sereinement ; la <strong>gestion libre</strong> si vous aimez décider et voulez réduire les frais. Certains combinent les deux.")
  +BOX("💡 Voir notre <a href=\"/comparatifs/epargne-pilotee.html\">comparatif de la gestion pilotée</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Gestion pilotée ou libre, laquelle choisir ?","La pilotée pour déléguer sans y consacrer de temps ; la libre pour contrôler et réduire les frais si vous vous y connaissez."),
      ("La gestion pilotée coûte-t-elle plus cher ?","Oui, elle ajoute des frais de gestion, en contrepartie de l'allocation gérée par un professionnel."),
      ("Peut-on changer de mode de gestion ?","Oui, la plupart des contrats permettent de basculer entre gestion libre et pilotée.")]),

add(slug="tva-auto-entrepreneur",cat="compte-pro",
 title="TVA et auto-entrepreneur en 2026 : comment ça marche ?",
 desc="TVA et auto-entrepreneur en 2026 : franchise en base, seuils, mentions, passage à la TVA. Le guide clair pour savoir quand et comment facturer la TVA en micro.",
 h1="TVA et auto-entrepreneur : comment ça marche ?",
 lead="Tant qu'on est sous le seuil, l'auto-entrepreneur ne facture pas de TVA. Voici comment fonctionne ce régime et ce qui change au-delà.",
 body=H2("franchise","La franchise en base de TVA")
  +P("Sous un certain seuil de chiffre d'affaires, l'auto-entrepreneur bénéficie de la <strong>franchise en base</strong> : il <strong>ne facture pas la TVA</strong> et ne la récupère pas. La facture porte la mention « TVA non applicable, art. 293 B du CGI ».")
  +H2("seuil","Quand bascule-t-on à la TVA ?")
  +P("Au-delà du <strong>seuil de franchise</strong>, vous devez facturer la TVA, la déclarer et la reverser. Les montants exacts évoluent : vérifiez les seuils en vigueur sur les sources officielles.")
  +H2("consequences","Ce que ça change")
  +UL(["Vous ajoutez la TVA à vos prix (impact pour les clients particuliers).",
       "Vous pouvez <strong>récupérer la TVA</strong> sur vos achats professionnels.",
       "Des obligations déclaratives supplémentaires."])
  +BOX("💡 Voir <a href=\"/guides/comment-devenir-auto-entrepreneur.html\">devenir auto-entrepreneur</a> et le <a href=\"/comparatifs/comptes-pro.html\">comparatif des comptes pro</a>."),
 faq=[("L'auto-entrepreneur facture-t-il la TVA ?","Pas tant qu'il est sous le seuil de franchise en base : il facture sans TVA avec la mention légale. Au-delà, la TVA s'applique."),
      ("Quel est le seuil de TVA en micro ?","Il est fixé par l'administration et peut évoluer ; vérifiez le montant en vigueur sur les sources officielles."),
      ("Que se passe-t-il quand on dépasse le seuil ?","Vous devez facturer, déclarer et reverser la TVA, mais vous pouvez aussi la récupérer sur vos achats pro.")]),

add(slug="cotisations-urssaf-auto-entrepreneur",cat="compte-pro",
 title="Cotisations Urssaf de l'auto-entrepreneur en 2026 : comment ça marche ?",
 desc="Cotisations Urssaf de l'auto-entrepreneur en 2026 : calcul sur le chiffre d'affaires, déclaration, périodicité, ACRE. Le guide clair pour comprendre ses charges sociales.",
 h1="Cotisations Urssaf de l'auto-entrepreneur : comment ça marche ?",
 lead="En micro, les cotisations sociales se calculent simplement sur le chiffre d'affaires encaissé. Voici le fonctionnement.",
 body=H2("principe","Un calcul sur le chiffre d'affaires")
  +P("L'auto-entrepreneur paie ses <strong>cotisations sociales</strong> en pourcentage de son <strong>chiffre d'affaires encaissé</strong>. Pas de CA, pas de cotisation : c'est l'un des grands avantages du régime.")
  +H2("declaration","Déclarer et payer")
  +P("Vous déclarez votre CA <strong>mensuellement ou trimestriellement</strong> sur le site de l'Urssaf, qui calcule automatiquement les cotisations dues. Le taux dépend de votre activité.")
  +H2("acre","L'ACRE")
  +P("En début d'activité, l'<strong>ACRE</strong> peut réduire temporairement vos cotisations, sous conditions. Pensez à mettre de côté pour l'impôt et les charges.")
  +BOX("💡 Voir <a href=\"/guides/compte-pro-obligatoire-micro-entreprise.html\">compte pro et micro-entreprise</a> et le <a href=\"/comparatifs/comptes-pro.html\">comparatif des comptes pro</a>."),
 faq=[("Comment sont calculées les cotisations Urssaf en micro ?","En pourcentage du chiffre d'affaires encaissé, selon l'activité. Sans CA, aucune cotisation n'est due."),
      ("Quand déclarer son CA à l'Urssaf ?","Mensuellement ou trimestriellement, selon l'option choisie, sur le site de l'Urssaf."),
      ("Qu'est-ce que l'ACRE ?","Un dispositif qui réduit temporairement les cotisations en début d'activité, sous conditions d'éligibilité.")]),

add(slug="vpn-sur-mobile",cat="vpn",
 title="VPN sur mobile : comment ça marche et est-ce utile en 2026 ?",
 desc="VPN sur mobile en 2026 : utilité sur smartphone, Wi-Fi public, consommation de batterie, installation. Le guide pour protéger son téléphone avec un VPN.",
 h1="VPN sur mobile : est-ce utile ?",
 lead="On navigue surtout sur smartphone, souvent sur des Wi-Fi publics. Un VPN mobile a donc tout son sens. Voici pourquoi et comment.",
 body=H2("utilite","Pourquoi un VPN sur mobile ?")
  +UL(["<strong>Sécuriser les Wi-Fi publics</strong> (café, aéroport, hôtel).",
       "<strong>Protéger sa vie privée</strong> en masquant son adresse IP.",
       "Accéder à ses contenus en voyage."])
  +H2("batterie","Et la batterie ?")
  +P("Un VPN consomme un peu de <strong>batterie et de données</strong>, mais les applications modernes sont optimisées. Vous pouvez l'activer seulement sur les réseaux non sûrs.")
  +H2("installer","Comment l'installer ?")
  +P("Il suffit d'installer l'<strong>application du VPN</strong> (iOS ou Android), de se connecter et de choisir un serveur. Une option de connexion automatique sur Wi-Fi public est souvent disponible.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/vpn.html\">comparatif des VPN</a> et voir <a href=\"/guides/a-quoi-sert-un-vpn.html\">à quoi sert un VPN</a>."),
 faq=[("Un VPN est-il utile sur mobile ?","Oui, surtout sur les Wi-Fi publics : il sécurise la connexion et protège votre vie privée en masquant votre IP."),
      ("Un VPN vide-t-il la batterie ?","Il consomme un peu de batterie et de données, mais les applications récentes sont optimisées ; on peut l'activer à la demande."),
      ("Comment installer un VPN sur son téléphone ?","En installant l'application du fournisseur (iOS/Android), puis en se connectant à un serveur en un clic.")]),

add(slug="antivirus-gratuit-ou-payant",cat="vpn",
 title="Antivirus gratuit ou payant : que choisir en 2026 ?",
 desc="Antivirus gratuit ou payant en 2026 : différences, protections incluses, quand le payant vaut le coup. Le guide pour choisir la bonne protection pour son ordinateur.",
 h1="Antivirus gratuit ou payant : que choisir ?",
 lead="Les antivirus gratuits protègent l'essentiel, mais les versions payantes ajoutent des couches utiles. Voici comment trancher.",
 body=H2("gratuit","Ce que couvre le gratuit")
  +P("Un <strong>antivirus gratuit</strong> (ou la protection intégrée au système) bloque déjà l'essentiel des menaces courantes. C'est suffisant pour un usage prudent.")
  +H2("payant","Ce qu'ajoute le payant")
  +UL(["<strong>Protection web</strong> et anti-phishing renforcée.",
       "<strong>Pare-feu</strong> avancé, protection des paiements.",
       "Parfois un <strong>VPN</strong>, un gestionnaire de mots de passe, le contrôle parental.",
       "Support et protection multi-appareils."])
  +H2("choisir","Lequel choisir ?")
  +P("Le <strong>gratuit</strong> suffit pour un usage simple et prudent ; le <strong>payant</strong> se justifie pour un usage familial, sensible ou si vous voulez tout regrouper (antivirus + VPN + mots de passe).")
  +BOX("💡 Voir notre <a href=\"/guides/meilleur-antivirus.html\">guide meilleur antivirus</a> et le <a href=\"/comparatifs/vpn.html\">comparatif VPN</a>."),
 faq=[("Un antivirus gratuit suffit-il ?","Pour un usage prudent, oui : il bloque l'essentiel des menaces courantes. Le payant ajoute des protections supplémentaires."),
      ("Qu'apporte un antivirus payant ?","Une protection web renforcée, un pare-feu avancé et souvent des extras (VPN, gestionnaire de mots de passe, contrôle parental)."),
      ("Faut-il un antivirus en plus du système ?","La protection intégrée suffit souvent ; un antivirus dédié est utile si vous téléchargez beaucoup ou voulez plus de fonctionnalités.")])

os.makedirs("guides",exist_ok=True)
for d in G:
    open(f"guides/{d['slug']}.html","w",encoding="utf-8").write(page(d))
print("batch 8 guides créés :", len(G))
