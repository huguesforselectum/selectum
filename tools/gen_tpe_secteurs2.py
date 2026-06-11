#!/usr/bin/env python3
# -*- coding: utf-8 -*-
exec(open("tools/gen_tpe_seo.py").read().split("\nn=0")[0])  # ACT, page
import os

ORDER={
 "retail":["flatpay","square","sumup","mypos"],
 "premium":["flatpay","square","mypos","sumup"],
 "chr":["flatpay","square","mypos","sumup"],
 "sante":["flatpay","sumup","mypos","square"],
 "mobile":["sumup","viva-wallet","flatpay","zettle"],
}
INTRO={
 "retail":"encaissement rapide en boutique, paiement sans contact et fiabilité au quotidien",
 "premium":"paniers élevés, paiement en plusieurs fois et expérience client soignée",
 "chr":"service rapide, additions, pourboires et caisse connectée",
 "sante":"consultations, honoraires et simplicité de l'encaissement",
 "mobile":"un terminal mobile autonome (4G + batterie) pour encaisser partout",
}
# (slug, libellé activité, article 'un/une', type)
S=[
 ("tabac-presse","bureau de tabac","un","retail"),("primeur","primeur","un","retail"),
 ("poissonnerie","poissonnerie","une","retail"),("fromagerie","fromagerie","une","retail"),
 ("bijouterie","bijouterie","une","premium"),("pret-a-porter","magasin de prêt-à-porter","un","retail"),
 ("magasin-chaussures","magasin de chaussures","un","retail"),("magasin-decoration","magasin de décoration","un","retail"),
 ("jardinerie","jardinerie","une","retail"),("animalerie","animalerie","une","retail"),
 ("librairie","librairie","une","retail"),("magasin-jouets","magasin de jouets","un","retail"),
 ("magasin-sport","magasin de sport","un","retail"),("velociste","magasin de vélo","un","premium"),
 ("magasin-bio","magasin bio","un","retail"),("quincaillerie","quincaillerie","une","retail"),
 ("magasin-meubles","magasin de meubles","un","premium"),("maroquinerie","maroquinerie","une","premium"),
 ("pizzeria","pizzeria","une","chr"),("creperie","crêperie","une","chr"),
 ("snack-fast-food","snack / fast-food","un","chr"),("restaurant-japonais","restaurant japonais","un","chr"),
 ("salon-de-the","salon de thé","un","chr"),("bar-a-vin","bar à vin","un","chr"),
 ("glacier","glacier","un","chr"),("patisserie","pâtisserie","une","retail"),
 ("hotel","hôtel","un","premium"),("gite-chambre-hotes","gîte / chambre d'hôtes","un","premium"),
 ("veterinaire","cabinet vétérinaire","un","sante"),("kine-osteo","cabinet de kiné / ostéo","un","sante"),
 ("dentiste","cabinet dentaire","un","sante"),("tatoueur","salon de tatouage","un","premium"),
 ("barbier","barbier","un","retail"),("onglerie","onglerie","une","retail"),
 ("spa","spa / centre de bien-être","un","premium"),("photographe","photographe","un","mobile"),
 ("toiletteur","salon de toilettage","un","retail"),("paysagiste","paysagiste","un","mobile"),
 ("auto-ecole","auto-école","une","sante"),("escape-game","escape game","un","retail"),
 ("studio-yoga","studio de yoga / pilates","un","sante"),("brocante-antiquaire","brocante / antiquaire","une","mobile"),
]
n=0
for slug,label,art,typ in S:
    fslug=f"meilleur-tpe-{slug}"
    if os.path.exists(f"comparatifs/{fslug}.html"): continue
    cap=label[0].upper()+label[1:]
    title=f"Meilleur TPE pour {label} 2026 : top 4"
    desc=f"Quel TPE pour {art} {label} en 2026 ? Top 4 des meilleurs terminaux de paiement adaptés, comparés sur la commission, l'engagement et les services."
    h1=f"Meilleur TPE pour {label} : le top 4 en 2026"
    intro=f"{cap} : {INTRO[typ]}. Voici notre sélection des meilleurs TPE pour votre activité, du plus avantageux au plus flexible."
    open(f"comparatifs/{fslug}.html","w").write(page(fslug,title,desc,h1,intro,ORDER[typ])); n+=1
print("nouveaux comparatifs TPE secteurs:",n)
