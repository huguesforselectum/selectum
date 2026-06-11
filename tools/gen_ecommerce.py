#!/usr/bin/env python3
# -*- coding: utf-8 -*-
exec(open("tools/gen_verticals.py").read().split('print("lib')[0])  # head, topcard, card, build

ACT={
 "shopify":dict(slug="shopify",name="Shopify",go="/go/shopify",score="9,3",price="dès 33 €/mois",note="",
   desc="La plateforme e-commerce tout-en-un n°1 : simple, puissante, hébergée, avec essai gratuit.",
   pts=["Tout-en-un hébergé","Essai gratuit","+8 000 applications","Vendre multicanal"]),
 "woocommerce":dict(slug="woocommerce",name="WooCommerce",go="/go/woocommerce",score="8,8",price="Gratuit",note="+ hébergement",
   desc="L'extension e-commerce open-source de WordPress : flexible, économique et excellente pour le SEO.",
   pts=["Open-source gratuit","Sur WordPress","100% personnalisable","SEO puissant"]),
 "wix":dict(slug="wix",name="Wix",go="/go/wix",score="8,4",price="dès 17 €/mois",note="",
   desc="Le créateur de site le plus simple, idéal pour les vitrines et petites boutiques.",
   pts=["Ultra simple","Éditeur drag & drop","Templates variés","Tout-en-un"]),
 "prestashop":dict(slug="prestashop",name="PrestaShop",go="/go/prestashop",score="8,3",price="Gratuit",note="+ hébergement",
   desc="La solution e-commerce open-source française, puissante pour les catalogues complexes.",
   pts=["Open-source français","Catalogues riches","Personnalisable","Communauté FR"]),
 "squarespace":dict(slug="squarespace",name="Squarespace",go="/go/squarespace",score="8,2",price="dès 23 €/mois",note="",
   desc="Design haut de gamme, idéal pour les créateurs et les marques visuelles.",
   pts=["Design premium","Tout-en-un","Templates léchés","Simple à utiliser"]),
 "bigcommerce":dict(slug="bigcommerce",name="BigCommerce",go="/go/bigcommerce",score="8,1",price="dès 29 €/mois",note="",
   desc="Plateforme SaaS robuste, sans frais de transaction, pensée pour les boutiques en croissance.",
   pts=["SaaS robuste","0 frais de transaction","Multicanal","Très évolutif"]),
}
CAT="E-commerce"; LINK="/comparatifs/ecommerce.html"
related=[("Meilleure plateforme e-commerce","/comparatifs/ecommerce.html"),
 ("Créer une boutique en ligne","/comparatifs/creer-boutique-en-ligne.html"),
 ("Plateforme e-commerce pas cher","/comparatifs/plateforme-ecommerce-pas-cher.html"),
 ("Vendre en ligne","/comparatifs/vendre-en-ligne.html")]

PAGES=[
 ("ecommerce","Meilleure plateforme e-commerce 2026 : le comparatif pour créer sa boutique","Quelle plateforme e-commerce choisir en 2026 ? Comparatif Shopify, WooCommerce, Wix, PrestaShop, Squarespace. Prix, simplicité, SEO et évolutivité.","Meilleure plateforme e-commerce 2026","Créer une boutique en ligne n'a jamais été aussi simple — mais chaque plateforme a ses forces. Voici notre comparatif pour bien choisir selon votre projet.",["shopify","woocommerce","wix","prestashop","squarespace"]),
 ("creer-boutique-en-ligne","Créer une boutique en ligne 2026 : top 4 des meilleures solutions","Comment créer une boutique en ligne en 2026 ? Top 4 des plateformes les plus simples et complètes. Shopify, Wix, WooCommerce, Squarespace.","Créer une boutique en ligne : le top 4 en 2026","Lancer sa boutique en ligne rapidement, sans (trop) de technique : voici les meilleures plateformes pour créer son site marchand.",["shopify","wix","woocommerce","squarespace"]),
 ("plateforme-ecommerce-pas-cher","Plateforme e-commerce pas cher 2026 : top 4","Quelle plateforme e-commerce pas cher en 2026 ? Top 4 des solutions au meilleur coût. WooCommerce, Wix, PrestaShop, Shopify.","Plateforme e-commerce pas cher : le top 4 en 2026","Lancer une boutique sans se ruiner : les solutions open-source et les formules d'entrée de gamme. Voici les moins chères.",["woocommerce","wix","prestashop","shopify"]),
 ("vendre-en-ligne","Meilleur site pour vendre en ligne 2026 : top 4","Quel est le meilleur site pour vendre en ligne en 2026 ? Top 4 des plateformes pour vendre ses produits. Shopify, WooCommerce, Wix, BigCommerce.","Meilleur site pour vendre en ligne : le top 4 en 2026","Vendre ses produits en ligne efficacement : paiement, gestion, multicanal. Voici les meilleures plateformes.",["shopify","woocommerce","wix","bigcommerce"]),
 ("plateforme-ecommerce-debutant","Plateforme e-commerce pour débuter 2026 : top 4","Quelle plateforme e-commerce pour débuter en 2026 ? Top 4 des plus simples pour se lancer sans technique. Shopify, Wix, Squarespace, WooCommerce.","Plateforme e-commerce pour débuter : le top 4 en 2026","Débuter dans l'e-commerce sans compétence technique : voici les plateformes les plus accessibles.",["shopify","wix","squarespace","woocommerce"]),
]
n=0
for slug,title,desc,h1,intro,order in PAGES:
    if build(slug,title,desc,h1,intro,order,ACT,CAT,LINK,related): n+=1
print("comparatifs e-commerce générés:",n)
