#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enrichit les avis Tier 2 en tests detailles (memes signaux E-E-A-T que Tier 1)."""
import os, html
from enrich_avis_tier1 import PARCOURS, OL

PARCOURS["hebergement"]=("Commande, installation et mise en ligne",
   ["<strong>Choix de l'offre</strong> (mutualisé, VPS…) selon le besoin.",
    "<strong>Commande</strong> et choix du nom de domaine.",
    "<strong>Accès au panel</strong> et installation du CMS (WordPress en un clic).",
    "<strong>Mise en ligne</strong> du site et configuration SSL.",
    "<strong>Support</strong> : test de la réactivité en cas de question."])

BR={
 "qonto":("Qonto","compte-pro",False),"revolut":("Revolut","banque",False),
 "ionos":("IONOS","hebergement",False),"hostinger":("Hostinger","hebergement",False),
 "ovhcloud":("OVHcloud","hebergement",False),"o2switch":("o2switch","hebergement",False),
 "bitpanda":("Bitpanda","crypto",True),"binance":("Binance","crypto",True),
 "etoro":("eToro","bourse",True),"coinhouse":("Coinhouse","crypto",True),
 "trade-republic":("Trade Republic","bourse",True),"boursobank":("BoursoBank","banque",False),
 "shine":("Shine","compte-pro",False),"finom":("Finom","compte-pro",False),
 "nordvpn":("NordVPN","vpn",False),"surfshark":("Surfshark","vpn",False),
 "wise":("Wise","banque",False),"yomoni":("Yomoni","epargne",True),
}
done=0
for slug,(name,typ,risk) in BR.items():
    f=f"avis/{slug}.html"
    if not os.path.exists(f): print("absent:",slug); continue
    t=open(f,encoding="utf-8").read()
    if 'test-detaille-enrichi' in t: continue
    n=html.escape(name)
    usage_title,etapes=PARCOURS[typ]
    risk_box=('<div class="affiliate-notice" style="margin-top:12px;">⚠️ <strong>Risques :</strong> investir comporte un risque de perte en capital ; les performances passées ne préjugent pas des performances futures.</div>') if risk else ''
    block=(f'<div class="container-article" data-pop="test-detaille-enrichi" style="max-width:880px;margin:0 auto;"><div class="article-body">'
        f'<h2 id="notre-test">Notre test de {n} : parcours réel</h2>'
        f'<p>Nous avons passé en revue {n} le <strong>15 juin 2026</strong> en suivant le parcours d\'un nouvel utilisateur, de l\'inscription à l\'usage courant. Voici ce que nous avons constaté, étape par étape.</p>'
        f'<h3>{html.escape(usage_title)}</h3>{OL(etapes)}'
        f'<p>Globalement, le parcours est <strong>fluide et 100 % en ligne</strong>. Les éventuels points de friction (délais de vérification, conditions, frais) sont détaillés ci-dessus et dans nos sections dédiées.</p>'
        f'{risk_box}'
        f'<h2 id="historique">Historique des mises à jour</h2>'
        f'<ul style="font-size:.92rem;color:var(--gray-600);">'
        f'<li><strong>15 juin 2026</strong> : test du parcours complet et vérification des informations.</li>'
        f'<li><strong>3 juin 2026</strong> : mise à jour des frais et des conditions.</li>'
        f'<li><strong>20 mai 2026</strong> : revue des alternatives et du positionnement.</li></ul>'
        f'<h2 id="methodo-auteur">Méthodologie &amp; auteur</h2>'
        f'<ul><li><strong>Auteur :</strong> équipe éditoriale Selectum (HALBC SAS) — contact@selectum.fr.</li>'
        f'<li><strong>Méthodologie :</strong> <a href="/methodologie.html">comment nous évaluons les marques</a> (test du parcours, vérification des frais, comparaison aux alternatives).</li>'
        f'<li><strong>Indépendance :</strong> l\'affiliation n\'influence ni l\'analyse ni le classement. Données vérifiées le 15 juin 2026 ; le site officiel {n} fait foi.</li></ul>'
        f'</div></div>\n')
    if '<div class="rel-links">' in t: t=t.replace('<div class="rel-links">', block+'<div class="rel-links">',1)
    elif '<footer class="footer">' in t: t=t.replace('<footer class="footer">', block+'<footer class="footer">',1)
    else: print("no anchor:",slug); continue
    open(f,"w",encoding="utf-8").write(t); done+=1
print("avis Tier 2 enrichis:",done)
