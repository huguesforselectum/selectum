#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guides informationnels a forte intention sur les verticales principales (autorite thematique)."""
import os, html, json
FONT="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
D="15 juin 2026"

def P(*x): return "".join(f"<p>{p}</p>" for p in x)
def H2(i,t): return f'<h2 id="{i}">{t}</h2>'
def UL(x): return "<ul>"+"".join(f"<li>{i}</li>" for i in x)+"</ul>"
def OL(x): return "<ol>"+"".join(f"<li>{i}</li>" for i in x)+"</ol>"
def BOX(t): return f'<div class="highlight-box"><p>{t}</p></div>'

# liens silo par categorie (comparatif + 3 Tier 1 code-promo + ancres variees)
SILO={
 "crypto":[("/comparatifs/crypto.html","Comparatif des applications crypto"),("/code-promo/coinbase.html","Code promo Coinbase"),("/code-promo/bitpanda.html","Offres Bitpanda"),("/code-promo/kraken.html","Code promo Kraken")],
 "bourse":[("/comparatifs/trading-bourse.html","Comparatif des courtiers en bourse"),("/code-promo/xtb.html","Code promo XTB"),("/code-promo/trade-republic.html","Offres Trade Republic"),("/code-promo/etoro.html","Code promo eToro")],
 "banque":[("/comparatifs/banque-en-ligne.html","Comparatif des banques en ligne"),("/code-promo/n26.html","Code promo N26"),("/code-promo/revolut.html","Offres Revolut"),("/code-promo/boursobank.html","Code promo BoursoBank")],
 "compte-pro":[("/comparatifs/comptes-pro.html","Comparatif des comptes pro"),("/code-promo/qonto.html","Code promo Qonto"),("/code-promo/shine.html","Offres Shine"),("/code-promo/finom.html","Code promo Finom")],
 "hebergement":[("/comparatifs/hebergement-web.html","Comparatif des hébergeurs web"),("/code-promo/ionos.html","Code promo IONOS"),("/code-promo/hostinger.html","Offres Hostinger"),("/code-promo/o2switch.html","Code promo o2switch")],
 "epargne":[("/comparatifs/assurance-vie.html","Comparatif assurance-vie"),("/code-promo/linxea.html","Code promo Linxea"),("/code-promo/nalo.html","Offres Nalo"),("/code-promo/yomoni.html","Code promo Yomoni")],
 "vpn":[("/comparatifs/vpn.html","Comparatif des VPN"),("/code-promo/expressvpn.html","Code promo ExpressVPN"),("/code-promo/nordvpn.html","Offres NordVPN"),("/code-promo/surfshark.html","Code promo Surfshark")],
}
CATLABEL={"crypto":"Crypto","bourse":"Bourse","banque":"Banque","compte-pro":"Compte pro","hebergement":"Hébergement","epargne":"Épargne","vpn":"Tech"}

G=[]
def add(**k): G.append(k)

add(slug="comment-acheter-cryptomonnaies",cat="crypto",
 title="Comment acheter des cryptomonnaies en 2026 : guide pour débuter",
 desc="Comment acheter des cryptomonnaies en 2026 quand on débute : choisir une application, créer un compte, premier achat, sécurité et fiscalité. Le guide pas à pas.",
 h1="Comment acheter des cryptomonnaies en 2026 (guide débutant)",
 lead="Acheter du Bitcoin ou de l'Ethereum n'a jamais été aussi simple, mais quelques réflexes évitent les erreurs coûteuses. Voici la méthode étape par étape.",
 body=H2("etapes","Acheter sa première crypto en 5 étapes")
  +OL(["<strong>Choisissez une application crypto</strong> régulée et adaptée à votre niveau (voir notre comparatif).",
       "<strong>Créez un compte</strong> et validez votre identité (vérification KYC, 100 % en ligne).",
       "<strong>Déposez des euros</strong> par virement SEPA (moins cher que la carte).",
       "<strong>Passez votre premier achat</strong> via l'interface « pro/advanced » pour réduire les frais.",
       "<strong>Sécurisez</strong> : activez la double authentification (2FA) et, pour de gros montants, un portefeuille externe."])
  +H2("frais","Attention aux frais")
  +P("Le poste le plus cher n'est pas le bonus de bienvenue mais les <strong>frais d'achat</strong> : l'achat « instantané » et la carte bancaire coûtent bien plus que l'interface pro + virement SEPA. Notre <a href=\"/etudes/barometre-frais-crypto.html\">baromètre des frais crypto</a> détaille les écarts.")
  +H2("securite","Sécuriser ses cryptos")
  +UL(["Activez la <strong>2FA</strong> et une liste blanche d'adresses de retrait.",
       "Pour de gros montants, transférez vers un <strong>portefeuille personnel</strong> (hardware wallet).",
       "Ne partagez jamais votre phrase de récupération."])
  +H2("fiscalite","Et la fiscalité ?")
  +P("En France, les <strong>plus-values</strong> réalisées lors de la conversion crypto → euros sont imposables. Conservez l'historique de vos transactions ; des outils dédiés facilitent la déclaration.")
  +BOX("💡 Pour débuter simplement, regardez notre <a href=\"/comparatifs/crypto-debutant.html\">sélection des plateformes crypto pour débutants</a>."),
 faq=[("Quel est le montant minimum pour acheter de la crypto ?","Très faible : la plupart des applications permettent d'acheter une fraction de crypto, vous pouvez commencer avec quelques euros."),
      ("Quelle est la meilleure application pour débuter ?","Coinbase et Bitpanda sont réputés simples pour débuter ; Kraken et Binance offrent des frais plus bas. Voir notre comparatif."),
      ("Faut-il déclarer ses cryptos aux impôts ?","Oui, les comptes détenus à l'étranger et les plus-values de cession sont à déclarer en France.")]),

add(slug="declarer-cryptomonnaies-impots",cat="crypto",
 title="Déclarer ses cryptomonnaies aux impôts en France (2026)",
 desc="Comment déclarer ses cryptomonnaies aux impôts en France en 2026 : plus-values, flat tax, comptes à l'étranger, seuils et outils. Le guide clair pour ne rien oublier.",
 h1="Déclarer ses cryptomonnaies aux impôts en France",
 lead="La fiscalité crypto fait peur, mais les règles sont plus simples qu'on ne le croit pour un particulier. Voici l'essentiel — sans jargon.",
 body=H2("principe","Ce qui est imposable (et ce qui ne l'est pas)")
  +P("Tant que vos cryptos restent en cryptos, il ne se passe rien fiscalement. L'imposition se déclenche lors d'une <strong>cession contre de la monnaie « classique »</strong> (euros) ou un achat de bien/service. Les échanges crypto-crypto ne sont en principe pas imposés au moment où ils ont lieu.")
  +H2("taux","Quel taux d'imposition ?")
  +P("Pour un particulier, les plus-values relèvent en général du <strong>prélèvement forfaitaire unique (flat tax) de 30 %</strong> (impôt + prélèvements sociaux). Une option pour le barème progressif est possible selon les situations.")
  +H2("comptes","Déclarer ses comptes à l'étranger")
  +P("Les <strong>comptes d'actifs numériques ouverts à l'étranger</strong> (la plupart des plateformes) doivent être déclarés chaque année, même sans plus-value. L'oubli expose à une amende.")
  +BOX("💡 Ceci est une information générale, pas un conseil fiscal personnalisé. En cas de doute, rapprochez-vous d'un professionnel ou de l'administration fiscale.")
  +H2("outils","Outils pour s'y retrouver")
  +P("Des logiciels de calcul de plus-values crypto agrègent vos transactions et génèrent les montants à reporter. Gardez toujours l'<strong>historique complet</strong> de vos opérations."),
 faq=[("Les échanges crypto-crypto sont-ils imposés ?","En principe, l'imposition intervient lors de la conversion en euros (ou achat de bien/service), pas lors d'un simple échange crypto-crypto."),
      ("Quel est le taux d'imposition des cryptos ?","Le plus souvent la flat tax de 30 % pour un particulier, avec option possible pour le barème selon les cas."),
      ("Dois-je déclarer si je n'ai pas vendu ?","Vous devez déclarer vos comptes ouverts à l'étranger même sans cession. Les plus-values ne sont imposées qu'en cas de cession.")]),

add(slug="comment-investir-en-bourse-debutant",cat="bourse",
 title="Comment investir en bourse quand on débute (2026)",
 desc="Comment investir en bourse en 2026 quand on débute : PEA ou CTO, ETF, courtier, montant de départ, erreurs à éviter. Le guide simple pour se lancer sereinement.",
 h1="Comment investir en bourse quand on débute",
 lead="Pas besoin d'être expert ni riche pour commencer à investir en bourse. Avec une méthode simple et passive, on évite l'essentiel des erreurs.",
 body=H2("enveloppe","Étape 1 : choisir son enveloppe (PEA ou CTO)")
  +P("Le <strong>PEA</strong> offre une fiscalité avantageuse après 5 ans mais se limite aux actions européennes (et ETF éligibles). Le <strong>compte-titres (CTO)</strong> est plus flexible (marchés mondiaux) mais fiscalisé au fil de l'eau. Beaucoup de débutants commencent par un PEA.")
  +H2("etf","Étape 2 : privilégier les ETF")
  +P("Plutôt que de parier sur des actions individuelles, un <strong>ETF</strong> (tracker) réplique un indice large (MSCI World, S&amp;P 500) à frais très bas. C'est l'approche la plus simple et diversifiée pour débuter.")
  +H2("courtier","Étape 3 : choisir un courtier")
  +P("Comparez les <strong>frais d'ordre</strong>, l'éligibilité PEA et l'ergonomie. Voir notre <a href=\"/comparatifs/trading-bourse.html\">comparatif des courtiers en bourse</a> et notre guide <a href=\"/comparatifs/courtier-etf.html\">meilleur courtier ETF</a>.")
  +H2("methode","Étape 4 : la méthode qui marche")
  +UL(["<strong>Investir régulièrement</strong> (versements programmés) pour lisser les points d'entrée.",
       "<strong>Diversifier</strong> via un ETF World en cœur de portefeuille.",
       "<strong>Garder le cap</strong> sur le long terme malgré la volatilité.",
       "<strong>Minimiser les frais</strong>, qui grignotent la performance sur 20 ans."])
  +BOX("⚠️ Investir comporte un risque de perte en capital. N'investissez que ce que vous pouvez immobiliser sur le long terme."),
 faq=[("Combien faut-il pour commencer à investir en bourse ?","On peut commencer avec quelques dizaines d'euros grâce aux ETF et aux courtiers sans minimum élevé."),
      ("PEA ou compte-titres pour débuter ?","Le PEA est souvent privilégié pour son avantage fiscal après 5 ans ; le CTO offre plus de flexibilité (marchés mondiaux)."),
      ("Quel ETF choisir pour débuter ?","Un ETF World (type MSCI World) en cœur de portefeuille est l'option la plus simple et diversifiée.")]),

add(slug="pea-ou-compte-titres",cat="bourse",
 title="PEA ou compte-titres (CTO) : lequel choisir en 2026 ?",
 desc="PEA ou compte-titres en 2026 : fiscalité, plafonds, actions éligibles, souplesse. Comparatif clair pour choisir la bonne enveloppe selon votre projet d'investissement.",
 h1="PEA ou compte-titres (CTO) : lequel choisir ?",
 lead="Les deux enveloppes permettent d'investir en bourse, mais leur fiscalité et leur souplesse diffèrent. Voici comment trancher selon votre objectif.",
 body=H2("pea","Le PEA en bref")
  +UL(["<strong>Fiscalité avantageuse</strong> : exonération d'impôt sur les gains après 5 ans (hors prélèvements sociaux).",
       "<strong>Plafond</strong> de versement de 150 000 €.",
       "Limité aux <strong>actions européennes</strong> et ETF éligibles.",
       "Idéal pour une stratégie actions/ETF long terme."])
  +H2("cto","Le compte-titres (CTO) en bref")
  +UL(["<strong>Aucune limite</strong> de versement ni de marché : actions monde, ETF, obligations…",
       "<strong>Fiscalité au fil de l'eau</strong> : flat tax de 30 % sur les gains à chaque cession.",
       "Plus souple, mais moins avantageux fiscalement sur le long terme."])
  +H2("choisir","Lequel choisir ?")
  +P("Pour une stratégie <strong>actions/ETF européens à long terme</strong>, le PEA est souvent le meilleur point de départ. Pour accéder aux <strong>marchés mondiaux</strong> ou à des produits non éligibles au PEA, le CTO s'impose. Beaucoup d'investisseurs ont les deux.")
  +BOX("💡 Comparez les courtiers proposant le PEA dans notre <a href=\"/comparatifs/trading-bourse.html\">comparatif bourse</a>."),
 faq=[("Peut-on avoir un PEA et un CTO en même temps ?","Oui, c'est même courant : le PEA pour les actions/ETF européens long terme, le CTO pour le reste."),
      ("Quel est l'avantage fiscal du PEA ?","Après 5 ans, les gains sont exonérés d'impôt sur le revenu (les prélèvements sociaux restent dus)."),
      ("Peut-on investir en actions américaines avec un PEA ?","Non directement : le PEA est limité aux titres européens. Pour les actions US, il faut un compte-titres.")]),

add(slug="neobanque-ou-banque-traditionnelle",cat="banque",
 title="Néobanque ou banque traditionnelle : que choisir en 2026 ?",
 desc="Néobanque ou banque traditionnelle en 2026 : frais, services, crédit, dépôt d'espèces, accompagnement. Comparatif clair pour choisir le compte adapté à votre profil.",
 h1="Néobanque ou banque traditionnelle : que choisir ?",
 lead="Les néobanques séduisent par leurs frais réduits et leur appli, mais les banques classiques gardent des atouts. Voici comment choisir selon vos besoins.",
 body=H2("neobanque","Les néobanques : pour qui ?")
  +UL(["<strong>Frais réduits</strong> et carte souvent gratuite.",
       "Ouverture et gestion <strong>100 % mobile</strong>, en quelques minutes.",
       "Idéales comme <strong>compte principal léger</strong> ou compte secondaire pour les paiements à l'étranger.",
       "Limites : dépôt d'espèces compliqué, crédit immobilier rare, accompagnement humain limité."])
  +H2("banque","Les banques traditionnelles : pour qui ?")
  +UL(["<strong>Gamme complète</strong> : crédit immo, épargne, assurance, conseiller dédié.",
       "Réseau d'agences pour le dépôt d'espèces et l'accompagnement.",
       "Souvent plus chères en frais de tenue de compte."])
  +H2("choisir","Notre conseil")
  +P("Pour <strong>réduire vos frais</strong> au quotidien, une néobanque (ou banque en ligne complète comme BoursoBank) est imbattable. Pour un <strong>crédit immobilier</strong> ou un accompagnement patrimonial, la banque traditionnelle garde l'avantage. Beaucoup combinent les deux.")
  +BOX("💡 Voir notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a> pour trouver la moins chère selon votre profil."),
 faq=[("Une néobanque peut-elle être mon compte principal ?","Oui, pour la plupart des usages quotidiens. Vérifiez juste le dépôt d'espèces et la domiciliation de revenus si nécessaire."),
      ("Les néobanques sont-elles sûres ?","Les acteurs agréés offrent une garantie des dépôts comme les banques classiques. Vérifiez le statut (agrément, garantie)."),
      ("Peut-on obtenir un crédit immobilier en néobanque ?","C'est rare : pour un prêt immobilier, les banques traditionnelles ou en ligne complètes restent la voie principale.")]),

add(slug="compte-pro-obligatoire-micro-entreprise",cat="compte-pro",
 title="Compte pro obligatoire en micro-entreprise ? Ce que dit la loi (2026)",
 desc="Compte pro obligatoire en micro-entreprise en 2026 : seuil de 10 000 €, compte dédié vs compte pro, sanctions. Le point clair sur vos obligations d'auto-entrepreneur.",
 h1="Compte pro obligatoire en micro-entreprise ? Ce que dit la loi",
 lead="Beaucoup d'auto-entrepreneurs se demandent s'ils doivent ouvrir un compte professionnel. Voici la règle exacte, sans approximation.",
 body=H2("regle","La règle : compte dédié, pas forcément « pro »")
  +P("En micro-entreprise, vous devez disposer d'un <strong>compte bancaire dédié</strong> à votre activité <strong>dès que votre chiffre d'affaires dépasse 10 000 € deux années civiles consécutives</strong>. Ce compte dédié n'est <strong>pas obligatoirement un « compte pro »</strong> facturé : un second compte courant à votre nom peut suffire.")
  +H2("dedie-vs-pro","Compte dédié vs compte pro : la nuance")
  +UL(["<strong>Compte dédié</strong> : un compte séparé pour isoler les flux de l'activité. Suffisant pour respecter l'obligation.",
       "<strong>Compte pro</strong> : offre dédiée avec outils (facturation, encaissement, comptabilité) — utile mais payant, et non imposé."])
  +H2("interet","Pourquoi en ouvrir un quand même ?")
  +P("Même en dessous du seuil, un compte séparé <strong>simplifie la comptabilité</strong>, clarifie les déclarations URSSAF et rassure en cas de contrôle. Les comptes pros en ligne sont peu chers et rapides à ouvrir.")
  +BOX("💡 Voir notre <a href=\"/comparatifs/comptes-pro.html\">comparatif des comptes pro</a> et notre <a href=\"/comparatifs/compte-pro-auto-entrepreneur.html\">sélection pour auto-entrepreneurs</a>."),
 faq=[("Le compte pro est-il obligatoire en micro-entreprise ?","Non : un compte dédié à l'activité est obligatoire au-delà de 10 000 € de CA pendant deux ans, mais ce n'est pas forcément un compte « pro » payant."),
      ("Un compte courant classique suffit-il ?","Oui, un second compte courant à votre nom peut faire office de compte dédié pour respecter l'obligation."),
      ("Quel est le seuil exact ?","10 000 € de chiffre d'affaires annuel, dépassé deux années civiles consécutives.")]),

add(slug="comment-creer-un-site-internet",cat="hebergement",
 title="Comment créer un site internet en 2026 : guide débutant",
 desc="Comment créer un site internet en 2026 : nom de domaine, hébergement, CMS (WordPress) ou créateur de site, étapes et budget. Le guide clair pour se lancer.",
 h1="Comment créer un site internet en 2026 (guide débutant)",
 lead="Créer un site n'a jamais été aussi accessible. Selon votre projet, deux voies s'offrent à vous : le créateur de site tout-en-un ou WordPress + hébergement.",
 body=H2("etapes","Les 4 briques d'un site web")
  +OL(["<strong>Un nom de domaine</strong> (votre adresse, ex. monsite.fr).",
       "<strong>Un hébergement</strong> (l'espace où vivent vos fichiers).",
       "<strong>Un outil de création</strong> : WordPress (flexible) ou un créateur de site (simple).",
       "<strong>Du contenu</strong> : pages, textes, images."])
  +H2("voie","Quelle voie choisir ?")
  +UL(["<strong>Créateur de site</strong> (Shopify pour vendre, Wix/Squarespace pour vitrine) : le plus simple, tout est intégré.",
       "<strong>WordPress + hébergement</strong> : plus flexible et économique sur la durée, idéal pour blog, vitrine évolutive ou e-commerce avec WooCommerce."])
  +H2("budget","Quel budget ?")
  +P("Comptez quelques euros par mois pour un hébergement mutualisé + le nom de domaine. Les prix d'appel sont agressifs : voir notre <a href=\"/etudes/classement-hebergeurs-moins-chers.html\">classement des hébergeurs les moins chers</a> (attention au prix de renouvellement).")
  +BOX("💡 Pour choisir : <a href=\"/comparatifs/hebergement-web.html\">comparatif des hébergeurs web</a> et <a href=\"/comparatifs/hebergement-wordpress.html\">hébergement WordPress</a>."),
 faq=[("Combien coûte un site internet ?","Pour un site simple en autonomie, quelques euros par mois (hébergement + domaine). Un site sur-mesure par une agence coûte beaucoup plus."),
      ("WordPress ou créateur de site ?","WordPress pour la flexibilité et l'économie long terme ; un créateur de site (Shopify, Wix) pour la simplicité tout-en-un."),
      ("Faut-il des compétences techniques ?","Non pour un créateur de site. WordPress demande un peu d'apprentissage mais reste accessible aux débutants.")]),

add(slug="hebergement-wordpress-pas-cher",cat="hebergement",
 title="Hébergement WordPress pas cher : comment bien choisir (2026)",
 desc="Hébergement WordPress pas cher en 2026 : critères (performance, support, prix de renouvellement), pièges à éviter et meilleures offres. Le guide pour héberger WordPress.",
 h1="Hébergement WordPress pas cher : comment choisir",
 lead="WordPress fait tourner une grande partie du web. Pour qu'il soit rapide et fiable sans se ruiner, voici les critères qui comptent vraiment.",
 body=H2("criteres","Les critères d'un bon hébergement WordPress")
  +UL(["<strong>Performance</strong> : SSD/NVMe, cache intégré, PHP récent.",
       "<strong>Installation WordPress en 1 clic</strong> et mises à jour facilitées.",
       "<strong>Support réactif</strong>, idéalement en français.",
       "<strong>Prix de renouvellement</strong> raisonnable (le vrai piège, voir plus bas).",
       "<strong>Certificat SSL</strong> et sauvegardes inclus."])
  +H2("piege","Le piège du prix d'appel")
  +P("Beaucoup d'hébergeurs affichent un tarif promotionnel la première année puis renouvellent bien plus cher. Raisonnez en <strong>coût total sur 3 ans</strong>. Notre <a href=\"/etudes/classement-hebergeurs-moins-chers.html\">classement des hébergeurs les moins chers</a> détaille les écarts.")
  +H2("offres","Les bonnes options")
  +P("Hostinger et IONOS sont agressifs sur les prix d'appel ; o2switch propose un tarif unique stable très apprécié pour WordPress. Comparez dans notre <a href=\"/comparatifs/hebergement-web.html\">comparatif des hébergeurs</a>."),
 faq=[("Quel est le meilleur hébergement WordPress pas cher ?","Hostinger et IONOS sur le prix d'appel, o2switch pour un tarif stable. Le bon choix dépend de votre trafic et de vos besoins."),
      ("Un hébergement mutualisé suffit-il pour WordPress ?","Oui pour un site débutant ou à trafic modéré. Pour un gros trafic, envisagez un VPS ou un hébergement infogéré."),
      ("Faut-il un hébergement WordPress « spécial » ?","Pas obligatoirement : un bon mutualisé avec installation 1 clic suffit. L'infogéré apporte performance et tranquillité en plus.")]),

add(slug="comment-placer-10000-euros",cat="epargne",
 title="Comment placer 10 000 € en 2026 : les meilleures options",
 desc="Comment placer 10 000 € en 2026 : épargne de précaution, assurance-vie, ETF, SCPI, selon votre horizon et votre risque. Le guide pour faire fructifier 10 000 euros.",
 h1="Comment placer 10 000 € en 2026 ?",
 lead="10 000 € à placer, c'est l'occasion de poser de bonnes bases. La clé : répartir selon votre horizon et votre tolérance au risque, pas tout mettre au même endroit.",
 body=H2("precaution","1. Sécuriser une épargne de précaution")
  +P("Gardez d'abord 2 à 6 mois de dépenses disponibles immédiatement : <strong>Livret A, LDDS</strong>, et le <strong>LEP</strong> si vous y êtes éligible (le mieux rémunéré).")
  +H2("moyen-long","2. Faire fructifier le reste")
  +UL(["<strong>Assurance-vie</strong> (fonds euros + unités de compte) : l'enveloppe reine, fiscalité douce après 8 ans.",
       "<strong>ETF</strong> en assurance-vie ou via un PEA : performance des marchés à frais bas, sur le long terme.",
       "<strong>SCPI</strong> : de l'immobilier sans gestion, pour diversifier.",
       "Plus l'horizon est long, plus la part investie (vs sécurisée) peut être élevée."])
  +H2("repartition","Exemple de répartition (à adapter)")
  +P("Profil prudent : majorité en sécurisé (livrets, fonds euros). Profil long terme : une bonne part en ETF/unités de compte. Il n'y a pas de réponse unique — votre horizon et votre tolérance au risque priment.")
  +BOX("💡 Ceci n'est pas un conseil personnalisé. Comparez les contrats dans notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Où placer 10 000 € sans risque ?","Sur les livrets réglementés garantis (LEP si éligible, Livret A, LDDS) pour la partie sécurisée et disponible."),
      ("Faut-il tout mettre en assurance-vie ?","Non : gardez d'abord une épargne de précaution disponible, puis utilisez l'assurance-vie pour le long terme."),
      ("Quel placement rapporte le plus ?","Sur le long terme, les unités de compte (ETF, SCPI) visent plus de rendement, au prix d'un risque de perte en capital.")]),

add(slug="a-quoi-sert-un-vpn",cat="vpn",
 title="À quoi sert un VPN et comment le choisir en 2026 ?",
 desc="À quoi sert un VPN en 2026 : confidentialité, sécurité sur le Wi-Fi public, streaming, et comment choisir (vitesse, prix, no-log). Le guide clair pour bien choisir son VPN.",
 h1="À quoi sert un VPN et comment le choisir ?",
 lead="Un VPN chiffre votre connexion et masque votre adresse IP. Utile pour la vie privée et la sécurité — voici ses vrais usages et comment choisir.",
 body=H2("usages","À quoi sert vraiment un VPN ?")
  +UL(["<strong>Protéger sa connexion</strong> sur les Wi-Fi publics (café, aéroport).",
       "<strong>Préserver sa vie privée</strong> en masquant son adresse IP à son fournisseur d'accès et aux sites.",
       "<strong>Accéder à des contenus</strong> selon la zone géographique (streaming, voyages).",
       "Ce qu'un VPN ne fait pas : vous rendre totalement anonyme ni remplacer un antivirus."])
  +H2("choisir","Comment choisir son VPN ?")
  +UL(["<strong>Politique no-log</strong> vérifiée et juridiction respectueuse de la vie privée.",
       "<strong>Vitesse</strong> et nombre de serveurs (important pour le streaming).",
       "<strong>Prix</strong> : les grosses réductions ne valent que sur les engagements longs.",
       "<strong>Nombre d'appareils</strong> couverts simultanément."])
  +H2("offres","Les valeurs sûres")
  +P("ExpressVPN (rapide, premium), NordVPN (complet) et Surfshark (le meilleur rapport qualité/prix, appareils illimités) sont des références. Comparez dans notre <a href=\"/comparatifs/vpn.html\">comparatif des VPN</a>."),
 faq=[("Un VPN gratuit est-il fiable ?","Méfiance : beaucoup de VPN gratuits financent leur service par la revente de données. Pour un usage sérieux, un VPN payant no-log est préférable."),
      ("Un VPN ralentit-il la connexion ?","Un peu, car le trafic est chiffré et redirigé. Les bons VPN limitent fortement cette perte de vitesse."),
      ("Quel est le meilleur VPN en 2026 ?","ExpressVPN, NordVPN et Surfshark figurent parmi les références. Le meilleur dépend de votre usage et de votre budget.")])

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
print("guides verticales créés :", len(G))
for d in G: print("  guides/"+d['slug']+".html ("+d['cat']+")")
