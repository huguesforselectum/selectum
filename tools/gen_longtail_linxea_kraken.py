#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages long-tail (requêtes inexplorées) pour Kraken & Linxea -> guides/."""
import os, html, json
DATE="2026-06-11"
FONT="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"

BRAND={
 "kraken":dict(name="Kraken",logo="/assets/logos/kraken.png",cat="plateforme crypto",
   compar="/comparatifs/crypto.html",compar_label="Comparatif plateforme crypto",
   avis="/avis/kraken.html",promo="/code-promo/kraken.html",parr="/parrainage/kraken.html",
   go="/go/kraken",risk="Investir dans les crypto-actifs comporte un risque de perte en capital."),
 "linxea":dict(name="Linxea",logo="/assets/logos/linxea.png",cat="assurance-vie en ligne",
   compar="/comparatifs/assurance-vie.html",compar_label="Comparatif assurance-vie",
   avis="/avis/linxea.html",promo="/code-promo/linxea.html",parr="/parrainage/linxea.html",
   go="/go/linxea",risk="L'assurance-vie comporte un risque de perte en capital sur les unités de compte."),
}

def P(*ps): return "".join(f"<p>{x}</p>" for x in ps)
def H2(id,t): return f'<h2 id="{id}">{t}</h2>'
def OL(items): return "<ol>"+"".join(f"<li>{i}</li>" for i in items)+"</ol>"
def UL(items): return "<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"

# Chaque page: slug, brand, title, desc, h1, subtitle, breadcrumb_leaf, body(html), faq[(q,a)]
PAGES=[]
def add(**k): PAGES.append(k)

# ---------- KRAKEN ----------
add(slug="kraken-frais",brand="kraken",
 title="Frais Kraken 2026 : maker, taker, retrait et dépôt — le vrai coût",
 desc="Frais Kraken 2026 expliqués : trading maker/taker, frais de dépôt, retrait SEPA, conversion. Combien coûte vraiment Kraken et comment payer moins.",
 h1="Frais Kraken 2026 : combien coûte vraiment la plateforme ?",
 subtitle="Trading, dépôt, retrait, conversion : on décortique la grille tarifaire de Kraken.",
 leaf="Frais Kraken",
 body=H2("trading","Frais de trading Kraken (maker / taker)")
  +P("Comme la plupart des plateformes crypto, Kraken applique un modèle <strong>maker/taker</strong> : "
     "le « maker » (ordre limite qui apporte de la liquidité) paie moins cher que le « taker » (ordre au marché). "
     "Les frais sont <strong>dégressifs selon votre volume sur 30 jours</strong> : plus vous tradez, plus le taux baisse.")
  +P("L'interface <strong>Kraken Pro</strong> affiche des frais nettement inférieurs à l'achat simple « instant buy ». "
     "Si vous voulez réduire la note, privilégiez Kraken Pro et les ordres limites.")
  +H2("depot-retrait","Frais de dépôt et de retrait")
  +UL(["<strong>Dépôt SEPA en euros</strong> : généralement gratuit ou à coût très faible.",
       "<strong>Retrait SEPA</strong> : un montant fixe modique par virement.",
       "<strong>Retrait crypto</strong> : des frais de réseau (blockchain) s'appliquent et varient selon l'actif.",
       "<strong>Carte bancaire</strong> : l'achat par carte est plus cher que le virement."])
  +H2("reduire","Comment réduire ses frais sur Kraken")
  +OL(["Utiliser <strong>Kraken Pro</strong> plutôt que l'achat express.",
       "Passer des <strong>ordres limites (maker)</strong> plutôt qu'au marché.",
       "Alimenter le compte par <strong>virement SEPA</strong> plutôt que par carte.",
       "Regrouper ses achats pour franchir les paliers de volume."])
  +P("Pour comparer les frais avec d'autres acteurs, voyez notre "
     "<a href=\"/comparatifs/crypto-frais-bas.html\">comparatif des plateformes crypto à frais bas</a>."),
 faq=[("Kraken est-il cher ?","Sur Kraken Pro avec des ordres limites, les frais sont compétitifs et dégressifs selon le volume. L'achat « instant » est plus cher : c'est le poste à éviter pour économiser."),
      ("Quels sont les frais de retrait en euros sur Kraken ?","Le retrait SEPA en euros est facturé à un montant fixe modique. Les retraits en crypto supportent en plus les frais de réseau de la blockchain concernée."),
      ("Kraken Pro est-il moins cher que Kraken classique ?","Oui : Kraken Pro applique la grille maker/taker dégressive, bien plus avantageuse que l'achat instantané de l'interface simple.")])

add(slug="kraken-staking",brand="kraken",
 title="Staking Kraken 2026 : rendement, cryptos éligibles et risques",
 desc="Staking sur Kraken : comment ça marche, quelles cryptos (ETH, SOL, DOT…), rendement estimé, fiscalité et risques. Le guide complet du staking Kraken.",
 h1="Staking Kraken : rendement, cryptos éligibles et risques",
 subtitle="Faire travailler ses crypto-actifs sur Kraken : fonctionnement, rendement et points de vigilance.",
 leaf="Staking Kraken",
 body=H2("cest-quoi","Le staking sur Kraken, c'est quoi ?")
  +P("Le <strong>staking</strong> consiste à immobiliser certaines cryptomonnaies pour participer à la sécurisation d'un réseau "
     "(preuve d'enjeu) et percevoir une récompense. Kraken propose le staking sur plusieurs actifs directement depuis le compte, "
     "sans gérer soi-même la partie technique.")
  +H2("cryptos","Quelles cryptos peut-on staker ?")
  +P("La liste évolue, mais le staking concerne généralement des actifs majeurs en preuve d'enjeu comme "
     "<strong>Ethereum (ETH)</strong>, <strong>Solana (SOL)</strong>, <strong>Polkadot (DOT)</strong> ou encore <strong>Cardano (ADA)</strong>. "
     "Le rendement annuel estimé diffère selon la crypto et les conditions de réseau.")
  +H2("risques","Rendement et risques à connaître")
  +UL(["Le <strong>rendement n'est pas garanti</strong> et fluctue avec le réseau.",
       "Certaines cryptos imposent une <strong>période de déblocage</strong> avant de pouvoir retirer.",
       "La <strong>valeur de l'actif</strong> peut baisser : le rendement ne protège pas du risque de marché.",
       "Les <strong>récompenses de staking sont imposables</strong> : renseignez-vous sur votre fiscalité."])
  +P("Le staking est une fonctionnalité avancée : avant de vous lancer, lisez notre <a href=\"/avis/kraken.html\">avis Kraken</a>."),
 faq=[("Le staking Kraken est-il sans risque ?","Non. Le rendement n'est pas garanti, l'actif peut perdre de la valeur et certaines cryptos imposent un délai de déblocage. Le staking ne supprime pas le risque de marché."),
      ("Quel rendement espérer avec le staking sur Kraken ?","Cela dépend de la crypto stakée et des conditions du réseau. Les taux affichés sont des estimations annualisées variables, jamais des promesses."),
      ("Peut-on retirer ses cryptos stakées à tout moment ?","Selon l'actif. Certaines cryptos sont déblocables rapidement, d'autres imposent une période d'attente avant de récupérer les fonds.")])

add(slug="acheter-ethereum-kraken",brand="kraken",
 title="Acheter de l'Ethereum sur Kraken : guide étape par étape 2026",
 desc="Comment acheter de l'Ethereum (ETH) sur Kraken en 2026 : inscription, dépôt en euros, passer un ordre, frais et sécurité. Tutoriel pas à pas.",
 h1="Acheter de l'Ethereum (ETH) sur Kraken : le guide pas à pas",
 subtitle="De l'inscription au premier achat d'ETH : toutes les étapes, frais et bonnes pratiques.",
 leaf="Acheter de l'Ethereum sur Kraken",
 body=H2("etapes","Acheter de l'ETH sur Kraken en 5 étapes")
  +OL(["<strong>Créez votre compte</strong> sur Kraken et validez votre identité (KYC).",
       "<strong>Déposez des euros</strong> par virement SEPA (le moyen le moins cher).",
       "Ouvrez <strong>Kraken Pro</strong> et sélectionnez la paire <strong>ETH/EUR</strong>.",
       "Passez un <strong>ordre limite</strong> (frais maker réduits) ou au marché pour un achat immédiat.",
       "Sécurisez : activez la <strong>double authentification (2FA)</strong> et envisagez un portefeuille externe."])
  +H2("frais","Combien coûte l'achat d'Ethereum sur Kraken ?")
  +P("Le coût dépend de l'interface utilisée : l'achat express est plus cher que Kraken Pro. "
     "Pour le détail, consultez notre <a href=\"/guides/kraken-frais.html\">page dédiée aux frais Kraken</a>.")
  +H2("conserver","Conserver son Ethereum en sécurité")
  +P("Vous pouvez laisser vos ETH sur la plateforme ou les transférer vers un portefeuille personnel (hardware wallet) "
     "pour une sécurité maximale. Le staking d'ETH est également possible — voyez notre <a href=\"/guides/kraken-staking.html\">guide staking Kraken</a>."),
 faq=[("Quel est le montant minimum pour acheter de l'ETH sur Kraken ?","Le minimum est faible : vous pouvez acheter une fraction d'Ethereum, ce qui permet de commencer avec un petit montant."),
      ("Vaut-il mieux acheter de l'ETH sur Kraken Pro ?","Oui, Kraken Pro offre des frais bien inférieurs à l'achat instantané, surtout avec des ordres limites."),
      ("Peut-on staker l'Ethereum acheté sur Kraken ?","Oui, Kraken propose le staking d'ETH. Le rendement est variable et certaines conditions de déblocage s'appliquent.")])

add(slug="kraken-retrait-euros",brand="kraken",
 title="Retirer ses euros de Kraken : délais, frais et virement SEPA 2026",
 desc="Comment retirer ses euros de Kraken : virement SEPA, délais, frais, plafonds et vérifications. Guide pour récupérer son argent sur Kraken sans erreur.",
 h1="Retirer ses euros de Kraken : délais, frais et SEPA",
 subtitle="Récupérer son argent sur Kraken : la procédure complète, les délais et les frais.",
 leaf="Retrait euros Kraken",
 body=H2("procedure","Comment retirer ses euros de Kraken")
  +OL(["Vendez vos crypto-actifs contre des <strong>euros</strong> sur Kraken Pro.",
       "Ajoutez et vérifiez votre <strong>compte bancaire (IBAN)</strong>.",
       "Lancez un <strong>retrait SEPA</strong> du montant souhaité.",
       "Attendez la réception : le virement SEPA arrive généralement sous <strong>1 à 3 jours ouvrés</strong>."])
  +H2("frais-delais","Frais et délais de retrait")
  +P("Le retrait SEPA en euros est facturé à un <strong>montant fixe modique</strong>. Les délais dépendent de votre banque "
     "et des contrôles de sécurité éventuels. Un premier retrait peut prendre un peu plus de temps (vérifications).")
  +H2("conseils","Bonnes pratiques avant de retirer")
  +UL(["Vérifiez que votre <strong>identité est entièrement validée</strong> (KYC) pour éviter les blocages.",
       "Assurez-vous que l'<strong>IBAN est à votre nom</strong> : Kraken refuse les comptes tiers.",
       "Activez la <strong>2FA</strong> et la liste blanche d'adresses pour sécuriser vos retraits."]),
 faq=[("Combien de temps pour retirer ses euros de Kraken ?","Un virement SEPA arrive généralement en 1 à 3 jours ouvrés, selon votre banque et les vérifications de sécurité."),
      ("Y a-t-il des frais pour retirer en euros sur Kraken ?","Oui, un montant fixe modique s'applique au retrait SEPA. C'est bien moins cher qu'un retrait par carte."),
      ("Pourquoi mon retrait Kraken est-il bloqué ?","Le plus souvent à cause d'une vérification d'identité incomplète, d'un IBAN non vérifié ou d'un compte bancaire qui n'est pas à votre nom.")])

add(slug="kraken-securite-fiabilite",brand="kraken",
 title="Kraken est-il fiable et sécurisé ? Avis sécurité 2026",
 desc="Kraken est-il fiable ? Sécurité, preuve de réserves, 2FA, régulation en France (PSAN/AMF), historique. Notre analyse de la fiabilité de Kraken.",
 h1="Kraken est-il fiable et sécurisé ? Notre analyse",
 subtitle="Sécurité, régulation et réputation : ce qu'il faut savoir avant d'ouvrir un compte Kraken.",
 leaf="Sécurité Kraken",
 body=H2("historique","Une réputation établie")
  +P("Kraken est l'un des plus anciens acteurs du marché crypto et figure parmi les plateformes réputées pour leur "
     "<strong>sécurité</strong>. Ancienneté et absence de piratage majeur de grande ampleur jouent en sa faveur.")
  +H2("securite","Les dispositifs de sécurité")
  +UL(["<strong>Double authentification (2FA)</strong> et clés de sécurité.",
       "<strong>Liste blanche d'adresses</strong> de retrait et verrou global du compte.",
       "<strong>Preuve de réserves</strong> : Kraken publie des audits prouvant la détention des fonds clients.",
       "Stockage majoritaire des actifs en <strong>cold storage</strong> (hors ligne)."])
  +H2("regulation","Kraken est-il régulé en France ?")
  +P("La régulation des plateformes crypto en France passe par le statut <strong>PSAN</strong> (enregistrement auprès de l'AMF). "
     "Vérifiez toujours le statut à jour de l'acteur. Pour notre évaluation complète, voyez l'<a href=\"/avis/kraken.html\">avis Kraken</a>."),
 faq=[("Kraken est-il une plateforme fiable ?","Kraken est un acteur ancien et réputé pour sa sécurité, avec preuve de réserves et stockage à froid. Aucun placement crypto n'est toutefois sans risque."),
      ("Kraken est-il régulé en France ?","La régulation passe par le statut PSAN auprès de l'AMF. Vérifiez le statut à jour avant d'investir."),
      ("Mes cryptos sont-elles en sécurité sur Kraken ?","Kraken utilise le cold storage et la 2FA. Pour une sécurité maximale, vous pouvez aussi transférer vos actifs vers un portefeuille personnel.")])

# ---------- LINXEA ----------
add(slug="linxea-spirit-2",brand="linxea",
 title="Linxea Spirit 2 : avis, frais et supports (SCPI, ETF) 2026",
 desc="Linxea Spirit 2 en 2026 : avis, frais de gestion, SCPI sans frais d'entrée, ETF, fonds euros. Tout sur le contrat phare de Linxea avant de souscrire.",
 h1="Linxea Spirit 2 : avis, frais et supports d'investissement",
 subtitle="Le contrat d'assurance-vie phare de Linxea passé au crible : frais, SCPI, ETF et fonds euros.",
 leaf="Linxea Spirit 2",
 body=H2("presentation","Linxea Spirit 2, c'est quoi ?")
  +P("<strong>Linxea Spirit 2</strong> est l'un des contrats d'assurance-vie en ligne les plus réputés du marché, "
     "apprécié pour ses <strong>frais réduits</strong> et sa large gamme de supports. Il est assuré par un acteur établi et "
     "se distingue notamment sur l'accès aux <strong>SCPI</strong> et aux <strong>ETF</strong>.")
  +H2("frais","Les frais de Linxea Spirit 2")
  +UL(["<strong>0 % de frais d'entrée</strong> et 0 % de frais de versement.",
       "Des <strong>frais de gestion annuels</strong> parmi les plus bas du marché sur les unités de compte.",
       "<strong>Aucun frais d'arbitrage</strong> en ligne dans la plupart des cas.",
       "Accès aux <strong>SCPI à conditions avantageuses</strong> (souvent 100 % de la valeur de retrait)."])
  +H2("supports","SCPI, ETF et fonds euros")
  +P("Le contrat donne accès à un fonds en euros, à de nombreuses <strong>SCPI</strong>, à des <strong>ETF/trackers</strong> à frais bas "
     "et à une large sélection d'unités de compte. C'est ce qui en fait un favori des investisseurs autonomes. "
     "Voyez aussi notre <a href=\"/guides/linxea-etf.html\">guide des ETF chez Linxea</a> et notre <a href=\"/guides/linxea-scpi.html\">guide SCPI Linxea</a>."),
 faq=[("Linxea Spirit 2 a-t-il des frais d'entrée ?","Non. Linxea Spirit 2 applique 0 % de frais d'entrée et 0 % de frais de versement, ce qui est un de ses gros atouts."),
      ("Peut-on investir en SCPI avec Linxea Spirit 2 ?","Oui, le contrat propose un large choix de SCPI, souvent à des conditions de retrait avantageuses."),
      ("Linxea Spirit 2 convient-il aux débutants ?","Oui, à condition d'être à l'aise avec la gestion libre. Les profils prudents peuvent privilégier le fonds en euros.")])

add(slug="linxea-frais",brand="linxea",
 title="Frais Linxea 2026 : gestion, versement, arbitrage — le détail",
 desc="Frais Linxea expliqués : 0 % d'entrée, frais de gestion, arbitrage, frais des SCPI et ETF. Combien coûte vraiment une assurance-vie Linxea en 2026.",
 h1="Frais Linxea : le détail complet des coûts",
 subtitle="Entrée, versement, gestion, arbitrage : tout ce que vous payez (et ne payez pas) chez Linxea.",
 leaf="Frais Linxea",
 body=H2("entree","0 % de frais d'entrée et de versement")
  +P("L'un des grands arguments de Linxea : <strong>aucun frais d'entrée ni de versement</strong>. "
     "Tout l'argent que vous versez est investi, contrairement à de nombreux contrats bancaires qui prélèvent 2 à 5 % à l'entrée.")
  +H2("gestion","Frais de gestion annuels")
  +P("Les <strong>frais de gestion</strong> sur les unités de compte comptent parmi les plus bas du marché. "
     "Le fonds en euros a ses propres frais de gestion, distincts. Ces frais réduits améliorent mécaniquement votre performance nette sur le long terme.")
  +H2("autres","Arbitrage, SCPI et ETF")
  +UL(["<strong>Arbitrages en ligne gratuits</strong> dans la plupart des cas.",
       "<strong>SCPI</strong> : Linxea négocie souvent un retrait à 100 % de la valeur, ce qui réduit le coût d'entrée.",
       "<strong>ETF</strong> : frais de support très faibles, idéaux pour une stratégie passive."])
  +P("Comparez avec les autres contrats dans notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Linxea prend-il des frais d'entrée ?","Non. Linxea applique 0 % de frais d'entrée et 0 % de frais de versement sur ses contrats."),
      ("Quels sont les frais de gestion chez Linxea ?","Les frais de gestion annuels sur unités de compte sont parmi les plus bas du marché. Le fonds en euros a des frais de gestion distincts."),
      ("Les arbitrages sont-ils payants chez Linxea ?","Dans la plupart des cas, les arbitrages réalisés en ligne sont gratuits.")])

add(slug="linxea-scpi",brand="linxea",
 title="SCPI via Linxea 2026 : liste, frais et rendement en assurance-vie",
 desc="Investir en SCPI via l'assurance-vie Linxea : avantages, frais réduits, retrait à 100 %, fiscalité et points de vigilance. Le guide SCPI Linxea 2026.",
 h1="Investir en SCPI via Linxea : le guide complet",
 subtitle="Pierre-papier en assurance-vie : pourquoi Linxea est un canal apprécié pour les SCPI.",
 leaf="SCPI Linxea",
 body=H2("pourquoi","Pourquoi loger ses SCPI dans une assurance-vie Linxea ?")
  +P("Acheter des <strong>SCPI</strong> (pierre-papier) au sein d'une assurance-vie comme Linxea cumule deux avantages : "
     "la <strong>fiscalité avantageuse de l'assurance-vie</strong> et des <strong>frais d'entrée réduits</strong>. "
     "Linxea négocie souvent un retrait à <strong>100 % de la valeur</strong>, ce qui supprime une partie du coût habituel des SCPI.")
  +H2("avantages","Les avantages")
  +UL(["<strong>Frais d'entrée réduits</strong> par rapport à l'achat en direct.",
       "<strong>Fiscalité de l'assurance-vie</strong> après 8 ans (abattement annuel).",
       "<strong>Mutualisation</strong> : accès à un parc immobilier diversifié dès quelques centaines d'euros.",
       "<strong>Liquidité</strong> améliorée via le contrat (rachat partiel)."])
  +H2("vigilance","Points de vigilance")
  +P("Les SCPI restent un placement de <strong>long terme</strong> : la valeur des parts et les revenus ne sont pas garantis, "
     "et une part des loyers peut être conservée par l'assureur. Diversifiez et gardez un horizon de plusieurs années. "
     "Voyez notre <a href=\"/avis/linxea.html\">avis Linxea</a> pour le détail."),
 faq=[("Peut-on acheter des SCPI avec Linxea ?","Oui, les contrats Linxea donnent accès à de nombreuses SCPI, souvent avec un retrait à 100 % de la valeur."),
      ("Quel est l'avantage des SCPI en assurance-vie ?","On cumule la fiscalité avantageuse de l'assurance-vie et des frais d'entrée réduits par rapport à l'achat en direct."),
      ("Les SCPI sont-elles sans risque chez Linxea ?","Non. La valeur des parts et les revenus ne sont pas garantis. Les SCPI sont un placement de long terme.")])

add(slug="linxea-etf",brand="linxea",
 title="ETF chez Linxea 2026 : trackers, frais bas et gestion passive",
 desc="Investir en ETF (trackers) via l'assurance-vie Linxea : sélection, frais réduits, MSCI World, stratégie passive et fiscalité. Le guide ETF Linxea 2026.",
 h1="Investir en ETF chez Linxea : trackers et gestion passive",
 subtitle="Bâtir un portefeuille passif à frais bas dans une assurance-vie Linxea.",
 leaf="ETF Linxea",
 body=H2("pourquoi","Pourquoi des ETF dans une assurance-vie Linxea ?")
  +P("Les <strong>ETF</strong> (ou trackers) répliquent un indice (MSCI World, S&amp;P 500, CAC 40…) à <strong>frais très faibles</strong>. "
     "Logés dans une assurance-vie Linxea, ils profitent de la <strong>fiscalité avantageuse après 8 ans</strong> et de l'absence de frais d'entrée.")
  +H2("selection","Une sélection d'ETF à frais bas")
  +P("Les contrats Linxea référencent des ETF actions monde, zones géographiques, obligataires et thématiques. "
     "Pour une stratégie passive « lazy », un <strong>ETF World</strong> en cœur de portefeuille reste l'approche la plus simple.")
  +H2("strategie","Stratégie passive : les principes")
  +UL(["<strong>Diversifier</strong> via un indice large plutôt que des paris individuels.",
       "<strong>Investir régulièrement</strong> (versements programmés) pour lisser les points d'entrée.",
       "<strong>Minimiser les frais</strong> : ETF à faible coût + frais de gestion réduits Linxea.",
       "<strong>Garder le cap</strong> sur le long terme malgré la volatilité."]),
 faq=[("Peut-on acheter des ETF chez Linxea ?","Oui, les contrats Linxea référencent de nombreux ETF (actions monde, zones, obligataires, thématiques) à frais bas."),
      ("Quel ETF choisir chez Linxea pour débuter ?","Un ETF World (type MSCI World) en cœur de portefeuille est l'option la plus simple pour une stratégie passive diversifiée."),
      ("Les ETF en assurance-vie sont-ils fiscalement avantageux ?","Oui : logés en assurance-vie, ils bénéficient de l'abattement fiscal après 8 ans de détention du contrat.")])

add(slug="linxea-retrait-fiscalite",brand="linxea",
 title="Retrait Linxea 2026 : délais et fiscalité de l'assurance-vie",
 desc="Retrait (rachat) sur assurance-vie Linxea : délais, fiscalité avant et après 8 ans, abattement, prélèvements sociaux. Comment récupérer son argent chez Linxea.",
 h1="Retrait Linxea : délais et fiscalité de l'assurance-vie",
 subtitle="Rachat partiel ou total : ce que vous récupérez, en combien de temps et avec quelle fiscalité.",
 leaf="Retrait & fiscalité Linxea",
 body=H2("comment","Comment retirer de l'argent chez Linxea")
  +P("On parle de <strong>rachat</strong> (partiel ou total). La demande se fait <strong>en ligne</strong> depuis votre espace Linxea. "
     "Les fonds sont ensuite virés sur votre compte bancaire, généralement sous <strong>quelques jours ouvrés</strong> "
     "(le délai peut être plus long si des SCPI ou supports particuliers sont concernés).")
  +H2("fiscalite","La fiscalité du retrait")
  +P("L'assurance-vie n'est imposée que sur la <strong>part de gains</strong> contenue dans le retrait, pas sur le capital versé. "
     "La fiscalité dépend de l'ancienneté du contrat :")
  +UL(["<strong>Avant 8 ans</strong> : les gains sont soumis au prélèvement forfaitaire (ou au barème), plus prélèvements sociaux.",
       "<strong>Après 8 ans</strong> : abattement annuel de <strong>4 600 €</strong> (9 200 € pour un couple) sur les gains, puis taux réduit.",
       "<strong>Prélèvements sociaux</strong> (17,2 %) dus dans tous les cas sur les gains."])
  +H2("conseil","Le bon réflexe")
  +P("Pour optimiser, beaucoup d'épargnants <strong>attendent les 8 ans</strong> avant les gros retraits afin de profiter de l'abattement. "
     "Ceci n'est pas un conseil personnalisé : votre situation prime. Voyez notre <a href=\"/avis/linxea.html\">avis Linxea</a>."),
 faq=[("Combien de temps pour récupérer son argent chez Linxea ?","Un rachat est généralement viré sous quelques jours ouvrés. Le délai peut s'allonger si des SCPI ou supports spécifiques sont vendus."),
      ("Comment est imposé un retrait d'assurance-vie Linxea ?","Seuls les gains sont imposés. Après 8 ans, un abattement annuel de 4 600 € (9 200 € pour un couple) s'applique, plus les prélèvements sociaux."),
      ("Peut-on faire un retrait partiel chez Linxea ?","Oui, le rachat partiel permet de retirer une partie de l'épargne tout en gardant le contrat ouvert et son antériorité fiscale.")])

add(slug="assurance-vie-sans-frais-entree",brand="linxea",
 title="Assurance-vie sans frais d'entrée 2026 : le comparatif",
 desc="Les meilleures assurances-vie sans frais d'entrée en 2026 : pourquoi ça change tout, comment choisir et où Linxea se positionne. Guide et comparatif.",
 h1="Assurance-vie sans frais d'entrée : pourquoi c'est essentiel",
 subtitle="Les frais d'entrée grignotent votre capital dès le départ. Voici comment les éviter.",
 leaf="Assurance-vie sans frais d'entrée",
 body=H2("pourquoi","Pourquoi fuir les frais d'entrée")
  +P("De nombreux contrats bancaires prélèvent <strong>2 à 5 % de frais d'entrée</strong> sur chaque versement. "
     "Sur 10 000 € versés, c'est jusqu'à 500 € qui ne travaillent jamais pour vous. Les <strong>contrats en ligne</strong> comme "
     "ceux de <strong>Linxea</strong> appliquent <strong>0 % de frais d'entrée</strong> : 100 % de votre argent est investi.")
  +H2("criteres","Comment choisir une assurance-vie sans frais d'entrée")
  +UL(["<strong>0 % de frais d'entrée et de versement</strong> (non négociable).",
       "<strong>Frais de gestion réduits</strong> sur les unités de compte.",
       "<strong>Large choix de supports</strong> : fonds euros, ETF, SCPI.",
       "<strong>Arbitrages gratuits</strong> en ligne."])
  +H2("positionnement","Où se situe Linxea")
  +P("Linxea fait partie des références sur ce créneau : 0 % d'entrée, frais de gestion bas et accès SCPI/ETF. "
     "Comparez l'ensemble des contrats dans notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a> "
     "et lisez notre <a href=\"/guides/linxea-frais.html\">détail des frais Linxea</a>."),
 faq=[("Quelles assurances-vie n'ont pas de frais d'entrée ?","Les contrats en ligne comme ceux de Linxea appliquent 0 % de frais d'entrée et de versement, contrairement à beaucoup de contrats bancaires."),
      ("Les frais d'entrée sont-ils vraiment importants ?","Oui : 2 à 5 % prélevés à chaque versement réduisent directement le capital investi et donc la performance à long terme."),
      ("Linxea est-il sans frais d'entrée ?","Oui, Linxea applique 0 % de frais d'entrée et de versement sur ses contrats d'assurance-vie.")])

def faq_ld(faq):
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)

def page(d):
    b=BRAND[d["brand"]]; url=f"https://selectum.fr/guides/{d['slug']}.html"
    title=html.escape(d["title"]); desc=html.escape(d["desc"])
    art_ld=json.dumps({"@context":"https://schema.org","@type":"Article","headline":d["title"],"description":d["desc"],
        "author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum",
        "logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},
        "datePublished":DATE,"dateModified":DATE,"mainEntityOfPage":url},ensure_ascii=False)
    bc_ld=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
        {"@type":"ListItem","position":2,"name":"Guides","item":"https://selectum.fr/guides/"},
        {"@type":"ListItem","position":3,"name":d["leaf"],"item":url}]},ensure_ascii=False)
    faq_html='<div class="faq"><h2>❓ Questions fréquentes</h2>'+''.join(
        f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>'
        for q,a in d["faq"])+'</div>'
    # siblings same brand for maillage
    sibs=[p for p in PAGES if p["brand"]==d["brand"] and p["slug"]!=d["slug"]][:3]
    rel=''.join(f'<a href="/guides/{s["slug"]}.html" class="rel-chip">{html.escape(s["leaf"])} →</a>' for s in sibs)
    rel+=f'<a href="{b["compar"]}" class="rel-chip">{b["compar_label"]} →</a>'
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="article"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{art_ld}</script>
<script type="application/ld+json">{faq_ld(d["faq"])}</script>
<script type="application/ld+json">{bc_ld}</script>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="{b['compar']}" class="btn-primary">Voir le comparatif →</a></div>
</div></div></header>
<div class="brand-hero"><div class="container-article">
  <div class="brand-hero-logo"><img src="{b['logo']}" alt="{html.escape(b['name'])}"></div>
  <div class="brand-hero-text">
    <div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / <a href="/guides/" style="color:rgba(255,255,255,.8)">Guides</a> / {html.escape(d['leaf'])}</div>
    <h1>{html.escape(d['h1'])}</h1>
    <p class="subtitle">{html.escape(d['subtitle'])}</p>
    <p class="updated">🗓️ Mis à jour le 11 juin 2026</p>
  </div></div></div>
<div class="container-article"><div class="article-layout" style="grid-template-columns: 1fr 300px;"><main class="article-body">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. {html.escape(b['risk'])}</div>
  {d['body']}
  {faq_html}
  <div class="rel-links"><h2>À lire aussi</h2><div class="rel-list">{rel}</div></div>
</main>
<aside class="sidebar">
  <div class="sidebar-cta"><h4>👉 {html.escape(b['name'])}</h4><p>Découvrez l'offre {html.escape(b['name'])} du moment.</p><a href="{b['go']}" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
  <div class="sidebar-card"><h4>🔗 À lire aussi</h4><ul class="sidebar-toc"><li><a href="{b['avis']}">Avis {html.escape(b['name'])} →</a></li><li><a href="{b['promo']}">Code promo {html.escape(b['name'])} →</a></li><li><a href="{b['parr']}">Parrainage {html.escape(b['name'])} →</a></li><li><a href="{b['compar']}">{html.escape(b['compar_label'])} →</a></li></ul></div>
</aside>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

os.makedirs("guides",exist_ok=True)
n=0
for d in PAGES:
    open(f"guides/{d['slug']}.html","w",encoding="utf-8").write(page(d))
    n+=1
print("pages générées:",n)
for d in PAGES: print("  guides/"+d["slug"]+".html")
