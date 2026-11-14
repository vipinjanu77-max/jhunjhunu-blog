#!/usr/bin/env python3
"""Jhunjhunu Blog launch site generator. Static, bilingual (hi default, en), no dependencies.
Usage: python3 build.py [BASE_URL]   -> writes ./dist
"""
import os, sys, shutil, html, json, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sections as SEC
import portal as PORTAL

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://vipinjanu77-max.github.io/jhunjhunu-blog/").rstrip("/") + "/"
DIST = os.path.join(ROOT, "docs")
IG = "https://www.instagram.com/jhunjhunu_blog/"
IG_DM = "https://ig.me/m/jhunjhunu_blog"
CHECKED = {"en": "21 Oct 2026", "hi": "21 अक्टू॰ 2026"}

T = {
 "en": dict(explore="Explore", jobs="Jobs", events="Events", businesses="Businesses", advertise="Advertise with us", home="Home", talks="Jhunjhunu Talks", info="Services & helplines", facts="Know Jhunjhunu", videos="Videos", help="Need help?", involve="Get involved", about="About",
   editorial="Editorial policy", corrections="Corrections", privacy="Privacy policy", terms="Terms",
   other="हिंदी", other_lang="hi", skip="Skip to content", menu="Menu", follow="Follow on Instagram",
   promise="Jhunjhunu Ki Kahani, Jhunjhunu Ke Logon Ki Zubaani.", independent="Jhunjhunu Blog is independent. Sponsored content, when there is any, will always be labelled.",
   official="Official link ↗", applies="Applies to", source="Source", checked="Last checked", all_india="All India",
   notgov="Jhunjhunu Blog is an independent platform, not a government website. Always confirm with the official source.",
   share="Share on WhatsApp", sections="Sections", jb="Jhunjhunu Blog", policies="Policies", cat_help="Emergency & helplines",
   report="Spotted a mistake? Tell us", nf_title="Page not found", nf_text="This page doesn't exist, or it has moved.", nf_btn="Go to the home page"),
 "hi": dict(explore="घूमिए", jobs="नौकरी", events="कार्यक्रम", businesses="कारोबार", advertise="हमारे साथ विज्ञापन", home="होम", talks="झुंझुनू टॉक्स", info="सेवाएँ और हेल्पलाइन", facts="जानिए झुंझुनू", videos="वीडियो", help="मदद", involve="जुड़िए", about="हमारे बारे में",
   editorial="संपादकीय नीति", corrections="सुधार", privacy="गोपनीयता नीति", terms="उपयोग की शर्तें",
   other="English", other_lang="en", skip="मुख्य सामग्री पर जाएँ", menu="मेन्यू", follow="Instagram पर फ़ॉलो करें",
   promise="झुंझुनू की कहानी, झुंझुनू के लोगों की ज़ुबानी।", independent="झुंझुनू ब्लॉग स्वतंत्र है। प्रायोजित सामग्री होने पर उस पर हमेशा साफ़ लेबल रहेगा।",
   official="आधिकारिक लिंक ↗", applies="लागू क्षेत्र", source="स्रोत", checked="अंतिम जाँच", all_india="पूरे भारत में",
   notgov="झुंझुनू ब्लॉग एक स्वतंत्र प्लेटफ़ॉर्म है, सरकारी वेबसाइट नहीं। हमेशा आधिकारिक स्रोत से पुष्टि करें।",
   share="WhatsApp पर शेयर करें", sections="सेक्शन", jb="झुंझुनू ब्लॉग", policies="नीतियाँ", cat_help="आपातकालीन और हेल्पलाइन",
   report="कोई ग़लती दिखी? हमें बताइए", nf_title="पेज नहीं मिला", nf_text="यह पेज मौजूद नहीं है या इसका पता बदल गया है।", nf_btn="होम पेज पर जाएँ"),
}

NAV = ["jobs", "events", "businesses", "explore", "info", "facts", "videos", "help"]
SVG_MENU = '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h16v2H4z"/></svg>'
SVG_IG = '<svg class="icon icon-sm" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5Zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7Zm5 3.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Zm0 2a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5ZM17.5 5.8a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"/></svg>'

e = html.escape

def page(lang, slug, title, desc, body, crumbs=None, og_type="website"):
    """slug: '' for home, or 'info/112-...' etc. Writes dist/<lang>/<slug>/index.html"""
    t = T[lang]
    depth = 1 + (len(slug.split("/")) if slug else 0)
    up = "../" * depth            # to site root
    home = up + lang + "/"
    def href(s): return home + (s + "/" if s else "")
    path = f"{lang}/{slug + '/' if slug else ''}"
    other = t["other_lang"]
    url = BASE + path
    alt_hi, alt_en = BASE + f"hi/{slug + '/' if slug else ''}", BASE + f"en/{slug + '/' if slug else ''}"
    full_title = title if slug == "" else f"{title} | {t['jb']}"
    nav = "".join(f'<li><a href="{href(k)}"{" aria-current=\"page\"" if slug.split("/")[0]==k else ""}>{e(t[k])}</a></li>' for k in NAV)
    crumb_html = ""
    if crumbs is not None:
        items = [f'<li><a href="{href("")}">{e(t["home"])}</a></li>'] + [f'<li><a href="{href(s)}">{e(n)}</a></li>' for n, s in crumbs] + [f'<li><span aria-current="page">{e(title)}</span></li>']
        crumb_html = f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
    ld = {"@context": "https://schema.org", "@type": "Organization", "name": "Jhunjhunu Blog", "alternateName": "झुंझुनू ब्लॉग",
          "url": BASE, "logo": BASE + "brand/logo-360.png", "sameAs": [IG],
          "areaServed": {"@type": "AdministrativeArea", "name": "Jhunjhunu district, Rajasthan, India"}}
    doc = f'''<!doctype html>
<html lang="{lang}-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#720412">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="hi-IN" href="{alt_hi}"><link rel="alternate" hreflang="en-IN" href="{alt_en}"><link rel="alternate" hreflang="x-default" href="{alt_hi}">
<meta property="og:site_name" content="Jhunjhunu Blog">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{lang}_IN">
<meta property="og:image" content="{BASE}brand/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mukta:wght@400;500;700&family=Tiro+Devanagari+Hindi&display=swap">
<link rel="stylesheet" href="{up}css/site.css">
<link rel="icon" href="{up}brand/favicon.png">
<link rel="apple-touch-icon" href="{up}brand/favicon.png">
</head>
<body data-lang="{lang}">
<a class="skip" href="#main">{e(t["skip"])}</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="logo" href="{href("")}" aria-label="{e(t["jb"])}, {e(t["home"])}">
      <img src="{up}brand/logo-360.png" width="142" height="80" alt="{e(t["jb"])}">
    </a>
    <div class="header-actions">
      <a class="lang-switch" href="{up}{other}/{slug + '/' if slug else ''}" hreflang="{other}-IN" lang="{other}">{e(t["other"])}</a>
      <a class="btn btn-small btn-primary hide-sm" href="{IG}" target="_blank" rel="noopener">{SVG_IG} {e(t["follow"])}</a>
      <details class="mobile-menu">
        <summary aria-label="{e(t["menu"])}">{SVG_MENU}<span class="sr-only">{e(t["menu"])}</span></summary>
        <nav class="mobile-nav" aria-label="{e(t["menu"])}">
          <ul><li><a href="{href("")}">{e(t["home"])}</a></li>{nav}<li><a href="{href("about")}">{e(t["about"])}</a></li></ul>
          <ul class="mobile-secondary"><li><a href="{IG}" target="_blank" rel="noopener">{e(t["follow"])}</a></li></ul>
        </nav>
      </details>
    </div>
  </div>
  <nav class="main-nav" aria-label="Main"><div class="wrap"><ul>{nav}</ul></div></nav>
</header>
<main id="main">
{crumb_html and f'<div class="wrap page-crumbs">{crumb_html}</div>'}
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <img src="{up}brand/logo-360.png" width="142" height="80" alt="{e(t["jb"])}" class="footer-logo" loading="lazy">
      <p class="footer-promise">{e(t["promise"])}</p>
      <p class="muted small">{e(t["independent"])}</p>
    </div>
    <nav aria-label="{e(t["sections"])}"><h2 class="footer-h">{e(t["sections"])}</h2><ul>
      <li><a href="{href("videos")}">{e(t["videos"])}</a></li><li><a href="{href("facts")}">{e(t["facts"])}</a></li><li><a href="{href("explore")}">{e(t["explore"])}</a></li><li><a href="{href("jobs")}">{e(t["jobs"])}</a></li><li><a href="{href("events")}">{e(t["events"])}</a></li><li><a href="{href("businesses")}">{e(t["businesses"])}</a></li><li><a href="{href("info")}">{e(t["info"])}</a></li></ul></nav>
    <nav aria-label="{e(t["jb"])}"><h2 class="footer-h">{e(t["jb"])}</h2><ul>
      <li><a href="{href("about")}">{e(t["about"])}</a></li><li><a href="{href("help")}">{e(t["help"])}</a></li><li><a href="{href("involve")}">{e(t["involve"])}</a></li><li><a href="{href("advertise")}">{e(t["advertise"])}</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram ↗</a></li></ul></nav>
    <nav aria-label="{e(t["policies"])}"><h2 class="footer-h">{e(t["policies"])}</h2><ul>
      <li><a href="{href("editorial-policy")}">{e(t["editorial"])}</a></li><li><a href="{href("corrections")}">{e(t["corrections"])}</a></li>
      <li><a href="{href("privacy")}">{e(t["privacy"])}</a></li><li><a href="{href("terms")}">{e(t["terms"])}</a></li></ul></nav>
  </div>
  <div class="wrap footer-base"><span>© 2026 Jhunjhunu Blog · Jhunjhunu, Rajasthan</span>
    <a href="{up}{other}/{slug + '/' if slug else ''}" lang="{other}">{e(t["other"])}</a></div>
</footer>
</body>
</html>
'''
    out = os.path.join(DIST, path, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(doc)
    return path

# ---------------------------------------------------------------- content
INFO = [
 dict(slug="112-national-emergency-number", num="112", off="https://112.gov.in/", src="https://112.gov.in/", src_name="112.gov.in",
   en=dict(title="112: National emergency number (police, fire, ambulance)",
     lead="India's single emergency number, run under the Emergency Response Support System (ERSS).",
     body="<p>Call 112 for police, fire or ambulance help anywhere in India. The call is free.</p><p>What we have not yet confirmed: how 112 calls are routed inside Jhunjhunu district. If you know, tell us and include a source.</p>"),
   hi=dict(title="112: राष्ट्रीय आपातकालीन नंबर (पुलिस, फ़ायर, एम्बुलेंस)",
     lead="भारत का एक ही आपातकालीन नंबर, जो इमरजेंसी रिस्पॉन्स सपोर्ट सिस्टम (ERSS) के तहत चलता है।",
     body="<p>पुलिस, फ़ायर या एम्बुलेंस की मदद के लिए भारत में कहीं से भी 112 पर कॉल करें। कॉल मुफ़्त है।</p><p>जो हमने अभी पक्का नहीं किया है: झुंझुनू ज़िले के अंदर 112 की कॉल किस तरह आगे भेजी जाती है। अगर आप जानते हैं तो स्रोत के साथ हमें बताइए।</p>")),
 dict(slug="1930-cyber-fraud-helpline", num="1930", off="https://cybercrime.gov.in/", src="https://cybercrime.gov.in/", src_name="cybercrime.gov.in",
   en=dict(title="1930: Cyber fraud helpline and cybercrime.gov.in",
     lead="Report online financial fraud on 1930, or file a complaint on the National Cyber Crime Reporting Portal.",
     body="<p>If you have lost money to online fraud, report it as quickly as you can.</p><ul><li>Call 1930</li><li>Or file a complaint at cybercrime.gov.in</li></ul>"),
   hi=dict(title="1930: साइबर धोखाधड़ी हेल्पलाइन और cybercrime.gov.in",
     lead="ऑनलाइन वित्तीय धोखाधड़ी की शिकायत 1930 पर करें या राष्ट्रीय साइबर अपराध रिपोर्टिंग पोर्टल पर दर्ज करें।",
     body="<p>अगर ऑनलाइन धोखाधड़ी से आपके पैसे गए हैं, तो जितनी जल्दी हो सके शिकायत करें।</p><ul><li>1930 पर कॉल करें</li><li>या cybercrime.gov.in पर शिकायत दर्ज करें</li></ul>")),
]

def info_card(lang, it, href):
    t, c = T[lang], it[lang]
    return f'''<article class="info-item info-compact">
  <div class="info-main"><div class="card-top"><span class="card-cat">{e(t["cat_help"])}</span></div>
    <h3 class="card-title"><a href="{href}">{e(c["title"])}</a></h3>
    <p class="row-meta">{e(t["applies"])}: {e(t["all_india"])}</p><p class="checked">{e(t["checked"])}: {CHECKED[lang]}</p></div>
  <div class="info-actions"><a class="btn btn-primary btn-small" href="tel:{it["num"]}">{it["num"]}</a>
    <a class="btn btn-ghost btn-small" href="{it["off"]}" target="_blank" rel="noopener">{e(t["official"])}</a></div>
</article>'''

COPY = {
 "en": dict(
  home_title="Jhunjhunu Blog: Jhunjhunu's people, stories and conversations",
  home_desc="Jhunjhunu Blog tells the stories of Jhunjhunu and its people through long-form conversations, local stories and useful information.",
  eyebrow="Jhunjhunu Ki Kahani, Jhunjhunu Ke Logon Ki Zubaani",
  h1="Jhunjhunu's people, stories and conversations.",
  sub="We're starting with honest, long-form conversations with the people who make Jhunjhunu what it is: entrepreneurs, teachers, veterans, artists, achievers and everyday local heroes.",
  cta2="Suggest a guest",
  talks_h="JHUNJHUNU TALKS", talks_p="Our long-form interview show. The first episodes are being recorded now. Follow us on Instagram to know the moment Episode 1 is out.",
  talks_more="About the show",
  pillars_h="What we'll cover",
  pillars=[("People", "Stories of people from Jhunjhunu, and what the district can learn from them."), ("Entrepreneurs", "How local businesses started, struggled and grew."),
           ("Local heroes", "Teachers, volunteers, farmers, coaches and craftspeople doing meaningful work."), ("Culture & heritage", "Shekhawati's havelis, food, folk culture and memories.")],
  ess_h="Everyday essentials", ess_p="Helplines and official links, each with its source and the date we last checked it.", all="View all",
  inv_h="Know a story Jhunjhunu should hear?", inv_p="Tell us who we should interview next, or which local story deserves to be told. Send us a message on Instagram.", inv_btn="Message us on Instagram",
  # talks
  t_title="JHUNJHUNU TALKS", t_desc="JHUNJHUNU TALKS is Jhunjhunu Blog's long-form interview show with the people of Jhunjhunu.",
  t_lead="Long-form conversations with the people of Jhunjhunu: how they started, the decisions that changed their lives, and what they've learned.",
  t_body="""<h2>What to expect</h2><p>Each episode is one unhurried conversation. Not a list of achievements, but the real story: the roots, the struggles, the turning point, the failures and the lessons, and why Jhunjhunu matters to it.</p>
<h2>Episodes</h2><div class="empty"><p class="empty-title">The first episodes are in production.</p><p class="muted">Episodes will appear here as they're published. Follow us on Instagram so you don't miss Episode 1.</p></div>
<h2>Our promise to guests and viewers</h2><ul><li>We research every guest before we sit down with them.</li><li>We never change what a guest meant to make a clip more dramatic.</li><li>If a business pays for any feature, it will be clearly labelled as sponsored.</li></ul>""",
  t_suggest="Suggest a guest",
  # info
  i_title="Services & helplines", i_desc="Emergency helplines and online government services for Jhunjhunu: SSO, e-Mitra, Jan Aadhaar, Rajasthan Sampark 181, land records and more.",
  i_lead="Helplines and official links, each with where it applies, its source and the date we last checked it. We add an item only after checking it against an official source.",
  # involve
  g_title="Get involved", g_desc="Suggest a guest or a story for Jhunjhunu Blog, or tell us about a mistake.",
  g_lead="Jhunjhunu Blog is built with the people of Jhunjhunu. Here's how you can take part.",
  g_cards=[("Suggest a guest", "Know someone from Jhunjhunu with a story worth hearing? Tell us who they are and why."),
           ("Share a local story", "A business with an interesting history, a local hero, a tradition worth recording. Send it our way."),
           ("Report a mistake", "If something we published is wrong, tell us. We correct mistakes openly.")],
  g_how="All of these happen through Instagram messages for now. We read every message. We check any facts before we publish them, and we never share your details with anyone without your permission.",
  # about
  a_title="About Jhunjhunu Blog", a_desc="Jhunjhunu Blog is an independent local media platform from Jhunjhunu, Rajasthan.",
  a_body="""<p class="lead">Jhunjhunu Blog is an independent local media platform from Jhunjhunu, Rajasthan, in the Shekhawati region.</p>
<p>We begin as a conversation and storytelling platform: interviews and stories about the people, businesses, culture and community of Jhunjhunu district. Our first format is JHUNJHUNU TALKS, a long-form interview show.</p>
<h2>How we work</h2><ul><li>We check facts before we publish, and we say where information comes from.</li><li>We keep editorial and paid content apart. Anything sponsored is labelled.</li><li>We correct mistakes openly.</li><li>We get consent from the people we feature, and a parent's consent for anyone under 18.</li></ul>
<h2>Not a government website</h2><p>Jhunjhunu Blog is not run by or affiliated with any government office. For official decisions, always confirm with the official source we link to.</p>
<h2>Contact</h2><p>The quickest way to reach us is a message on Instagram, <a href="{IG}" target="_blank" rel="noopener">@jhunjhunu_blog</a>.</p>""",
  # policies
  e_title="Editorial policy", e_desc="How Jhunjhunu Blog checks facts, labels content and stays independent.",
  e_body="""<h2>Accuracy</h2><p>We check facts against official or primary sources before publishing. Useful-information items show their source and the date we last checked them.</p>
<h2>What we label</h2><ul><li><strong>Interview:</strong> a guest's own account, in their words. We check factual claims where we can, and say when we couldn't.</li><li><strong>Opinion:</strong> the author's view, clearly marked.</li><li><strong>Sponsored:</strong> paid for by a business and labelled wherever it appears.</li></ul>
<h2>Editing interviews</h2><p>We edit for length and clarity, but we never change what a guest meant, cut an answer so it says the opposite, or invent quotes.</p>
<h2>Independence</h2><p>Sponsors and partners have no say over our editorial decisions. Paying never buys a positive story. We do not publish political promotion as editorial content. If we have a personal or business connection to someone we cover, we say so.</p>
<h2>People and privacy</h2><p>We get consent from the people we feature, and a parent's consent for anyone under 18. We do not publish private details such as home addresses.</p>
<h2>Corrections</h2><p>If we get something wrong, we correct it openly. See our corrections page.</p>""",
  c_title="Corrections", c_desc="Corrections to anything published on Jhunjhunu Blog.",
  c_body="""<p class="lead">When we get something wrong, we correct it openly and note what changed and when.</p>
<p>To report a mistake, send us a message on Instagram with the page and what's wrong. If you can, include a source.</p>
<h2>Corrections log</h2><div class="empty"><p class="muted">No corrections so far.</p></div>""",
  p_title="Privacy policy", p_desc="What information Jhunjhunu Blog collects and how it is used.",
  p_body="""<p class="lead">This website has no accounts and no advertising trackers.</p>
<h2>What this website collects</h2><ul><li>We do not use analytics or advertising cookies.</li><li>The website is hosted on GitHub Pages, which may keep basic technical logs (such as IP addresses) to run and secure the service. Fonts are loaded from Google Fonts, and the home-page weather from Open-Meteo. Both receive your IP address when the page loads.</li></ul>
<h2>Forms (resume, job posts, listings, questions)</h2><p>When you send us your resume or a submission, we use it only for the purpose you sent it for. Resumes are shared with an employer only after you agree. You can ask us to delete your details at any time, and we delete resumes that have been inactive for 12 months.</p>
<h2>When you message us</h2><p>If you message us on Instagram, we see what you send and your Instagram profile. We use it only to reply and to follow up on your suggestion. We do not sell it or share it with any business without your clear permission, and we do not add you to any WhatsApp group or list automatically.</p>
<h2>Your choices</h2><p>You can ask us to delete your messages or any details you've shared with us by messaging us on Instagram.</p>
<p class="small muted">Last updated: 14 Nov 2026.</p>""",
  tm_title="Terms of use", tm_desc="Terms for using the Jhunjhunu Blog website.",
  tm_body="""<h2>Using the site</h2><p>Information on Jhunjhunu Blog is provided in good faith and checked where stated, but it can change. Confirm important details, especially fees, timings and government processes, with the official source.</p>
<h2>Interviews and opinions</h2><p>Views expressed by guests in interviews are their own and are not necessarily the views of Jhunjhunu Blog.</p>
<h2>Our content</h2><p>Text, photos and videos on this site belong to Jhunjhunu Blog or the people who created them. You're welcome to share links. Please ask before reusing our content elsewhere.</p>
<h2>Suggestions</h2><p>When you send us a suggestion or a story, you confirm it is accurate as far as you know. We may check, edit, decline or not use any suggestion.</p>
<h2>Reporting problems</h2><p>If something is wrong, message us on Instagram and we will review it.</p>
<p class="small muted">Last updated: 14 Nov 2026.</p>"""),
 "hi": dict(
  home_title="झुंझुनू ब्लॉग: झुंझुनू के लोग, कहानियाँ और बातचीत",
  home_desc="झुंझुनू ब्लॉग लंबी बातचीत, स्थानीय कहानियों और ज़रूरी जानकारी के ज़रिए झुंझुनू और यहाँ के लोगों की कहानियाँ सामने लाता है।",
  eyebrow="झुंझुनू की कहानी, झुंझुनू के लोगों की ज़ुबानी",
  h1="झुंझुनू के लोग, कहानियाँ और बातचीत।",
  sub="हम शुरुआत कर रहे हैं उन लोगों से खुली और लंबी बातचीत के साथ जो झुंझुनू को झुंझुनू बनाते हैं: उद्यमी, शिक्षक, फ़ौजी, कलाकार, उपलब्धि हासिल करने वाले और हमारे आस-पास के असली हीरो।",
  cta2="मेहमान सुझाइए",
  talks_h="झुंझुनू टॉक्स", talks_p="हमारा लंबा इंटरव्यू शो। पहले एपिसोड की रिकॉर्डिंग चल रही है। एपिसोड 1 आते ही जानने के लिए हमें Instagram पर फ़ॉलो करें।",
  talks_more="शो के बारे में",
  pillars_h="हम किन चीज़ों पर बात करेंगे",
  pillars=[("लोग", "झुंझुनू के लोगों की कहानियाँ, और उनसे ज़िला क्या सीख सकता है।"), ("उद्यमी", "स्थानीय कारोबार कैसे शुरू हुए, किन मुश्किलों से गुज़रे और कैसे बढ़े।"),
           ("स्थानीय हीरो", "शिक्षक, स्वयंसेवक, किसान, कोच और कारीगर जो सार्थक काम कर रहे हैं।"), ("संस्कृति और विरासत", "शेखावाटी की हवेलियाँ, खान-पान, लोक संस्कृति और यादें।")],
  ess_h="रोज़ काम की जानकारी", ess_p="हेल्पलाइन और आधिकारिक लिंक, हर एक के साथ उसका स्रोत और हमारी पिछली जाँच की तारीख़।", all="सब देखें",
  inv_h="कोई ऐसी कहानी जो झुंझुनू को सुननी चाहिए?", inv_p="हमें बताइए कि अगला इंटरव्यू किसका हो, या कौन-सी स्थानीय कहानी सामने आनी चाहिए। Instagram पर हमें मैसेज करें।", inv_btn="Instagram पर मैसेज करें",
  t_title="झुंझुनू टॉक्स", t_desc="झुंझुनू टॉक्स, झुंझुनू ब्लॉग का झुंझुनू के लोगों के साथ लंबा इंटरव्यू शो है।",
  t_lead="झुंझुनू के लोगों के साथ लंबी बातचीत: उन्होंने शुरुआत कैसे की, किन फ़ैसलों ने उनकी ज़िंदगी बदली, और उन्होंने क्या सीखा।",
  t_body="""<h2>शो में क्या होगा</h2><p>हर एपिसोड एक इत्मीनान भरी बातचीत है। उपलब्धियों की लिस्ट नहीं, बल्कि असली कहानी: जड़ें, संघर्ष, मोड़, नाकामियाँ और सबक, और इस कहानी में झुंझुनू की जगह।</p>
<h2>एपिसोड</h2><div class="empty"><p class="empty-title">पहले एपिसोड तैयार हो रहे हैं।</p><p class="muted">एपिसोड प्रकाशित होते ही यहाँ दिखेंगे। एपिसोड 1 मिस न हो, इसके लिए Instagram पर फ़ॉलो करें।</p></div>
<h2>मेहमानों और दर्शकों से हमारा वादा</h2><ul><li>हर मेहमान से बात करने से पहले हम उनके बारे में रिसर्च करते हैं।</li><li>क्लिप को ज़्यादा नाटकीय बनाने के लिए हम कभी मेहमान की बात का मतलब नहीं बदलते।</li><li>अगर कोई कारोबार किसी फ़ीचर के लिए भुगतान करता है, तो उस पर साफ़ "प्रायोजित" लिखा होगा।</li></ul>""",
  t_suggest="मेहमान सुझाइए",
  i_title="सेवाएँ और हेल्पलाइन", i_desc="झुंझुनू के लिए आपातकालीन हेल्पलाइन और ऑनलाइन सरकारी सेवाएँ: SSO, ई-मित्र, जन आधार, राजस्थान संपर्क 181, भूमि रिकॉर्ड और बहुत कुछ।",
  i_lead="हेल्पलाइन और आधिकारिक लिंक, हर एक के साथ उसका लागू क्षेत्र, स्रोत और हमारी पिछली जाँच की तारीख़। हम कोई भी जानकारी आधिकारिक स्रोत से मिलान करने के बाद ही जोड़ते हैं।",
  g_title="जुड़िए", g_desc="झुंझुनू ब्लॉग के लिए कोई मेहमान या कहानी सुझाइए, या किसी ग़लती के बारे में बताइए।",
  g_lead="झुंझुनू ब्लॉग झुंझुनू के लोगों के साथ मिलकर बन रहा है। आप ऐसे जुड़ सकते हैं।",
  g_cards=[("मेहमान सुझाइए", "झुंझुनू के किसी ऐसे व्यक्ति को जानते हैं जिसकी कहानी सुनने लायक है? हमें बताइए वे कौन हैं और क्यों।"),
           ("कोई स्थानीय कहानी भेजिए", "कोई दिलचस्प इतिहास वाला कारोबार, कोई स्थानीय हीरो, कोई परंपरा जिसे दर्ज किया जाना चाहिए। हमें भेजिए।"),
           ("ग़लती बताइए", "अगर हमारी प्रकाशित किसी बात में ग़लती है, तो हमें बताइए। हम ग़लतियाँ खुलकर सुधारते हैं।")],
  g_how="फ़िलहाल यह सब Instagram मैसेज से होता है। हम हर मैसेज पढ़ते हैं। प्रकाशित करने से पहले हम तथ्यों की जाँच करते हैं, और आपकी अनुमति के बिना आपकी जानकारी किसी से साझा नहीं करते।",
  a_title="हमारे बारे में", a_desc="झुंझुनू ब्लॉग, झुंझुनू (राजस्थान) का एक स्वतंत्र स्थानीय मीडिया प्लेटफ़ॉर्म है।",
  a_body="""<p class="lead">झुंझुनू ब्लॉग, शेखावाटी क्षेत्र के झुंझुनू (राजस्थान) का एक स्वतंत्र स्थानीय मीडिया प्लेटफ़ॉर्म है।</p>
<p>हमारी शुरुआत बातचीत और कहानियों के प्लेटफ़ॉर्म के रूप में हो रही है: झुंझुनू ज़िले के लोगों, कारोबार, संस्कृति और समुदाय पर इंटरव्यू और कहानियाँ। हमारा पहला फ़ॉर्मेट है झुंझुनू टॉक्स, एक लंबा इंटरव्यू शो।</p>
<h2>हम कैसे काम करते हैं</h2><ul><li>प्रकाशित करने से पहले हम तथ्यों की जाँच करते हैं, और बताते हैं कि जानकारी कहाँ से आई है।</li><li>संपादकीय और भुगतान वाली सामग्री को हम अलग रखते हैं। प्रायोजित सामग्री पर लेबल होता है।</li><li>हम ग़लतियाँ खुलकर सुधारते हैं।</li><li>जिनकी कहानी हम दिखाते हैं उनकी सहमति लेते हैं, और 18 साल से कम उम्र वालों के लिए माता-पिता की सहमति।</li></ul>
<h2>सरकारी वेबसाइट नहीं</h2><p>झुंझुनू ब्लॉग किसी सरकारी दफ़्तर द्वारा नहीं चलाया जाता और न ही उससे जुड़ा है। सरकारी काम के लिए हमेशा उस आधिकारिक स्रोत से पुष्टि करें जिसका लिंक हम देते हैं।</p>
<h2>संपर्क</h2><p>हम तक पहुँचने का सबसे आसान तरीक़ा है Instagram पर मैसेज: <a href="{IG}" target="_blank" rel="noopener">@jhunjhunu_blog</a>।</p>""",
  e_title="संपादकीय नीति", e_desc="झुंझुनू ब्लॉग तथ्यों की जाँच कैसे करता है, सामग्री पर लेबल कैसे लगाता है और स्वतंत्र कैसे रहता है।",
  e_body="""<h2>सटीकता</h2><p>प्रकाशित करने से पहले हम तथ्यों को आधिकारिक या मूल स्रोतों से मिलाते हैं। ज़रूरी जानकारी के हर आइटम पर उसका स्रोत और पिछली जाँच की तारीख़ लिखी होती है।</p>
<h2>हम क्या लेबल करते हैं</h2><ul><li><strong>इंटरव्यू:</strong> मेहमान की अपनी बात, उनके शब्दों में। जहाँ हो सके हम तथ्यों की जाँच करते हैं, और जहाँ न हो सके वहाँ यह बताते हैं।</li><li><strong>राय:</strong> लेखक का अपना नज़रिया, साफ़ तौर पर चिह्नित।</li><li><strong>प्रायोजित:</strong> किसी कारोबार द्वारा भुगतान किया गया, और जहाँ भी दिखे वहाँ लेबल के साथ।</li></ul>
<h2>इंटरव्यू की एडिटिंग</h2><p>हम लंबाई और स्पष्टता के लिए एडिट करते हैं, लेकिन कभी मेहमान की बात का मतलब नहीं बदलते, जवाब को काटकर उलटा मतलब नहीं बनाते, और न ही कोई बात गढ़ते हैं।</p>
<h2>स्वतंत्रता</h2><p>प्रायोजकों और पार्टनर्स का हमारे संपादकीय फ़ैसलों पर कोई दख़ल नहीं होता। पैसे से अच्छी कहानी नहीं ख़रीदी जा सकती। हम राजनीतिक प्रचार को संपादकीय सामग्री के रूप में प्रकाशित नहीं करते। अगर जिसके बारे में हम लिख रहे हैं उससे हमारा कोई निजी या कारोबारी संबंध है, तो हम यह बताते हैं।</p>
<h2>लोग और गोपनीयता</h2><p>जिनकी कहानी हम दिखाते हैं उनकी सहमति लेते हैं, और 18 साल से कम उम्र वालों के लिए माता-पिता की सहमति। हम घर का पता जैसी निजी जानकारी प्रकाशित नहीं करते।</p>
<h2>सुधार</h2><p>अगर हमसे कोई ग़लती होती है, तो हम उसे खुलकर सुधारते हैं। हमारा सुधार पेज देखें।</p>""",
  c_title="सुधार", c_desc="झुंझुनू ब्लॉग पर प्रकाशित किसी भी सामग्री में किए गए सुधार।",
  c_body="""<p class="lead">जब हमसे कोई ग़लती होती है, तो हम उसे खुलकर सुधारते हैं और बताते हैं कि क्या और कब बदला।</p>
<p>ग़लती बताने के लिए Instagram पर हमें पेज और ग़लती के बारे में मैसेज करें। हो सके तो स्रोत भी भेजें।</p>
<h2>सुधार रिकॉर्ड</h2><div class="empty"><p class="muted">अभी तक कोई सुधार नहीं।</p></div>""",
  p_title="गोपनीयता नीति", p_desc="झुंझुनू ब्लॉग कौन-सी जानकारी लेता है और उसका इस्तेमाल कैसे होता है।",
  p_body="""<p class="lead">इस वेबसाइट पर कोई अकाउंट और कोई विज्ञापन ट्रैकर नहीं है।</p>
<h2>यह वेबसाइट क्या जानकारी लेती है</h2><ul><li>हम एनालिटिक्स या विज्ञापन कुकीज़ का इस्तेमाल नहीं करते।</li><li>वेबसाइट GitHub Pages पर होस्ट है, जो सेवा चलाने और सुरक्षित रखने के लिए बुनियादी तकनीकी लॉग (जैसे IP पता) रख सकता है। फ़ॉन्ट Google Fonts से और होम पेज का मौसम Open-Meteo से लोड होता है। पेज खुलते समय दोनों को आपका IP पता मिलता है।</li></ul>
<h2>फ़ॉर्म (रिज़्यूमे, नौकरी पोस्ट, लिस्टिंग, सवाल)</h2><p>आप जो रिज़्यूमे या जानकारी भेजते हैं, उसका इस्तेमाल हम सिर्फ़ उसी काम के लिए करते हैं जिसके लिए आपने भेजा है। रिज़्यूमे किसी नियोक्ता को आपकी सहमति के बाद ही दिया जाता है। आप कभी भी अपनी जानकारी हटाने के लिए कह सकते हैं, और 12 महीने से निष्क्रिय रिज़्यूमे हम हटा देते हैं।</p>
<h2>जब आप हमें मैसेज करते हैं</h2><p>अगर आप Instagram पर हमें मैसेज करते हैं, तो हमें आपका मैसेज और आपकी Instagram प्रोफ़ाइल दिखती है। हम इसका इस्तेमाल सिर्फ़ जवाब देने और आपके सुझाव पर आगे काम करने के लिए करते हैं। हम इसे बेचते नहीं, आपकी साफ़ अनुमति के बिना किसी कारोबार से साझा नहीं करते, और आपको अपने-आप किसी WhatsApp ग्रुप या लिस्ट में नहीं जोड़ते।</p>
<h2>आपके विकल्प</h2><p>आप Instagram पर मैसेज करके हमसे अपने मैसेज या साझा की गई कोई भी जानकारी हटाने के लिए कह सकते हैं।</p>
<p class="small muted">पिछला अपडेट: 14 नवं॰ 2026।</p>""",
  tm_title="उपयोग की शर्तें", tm_desc="झुंझुनू ब्लॉग वेबसाइट के इस्तेमाल की शर्तें।",
  tm_body="""<h2>साइट का इस्तेमाल</h2><p>झुंझुनू ब्लॉग पर जानकारी नेक नीयत से दी जाती है और जहाँ लिखा हो वहाँ जाँची गई होती है, लेकिन यह बदल सकती है। ज़रूरी बातें, ख़ासकर फ़ीस, समय और सरकारी प्रक्रियाएँ, आधिकारिक स्रोत से पक्की करें।</p>
<h2>इंटरव्यू और राय</h2><p>इंटरव्यू में मेहमानों के विचार उनके अपने हैं, ज़रूरी नहीं कि वे झुंझुनू ब्लॉग के विचार हों।</p>
<h2>हमारी सामग्री</h2><p>इस साइट के टेक्स्ट, फ़ोटो और वीडियो झुंझुनू ब्लॉग या उन्हें बनाने वालों के हैं। लिंक शेयर करने का स्वागत है। हमारी सामग्री कहीं और इस्तेमाल करने से पहले कृपया पूछ लें।</p>
<h2>सुझाव</h2><p>जब आप हमें कोई सुझाव या कहानी भेजते हैं, तो आप पुष्टि करते हैं कि आपकी जानकारी के हिसाब से वह सही है। हम किसी भी सुझाव की जाँच कर सकते हैं, उसे एडिट कर सकते हैं, या इस्तेमाल न करने का फ़ैसला कर सकते हैं।</p>
<h2>समस्या बताना</h2><p>अगर कुछ ग़लत है, तो Instagram पर मैसेज करें, हम उसकी समीक्षा करेंगे।</p>
<p class="small muted">पिछला अपडेट: 14 नवं॰ 2026।</p>"""),
}

def prose_page(lang, slug, title, desc, inner):
    body = f'<div class="wrap page detail-narrow"><h1>{e(title)}</h1><div class="prose">{inner.replace("{IG}", IG)}</div></div>'
    page(lang, slug, title, desc, body, crumbs=[])

def build():
    if os.path.exists(DIST): shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(ROOT, "static"), DIST, dirs_exist_ok=True)
    for lang in ("hi", "en"):
        t, c = T[lang], COPY[lang]
        up = "../"
        # ---- home (city portal)
        ess = "".join(info_card(lang, it, f'info/{it["slug"]}/') for it in INFO)
        _, explore_band = SEC.home_extra(lang)
        page(lang, "", PORTAL.P[lang]["h1"] + " | " + t["jb"], PORTAL.P[lang]["sub"], PORTAL.home(lang, T, IG, IG_DM, explore_band, ess))
        # ---- old talks URL -> videos
        tdir = os.path.join(DIST, lang, "talks"); os.makedirs(tdir, exist_ok=True)
        open(os.path.join(tdir, "index.html"), "w").write(f'<!doctype html><meta charset="utf-8"><title>Videos</title><link rel="canonical" href="{BASE}{lang}/videos/"><meta http-equiv="refresh" content="0; url=../videos/"><a href="../videos/">Videos</a>')
        # ---- info list + items
        cards = "".join(info_card(lang, it, f'{it["slug"]}/') for it in INFO)
        page(lang, "info", c["i_title"], c["i_desc"], f'''<div class="wrap page"><h1>{e(c["i_title"])}</h1><p class="lead detail-narrow">{e(c["i_lead"])}</p>
<div class="info-group"><h2>{e(t["cat_help"])}</h2><div class="essentials">{cards}</div></div>
<div class="info-group"><h2>{e(PORTAL.P[lang]["services_h"])}</h2><div class="essentials">{PORTAL.gov_cards(lang, T)}</div><p class="checked">{e(t["checked"])}: {SEC.CHECKED2[lang]}</p></div><p class="notice notice-info">{e(t["notgov"])}</p></div>''', crumbs=[])
        for it in INFO:
            ci = it[lang]; url = BASE + f'{lang}/info/{it["slug"]}/'
            wa = "https://wa.me/?text=" + urllib.parse.quote(ci["title"] + " " + url)
            page(lang, f'info/{it["slug"]}', ci["title"], ci["lead"], f'''<div class="wrap page detail detail-info">
<div class="detail-badges"><span class="card-cat">{e(t["cat_help"])}</span></div><h1>{e(ci["title"])}</h1>
<p class="detail-scope"><span class="scope">{e(t["all_india"])}</span></p><div class="detail-narrow"><p class="lead">{e(ci["lead"])}</p>
<div class="action-bar"><a class="btn btn-primary" href="tel:{it["num"]}">{it["num"]}</a><a class="btn btn-ghost" href="{it["off"]}" target="_blank" rel="noopener">{e(t["official"])}</a></div>
<dl class="facts"><div><dt>{e(t["applies"])}</dt><dd>{e(t["all_india"])}</dd></div><div><dt>{e(t["source"])}</dt><dd><a href="{it["src"]}" target="_blank" rel="noopener">{it["src_name"]}</a></dd></div></dl>
<p class="checked">{e(t["checked"])}: {CHECKED[lang]}</p><div class="prose">{ci["body"]}</div><p class="notice notice-info">{e(t["notgov"])}</p></div>
<div class="detail-tools"><div class="share"><a class="btn btn-ghost btn-small" href="{wa}" target="_blank" rel="noopener">{e(t["share"])}</a></div>
<a class="report-link" href="{IG_DM}" target="_blank" rel="noopener">{e(t["report"])}</a></div></div>''', crumbs=[(c["i_title"], "info")], og_type="article")
        # ---- involve
        gc = "".join(f'<article class="card"><h2 class="card-title">{e(a)}</h2><p class="card-text">{e(b)}</p></article>' for a, b in c["g_cards"])
        page(lang, "involve", c["g_title"], c["g_desc"], f'''<div class="wrap page"><h1>{e(c["g_title"])}</h1><p class="lead detail-narrow">{e(c["g_lead"])}</p>
<div class="grid grid-3">{gc}</div><div class="invite-box"><p>{e(c["g_how"])}</p><a class="btn btn-primary" href="{IG_DM}" target="_blank" rel="noopener">{e(c["inv_btn"])}</a></div></div>''', crumbs=[])
        # ---- prose pages
        prose_page(lang, "about", c["a_title"], c["a_desc"], c["a_body"])
        prose_page(lang, "editorial-policy", c["e_title"], c["e_desc"], c["e_body"])
        prose_page(lang, "corrections", c["c_title"], c["c_desc"], c["c_body"])
        prose_page(lang, "privacy", c["p_title"], c["p_desc"], c["p_body"])
        prose_page(lang, "terms", c["tm_title"], c["tm_desc"], c["tm_body"])
        SEC.build_sections(lang, page, IG, IG_DM, BASE)
        PORTAL.build_portal(lang, page, T, IG, IG_DM, BASE, INFO, DIST)
    # ---- root: Hindi-first redirect page
    open(os.path.join(DIST, "index.html"), "w").write(f'''<!doctype html><html lang="hi-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jhunjhunu Blog | झुंझुनू ब्लॉग</title><link rel="canonical" href="{BASE}hi/"><meta http-equiv="refresh" content="0; url=hi/">
<meta name="description" content="{e(COPY["hi"]["home_desc"])}"><meta property="og:title" content="Jhunjhunu Blog | झुंझुनू ब्लॉग"><meta property="og:image" content="{BASE}brand/og-image.png">
<link rel="icon" href="brand/favicon.png"><script>location.replace("hi/")</script></head>
<body style="font-family:system-ui;text-align:center;padding:40px;background:#FFF6E8"><img src="brand/logo-360.png" width="180" alt="Jhunjhunu Blog" style="margin:auto">
<p><a href="hi/">हिंदी</a> · <a href="en/">English</a></p></body></html>''')
    # ---- 404 (GitHub Pages serves /404.html for any missing path; use absolute asset URLs)
    t = T["hi"]
    open(os.path.join(DIST, "404.html"), "w").write(f'''<!doctype html><html lang="hi-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t["nf_title"]} | Jhunjhunu Blog</title><meta name="robots" content="noindex"><link rel="stylesheet" href="{BASE}css/site.css"><link rel="icon" href="{BASE}brand/favicon.png"></head>
<body><main class="wrap page detail-narrow" style="text-align:center;padding:60px 16px"><img src="{BASE}brand/logo-360.png" width="180" alt="Jhunjhunu Blog" style="margin:0 auto 20px">
<h1>{t["nf_title"]}</h1><p>{t["nf_text"]}</p><p lang="en" class="muted">{T["en"]["nf_text"]}</p>
<p class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="{BASE}hi/">{t["nf_btn"]}</a><a class="btn btn-ghost" href="{BASE}en/">Home (English)</a></p></main></body></html>''')
    PORTAL.search_index(DIST, BASE)
    # ---- sitemap / robots
    urls = []
    for root, _, files in os.walk(DIST):
        if "index.html" in files:
            rel = os.path.relpath(root, DIST).replace(os.sep, "/")
            if rel != ".": urls.append(BASE + rel + "/")
    sm = "\n".join(f"<url><loc>{u}</loc></url>" for u in sorted(urls))
    open(os.path.join(DIST, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    open(os.path.join(DIST, ".nojekyll"), "w").write("")
    # language memory (tiny inline-free script file)
    print(f"built {len(urls)} pages -> {DIST} (base {BASE})")

if __name__ == "__main__":
    build()
