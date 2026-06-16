#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 2 : guides verticales (credit/assurance/transfert/energie/PER) + long-tail 'meilleur X pour Y'."""
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
 "credit":[("/comparatifs/credit-conso.html","Comparatif crédit conso"),("/comparatifs/rachat-credit.html","Rachat de crédit"),("/comparatifs/courtage-immobilier.html","Courtage immobilier")],
 "assurance":[("/comparatifs/assurance-auto.html","Comparatif assurance auto"),("/comparatifs/assurance-habitation.html","Assurance habitation"),("/comparatifs/mutuelle-sante.html","Mutuelle santé")],
 "transfert":[("/comparatifs/transfert-argent.html","Comparatif transfert d'argent"),("/code-promo/wise.html","Code promo Wise"),("/comparatifs/change-multidevises.html","Change multi-devises")],
 "energie":[("/comparatifs/fournisseur-energie.html","Comparatif fournisseurs d'énergie"),("/comparatifs/kit-solaire-autoconsommation.html","Kit solaire autoconsommation")],
}
CATLABEL={"crypto":"Crypto","bourse":"Bourse","banque":"Banque","compte-pro":"Compte pro","epargne":"Épargne","credit":"Crédit","assurance":"Assurance","transfert":"Transfert d'argent","energie":"Énergie"}

G=[]
def add(**k): G.append(k)

# ---------- Crédit ----------
add(slug="comment-obtenir-credit-consommation",cat="credit",
 title="Comment obtenir un crédit à la consommation en 2026 ?",
 desc="Comment obtenir un crédit à la consommation en 2026 : TAEG, capacité d'emprunt, justificatifs, délai de rétractation et erreurs à éviter. Le guide clair pour bien emprunter.",
 h1="Comment obtenir un crédit à la consommation ?",
 lead="Prêt personnel, crédit auto, crédit travaux : voici comment obtenir un crédit conso au meilleur taux, sans mauvaise surprise.",
 body=H2("types","Les types de crédit conso")
  +UL(["<strong>Prêt personnel</strong> : somme libre d'utilisation, mensualités fixes.",
       "<strong>Crédit affecté</strong> (auto, travaux) : lié à un achat précis.",
       "<strong>Crédit renouvelable</strong> : réserve d'argent, à manier avec prudence (taux élevés)."])
  +H2("taeg","Le seul chiffre qui compte : le TAEG")
  +P("Le <strong>TAEG</strong> (taux annuel effectif global) inclut tous les frais : c'est lui qu'il faut comparer, pas le taux nominal. Plus il est bas, moins votre crédit coûte.")
  +H2("etapes","Les étapes pour emprunter")
  +OL(["Estimez votre <strong>capacité d'emprunt</strong> (taux d'endettement raisonnable).",
       "Comparez les offres sur le <strong>TAEG</strong> et le coût total.",
       "Préparez les <strong>justificatifs</strong> (identité, revenus, RIB).",
       "Profitez du <strong>délai de rétractation de 14 jours</strong> après signature."])
  +BOX("💡 Comparez les offres dans notre <a href=\"/comparatifs/credit-conso.html\">comparatif crédit conso</a>. Un crédit vous engage et doit être remboursé."),
 faq=[("Quel est le meilleur taux pour un crédit conso ?","Cela dépend du montant, de la durée et de votre profil. Comparez toujours le TAEG, qui inclut tous les frais."),
      ("Peut-on annuler un crédit après signature ?","Oui, vous disposez d'un délai légal de rétractation de 14 jours après la signature de l'offre."),
      ("Quel taux d'endettement ne pas dépasser ?","On considère généralement qu'un taux d'endettement autour de 35 % est un repère de prudence, variable selon les situations.")]),

add(slug="rachat-de-credit-comment-ca-marche",cat="credit",
 title="Rachat de crédit : comment ça marche et quand y recourir (2026)",
 desc="Rachat de crédit en 2026 : principe, avantages, coût, quand c'est intéressant et pièges à éviter. Le guide clair pour regrouper ses crédits et baisser ses mensualités.",
 h1="Rachat de crédit : comment ça marche ?",
 lead="Regrouper ses crédits en un seul peut réduire la mensualité et soulager le budget — mais ce n'est pas toujours une bonne affaire. Décryptage.",
 body=H2("principe","Le principe du rachat de crédit")
  +P("Le <strong>rachat (ou regroupement) de crédit</strong> consiste à remplacer plusieurs crédits par un seul, avec une <strong>mensualité unique plus basse</strong> grâce à un allongement de la durée. On gagne en trésorerie mensuelle, mais le coût total augmente souvent.")
  +H2("quand","Quand est-ce intéressant ?")
  +UL(["Quand le <strong>taux d'endettement est trop élevé</strong> et pèse sur le budget.",
       "Pour <strong>simplifier</strong> sa gestion (une seule mensualité).",
       "Quand les taux ont baissé depuis vos crédits initiaux."])
  +H2("vigilance","Les points de vigilance")
  +P("Allonger la durée fait <strong>monter le coût total</strong>. Surveillez les frais (dossier, garantie, éventuelles indemnités de remboursement anticipé). Comparez le <strong>coût total</strong>, pas seulement la mensualité.")
  +BOX("💡 Voir notre <a href=\"/comparatifs/rachat-credit.html\">comparatif rachat de crédit</a>. Un crédit vous engage et doit être remboursé."),
 faq=[("Le rachat de crédit fait-il baisser le coût total ?","Pas forcément : il baisse la mensualité en allongeant la durée, ce qui augmente souvent le coût total. À évaluer au cas par cas."),
      ("Peut-on inclure un crédit immobilier ?","Oui, certains rachats regroupent crédits conso et immobilier, mais les conditions diffèrent."),
      ("Y a-t-il des frais ?","Oui : frais de dossier, garantie, et parfois indemnités de remboursement anticipé. À intégrer dans le calcul.")]),

# ---------- Assurance ----------
add(slug="comment-changer-assurance-auto",cat="assurance",
 title="Comment changer d'assurance auto en 2026 (loi Hamon) ?",
 desc="Comment changer d'assurance auto en 2026 : loi Hamon, résiliation après 1 an, démarches, économies possibles. Le guide simple pour résilier et changer sans stress.",
 h1="Comment changer d'assurance auto (loi Hamon) ?",
 lead="Changer d'assurance auto est devenu très simple grâce à la loi Hamon. À la clé, souvent plusieurs dizaines d'euros d'économies par an.",
 body=H2("hamon","La loi Hamon en bref")
  +P("Depuis la <strong>loi Hamon</strong>, vous pouvez résilier votre assurance auto <strong>à tout moment après la première année</strong>, sans frais ni justificatif. Le nouvel assureur s'occupe même des démarches de résiliation.")
  +H2("etapes","Changer en 4 étapes")
  +OL(["<strong>Comparez les offres</strong> à garanties équivalentes (pas seulement le prix).",
       "<strong>Souscrivez</strong> le nouveau contrat.",
       "Le nouvel assureur <strong>résilie l'ancien</strong> à votre place.",
       "Vérifiez la <strong>date de prise d'effet</strong> pour éviter tout trou de couverture."])
  +H2("economie","Combien peut-on économiser ?")
  +P("Les écarts de prix entre assureurs sont importants à garanties comparables. Mettre en concurrence chaque année est l'un des gestes les plus rentables sur le budget auto.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/assurance-auto.html\">comparatif assurance auto</a>."),
 faq=[("Quand peut-on résilier son assurance auto ?","À tout moment après la première année d'engagement, grâce à la loi Hamon, sans frais ni motif."),
      ("Qui s'occupe de la résiliation ?","Le nouvel assureur prend en charge la résiliation de votre ancien contrat."),
      ("Faut-il un justificatif pour changer ?","Non, après un an la résiliation est libre. Comparez juste les garanties pour ne pas perdre en couverture.")]),

add(slug="comment-choisir-mutuelle-sante",cat="assurance",
 title="Mutuelle santé : comment bien choisir en 2026 ?",
 desc="Comment choisir sa mutuelle santé en 2026 : garanties utiles, niveaux de remboursement, reste à charge, profil. Le guide pour trouver la complémentaire santé adaptée.",
 h1="Mutuelle santé : comment bien choisir ?",
 lead="Une bonne mutuelle, c'est celle qui colle à VOS besoins, pas la plus chère ni la moins chère. Voici comment choisir intelligemment.",
 body=H2("besoins","Partez de vos besoins réels")
  +P("Avant le prix, identifiez vos <strong>postes de dépenses</strong> : optique, dentaire, hospitalisation, médecines douces… Une mutuelle généreuse sur l'optique est inutile si vous n'en avez pas besoin.")
  +H2("garanties","Lire les niveaux de garanties")
  +UL(["Les remboursements s'expriment en % de la base Sécu ou en forfaits €.",
       "Visez à <strong>réduire votre reste à charge</strong> sur les postes qui vous concernent.",
       "Attention aux <strong>délais de carence</strong> et plafonds annuels."])
  +H2("profil","Adapter à son profil")
  +P("Un jeune actif, une famille ou un senior n'ont pas les mêmes besoins. Réévaluez votre contrat quand votre situation change.")
  +BOX("💡 Comparez les offres dans notre <a href=\"/comparatifs/mutuelle-sante.html\">comparatif mutuelle santé</a>."),
 faq=[("Comment payer moins cher sa mutuelle ?","En choisissant des garanties adaptées à vos besoins réels plutôt qu'une couverture maximale inutile, et en comparant régulièrement."),
      ("Peut-on changer de mutuelle facilement ?","Oui, la résiliation infra-annuelle permet de changer après un an d'engagement, sans frais."),
      ("Quelles garanties privilégier ?","Celles qui correspondent à vos dépenses : optique, dentaire, hospitalisation… Inutile de surpayer des postes que vous n'utilisez pas.")]),

# ---------- Transfert ----------
add(slug="envoyer-argent-etranger-meilleur-taux",cat="transfert",
 title="Comment envoyer de l'argent à l'étranger au meilleur taux (2026) ?",
 desc="Comment envoyer de l'argent à l'étranger au meilleur taux en 2026 : éviter les frais cachés du change, comparer les services (Wise, Revolut…), délais et sécurité.",
 h1="Comment envoyer de l'argent à l'étranger au meilleur taux ?",
 lead="Les banques classiques facturent cher les transferts internationaux, surtout via un taux de change défavorable. Voici comment payer beaucoup moins.",
 body=H2("piege","Le vrai piège : le taux de change")
  +P("Beaucoup de services affichent « 0 frais » mais se rémunèrent sur un <strong>taux de change défavorable</strong> (une marge cachée). Comparez toujours le <strong>montant réellement reçu</strong> par le destinataire.")
  +H2("solutions","Les solutions les moins chères")
  +UL(["Les spécialistes du transfert (Wise, Revolut…) appliquent souvent le <strong>taux de change réel</strong> avec une commission transparente.",
       "Pour les petits montants réguliers, certaines apps sont quasi gratuites.",
       "Les banques traditionnelles restent les plus chères."])
  +H2("verifier","Ce qu'il faut vérifier")
  +P("Le <strong>montant reçu net</strong>, le <strong>délai</strong>, et la couverture du pays de destination. Pour un envoi important, vérifiez aussi les plafonds.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/transfert-argent.html\">comparatif transfert d'argent</a> et notre <a href=\"/comparatifs/change-multidevises.html\">comparatif change multi-devises</a>."),
 faq=[("Quel est le moins cher pour envoyer de l'argent à l'étranger ?","Les spécialistes comme Wise appliquent souvent le taux réel avec une commission transparente, généralement moins cher qu'une banque."),
      ("Pourquoi « 0 frais » n'est pas toujours gratuit ?","Parce que la marge peut être cachée dans un taux de change défavorable. Comparez le montant réellement reçu."),
      ("Combien de temps prend un transfert international ?","De quelques minutes à quelques jours selon le service, le pays et le mode de réception.")]),

# ---------- Énergie ----------
add(slug="comment-changer-fournisseur-energie",cat="energie",
 title="Comment changer de fournisseur d'énergie en 2026 (étapes) ?",
 desc="Comment changer de fournisseur d'électricité ou de gaz en 2026 : démarches gratuites, sans coupure, économies possibles et pièges. Le guide simple pour changer sereinement.",
 h1="Comment changer de fournisseur d'énergie ?",
 lead="Changer de fournisseur d'électricité ou de gaz est gratuit, sans coupure et sans engagement. C'est l'un des gestes les plus simples pour baisser sa facture.",
 body=H2("simple","Un changement simple et sans risque")
  +UL(["<strong>Gratuit</strong> et sans frais de résiliation.",
       "<strong>Sans coupure</strong> : c'est le même réseau, seul le fournisseur change.",
       "<strong>Sans engagement</strong> : vous pouvez revenir ou rechanger à tout moment.",
       "Aucune démarche auprès de l'ancien fournisseur : le nouveau s'en charge."])
  +H2("etapes","Changer en 3 étapes")
  +OL(["<strong>Comparez les offres</strong> (prix du kWh, abonnement, type d'offre).",
       "<strong>Souscrivez</strong> chez le nouveau fournisseur (munissez-vous d'une facture pour le PDL/PCE).",
       "Le nouveau fournisseur <strong>résilie l'ancien contrat</strong> automatiquement."])
  +H2("offres","Prix fixe, indexé ou vert ?")
  +P("Le <strong>prix fixe</strong> sécurise, l'<strong>indexé</strong> suit le marché, le <strong>vert</strong> soutient les renouvelables. Certaines offres vertes sont parmi les moins chères.")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/fournisseur-energie.html\">comparatif des fournisseurs d'énergie</a>."),
 faq=[("Changer de fournisseur coupe-t-il l'électricité ?","Non, jamais. Le réseau reste le même, seul le fournisseur change. Aucune intervention technique n'est nécessaire."),
      ("Le changement est-il payant ?","Non, c'est entièrement gratuit et sans frais de résiliation."),
      ("Peut-on revenir au tarif réglementé ?","Oui, vous pouvez changer ou revenir à tout moment, sans engagement.")]),

# ---------- PER / retraite ----------
add(slug="per-comment-preparer-retraite",cat="epargne",
 title="PER : comment préparer sa retraite en 2026 ?",
 desc="Le Plan d'épargne retraite (PER) en 2026 : fonctionnement, avantage fiscal, sortie en capital ou rente, pour qui c'est intéressant. Le guide pour préparer sa retraite.",
 h1="PER : comment préparer sa retraite ?",
 lead="Le Plan d'épargne retraite combine un avantage fiscal immédiat et une grande liberté de sortie. Voici comment l'utiliser intelligemment.",
 body=H2("principe","Comment fonctionne le PER")
  +P("Le <strong>PER</strong> permet d'épargner pour la retraite avec un atout majeur : les versements sont <strong>déductibles du revenu imposable</strong> (dans certaines limites), ce qui réduit votre impôt dès l'année du versement.")
  +H2("pour-qui","Pour qui est-ce intéressant ?")
  +UL(["Les contribuables <strong>fortement imposés</strong> (plus la tranche est élevée, plus l'économie d'impôt est forte).",
       "Ceux qui veulent <strong>préparer la retraite</strong> sur un horizon long.",
       "Les profils prêts à <strong>bloquer l'épargne</strong> jusqu'à la retraite (hors déblocages anticipés)."])
  +H2("sortie","Sortie en capital ou en rente")
  +P("À la retraite, le PER offre une <strong>liberté de sortie</strong> : capital, rente, ou les deux. Il est aussi déblocable par anticipation pour l'achat de la résidence principale.")
  +BOX("⚠️ L'avantage fiscal à l'entrée se paie partiellement à la sortie. Le PER est surtout gagnant si votre tranche d'imposition baisse à la retraite. Voir notre <a href=\"/comparatifs/per-retraite.html\">comparatif PER</a>."),
 faq=[("Quel est l'avantage fiscal du PER ?","Les versements sont déductibles du revenu imposable dans certaines limites, réduisant l'impôt dès l'année du versement."),
      ("Peut-on récupérer son PER en capital ?","Oui, à la retraite la sortie peut se faire en capital, en rente, ou un mélange des deux."),
      ("Le PER est-il bloqué jusqu'à la retraite ?","En principe oui, sauf cas de déblocage anticipé comme l'achat de la résidence principale.")]),

# ---------- Long-tail "meilleur X pour Y" ----------
add(slug="meilleur-compte-pro-freelance",cat="compte-pro",
 title="Meilleur compte pro pour freelance et auto-entrepreneur (2026)",
 desc="Quel est le meilleur compte pro pour un freelance ou auto-entrepreneur en 2026 ? Critères, sélection (Qonto, Shine, Finom…) et conseils pour bien choisir.",
 h1="Meilleur compte pro pour freelance & auto-entrepreneur",
 lead="Un freelance n'a pas besoin du compte pro le plus complet, mais du plus adapté : simple, peu cher, avec les bons outils. Voici comment choisir.",
 body=H2("criteres","Les critères qui comptent pour un freelance")
  +UL(["<strong>Prix</strong> : un plan d'entrée suffit souvent au démarrage.",
       "<strong>Outils intégrés</strong> : facturation, suivi URSSAF, catégorisation des dépenses.",
       "<strong>Carte</strong> et virements adaptés à un faible volume.",
       "<strong>Simplicité</strong> d'ouverture et de gestion."])
  +H2("selection","Notre sélection")
  +UL(["<strong>Shine</strong> : pensé pour les indépendants, outils admin intégrés.",
       "<strong>Finom</strong> : plan gratuit et cashback, idéal pour démarrer.",
       "<strong>Qonto</strong> : la référence si vous voulez le plus complet et fiable."])
  +H2("rappel","Compte pro obligatoire ?")
  +P("En micro-entreprise, un <strong>compte dédié</strong> devient obligatoire au-delà de 10 000 € de CA pendant deux ans — pas forcément un « compte pro » payant. Détails dans notre <a href=\"/guides/compte-pro-obligatoire-micro-entreprise.html\">guide dédié</a>.")
  +BOX("💡 Comparez tout dans notre <a href=\"/comparatifs/comptes-pro.html\">comparatif des comptes pro</a> et notre <a href=\"/comparatifs/compte-pro-auto-entrepreneur.html\">sélection auto-entrepreneur</a>."),
 faq=[("Quel est le meilleur compte pro pour un freelance ?","Shine et Finom sont parfaits pour démarrer (simples, peu chers) ; Qonto pour le plus complet. Le bon choix dépend de votre volume d'activité."),
      ("Un auto-entrepreneur a-t-il besoin d'un compte pro ?","Un compte dédié devient obligatoire au-delà de 10 000 € de CA pendant deux ans, mais pas forcément un compte « pro » payant."),
      ("Combien coûte un compte pro pour freelance ?","De 0 € (offres d'entrée gratuites) à une quinzaine d'euros par mois selon les fonctions.")]),

add(slug="meilleure-carte-bancaire-voyage",cat="banque",
 title="Meilleure carte bancaire pour voyager à l'étranger (2026)",
 desc="Quelle est la meilleure carte bancaire pour voyager en 2026 ? Éviter les frais à l'étranger (paiement, retrait, change), sélection (N26, Revolut…) et conseils.",
 h1="Meilleure carte bancaire pour voyager à l'étranger",
 lead="Payer et retirer à l'étranger avec sa carte habituelle peut coûter cher en frais. Voici les cartes qui suppriment (presque) tous ces frais.",
 body=H2("frais","Les frais à traquer en voyage")
  +UL(["<strong>Frais de paiement</strong> hors zone euro (commission sur le change).",
       "<strong>Frais de retrait</strong> aux distributeurs étrangers.",
       "<strong>Taux de change</strong> appliqué (souvent défavorable chez les banques classiques)."])
  +H2("selection","Les meilleures cartes voyage")
  +UL(["<strong>N26</strong> et <strong>Revolut</strong> : paiements à l'étranger sans surcoût et change avantageux.",
       "Les néobanques multidevises permettent de détenir plusieurs devises.",
       "Vérifiez les <strong>plafonds de retrait gratuit</strong> selon la formule."])
  +H2("conseil","Le bon réflexe")
  +P("En voyage, payez toujours <strong>dans la devise locale</strong> (refusez la conversion proposée par le terminal, souvent défavorable).")
  +BOX("💡 Comparez dans notre <a href=\"/comparatifs/banque-en-ligne.html\">comparatif des banques en ligne</a>."),
 faq=[("Quelle carte pour voyager sans frais ?","N26 et Revolut sont des références : paiements à l'étranger sans surcoût et change avantageux. Vérifiez les plafonds de retrait gratuit."),
      ("Faut-il payer en euros ou en devise locale à l'étranger ?","Toujours en devise locale : la conversion proposée par le terminal (DCC) est généralement défavorable."),
      ("Les retraits à l'étranger sont-ils gratuits ?","Souvent gratuits jusqu'à un plafond selon la formule. Au-delà, des frais peuvent s'appliquer.")]),

add(slug="meilleur-courtier-pea",cat="bourse",
 title="Meilleur courtier pour un PEA en 2026 : comment choisir",
 desc="Quel est le meilleur courtier pour ouvrir un PEA en 2026 ? Frais d'ordre, droits de garde, ergonomie, sélection. Le guide pour choisir où ouvrir son PEA.",
 h1="Meilleur courtier pour un PEA : comment choisir",
 lead="Le PEA est l'enveloppe idéale pour investir en actions/ETF européens avec un avantage fiscal. Encore faut-il choisir le bon courtier.",
 body=H2("criteres","Ce qui compte pour un PEA")
  +UL(["<strong>Frais d'ordre</strong> bas (impact direct sur la performance).",
       "<strong>Absence de droits de garde</strong> idéalement.",
       "<strong>Éligibilité PEA</strong> et largeur de l'offre d'ETF/actions.",
       "<strong>Ergonomie</strong> et qualité de l'application."])
  +H2("selection","Les bons choix")
  +P("Plusieurs courtiers et banques en ligne proposent un PEA compétitif. Comparez les <strong>frais d'ordre</strong> et l'offre d'ETF éligibles. Voir notre <a href=\"/comparatifs/trading-bourse.html\">comparatif des courtiers</a> et notre guide <a href=\"/guides/pea-ou-compte-titres.html\">PEA ou compte-titres</a>.")
  +H2("rappel","Pourquoi le PEA ?")
  +P("Après 5 ans, les gains du PEA sont <strong>exonérés d'impôt sur le revenu</strong> (hors prélèvements sociaux) — un atout majeur pour l'investissement long terme.")
  +BOX("⚠️ Investir comporte un risque de perte en capital."),
 faq=[("Quel courtier choisir pour un PEA ?","Privilégiez des frais d'ordre bas, l'absence de droits de garde et une bonne offre d'ETF éligibles. Voir notre comparatif bourse."),
      ("Le PEA a-t-il des frais ?","Les frais varient selon le courtier : frais d'ordre, et parfois droits de garde (à éviter). Comparez avant d'ouvrir."),
      ("Quel est l'avantage fiscal du PEA ?","Après 5 ans, les gains sont exonérés d'impôt sur le revenu (les prélèvements sociaux restent dus).")]),

add(slug="meilleure-application-acheter-bitcoin",cat="crypto",
 title="Meilleure application pour acheter du Bitcoin en 2026",
 desc="Quelle est la meilleure application pour acheter du Bitcoin en 2026 ? Frais, sécurité, simplicité, sélection (Coinbase, Bitpanda, Kraken…). Le guide pour bien choisir.",
 h1="Meilleure application pour acheter du Bitcoin",
 lead="Acheter du Bitcoin demande une application fiable, sécurisée et pas trop chère. Voici comment choisir selon votre profil.",
 body=H2("criteres","Les critères de choix")
  +UL(["<strong>Frais</strong> : privilégiez l'interface pro et le virement SEPA (voir notre baromètre).",
       "<strong>Sécurité</strong> : 2FA, stockage à froid, réputation.",
       "<strong>Simplicité</strong> pour débuter, ou outils avancés pour aller plus loin.",
       "<strong>Régulation</strong> (statut PSAN en France)."])
  +H2("selection","Notre sélection")
  +UL(["<strong>Coinbase</strong> et <strong>Bitpanda</strong> : simples, rassurants pour débuter.",
       "<strong>Kraken</strong> : sécurité reconnue et frais bas via Kraken Pro.",
       "<strong>Bitstack</strong> : pour épargner en Bitcoin automatiquement."])
  +P("Comparez tout dans notre <a href=\"/comparatifs/crypto.html\">comparatif des applications crypto</a> et notre <a href=\"/etudes/barometre-frais-crypto.html\">baromètre des frais</a>.")
  +BOX("⚠️ Investir dans les crypto-actifs comporte un risque de perte en capital."),
 faq=[("Quelle est la meilleure app pour acheter du Bitcoin ?","Coinbase et Bitpanda pour la simplicité, Kraken pour la sécurité et les frais bas. Le meilleur dépend de votre profil."),
      ("Quel est le montant minimum pour acheter du Bitcoin ?","Très faible : vous pouvez acheter une fraction de Bitcoin et commencer avec quelques euros."),
      ("Faut-il sortir son Bitcoin de la plateforme ?","Pour de gros montants ou un horizon long, beaucoup transfèrent vers un portefeuille personnel (cold wallet).")])

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
print("batch 2 guides créés :", len(G))
for d in G: print("  guides/"+d['slug']+".html ("+d['cat']+")")
