#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""3 outils interactifs : calculateur TPE, baromètre comptes pro, checklist indépendant."""
import html, json, os
FONT="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"

def head(slug,title,desc,faq,leaf):
    url=f"https://selectum.fr/outils/{slug}.html"
    t=html.escape(title);d=html.escape(desc)
    art=json.dumps({"@context":"https://schema.org","@type":"WebApplication","name":title,"description":desc,
      "applicationCategory":"FinanceApplication","operatingSystem":"Web","offers":{"@type":"Offer","price":"0","priceCurrency":"EUR"},
      "url":url,"publisher":{"@type":"Organization","name":"Selectum"}},ensure_ascii=False)
    fq=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},ensure_ascii=False)
    bc=json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Accueil","item":"https://selectum.fr/"},
      {"@type":"ListItem","position":2,"name":"Outils","item":"https://selectum.fr/outils.html"},
      {"@type":"ListItem","position":3,"name":leaf,"item":url}]},ensure_ascii=False)
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title><meta name="description" content="{d}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="{url}"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{art}</script>
<script type="application/ld+json">{fq}</script>
<script type="application/ld+json">{bc}</script>
<style>
.tool-form{{background:var(--gray-50);border:1px solid var(--gray-200);border-radius:14px;padding:22px;margin:20px 0;}}
.tool-row{{display:grid;grid-template-columns:1fr 160px;gap:12px;align-items:center;margin-bottom:12px;}}
.tool-row label{{font-weight:600;color:var(--gray-800);font-size:.95rem;}}
.tool-row input,.tool-row select{{padding:10px 12px;border:1px solid var(--gray-300);border-radius:8px;font:inherit;width:100%;box-sizing:border-box;}}
.tool-note{{font-size:.8rem;color:var(--gray-500);margin-top:-6px;margin-bottom:10px;}}
.result-card{{border:1px solid var(--gray-200);border-radius:12px;padding:16px 18px;margin:10px 0;display:flex;align-items:center;gap:14px;flex-wrap:wrap;}}
.result-card.best{{border-color:#16a34a;background:#f0fdf4;}}
.result-card .rc-name{{font-weight:800;min-width:90px;}}
.result-card .rc-cost{{font-weight:800;font-size:1.15rem;margin-left:auto;}}
.result-card .rc-detail{{font-size:.82rem;color:var(--gray-500);width:100%;}}
.check-item{{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border:1px solid var(--gray-200);border-radius:10px;margin-bottom:8px;cursor:pointer;background:#fff;}}
.check-item input{{margin-top:3px;}}
.check-item.done{{background:#f0fdf4;border-color:#bbf7d0;}}
.check-item.done span{{text-decoration:line-through;color:var(--gray-500);}}
.progress-wrap{{background:var(--gray-200);border-radius:99px;height:10px;margin:14px 0 22px;overflow:hidden;}}
.progress-bar{{background:linear-gradient(90deg,#1B5FD9,#16a34a);height:100%;width:0;transition:width .3s;}}
@media print{{.header,.footer,.affiliate-notice,.rel-links,.no-print{{display:none!important}}}}
@media (max-width:640px){{.tool-row{{grid-template-columns:1fr;}}}}
</style>
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/outils.html" class="btn-primary">Tous nos outils →</a></div>
</div></div></header>'''

def footer():
    return '''<footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none;padding:24px 0;">
<p>© 2026 Selectum — Un service de HALBC SAS. <a href="/mentions-legales.html" style="color:var(--gray-500)">Mentions légales</a> · <a href="/politique-confidentialite.html" style="color:var(--gray-500)">Confidentialité</a></p>
</div></div></footer></body></html>'''

def hero(h1,sub,leaf):
    return f'''<div class="article-header"><div class="container-article">
  <div class="article-breadcrumb"><a href="/index.html">Accueil</a><span>/</span><a href="/outils.html">Outils</a><span>/</span>{html.escape(leaf)}</div>
  <h1>{html.escape(h1)}</h1>
  <p class="updated">🗓️ Mis à jour le 11 juin 2026 — outil gratuit, sans inscription</p>
  <p class="subtitle" style="color:rgba(255,255,255,.85)">{html.escape(sub)}</p>
</div></div>'''

def faq_html(faq):
    return '<div class="faq"><h2>❓ Questions fréquentes</h2>'+''.join(
      f'<div class="faq-item"><div class="faq-question">{html.escape(q)} <span>+</span></div><div class="faq-answer">{html.escape(a)}</div></div>' for q,a in faq)+'</div>'

def rel(chips):
    return '<div class="rel-links"><h2>À lire aussi</h2><div class="rel-list">'+''.join(
      f'<a href="{u}" class="rel-chip">{html.escape(l)} →</a>' for u,l in chips)+'</div></div>'

# ============ 1. CALCULATEUR TPE ============
faq1=[("Comment est calculé le coût réel d'un TPE ?","Coût mensuel = commissions (CA carte × taux) + abonnement éventuel + amortissement du matériel (prix d'achat lissé sur la durée d'utilisation). Notre calculateur additionne ces trois postes."),
("Quel TPE est le moins cher pour un petit volume ?","Pour de petits volumes d'encaissement, les lecteurs sans abonnement (type SumUp) sont généralement les plus économiques : on ne paie qu'à la transaction."),
("À partir de quel chiffre d'affaires un abonnement fixe devient-il rentable ?","Quand les commissions économisées dépassent le coût de l'abonnement. Le calculateur vous montre le point de bascule selon votre CA carte mensuel."),
("Les taux pré-remplis sont-ils contractuels ?","Non, ce sont des valeurs indicatives publiques que vous pouvez modifier. Les tarifs réels dépendent des offres en vigueur et de votre profil — vérifiez sur le site de chaque acteur.")]
calc=head("calculateur-cout-tpe","Calculateur : coût réel d'un terminal de paiement (TPE) 2026",
 "Calculez le coût réel de votre TPE : commissions, abonnement, matériel amorti. Comparez SumUp, Zettle, myPOS et Flatpay selon votre chiffre d'affaires carte.",
 faq1,"Calculateur coût TPE")
calc+=hero("Calculateur : le coût réel de votre terminal de paiement",
 "Commissions + abonnement + matériel : découvrez ce que votre TPE vous coûte vraiment chaque mois, selon votre activité.","Calculateur coût TPE")
calc+='''<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Taux indicatifs modifiables — vérifiez les conditions en vigueur chez chaque acteur.</div>
<div class="tool-form" id="calc">
  <div class="tool-row"><label for="ca">CA encaissé par carte / mois (€)</label><input type="number" id="ca" value="5000" min="0" step="100"></div>
  <div class="tool-row"><label for="duree">Durée d'amortissement du matériel (mois)</label><input type="number" id="duree" value="36" min="1"></div>
  <p class="tool-note">Les taux et prix ci-dessous sont <strong>pré-remplis à titre indicatif</strong> : ajustez-les selon le devis ou la grille tarifaire réelle.</p>
  <div style="overflow-x:auto;"><table class="comparison-table" style="min-width:560px;">
    <thead><tr><th>Acteur</th><th>Commission (%)</th><th>Abonnement (€/mois)</th><th>Matériel (€)</th></tr></thead>
    <tbody id="rows"></tbody>
  </table></div>
</div>
<h2>Résultat : coût mensuel estimé</h2>
<div id="results"></div>
<div class="highlight-box"><p id="verdict">💡 Renseignez votre CA pour voir le classement.</p></div>
<h2>Comment lire ce résultat ?</h2>
<p>Le <strong>coût réel d'un TPE</strong> ne se limite pas à la commission affichée : il faut ajouter l'abonnement éventuel et le <strong>matériel amorti</strong> sur sa durée de vie. À faible volume, le « sans abonnement » gagne presque toujours ; à fort volume, un abonnement fixe avec commission réduite peut devenir nettement plus rentable.</p>
<p>Pour le détail des offres : <a href="/comparatifs/terminaux-paiement.html">comparatif des terminaux de paiement</a>, <a href="/comparatifs/tpe-petit-commerce.html">TPE pour petit commerce</a>, <a href="/comparatifs/tpe-micro-entreprise.html">TPE micro-entreprise</a>.</p>
'''+faq_html(faq1)+rel([("/comparatifs/terminaux-paiement.html","Comparatif terminaux de paiement"),("/comparatifs/tpe-gratuit.html","TPE gratuit : que valent les offres ?"),("/outils/barometre-frais-comptes-pro.html","Baromètre des frais des comptes pro"),("/outils/checklist-independant.html","Checklist : lancer son activité d'indépendant")])+'''
</div></div>
<script>
var ACT=[
 {n:"SumUp",go:"/go/sumup",com:1.75,abo:0,mat:39},
 {n:"Zettle",go:"/go/zettle",com:1.75,abo:0,mat:29},
 {n:"myPOS",go:"/go/mypos",com:1.75,abo:0,mat:29},
 {n:"Flatpay",go:"/go/flatpay",com:0.99,abo:49,mat:0}
];
function build(){var tb=document.getElementById("rows");tb.innerHTML=ACT.map(function(a,i){
 return '<tr><td><strong>'+a.n+'</strong></td>'+
 '<td><input type="number" step="0.01" min="0" data-i="'+i+'" data-k="com" value="'+a.com+'" style="width:90px;padding:6px;border:1px solid var(--gray-300);border-radius:6px;"></td>'+
 '<td><input type="number" step="1" min="0" data-i="'+i+'" data-k="abo" value="'+a.abo+'" style="width:90px;padding:6px;border:1px solid var(--gray-300);border-radius:6px;"></td>'+
 '<td><input type="number" step="1" min="0" data-i="'+i+'" data-k="mat" value="'+a.mat+'" style="width:90px;padding:6px;border:1px solid var(--gray-300);border-radius:6px;"></td></tr>';}).join("");}
function fmt(x){return x.toLocaleString("fr-FR",{maximumFractionDigits:0})+" €";}
function calc(){
 var ca=parseFloat(document.getElementById("ca").value)||0;
 var du=Math.max(1,parseFloat(document.getElementById("duree").value)||36);
 document.querySelectorAll("#rows input").forEach(function(inp){ACT[+inp.dataset.i][inp.dataset.k]=parseFloat(inp.value)||0;});
 var res=ACT.map(function(a){var commission=ca*a.com/100;var amort=a.mat/du;
   return {n:a.n,go:a.go,total:commission+a.abo+amort,commission:commission,abo:a.abo,amort:amort};})
  .sort(function(x,y){return x.total-y.total;});
 document.getElementById("results").innerHTML=res.map(function(r,i){
  return '<div class="result-card'+(i===0?' best':'')+'"><div class="rc-name">'+(i===0?'🏆 ':'')+r.n+'</div>'+
  '<a href="'+r.go+'" class="btn-green" target="_blank" rel="sponsored nofollow noopener" style="padding:8px 14px;font-size:.85rem;">Voir l\\u2019offre →</a>'+
  '<div class="rc-cost">'+fmt(r.total)+'/mois</div>'+
  '<div class="rc-detail">Commissions '+fmt(r.commission)+' · abonnement '+fmt(r.abo)+' · matériel amorti '+fmt(r.amort)+' — soit '+fmt(r.total*12)+'/an</div></div>';}).join("");
 var b=res[0],s=res[1];
 document.getElementById("verdict").innerHTML='💡 Pour <strong>'+fmt(ca)+'</strong> de CA carte mensuel, <strong>'+b.n+'</strong> est le plus économique ('+fmt(b.total)+'/mois), soit <strong>'+fmt((s.total-b.total)*12)+' d\\u2019économie par an</strong> vs '+s.n+'.';
}
build();calc();
document.getElementById("calc").addEventListener("input",calc);
</script>
'''+footer()

# ============ 2. BAROMÈTRE COMPTES PRO ============
faq2=[("Quels frais regarder sur un compte pro ?","L'abonnement mensuel, les frais de virements au-delà du quota, le coût de la carte, les commissions de mouvement et les frais d'encaissement (TPE, prélèvements)."),
("Un compte pro gratuit existe-t-il vraiment ?","Des offres d'entrée à 0 €/mois existent (Shine, Finom), souvent avec des quotas limités. Dès que l'activité grossit, un plan payant devient souvent plus rentable que les frais hors forfait."),
("Le baromètre est-il mis à jour ?","Oui, les tarifs d'entrée affichés correspondent aux offres publiques constatées à la date de mise à jour. Vérifiez toujours la grille en vigueur avant de souscrire."),
("Néobanque pro ou banque traditionnelle ?","Les comptes pro en ligne sont en général 2 à 4 fois moins chers que les banques traditionnelles pour les indépendants et TPE, avec une ouverture en quelques minutes.")]
baro=head("barometre-frais-comptes-pro","Baromètre 2026 des frais des comptes pro : qui est le moins cher ?",
 "Baromètre des frais des comptes pro 2026 : abonnements, cartes, virements de Qonto, Shine, Blank, Finom. Simulez votre coût annuel selon votre profil.",
 faq2,"Baromètre frais comptes pro")
baro+=hero("Baromètre des frais des comptes pro",
 "Abonnement, carte, virements : comparez le coût annuel réel des comptes professionnels selon votre profil.","Baromètre frais comptes pro")
baro+='''<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Tarifs d'entrée publics constatés en juin 2026 — susceptibles d'évoluer.</div>
<div class="tool-form">
  <div class="tool-row"><label for="profil">Votre profil</label>
  <select id="profil"><option value="micro">Micro-entrepreneur</option><option value="tpe">TPE / société (SASU, EURL…)</option></select></div>
</div>
<h2>Le baromètre <span id="bar-label" style="color:var(--gray-500);font-size:1rem;font-weight:500;"></span></h2>
<div id="bar"></div>
<div class="highlight-box"><p>💡 <strong>Lecture :</strong> coût d'entrée = abonnement du plan le moins cher adapté au profil, hors frais variables (virements hors quota, retraits, encaissements). Pour une comparaison complète, voyez le <a href="/comparatifs/comptes-pro.html">comparatif des comptes pro</a>.</p></div>
<h2>Ce que cachent les « à partir de »</h2>
<p>Un tarif d'appel bas peut masquer des <strong>frais variables</strong> élevés : virements supplémentaires facturés à l'unité, cartes physiques en option, commissions de mouvement. Le bon réflexe : estimer votre <strong>volume mensuel de virements et d'encaissements</strong>, puis comparer le coût total — c'est souvent là que le classement s'inverse.</p>
<p>À lire en complément : <a href="/comparatifs/comptes-pro.html">comparatif comptes pro</a>, <a href="/avis/qonto.html">avis Qonto</a>, <a href="/avis/shine.html">avis Shine</a>, <a href="/comparatifs/logiciels-comptabilite.html">comparatif logiciels de comptabilité</a>.</p>
'''+faq_html(faq2)+rel([("/comparatifs/comptes-pro.html","Comparatif comptes pro"),("/outils/calculateur-cout-tpe.html","Calculateur : coût réel d'un TPE"),("/outils/checklist-independant.html","Checklist : lancer son activité d'indépendant"),("/comparatifs/facturation.html","Comparatif logiciels de facturation")])+'''
</div></div>
<script>
var BANKS=[
 {n:"Shine",go:"/go/shine",micro:0,tpe:14.9,note:"Offre d'entrée gratuite, plans payants pour les besoins avancés"},
 {n:"Finom",go:"/go/finom",micro:0,tpe:14,note:"Plan Solo gratuit, cashback sur les plans payants"},
 {n:"Blank",go:"/go/blank",micro:8,tpe:17,note:"Tout-en-un avec outils administratifs intégrés"},
 {n:"Qonto",go:"/go/qonto",micro:9,tpe:29,note:"La référence des comptes pro en ligne, très complet"}
];
function fmt2(x){return x.toLocaleString("fr-FR",{maximumFractionDigits:2})+" €";}
function render(){
 var p=document.getElementById("profil").value;
 document.getElementById("bar-label").textContent=p==="micro"?"— profil micro-entrepreneur":"— profil TPE / société";
 var rows=BANKS.map(function(b){return {n:b.n,go:b.go,m:p==="micro"?b.micro:b.tpe,note:b.note};})
  .sort(function(a,b){return a.m-b.m;});
 var max=Math.max.apply(null,rows.map(function(r){return r.m;}))||1;
 document.getElementById("bar").innerHTML=rows.map(function(r,i){
  var w=Math.max(4,Math.round(r.m/max*100));
  return '<div class="result-card'+(i===0?' best':'')+'"><div class="rc-name">'+(i===0?'🏆 ':'')+r.n+'</div>'+
  '<a href="'+r.go+'" class="btn-green" target="_blank" rel="sponsored nofollow noopener" style="padding:8px 14px;font-size:.85rem;">Voir l\\u2019offre →</a>'+
  '<div class="rc-cost">'+(r.m===0?"0 €":fmt2(r.m))+'/mois</div>'+
  '<div style="width:100%;background:var(--gray-100);border-radius:99px;height:8px;"><div style="width:'+w+'%;height:8px;border-radius:99px;background:'+(i===0?'#16a34a':'#1B5FD9')+';"></div></div>'+
  '<div class="rc-detail">'+r.note+' — soit '+fmt2(r.m*12)+'/an</div></div>';}).join("");
}
render();document.getElementById("profil").addEventListener("change",render);
</script>
'''+footer()

# ============ 3. CHECKLIST INDÉPENDANT ============
faq3=[("Quelles démarches pour devenir indépendant en France ?","Choisir un statut (micro-entreprise, EI, SASU, EURL…), immatriculer l'activité sur le guichet unique de l'INPI, ouvrir un compte dédié, souscrire les assurances nécessaires et mettre en place facturation et comptabilité."),
("Un compte bancaire dédié est-il obligatoire ?","Pour la micro-entreprise, un compte dédié à l'activité est obligatoire au-delà de 10 000 € de CA annuel pendant deux années consécutives. Pour les sociétés, le compte professionnel est requis dès la création."),
("Cette checklist est-elle gratuite ?","Oui, entièrement gratuite et sans inscription. Votre progression est sauvegardée dans votre navigateur et la liste est imprimable."),
("Quelles assurances pour un indépendant ?","Selon l'activité : responsabilité civile professionnelle (RC Pro), garantie décennale pour le bâtiment, multirisque locale, et une mutuelle santé adaptée aux indépendants.")]
CHK=[("Avant de se lancer",[
 "Valider l'idée : premiers clients potentiels identifiés, prix testés",
 "Choisir le statut juridique (micro-entreprise, EI, SASU, EURL…)",
 "Estimer le prévisionnel simple : charges, seuil de rentabilité",
 "Vérifier les qualifications/diplômes exigés pour l'activité réglementée",
 "Choisir une domiciliation (domicile, local, société de domiciliation)"]),
("Création de l'activité",[
 "Immatriculer l'activité sur le guichet unique (INPI)",
 "Obtenir le SIREN/SIRET et vérifier l'avis INSEE",
 "Ouvrir un compte bancaire dédié ou professionnel",
 "Souscrire la RC Pro (et décennale si bâtiment)",
 "Choisir une mutuelle / prévoyance d'indépendant",
 "Déclarer l'option fiscale (versement libératoire, TVA…)"]),
("Gestion courante",[
 "Mettre en place un outil de facturation conforme (mentions légales)",
 "Organiser la comptabilité : logiciel ou expert-comptable",
 "Programmer les déclarations Urssaf (mensuelles ou trimestrielles)",
 "Suivre la TVA si assujetti (seuils de franchise)",
 "Provisionner impôts et cotisations sur un compte d'épargne",
 "Encaisser par carte si besoin : choisir un TPE adapté",
 "Sauvegarder les justificatifs (10 ans pour les documents comptables)"])]
chk=head("checklist-independant","Checklist gratuite 2026 : ouvrir et gérer son activité d'indépendant",
 "Checklist gratuite et interactive pour lancer son activité d'indépendant : statut, immatriculation INPI, compte pro, assurances, facturation, Urssaf. Imprimable.",
 faq3,"Checklist indépendant")
chk+=hero("Checklist : ouvrir et gérer son activité d'indépendant",
 "Toutes les étapes pour créer puis gérer votre activité, à cocher au fur et à mesure. Gratuit, sauvegardé dans votre navigateur, imprimable.","Checklist indépendant")
items="".join(f'<h2>{html.escape(sec)}</h2>'+"".join(
 f'<label class="check-item"><input type="checkbox" data-k="chk-{si}-{ii}"><span>{html.escape(it)}</span></label>'
 for ii,it in enumerate(its)) for si,(sec,its) in enumerate(CHK))
chk+=f'''<div class="container-article"><div class="article-body" style="max-width:880px;margin:0 auto;">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous. Informations générales — elles ne remplacent pas un conseil juridique ou comptable personnalisé.</div>
<div class="no-print" style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;">
  <div class="progress-wrap" style="flex:1;min-width:200px;"><div class="progress-bar" id="pbar"></div></div>
  <strong id="pct">0 %</strong>
  <button onclick="window.print()" class="btn-primary" style="border:none;cursor:pointer;font:inherit;">🖨️ Imprimer</button>
  <button onclick="resetChk()" style="border:1px solid var(--gray-300);background:#fff;border-radius:8px;padding:10px 14px;cursor:pointer;font:inherit;">Réinitialiser</button>
</div>
{items}
<div class="highlight-box"><p>💡 <strong>Pour vous équiper :</strong> <a href="/comparatifs/comptes-pro.html">choisir un compte pro</a> · <a href="/outils/barometre-frais-comptes-pro.html">baromètre des frais</a> · <a href="/comparatifs/facturation.html">logiciel de facturation</a> · <a href="/comparatifs/logiciels-comptabilite.html">comptabilité</a> · <a href="/outils/calculateur-cout-tpe.html">calculer le coût d'un TPE</a> · <a href="/comparatifs/mutuelle-sante.html">mutuelle santé</a>.</p></div>
'''+faq_html(faq3)+rel([("/comparatifs/comptes-pro.html","Comparatif comptes pro"),("/comparatifs/facturation.html","Comparatif logiciels de facturation"),("/outils/calculateur-cout-tpe.html","Calculateur : coût réel d'un TPE"),("/outils/barometre-frais-comptes-pro.html","Baromètre des frais des comptes pro")])+'''
</div></div>
<script>
var boxes=document.querySelectorAll(".check-item input");
function save(){var s={};boxes.forEach(function(b){s[b.dataset.k]=b.checked;});localStorage.setItem("selectum-checklist",JSON.stringify(s));}
function update(){var done=0;boxes.forEach(function(b){b.closest(".check-item").classList.toggle("done",b.checked);if(b.checked)done++;});
 var p=Math.round(done/boxes.length*100);document.getElementById("pbar").style.width=p+"%";document.getElementById("pct").textContent=p+" %";}
function resetChk(){boxes.forEach(function(b){b.checked=false;});save();update();}
try{var s=JSON.parse(localStorage.getItem("selectum-checklist")||"{}");boxes.forEach(function(b){b.checked=!!s[b.dataset.k];});}catch(e){}
boxes.forEach(function(b){b.addEventListener("change",function(){save();update();});});
update();
</script>
'''+footer()

# ============ HUB outils.html ============
hub=f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="theme-color" content="#1B5FD9"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Outils gratuits : calculateurs et checklists | Selectum</title><meta name="description" content="Nos outils gratuits pour pros et indépendants : calculateur de coût de TPE, baromètre des frais des comptes pro, checklist pour lancer son activité.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="{FONT}" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"><link rel="icon" type="image/svg+xml" href="/assets/selectum-appicon.svg">
<link rel="stylesheet" href="/css/style.css">
<link rel="canonical" href="https://selectum.fr/outils.html"><meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Selectum">
<meta property="og:title" content="Outils gratuits : calculateurs et checklists | Selectum"><meta property="og:description" content="Calculateur de coût de TPE, baromètre des frais des comptes pro, checklist indépendant : nos outils gratuits, sans inscription.">
<meta property="og:url" content="https://selectum.fr/outils.html"><meta property="og:image" content="https://selectum.fr/assets/selectum-logo.png">
<meta name="twitter:card" content="summary">
</head><body>
<header class="header"><div class="container"><div class="header-inner">
<a href="/index.html" class="logo"><img src="/assets/selectum-logo.svg" alt="Selectum — Comparatifs indépendants" class="logo-img"></a>
<nav class="nav"></nav><div class="header-cta"><a href="/autres-comparatifs.html" class="btn-primary">Voir les comparatifs →</a></div>
</div></div></header>
<div class="hero" style="padding:56px 0 48px;"><div class="container"><div class="hero-content">
<h1>Outils gratuits</h1><p>Calculateurs et checklists pour décider vite et bien — sans inscription.</p>
</div></div></div>
<section class="section"><div class="container"><div class="section-title"><div class="eyebrow">Pros &amp; indépendants</div><h2>Nos outils du moment</h2></div>
<div class="hub-grid">
<a href="/outils/calculateur-cout-tpe.html" class="hub-item">🧮 Calculateur : coût réel d'un terminal de paiement (TPE)</a>
<a href="/outils/barometre-frais-comptes-pro.html" class="hub-item">📊 Baromètre des frais des comptes pro</a>
<a href="/outils/checklist-independant.html" class="hub-item">✅ Checklist gratuite : ouvrir et gérer son activité d'indépendant</a>
</div></div></section>
'''+footer()

os.makedirs("outils",exist_ok=True)
open("outils/calculateur-cout-tpe.html","w",encoding="utf-8").write(calc)
open("outils/barometre-frais-comptes-pro.html","w",encoding="utf-8").write(baro)
open("outils/checklist-independant.html","w",encoding="utf-8").write(chk)
open("outils.html","w",encoding="utf-8").write(hub)
print("4 fichiers écrits : 3 outils + hub outils.html")
