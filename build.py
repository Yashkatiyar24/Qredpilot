"""Build the QredPilot site into ./site.

- index.html is hand-written at the repo root (redesign) and copied through.
- The 4 demo-flow pages come from the Stitch exports, rebranded with the real
  logo and wired together. Re-run after re-exporting; it fails loudly if an
  expected edit no longer matches.
"""
import re
import shutil
import hashlib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "site"
ASSETS = OUT / "assets"

PAGES = {
    "book_a_demo_step_1_requirements_stack": "book-demo-1.html",
    "book_a_demo_step_2_time_slot_architect_match": "book-demo-2.html",
    "book_a_demo_step_3_interactive_voice_sandbox": "book-demo-3.html",
    "book_a_demo_step_4_executive_confirmation": "book-demo-4.html",
}

# data-path -> real href. Unlisted paths (login, privacy-policy, ...) stay "#".
LINKS = {
    "platform": "index.html",
    "book-a-demo": "book-demo-1.html",
    "contact-sales": "book-demo-1.html",
    "ai-voice-calling": "index.html#ai-voice-calling",
    "ai-voice-ops": "index.html#ai-voice-ops",
    "voice-intelligence": "index.html#voice-intelligence",
    "solutions": "index.html#solutions",
    "lending-solutions": "index.html#solutions",
    "insurance-solutions": "index.html#solutions",
    "fintech-solutions": "index.html#solutions",
    "financial-services": "index.html#solutions",
    "resources": "index.html#integrations",
    "security": "index.html#security",
}

LOGO_IMG = '<img src="assets/logo.png" alt="QredPilot" style="height:30px;width:auto;display:block"/>'

# Per-page exact edits: (old, new). Each must match exactly once or the build fails.
EDITS = {
    "book-demo-1.html": [
        ("submitBtn.classList.add('bg-emerald-600', 'text-white');",
         "submitBtn.classList.add('bg-emerald-600', 'text-white');\n"
         "            setTimeout(() => location.href = 'book-demo-2.html', 500);"),
    ],
    "book-demo-2.html": [
        ("confirmBtn.classList.add('bg-emerald-600');",
         "confirmBtn.classList.add('bg-emerald-600');\n"
         "            setTimeout(() => location.href = 'book-demo-3.html', 500);"),
        ('type="button">\n<span class="material-symbols-outlined text-base">arrow_back</span>',
         'type="button" onclick="location.href=\'book-demo-1.html\'">\n'
         '<span class="material-symbols-outlined text-base">arrow_back</span>'),
    ],
    "book-demo-3.html": [
        ('data-path="resources" href="#">\n            Continue to Confirmation',
         'href="book-demo-4.html">\n            Continue to Confirmation'),
    ],
    "book-demo-4.html": [
        ('<button class="font-body-md text-body-md font-semibold text-primary hover:text-on-primary-fixed-variant transition-colors flex items-center gap-1">\n'
         '<span class="material-symbols-outlined text-sm">edit_calendar</span>',
         '<button onclick="location.href=\'book-demo-2.html\'" class="font-body-md text-body-md font-semibold text-primary hover:text-on-primary-fixed-variant transition-colors flex items-center gap-1">\n'
         '<span class="material-symbols-outlined text-sm">edit_calendar</span>'),
    ],
}


def sub1(pattern, repl, html, flags=0, what=""):
    html, n = re.subn(pattern, repl, html, flags=flags)
    assert n == 1, f"expected 1 match for {what or pattern[:60]!r}, got {n}"
    return html


def rebrand(html):
    """Swap the placeholder icon+text brand for the real logo; drop fake avatar."""
    # header brand anchor -> logo image
    html = sub1(
        r'(<a class="flex items-center gap-3 focus:outline-none" data-path="platform"[^>]*>).*?(</a>)',
        rf"\1{LOGO_IMG}\2", html, flags=re.S, what="header brand")
    # footer brand mark -> logo image
    html = sub1(
        r'<div class="flex items-center gap-3"><div class="w-8 h-8 rounded-lg bg-primary[^>]*>'
        r'<span class="material-symbols-outlined text-lg">graphic_eq</span></div>'
        r'<span[^>]*>QredPilot</span></div>',
        LOGO_IMG.replace('height:30px', 'height:28px'), html, what="footer brand")
    # fake profile avatar in the header -> remove (marketing page, nobody is logged in)
    html = re.sub(r'<img alt="Profile"[^>]*>', '', html)
    # favicon
    html = html.replace("</head>", '<link rel="icon" type="image/png" href="assets/favicon.png"/></head>', 1)
    return html


def localize_images(html):
    """Download remote googleusercontent images into assets/ and point at the copies."""
    for url in set(re.findall(r'https://lh3\.googleusercontent\.com/[^"]+', html)):
        name = "img-" + hashlib.sha1(url.encode()).hexdigest()[:10] + ".png"
        dest = ASSETS / name
        if not dest.exists():
            try:
                urllib.request.urlretrieve(url, dest)
            except OSError as e:  # link expired: leave the remote URL in place
                print("  ! could not fetch", url[:60], e)
                continue
        html = html.replace(url, f"assets/{name}")
    return html


def build():
    ASSETS.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "index.html", OUT / "index.html")
    print("built", OUT / "index.html", "(hand-written)")
    for src, name in PAGES.items():
        html = (ROOT / src / "code.html").read_text()
        for old, new in EDITS[name]:
            assert html.count(old) == 1, f"{name}: expected one match for {old[:60]!r}"
            html = html.replace(old, new)
        html = rebrand(html)
        html = localize_images(html)
        # sticky header would hide anchored section titles
        html = html.replace("</head>", "<style>html{scroll-padding-top:5.5rem;scroll-behavior:smooth}</style></head>", 1)
        html = re.sub(
            r'data-path="([\w-]+)"(\s+)href="#"',
            lambda m: f'data-path="{m[1]}"{m[2]}href="{LINKS.get(m[1], "#")}"',
            html,
        )
        (OUT / name).write_text(html)
        print("built", OUT / name)


if __name__ == "__main__":
    build()
