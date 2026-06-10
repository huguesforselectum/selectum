#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import importlib.util
spec=importlib.util.spec_from_file_location("ga","tools/gen_actu.py")
# on réutilise la fonction page() de gen_actu via exec
src=open("tools/gen_actu.py").read()
# isole tout sauf la boucle finale
src=src.split("n=0")[0]
ns={}; exec(src, ns)
page=ns["page"]
LABELS={
 "assurance-emprunteur":"assurance emprunteur","assurance-habitation":"assurance habitation","assurance-vie":"assurance-vie",
 "box-abonnement":"box & abonnements","box-internet":"box internet","cartes-famille":"cartes ados & famille",
 "change-multidevises":"change multi-devises","comptes-pro":"comptes pro","courtage-immobilier":"courtage immobilier",
 "credit-conso":"crédit conso","epargne-pilotee":"épargne pilotée","facturation":"logiciels de facturation",
 "formation":"plateformes de formation","logiciels-crm":"logiciels CRM","per-retraite":"PER / retraite",
 "rachat-credit":"rachat de crédit","terminaux-paiement":"terminaux de paiement","transfert-argent":"transfert d'argent"}
todo=json.load(open("/tmp/actu_todo.json"))
n=0
for slug in todo:
    cl=LABELS.get(slug, slug.replace('-',' '))
    open(f"actualites/{slug}.html","w").write(page(slug,cl)); n+=1
print("actualités hors top8 générées:",n)
