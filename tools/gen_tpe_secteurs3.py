#!/usr/bin/env python3
# -*- coding: utf-8 -*-
exec(open("tools/gen_tpe_seo.py").read().split("\nn=0")[0])
import os
ORDER={"retail":["flatpay","square","sumup","mypos"],"premium":["flatpay","square","mypos","sumup"],
 "chr":["flatpay","square","mypos","sumup"],"sante":["flatpay","sumup","mypos","square"],
 "mobile":["sumup","viva-wallet","flatpay","zettle"]}
INTRO={"retail":"encaissement rapide en boutique, sans-contact et fiabilité au quotidien",
 "premium":"paniers élevés, paiement en plusieurs fois et expérience client soignée",
 "chr":"service rapide, additions, pourboires et caisse connectée",
 "sante":"consultations, honoraires et simplicité de l'encaissement",
 "mobile":"un terminal mobile autonome (4G + batterie) pour encaisser partout"}
S=[
 ("serrurier","serrurier","un","mobile"),("demenageur","déménageur","un","mobile"),
 ("dj-musicien","DJ / musicien","un","mobile"),("food-court","food court","un","chr"),
 ("dark-kitchen","dark kitchen","une","chr"),("producteur-vente-directe","producteur en vente directe","un","mobile"),
 ("station-service","station-service","une","retail"),("laverie","laverie automatique","une","retail"),
 ("pressing","pressing","un","retail"),("cordonnerie","cordonnerie","une","retail"),
 ("coiffeur-domicile","coiffeur à domicile","un","mobile"),("estheticienne-domicile","esthéticienne à domicile","une","mobile"),
 ("naturopathe","naturopathe","un","sante"),("sophrologue","sophrologue","un","sante"),
 ("psychologue","psychologue","un","sante"),("coach-sportif","coach sportif","un","mobile"),
 ("camion-pizza","camion à pizza","un","mobile"),("vendeur-glaces","marchand de glaces","un","mobile"),
 ("ecole-de-danse","école de danse","une","sante"),("magasin-informatique","magasin informatique","un","premium"),
 ("reparateur-telephone","réparateur de téléphone","un","retail"),("magasin-vape","magasin de cigarette électronique","un","retail"),
 ("magasin-musique","magasin de musique","un","premium"),("galerie-art","galerie d'art","une","premium"),
 ("bar-a-chicha","bar à chicha","un","chr"),("kebab","kebab","un","chr"),
 ("brasserie","brasserie","une","chr"),("discotheque","discothèque","une","chr"),
 ("cafe-restaurant","café-restaurant","un","chr"),("salon-de-massage","salon de massage","un","premium"),
 ("magasin-puericulture","magasin de puériculture","un","retail"),("opticien-domicile","opticien à domicile","un","mobile"),
]
n=0
for slug,label,art,typ in S:
    fslug=f"meilleur-tpe-{slug}"
    if os.path.exists(f"comparatifs/{fslug}.html"): continue
    cap=label[0].upper()+label[1:]
    title=f"Meilleur TPE pour {label} 2026 : top 4"
    desc=f"Quel TPE pour {art} {label} en 2026 ? Top 4 des meilleurs terminaux de paiement adaptés, comparés sur la commission, l'engagement et les services."
    h1=f"Meilleur TPE pour {label} : le top 4 en 2026"
    intro=f"{cap} : {INTRO[typ]}. Voici notre sélection des meilleurs TPE pour votre activité."
    open(f"comparatifs/{fslug}.html","w").write(page(fslug,title,desc,h1,intro,ORDER[typ])); n+=1

# angles paiement long-tail
A=[
 ("tpe-paiement-plusieurs-fois","TPE avec paiement en plusieurs fois 2026 : top 4","Quel TPE propose le paiement en 3 ou 4 fois en 2026 ? Top 4 des terminaux avec facilités de paiement. Flatpay, Square, myPOS, SumUp.","Meilleur TPE avec paiement en plusieurs fois : le top 4 en 2026","Proposer le paiement en 3x ou 4x booste vos ventes sur les paniers élevés. Voici les meilleurs TPE compatibles.",["flatpay","square","mypos","sumup"]),
 ("tpe-pourboire","Meilleur TPE avec pourboire 2026 : top 4","Quel TPE gère le pourboire en 2026 ? Top 4 des terminaux idéaux pour la restauration et les services. Flatpay, Square, SumUp, myPOS.","Meilleur TPE avec pourboire : le top 4 en 2026","Gestion du pourboire à l'encaissement : un vrai plus en CHR et services. Voici les meilleurs TPE.",["flatpay","square","sumup","mypos"]),
 ("tpe-deux-commerces","TPE pour 2 commerces ou plus 2026 : top 4 multi-points de vente","Quel TPE pour plusieurs commerces en 2026 ? Top 4 des solutions multi-points de vente avec reporting centralisé. Flatpay, Square, myPOS, SumUp.","Meilleur TPE multi-commerces : le top 4 en 2026","Plusieurs boutiques ou points de vente ? Il faut un reporting centralisé et plusieurs terminaux. Voici les meilleures solutions.",["flatpay","square","mypos","sumup"]),
 ("tpe-micro-entreprise","Meilleur TPE pour micro-entreprise 2026 : top 4","Quel TPE pour une micro-entreprise en 2026 ? Top 4 des terminaux simples et économiques sans paperasse. SumUp, Flatpay, Zettle, Viva.","Meilleur TPE pour micro-entreprise : le top 4 en 2026","En micro-entreprise, on veut simple, économique et sans engagement. Voici les meilleurs TPE.",["sumup","flatpay","zettle","viva-wallet"]),
 ("tpe-marche-de-noel","Meilleur TPE pour marché de Noël 2026 : top 4 mobile","Quel TPE pour un marché de Noël ou un stand éphémère en 2026 ? Top 4 mobiles et sans engagement. SumUp, Viva, Zettle, Flatpay.","Meilleur TPE pour marché de Noël : le top 4 en 2026","Stand éphémère, marché de Noël, vente saisonnière : un TPE mobile sans engagement est idéal. Voici les meilleurs.",["sumup","viva-wallet","zettle","flatpay"]),
]
for slug,title,desc,h1,intro,order in A:
    if os.path.exists(f"comparatifs/{slug}.html"): continue
    open(f"comparatifs/{slug}.html","w").write(page(slug,title,desc,h1,intro,order)); n+=1
print("nouvelles pages TPE (secteurs+angles):",n)
