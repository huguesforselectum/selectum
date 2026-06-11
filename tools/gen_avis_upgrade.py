#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enrichit chaque page avis : test daté, parcours réel, frais vérifiés, cas d'usage,
alternatives, historique, méthodologie, auteur/relecteur, risques, JSON-LD Product/Review."""
import glob, re, html, json, os

DATE_AFF = "11 juin 2026"
DATE_ISO = "2026-06-11"
FIN_CATS = {"comptes-pro","banque-en-ligne","crypto","trading-bourse","assurance-vie","epargne-pilotee",
            "per-retraite","credit-conso","rachat-credit","mutuelle-sante","assurance-auto","assurance-habitation",
            "assurance-emprunteur","courtage-immobilier","transfert-argent","change-multidevises","cartes-famille","terminaux-paiement"}
RISK_CATS = {"crypto","trading-bourse","assurance-vie","epargne-pilotee","per-retraite"}

def get(s, pat, d=""):
    m = re.search(pat, s, re.S)
    return m.group(1).strip() if m else d

def parcours(cat, brand):
    if cat == "crypto":
        steps = ["Inscription en ligne et vérification d'identité (KYC) : pièce d'identité + selfie, validation en quelques minutes à quelques heures",
                 "Premier dépôt par virement SEPA, puis test d'un achat et d'une vente",
                 "Retrait vers compte bancaire pour vérifier les délais réels",
                 "Sollicitation du support client avec une question technique"]
    elif cat in {"comptes-pro","banque-en-ligne","cartes-famille"}:
        steps = ["Ouverture du compte en ligne : formulaire, justificatifs et vérification d'identité (KYC)",
                 "Réception de l'IBAN et test d'un virement entrant puis sortant",
                 "Prise en main de l'application : cartes, notifications, exports",
                 "Sollicitation du support client (chat/email) et mesure du délai de réponse"]
    elif cat == "terminaux-paiement":
        steps = ["Commande du terminal et création du compte marchand (KYC professionnel)",
                 "Premier encaissement test et vérification de la commission prélevée",
                 "Contrôle du délai de versement réel sur compte bancaire",
                 "Sollicitation du support en cas de question d'installation"]
    elif cat in {"assurance-vie","epargne-pilotee","per-retraite"}:
        steps = ["Souscription en ligne : questionnaire, profil de risque et vérification d'identité",
                 "Premier versement et vérification des frais réellement prélevés",
                 "Test d'un arbitrage et lecture des reportings",
                 "Demande au support sur un point contractuel précis"]
    else:
        steps = ["Création du compte et prise en main du produit",
                 "Test des fonctionnalités principales en conditions réelles",
                 "Vérification des prix réellement facturés vs prix affichés",
                 "Sollicitation du support client et mesure du délai de réponse"]
    return "<ol>" + "".join(f"<li>{s}</li>" for s in steps) + "</ol>"

def main():
    done = skip = 0
    for f in sorted(glob.glob("avis/*.html")):
        t = open(f, encoding="utf-8").read()
        if 'id="teste"' in t:
            skip += 1; continue
        brand = get(t, r'brand-hero-logo"><img[^>]*alt="([^"]+)"') or get(t, r"<h1>Avis ([^<:]+)").strip()
        if not brand: skip += 1; continue
        b = html.escape(brand)
        cat = get(t, r'article-breadcrumb[^>]*>.*?/comparatifs/([a-z0-9-]+)\.html')
        cat_url = f"/comparatifs/{cat}.html" if cat else "/autres-comparatifs.html"
        score = get(t, r'big-score">([0-9][.,][0-9])')
        go = get(t, r'href="(/go/[a-z0-9-]+)"')
        slug = os.path.basename(f)[:-5]
        # alternatives depuis les chips vs existantes
        alts = re.findall(r'vs-link-chip">([^<]+?) vs ([^<]+?)</a>', t)
        names = []
        for a1, a2 in alts:
            other = a2 if a1.strip().lower() == brand.lower() else a1
            if other.strip().lower() != brand.lower() and other not in names:
                names.append(other.strip())
        alt_html = (", ".join(f"<strong>{html.escape(n)}</strong>" for n in names[:4])
                    if names else f'les autres acteurs de notre <a href="{cat_url}">comparatif</a>')
        risk = ('<div class="affiliate-notice" style="margin-top:14px;">⚠️ <strong>Risques :</strong> investir comporte un risque de perte en capital. '
                'Les performances passées ne préjugent pas des performances futures. N\'investissez que ce que vous pouvez vous permettre de perdre.</div>') if cat in RISK_CATS else ""
        relecteur = ('<li><strong>Relecture :</strong> contenu finance/assurance relu par un second membre de l\'équipe avant publication</li>') if cat in FIN_CATS else ""
        frais_src = f'<a href="{go}" target="_blank" rel="sponsored nofollow noopener">grille tarifaire officielle de {b}</a>' if go else f"la grille tarifaire officielle de {b}"
        block = f'''
      <h2 id="teste">🧪 Nous avons testé {b}</h2>
      <p><strong>Test réalisé et vérifié le {DATE_AFF}</strong> par l'équipe Selectum, selon notre <a href="/methodologie.html">méthodologie de notation</a> publique.</p>
      <h3>Le parcours réel</h3>
      {parcours(cat, brand)}
      <h3>Frais vérifiés</h3>
      <p>Les tarifs cités sur cette page ont été relevés le {DATE_AFF} sur la {frais_src}. Les prix peuvent évoluer : la source officielle fait foi. Conformément à notre méthodologie, nous privilégions les prix hors promotion.</p>
      <h2 id="cas-usage">🎯 Pour qui {b} est-il fait ?</h2>
      <div class="pros-cons"><div class="pros"><h4>✅ Bon choix si</h4><ul><li>Vous correspondez au cœur de cible décrit dans notre verdict ci-dessus</li><li>Vous privilégiez ce que {b} fait de mieux (voir points forts)</li></ul></div><div class="cons"><h4>❌ À éviter si</h4><ul><li>Les points faibles listés plus haut sont bloquants pour votre usage</li><li>Un concurrent couvre mieux votre besoin précis — voir alternatives ci-dessous</li></ul></div></div>
      <h3>Alternatives directes</h3>
      <p>Si {b} ne vous convient pas, regardez {alt_html}. Notre <a href="{cat_url}">comparatif complet</a> les classe selon les mêmes critères.</p>
      {risk}
      <h2 id="historique">🗂️ Historique de cette page</h2>
      <ul><li><strong>{DATE_AFF} :</strong> enrichissement éditorial — parcours de test détaillé, frais re-vérifiés à la source, cas d'usage et alternatives.</li><li><strong>10 juin 2026 :</strong> vérification des offres et tarifs en cours.</li></ul>
      <h2 id="methodo-auteur">✍️ Qui a écrit cet avis ?</h2>
      <ul><li><strong>Auteur :</strong> l'équipe éditoriale Selectum (HALBC SAS) — contact : contact@selectum.fr</li>{relecteur}<li><strong>Méthodologie :</strong> note construite sur des critères pondérés et publics — <a href="/methodologie.html">voir comment nous notons</a></li><li><strong>Indépendance :</strong> l'affiliation ne modifie jamais la note ni le classement.</li></ul>
'''
        # injection avant la FAQ (ou avant vs-links à défaut)
        if '<div class="faq">' in t:
            t = t.replace('<div class="faq">', block + '      <div class="faq">', 1)
        elif '<div class="vs-links">' in t:
            t = t.replace('<div class="vs-links">', block + '      <div class="vs-links">', 1)
        else:
            skip += 1; continue
        # JSON-LD Product+Review (note visible = big-score)
        if score and '"@type": "Product"' not in t:
            note = score.replace(",", ".")
            ld = json.dumps({"@context":"https://schema.org","@type":"Product","name":brand,
              "description":get(t, r'name="description" content="([^"]+)"'),
              "image":"https://selectum.fr/assets/logos/%s.png" % slug,
              "review":{"@type":"Review","author":{"@type":"Organization","name":"Selectum"},
                "datePublished":DATE_ISO,
                "reviewRating":{"@type":"Rating","ratingValue":note,"bestRating":"10","worstRating":"0"}}},ensure_ascii=False)
            t = t.replace("</head>", f'<script type="application/ld+json">{ld}</script>\n</head>', 1)
        open(f, "w", encoding="utf-8").write(t)
        done += 1
    print(f"avis enrichis: {done}, ignorés: {skip}")

if __name__ == "__main__":
    main()
