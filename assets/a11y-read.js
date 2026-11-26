// Adds a speaker button beside the main text blocks. The buttons stay hidden unless read-aloud is switched on in the
// reading settings panel. All speech goes through Discovery Lab's speak(); nothing here calls speechSynthesis directly.
import { speakerButton } from "/discovery-lab/engine/accessibility.js";

const SELECTORS = [
  ".hero__lede", ".welcome p:not(.welcome__note)", ".section-head > p", ".problem__copy p", ".purpose p",
  ".prose p", ".dl-feature p", ".final p", ".card p", ".ba__caps p"
];
const seen = new Set();
function attach() {
  document.querySelectorAll(SELECTORS.join(",")).forEach(p => {
    if (seen.has(p) || p.closest(".a11y-panel") || !p.textContent.trim()) return;
    seen.add(p);
    const text = p.innerText.trim();
    p.append(speakerButton(() => text));
  });
}
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", attach, { once: true });
else attach();
