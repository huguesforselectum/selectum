#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enrichit les comparatifs money strategiques : guide d'achat + FAQ (schema), maillage guides."""
import os, re, html, json
def UL(x): return "<ul>"+"".join(f"<li>{i}</li>" for i in x)+"</ul>"
def P(*x): return "".join(f"<p>{p}</p>" for p in x)

# slug : (label, intro, criteres[], pour_qui, erreurs[], faq[(q,a)], guides_lies[(url,txt)])
C={
 "crypto":("application crypto",
  "Choisir une application crypto, c'est arbitrer entre frais, sécurité, simplicité et choix d'actifs. Voici les critères qui comptent vraiment et comment éviter les pièges du débutant.",
  ["<strong>Les frais réels</strong> : comparez l'achat « instantané » (cher, spread inclus) et l'interface pro/advanced (frais maker/taker dégressifs). Le mode d'achat pèse plus que le bonus de bienvenue.",
   "<strong>La sécurité</strong> : double authentification (2FA), stockage à froid (cold storage), preuve de réserves, ancienneté de l'acteur.",
   "<strong>La régulation</strong> : statut PSAN (enregistrement AMF) pour les acteurs opérant en France.",
   "<strong>Le choix d'actifs</strong> et les fonctionnalités (staking, épargne programmée, carte)."],
  "les débutants privilégieront la simplicité (Coinbase, Bitpanda) ; les profils actifs viseront des frais bas (Kraken, Binance) ; ceux qui veulent un acteur français régulé regarderont Coinhouse",
  ["Acheter par carte bancaire (le mode le plus cher) au lieu du virement SEPA","Rester sur l'interface « instantanée » au lieu de l'interface pro","Laisser de gros montants sur la plateforme sans portefeuille personnel","Négliger la 2FA"],
  [("Quelle est la meilleure application crypto pour débuter ?","Coinbase et Bitpanda sont réputés simples et rassurants. Pour des frais plus bas, Kraken et Binance sont des références. Le bon choix dépend de votre niveau et de vos objectifs."),
   ("Comment réduire ses frais crypto ?","Utilisez l'interface pro/advanced, passez des ordres limites (maker) et alimentez votre compte par virement SEPA plutôt que par carte."),
   ("Faut-il sortir ses cryptos de la plateforme ?","Pour de gros montants ou un horizon long, beaucoup transfèrent vers un portefeuille personnel (cold wallet) pour ne pas dépendre d'un tiers.")],
  [("/guides/comment-acheter-cryptomonnaies.html","Comment acheter des cryptomonnaies"),("/etudes/barometre-frais-crypto.html","Baromètre des frais crypto"),("/guides/hot-wallet-ou-cold-wallet.html","Hot ou cold wallet ?")]),
 "banque-en-ligne":("banque en ligne",
  "Une banque en ligne fait économiser des dizaines à des centaines d'euros par an de frais, tout en offrant une appli moderne. Voici comment choisir celle qui colle à votre profil.",
  ["<strong>Les frais</strong> : tenue de compte, carte, paiements et retraits à l'étranger.","<strong>Les conditions</strong> : revenus minimums ou usage minimum pour la gratuité.","<strong>La gamme</strong> : épargne (livrets, assurance-vie), voire crédit immobilier pour les banques complètes.","<strong>La prime de bienvenue</strong>, appréciable mais secondaire face aux frais récurrents."],
  "une néobanque (N26, Revolut) convient pour le quotidien et l'international ; une banque en ligne complète (BoursoBank) pour une banque principale avec épargne et crédit",
  ["Choisir uniquement pour la prime de bienvenue","Ignorer les conditions de gratuité (usage/revenus)","Oublier de vérifier le dépôt d'espèces si vous en avez besoin"],
  [("Quelle est la banque en ligne la moins chère ?","Cela dépend de votre usage. Les néobanques (N26, Revolut) offrent une carte gratuite sans condition ; BoursoBank est très complète avec des frais réduits."),
   ("Une banque en ligne peut-elle être mon compte principal ?","Oui pour la plupart des usages. Vérifiez le dépôt d'espèces et la domiciliation de revenus si nécessaire."),
   ("Les banques en ligne sont-elles sûres ?","Les acteurs agréés offrent la garantie des dépôts comme les banques classiques.")],
  [("/guides/neobanque-ou-banque-traditionnelle.html","Néobanque ou banque traditionnelle ?"),("/guides/meilleure-carte-bancaire-gratuite.html","Meilleure carte gratuite"),("/guides/comment-changer-de-banque.html","Comment changer de banque")]),
 "comptes-pro":("compte pro",
  "Le bon compte pro dépend de votre statut et de votre volume d'activité. Voici les critères pour choisir sans payer pour des fonctions inutiles.",
  ["<strong>Le prix</strong> et les quotas (virements, encaissements) hors forfait.","<strong>Les outils</strong> : facturation, gestion des dépenses, compta, dépôt de capital.","<strong>Le statut</strong> : micro-entreprise (compte dédié suffisant) ou société (compte pro requis).","<strong>La carte</strong> et les plafonds adaptés."],
  "un indépendant qui démarre se contentera d'une offre d'entrée (Shine, Finom) ; une société choisira un acteur complet (Qonto) ; les gros besoins de cartes regarderont des solutions dédiées",
  ["Payer pour des fonctions avancées inutiles au démarrage","Sous-estimer les frais hors forfait (virements supplémentaires)","Confondre compte dédié (micro) et compte pro obligatoire (société)"],
  [("Quel est le meilleur compte pro ?","Qonto est la référence complète ; Shine et Finom sont parfaits pour démarrer à moindre coût. Le choix dépend de votre volume et de vos besoins."),
   ("Un compte pro est-il obligatoire ?","Pour une société, oui dès la création. En micro-entreprise, un compte dédié devient obligatoire au-delà de 10 000 € de CA pendant deux ans."),
   ("Existe-t-il un compte pro gratuit ?","Des offres d'entrée à 0 €/mois existent (Shine, Finom), avec des quotas limités.")],
  [("/guides/meilleur-compte-pro-freelance.html","Meilleur compte pro freelance"),("/guides/compte-pro-obligatoire-micro-entreprise.html","Compte pro obligatoire en micro ?"),("/guides/compte-pro-gratuit.html","Compte pro gratuit ?")]),
 "trading-bourse":("courtier en bourse",
  "Le courtier idéal dépend de votre enveloppe (PEA ou CTO) et de votre style d'investissement. Voici comment choisir pour investir au meilleur coût.",
  ["<strong>Les frais d'ordre</strong> et l'absence de droits de garde.","<strong>L'éligibilité PEA</strong> et l'accès aux ETF.","<strong>Les fonctionnalités</strong> : plans d'épargne programmés, fractions d'actions.","<strong>L'ergonomie</strong> et la pédagogie de l'application."],
  "un débutant privilégiera la simplicité et le PEA (Trade Republic, XTB) ; un investisseur actif visera un courtier complet et low-cost (DEGIRO, Interactive Brokers)",
  ["Se focaliser sur le bonus plutôt que sur les frais d'ordre","Choisir un courtier sans PEA alors qu'on investit en actions européennes","Négliger la fiscalité de l'enveloppe (CTO vs PEA)"],
  [("Quel est le meilleur courtier en bourse ?","Trade Republic et XTB pour débuter simplement, DEGIRO et Interactive Brokers pour les profils actifs. Comparez les frais d'ordre et l'éligibilité PEA."),
   ("PEA ou compte-titres ?","Le PEA offre un avantage fiscal après 5 ans (actions/ETF européens) ; le CTO est plus flexible (marchés mondiaux)."),
   ("Combien faut-il pour commencer ?","Quelques dizaines d'euros suffisent grâce aux ETF et aux courtiers sans minimum élevé.")],
  [("/guides/comment-investir-en-bourse-debutant.html","Comment investir en bourse"),("/guides/pea-ou-compte-titres.html","PEA ou compte-titres ?"),("/guides/comment-choisir-un-etf.html","Comment choisir un ETF")]),
 "assurance-vie":("assurance-vie",
  "L'assurance-vie est l'enveloppe reine de l'épargne française. Le bon contrat se reconnaît à ses frais et à la qualité de ses supports.",
  ["<strong>0 % de frais d'entrée</strong> et de versement.","<strong>Frais de gestion bas</strong> sur les unités de compte.","<strong>La qualité du fonds euros</strong> et le choix de supports (ETF, SCPI).","<strong>Gestion libre ou pilotée</strong> selon votre autonomie."],
  "les autonomes choisiront un contrat en gestion libre à frais bas (Linxea) ; ceux qui veulent être accompagnés opteront pour la gestion pilotée (Nalo, Yomoni)",
  ["Souscrire un contrat avec frais d'entrée (jusqu'à 5 % perdus)","Négliger les frais de gestion qui rognent la performance sur 20 ans","Oublier de prendre date tôt pour lancer le compteur des 8 ans"],
  [("Quelle est la meilleure assurance-vie ?","Un contrat à 0 % de frais d'entrée et frais de gestion bas : Linxea en gestion libre, Nalo/Yomoni en gestion pilotée."),
   ("Faut-il prendre date sur une assurance-vie ?","Oui : l'antériorité fiscale court dès l'ouverture. Ouvrir tôt, même avec peu, est malin."),
   ("Fonds euros ou unités de compte ?","Le fonds euros sécurise, les UC visent plus de rendement avec un risque. L'idéal est un mix selon l'horizon.")],
  [("/guides/meilleure-assurance-vie-debutant.html","Meilleure assurance-vie pour débuter"),("/guides/fonds-euros-vs-unites-de-compte.html","Fonds euros ou UC ?"),("/guides/comment-placer-10000-euros.html","Comment placer 10 000 €")]),
 "hebergement-web":("hébergeur web",
  "L'hébergement web est l'un des secteurs aux prix d'appel les plus agressifs. Le piège ? Le prix de renouvellement. Voici comment choisir.",
  ["<strong>La performance</strong> (SSD/NVMe, cache, PHP récent).","<strong>Le prix de renouvellement</strong>, souvent bien plus élevé que la 1re année.","<strong>Le support</strong>, idéalement en français.","<strong>Les ressources</strong> et la compatibilité WordPress/e-commerce."],
  "un débutant prendra un mutualisé performant ; o2switch séduit par son tarif unique stable ; pour un gros trafic, visez un VPS ou un hébergement infogéré",
  ["Se fier au seul prix d'appel sans regarder le renouvellement","Sous-dimensionner pour un site e-commerce","Oublier les sauvegardes et le SSL"],
  [("Quel est le meilleur hébergeur web ?","Hostinger et IONOS sur le prix d'appel, o2switch pour un tarif stable, OVHcloud pour le VPS. Comparez le coût total sur 3 ans."),
   ("Le prix d'appel est-il le vrai prix ?","Pas toujours : beaucoup renouvellent plus cher. Raisonnez en coût total sur la durée."),
   ("Quel hébergement pour WordPress ?","Un bon mutualisé avec installation 1 clic suffit pour débuter ; l'infogéré apporte performance et tranquillité.")],
  [("/guides/comment-creer-un-site-internet.html","Comment créer un site internet"),("/guides/hebergement-wordpress-pas-cher.html","Hébergement WordPress pas cher"),("/etudes/classement-hebergeurs-moins-chers.html","Classement des hébergeurs les moins chers")]),
 "vpn":("VPN",
  "Un VPN protège votre vie privée et sécurise votre connexion. Le bon choix se joue sur la vitesse, la politique de logs et le prix sur engagement long.",
  ["<strong>La politique no-log</strong> et la juridiction.","<strong>La vitesse</strong> et le nombre de serveurs (important pour le streaming).","<strong>Le prix</strong> : les grosses réductions ne valent que sur 1-2 ans.","<strong>Les appareils</strong> couverts et les outils annexes."],
  "ExpressVPN pour la performance premium, NordVPN pour le tout-en-un, Surfshark pour le meilleur rapport qualité/prix (appareils illimités)",
  ["Choisir un VPN gratuit (souvent financé par la revente de données)","S'abonner au mensuel (cher) au lieu de l'engagement long","Oublier le prix de renouvellement"],
  [("Quel est le meilleur VPN ?","ExpressVPN, NordVPN et Surfshark sont des références. Le meilleur dépend de votre usage et de votre budget."),
   ("Un VPN gratuit est-il fiable ?","Rarement pour un usage sérieux : beaucoup se financent par la revente de données."),
   ("Un VPN ralentit-il la connexion ?","Un peu, car le trafic est chiffré ; les bons VPN limitent fortement cette perte.")],
  [("/guides/a-quoi-sert-un-vpn.html","À quoi sert un VPN"),("/guides/meilleur-vpn-pas-cher.html","Meilleur VPN pas cher"),("/guides/comment-securiser-son-compte-en-ligne.html","Sécuriser ses comptes en ligne")]),
 "terminaux-paiement":("terminal de paiement",
  "Le bon TPE dépend surtout de votre volume d'encaissement. Voici comment arbitrer entre lecteur sans abonnement et tarif fixe.",
  ["<strong>Les commissions</strong> par transaction.","<strong>L'abonnement</strong> éventuel (rentable à fort volume).","<strong>Le versement</strong> (délai, instantané) et le matériel.","<strong>La compatibilité</strong> avec votre activité (mobile, boutique)."],
  "les petits volumes privilégieront le sans-abonnement (SumUp) ; les forts volumes un tarif fixe (Flatpay) ; le versement instantané intéressera ceux qui ont besoin de trésorerie",
  ["Payer un abonnement inutile pour un petit volume","Ne regarder que la commission sans le matériel amorti","Oublier de comparer le coût réel selon votre CA carte"],
  [("Quel est le meilleur terminal de paiement ?","SumUp pour les petits volumes (sans abonnement), Flatpay à fort volume (tarif fixe), myPOS pour le versement instantané."),
   ("Faut-il un abonnement pour un TPE ?","Pas forcément : le sans-abonnement est imbattable à faible volume ; l'abonnement devient rentable au-delà d'un certain CA."),
   ("Comment calculer le coût réel d'un TPE ?","Additionnez commissions, abonnement et matériel amorti. Notre calculateur le fait pour votre CA carte.")],
  [("/outils/calculateur-cout-tpe.html","Calculateur coût TPE"),("/comparatifs/tpe-petit-commerce.html","TPE pour petit commerce"),("/comparatifs/tpe-micro-entreprise.html","TPE micro-entreprise")]),
 "credit-conso":("crédit à la consommation",
  "Un crédit conso se compare sur un seul chiffre : le TAEG. Voici comment emprunter au meilleur coût sans mauvaise surprise.",
  ["<strong>Le TAEG</strong> (taux annuel effectif global), qui inclut tous les frais.","<strong>Le coût total</strong> du crédit, pas seulement la mensualité.","<strong>La durée</strong> adaptée à votre capacité de remboursement.","<strong>Le type</strong> : prêt personnel, affecté ou renouvelable (à éviter)."],
  "un projet précis (auto, travaux) appelle un crédit affecté ; un besoin libre, un prêt personnel ; évitez le crédit renouvelable, plus cher",
  ["Comparer le taux nominal au lieu du TAEG","S'endetter au-delà d'un taux d'endettement raisonnable","Souscrire un crédit renouvelable pour un besoin ponctuel"],
  [("Quel est le meilleur crédit conso ?","Celui au TAEG le plus bas pour votre profil. Comparez toujours le coût total, pas seulement la mensualité."),
   ("Peut-on annuler un crédit après signature ?","Oui, un délai légal de rétractation de 14 jours s'applique."),
   ("Quel taux d'endettement ne pas dépasser ?","Environ 35 % est un repère de prudence, variable selon les situations.")],
  [("/guides/comment-obtenir-credit-consommation.html","Comment obtenir un crédit conso"),("/guides/credit-auto-ou-loa.html","Crédit auto ou LOA ?"),("/guides/rachat-de-credit-comment-ca-marche.html","Rachat de crédit")]),
 "assurance-auto":("assurance auto",
  "L'assurance auto se compare à garanties équivalentes, pas seulement au prix. Et grâce à la loi Hamon, changer est devenu très simple.",
  ["<strong>La formule</strong> : au tiers, intermédiaire ou tous risques selon la valeur du véhicule.","<strong>Les garanties</strong> et les franchises.","<strong>Le prix</strong> à garanties comparables.","<strong>La gestion des sinistres</strong> et l'assistance."],
  "au tiers pour une voiture ancienne ou peu chère ; tous risques pour un véhicule récent ou de valeur ; les jeunes conducteurs viseront les formules au kilomètre",
  ["Comparer le prix sans regarder les garanties","Rester par inertie chez le même assureur","Sur-assurer une vieille voiture"],
  [("Comment payer moins cher son assurance auto ?","Comparez chaque année à garanties équivalentes et profitez de la loi Hamon pour changer sans frais après un an."),
   ("Tiers ou tous risques ?","Au tiers pour un véhicule ancien ou peu cher ; tous risques pour une voiture récente ou de valeur."),
   ("Comment changer d'assurance auto ?","Après un an, la loi Hamon permet de résilier à tout moment ; le nouvel assureur s'occupe des démarches.")],
  [("/guides/comment-changer-assurance-auto.html","Comment changer d'assurance auto"),("/guides/meilleure-assurance-jeune-conducteur.html","Assurance jeune conducteur"),("/guides/meilleure-assurance-moto.html","Meilleure assurance moto")]),
 "per-retraite":("PER",
  "Le PER combine un avantage fiscal à l'entrée et une liberté de sortie. Le bon plan se reconnaît à ses frais bas et ses bons supports.",
  ["<strong>0 % de frais d'entrée</strong> et de versement.","<strong>Frais de gestion bas</strong> et large choix d'ETF.","<strong>La qualité du fonds euros</strong>.","<strong>Gestion libre ou pilotée</strong>."],
  "le PER est surtout intéressant pour les contribuables fortement imposés ; les autonomes choisiront un PER en gestion libre à frais bas",
  ["Souscrire un PER avec frais d'entrée","Oublier que l'avantage fiscal à l'entrée se paie partiellement à la sortie","Bloquer une épargne dont on aura besoin avant la retraite"],
  [("Quel est le meilleur PER ?","Un PER à 0 % de frais d'entrée et frais de gestion bas (Linxea, Yomoni, Nalo). Le choix dépend de votre fiscalité."),
   ("Le PER est-il intéressant pour tout le monde ?","Surtout pour les contribuables fortement imposés. Moins pertinent si votre tranche est faible."),
   ("Peut-on récupérer son PER en capital ?","Oui, à la retraite la sortie peut se faire en capital, en rente, ou un mélange.")],
  [("/guides/per-comment-preparer-retraite.html","PER : préparer sa retraite"),("/guides/meilleur-per.html","Meilleur PER"),("/guides/per-ou-assurance-vie.html","PER ou assurance-vie ?")]),
 "transfert-argent":("service de transfert d'argent",
  "Pour envoyer de l'argent à l'étranger, le vrai coût se cache souvent dans le taux de change. Voici comment payer le moins cher.",
  ["<strong>Le taux de change</strong> appliqué (la marge cachée).","<strong>Les frais</strong> affichés.","<strong>Le montant réellement reçu</strong> par le destinataire.","<strong>Le délai</strong> et les pays couverts."],
  "Wise pour le taux réel et la transparence ; les apps spécialisées pour les petits montants réguliers vers certaines zones ; évitez les banques classiques",
  ["Se fier au « 0 frais » sans regarder le taux de change","Comparer les frais sans comparer le montant reçu","Utiliser sa banque classique (souvent la plus chère)"],
  [("Quel est le moins cher pour envoyer de l'argent à l'étranger ?","Les spécialistes comme Wise appliquent le taux réel avec une commission transparente, généralement moins cher qu'une banque."),
   ("Pourquoi « 0 frais » n'est pas gratuit ?","Parce que la marge peut être cachée dans un taux de change défavorable. Comparez le montant reçu."),
   ("Combien de temps prend un transfert ?","De quelques minutes à quelques jours selon le service et le pays.")],
  [("/guides/envoyer-argent-etranger-meilleur-taux.html","Envoyer de l'argent au meilleur taux"),("/comparatifs/change-multidevises.html","Change multi-devises"),("/code-promo/wise.html","Code promo Wise")]),
}

def faqld(faq):
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)

done=0
for slug,(label,intro,crit,pour,err,faq,guides) in C.items():
    f=f"comparatifs/{slug}.html"
    if not os.path.exists(f): print("absent:",slug); continue
    t=open(f,encoding="utf-8").read()
    if 'guide-achat-enrichi' in t: continue
    n=html.escape(label)
    faqh="".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)
    gl="".join(f'<a href="{u}" class="rel-chip">{html.escape(x)} →</a>' for u,x in guides)
    block=(f'<div class="container-article" data-pop="guide-achat-enrichi" style="max-width:920px;margin:0 auto;"><div class="article-body">'
        f'<h2 id="guide-achat">Comment choisir {n} en 2026 ?</h2>'
        f'<p>{html.escape(intro)}</p>'
        f'<h3>Les critères qui comptent</h3>{UL(crit)}'
        f'<h3>Pour qui ?</h3><p>Concrètement, {html.escape(pour)}.</p>'
        f'<h3>Les erreurs à éviter</h3>{UL(err)}'
        f'<div class="faq" style="margin-top:18px;"><h2>❓ Questions fréquentes</h2>{faqh}</div>'
        f'<div class="rel-links"><h2>📚 Guides utiles</h2><div class="rel-list">{gl}</div></div>'
        f'</div></div>\n')
    # injecter avant la 1re rel-links existante, sinon avant footer
    if '<div class="rel-links">' in t:
        t=t.replace('<div class="rel-links">', block+'<div class="rel-links">',1)
    elif '<footer class="footer">' in t:
        t=t.replace('<footer class="footer">', block+'<footer class="footer">',1)
    else:
        continue
    # ajouter FAQPage schema si absent
    if 'FAQPage' not in t:
        t=t.replace('</head>', f'<script type="application/ld+json">{faqld(faq)}</script>\n</head>',1)
    open(f,"w",encoding="utf-8").write(t); done+=1
    print(f"enrichi: {slug} (+{len(' '.join(crit+err+[intro,pour])).split().__len__() if False else 0})")
print("comparatifs enrichis:",done)
