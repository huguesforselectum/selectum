#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 6 : long-tail supplementaire."""
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
 "epargne":[("/comparatifs/assurance-vie.html","Comparatif assurance-vie"),("/comparatifs/per-retraite.html","Comparatif PER"),("/code-promo/linxea.html","Code promo Linxea"),("/code-promo/yomoni.html","Offres Yomoni")],
 "credit":[("/comparatifs/credit-conso.html","Comparatif crédit conso"),("/comparatifs/rachat-credit.html","Rachat de crédit"),("/comparatifs/courtage-immobilier.html","Courtage immobilier")],
 "assurance":[("/comparatifs/assurance-auto.html","Comparatif assurance auto"),("/comparatifs/assurance-habitation.html","Assurance habitation"),("/comparatifs/mutuelle-sante.html","Mutuelle santé")],
 "vpn":[("/comparatifs/vpn.html","Comparatif des VPN"),("/code-promo/expressvpn.html","Code promo ExpressVPN"),("/code-promo/nordvpn.html","Offres NordVPN"),("/code-promo/surfshark.html","Code promo Surfshark")],
}
CATLABEL={"crypto":"Crypto","banque":"Banque","epargne":"Épargne","credit":"Crédit","assurance":"Assurance","vpn":"Tech"}
G=[]
def add(**k): G.append(k)

add(slug="assurance-trottinette-electrique",cat="assurance",
 title="Assurance trottinette électrique en 2026 : est-ce obligatoire ?",
 desc="Assurance trottinette électrique (EDPM) en 2026 : obligation légale, garanties, prix, sanctions. Le guide clair pour assurer sa trottinette et rouler en règle.",
 h1="Assurance trottinette électrique : est-ce obligatoire ?",
 lead="Rouler en trottinette électrique sans assurance peut coûter cher. Voici ce que dit la loi et comment bien s'assurer.",
 body=H2("obligation","Une obligation légale")
  +P("Les <strong>EDPM</strong> (engins de déplacement personnel motorisés), dont la trottinette électrique, sont soumis à l'obligation d'<strong>assurance responsabilité civile</strong>, comme un véhicule. Rouler sans assurance expose à une amende.")
  +H2("garanties","Quelles garanties ?")
  +UL(["<strong>Responsabilité civile</strong> (obligatoire) : couvre les dommages causés à autrui.",
       "<strong>Vol et dommages</strong> : optionnel mais utile pour une trottinette de valeur.",
       "<strong>Garantie corporelle</strong> du conducteur."])
  +H2("prix","Combien ça coûte ?")
  +P("Les tarifs sont modestes pour la RC seule, plus élevés avec vol et dommages. Certaines assurances habitation incluent une part de couverture — à vérifier.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/assurance-auto.html\">comparatif assurance</a>."),
 faq=[("L'assurance trottinette est-elle obligatoire ?","Oui, la responsabilité civile est obligatoire pour les trottinettes électriques (EDPM), comme pour un véhicule."),
      ("Combien coûte une assurance trottinette ?","La RC seule est peu coûteuse ; ajouter vol et dommages augmente la prime selon la valeur de l'engin."),
      ("Mon assurance habitation couvre-t-elle ma trottinette ?","Parfois en partie, mais rarement la RC circulation obligatoire. Vérifiez votre contrat.")]),

add(slug="faut-il-un-antivirus-sur-mac",cat="vpn",
 title="Faut-il un antivirus sur Mac en 2026 ?",
 desc="Faut-il un antivirus sur Mac en 2026 ? Risques réels (phishing, malwares), protections intégrées, quand un antivirus est utile. Le guide clair pour sécuriser son Mac.",
 h1="Faut-il un antivirus sur Mac ?",
 lead="Les Mac sont réputés sûrs, mais pas invulnérables. Voici quand un antivirus est utile et comment se protéger efficacement.",
 body=H2("realite","Mac n'est pas invulnérable")
  +P("macOS intègre des protections, mais les Mac sont de plus en plus ciblés par les <strong>malwares</strong> et surtout le <strong>phishing</strong> (qui ne dépend pas du système). Aucun appareil connecté n'est totalement à l'abri.")
  +H2("quand","Quand un antivirus est utile")
  +UL(["Si vous <strong>téléchargez beaucoup</strong> de logiciels hors App Store.",
       "Pour une <strong>protection web</strong> anti-phishing renforcée.",
       "Pour un usage familial ou professionnel sensible."])
  +H2("autres","Au-delà de l'antivirus")
  +P("Les bons réflexes comptent autant : mises à jour, mots de passe forts (gestionnaire), méfiance face aux emails. Un <strong>VPN</strong> protège la connexion — voir <a href=\"/guides/a-quoi-sert-un-vpn.html\">à quoi sert un VPN</a>.")
  +BOX("💡 Voir notre <a href=\"/guides/meilleur-antivirus.html\">guide meilleur antivirus</a> et le <a href=\"/comparatifs/vpn.html\">comparatif VPN</a>."),
 faq=[("Mac a-t-il besoin d'un antivirus ?","Pas indispensable pour un usage prudent grâce aux protections intégrées, mais utile contre le phishing et si vous téléchargez beaucoup hors App Store."),
      ("Les Mac attrapent-ils des virus ?","Moins que Windows, mais ils sont de plus en plus ciblés, et le phishing les concerne autant."),
      ("Quel antivirus pour Mac ?","Bitdefender et Avast proposent des versions Mac. Un VPN complète la protection de la vie privée.")]),

add(slug="meilleure-carte-bancaire-gratuite",cat="banque",
 title="Meilleure carte bancaire gratuite en 2026",
 desc="Quelle est la meilleure carte bancaire gratuite en 2026 ? Conditions de revenus, paiements à l'étranger, assurances. Critères et sélection pour une carte sans frais.",
 h1="Meilleure carte bancaire gratuite",
 lead="Plusieurs banques offrent une carte gratuite, parfois sous condition. Voici comment choisir la vraie carte sans frais adaptée à vous.",
 body=H2("conditions","Gratuite, mais sous conditions ?")
  +P("Beaucoup de cartes « gratuites » exigent un <strong>usage minimum</strong> (un paiement par mois) ou des <strong>conditions de revenus</strong>. Les néobanques proposent souvent une carte gratuite <strong>sans condition</strong>.")
  +H2("criteres","Ce qui compte")
  +UL(["Gratuité <strong>réelle</strong> (sans condition cachée).",
       "<strong>Paiements à l'étranger</strong> sans surcoût.",
       "<strong>Assurances</strong> et plafonds adaptés.",
       "Parfois une <strong>prime de bienvenue</strong>."])
  +H2("selection","Notre sélection")
  +P("<strong>N26</strong> et <strong>Revolut</strong> pour une carte gratuite sans condition et idéale à l'étranger ; <strong>BoursoBank</strong> pour une banque complète avec carte gratuite (sous condition d'usage).")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a>."),
 faq=[("Quelle carte bancaire est vraiment gratuite ?","Les néobanques (N26, Revolut) offrent une carte gratuite sans condition. Les banques en ligne (BoursoBank) sont gratuites sous condition d'usage."),
      ("Une carte gratuite a-t-elle des assurances ?","Les cartes d'entrée ont des assurances de base ; les gammes supérieures (souvent payantes) offrent plus."),
      ("Carte gratuite et paiements à l'étranger ?","N26 et Revolut permettent de payer à l'étranger sans surcoût, idéal en voyage.")]),

add(slug="comment-changer-de-banque",cat="banque",
 title="Comment changer de banque en 2026 (mobilité bancaire) ?",
 desc="Comment changer de banque en 2026 grâce à la mobilité bancaire : le service d'aide à la mobilité, démarches automatiques, délais. Le guide pour changer sans stress.",
 h1="Comment changer de banque (mobilité bancaire) ?",
 lead="Changer de banque est devenu simple grâce au service d'aide à la mobilité bancaire. La nouvelle banque s'occupe de presque tout.",
 body=H2("mobilite","Le service d'aide à la mobilité")
  +P("Depuis la <strong>loi Macron</strong>, votre nouvelle banque peut prendre en charge le <strong>transfert de vos prélèvements et virements récurrents</strong> à votre place, gratuitement. Vous signez un mandat, elle s'occupe du reste.")
  +H2("etapes","Les étapes")
  +OL(["<strong>Ouvrez</strong> le nouveau compte.",
       "Signez le <strong>mandat de mobilité bancaire</strong>.",
       "La nouvelle banque informe les émetteurs (employeur, fournisseurs…).",
       "<strong>Clôturez</strong> l'ancien compte une fois les opérations basculées."])
  +H2("conseil","Le bon réflexe")
  +P("Gardez l'ancien compte ouvert <strong>quelques semaines</strong> le temps que tous les prélèvements basculent, pour éviter tout incident.")
  +BOX("💡 Comparez les banques dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a>."),
 faq=[("La mobilité bancaire est-elle gratuite ?","Oui, le service d'aide à la mobilité bancaire est gratuit et pris en charge par la nouvelle banque."),
      ("Combien de temps pour changer de banque ?","Le basculement des prélèvements et virements prend généralement quelques semaines."),
      ("Faut-il clôturer soi-même l'ancien compte ?","Oui, la clôture de l'ancien compte reste à votre initiative, une fois les opérations transférées.")]),

add(slug="meilleure-assurance-habitation-etudiant",cat="assurance",
 title="Meilleure assurance habitation étudiant en 2026",
 desc="Quelle est la meilleure assurance habitation pour étudiant en 2026 ? Obligation, garanties utiles, prix, colocation. Le guide pour assurer son logement étudiant pas cher.",
 h1="Meilleure assurance habitation pour étudiant",
 lead="Une assurance habitation est obligatoire pour un logement étudiant. Voici comment trouver une couverture adaptée au meilleur prix.",
 body=H2("obligation","Obligatoire pour un locataire")
  +P("En tant que locataire (y compris en résidence étudiante ou colocation), l'<strong>assurance habitation est obligatoire</strong>. Le propriétaire peut l'exiger à l'entrée dans les lieux.")
  +H2("garanties","Les garanties utiles")
  +UL(["<strong>Responsabilité civile</strong> et risques locatifs (dégât des eaux, incendie).",
       "<strong>Vol</strong> et dommages aux biens (selon la valeur).",
       "Adapter aux <strong>petites surfaces</strong> pour payer moins."])
  +H2("prix","Payer moins cher")
  +P("Les contrats étudiants sont souvent peu chers. Comparez, et en <strong>colocation</strong>, vérifiez si un contrat unique couvre tous les colocataires.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/assurance-habitation.html\">comparatif assurance habitation</a>."),
 faq=[("L'assurance habitation est-elle obligatoire pour un étudiant ?","Oui, pour tout locataire, y compris en résidence étudiante ou colocation."),
      ("Combien coûte une assurance habitation étudiant ?","Généralement peu cher pour une petite surface ; comparez les offres dédiées aux étudiants."),
      ("Comment assurer une colocation ?","Soit chaque colocataire s'assure, soit un contrat unique couvre le logement ; vérifiez les conditions.")]),

add(slug="credit-auto-ou-loa",cat="credit",
 title="Crédit auto ou LOA : que choisir pour financer sa voiture (2026) ?",
 desc="Crédit auto ou LOA (leasing) en 2026 : propriété, coût total, kilométrage, flexibilité. Comparatif clair pour choisir comment financer l'achat de sa voiture.",
 h1="Crédit auto ou LOA : que choisir ?",
 lead="Acheter à crédit ou louer avec option d'achat (LOA) ? Le bon choix dépend de votre usage et de votre rapport à la propriété.",
 body=H2("credit","Le crédit auto")
  +UL(["Vous devenez <strong>propriétaire</strong> du véhicule.",
       "<strong>Mensualités</strong> sur une durée définie, puis plus rien.",
       "Idéal si vous gardez longtemps la voiture."])
  +H2("loa","La LOA (leasing)")
  +UL(["Vous <strong>louez</strong> avec une option d'achat en fin de contrat.",
       "<strong>Mensualités souvent plus basses</strong>, mais kilométrage limité.",
       "Pratique pour changer régulièrement de véhicule."])
  +H2("choisir","Lequel choisir ?")
  +P("Le <strong>crédit</strong> si vous gardez la voiture longtemps et voulez la posséder ; la <strong>LOA</strong> si vous changez souvent et privilégiez une mensualité basse. Comparez le <strong>coût total</strong> dans les deux cas.")
  +BOX("💡 Voir notre <a href=\"/comparatifs/credit-conso.html\">comparatif crédit conso</a>. Un crédit vous engage et doit être remboursé."),
 faq=[("Crédit auto ou LOA, lequel est moins cher ?","Comparez le coût total : la LOA a des mensualités plus basses mais vous ne possédez pas la voiture. Le crédit coûte parfois moins sur la durée si vous gardez le véhicule."),
      ("La LOA permet-elle de devenir propriétaire ?","Oui, via l'option d'achat en fin de contrat, à un prix fixé au départ."),
      ("Quel financement pour changer souvent de voiture ?","La LOA est adaptée si vous renouvelez votre véhicule régulièrement.")]),

add(slug="comment-epargner-chaque-mois",cat="epargne",
 title="Comment épargner chaque mois en 2026 : méthode simple",
 desc="Comment épargner chaque mois en 2026 : se payer en premier, virement automatique, répartition livrets/placements. Le guide concret pour épargner régulièrement.",
 h1="Comment épargner chaque mois ?",
 lead="Épargner régulièrement est plus efficace qu'un gros effort ponctuel. La clé : automatiser et se payer en premier.",
 body=H2("methode","La méthode qui marche")
  +OL(["<strong>Se payer en premier</strong> : virer une somme vers l'épargne dès la réception du salaire.",
       "<strong>Automatiser</strong> ce virement (le jour de la paie).",
       "Commencer <strong>petit</strong> mais régulier, puis augmenter."])
  +H2("repartition","Où placer cette épargne ?")
  +UL(["<strong>Épargne de précaution</strong> sur les livrets (Livret A, LDDS, LEP).",
       "<strong>Long terme</strong> via des versements programmés en assurance-vie ou ETF.",
       "Adapter selon votre horizon et votre tolérance au risque."])
  +H2("astuce","L'astuce des versements programmés")
  +P("Investir une somme fixe chaque mois (en ETF ou assurance-vie) lisse les points d'entrée et crée une discipline d'épargne puissante sur le long terme.")
  +BOX("💡 Voir <a href=\"/guides/comment-placer-10000-euros.html\">comment placer son épargne</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Combien faut-il épargner par mois ?","Il n'y a pas de règle unique. L'important est la régularité : même un petit montant automatisé crée une habitude efficace."),
      ("Comment être sûr d'épargner ?","Automatisez un virement vers l'épargne le jour de la paie : c'est la méthode « se payer en premier »."),
      ("Où placer son épargne mensuelle ?","Livrets pour la précaution, versements programmés en assurance-vie/ETF pour le long terme.")]),

add(slug="livret-a-plein-que-faire",cat="epargne",
 title="Livret A plein : que faire de son épargne en 2026 ?",
 desc="Livret A plein en 2026 : où placer la suite de son épargne ? LDDS, LEP, fonds euros, ETF. Le guide pour faire fructifier son argent au-delà du plafond du Livret A.",
 h1="Livret A plein : que faire de son épargne ?",
 lead="Votre Livret A a atteint le plafond de 22 950 € ? Voici où orienter la suite de votre épargne selon votre horizon.",
 body=H2("livrets","1. Les autres livrets")
  +UL(["<strong>LDDS</strong> (plafond 12 000 €) : mêmes taux, en complément.",
       "<strong>LEP</strong> (si éligible) : le mieux rémunéré des livrets garantis.",
       "Ces livrets restent garantis et disponibles."])
  +H2("placements","2. Au-delà des livrets")
  +UL(["<strong>Fonds euros</strong> en assurance-vie : sécurisé, sans plafond réglementaire.",
       "<strong>ETF</strong> (assurance-vie ou PEA) pour viser plus de rendement sur le long terme.",
       "<strong>SCPI</strong> pour diversifier dans l'immobilier."])
  +H2("conseil","Le bon ordre")
  +P("Remplissez d'abord LDDS et LEP (si éligible), puis orientez le surplus vers une <strong>assurance-vie</strong> pour le long terme.")
  +BOX("💡 Voir <a href=\"/guides/comment-placer-10000-euros.html\">comment placer son épargne</a> et le <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Que faire quand le Livret A est plein ?","Remplir le LDDS et le LEP (si éligible), puis orienter le surplus vers une assurance-vie pour le long terme."),
      ("Quel est le plafond du Livret A ?","22 950 € de versements. Au-delà, seuls les intérêts continuent de s'ajouter."),
      ("Le fonds euros a-t-il un plafond ?","Non, contrairement aux livrets réglementés, le fonds euros d'une assurance-vie n'a pas de plafond réglementaire.")]),

add(slug="qu-est-ce-que-la-defi",cat="crypto",
 title="DeFi : qu'est-ce que la finance décentralisée en 2026 ?",
 desc="La DeFi (finance décentralisée) en 2026 : définition, usages (prêt, échange, rendement), risques. Le guide clair pour comprendre la finance décentralisée crypto.",
 h1="DeFi : qu'est-ce que la finance décentralisée ?",
 lead="La DeFi promet des services financiers sans intermédiaire, directement sur la blockchain. Voici ce que c'est, et ses risques.",
 body=H2("definition","La DeFi en bref")
  +P("La <strong>DeFi</strong> (Decentralized Finance) regroupe des services financiers — prêt, échange, épargne — fonctionnant via des <strong>contrats intelligents</strong> sur la blockchain (surtout Ethereum), sans banque ni intermédiaire.")
  +H2("usages","Les usages")
  +UL(["<strong>Échanger</strong> des cryptos sans plateforme centralisée (DEX).",
       "<strong>Prêter / emprunter</strong> des cryptos.",
       "<strong>Générer du rendement</strong> (staking, liquidité)."])
  +H2("risques","Les risques (importants)")
  +UL(["<strong>Failles de contrats intelligents</strong> et piratages.",
       "<strong>Volatilité</strong> et pertes possibles.",
       "Aucune garantie ni recours en cas de problème.",
       "Complexité technique élevée."])
  +BOX("⚠️ La DeFi est risquée et réservée aux utilisateurs avertis. Investir comporte un risque de perte en capital. Pour débuter simplement, voir notre <a href=\"/comparatifs/crypto.html\">comparatif des applications crypto</a>."),
 faq=[("Qu'est-ce que la DeFi ?","La finance décentralisée : des services financiers (prêt, échange, rendement) sur la blockchain, sans intermédiaire, via des contrats intelligents."),
      ("La DeFi est-elle risquée ?","Oui, fortement : failles techniques, piratages, volatilité et absence de recours. Elle s'adresse aux utilisateurs avertis."),
      ("Faut-il débuter par la DeFi ?","Non : mieux vaut commencer par une application crypto régulée avant d'explorer la DeFi.")]),

add(slug="comment-securiser-son-compte-en-ligne",cat="vpn",
 title="Comment sécuriser ses comptes en ligne en 2026 ?",
 desc="Comment sécuriser ses comptes en ligne en 2026 : mots de passe forts, double authentification (2FA), gestionnaire, anti-phishing. Le guide concret pour se protéger.",
 h1="Comment sécuriser ses comptes en ligne ?",
 lead="Quelques réflexes simples suffisent à éviter la grande majorité des piratages. Voici l'essentiel à mettre en place.",
 body=H2("mdp","1. Des mots de passe forts et uniques")
  +P("Utilisez un <strong>mot de passe différent</strong> pour chaque service, long et complexe. Un <strong>gestionnaire de mots de passe</strong> les retient à votre place.")
  +H2("2fa","2. La double authentification (2FA)")
  +P("Activez la <strong>2FA</strong> partout où c'est possible (banque, email, crypto). Même si votre mot de passe fuite, l'accès reste protégé.")
  +H2("phishing","3. Se méfier du phishing")
  +UL(["Ne cliquez pas sur les liens d'emails/SMS suspects.",
       "Vérifiez l'adresse exacte des sites avant de saisir vos identifiants.",
       "Aucune banque ne demande vos codes par email ou téléphone."])
  +H2("vpn","4. Protéger sa connexion")
  +P("Sur un Wi-Fi public, un <strong>VPN</strong> chiffre votre trafic — voir <a href=\"/guides/a-quoi-sert-un-vpn.html\">à quoi sert un VPN</a>.")
  +BOX("💡 Voir notre <a href=\"/guides/meilleur-antivirus.html\">guide antivirus</a> et le <a href=\"/comparatifs/vpn.html\">comparatif VPN</a>."),
 faq=[("Comment protéger ses comptes en ligne ?","Mots de passe forts et uniques (gestionnaire), double authentification (2FA) partout, et méfiance face au phishing."),
      ("Qu'est-ce que la 2FA ?","La double authentification ajoute une seconde preuve d'identité (code, appli) en plus du mot de passe, pour bloquer les accès non autorisés."),
      ("Un gestionnaire de mots de passe est-il sûr ?","Oui, c'est bien plus sûr que de réutiliser le même mot de passe partout. Il chiffre vos identifiants.")])

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
print("batch 6 guides créés :", len(G))
