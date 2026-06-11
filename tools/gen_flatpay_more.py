#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html, json
exec(open("tools/gen_flatpay.py").read().split("n=0")[0])  # headhtml, footer, faq_ld

def article(slug,title,desc,h1,body,qa):
    url=f"https://selectum.fr/guides/{slug}.html"
    ld=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-11","dateModified":"2026-06-11","mainEntityOfPage":url},ensure_ascii=False)
    qx=[(html.escape(q),html.escape(a)) for q,a in qa]
    extra=f'\n<script type="application/ld+json">{ld}</script>'+faq_ld(qx)
    faq='<div class="faq"><h2>❓ Questions fréquentes</h2>'+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qx)+'</div>'
    open(f"guides/{slug}.html","w").write(f'''{headhtml(title,desc,url,extra)}
<div class="brand-hero"><div class="container-article">
<div class="brand-hero-logo"><img src="/assets/logos/flatpay.png" alt="Flatpay"></div>
<div class="brand-hero-text"><div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / Guides / Flatpay</div>
<h1>{html.escape(h1)}</h1><p class="updated">🗓️ Mis à jour le 11 juin 2026</p></div></div></div>
<div class="container-article"><div class="article-layout" style="grid-template-columns: 1fr 300px;"><main class="article-body">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
{body}
{faq}
</main>
<aside class="sidebar">
<div class="sidebar-cta"><h4>👉 Flatpay</h4><p>TPE à commission fixe 1,29%, terminal offert dès 2 000 €/mois.</p><a href="/go/flatpay" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
<div class="sidebar-card"><h4>🔗 À lire aussi</h4><ul class="sidebar-toc">
<li><a href="/avis/flatpay.html">Avis Flatpay →</a></li><li><a href="/guides/flatpay-tarifs.html">Tarifs Flatpay →</a></li>
<li><a href="/comparatifs/flatpay-vs-sumup.html">Flatpay vs SumUp →</a></li><li><a href="/comparatifs/terminaux-paiement.html">Comparatif TPE →</a></li></ul></div>
</aside></div></div>{footer()}''')
    print("article:",slug)

article("flatpay-engagement-resiliation","Flatpay : engagement et résiliation (36 mois) — ce qu'il faut savoir | Selectum",
 "Engagement Flatpay : durée de 36 mois, conditions de résiliation et points de vigilance avant de signer. Notre analyse complète 2026.",
 "Flatpay : engagement et résiliation",
 '''<div class="intro-box"><p>C'est LE point à connaître avant de souscrire Flatpay : l'engagement de 36 mois. On vous explique tout, sans langue de bois.</p></div>
<h2 id="duree">Une durée d'engagement de 36 mois</h2>
<p>Contrairement à SumUp ou Zettle (sans engagement), Flatpay vous engage sur <strong>3 ans (36 mois)</strong>. En contrepartie : pas d'abonnement, terminal offert dès 2 000 €/mois d'encaissement, et une commission fixe de 1,29%.</p>
<h2 id="pour-qui">Pour qui c'est adapté (ou pas)</h2>
<div class="pros-cons"><div class="pros"><h4>✅ Adapté si</h4><ul><li>Commerce établi avec volume régulier</li><li>Vous encaissez &gt; 2 000 €/mois</li><li>Vous voulez une commission basse et stable</li></ul></div>
<div class="cons"><h4>❌ À éviter si</h4><ul><li>Activité saisonnière ou qui démarre</li><li>Volume faible / irrégulier</li><li>Vous voulez pouvoir arrêter à tout moment</li></ul></div></div>
<div class="highlight-box"><p>💡 Si l'engagement vous freine, comparez les alternatives <a href="/comparatifs/tpe-sans-engagement.html">sans engagement</a> (SumUp, Zettle, myPOS).</p></div>''',
 [("Quelle est la durée d'engagement Flatpay ?","Flatpay impose un engagement de 36 mois (3 ans). C'est la contrepartie de l'absence d'abonnement et du terminal offert."),
  ("Peut-on résilier Flatpay avant la fin ?","La résiliation avant terme est encadrée par le contrat. Vérifiez les conditions exactes avant de signer ; un commerce saisonnier devrait privilégier une solution sans engagement."),
  ("Flatpay a-t-il un abonnement ?","Non, aucun abonnement. Vous payez une commission de 1,29% par transaction, et le terminal est offert au-delà de 2 000 €/mois.")])

article("flatpay-vs-banque","Flatpay ou le TPE de votre banque ? Comparatif 2026 | Selectum",
 "Flatpay vs TPE bancaire : commission, abonnement, engagement, transparence. Faut-il quitter le terminal de sa banque pour Flatpay ?",
 "Flatpay ou le TPE de votre banque ?",
 '''<div class="intro-box"><p>Beaucoup de commerçants paient cher le TPE de leur banque. Flatpay est-il plus avantageux ? Comparons.</p></div>
<h2 id="modele">Deux modèles opposés</h2>
<div class="comparison-table-wrap"><table class="comparison-table"><thead><tr><th>Critère</th><th>Flatpay</th><th>TPE bancaire</th></tr></thead><tbody>
<tr><td>Commission</td><td>1,29% fixe (toutes cartes)</td><td>Variable + frais par type de carte</td></tr>
<tr><td>Abonnement / location</td><td>0 € (terminal offert*)</td><td>15 à 30 €/mois</td></tr>
<tr><td>Transparence</td><td>Très élevée</td><td>Souvent opaque</td></tr>
<tr><td>Engagement</td><td>36 mois</td><td>12 à 48 mois</td></tr></tbody></table></div>
<p>*Terminal offert au-delà de 2 000 €/mois d'encaissement, sinon 50 €/mois.</p>
<div class="highlight-box"><p>💡 Pour un commerce à volume régulier, Flatpay évite les frais fixes et les surcoûts par type de carte. Voir aussi <a href="/guides/flatpay-vs-achat-tpe.html">Flatpay vs acheter son TPE</a>.</p></div>''',
 [("Flatpay est-il moins cher que le TPE de ma banque ?","Souvent oui, grâce à l'absence d'abonnement et à la commission fixe toutes cartes. Cela dépend de votre volume et des frais négociés avec votre banque."),
  ("Faut-il fermer son compte bancaire pour Flatpay ?","Non. Flatpay est un service d'encaissement indépendant : vous gardez votre banque, les fonds sont versés sur votre compte.")])

article("flatpay-delai-virement","Flatpay : délai de versement des fonds (quand suis-je payé ?) | Selectum",
 "Délai de virement Flatpay : sous combien de temps recevez-vous vos encaissements ? Fonctionnement des versements et bonnes pratiques 2026.",
 "Flatpay : délai de versement des fonds",
 '''<div class="intro-box"><p>Une question essentielle pour la trésorerie : quand l'argent encaissé arrive-t-il sur votre compte ?</p></div>
<h2 id="delai">Le délai de versement</h2>
<p>Avec Flatpay, les fonds encaissés sont généralement versés sur votre compte bancaire sous <strong>1 à 2 jours ouvrés</strong>, selon votre banque. Les week-ends et jours fériés peuvent allonger ce délai.</p>
<h2 id="conseils">Bonnes pratiques trésorerie</h2>
<ul><li>Vérifiez l'IBAN renseigné pour éviter tout retard</li><li>Anticipez les week-ends pour vos besoins de liquidités</li><li>Suivez vos versements dans l'espace Flatpay</li></ul>''',
 [("Sous combien de temps Flatpay verse l'argent ?","En général sous 1 à 2 jours ouvrés sur votre compte bancaire, selon votre banque."),
  ("Les versements sont-ils instantanés ?","Pas en instantané : comptez 1 à 2 jours ouvrés. Pour des fonds immédiats, des solutions comme myPOS proposent un compte intégré.")])

print("articles flatpay+ générés")
