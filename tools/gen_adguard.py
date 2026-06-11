#!/usr/bin/env python3
# -*- coding: utf-8 -*-
exec(open("tools/gen_verticals.py").read().split('print("lib')[0])
ACT={
 "adguard":dict(slug="adguard",name="AdGuard",go="/go/adguard",score="9,2",price="Licence à vie ~40 €",note="",
   desc="Le bloqueur de pub le plus complet : il filtre pubs et traceurs dans le navigateur ET dans toutes vos applications, au niveau du système.",
   pts=["Bloque pubs + traceurs partout","Niveau système (toutes apps)","Licence à vie possible","DNS & VPN AdGuard"]),
 "ublock":dict(slug="ublock",name="uBlock Origin",go="/go/ublock",score="9,0",price="Gratuit",note="open-source",
   desc="Le bloqueur open-source le plus efficace et le plus léger, directement dans le navigateur.",
   pts=["100% gratuit & open-source","Ultra léger","Très efficace","Navigateur uniquement"]),
 "brave":dict(slug="brave",name="Brave",go="/go/brave",score="8,4",price="Gratuit",note="navigateur",
   desc="Un navigateur rapide et privé avec bloqueur de pub et de traceurs intégré.",
   pts=["Bloqueur intégré","Navigateur complet","Rapide & privé","Sans extension"]),
 "ghostery":dict(slug="ghostery",name="Ghostery",go="/go/ghostery",score="8,2",price="Gratuit / Premium",note="",
   desc="Le spécialiste de l'anti-pistage, avec tableau de bord des traceurs et recherche privée.",
   pts=["Anti-traçage poussé","Open-source","Tableau de bord traceurs","Version premium"]),
 "adblockplus":dict(slug="adblockplus",name="AdBlock Plus",go="/go/adblockplus",score="8,0",price="Gratuit",note="",
   desc="Le bloqueur le plus populaire au monde (100M+ utilisateurs), simple à installer.",
   pts=["100M+ utilisateurs","Très simple","Gratuit","Pubs « acceptables » par défaut"]),
}
CAT="Bloqueur de pub"; LINK="/comparatifs/bloqueur-de-pub.html"
related=[("Meilleur bloqueur de pub","/comparatifs/bloqueur-de-pub.html"),
 ("Bloqueur de pub gratuit","/comparatifs/bloqueur-de-pub-gratuit.html"),
 ("Bloqueur de pub Chrome","/comparatifs/bloqueur-de-pub-chrome.html"),
 ("Bloquer les pubs YouTube","/comparatifs/bloqueur-de-pub-youtube.html")]
PAGES=[
 ("bloqueur-de-pub","Meilleur bloqueur de pub 2026 : le comparatif (AdGuard, uBlock…)","Quel est le meilleur bloqueur de pub en 2026 ? Comparatif AdGuard, uBlock Origin, Brave, Ghostery. Efficacité, prix, navigateur vs système.","Meilleur bloqueur de pub 2026","Pubs intrusives, traceurs, vidéos forcées… un bon bloqueur change tout. Voici notre comparatif des meilleures solutions selon votre usage.",["adguard","ublock","brave","ghostery"]),
 ("bloqueur-de-pub-gratuit","Meilleur bloqueur de pub gratuit 2026 : top 4","Quel bloqueur de pub gratuit choisir en 2026 ? Top 4 des solutions gratuites et efficaces. uBlock Origin, Brave, AdBlock Plus, Ghostery.","Meilleur bloqueur de pub gratuit : le top 4 en 2026","Bloquer les pubs sans payer, c'est possible et efficace. Voici les meilleurs bloqueurs 100% gratuits.",["ublock","brave","adblockplus","ghostery"]),
 ("bloqueur-de-pub-chrome","Meilleur bloqueur de pub Chrome 2026 : top 4","Quel bloqueur de pub pour Chrome en 2026 (après Manifest V3) ? Top 4. AdGuard, uBlock Origin, Ghostery, AdBlock Plus.","Meilleur bloqueur de pub Chrome : le top 4 en 2026","Avec Manifest V3, tous les bloqueurs ne se valent plus sur Chrome. Voici les plus efficaces aujourd'hui.",["adguard","ublock","ghostery","adblockplus"]),
 ("bloqueur-de-pub-youtube","Bloquer les pubs YouTube 2026 : top 4 des solutions","Comment bloquer les pubs YouTube en 2026 ? Top 4 des bloqueurs qui fonctionnent encore. AdGuard, uBlock Origin, Brave, Ghostery.","Bloquer les pubs YouTube : le top 4 en 2026","YouTube durcit la lutte contre les bloqueurs. Voici les solutions qui marchent encore pour regarder sans pub.",["adguard","ublock","brave","ghostery"]),
 ("bloqueur-de-pub-iphone","Meilleur bloqueur de pub iPhone 2026 : top 3","Quel bloqueur de pub pour iPhone en 2026 ? Top 3 des solutions iOS efficaces. AdGuard, Ghostery, Brave.","Meilleur bloqueur de pub iPhone : le top 3 en 2026","Sur iOS, le choix est plus restreint. Voici les meilleurs bloqueurs de pub pour iPhone et iPad.",["adguard","ghostery","brave"]),
]
n=0
for slug,title,desc,h1,intro,order in PAGES:
    if build(slug,title,desc,h1,intro,order,ACT,CAT,LINK,related): n+=1
print("comparatifs bloqueur de pub générés:",n)
