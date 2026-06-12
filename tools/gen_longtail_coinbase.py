#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages long-tail Coinbase -> guides/ (réutilise le gabarit de gen_longtail_linxea_kraken.py)."""
import os

# On charge les helpers + page() du générateur existant, sans déclencher sa génération
src = open("tools/gen_longtail_linxea_kraken.py", encoding="utf-8").read()
prefix = src.split('os.makedirs("guides"', 1)[0]
ns = {}
exec(prefix, ns)
P, H2, OL, UL = ns["P"], ns["H2"], ns["OL"], ns["UL"]
BRAND = ns["BRAND"]; page = ns["page"]
def BOX(t): return f'<div class="highlight-box"><p>{t}</p></div>'

# NB compliance Coinbase : ne pas qualifier Coinbase de "plateforme"/"exchange" crypto.
BRAND["coinbase"] = dict(name="Coinbase", logo="/assets/logos/coinbase.png", cat="application crypto",
    compar="/comparatifs/crypto.html", compar_label="Comparatif crypto",
    avis="/avis/coinbase.html", promo="/code-promo/coinbase.html", parr="/parrainage/coinbase.html",
    go="/go/coinbase", risk="Investir dans les crypto-actifs comporte un risque de perte en capital.")

PAGES = []
def add(**k): PAGES.append(k)

add(slug="coinbase-frais", brand="coinbase",
 title="Frais Coinbase 2026 : achat, trading, retrait — le vrai coût",
 desc="Frais Coinbase 2026 expliqués : achat simple vs Coinbase Advanced, spread, retrait SEPA, abonnement Coinbase One. Comment payer moins cher sur Coinbase.",
 h1="Frais Coinbase 2026 : combien ça coûte vraiment ?",
 subtitle="Achat express, Coinbase Advanced, spread, retraits : on décortique la grille tarifaire de Coinbase.",
 leaf="Frais Coinbase",
 body=H2("interfaces","Deux interfaces, deux niveaux de frais")
  +P("Coinbase propose deux expériences avec des frais très différents. L'<strong>achat simple</strong> (interface classique) applique des frais plus élevés, "
     "tandis que <strong>Coinbase Advanced</strong> (anciennement Coinbase Pro) fonctionne sur un modèle <strong>maker/taker</strong> dégressif selon le volume, "
     "nettement plus avantageux.")
  +P("À cela s'ajoute le <strong>spread</strong> (écart entre prix d'achat et de vente), à prendre en compte dans le coût réel.")
  +H2("reduire","Comment réduire ses frais sur Coinbase")
  +OL(["Utiliser <strong>Coinbase Advanced</strong> plutôt que l'achat express.",
       "Privilégier les <strong>ordres limites (maker)</strong> plutôt qu'au marché.",
       "Alimenter le compte par <strong>virement SEPA</strong> en euros plutôt que par carte bancaire.",
       "Évaluer l'abonnement <strong>Coinbase One</strong> (frais de trading réduits/annulés contre un forfait mensuel) si vous tradez souvent."])
  +H2("depot-retrait","Dépôt et retrait")
  +UL(["<strong>Dépôt SEPA en euros</strong> : généralement gratuit ou à coût faible.",
       "<strong>Retrait SEPA</strong> : un montant fixe modique.",
       "<strong>Carte bancaire</strong> : plus cher, à éviter pour économiser.",
       "<strong>Retrait crypto</strong> : frais de réseau (blockchain) variables selon l'actif."])
  +BOX("💡 <strong>À retenir :</strong> sur Coinbase, l'essentiel des économies vient du choix <strong>Coinbase Advanced + virement SEPA</strong> "
       "au lieu de l'achat express par carte. Comparez aussi les <a href=\"/comparatifs/crypto-frais-bas.html\">plateformes crypto à frais bas</a>."),
 faq=[("Coinbase est-il cher ?","L'achat express de Coinbase est l'un de ses postes les plus chers. Sur Coinbase Advanced avec des ordres limites, les frais deviennent bien plus compétitifs."),
      ("Comment payer moins de frais sur Coinbase ?","Utilisez Coinbase Advanced, passez des ordres limites, déposez en euros par SEPA et regardez l'abonnement Coinbase One si vous tradez régulièrement."),
      ("Qu'est-ce que le spread Coinbase ?","C'est l'écart entre le prix d'achat et de vente affiché. Il s'ajoute aux frais et fait partie du coût réel d'une transaction.")])

add(slug="acheter-bitcoin-coinbase", brand="coinbase",
 title="Acheter du Bitcoin sur Coinbase : guide pas à pas 2026",
 desc="Comment acheter du Bitcoin (BTC) sur Coinbase en 2026 : inscription, vérification, dépôt SEPA, premier achat, frais et sécurité. Tutoriel étape par étape.",
 h1="Acheter du Bitcoin sur Coinbase : le guide pas à pas",
 subtitle="De l'inscription au premier achat de BTC : toutes les étapes, les frais et les bonnes pratiques.",
 leaf="Acheter du Bitcoin sur Coinbase",
 body=H2("etapes","Acheter du Bitcoin sur Coinbase en 5 étapes")
  +OL(["<strong>Créez votre compte</strong> Coinbase et validez votre identité (KYC).",
       "<strong>Déposez des euros</strong> par virement SEPA (le moyen le moins cher).",
       "Ouvrez <strong>Coinbase Advanced</strong> et sélectionnez la paire <strong>BTC/EUR</strong>.",
       "Passez un <strong>ordre limite</strong> (frais réduits) ou au marché pour un achat immédiat.",
       "Sécurisez : activez la <strong>double authentification (2FA)</strong> et envisagez un portefeuille externe."])
  +H2("frais","Combien coûte l'achat de Bitcoin sur Coinbase ?")
  +P("Le coût dépend de l'interface : l'achat express est plus cher que Coinbase Advanced. Pour le détail, voyez notre "
     "<a href=\"/guides/coinbase-frais.html\">page dédiée aux frais Coinbase</a>.")
  +H2("conserver","Conserver son Bitcoin en sécurité")
  +P("Vous pouvez laisser vos BTC sur la plateforme ou les transférer vers un <strong>portefeuille personnel</strong> (hardware wallet) pour une sécurité maximale. "
     "Coinbase propose aussi son propre wallet auto-hébergé."),
 faq=[("Quel est le minimum pour acheter du Bitcoin sur Coinbase ?","Le minimum est faible : vous pouvez acheter une fraction de Bitcoin, ce qui permet de commencer avec un petit montant."),
      ("Vaut-il mieux acheter du BTC sur Coinbase Advanced ?","Oui, Coinbase Advanced offre des frais bien inférieurs à l'achat express, surtout avec des ordres limites."),
      ("Faut-il sortir son Bitcoin de Coinbase ?","Pour de gros montants ou un horizon long, beaucoup transfèrent vers un portefeuille personnel (cold wallet) pour ne pas dépendre de la plateforme.")])

add(slug="acheter-ethereum-coinbase", brand="coinbase",
 title="Acheter de l'Ethereum sur Coinbase : guide 2026 étape par étape",
 desc="Comment acheter de l'Ethereum (ETH) sur Coinbase en 2026 : inscription, dépôt euros, ordre, frais, staking ETH et sécurité. Tutoriel pas à pas.",
 h1="Acheter de l'Ethereum (ETH) sur Coinbase : le guide",
 subtitle="Acheter de l'ETH au meilleur coût sur Coinbase, et savoir quoi en faire ensuite.",
 leaf="Acheter de l'Ethereum sur Coinbase",
 body=H2("etapes","Acheter de l'ETH sur Coinbase en 5 étapes")
  +OL(["<strong>Créez et vérifiez</strong> votre compte Coinbase (KYC).",
       "<strong>Déposez des euros</strong> par virement SEPA.",
       "Ouvrez <strong>Coinbase Advanced</strong> et choisissez la paire <strong>ETH/EUR</strong>.",
       "Passez un <strong>ordre limite</strong> pour réduire les frais, ou au marché pour acheter tout de suite.",
       "Activez la <strong>2FA</strong> et sécurisez votre accès."])
  +H2("staking","Staker son Ethereum sur Coinbase")
  +P("Coinbase permet de <strong>staker l'ETH</strong> pour percevoir une récompense. Le rendement n'est pas garanti et des conditions de déblocage s'appliquent — "
     "voyez notre <a href=\"/guides/coinbase-staking.html\">guide staking Coinbase</a>.")
  +H2("frais","Frais d'achat de l'ETH")
  +P("Comme pour le Bitcoin, privilégiez <strong>Coinbase Advanced</strong> pour réduire les frais. Détail sur notre "
     "<a href=\"/guides/coinbase-frais.html\">page frais Coinbase</a>."),
 faq=[("Peut-on acheter une fraction d'Ethereum sur Coinbase ?","Oui, vous pouvez acheter une petite fraction d'ETH et commencer avec un montant modeste."),
      ("Coinbase permet-il de staker l'Ethereum ?","Oui, Coinbase propose le staking d'ETH. Le rendement est variable et des conditions de déblocage s'appliquent."),
      ("Quel est le moyen le moins cher d'acheter de l'ETH sur Coinbase ?","Déposer en euros par SEPA puis acheter via Coinbase Advanced avec un ordre limite.")])

add(slug="coinbase-staking", brand="coinbase",
 title="Staking Coinbase 2026 : rendement, cryptos et risques",
 desc="Staking sur Coinbase en 2026 : comment ça marche, cryptos éligibles (ETH, SOL…), rendement estimé, fiscalité et risques. Le guide du staking Coinbase.",
 h1="Staking Coinbase : rendement, cryptos éligibles et risques",
 subtitle="Faire travailler ses crypto-actifs sur Coinbase : fonctionnement, rendement et points de vigilance.",
 leaf="Staking Coinbase",
 body=H2("cest-quoi","Le staking sur Coinbase, c'est quoi ?")
  +P("Le <strong>staking</strong> consiste à immobiliser certaines cryptos en preuve d'enjeu pour percevoir une récompense. "
     "Coinbase propose le staking directement depuis le compte, sans gérer soi-même la partie technique.")
  +H2("cryptos","Quelles cryptos peut-on staker ?")
  +P("La liste évolue, mais elle concerne généralement des actifs majeurs comme <strong>Ethereum (ETH)</strong>, <strong>Solana (SOL)</strong> "
     "ou <strong>Cardano (ADA)</strong>. Le rendement annuel estimé varie selon l'actif et les conditions de réseau.")
  +H2("risques","Rendement et risques à connaître")
  +UL(["Le <strong>rendement n'est pas garanti</strong> et fluctue.",
       "Certaines cryptos imposent une <strong>période de déblocage</strong> avant retrait.",
       "La <strong>valeur de l'actif</strong> peut baisser : le staking ne protège pas du risque de marché.",
       "Les <strong>récompenses de staking sont imposables</strong> : renseignez-vous sur votre fiscalité."])
  +BOX("💡 Le staking est une fonctionnalité avancée. Avant de vous lancer, lisez notre <a href=\"/avis/coinbase.html\">avis Coinbase</a>."),
 faq=[("Le staking Coinbase est-il sans risque ?","Non. Le rendement n'est pas garanti, l'actif peut perdre de la valeur et certaines cryptos imposent un délai de déblocage."),
      ("Quel rendement avec le staking Coinbase ?","Cela dépend de la crypto et des conditions de réseau. Les taux affichés sont des estimations annualisées variables, pas des promesses."),
      ("Les récompenses de staking sont-elles imposables ?","Oui, en général les récompenses de staking constituent un revenu imposable. Renseignez-vous sur votre situation fiscale.")])

add(slug="coinbase-retrait-euros", brand="coinbase",
 title="Retirer ses euros de Coinbase : délais, frais et SEPA 2026",
 desc="Comment retirer ses euros de Coinbase : virement SEPA, délais, frais, vérifications et blocages éventuels. Guide pour récupérer son argent sur Coinbase.",
 h1="Retirer ses euros de Coinbase : délais, frais et SEPA",
 subtitle="Récupérer son argent sur Coinbase : la procédure, les délais et les frais.",
 leaf="Retrait euros Coinbase",
 body=H2("procedure","Comment retirer ses euros de Coinbase")
  +OL(["Vendez vos crypto-actifs contre des <strong>euros</strong> sur Coinbase.",
       "Ajoutez et vérifiez votre <strong>compte bancaire (IBAN)</strong>.",
       "Lancez un <strong>retrait SEPA</strong> du montant souhaité.",
       "Réception généralement sous <strong>1 à 3 jours ouvrés</strong> selon votre banque."])
  +H2("frais-delais","Frais et délais")
  +P("Le retrait SEPA en euros est facturé à un <strong>montant fixe modique</strong>. Un premier retrait peut prendre un peu plus de temps "
     "(vérifications de sécurité).")
  +H2("conseils","Bonnes pratiques")
  +UL(["Vérifiez que votre <strong>identité est validée</strong> (KYC) pour éviter les blocages.",
       "Assurez-vous que l'<strong>IBAN est à votre nom</strong>.",
       "Activez la <strong>2FA</strong> pour sécuriser vos retraits."]),
 faq=[("Combien de temps pour retirer ses euros de Coinbase ?","Un virement SEPA arrive généralement en 1 à 3 jours ouvrés, selon votre banque et les vérifications."),
      ("Y a-t-il des frais pour retirer en euros sur Coinbase ?","Oui, un montant fixe modique s'applique au retrait SEPA, bien moins cher qu'un retrait par carte."),
      ("Pourquoi mon retrait Coinbase est-il bloqué ?","Souvent à cause d'une vérification d'identité incomplète, d'un IBAN non vérifié ou d'un délai de sécurité sur un premier retrait.")])

add(slug="coinbase-securite-fiabilite", brand="coinbase",
 title="Coinbase est-il fiable et sécurisé ? Avis sécurité 2026",
 desc="Coinbase est-il fiable ? Sécurité, société cotée au Nasdaq, régulation en France (PSAN/AMF), 2FA, stockage à froid. Notre analyse de la fiabilité de Coinbase.",
 h1="Coinbase est-il fiable et sécurisé ? Notre analyse",
 subtitle="Sécurité, régulation et réputation : ce qu'il faut savoir avant d'ouvrir un compte Coinbase.",
 leaf="Sécurité Coinbase",
 body=H2("reputation","Une plateforme cotée et reconnue")
  +P("Coinbase est l'une des plateformes crypto les plus connues au monde et la première à être <strong>cotée en bourse (Nasdaq)</strong>, "
     "ce qui implique un niveau de transparence financière élevé. C'est un argument fort en matière de fiabilité.")
  +H2("securite","Les dispositifs de sécurité")
  +UL(["<strong>Double authentification (2FA)</strong> et clés de sécurité.",
       "Stockage majoritaire des actifs en <strong>cold storage</strong> (hors ligne).",
       "<strong>Liste blanche d'adresses</strong> de retrait et alertes de connexion.",
       "Coffre-fort (vault) avec délai de retrait pour les gros montants."])
  +H2("regulation","Coinbase est-il régulé en France ?")
  +P("La régulation des plateformes crypto en France passe par le statut <strong>PSAN</strong> (enregistrement auprès de l'AMF). "
     "Vérifiez le statut à jour de l'acteur. Pour notre évaluation complète, voyez l'<a href=\"/avis/coinbase.html\">avis Coinbase</a>."),
 faq=[("Coinbase est-il une plateforme fiable ?","Coinbase est un acteur majeur, coté au Nasdaq, avec stockage à froid et 2FA. Aucun placement crypto n'est toutefois sans risque."),
      ("Coinbase est-il régulé en France ?","La régulation passe par le statut PSAN auprès de l'AMF. Vérifiez le statut à jour avant d'investir."),
      ("Mes cryptos sont-elles en sécurité sur Coinbase ?","Coinbase utilise le cold storage et la 2FA. Pour une sécurité maximale, vous pouvez transférer vos actifs vers un portefeuille personnel.")])

# génération (page() lit PAGES dans son module d'origine pour le maillage : on l'y injecte)
ns["PAGES"] = PAGES
os.makedirs("guides", exist_ok=True)
for d in PAGES:
    open(f"guides/{d['slug']}.html", "w", encoding="utf-8").write(page(d))
print("pages Coinbase générées:", len(PAGES))
for d in PAGES: print("  guides/"+d["slug"]+".html")
