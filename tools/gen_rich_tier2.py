#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Étend le template Tier 1 (riche) aux grosses marques Tier 2 non-affiliées.
Réutilise gen_rich_affiliate (head/gen_codepromo/gen_parrainage/data)."""
import os

src = open("tools/gen_rich_affiliate.py", encoding="utf-8").read()
prefix = src.split("for slug,name,cat,compar,compar_label,bonus,alts,risk,has_guide in BR:", 1)[0]
ns = {}
exec(prefix, ns)
gen_codepromo = ns["gen_codepromo"]; gen_parrainage = ns["gen_parrainage"]

# Compléter les descriptions d'alternatives
ns["ALTDESC"].update({
 "shine":"Compte pro + outils admin","finom":"Plan gratuit + cashback","blank":"Tout-en-un indépendants",
 "n26":"Banque mobile sans frais de tenue","bunq":"Néobanque flexible, sous-comptes","boursobank":"Banque en ligne complète (groupe SG)",
 "monabanq":"Banque en ligne, service client salué","revolut":"Compte mobile multidevises + cashback","qonto":"La référence du compte pro",
 "ionos":"Prix d'appel agressifs, complet","hostinger":"Souvent le moins cher à l'entrée","ovhcloud":"Acteur français, VPS/cloud",
 "o2switch":"Offre unique simple et lisible","planethoster":"Mutualisé/cloud, France-Canada","infomaniak":"Hébergeur suisse écolo",
 "kraken":"App crypto axée sécurité","coinhouse":"Acteur français régulé","coinbase":"Application crypto grand public",
 "bitpanda":"Acteur européen tout-en-un","binance":"Le plus gros volume mondial","trade-republic":"Plans d'épargne, 1 €/ordre",
 "xtb":"0 % commission actions (seuil)","degiro":"Courtier low-cost","trading-212":"Actions et ETF sans commission","etoro":"Crypto + actions/ETF, social",
 "expressvpn":"Rapide et fiable, premium","surfshark":"Appareils illimités, pas cher","cyberghost":"Simple, orienté streaming",
 "nordvpn":"Très rapide, gros réseau","protonvpn":"Confidentialité suisse",
})

# slug, name, cat, compar, compar_label, bonus, alts, risk, hubcat, verdict
T2 = [
 ("qonto","Qonto","Compte pro","/comparatifs/comptes-pro.html","comparatif comptes pro",
  "offre de bienvenue / mois offerts sur l'abonnement",["shine","finom","blank"],False,"compte-pro",
  "Qonto est la référence du compte pro en ligne : très complet, fiable, mais pas le moins cher. L'offre de bienvenue est un plus ; choisissez-le surtout pour ses outils de gestion."),
 ("revolut","Revolut","Banque","/comparatifs/banque-en-ligne.html","comparatif banque en ligne",
  "offre de bienvenue (mois Premium offerts selon période)",["n26","bunq","boursobank"],False,"banque",
  "Revolut brille par le multidevises et le change à bon taux. L'offre de bienvenue va et vient ; l'intérêt réel est l'usage international et les sous-comptes."),
 ("ionos","IONOS","Hébergement","/comparatifs/hebergement-web.html","comparatif des hébergeurs web",
  "prix d'appel réduits la première année",["hostinger","ovhcloud","o2switch"],False,"hebergement",
  "IONOS est agressif sur les prix d'appel et très complet (domaines, mail, cloud). Surveillez le tarif de renouvellement, souvent bien plus élevé que la 1re année."),
 ("hostinger","Hostinger","Hébergement","/comparatifs/hebergement-web.html","comparatif des hébergeurs web",
  "réduction forte sur les plans longue durée",["ionos","o2switch","ovhcloud"],False,"hebergement",
  "Hostinger est souvent le moins cher à l'entrée, surtout sur les engagements longs. Le prix grimpe au renouvellement : engagez-vous long pour bloquer le tarif bas."),
 ("ovhcloud","OVHcloud","Hébergement","/comparatifs/hebergement-web.html","comparatif des hébergeurs web",
  "offres mutualisées et VPS à prix réduits",["ionos","hostinger","o2switch"],False,"hebergement",
  "OVHcloud est l'acteur français de référence, surtout fort sur le VPS et le cloud. Le mutualisé reste correct ; le support divise mais les prix sont compétitifs."),
 ("o2switch","o2switch","Hébergement","/comparatifs/hebergement-web.html","comparatif des hébergeurs web",
  "offre unique tout compris",["ionos","hostinger","planethoster"],False,"hebergement",
  "o2switch séduit par son offre unique simple (tout inclus, illimité) et son support français réactif. Pas de prix d'appel trompeur : le tarif reste stable, un vrai plus."),
 ("bitpanda","Bitpanda","Crypto","/comparatifs/crypto.html","comparatif crypto",
  "offre de bienvenue à l'inscription",["kraken","coinhouse","coinbase"],True,"crypto",
  "Bitpanda est l'un des plus simples pour débuter en Europe, avec crypto, actions et métaux. Les frais ne sont pas les plus bas : pour trader sérieusement, comparez."),
 ("binance","Binance","Crypto","/comparatifs/crypto.html","comparatif crypto",
  "offre de bienvenue / réduction de frais à l'inscription",["kraken","bitpanda","coinbase"],True,"crypto",
  "Binance offre le plus grand choix de cryptos et des frais très bas. L'interface est dense : plutôt pour utilisateurs à l'aise, et attention au statut réglementaire local."),
 ("etoro","eToro","Bourse","/comparatifs/trading-bourse.html","comparatif bourse",
  "compte de démonstration et offre de bienvenue selon profil",["trade-republic","xtb","degiro"],True,"bourse",
  "eToro mêle actions, ETF et crypto avec le copy-trading. Pratique pour débuter, mais surveillez les frais de retrait et de change. Investir comporte un risque de perte."),
 ("coinhouse","Coinhouse","Crypto","/comparatifs/crypto.html","comparatif crypto",
  "offre de bienvenue à l'inscription",["kraken","bitpanda","binance"],True,"crypto",
  "Coinhouse rassure par son statut d'acteur français régulé (PSAN) et son accompagnement. Les frais sont plus élevés que les gros exchanges : on paie la simplicité et le support."),
 ("trade-republic","Trade Republic","Bourse","/comparatifs/trading-bourse.html","comparatif bourse",
  "offre de bienvenue et plans d'épargne sans frais",["xtb","degiro","trading-212"],True,"bourse",
  "Trade Republic excelle sur les plans d'épargne automatiques en ETF à 1 €/ordre, et rémunère les liquidités. Idéal pour investir régulièrement et passivement."),
 ("boursobank","BoursoBank","Banque","/comparatifs/banque-en-ligne.html","comparatif banque en ligne",
  "prime de bienvenue à l'ouverture",["n26","revolut","monabanq"],False,"banque",
  "BoursoBank (ex-Boursorama) est une vraie banque en ligne complète avec prime de bienvenue récurrente et frais réduits. Un des meilleurs rapports services/prix du marché."),
 ("shine","Shine","Compte pro","/comparatifs/comptes-pro.html","comparatif comptes pro",
  "offre d'entrée gratuite et bonus selon formule",["qonto","finom","blank"],False,"compte-pro",
  "Shine vise les indépendants avec des outils administratifs (devis, factures, URSSAF). L'offre gratuite suffit pour démarrer ; les fonctions avancées sont payantes."),
 ("finom","Finom","Compte pro","/comparatifs/comptes-pro.html","comparatif comptes pro",
  "plan gratuit et cashback sur les plans payants",["qonto","shine","blank"],False,"compte-pro",
  "Finom propose un plan gratuit et du cashback, intéressant pour les petites structures. Comparez les quotas de virements, vite limités sur l'offre d'entrée."),
 ("nordvpn","NordVPN","Tech","/comparatifs/vpn.html","comparatif VPN",
  "réduction forte sur les abonnements longue durée",["expressvpn","surfshark","cyberghost"],False,"vpn",
  "NordVPN combine vitesse, gros réseau de serveurs et outils annexes. Les grosses réductions ne valent que sur les engagements 2 ans : le mensuel reste cher."),
 ("surfshark","Surfshark","Tech","/comparatifs/vpn.html","comparatif VPN",
  "réduction sur les plans longue durée (appareils illimités)",["nordvpn","expressvpn","cyberghost"],False,"vpn",
  "Surfshark est le meilleur rapport qualité/prix : appareils illimités et tarifs bas sur les engagements longs. Un excellent premier VPN sans se ruiner."),
 ("wise","Wise","Compte pro","/comparatifs/transfert-argent.html","comparatif transfert d'argent",
  "premier transfert offert / frais réduits à l'inscription",["revolut","n26","qonto"],False,"compte-pro",
  "Wise est imbattable sur le change au taux réel et les transferts internationaux transparents. Ce n'est pas une banque : à coupler avec un compte classique."),
]

# compléter VERDICT + HUBCAT
for slug,name,cat,compar,compar_label,bonus,alts,risk,hubcat,verdict in T2:
    ns["VERDICT"][slug]=verdict
    ns["HUBCAT"][slug]=hubcat

n=0
for slug,name,cat,compar,compar_label,bonus,alts,risk,hubcat,verdict in T2:
    has_guide = os.path.exists(f"guides/{slug}.html")
    gen_codepromo(slug,name,cat,compar,compar_label,bonus,alts,risk,has_guide)
    gen_parrainage(slug,name,cat,compar,compar_label,bonus,alts,risk,has_guide)
    n+=1
print("Tier 2 enrichi :", n, "marques (code-promo + parrainage) :", ", ".join(t[0] for t in T2))
