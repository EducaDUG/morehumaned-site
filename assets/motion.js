// MoreHuman Ed: motion layer. Content stays visible without this file.
(function () {
  var doc = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Split the hero headline into words that rise in
  var h1 = document.querySelector('.hero h1');
  if (h1 && !reduce) {
    var i = 0;
    (function walk(node) {
      [].slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (t) {
            if (!t) return;
            if (/^\s+$/.test(t)) { frag.appendChild(document.createTextNode(' ')); return; }
            var w = document.createElement('span'); w.className = 'word'; w.style.setProperty('--w', i++);
            var s = document.createElement('span'); s.textContent = t; w.appendChild(s); frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'EM') { walk(n); }
        else if (n.tagName === 'EM') { walk(n); }
      });
    })(h1);
  }
  // Start the entrance once the page has painted
  window.requestAnimationFrame(function () { window.requestAnimationFrame(function () { doc.classList.add('go'); }); });

  // Stagger tile animation
  [].forEach.call(document.querySelectorAll('.tiles.varied i'), function (el, n) { el.style.setProperty('--i', n); });

  // Gentle parallax on the compass (pointer) and scroll
  var vis = document.querySelector('.hero__visual');
  if (vis && !reduce && window.matchMedia('(pointer: fine)').matches) {
    var hero = document.querySelector('.hero');
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      vis.style.transform = 'translate(' + (x * 18).toFixed(1) + 'px,' + (y * 14).toFixed(1) + 'px) rotate(' + (x * 4).toFixed(2) + 'deg)';
    });
    hero.addEventListener('pointerleave', function () { vis.style.transform = ''; });
  }

  // Discovery Lab hand-off: a soft gradient into its colours, then navigate
  var DL = /^https:\/\/morehumaned\.com\/discovery-lab/i;
  var veil;
  function makeVeil() {
    veil = document.createElement('div'); veil.className = 'dl-veil'; veil.setAttribute('aria-hidden', 'true');
    var img = document.createElement('img'); img.alt = ''; img.src = (document.querySelector('link[rel=icon]') || {}).href || '';
    veil.appendChild(img); document.body.appendChild(veil);
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
    if (!DL.test(a.href) || a.target === '_blank') return;
    if (reduce) return;
    e.preventDefault();
    if (!veil) makeVeil();
    window.requestAnimationFrame(function () { veil.classList.add('on'); });
    setTimeout(function () { window.location.href = a.href; }, 850);
  });
  window.addEventListener('pageshow', function (e) { if (e.persisted && veil) veil.classList.remove('on'); });
})();

// Gentle parallax inside the photo breaks
(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var imgs = [].slice.call(document.querySelectorAll('[data-parallax]'));
  if (!imgs.length) return;
  var t = false;
  function run() {
    t = false;
    var vh = window.innerHeight;
    imgs.forEach(function (im) {
      var r = im.parentNode.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      var p = (r.top + r.height / 2 - vh / 2) / vh;
      im.style.transform = 'translateY(' + (p * -8).toFixed(2) + '%)';
    });
  }
  window.addEventListener('scroll', function () { if (!t) { t = true; requestAnimationFrame(run); } }, { passive: true });
  run();
})();

// Click-to-load video: nothing is requested from YouTube until the visitor presses play
document.addEventListener('click', function (e) {
  var a = e.target.closest && e.target.closest('a.yt[data-yt]');
  if (!a || e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
  e.preventDefault();
  var f = document.createElement('iframe');
  f.src = 'https://www.youtube-nocookie.com/embed/' + a.getAttribute('data-yt') + '?autoplay=1&rel=0&modestbranding=1';
  f.title = a.getAttribute('aria-label'); f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; f.allowFullscreen = true;
  a.replaceWith((function () { var d = document.createElement('div'); d.className = 'yt'; d.appendChild(f); return d; })());
});
