#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Articles d'actualité éditoriaux sur l'épargne des Français -> actualites/."""
import os, html, json
DATE="2026-06-11"; PUB="2026-06-09"
FONT="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"

def P(*ps): return "".join(f"<p>{x}</p>" for x in ps)
def H2(t): return f"<h2>{t}</h2>"
def UL(items): return "<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"
def OL(items): return "<ol>"+"".join(f"<li>{i}</li>" for i in items)+"</ol>"
def BOX(t): return f'<div class="highlight-box"><p>{t}</p></div>'

ART=[]
def add(**k): ART.append(k)

add(slug="livret-a-taux-2026",cat_link="/comparatifs/assurance-vie.html",cat_label="comparatif assurance-vie",
 title="Taux du Livret A en 2026 : ce qui change pour votre épargne",
 desc="Taux du Livret A 2026 : comment il est calculé, ce que ça change pour les épargnants et les alternatives plus rémunératrices. Notre décryptage.",
 h1="Taux du Livret A en 2026 : ce qui change pour votre épargne",
 lead="Placement préféré des Français, le Livret A reste un pilier de l'épargne de précaution. Mais avec un taux sous pression, faut-il revoir sa stratégie en 2026 ?",
 body=H2("Comment est fixé le taux du Livret A")
  +P("Le taux du Livret A n'est pas décidé au hasard : il suit une <strong>formule de calcul</strong> qui tient compte de "
     "l'inflation et des taux monétaires de court terme. Il est révisé périodiquement par les pouvoirs publics, qui peuvent "
     "lisser les variations pour protéger les épargnants comme le financement du logement social.")
  +P("Conséquence concrète : quand l'inflation reflue, le taux du Livret A a tendance à <strong>baisser</strong> à son tour. "
     "C'est précisément le mouvement qui inquiète une partie des 55 millions de détenteurs en France.")
  +H2("Ce que ça change pour les épargnants")
  +UL(["Le Livret A reste <strong>100 % garanti, liquide et défiscalisé</strong> : parfait pour l'épargne de précaution.",
       "Son rendement réel peut devenir <strong>faible voire négatif</strong> si l'inflation repart.",
       "Le <strong>plafond de 22 950 €</strong> atteint, l'argent supplémentaire dort sans rapporter davantage."])
  +BOX("💡 <strong>Le réflexe malin :</strong> garder 2 à 6 mois de dépenses sur le Livret A, puis orienter le surplus vers "
       "des placements mieux rémunérés sur le long terme (assurance-vie, fonds euros, ETF).")
  +H2("Les alternatives à considérer en 2026")
  +P("Pour faire travailler l'épargne au-delà du Livret A, plusieurs options existent selon votre horizon et votre tolérance au risque :")
  +UL(["Le <strong>LEP</strong> (Livret d'épargne populaire), mieux rémunéré, pour les revenus modestes.",
       "L'<strong>assurance-vie</strong> avec fonds euros sécurisé et unités de compte pour viser plus de rendement.",
       "Les <strong>ETF</strong> logés en assurance-vie pour une stratégie passive de long terme."])
  +P("Pour comparer les meilleurs contrats, voyez notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a> "
     "et notre guide <a href=\"/guides/assurance-vie-sans-frais-entree.html\">assurance-vie sans frais d'entrée</a>."),
 faq=[("Le taux du Livret A va-t-il baisser en 2026 ?","Le taux suit une formule indexée notamment sur l'inflation. Quand celle-ci reflue, le taux du Livret A tend à baisser lors des révisions périodiques."),
      ("Quel est le plafond du Livret A ?","Le plafond de versement du Livret A est de 22 950 €. Au-delà, seuls les intérêts continuent de s'ajouter."),
      ("Quelle alternative au Livret A une fois le plafond atteint ?","Le LDDS, le LEP (sous conditions de revenus) ou l'assurance-vie pour viser un meilleur rendement sur le long terme.")])

add(slug="lep-livret-epargne-populaire-2026",cat_link="/comparatifs/assurance-vie.html",cat_label="comparatif épargne",
 title="LEP 2026 : le placement le plus rentable et sans risque (pour qui ?)",
 desc="Le LEP (Livret d'épargne populaire) en 2026 : taux supérieur au Livret A, conditions de revenus, plafond 10 000 €. Qui peut en profiter et pourquoi l'ouvrir.",
 h1="LEP 2026 : le placement le plus rentable et sans risque (mais réservé)",
 lead="Souvent méconnu, le Livret d'épargne populaire est le placement sans risque le mieux rémunéré de France. Encore faut-il y avoir droit.",
 body=H2("Pourquoi le LEP bat tous les autres livrets")
  +P("Le <strong>LEP</strong> offre un taux structurellement <strong>supérieur à celui du Livret A</strong>, tout en étant "
     "100 % garanti, défiscalisé et liquide. C'est, mathématiquement, le meilleur placement sans risque accessible aux ménages éligibles.")
  +H2("Qui peut ouvrir un LEP ?")
  +P("Le LEP est <strong>réservé aux revenus modestes</strong> : votre revenu fiscal de référence ne doit pas dépasser un plafond "
     "révisé chaque année. Des millions de Français y ont droit <strong>sans le savoir</strong> et passent à côté.")
  +UL(["Plafond de versement : <strong>10 000 €</strong> (hors intérêts capitalisés).",
       "Un seul LEP par personne, deux maximum par foyer fiscal.",
       "Conditions de revenus vérifiées à l'ouverture puis périodiquement."])
  +BOX("💡 <strong>À faire :</strong> vérifiez votre revenu fiscal de référence sur votre dernier avis d'imposition. "
       "Si vous êtes éligible, le LEP devrait être <strong>rempli en priorité</strong>, avant même le Livret A.")
  +H2("Et après avoir rempli son LEP ?")
  +P("Une fois le plafond atteint, dirigez votre épargne vers le Livret A, le LDDS puis, pour le long terme, "
     "une <strong>assurance-vie</strong> à frais réduits. Découvrez notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Le LEP est-il vraiment sans risque ?","Oui, le capital est garanti par l'État, comme le Livret A. C'est un placement sécurisé et liquide."),
      ("Qui a droit au LEP ?","Les personnes dont le revenu fiscal de référence ne dépasse pas un plafond annuel. Beaucoup de Français éligibles l'ignorent."),
      ("Quel est le plafond du LEP ?","Le plafond de versement est de 10 000 €, hors intérêts capitalisés.")])

add(slug="ou-placer-son-epargne-2026",cat_link="/comparatifs/assurance-vie.html",cat_label="comparatif assurance-vie",
 title="Où placer son épargne en 2026 ? Le panorama des Français",
 desc="Où placer son argent en 2026 : Livret A, LEP, assurance-vie, fonds euros, ETF, SCPI, PER. Panorama des placements et stratégie selon votre horizon.",
 h1="Où placer son épargne en 2026 ? Le panorama complet",
 lead="Livret A saturé, inflation, marchés volatils : les Français cherchent où placer leur argent. Voici une cartographie claire des options en 2026.",
 body=H2("Étape 1 — Sécuriser son épargne de précaution")
  +P("Avant tout, constituez un <strong>matelas de sécurité</strong> de 2 à 6 mois de dépenses, disponible immédiatement : "
     "Livret A, LDDS et, si vous y êtes éligible, le <strong>LEP</strong> (le mieux rémunéré).")
  +H2("Étape 2 — Faire fructifier le moyen/long terme")
  +UL(["<strong>Assurance-vie</strong> : l'enveloppe reine, fiscalité douce après 8 ans, fonds euros + unités de compte.",
       "<strong>Fonds euros</strong> : sécurisé, rendement en hausse depuis la remontée des taux.",
       "<strong>ETF / trackers</strong> : pour viser la performance des marchés sur le long terme, à frais bas.",
       "<strong>SCPI</strong> : de l'immobilier sans gestion, pour diversifier et chercher du rendement.",
       "<strong>PER</strong> : pour préparer la retraite avec un avantage fiscal à l'entrée."])
  +BOX("💡 <strong>La règle d'or :</strong> diversifier selon l'horizon. Court terme = sécurité et liquidité ; "
       "long terme = on accepte un peu de volatilité pour viser plus de rendement.")
  +H2("Étape 3 — Choisir les bons contrats")
  +P("À performance égale, ce sont les <strong>frais</strong> qui font la différence sur 10 ou 20 ans. Privilégiez les contrats "
     "en ligne <strong>sans frais d'entrée</strong>. Comparez dans notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a> "
     "et notre <a href=\"/comparatifs/epargne-pilotee.html\">comparatif épargne pilotée</a>."),
 faq=[("Où placer son argent sans risque en 2026 ?","Sur les livrets réglementés garantis : LEP (si éligible), Livret A et LDDS pour l'épargne de précaution."),
      ("Quel placement rapporte le plus en 2026 ?","Sur le long terme, les unités de compte (ETF, SCPI) en assurance-vie visent plus de rendement, au prix d'un risque de perte en capital."),
      ("Combien faut-il garder sur ses livrets ?","En général 2 à 6 mois de dépenses courantes en épargne de précaution, le reste pouvant être investi à plus long terme.")])

add(slug="assurance-vie-collecte-2026",cat_link="/comparatifs/assurance-vie.html",cat_label="comparatif assurance-vie",
 title="Assurance-vie : pourquoi les Français y reviennent en 2026",
 desc="Assurance-vie en 2026 : collecte en hausse, fonds euros plus attractifs, fiscalité avantageuse. Pourquoi le placement préféré des Français retrouve la cote.",
 h1="Assurance-vie : pourquoi les Français y reviennent en 2026",
 lead="Avec la remontée des rendements des fonds euros et une fiscalité imbattable, l'assurance-vie retrouve les faveurs des épargnants.",
 body=H2("Le placement préféré des Français")
  +P("Avec plus de 1 900 milliards d'euros d'encours, l'<strong>assurance-vie</strong> reste, de loin, le placement le plus détenu en France. "
     "Après des années de taux bas, plusieurs facteurs expliquent son <strong>regain d'attractivité</strong> en 2026.")
  +H2("Trois raisons de ce retour en grâce")
  +OL(["<strong>Le fonds euros redevient intéressant</strong> : la remontée des taux a fait remonter les rendements, "
       "tout en gardant la garantie du capital.",
       "<strong>La fiscalité reste imbattable</strong> : après 8 ans, abattement annuel de 4 600 € (9 200 € pour un couple) sur les gains.",
       "<strong>La flexibilité</strong> : un seul contrat pour mêler sécurité (fonds euros) et performance (ETF, SCPI, unités de compte)."])
  +BOX("💡 <strong>Bon à savoir :</strong> l'antériorité fiscale court dès l'ouverture. Ouvrir un contrat tôt, même avec peu, "
       "permet de <strong>prendre date</strong> pour bénéficier plus vite des 8 ans.")
  +H2("Comment bien choisir son contrat")
  +P("Visez un contrat <strong>0 % de frais d'entrée</strong>, avec des frais de gestion bas et un large choix de supports. "
     "Notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a> et notre guide "
     "<a href=\"/guides/linxea-spirit-2.html\">Linxea Spirit 2</a> vous aident à trancher."),
 faq=[("Pourquoi ouvrir une assurance-vie en 2026 ?","Pour la fiscalité avantageuse après 8 ans, le retour des rendements des fonds euros et la flexibilité entre sécurité et performance."),
      ("Quel est l'avantage fiscal de l'assurance-vie ?","Après 8 ans, un abattement annuel de 4 600 € (9 200 € pour un couple) s'applique sur les gains lors des retraits."),
      ("Faut-il prendre date sur une assurance-vie ?","Oui, l'antériorité fiscale court dès l'ouverture : ouvrir tôt, même avec un petit montant, permet de lancer le compteur des 8 ans.")])

add(slug="fonds-euros-2026",cat_link="/comparatifs/assurance-vie.html",cat_label="comparatif assurance-vie",
 title="Fonds euros 2026 : le rendement remonte, faut-il y revenir ?",
 desc="Fonds euros en 2026 : rendement en hausse, capital garanti, bonus de taux. Faut-il privilégier le fonds euros ou les unités de compte ? Notre analyse.",
 h1="Fonds euros 2026 : le rendement remonte, faut-il y revenir ?",
 lead="Longtemps boudé pour ses rendements en berne, le fonds euros profite de la remontée des taux. Décryptage d'un placement qui redevient pertinent.",
 body=H2("Le fonds euros, c'est quoi ?")
  +P("Le <strong>fonds en euros</strong> est le support sécurisé de l'assurance-vie : votre <strong>capital est garanti</strong> "
     "et les intérêts acquis chaque année sont définitifs (effet cliquet). C'est le socle prudent de la plupart des contrats.")
  +H2("Pourquoi son rendement remonte")
  +P("La <strong>hausse des taux obligataires</strong> permet aux assureurs de réinvestir à de meilleures conditions. "
     "Résultat : les rendements servis sont repartis à la hausse, et certains contrats proposent même des <strong>bonus de taux</strong> "
     "conditionnés à une part d'unités de compte.")
  +BOX("💡 <strong>Stratégie :</strong> mixer fonds euros (sécurité) et unités de compte (performance) selon votre horizon. "
       "Plus l'horizon est long, plus la part d'unités de compte peut être élevée.")
  +H2("Fonds euros ou unités de compte ?")
  +UL(["<strong>Fonds euros</strong> : capital garanti, idéal pour la part prudente et les horizons courts.",
       "<strong>Unités de compte</strong> (ETF, SCPI…) : potentiel supérieur mais risque de perte en capital.",
       "La bonne allocation dépend de votre <strong>âge, projet et tolérance au risque</strong>."])
  +P("Pour choisir un contrat au bon fonds euros, voyez notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Le fonds euros est-il garanti ?","Oui, le capital placé sur un fonds en euros est garanti, et les intérêts annuels sont définitivement acquis (effet cliquet)."),
      ("Le rendement des fonds euros augmente-t-il en 2026 ?","La remontée des taux obligataires a permis aux assureurs d'améliorer les rendements servis, avec parfois des bonus de taux."),
      ("Vaut-il mieux le fonds euros ou les unités de compte ?","Le fonds euros sécurise, les unités de compte visent plus de rendement avec un risque. L'idéal est souvent un mix selon l'horizon.")])

add(slug="per-plan-epargne-retraite-2026",cat_link="/comparatifs/per-retraite.html",cat_label="comparatif PER",
 title="PER 2026 : pourquoi de plus en plus de Français l'adoptent",
 desc="Le Plan d'épargne retraite (PER) en 2026 : avantage fiscal à l'entrée, fonctionnement, sortie en capital ou rente. Pourquoi le PER séduit les épargnants.",
 h1="PER 2026 : pourquoi de plus en plus de Français l'adoptent",
 lead="Avantage fiscal immédiat et sortie en capital possible : le Plan d'épargne retraite s'impose comme un outil clé pour préparer l'avenir.",
 body=H2("Le PER, comment ça marche")
  +P("Le <strong>Plan d'épargne retraite</strong> permet de se constituer un complément de revenus pour la retraite. "
     "Son grand atout : les versements sont <strong>déductibles de votre revenu imposable</strong> (dans certaines limites), "
     "ce qui réduit votre impôt dès l'année du versement.")
  +H2("Pour qui le PER est-il intéressant ?")
  +UL(["Les contribuables <strong>fortement imposés</strong> : plus votre tranche est élevée, plus l'économie d'impôt est forte.",
       "Ceux qui veulent <strong>préparer la retraite</strong> avec un horizon long.",
       "Les profils prêts à <strong>bloquer l'épargne</strong> jusqu'à la retraite (hors cas de déblocage anticipé)."])
  +BOX("💡 <strong>Attention :</strong> l'avantage fiscal à l'entrée se paie partiellement à la sortie (imposition). "
       "Le PER est surtout gagnant si votre tranche d'imposition baisse à la retraite.")
  +H2("Sortie en capital ou en rente")
  +P("À la retraite, le PER offre une <strong>liberté de sortie</strong> : en capital (en une ou plusieurs fois), en rente, ou un mix. "
     "Le PER est aussi déblocable par anticipation pour l'<strong>achat de la résidence principale</strong>. "
     "Comparez les offres dans notre <a href=\"/comparatifs/per-retraite.html\">comparatif PER</a>."),
 faq=[("Quel est l'avantage fiscal du PER ?","Les versements sont déductibles du revenu imposable dans certaines limites, réduisant l'impôt dès l'année du versement."),
      ("Peut-on récupérer son PER en capital ?","Oui, à la retraite la sortie peut se faire en capital, en rente ou un mélange des deux."),
      ("Le PER est-il bloqué jusqu'à la retraite ?","En principe oui, sauf cas de déblocage anticipé comme l'achat de la résidence principale ou certains accidents de la vie.")])

add(slug="inflation-epargne-2026",cat_link="/comparatifs/assurance-vie.html",cat_label="comparatif assurance-vie",
 title="Inflation et épargne 2026 : comment protéger son argent",
 desc="Inflation en 2026 : comment éviter que votre épargne perde de la valeur. Livrets indexés, fonds euros, ETF, immobilier : les stratégies anti-inflation.",
 h1="Inflation et épargne en 2026 : comment protéger son argent",
 lead="L'argent qui dort sur un compte courant perd du pouvoir d'achat chaque année. Voici comment faire travailler son épargne face à l'inflation.",
 body=H2("Pourquoi l'inflation grignote votre épargne")
  +P("Avec l'inflation, <strong>100 € aujourd'hui achètent moins que 100 € il y a deux ans</strong>. "
     "L'argent laissé sur un compte courant non rémunéré perd mécaniquement du pouvoir d'achat. C'est l'ennemi silencieux de l'épargnant.")
  +H2("Les placements qui résistent le mieux")
  +UL(["<strong>Livrets réglementés</strong> (LEP en tête) : partiellement indexés sur l'inflation et garantis.",
       "<strong>Fonds euros</strong> : sécurité du capital avec un rendement reparti à la hausse.",
       "<strong>Actions / ETF</strong> : historiquement, les marchés battent l'inflation sur le long terme.",
       "<strong>Immobilier et SCPI</strong> : des loyers souvent indexés, une protection réelle sur la durée."])
  +BOX("💡 <strong>Le piège à éviter :</strong> laisser de grosses sommes sur le compte courant. Au-delà de l'épargne de précaution, "
       "chaque euro non placé perd de la valeur.")
  +H2("Construire une épargne anti-inflation")
  +P("La clé : <strong>diversifier</strong> entre sécurité (livrets, fonds euros) et actifs de long terme (ETF, SCPI) "
     "logés dans une assurance-vie à frais bas. Voyez notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a> "
     "et notre guide <a href=\"/guides/linxea-etf.html\">ETF chez Linxea</a>."),
 faq=[("Comment protéger son épargne de l'inflation ?","En évitant de laisser dormir l'argent sur un compte courant et en diversifiant entre livrets, fonds euros et actifs longs (ETF, SCPI)."),
      ("Quel placement bat l'inflation ?","Sur le long terme, les actions/ETF et l'immobilier ont historiquement dépassé l'inflation, au prix d'un risque de perte en capital."),
      ("Le Livret A protège-t-il de l'inflation ?","Partiellement : son taux est en partie indexé sur l'inflation, mais le rendement réel peut être faible voire négatif.")])

add(slug="livret-a-ou-assurance-vie-2026",cat_link="/comparatifs/assurance-vie.html",cat_label="comparatif assurance-vie",
 title="Livret A ou assurance-vie : où placer son épargne en 2026 ?",
 desc="Livret A ou assurance-vie en 2026 : liquidité, rendement, fiscalité, risque. Le match complet pour savoir où placer son argent selon vos objectifs.",
 h1="Livret A ou assurance-vie : où placer son épargne en 2026 ?",
 lead="Ce n'est pas l'un OU l'autre : Livret A et assurance-vie répondent à deux besoins différents. Voici comment les combiner intelligemment.",
 body=H2("Deux placements, deux usages")
  +P("Opposer le <strong>Livret A</strong> et l'<strong>assurance-vie</strong> n'a pas vraiment de sens : ils sont complémentaires. "
     "Le premier sert l'épargne de précaution, le second la constitution d'un capital sur le long terme.")
  +H2("Le match en 4 critères")
  +UL(["<strong>Liquidité</strong> : avantage Livret A (retrait immédiat). L'assurance-vie reste toutefois disponible sous quelques jours.",
       "<strong>Rendement</strong> : avantage assurance-vie sur le long terme (fonds euros + unités de compte).",
       "<strong>Fiscalité</strong> : avantage assurance-vie après 8 ans (abattement). Le Livret A est défiscalisé mais plafonné.",
       "<strong>Risque</strong> : Livret A 100 % garanti ; assurance-vie garantie sur le fonds euros, à risque sur les unités de compte."])
  +BOX("💡 <strong>La bonne combinaison :</strong> Livret A (+ LEP/LDDS) pour la sécurité disponible, puis assurance-vie "
       "pour faire fructifier le surplus à long terme. Prenez date tôt sur l'assurance-vie.")
  +H2("Notre recommandation")
  +P("Remplissez d'abord vos livrets de précaution, puis ouvrez une <strong>assurance-vie à frais réduits</strong> pour le long terme. "
     "Comparez les contrats dans notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Vaut-il mieux le Livret A ou l'assurance-vie ?","Les deux sont complémentaires : Livret A pour l'épargne de précaution disponible, assurance-vie pour le rendement de long terme."),
      ("L'assurance-vie est-elle plus rentable que le Livret A ?","Sur le long terme, oui en général, grâce aux fonds euros et aux unités de compte, mais avec un risque sur la partie investie."),
      ("Peut-on avoir un Livret A et une assurance-vie ?","Oui, et c'est même recommandé : ils répondent à deux besoins différents, sécurité d'un côté, croissance de l'autre.")])

add(slug="scpi-2026-rendement-risques",cat_link="/guides/linxea-scpi.html",cat_label="guide SCPI",
 title="SCPI en 2026 : rendements, risques et perspectives",
 desc="SCPI en 2026 : rendements, comment investir (direct ou assurance-vie), risques et fiscalité. Tout savoir sur la pierre-papier avant de se lancer.",
 h1="SCPI en 2026 : rendements, risques et comment investir",
 lead="L'immobilier sans les contraintes de gestion : les SCPI séduisent pour leur rendement, mais 2026 invite à la sélectivité.",
 body=H2("Les SCPI, comment ça marche")
  +P("Une <strong>SCPI</strong> (société civile de placement immobilier) collecte l'argent des épargnants pour acheter et gérer "
     "un parc immobilier (bureaux, commerces, santé, logistique…). Vous percevez une <strong>quote-part des loyers</strong> "
     "au prorata de vos parts, sans gérer quoi que ce soit.")
  +H2("Rendements et perspectives 2026")
  +P("Après une phase de repli des valorisations immobilières, le marché SCPI se montre plus <strong>sélectif</strong> en 2026. "
     "Certaines SCPI récentes affichent des rendements attractifs, mais les performances passées ne préjugent pas du futur.")
  +H2("Comment investir en SCPI")
  +UL(["<strong>En direct</strong> : achat de parts, revenus fonciers imposés au barème.",
       "<strong>Via l'assurance-vie</strong> : frais d'entrée réduits et fiscalité avantageuse — voir notre <a href=\"/guides/linxea-scpi.html\">guide SCPI Linxea</a>.",
       "<strong>À crédit</strong> : pour profiter de l'effet de levier (réservé aux profils avertis)."])
  +BOX("💡 <strong>Points de vigilance :</strong> placement de long terme, capital et revenus non garantis, liquidité limitée. "
       "Diversifiez entre plusieurs SCPI et secteurs.")
  +P("Pour loger des SCPI dans un contrat performant, voyez notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Quel rendement pour une SCPI en 2026 ?","Les rendements varient selon les SCPI et le secteur. Le marché est plus sélectif en 2026 et les performances passées ne garantissent pas l'avenir."),
      ("Les SCPI sont-elles risquées ?","Oui, le capital et les revenus ne sont pas garantis et la liquidité est limitée. C'est un placement de long terme à diversifier."),
      ("Comment investir en SCPI sans payer trop de frais ?","Via une assurance-vie qui négocie souvent des frais d'entrée réduits et une fiscalité avantageuse, comme chez Linxea.")])

add(slug="comparatif-taux-livrets-2026",cat_link="/comparatifs/assurance-vie.html",cat_label="comparatif épargne",
 title="Livret A, LDDS, LEP, fonds euros : le comparatif des taux 2026",
 desc="Comparatif des taux d'épargne 2026 : Livret A, LDDS, LEP, fonds euros. Plafonds, fiscalité, garantie. Quel livret choisir et dans quel ordre les remplir.",
 h1="Livret A, LDDS, LEP, fonds euros : le comparatif des taux 2026",
 lead="Tous les placements sécurisés ne se valent pas. Voici dans quel ordre remplir vos enveloppes pour maximiser votre épargne garantie.",
 body=H2("Le classement des placements sécurisés")
  +P("Pour l'épargne <strong>garantie et disponible</strong>, il existe une hiérarchie assez claire selon le rendement et les conditions :")
  +OL(["<strong>LEP</strong> — le mieux rémunéré, mais réservé aux revenus modestes (plafond 10 000 €).",
       "<strong>Livret A</strong> — universel, défiscalisé, garanti (plafond 22 950 €).",
       "<strong>LDDS</strong> — mêmes taux que le Livret A, en complément (plafond 12 000 €).",
       "<strong>Fonds euros</strong> — via l'assurance-vie, capital garanti, rendement reparti à la hausse, sans plafond réglementaire."])
  +H2("Dans quel ordre les remplir ?")
  +P("La stratégie efficace : <strong>LEP en priorité</strong> (si éligible), puis Livret A et LDDS pour la précaution, "
     "et enfin le <strong>fonds euros</strong> d'une assurance-vie pour l'épargne sécurisée de long terme une fois les livrets pleins.")
  +BOX("💡 <strong>Astuce fiscalité :</strong> les livrets réglementés sont défiscalisés. Le fonds euros est fiscalisé sur les gains, "
       "mais profite de l'abattement de l'assurance-vie après 8 ans.")
  +H2("Et pour aller chercher plus de rendement ?")
  +P("Au-delà du sécurisé, les <strong>unités de compte</strong> (ETF, SCPI) visent plus de performance avec un risque. "
     "Comparez les contrats dans notre <a href=\"/comparatifs/assurance-vie.html\">comparatif assurance-vie</a>."),
 faq=[("Quel livret a le meilleur taux en 2026 ?","Le LEP offre le meilleur taux parmi les livrets garantis, mais il est réservé aux revenus modestes. Sinon, Livret A et LDDS."),
      ("Dans quel ordre remplir ses livrets ?","LEP en priorité si éligible, puis Livret A et LDDS, et enfin le fonds euros d'une assurance-vie pour la suite."),
      ("Le fonds euros a-t-il un plafond ?","Non, contrairement aux livrets réglementés, le fonds euros d'une assurance-vie n'a pas de plafond réglementaire de versement.")])

def faq_ld(faq):
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)

def page(d):
    url=f"https://selectum.fr/actualites/{d['slug']}.html"
    title=html.escape(d["title"]); desc=html.escape(d["desc"])
    art_ld=json.dumps({"@context":"https://schema.org","@type":"NewsArticle","headline":d["title"],"description":d["desc"],
        "author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum",
        "logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},
        "datePublished":PUB,"dateModified":DATE,"mainEntityOfPage":url},ensure_ascii=False)
    bc_ld=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
        {"@type":"ListItem","position":2,"name":"Actualités","item":"https://selectum.fr/actualites.html"},
        {"@type":"ListItem","position":3,"name":d["title"],"item":url}]},ensure_ascii=False)
    faq_html='<div class="faq"><h2>❓ Questions fréquentes</h2>'+''.join(
        f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>'
        for q,a in d["faq"])+'</div>'
    sibs=[a for a in ART if a["slug"]!=d["slug"]][:4]
    rel=''.join(f'<a href="/actualites/{s["slug"]}.html" class="rel-chip">{html.escape(s["h1"][:58])} →</a>' for s in sibs)
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
<nav class="nav"></nav><div class="header-cta"><a href="{d['cat_link']}" class="btn-primary">Voir le {html.escape(d['cat_label'])} →</a></div>
</div></div></header>
<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/actualites.html">Actualités</a><span>/</span>Épargne</div>
  <h1>{html.escape(d['h1'])}</h1>
  <p class="updated">🗓️ Publié le 9 juin 2026 — mis à jour le 11 juin 2026</p>
</div></div>
<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
  <div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> article informatif. Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Investir comporte un risque de perte en capital.</div>
  <p class="intro" style="font-size:1.12rem;color:var(--gray-700);">{html.escape(d['lead'])}</p>
  {d['body']}
  {faq_html}
  <div class="rel-links"><h2>À lire aussi</h2><div class="rel-list">{rel}</div></div>
</div></div>
<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

os.makedirs("actualites",exist_ok=True)
for d in ART:
    open(f"actualites/{d['slug']}.html","w",encoding="utf-8").write(page(d))
print("articles actualités générés:",len(ART))
for d in ART: print("  actualites/"+d["slug"]+".html")
