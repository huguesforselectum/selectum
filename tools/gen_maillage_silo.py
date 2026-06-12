#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maillage interne en silos : module 'Offres populaires [categorie]' sur les pages fortes
(comparatifs/avis/guides indexes), scope par categorie, ancres variees. + bloc home."""
import glob, re, os, html

# catkey par comparatif (categorie reelle)
COMP2CAT={}
for b in ["crypto","crypto-debutant","crypto-frais-bas","acheter-bitcoin"]: COMP2CAT[b]="crypto"
COMP2CAT["hebergement-web"]="hebergement"
for b in ["banque-en-ligne","cartes-famille"]: COMP2CAT[b]="banque"
COMP2CAT["comptes-pro"]="compte-pro"; COMP2CAT["transfert-argent"]="compte-pro"; COMP2CAT["change-multidevises"]="compte-pro"
COMP2CAT["terminaux-paiement"]="paiement"
COMP2CAT["trading-bourse"]="bourse"
for b in ["vpn","bloqueur-de-pub"]: COMP2CAT[b]="vpn"
for b in ["assurance-animaux","mutuelle-sante","assurance-auto","assurance-habitation","assurance-emprunteur"]: COMP2CAT[b]="assurance"
for b in ["assurance-vie","epargne-pilotee","per-retraite","crowdlending-p2p"]: COMP2CAT[b]="epargne"

# brand -> catkey via 1re apparition dans un comparatif categorie
brand2cat={}
for f in glob.glob("comparatifs/*.html"):
    base=os.path.basename(f)[:-5]
    if base not in COMP2CAT: continue
    for m in re.finditer(r'/go/([a-z0-9-]+)', open(f,encoding="utf-8").read()):
        brand2cat.setdefault(m.group(1), COMP2CAT[base])

# Modules par categorie : (url, ancre) — ancres variees
MOD={
 "crypto":[("/code-promo/coinbase.html","Code promo Coinbase"),("/code-promo/bitpanda.html","Offres Bitpanda"),
   ("/code-promo/kraken.html","Code promo Kraken"),("/code-promo/binance.html","Réductions Binance"),
   ("/code-promo/etoro.html","Promo eToro"),("/etudes/barometre-frais-crypto.html","Baromètre des frais crypto"),
   ("/comparatifs/crypto.html","Meilleure application crypto")],
 "hebergement":[("/code-promo/ionos.html","Code promo IONOS"),("/code-promo/hostinger.html","Offres Hostinger"),
   ("/code-promo/ovhcloud.html","Code promo OVHcloud"),("/code-promo/o2switch.html","Réductions o2switch"),
   ("/etudes/classement-hebergeurs-moins-chers.html","Hébergeurs les moins chers"),
   ("/comparatifs/hebergement-web.html","Meilleur hébergeur web")],
 "banque":[("/code-promo/n26.html","Code promo N26"),("/code-promo/revolut.html","Offres Revolut"),
   ("/code-promo/boursobank.html","Code promo BoursoBank"),("/code-promo/monabanq.html","Promo Monabanq"),
   ("/comparatifs/banque-en-ligne.html","Meilleure banque en ligne")],
 "compte-pro":[("/code-promo/qonto.html","Code promo Qonto"),("/code-promo/shine.html","Offres Shine"),
   ("/code-promo/finom.html","Code promo Finom"),("/code-promo/wise.html","Réductions Wise"),
   ("/comparatifs/comptes-pro.html","Meilleur compte pro")],
 "bourse":[("/code-promo/xtb.html","Code promo XTB"),("/code-promo/trade-republic.html","Offres Trade Republic"),
   ("/code-promo/etoro.html","Code promo eToro"),("/code-promo/degiro.html","Promo DEGIRO"),
   ("/comparatifs/trading-bourse.html","Meilleur courtier en bourse")],
 "paiement":[("/code-promo/sumup.html","Code promo SumUp"),("/code-promo/flatpay.html","Offres Flatpay"),
   ("/code-promo/zettle.html","Code promo Zettle"),("/code-promo/mypos.html","Réductions myPOS"),
   ("/comparatifs/terminaux-paiement.html","Meilleur terminal de paiement")],
 "vpn":[("/code-promo/expressvpn.html","Code promo ExpressVPN"),("/code-promo/nordvpn.html","Offres NordVPN"),
   ("/code-promo/surfshark.html","Code promo Surfshark"),("/code-promo/cyberghost.html","Promo CyberGhost"),
   ("/comparatifs/vpn.html","Meilleur VPN")],
 "assurance":[("/code-promo/santevet.html","Code promo SantéVet"),("/code-promo/dalma.html","Offres Dalma"),
   ("/comparatifs/assurance-animaux.html","Meilleure assurance animaux")],
 "epargne":[("/code-promo/linxea.html","Code promo Linxea"),("/code-promo/nalo.html","Offres Nalo"),
   ("/code-promo/yomoni.html","Code promo Yomoni"),("/comparatifs/assurance-vie.html","Meilleure assurance-vie")],
}
TITLE={"crypto":"crypto","hebergement":"hébergement web","banque":"banque en ligne","compte-pro":"compte pro",
 "bourse":"bourse","paiement":"terminal de paiement","vpn":"VPN","assurance":"assurance","epargne":"épargne"}

def page_cat(path, txt):
    base=os.path.basename(path)[:-5]
    if path.startswith("comparatifs/") and base in COMP2CAT: return COMP2CAT[base]
    # sinon : majorite des marques /go
    cats={}
    for m in re.finditer(r'/go/([a-z0-9-]+)', txt):
        c=brand2cat.get(m.group(1))
        if c: cats[c]=cats.get(c,0)+1
    # ou via le slug (avis/guides/<slug>)
    if not cats:
        c=brand2cat.get(base.split("-vs-")[0].replace("avis-","").replace("alternative-",""))
        if c: return c
    return max(cats,key=cats.get) if cats else None

def module_html(cat, self_path):
    items=[(u,a) for u,a in MOD[cat] if not u.endswith(os.path.basename(self_path))]
    chips="".join(f'<a href="{u}" class="rel-chip">{html.escape(a)} →</a>' for u,a in items)
    return (f'<div class="container-article" data-pop="1" style="max-width:1080px;margin:0 auto;">'
        f'<div class="rel-links"><h2>💡 Offres populaires en {TITLE[cat]}</h2><div class="rel-list">{chips}</div></div></div>\n')

inj=0
for path in glob.glob("comparatifs/*.html")+glob.glob("avis/*.html")+glob.glob("guides/*.html"):
    txt=open(path,encoding="utf-8").read()
    if 'data-pop="1"' in txt: continue
    if 'content="noindex' in txt: continue
    cat=page_cat(path,txt)
    if not cat or cat not in MOD: continue
    mod=module_html(cat,path)
    if '<footer class="footer">' in txt:
        txt=txt.replace('<footer class="footer">', mod+'<footer class="footer">',1)
        open(path,"w",encoding="utf-8").write(txt); inj+=1
print("module 'offres populaires' injecté sur",inj,"pages (silo)")

# ===== Bloc home : offres les plus consultees =====
home=open("index.html",encoding="utf-8").read()
if 'offres-consultees' not in home:
    HL=[("/code-promo/coinbase.html","Code promo Coinbase"),("/code-promo/ionos.html","Code promo IONOS"),
        ("/code-promo/bitpanda.html","Code promo Bitpanda"),("/code-promo/hostinger.html","Code promo Hostinger"),
        ("/code-promo/qonto.html","Code promo Qonto"),("/code-promo/xtb.html","Code promo XTB"),
        ("/code-promo/n26.html","Code promo N26"),("/comparatifs/crypto.html","Meilleure application crypto"),
        ("/comparatifs/hebergement-web.html","Meilleur hébergeur web"),("/code-promo.html","Tous les codes promo")]
    chips="".join(f'<a href="{u}" class="hub-item">{html.escape(a)}</a>' for u,a in HL)
    sec=(f'<section class="section" id="offres-consultees"><div class="container">'
        f'<div class="section-title"><div class="eyebrow">Bons plans</div><h2>Les offres les plus consultées</h2></div>'
        f'<div class="hub-grid">{chips}</div></div></section>\n')
    if '<footer' in home:
        home=home.replace('<footer', sec+'<footer',1)
        open("index.html","w",encoding="utf-8").write(home); print("bloc home 'offres les plus consultées' ajouté")
else: print("bloc home déjà présent")
