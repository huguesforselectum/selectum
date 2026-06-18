#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, html, json
def UL(x): return "<ul>"+"".join(f"<li>{i}</li>" for i in x)+"</ul>"
C={
 "mutuelle-sante":("mutuelle santé",
  "La meilleure mutuelle est celle qui colle à VOS besoins, pas la plus chère ni la moins chère. Voici comment choisir intelligemment.",
  ["<strong>Vos postes de dépenses</strong> : optique, dentaire, hospitalisation, médecines douces.","<strong>Les niveaux de remboursement</strong> (% base Sécu ou forfaits €).","<strong>Le reste à charge</strong> sur les postes qui vous concernent.","<strong>Délais de carence</strong> et plafonds annuels."],
  "adaptez la couverture à votre profil (jeune actif, famille, senior) et réévaluez quand votre situation change",
  ["Surpayer des garanties inutiles","Choisir uniquement sur le prix","Ignorer les délais de carence"],
  [("Comment choisir sa mutuelle santé ?","Partez de vos besoins réels (optique, dentaire, hospitalisation) plutôt que d'une couverture maximale, et comparez le reste à charge."),
   ("Peut-on changer de mutuelle facilement ?","Oui, la résiliation infra-annuelle permet de changer après un an, sans frais."),
   ("Comment payer moins cher sa mutuelle ?","En ajustant les garanties à vos besoins et en comparant régulièrement.")],
  [("/guides/comment-choisir-mutuelle-sante.html","Comment choisir sa mutuelle"),("/guides/comment-resilier-mutuelle.html","Comment résilier sa mutuelle")]),
 "assurance-habitation":("assurance habitation",
  "Obligatoire pour les locataires, l'assurance habitation se compare à garanties équivalentes. Voici les critères clés.",
  ["<strong>Responsabilité civile</strong> et risques locatifs (dégât des eaux, incendie).","<strong>Vol et dommages</strong> selon la valeur de vos biens.","<strong>Le prix</strong> adapté à la surface.","<strong>Franchises et plafonds</strong>."],
  "adaptez aux petites surfaces pour payer moins ; en colocation, vérifiez si un contrat unique couvre tout le monde",
  ["Sous-estimer la valeur de ses biens","Comparer le prix sans les garanties","Oublier de résilier l'ancien contrat"],
  [("L'assurance habitation est-elle obligatoire ?","Oui pour les locataires (y compris résidence étudiante) et en copropriété ; conseillée pour les propriétaires."),
   ("Comment payer moins cher ?","Adaptez les garanties à votre logement et comparez chaque année."),
   ("Comment résilier son assurance habitation ?","Après un an, la loi Hamon permet de résilier à tout moment.")],
  [("/guides/comment-resilier-assurance-habitation.html","Résilier son assurance habitation"),("/guides/meilleure-assurance-habitation-etudiant.html","Assurance habitation étudiant")]),
 "fournisseur-energie":("fournisseur d'énergie",
  "Changer de fournisseur est gratuit, sans coupure et sans engagement. Voici comment choisir une offre moins chère, voire verte.",
  ["<strong>Le prix du kWh</strong> et de l'abonnement.","<strong>Le type d'offre</strong> : prix fixe, indexé ou vert.","<strong>Le service client</strong>.","<strong>Les conditions</strong> et la transparence."],
  "le prix fixe sécurise, l'indexé suit le marché, le vert soutient les renouvelables — certaines offres vertes sont parmi les moins chères",
  ["Rester au tarif réglementé par inertie","Ne regarder que l'abonnement sans le prix du kWh","Croire qu'un changement coupe l'électricité (faux)"],
  [("Quel est le fournisseur d'énergie le moins cher ?","Cela dépend de votre consommation. Comparez le prix du kWh et de l'abonnement pour votre profil."),
   ("Changer de fournisseur coupe-t-il l'électricité ?","Non, jamais : le réseau reste le même, seul le fournisseur change."),
   ("Les offres vertes sont-elles plus chères ?","Pas forcément : certaines sont parmi les moins chères du marché.")],
  [("/guides/comment-changer-fournisseur-energie.html","Comment changer de fournisseur"),("/guides/comment-reduire-facture-energie.html","Réduire sa facture d'énergie")]),
 "assurance-animaux":("assurance pour animaux",
  "Une mutuelle animale rembourse les frais vétérinaires. Voici comment choisir la bonne formule pour votre chien ou chat.",
  ["<strong>Le taux de remboursement</strong> et le plafond annuel.","<strong>Les exclusions</strong> et délais de carence.","<strong>La franchise</strong>.","<strong>Le prix</strong> selon l'espèce, la race et l'âge."],
  "anticipez les gros frais vétérinaires ; pour un animal âgé ou une race à exclusions, étudiez de près le rapport prix/garanties",
  ["Comparer le prix sans les plafonds et exclusions","Attendre que l'animal soit malade pour souscrire","Ignorer le délai de carence"],
  [("L'assurance animaux est-elle utile ?","Elle protège des grosses dépenses vétérinaires imprévues, selon l'âge et la race de l'animal."),
   ("Combien coûte une assurance chien ou chat ?","De quelques euros à plus de 50 €/mois selon la formule, l'espèce, la race et l'âge."),
   ("Y a-t-il un délai de carence ?","Oui, la plupart des contrats en appliquent un avant la prise en charge.")],
  []),
 "crowdlending-p2p":("plateforme de crowdlending",
  "Le crowdlending vise un rendement supérieur aux livrets, au prix d'un risque réel. Voici comment choisir une plateforme.",
  ["<strong>L'ancienneté</strong> et la régulation.","<strong>Le type de prêts</strong> (conso, immobilier, entreprises).","<strong>Les garanties de rachat</strong> et l'historique de défauts.","<strong>La diversification</strong> possible."],
  "réservé aux investisseurs avertis cherchant du rendement ; diversifiez sur plusieurs plateformes et types de prêts",
  ["Investir une part trop importante de son épargne","Négliger le risque de défaut et la liquidité limitée","Se fier au seul rendement affiché"],
  [("Le crowdlending est-il risqué ?","Oui : risque de perte en capital, de défaut et liquidité limitée. Diversifiez et n'investissez qu'une part mesurée."),
   ("Quel rendement espérer ?","Souvent de 5 % à plus de 12 % annoncés, sans garantie. Le rendement réel dépend des défauts."),
   ("Comment choisir une plateforme ?","Regardez l'ancienneté, la régulation, les garanties de rachat et l'historique.")],
  [("/comparatifs/assurance-vie.html","Comparatif assurance-vie"),("/guides/comment-investir-dans-immobilier.html","Comment investir dans l'immobilier")]),
 "forfait-mobile":("forfait mobile",
  "Les forfaits low-cost se livrent une vraie bataille. Voici comment choisir le bon rapport data/prix.",
  ["<strong>L'enveloppe data</strong> adaptée à votre usage.","<strong>Le prix</strong> et sa stabilité après promo.","<strong>Le réseau</strong> hôte (couverture).","<strong>Sans engagement</strong> pour profiter des promos."],
  "estimez votre consommation data réelle ; privilégiez le sans engagement pour changer dès qu'une meilleure offre apparaît",
  ["Prendre trop de data inutilisée","Oublier la hausse de prix après la promo","Négliger la couverture réseau"],
  [("Quel est le forfait mobile le moins cher ?","Les offres low-cost démarrent à quelques euros. Le bon choix dépend de votre data et de la couverture."),
   ("Forfait avec ou sans engagement ?","Sans engagement de préférence, pour changer librement et profiter des promotions."),
   ("Peut-on garder son numéro ?","Oui, via la portabilité avec votre code RIO.")],
  []),
 "esim-voyage":("eSIM de voyage",
  "Une eSIM de voyage offre de la data à l'étranger sans carte physique ni frais d'itinérance. Voici comment choisir.",
  ["<strong>La couverture</strong> (pays ou zone).","<strong>Le prix</strong> du Go et les forfaits.","<strong>La compatibilité</strong> eSIM de votre téléphone.","<strong>La facilité</strong> d'activation."],
  "idéale pour les voyageurs ; vérifiez d'abord que votre téléphone est compatible eSIM",
  ["Acheter sans vérifier la compatibilité eSIM","Choisir une offre data sans couverture du bon pays","Attendre les appels/SMS (souvent non inclus)"],
  [("Comment fonctionne une eSIM de voyage ?","Vous achetez un forfait data pour un pays ou une zone, puis activez l'eSIM via un QR code, sans carte physique."),
   ("Mon téléphone est-il compatible eSIM ?","La plupart des smartphones récents le sont (iPhone XS+, Pixel, Galaxy récents)."),
   ("L'eSIM inclut-elle les appels ?","La plupart des offres ne comprennent que la data ; les appels passent par des applications.")],
  []),
 "courtage-immobilier":("courtier immobilier",
  "Un courtier met les banques en concurrence pour obtenir le meilleur crédit immobilier. Voici comment bien le choisir.",
  ["<strong>Le réseau de banques</strong> partenaires.","<strong>Les frais de courtage</strong> et leur transparence.","<strong>L'accompagnement</strong> (montage du dossier, négociation).","<strong>La capacité à négocier l'assurance emprunteur</strong>."],
  "utile pour gagner du temps et obtenir de meilleures conditions, surtout pour un premier achat",
  ["Se focaliser sur le taux sans l'assurance emprunteur","Ne pas comparer plusieurs courtiers","Négliger le coût total du crédit"],
  [("Un courtier immobilier est-il utile ?","Souvent oui : il met les banques en concurrence et peut obtenir de meilleures conditions, y compris sur l'assurance."),
   ("Combien coûte un courtier immobilier ?","Des frais de courtage s'appliquent, parfois compensés par les économies obtenues. Vérifiez la transparence."),
   ("Comment obtenir le meilleur taux ?","Soignez votre profil (apport, finances), mettez les banques en concurrence et déléguez l'assurance emprunteur.")],
  [("/guides/meilleur-taux-credit-immobilier.html","Meilleur taux immobilier"),("/guides/comment-changer-assurance-emprunteur.html","Changer d'assurance emprunteur")]),
 "rachat-credit":("organisme de rachat de crédit",
  "Le rachat de crédit regroupe vos prêts en un seul, avec une mensualité plus basse. Voici comment choisir et éviter les pièges.",
  ["<strong>Le coût total</strong> (pas seulement la mensualité).","<strong>Les frais</strong> (dossier, garantie, indemnités).","<strong>La durée</strong> et son impact sur le coût.","<strong>La capacité à inclure</strong> conso et immobilier."],
  "pertinent quand le taux d'endettement est trop élevé ou pour simplifier sa gestion, mais à étudier au cas par cas",
  ["Ne regarder que la baisse de mensualité","Allonger excessivement la durée (coût total en hausse)","Oublier les frais annexes"],
  [("Le rachat de crédit fait-il baisser le coût total ?","Pas forcément : il baisse la mensualité en allongeant la durée, ce qui augmente souvent le coût total."),
   ("Peut-on inclure un crédit immobilier ?","Oui, certains rachats regroupent conso et immobilier, avec des conditions différentes."),
   ("Y a-t-il des frais ?","Oui : dossier, garantie, et parfois indemnités de remboursement anticipé.")],
  [("/guides/rachat-de-credit-comment-ca-marche.html","Rachat de crédit : comment ça marche")]),
 "epargne-pilotee":("gestion pilotée",
  "La gestion pilotée confie votre épargne à des experts, en ETF, selon votre profil. Idéal si vous ne voulez pas gérer vous-même.",
  ["<strong>Les frais de gestion</strong> (pilotée = un peu plus chère que la gestion libre).","<strong>La qualité de l'allocation</strong> (ETF, diversification).","<strong>L'enveloppe</strong> : assurance-vie, PER, PEA.","<strong>La personnalisation</strong> selon votre profil de risque."],
  "parfaite pour les épargnants qui veulent investir sans s'en occuper ; les autonomes préféreront la gestion libre, moins chère",
  ["Payer des frais élevés pour une allocation banale","Choisir un profil de risque inadapté à son horizon","Oublier que le capital n'est pas garanti sur les unités de compte"],
  [("Qu'est-ce que la gestion pilotée ?","Votre épargne est investie pour vous par des experts, en ETF, selon votre profil de risque."),
   ("Gestion pilotée ou libre ?","Pilotée si vous voulez être accompagné ; libre (moins chère) si vous êtes à l'aise pour choisir vos supports."),
   ("La gestion pilotée est-elle risquée ?","Elle investit en partie en unités de compte : il existe un risque de perte en capital, modulé selon le profil.")],
  [("/guides/meilleure-assurance-vie-debutant.html","Meilleure assurance-vie débutant"),("/comparatifs/assurance-vie.html","Comparatif assurance-vie")]),
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
print("comparatifs enrichis (lot 2):",done)
