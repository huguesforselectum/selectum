#!/usr/bin/env python3
# -*- coding: utf-8 -*-
exec(open("tools/gen_verticals.py").read().split('print("lib')[0])

VERTICALS={
 "vpn":("VPN","/comparatifs/vpn.html",[
   ("vpn-pas-cher","Meilleur VPN pas cher 2026 : top 4 des VPN les moins chers","Quel VPN pas cher choisir en 2026 ? Top 4 des meilleurs VPN à petit prix sans sacrifier la sécurité. Surfshark, CyberGhost, NordVPN comparés.","Meilleur VPN pas cher : le top 4 en 2026","Un bon VPN ne coûte pas cher si vous prenez un engagement long. Voici les meilleurs VPN au meilleur prix.",["surfshark","cyberghost","nordvpn","protonvpn"]),
   ("vpn-netflix","Meilleur VPN pour Netflix 2026 : débloquer les catalogues","Quel VPN pour Netflix en 2026 ? Top 4 des VPN qui débloquent les catalogues étrangers en streaming HD. NordVPN, ExpressVPN, CyberGhost.","Meilleur VPN pour Netflix : le top 4 en 2026","Pour débloquer les catalogues Netflix étrangers en HD sans coupure, certains VPN sont bien plus performants. Voici les meilleurs.",["nordvpn","expressvpn","cyberghost","surfshark"]),
   ("vpn-gratuit","VPN gratuit 2026 : top 3 (et pourquoi se méfier)","Meilleur VPN gratuit en 2026 : Proton VPN offre un vrai forfait gratuit. Top 3 et les pièges des VPN 100% gratuits à éviter.","VPN gratuit : le top 3 en 2026","Les VPN « 100% gratuits » revendent souvent vos données. Proton VPN propose un vrai forfait gratuit sérieux. Voici les meilleures options.",["protonvpn","surfshark","nordvpn"]),
   ("vpn-streaming","Meilleur VPN streaming 2026 : top 4","Quel VPN pour le streaming en 2026 ? Top 4 pour Netflix, Disney+, Prime Video sans buffering. ExpressVPN, NordVPN, CyberGhost.","Meilleur VPN streaming : le top 4 en 2026","Streaming fluide et déblocage des plateformes : voici les VPN les plus rapides et fiables.",["expressvpn","nordvpn","cyberghost","surfshark"]),
 ]),
 "banque-en-ligne":("Banque","/comparatifs/banque-en-ligne.html",[
   ("banque-en-ligne-gratuite","Meilleure banque en ligne gratuite 2026 : top 4","Quelle banque en ligne gratuite en 2026 ? Top 4 des comptes sans frais avec carte gratuite. BoursoBank, Fortuneo, Hello bank!, Monabanq.","Meilleure banque en ligne gratuite : le top 4 en 2026","Compte courant et carte gratuits, sans frais cachés. Voici les meilleures banques en ligne gratuites.",["boursobank","fortuneo","hellobank","monabanq"]),
   ("banque-sans-condition-de-revenus","Banque en ligne sans condition de revenus 2026 : top 4","Quelle banque en ligne sans condition de revenus en 2026 ? Top 4 des comptes accessibles à tous. BoursoBank, Monabanq, Hello bank!.","Banque sans condition de revenus : le top 4 en 2026","Ouvrir un compte sans justifier de revenus minimums : voici les banques en ligne les plus accessibles.",["boursobank","monabanq","hellobank","fortuneo"]),
 ]),
 "assurance-auto":("Assurance auto","/comparatifs/assurance-auto.html",[
   ("assurance-auto-pas-cher","Assurance auto pas cher 2026 : top 4 des moins chères","Quelle assurance auto pas cher en 2026 ? Top 4 pour payer moins cher sans sacrifier les garanties. Direct Assurance, Macif, MAIF.","Assurance auto pas cher : le top 4 en 2026","Réduire sa prime auto sans baisser ses garanties, c'est possible. Voici les assurances auto les moins chères.",["direct-assurance","macif","maif","axa"]),
   ("assurance-auto-jeune-conducteur","Assurance auto jeune conducteur 2026 : top 4","Quelle assurance auto pour jeune conducteur en 2026 ? Top 4 pour limiter la surprime. Direct Assurance, MAIF, Macif.","Assurance auto jeune conducteur : le top 4 en 2026","Les jeunes conducteurs subissent une surprime : certaines assurances la limitent. Voici les meilleures offres.",["direct-assurance","maif","macif","axa"]),
   ("assurance-auto-resilie-malus","Assurance auto résilié / malus 2026 : top 4","Assurance auto pour résilié ou malussé en 2026 : top 4 des assureurs qui acceptent les profils à risque. Direct Assurance, MAIF.","Assurance auto résilié / malus : le top 4 en 2026","Résilié pour non-paiement ou fort malus ? Certains assureurs acceptent ces profils. Voici les meilleures options.",["direct-assurance","maif","axa","macif"]),
 ]),
 "mutuelle-sante":("Mutuelle","/comparatifs/mutuelle-sante.html",[
   ("mutuelle-pas-cher","Mutuelle pas cher 2026 : top 4 des complémentaires santé","Quelle mutuelle pas cher en 2026 ? Top 4 des complémentaires santé au meilleur rapport garanties/prix. Alan, Malakoff Humanis, Harmonie.","Mutuelle pas cher : le top 4 en 2026","Une bonne mutuelle au juste prix existe. Voici les complémentaires santé au meilleur rapport garanties/prix.",["alan","malakoffhumanis","harmonie-mutuelle","allianz"]),
   ("mutuelle-senior","Mutuelle senior 2026 : top 4 pour les retraités","Quelle mutuelle senior en 2026 ? Top 4 des complémentaires adaptées aux plus de 60 ans (optique, dentaire, hospitalisation). Malakoff, Harmonie.","Mutuelle senior : le top 4 en 2026","Les seniors ont des besoins spécifiques (optique, dentaire, hospitalisation). Voici les meilleures mutuelles senior.",["malakoffhumanis","harmonie-mutuelle","allianz","alan"]),
   ("mutuelle-tns-independant","Mutuelle TNS / indépendant 2026 : top 3 (loi Madelin)","Quelle mutuelle pour TNS ou indépendant en 2026 ? Top 3 des complémentaires éligibles loi Madelin. Alan, Malakoff Humanis, Harmonie.","Mutuelle TNS / indépendant : le top 3 en 2026","Travailleur non salarié : profitez d'une mutuelle déductible (loi Madelin) adaptée à votre activité. Voici les meilleures.",["alan","malakoffhumanis","harmonie-mutuelle"]),
 ]),
 "crypto":("Crypto","/comparatifs/crypto.html",[
   ("crypto-debutant","Meilleure plateforme crypto pour débuter 2026 : top 4","Quelle plateforme crypto pour débuter en 2026 ? Top 4 des plus simples et sûres. Bitpanda, Coinhouse, Kraken, Coinbase.","Meilleure plateforme crypto pour débuter : le top 4 en 2026","Débuter en crypto demande une plateforme simple, en français et régulée. Voici les meilleures pour démarrer.",["bitpanda","coinhouse","kraken","coinbase"]),
   ("crypto-frais-bas","Plateforme crypto frais bas 2026 : top 4 des moins chères","Quelle plateforme crypto avec les frais les plus bas en 2026 ? Top 4. Binance, Kraken, Bitpanda, Coinbase comparés.","Plateforme crypto frais bas : le top 4 en 2026","Les frais grignotent vos gains. Voici les plateformes crypto aux commissions les plus basses.",["binance","kraken","bitpanda","coinbase"]),
   ("acheter-bitcoin","Où acheter du Bitcoin en 2026 ? Top 4 des plateformes","Où acheter du Bitcoin en France en 2026 ? Top 4 des meilleures plateformes sûres et simples. Bitpanda, Kraken, Coinbase, Binance.","Où acheter du Bitcoin : le top 4 en 2026","Acheter du Bitcoin en toute sécurité : voici les meilleures plateformes pour acheter du BTC en France.",["bitpanda","kraken","coinbase","binance"]),
 ]),
}

total=0
for base,(cat,link,decls) in VERTICALS.items():
    ACT=load_actors(base)
    related=[(h1.split(':')[0].strip(), f"/comparatifs/{s}.html") for s,_,_,h1,_,_ in decls][:5]
    for slug,title,desc,h1,intro,order in decls:
        if build(slug,title,desc,h1,intro,order,ACT,cat,link,related): total+=1
        else: print("skip",slug,"(données manquantes)")
print("pages verticales générées:",total)
