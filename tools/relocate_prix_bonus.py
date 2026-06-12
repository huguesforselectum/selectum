#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sur tous les comparatifs : déplace l'argument prix dans une pastille du corps de la carte
et ajoute un badge 'Offre de bienvenue' (lien code-promo) à l'emplacement de l'ancien prix (près du CTA).
Les prix sont récupérés depuis la version git d'avant leur suppression."""
import os, re, glob, html, subprocess

PARENT = "79eead9~1"  # commit avec les prix

def old_prices(fname):
    """slug -> texte prix, depuis l'ancienne version du fichier (si elle existait)."""
    try:
        s = subprocess.run(["git","show",f"{PARENT}:{fname}"], capture_output=True, text=True).stdout
    except Exception:
        return {}
    if not s:
        return {}
    pm = {}
    # top-pick : ...tp-logo"><img src="/assets/logos/SLUG.png"... puis tp-price">VALUE</div>
    for m in re.finditer(r'/assets/logos/([a-z0-9-]+)\.png"[^>]*>\s*</div>\s*<div class="tp-main">.*?<div class="tp-price">([^<]+)</div>', s, re.S):
        pm.setdefault(m.group(1), m.group(2).strip())
    # secondaire : offer-logo brand ... SLUG.png ... offer-price-cap">VALUE<span>SUB</span>
    for m in re.finditer(r'offer-logo brand"><img[^>]*/assets/logos/([a-z0-9-]+)\.png"[^>]*>.*?<div class="offer-price-cap">([^<]*)(?:<span>([^<]*)</span>)?</div>', s, re.S):
        slug, val, sub = m.group(1), (m.group(2) or "").strip(), (m.group(3) or "").strip()
        txt = (val + (" " + sub if sub and val else sub)).strip()
        if slug not in pm and txt:
            pm[slug] = txt
    return pm

def first_slug(chunk):
    m = re.search(r'/assets/logos/([a-z0-9-]+)\.png', chunk)
    return m.group(1) if m else None

def bonus_badge(slug, name):
    if os.path.exists(f"code-promo/{slug}.html"):
        return f'<a class="card-bonus" href="/code-promo/{slug}.html" title="Offre de bienvenue {html.escape(name)}">🎁 Offre de bienvenue</a>'
    return ""

def transform(fname, pm):
    t = open(fname, encoding="utf-8").read()
    if 'class="offers-list"' not in t and 'offer-card' not in t:
        return False
    if 'card-bonus' in t or 'price-pill' in t or 'price-tag' in t:
        return False  # déjà traité
    parts = re.split(r'(<div class="offer-card)', t)
    # parts: [prefix, '<div class="offer-card', chunkA, '<div class="offer-card', chunkB, ...]
    out = [parts[0]]
    i = 1
    changed = False
    while i < len(parts):
        marker = parts[i]            # '<div class="offer-card'
        chunk = parts[i+1] if i+1 < len(parts) else ""
        is_top = chunk.startswith(' top-pick"')
        slug = first_slug(chunk)
        name_m = re.search(r'(?:tp-name|offer-name)">([^<]+)<', chunk)
        name = name_m.group(1).strip() if name_m else (slug or "")
        price = pm.get(slug, "") if slug else ""
        badge = bonus_badge(slug, name) if slug else ""
        if is_top:
            # pastille prix après le tagline
            if price:
                pill = f'<div class="tp-pills"><span class="price-pill">💶 {html.escape(price)}</span></div>'
                new, nrep = re.subn(r'(<div class="tp-tagline">.*?</div>)', lambda mm: mm.group(1)+pill, chunk, count=1, flags=re.S)
                if nrep: chunk = new; changed = True
            # badge bonus après le bouton CTA (à la place de l'ancien prix)
            if badge:
                new, nrep = re.subn(r'(<a class="btn-green tp-cta".*?</a>)', lambda mm: mm.group(1)+badge, chunk, count=1, flags=re.S)
                if nrep: chunk = new; changed = True
        else:
            # pastille prix dans offer-tags
            if price:
                tag = f'<span class="offer-tag price-tag">💶 {html.escape(price)}</span>'
                if '<div class="offer-tags">' in chunk:
                    new, nrep = re.subn(r'(<div class="offer-tags">)(.*?)(</div>)', lambda mm: mm.group(1)+mm.group(2)+tag+mm.group(3), chunk, count=1, flags=re.S)
                else:
                    new, nrep = re.subn(r'(<div class="offer-desc">.*?</div>)', lambda mm: mm.group(1)+f'<div class="offer-tags">{tag}</div>', chunk, count=1, flags=re.S)
                if nrep: chunk = new; changed = True
            # badge bonus après le bouton (à la place de l'ancien price-cap)
            if badge:
                new, nrep = re.subn(r'(<div class="offer-buy">.*?</a>)', lambda mm: mm.group(1)+badge, chunk, count=1, flags=re.S)
                if nrep: chunk = new; changed = True
        out.append(marker); out.append(chunk)
        i += 2
    if changed:
        open(fname, "w", encoding="utf-8").write("".join(out))
    return changed

def main():
    n = 0; stats = {"price":0,"badge":0}
    for f in sorted(glob.glob("comparatifs/*.html")):
        pm = old_prices(f)
        if transform(f, pm):
            n += 1
    print("comparatifs transformés:", n)

if __name__ == "__main__":
    main()
