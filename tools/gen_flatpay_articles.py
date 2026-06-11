#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html, json
exec(open("tools/gen_flatpay.py").read().split("n=0")[0])  # réutilise headhtml/footer/faq_ld

def article(slug,title,desc,h1,body_html,qa):
    url=f"https://selectum.fr/guides/{slug}.html"
    ld_art=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"author":{"@type":"Organization","name":"Selectum"},"publisher":{"@type":"Organization","name":"Selectum","logo":{"@type":"ImageObject","url":"https://selectum.fr/assets/selectum-logo.png"}},"datePublished":"2026-06-11","dateModified":"2026-06-11","mainEntityOfPage":url},ensure_ascii=False)
    qatxt=[(html.escape(q),html.escape(a)) for q,a in qa]
    extra=f'\n<script type="application/ld+json">{ld_art}</script>'+faq_ld(qatxt)
    faq='<div class="faq"><h2>❓ Questions fréquentes</h2>'+''.join(f'<div class="faq-item"><div class="faq-question">{q} <span>+</span></div><div class="faq-answer">{a}</div></div>' for q,a in qatxt)+'</div>'
    page=f'''{headhtml(title,desc,url,extra)}
<div class="brand-hero"><div class="container-article">
<div class="brand-hero-logo"><img src="/assets/logos/flatpay.png" alt="Flatpay"></div>
<div class="brand-hero-text">
<div class="article-breadcrumb" style="color:rgba(255,255,255,.6);margin-bottom:10px;"><a href="/index.html" style="color:rgba(255,255,255,.8)">Accueil</a> / Guides / Flatpay</div>
<h1>{html.escape(h1)}</h1><p class="updated">🗓️ Mis à jour le 11 juin 2026</p>
</div></div></div>
<div class="container-article"><div class="article-layout" style="grid-template-columns: 1fr 300px;"><main class="article-body">
<div class="affiliate-notice">ℹ️ <strong>Transparence :</strong> Selectum peut percevoir une commission via les liens partenaires, sans surcoût pour vous.</div>
{body_html}
{faq}
</main>
<aside class="sidebar">
<div class="sidebar-cta"><h4>👉 Flatpay</h4><p>TPE à commission fixe 1,29%, terminal offert dès 2 000 €/mois.</p><a href="/go/flatpay" class="btn-green" style="width:100%;justify-content:center;" target="_blank" rel="sponsored nofollow noopener">Voir l'offre →</a></div>
<div class="sidebar-card"><h4>🔗 À lire aussi</h4><ul class="sidebar-toc">
<li><a href="/avis/flatpay.html">Avis Flatpay →</a></li>
<li><a href="/code-promo/flatpay.html">Code promo Flatpay →</a></li>
<li><a href="/comparatifs/flatpay-vs-sumup.html">Flatpay vs SumUp →</a></li>
<li><a href="/comparatifs/terminaux-paiement.html">Comparatif TPE →</a></li>
</ul></div>
</aside>
</div></div>{footer()}'''
    open(f"guides/{slug}.html","w").write(page); print("article:",slug)

# 1) Tarifs
article("flatpay-tarifs","Flatpay : tarifs et commission 2026 (guide complet) | Selectum",
 "Tarifs Flatpay 2026 : commission fixe de 1,29%, frais de la caisse, location du terminal, conditions. Tout savoir sur le prix de Flatpay.",
 "Flatpay : tarifs et commission en 2026",
 '''<div class="intro-box"><p>Flatpay se distingue par une tarification <strong>simple et fixe</strong>, sans pourcentages variables selon le type de carte. Voici le détail de ses tarifs en 2026.</p></div>
<h2 id="commission">La commission Flatpay</h2>
<div class="comparison-table-wrap"><table class="comparison-table"><thead><tr><th>Offre</th><th>Commission</th><th>Détail</th></tr></thead><tbody>
<tr><td><strong>Terminal de paiement (TPE)</strong></td><td>1,29%</td><td>Taux fixe, toutes cartes</td></tr>
<tr><td><strong>Caisse tout-en-un</strong></td><td>1,69%</td><td>TPE + logiciel de caisse</td></tr>
<tr><td>Abonnement</td><td>0 €</td><td>Aucun abonnement fixe</td></tr>
<tr><td>Location du terminal</td><td>Offert*</td><td>*si &gt; 2 000 €/mois encaissés, sinon 50 € HT/mois</td></tr>
</tbody></table></div>
<h2 id="atout">Le vrai atout : un taux identique pour toutes les cartes</h2>
<p>Contrairement à beaucoup de concurrents qui majorent les cartes American Express ou les cartes hors zone euro, Flatpay applique <strong>le même taux de 1,29% quelle que soit la carte</strong>. Pour un commerce touristique ou avec une clientèle internationale, c'est un avantage concret.</p>
<h2 id="rentable">Est-ce rentable ?</h2>
<p>Le taux de 1,29% se situe dans la fourchette haute du marché en valeur brute, mais il reste <strong>plus bas que SumUp (1,75%) ou Square (1,65%)</strong> et la prévisibilité (pas de surprise selon les cartes) facilite la gestion. Le terminal offert dès 2 000 €/mois d'encaissement renforce l'intérêt pour les commerces à volume régulier.</p>
<div class="highlight-box"><p>💡 <strong>À retenir :</strong> Flatpay est le plus rentable si vous encaissez régulièrement plus de 2 000 €/mois. En dessous, la location de 50 €/mois s'applique. Voir aussi notre <a href="/guides/flatpay-gratuit.html">analyse "Flatpay est-il vraiment gratuit ?"</a></p></div>''',
 [("Quelle est la commission Flatpay ?","Flatpay applique 1,29% par transaction sur le TPE, et 1,69% sur la caisse tout-en-un. Le taux est identique pour toutes les cartes."),
  ("Y a-t-il un abonnement Flatpay ?","Non, aucun abonnement fixe. Le terminal est offert si vous encaissez plus de 2 000 €/mois, sinon une location de 50 € HT/mois s'applique."),
  ("Flatpay majore-t-il les cartes Amex ?","Non. C'est l'un de ses atouts : le taux de 1,29% s'applique à toutes les cartes, y compris American Express et les cartes hors zone euro.")])

# 2) Avantages / inconvénients
article("flatpay-avantages","Flatpay : avantages et inconvénients en 2026 | Selectum",
 "Avantages et inconvénients de Flatpay en 2026 : commission fixe, terminal offert, accompagnement... mais engagement 36 mois. Notre analyse complète.",
 "Flatpay : avantages et inconvénients",
 '''<div class="intro-box"><p>Flatpay séduit par sa simplicité tarifaire et son accompagnement, mais impose un engagement long. Voici le bilan objectif.</p></div>
<div class="pros-cons">
<div class="pros"><h4>✅ Avantages</h4><ul>
<li>Commission fixe et lisible (1,29%)</li>
<li>Même taux pour toutes les cartes (même Amex)</li>
<li>Aucun abonnement fixe</li>
<li>Terminal offert dès 2 000 €/mois encaissés</li>
<li>Accompagnement physique à l'installation</li>
<li>Support client réactif et humain</li>
</ul></div>
<div class="cons"><h4>❌ Inconvénients</h4><ul>
<li>Engagement de 36 mois</li>
<li>Location de 50 €/mois sous 2 000 €/mois d'encaissement</li>
<li>Taux brut élevé en valeur absolue</li>
<li>Peu adapté aux commerces saisonniers / faibles volumes</li>
</ul></div></div>
<h2 id="pour-qui">Pour qui Flatpay est-il fait ?</h2>
<p>Flatpay est idéal pour un <strong>commerce établi avec un volume régulier</strong> (restaurant, salon, boutique) qui veut une tarification prévisible et un accompagnement humain. Il l'est moins pour un commerce qui démarre sans visibilité ou très saisonnier — dans ce cas, une solution <a href="/comparatifs/flatpay-vs-sumup.html">sans engagement type SumUp</a> sera plus souple.</p>''',
 [("Quel est le principal inconvénient de Flatpay ?","L'engagement de 36 mois, qui le rend peu adapté aux commerces saisonniers ou qui démarrent sans visibilité sur leur volume."),
  ("Flatpay convient-il à un petit commerce ?","Oui s'il encaisse plus de 2 000 €/mois régulièrement. En dessous, la location mensuelle de 50 € s'applique et d'autres solutions sans engagement peuvent être plus avantageuses."),
  ("Le support Flatpay est-il bon ?","Oui, c'est un point fort souvent salué : accompagnement physique à l'installation et support client humain et réactif.")])

# 3) Gratuit ?
article("flatpay-gratuit","Flatpay est-il vraiment gratuit ? La vérité en 2026 | Selectum",
 "Flatpay gratuit ? On décrypte : pas d'abonnement, terminal offert dès 2 000 €/mois, mais commission 1,29% et engagement 36 mois. La réalité du \"gratuit\".",
 "Flatpay est-il vraiment gratuit ?",
 '''<div class="intro-box"><p>Flatpay communique sur un terminal « gratuit ». Démêlons le vrai du marketing.</p></div>
<h2 id="ce-qui-est-gratuit">Ce qui est réellement gratuit</h2>
<ul><li><strong>Aucun abonnement</strong> fixe mensuel.</li><li><strong>Le terminal est offert</strong> si vous encaissez plus de 2 000 €/mois.</li><li>Installation et accompagnement inclus.</li></ul>
<h2 id="ce-qui-est-payant">Ce qui reste payant</h2>
<ul><li>La <strong>commission de 1,29%</strong> sur chaque encaissement (1,69% pour la caisse).</li><li>Une <strong>location de 50 € HT/mois</strong> si vous encaissez moins de 2 000 €/mois.</li><li>Un <strong>engagement de 36 mois</strong>.</li></ul>
<div class="highlight-box"><p>💡 <strong>Verdict :</strong> Flatpay n'est pas « gratuit » au sens strict — vous payez une commission sur chaque vente. Mais l'absence d'abonnement et le terminal offert le rendent <strong>réellement sans frais fixes</strong> si votre volume dépasse 2 000 €/mois. C'est donc « gratuit » côté matériel, pas côté transactions.</p></div>''',
 [("Le terminal Flatpay est-il gratuit ?","Oui, le terminal est offert si vous encaissez plus de 2 000 €/mois. En dessous, une location de 50 € HT/mois s'applique."),
  ("Y a-t-il des frais cachés chez Flatpay ?","Non, la tarification est transparente : 1,29% par transaction, pas d'abonnement. Le seul coût additionnel possible est la location du terminal sous le seuil de 2 000 €/mois."),
  ("Flatpay prélève-t-il une commission ?","Oui, 1,29% par transaction sur le TPE (1,69% sur la caisse). C'est son modèle économique, à la place d'un abonnement.")])

# 4) vs achat TPE
article("flatpay-vs-achat-tpe","Flatpay ou acheter son TPE ? Comparatif 2026 | Selectum",
 "Faut-il choisir Flatpay (commission 1,29%, sans abonnement) ou acheter son propre terminal de paiement ? Comparatif des coûts réels en 2026.",
 "Flatpay ou acheter son propre TPE ?",
 '''<div class="intro-box"><p>Deux modèles s'opposent : la commission tout compris de Flatpay, ou l'achat d'un TPE bancaire classique avec abonnement. Lequel coûte le moins cher ?</p></div>
<h2 id="modeles">Deux modèles de coûts</h2>
<div class="comparison-table-wrap"><table class="comparison-table"><thead><tr><th>Critère</th><th>Flatpay</th><th>TPE bancaire (achat/location)</th></tr></thead><tbody>
<tr><td>Commission</td><td>1,29% fixe</td><td>Souvent plus basse (0,5–0,9%) mais + frais fixes</td></tr>
<tr><td>Abonnement / location</td><td>0 € (terminal offert*)</td><td>15 à 30 €/mois</td></tr>
<tr><td>Frais par carte</td><td>Inclus, taux unique</td><td>Variables (Amex, hors UE majorés)</td></tr>
<tr><td>Engagement</td><td>36 mois</td><td>12 à 48 mois</td></tr>
<tr><td>Transparence</td><td>Très élevée</td><td>Souvent complexe</td></tr>
</tbody></table></div>
<h2 id="verdict">Notre verdict</h2>
<p>Pour un <strong>volume faible à moyen</strong>, le tout-compris de Flatpay évite les frais fixes et les mauvaises surprises sur les types de cartes. Pour un <strong>très gros volume</strong>, un TPE bancaire avec une commission négociée plus basse peut redevenir avantageux malgré l'abonnement. L'avantage de Flatpay reste la <strong>simplicité et la prévisibilité</strong>.</p>
<div class="highlight-box"><p>💡 Comparez aussi Flatpay aux fintechs sans engagement : <a href="/comparatifs/flatpay-vs-sumup.html">vs SumUp</a>, <a href="/comparatifs/flatpay-vs-zettle.html">vs Zettle</a>, <a href="/comparatifs/flatpay-vs-mypos.html">vs myPOS</a>.</p></div>''',
 [("Flatpay est-il moins cher qu'un TPE bancaire ?","Cela dépend du volume. Flatpay évite les frais fixes et les surcoûts par type de carte, ce qui est avantageux pour un volume faible à moyen. Un très gros volume peut justifier un TPE bancaire à commission négociée."),
  ("Faut-il acheter un terminal avec Flatpay ?","Non. Le terminal est fourni (offert au-delà de 2 000 €/mois d'encaissement, sinon 50 €/mois de location)."),
  ("Quel modèle est le plus transparent ?","Flatpay, avec sa commission unique de 1,29% toutes cartes et l'absence d'abonnement, est nettement plus lisible qu'un contrat de TPE bancaire classique.")])

print("articles Flatpay générés")
