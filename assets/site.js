/* Selectum — comportements partagés (menu mobile, FAQ, codes promo) */
(function () {
  document.documentElement.classList.add('js');

  /* ---- Menu mobile (hamburger) ---- */
  function initMenu() {
    var header = document.querySelector('.header-inner');
    var nav = document.querySelector('.nav');
    if (!header || !nav) return;

    var toggle = document.createElement('button');
    toggle.className = 'menu-toggle';
    toggle.setAttribute('aria-label', 'Ouvrir le menu');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.innerHTML = '<span></span><span></span><span></span>';

    var cta = header.querySelector('.header-cta');
    if (cta) header.insertBefore(toggle, cta);
    else header.appendChild(toggle);

    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
    });

    /* Sous-menus déroulants : ouverture au tap sur mobile */
    nav.querySelectorAll('.nav-item > .nav-link').forEach(function (link) {
      link.addEventListener('click', function (e) {
        if (window.matchMedia('(max-width: 768px)').matches) {
          e.preventDefault();
          link.parentElement.classList.toggle('open');
        }
      });
    });

    /* Fermer le menu après clic sur un lien */
    nav.addEventListener('click', function (e) {
      var a = e.target.closest('a');
      if (a) { nav.classList.remove('open'); toggle.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); }
    });

    /* Fermer avec Échap */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open'); toggle.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---- Accordéon FAQ ---- */
  function initFaq() {
    document.querySelectorAll('.faq-item').forEach(function (item) {
      var q = item.querySelector('.faq-question');
      if (!q) return;
      var sign = q.querySelector('span');
      q.setAttribute('role', 'button');
      q.setAttribute('tabindex', '0');
      function toggle() {
        var open = item.classList.toggle('open');
        if (sign) sign.textContent = open ? '−' : '+';
      }
      q.addEventListener('click', toggle);
      q.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
      });
    });
  }

  /* ---- Révélation des codes promo ---- */
  function initPromo() {
    document.addEventListener('click', function (e) {
      var btn = e.target.closest('.promo-btn');
      if (!btn) return;
      var box = btn.closest('.promo-reveal');
      if (box && !box.classList.contains('revealed')) {
        e.preventDefault();
        box.classList.add('revealed');
        btn.textContent = "Voir l'offre →";
      }
    });
  }

  function init() { initMenu(); initFaq(); initPromo(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
