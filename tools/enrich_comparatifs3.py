#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, html, json
def UL(x): return "<ul>"+"".join(f"<li>{i}</li>" for i in x)+"</ul>"
C={
 "assurance-emprunteur":("assurance emprunteur",
  "Grâce à la loi Lemoine, on peut changer d'assurance de prêt à tout moment et économiser des milliers d'euros. Voici comment choisir.",
  ["<strong>Le taux</strong> et le coût total sur la durée du prêt.","<strong>L'équivalence des garanties</strong> exigée par la banque.","<strong>Les garanties</strong> (décès, invalidité, incapacité) et exclusions.","<strong>La quotité</strong> assurée par emprunteur."],
  "tout emprunteur immobilier a intérêt à comparer la délégation d'assurance plutôt que l'offre groupée de sa banque",
  ["Garder l'assurance groupée de la banque sans comparer","Choisir sur le seul taux sans vérifier les garanties","Oublier que la substitution est possible à tout moment (loi Lemoine)"],
  [("Comment changer d'assurance emprunteur ?","À tout moment grâce à la loi Lemoine, sans frais, tant que les garanties restent équivalentes."),
   ("Combien peut-on économiser ?","Souvent plusieurs milliers d'euros sur la durée du prêt en déléguant à un assureur moins cher."),
   ("La banque peut-elle refuser ?","Seulement si les garanties ne sont pas équivalentes. Sinon, elle doit accepter la substitution.")],
  [("/guides/comment-changer-assurance-emprunteur.html","Changer d'assurance emprunteur"),("/guides/meilleur-taux-credit-immobilier.html","Meilleur taux immobilier")]),
 "change-multidevises":("service de change multi-devises",
  "Pour détenir et dépenser plusieurs devises, le bon service se reconnaît à son taux de change réel et sa transparence.",
  ["<strong>Le taux de change</strong> appliqué (proche du taux interbancaire).","<strong>Les frais</strong> de conversion et de retrait.","<strong>Les devises</strong> supportées.","<strong>La carte</strong> et les plafonds."],
  "idéal pour les voyageurs, expatriés et freelances payés en devises ; comparez le coût réel d'une conversion",
  ["Se fier au « 0 frais » sans regarder le taux","Payer en euros à l'étranger (conversion DCC défavorable)","Négliger les plafonds de retrait gratuit"],
  [("Quel est le meilleur service de change multi-devises ?","Les acteurs appliquant le taux réel (Wise, Revolut) avec une commission transparente sont souvent les plus avantageux."),
   ("Comment éviter les frais de change ?","Utiliser un compte multidevises au taux réel et payer toujours dans la devise locale à l'étranger."),
   ("Peut-on détenir plusieurs devises ?","Oui, les comptes multidevises permettent de conserver et convertir plusieurs monnaies.")],
  [("/guides/envoyer-argent-etranger-meilleur-taux.html","Envoyer de l'argent au meilleur taux"),("/comparatifs/transfert-argent.html","Comparatif transfert d'argent")]),
 "logiciels-comptabilite":("logiciel de comptabilité",
  "Le bon logiciel de compta dépend de votre statut et de votre besoin d'accompagnement. Voici les critères pour choisir.",
  ["<strong>La conformité</strong> (factures, FEC, TVA).","<strong>L'automatisation</strong> (rapprochement bancaire, OCR des justificatifs).","<strong>L'accompagnement</strong> : logiciel seul ou expert-comptable en ligne.","<strong>Le prix</strong> et l'intégration avec votre banque."],
  "un indépendant simple choisira un outil de facturation/compta léger ; une société préférera un expert-comptable en ligne (Dougs, Keobiz)",
  ["Choisir un outil trop complexe pour ses besoins","Négliger l'intégration bancaire","Oublier l'obligation de conformité (FEC)"],
  [("Quel logiciel de comptabilité choisir ?","Un outil léger (Abby, Freebe, Tiime) pour un indépendant simple ; un expert-comptable en ligne (Dougs, Keobiz) pour une société."),
   ("Faut-il un expert-comptable ?","Pas obligatoire en micro-entreprise, mais utile pour une société ou une compta complexe."),
   ("Ces logiciels sont-ils conformes ?","Les outils sérieux génèrent des documents conformes (factures, FEC). Vérifiez avant de souscrire.")],
  [("/comparatifs/facturation.html","Comparatif facturation"),("/guides/meilleur-logiciel-facturation-auto-entrepreneur.html","Logiciel facturation auto-entrepreneur")]),
 "facturation":("logiciel de facturation",
  "Un bon logiciel de facturation génère des factures conformes et fait gagner du temps. Voici comment choisir.",
  ["<strong>La conformité</strong> des factures (mentions légales).","<strong>Devis, relances</strong> et suivi des paiements.","<strong>Le suivi du chiffre d'affaires</strong>.","<strong>Le prix</strong> (parfois inclus dans un compte pro)."],
  "un auto-entrepreneur se contentera d'un outil simple (Abby, Freebe) ; certains comptes pros (Shine, Qonto) l'incluent",
  ["Émettre des factures non conformes","Payer pour des fonctions inutiles","Ne pas centraliser devis et factures"],
  [("Quel logiciel de facturation pour auto-entrepreneur ?","Des outils dédiés (Abby, Freebe, Tiime) ou un compte pro avec facturation intégrée (Shine, Qonto)."),
   ("La facturation conforme est-elle obligatoire ?","Oui, vos factures doivent comporter les mentions légales. Un logiciel les génère automatiquement."),
   ("Existe-t-il des logiciels gratuits ?","Certains comptes pros incluent la facturation gratuitement ; des outils ont des formules gratuites limitées.")],
  [("/guides/meilleur-logiciel-facturation-auto-entrepreneur.html","Logiciel facturation auto-entrepreneur"),("/comparatifs/comptes-pro.html","Comparatif comptes pro")]),
 "logiciels-crm":("logiciel CRM",
  "Un CRM centralise vos contacts et votre pipeline commercial. Le bon choix dépend de la taille de votre équipe et de vos besoins.",
  ["<strong>La simplicité</strong> de prise en main.","<strong>Les fonctionnalités</strong> (pipeline, automatisations, emailing).","<strong>Les intégrations</strong> avec vos outils.","<strong>Le prix</strong> par utilisateur."],
  "un indépendant ou une TPE choisira un CRM simple ; une équipe commerciale visera un outil complet avec automatisations",
  ["Choisir un CRM surdimensionné","Négliger l'adoption par l'équipe","Sous-estimer le coût par utilisateur"],
  [("Quel CRM choisir ?","Un CRM simple pour un indépendant/TPE, un outil complet (pipeline, automatisations) pour une équipe commerciale."),
   ("Un CRM est-il utile pour un indépendant ?","Oui, pour centraliser contacts et suivi commercial, même seul."),
   ("Existe-t-il des CRM gratuits ?","Plusieurs CRM proposent une formule gratuite limitée, suffisante pour démarrer.")],
  []),
 "formation":("plateforme de formation en ligne",
  "Se former en ligne est accessible et souvent finançable. Voici comment choisir la bonne plateforme.",
  ["<strong>Le catalogue</strong> et la qualité des cours.","<strong>Les certifications</strong> reconnues.","<strong>Le financement</strong> (CPF éventuel).","<strong>Le format</strong> (vidéo, mentorat, rythme)."],
  "particuliers en reconversion ou montée en compétences ; vérifiez l'éligibilité au financement selon la formation",
  ["Choisir une formation non reconnue","Négliger le format et l'accompagnement","Oublier les options de financement"],
  [("Quelle plateforme de formation en ligne choisir ?","Cela dépend de votre objectif : certification reconnue, montée en compétences ou découverte. Comparez catalogue et financement."),
   ("Les formations en ligne sont-elles finançables ?","Certaines sont éligibles au CPF ou à d'autres dispositifs ; vérifiez selon la formation."),
   ("Les certifications sont-elles reconnues ?","Cela dépend de la plateforme et du programme. Privilégiez les certifications reconnues dans votre secteur.")],
  []),
 "creer-boutique-en-ligne":("solution pour créer une boutique en ligne",
  "Lancer une boutique en ligne se fait via une solution tout-en-un (Shopify) ou WordPress + WooCommerce. Voici comment choisir.",
  ["<strong>La simplicité</strong> vs la flexibilité.","<strong>Le coût total</strong> (abonnement, thèmes, apps).","<strong>Les moyens de paiement</strong> et la gestion des stocks.","<strong>La scalabilité</strong> pour absorber la croissance."],
  "Shopify pour vendre vite et simplement ; WordPress + WooCommerce pour plus de flexibilité et un coût maîtrisé sur la durée",
  ["Sous-estimer le coût des apps additionnelles","Négliger la performance (impact sur les ventes)","Choisir une solution difficile à faire évoluer"],
  [("Shopify ou WooCommerce ?","Shopify pour la simplicité tout-en-un ; WooCommerce (WordPress) pour la flexibilité et l'économie sur la durée."),
   ("Combien coûte une boutique en ligne ?","De quelques euros par mois (WooCommerce + hébergement) à un abonnement mensuel pour Shopify, plus les apps."),
   ("Faut-il des compétences techniques ?","Non pour Shopify ; un peu d'apprentissage pour WooCommerce, mais accessible.")],
  [("/guides/comment-creer-un-site-internet.html","Comment créer un site internet"),("/guides/meilleur-hebergement-ecommerce.html","Meilleur hébergement e-commerce")]),
 "ecommerce":("plateforme e-commerce",
  "La plateforme e-commerce idéale dépend de votre volume et de votre besoin de personnalisation. Voici les critères clés.",
  ["<strong>La facilité</strong> de mise en place.","<strong>Les frais</strong> (abonnement + commissions éventuelles).","<strong>Les fonctionnalités</strong> (paiement, stocks, marketing).","<strong>La performance</strong> et la scalabilité."],
  "les débutants iront vers une solution clé en main ; les gros catalogues ou besoins spécifiques vers une solution plus ouverte",
  ["Choisir sur le seul prix d'appel","Négliger les commissions par vente","Sous-dimensionner pour la croissance"],
  [("Quelle plateforme e-commerce choisir ?","Une solution tout-en-un (Shopify) pour démarrer vite ; WooCommerce pour la flexibilité. Selon votre volume et vos besoins."),
   ("Combien coûte une plateforme e-commerce ?","Un abonnement mensuel plus d'éventuelles commissions et apps. Comparez le coût total."),
   ("Quelle solution pour un gros catalogue ?","Des plateformes plus ouvertes ou dédiées, capables d'absorber le volume et la complexité.")],
  [("/comparatifs/creer-boutique-en-ligne.html","Créer une boutique en ligne"),("/guides/meilleur-hebergement-ecommerce.html","Hébergement e-commerce")]),
 "cartes-famille":("carte bancaire pour ado",
  "Une carte pour ado permet d'apprendre à gérer son argent en sécurité. Voici comment choisir l'offre adaptée.",
  ["<strong>Le contrôle parental</strong> (plafonds, suivi en temps réel).","<strong>Les frais</strong> de l'offre.","<strong>L'âge minimum</strong> et l'accord parental.","<strong>Les fonctionnalités</strong> pédagogiques (cagnottes, objectifs)."],
  "parents souhaitant donner de l'autonomie à un ado tout en gardant un œil sur les dépenses",
  ["Choisir sans contrôle parental adapté","Négliger les frais mensuels","Donner une carte sans accompagnement pédagogique"],
  [("Quelle carte bancaire pour un ado ?","Des offres dédiées (Pixpay, Kard) avec contrôle parental et fonctions pédagogiques sont les plus adaptées."),
   ("À partir de quel âge ?","Souvent dès 10-12 ans avec accord parental, selon l'offre."),
   ("Les parents gardent-ils le contrôle ?","Oui : plafonds, blocage et suivi des dépenses en temps réel depuis une application.")],
  []),
 "kit-solaire-autoconsommation":("kit solaire en autoconsommation",
  "Un kit solaire plug-and-play réduit la facture d'électricité sans gros chantier. Voici comment choisir.",
  ["<strong>La puissance</strong> adaptée à votre consommation en journée.","<strong>La qualité</strong> des panneaux et de l'onduleur.","<strong>La facilité d'installation</strong> (plug-and-play).","<strong>Le rapport prix / production</strong> et l'amortissement."],
  "particuliers voulant autoconsommer une partie de leur électricité ; dimensionnez selon votre talon de consommation",
  ["Surdimensionner le kit par rapport à sa consommation diurne","Négliger l'orientation et l'ensoleillement","Oublier les démarches (déclaration en mairie)"],
  [("Un kit solaire est-il rentable ?","La rentabilité dépend de votre consommation, de l'ensoleillement et du prix de l'électricité ; l'amortissement se compte en années."),
   ("Quelle puissance choisir ?","Dimensionnez selon votre consommation en journée (le talon), pour autoconsommer un maximum."),
   ("Faut-il une autorisation ?","Une déclaration préalable est souvent nécessaire ; les kits plug-and-play simplifient les démarches.")],
  []),
 "courtier-etf":("courtier pour ETF",
  "Pour investir en ETF à frais bas, le choix du courtier est déterminant. Voici les critères qui comptent.",
  ["<strong>Les frais d'ordre</strong> (impact direct sur la performance).","<strong>L'éligibilité PEA</strong> et le choix d'ETF.","<strong>Les plans d'épargne programmés</strong> en ETF.","<strong>L'absence de droits de garde</strong>."],
  "un investisseur passif privilégiera un courtier à frais bas avec plans d'épargne (Trade Republic) ; un profil PEA visera un courtier éligible",
  ["Payer des frais d'ordre élevés sur de petits montants","Choisir un courtier sans PEA pour des ETF européens","Négliger les versements programmés"],
  [("Quel courtier pour acheter des ETF ?","Un courtier à frais d'ordre bas avec plans d'épargne (Trade Republic, XTB) ou un courtier PEA éligible. Comparez les frais."),
   ("Peut-on acheter des ETF dans un PEA ?","Oui, de nombreux ETF sont éligibles au PEA, avec l'avantage fiscal après 5 ans."),
   ("Quel ETF choisir ?","Un ETF World à frais bas est l'option la plus simple pour débuter, en cœur de portefeuille.")],
  [("/guides/comment-choisir-un-etf.html","Comment choisir un ETF"),("/guides/etf-vs-actions.html","ETF ou actions ?"),("/guides/meilleur-courtier-pea.html","Meilleur courtier PEA")]),
 "box-internet":("box internet",
  "La bonne box internet dépend de l'éligibilité de votre logement et de votre usage. Voici comment choisir.",
  ["<strong>L'éligibilité</strong> fibre/ADSL à votre adresse.","<strong>Le débit</strong> et la stabilité.","<strong>Le prix</strong> et son évolution après la promo.","<strong>Les options</strong> (TV, téléphone, engagement)."],
  "vérifiez d'abord votre éligibilité fibre ; privilégiez le sans engagement pour profiter des promotions",
  ["Souscrire sans vérifier l'éligibilité fibre","Oublier la hausse de prix après la première année","Payer pour des options TV inutiles"],
  [("Quelle box internet choisir ?","Cela dépend de votre éligibilité (fibre/ADSL) et de votre usage. Comparez débit, prix et engagement."),
   ("Comment vérifier son éligibilité fibre ?","Via un test d'éligibilité avec votre adresse sur le site des opérateurs."),
   ("Faut-il s'engager ?","Pas nécessairement : des offres sans engagement existent et permettent de changer librement.")],
  []),
}
def faqld(faq): return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)
done=0
for slug,(label,intro,crit,pour,err,faq,guides) in C.items():
    f=f"comparatifs/{slug}.html"
    if not os.path.exists(f): print("absent:",slug); continue
    t=open(f,encoding="utf-8").read()
    if 'guide-achat-enrichi' in t: continue
    n=html.escape(label)
    faqh="".join(f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)
    gl="".join(f'<a href="{u}" class="rel-chip">{html.escape(x)} →</a>' for u,x in guides)
    glblock=f'<div class="rel-links"><h2>📚 Guides utiles</h2><div class="rel-list">{gl}</div></div>' if gl else ''
    block=(f'<div class="container-article" data-pop="guide-achat-enrichi" style="max-width:920px;margin:0 auto;"><div class="article-body">'
        f'<h2 id="guide-achat">Comment choisir {n} en 2026 ?</h2><p>{html.escape(intro)}</p>'
        f'<h3>Les critères qui comptent</h3>{UL(crit)}'
        f'<h3>Pour qui ?</h3><p>Concrètement, {html.escape(pour)}.</p>'
        f'<h3>Les erreurs à éviter</h3>{UL(err)}'
        f'<div class="faq" style="margin-top:18px;"><h2>❓ Questions fréquentes</h2>{faqh}</div>{glblock}</div></div>\n')
    if '<div class="rel-links">' in t: t=t.replace('<div class="rel-links">', block+'<div class="rel-links">',1)
    elif '<footer class="footer">' in t: t=t.replace('<footer class="footer">', block+'<footer class="footer">',1)
    else: continue
    if 'FAQPage' not in t: t=t.replace('</head>', f'<script type="application/ld+json">{faqld(faq)}</script>\n</head>',1)
    open(f,"w",encoding="utf-8").write(t); done+=1
print("comparatifs enrichis (lot 3):",done)
