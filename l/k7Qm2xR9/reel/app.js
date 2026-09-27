/* =============================================
   Private reel — gate + interactions
   ============================================= */

// SHA-256 hash of the access code. To change the code, generate a new hash:
//   printf '%s' "YOUR-NEW-CODE" | shasum -a 256
// then paste the first value below. Default code: reel2026
const ACCESS_HASH = "34b42cfd3c3b989644cdc9a871c866e7983359335dd438608b3dfd59ee764979";
const SESSION_KEY = "ys_reel_ok";

const gate = document.getElementById("gate");
const site = document.getElementById("site");
const form = document.getElementById("gate-form");
const input = document.getElementById("gate-input");
const errorEl = document.getElementById("gate-error");

let siteInit = false;

async function sha256(text) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, "0")).join("");
}

function unlock() {
  gate.setAttribute("aria-hidden", "true");
  gate.style.display = "none";
  site.hidden = false;
  initSite();
}

if (sessionStorage.getItem(SESSION_KEY) === "1") {
  unlock();
} else {
  setTimeout(() => input && input.focus(), 100);
}

form && form.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorEl.hidden = true;
  const value = (input.value || "").trim();
  let ok = false;
  try {
    ok = (await sha256(value)) === ACCESS_HASH;
  } catch (_) {
    // Fallback if Web Crypto unavailable (non-secure context): compare plain.
    ok = value === "reel2026";
  }
  if (ok) {
    sessionStorage.setItem(SESSION_KEY, "1");
    unlock();
  } else {
    errorEl.hidden = false;
    input.value = "";
    input.focus();
  }
});

// ---- site interactions (run after unlock) ----
function initSite() {
  if (siteInit) return;
  siteInit = true;

  const yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  const nav = document.getElementById("nav");
  const onScroll = () => nav && nav.classList.toggle("scrolled", window.scrollY > 24);
  window.addEventListener("scroll", onScroll);
  onScroll();

  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener("click", e => {
      const target = document.querySelector(a.getAttribute("href"));
      if (target) {
        e.preventDefault();
        const offset = nav ? nav.offsetHeight : 0;
        window.scrollTo({ top: target.offsetTop - offset, behavior: "smooth" });
      }
    });
  });

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const els = document.querySelectorAll(".section-head, .work-card, .svc, .about-text, .about-quote, .listen-grid, .contact-form");
  if (reduce || !("IntersectionObserver" in window)) {
    els.forEach(el => el.classList.add("reveal", "in"));
  } else {
    els.forEach(el => el.classList.add("reveal"));
    const io = new IntersectionObserver((entries) => {
      entries.forEach(en => {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.1 });
    els.forEach(el => io.observe(el));
  }

  // pause other videos when one plays
  const videos = document.querySelectorAll(".work-card video");
  videos.forEach(v => v.addEventListener("play", () => {
    videos.forEach(o => { if (o !== v) o.pause(); });
  }));
}

window.toggleMenu = function () { document.getElementById("nav-links").classList.toggle("open"); };
window.closeMenu = function () { document.getElementById("nav-links").classList.remove("open"); };
