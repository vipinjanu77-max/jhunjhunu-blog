"""Portal layer: city-portal home page, Videos section, Jhunjhunu facts, services, search, weather, highlights."""
import html, json, os, datetime
e = html.escape
ROOT = os.path.dirname(os.path.abspath(__file__))

# Forms: paste a form link (Tally / Google Form) here once created. Empty = fall back to Instagram DM.
FORMS = {"resume": "", "job_post": "", "listing": "", "event": "", "help": "", "apply": ""}

def today_ist():
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).date().isoformat()

def facts():
    data = json.load(open(os.path.join(ROOT, "facts.json")))
    t = today_ist()
    return [f for f in data if f.get("date", "") <= t]

FACT_CAT = {"Jhunjhunu Itihaas": ("Itihaas", "इतिहास"), "Shekhawati Itihaas": ("Itihaas", "इतिहास"), "Shekhawati Virasat": ("Heritage", "विरासत"),
            "Jhunjhunu Ka Garv": ("Pride of Jhunjhunu", "झुंझुनू का गौरव"), "Jhunjhunu Ke Udyogpati": ("Industrialists", "उद्योगपति"),
            "Kya Aap Jaante The?": ("Did you know?", "क्या आप जानते थे?")}

# ---- Highlights: curate weekly. Each needs a date and a source.
HIGHLIGHTS = [
 dict(date="2026-02-09", tag={"en": "Education", "hi": "शिक्षा"}, src=("ThePrint / PTI, 9 Feb 2026", "https://theprint.in/india/jhunjhunu-top-performer-in-academic-rankings-of-district-rajasthan-govt/2850096"),
   en=("Jhunjhunu ranked first in Rajasthan's district academic rankings", "The state school education department's district academic rankings for January 2026 put Jhunjhunu in first place."),
   hi=("राज्य की ज़िला एकेडमिक रैंकिंग में झुंझुनू पहले स्थान पर", "स्कूल शिक्षा विभाग की जनवरी 2026 की ज़िला एकेडमिक रैंकिंग में झुंझुनू ज़िला पहले स्थान पर रहा।")),
 dict(date="2026-11-14", tag={"en": "Season", "hi": "मौसम"}, src=("utsav.gov.in", "https://utsav.gov.in/view-event/shekhawati-festival"), link="events/",
   en=("Tourist season is on in Shekhawati", "Winter is the busiest time for heritage visits. The annual Shekhawati Festival's 2027 dates haven't been announced yet. We'll post them on our Events page."),
   hi=("शेखावाटी में पर्यटन का मौसम शुरू", "सर्दियों में हवेलियाँ देखने सबसे ज़्यादा लोग आते हैं। वार्षिक शेखावाटी महोत्सव की 2027 की तारीख़ें अभी घोषित नहीं हुई हैं। घोषणा होते ही हम इवेंट्स पेज पर डालेंगे।")),
]

GOV = [
 dict(name="SSO Rajasthan", url="https://sso.rajasthan.gov.in/", en="One login for most state services: recruitment, e-Mitra, Jan Aadhaar and more.", hi="ज़्यादातर राज्य सेवाओं के लिए एक लॉगिन: भर्ती, ई-मित्र, जन आधार और बहुत कुछ।"),
 dict(name="e-Mitra", url="https://emitra.rajasthan.gov.in/", en="Certificates (income, domicile, caste), bill payments and applications, online or at a kiosk.", hi="प्रमाण पत्र (आय, मूल निवास, जाति), बिल भुगतान और आवेदन, ऑनलाइन या कियोस्क पर।"),
 dict(name="Jan Aadhaar", url="https://janaadhaar.rajasthan.gov.in/", en="Rajasthan's family ID: enrolment, updates, status and e-card download.", hi="राजस्थान का पारिवारिक पहचान पत्र: नामांकन, अपडेट, स्टेटस और ई-कार्ड डाउनलोड।"),
 dict(name="Rajasthan Sampark (181)", url="https://sampark.rajasthan.gov.in/", tel="181", en="File and track a complaint about any state government service. Toll-free helpline 181.", hi="किसी भी राज्य सरकारी सेवा की शिकायत दर्ज करें और ट्रैक करें। टोल-फ़्री हेल्पलाइन 181।"),
 dict(name="Apna Khata (land records)", url="https://apnakhata.rajasthan.gov.in/", en="Jamabandi copies, mutation status and land-record applications.", hi="जमाबंदी नक़ल, नामांतरण स्टेटस और भूमि रिकॉर्ड से जुड़े आवेदन।"),
 dict(name="Jan Soochna Portal", url="https://jansoochna.rajasthan.gov.in/", en="Public information on government schemes and beneficiaries.", hi="सरकारी योजनाओं और लाभार्थियों की सार्वजनिक जानकारी।"),
 dict(name="Jhunjhunu district website", url="https://jhunjhunu.rajasthan.gov.in/", en="Official notices, offices and contacts of the district administration.", hi="ज़िला प्रशासन की आधिकारिक सूचनाएँ, दफ़्तर और संपर्क।"),
]

P = {
 "en": dict(
   eyebrow="Your City. Connected.", h1="Everything Jhunjhunu, in one place.",
   sub="Jobs, events, local businesses, places to visit, government services and helplines for Jhunjhunu district. Checked, and kept up to date.",
   search_ph="Search: jobs, Jan Aadhaar, Mandawa, 1930…", search_btn="Search",
   tiles=[("jobs", "Jobs", "Openings & resume bank"), ("events", "Events", "Fairs & festivals"), ("businesses", "Businesses", "Free local directory"), ("explore", "Explore", "Places to visit"),
          ("info", "Services & helplines", "e-Mitra, 181, 112, 1930"), ("facts", "Know Jhunjhunu", "History & achievers"), ("videos", "Videos", "Interviews & Reels"), ("help", "Need help?", "Ask us anything")],
   hl_h="Jhunjhunu highlights", hl_p="What's happening and worth knowing. Every item links to its source.",
   wx_h="Jhunjhunu weather", wx_loading="Loading weather…", wx_src="Source: Open-Meteo",
   fact_h="Know Jhunjhunu", fact_p="A new sourced fact about the district every day: history, heritage, and people who made Jhunjhunu proud.",
   jobs_h="Looking for work in Jhunjhunu?", jobs_p="Check official government vacancies, apply to local openings through us, or add your resume to our Jhunjhunu talent pool. We'll contact you when a matching job comes up.",
   jobs_b1="See jobs", jobs_b2="Add your resume",
   svc_h="How Jhunjhunu Blog can help", svc=[("Free business listing", "Get your business in front of local people.", "businesses"), ("Post a job, free", "Hiring? We'll share it after a quick check.", "jobs"),
          ("Resume bank", "Leave your resume with us for future openings.", "jobs"), ("List your event", "Fairs, camps, launches, community events.", "events"),
          ("Ask for help", "Don't know where to go? Ask us and we'll point you the right way.", "help"), ("Advertise", "Reach Jhunjhunu with clearly labelled campaigns.", "advertise")],
   vid_h="Watch: Jhunjhunu Blog videos", vid_p="Interviews with the people of Jhunjhunu (JHUNJHUNU TALKS), short Reels and daily updates on Instagram and Facebook.", vid_b="Go to Videos",
   # videos page
   v_title="Videos & Interviews", v_desc="JHUNJHUNU TALKS interviews, Reels and Shorts from Jhunjhunu Blog on YouTube, Instagram and Facebook.",
   v_lead="Alongside the website, Jhunjhunu Blog makes videos: long-form interviews, short Reels and daily posts about the district.",
   v_talks_h="JHUNJHUNU TALKS: interviews", v_talks_p="Long-form conversations with the people of Jhunjhunu. The first episodes are in production and will appear here, and on YouTube, once published.",
   v_reels_h="Reels & daily posts", v_reels_p="Short videos and daily Jhunjhunu facts on Instagram.", v_fb_h="Facebook", v_fb_p="Updates and clips for our Facebook community. Link coming soon.",
   v_yt_h="YouTube", v_yt_p="Full interviews will be published on YouTube. Channel link coming soon.",
   # facts page
   f_title="Know Jhunjhunu", f_desc="Sourced facts about Jhunjhunu district: history, Shekhawati heritage, industrialists and people who made Jhunjhunu proud.",
   f_lead="Facts about Jhunjhunu district, each with its source. New ones are added every day.", f_src="Source", all="All",
   # help page
   h_title="Need help?", h_desc="Ask Jhunjhunu Blog anything about Jhunjhunu: where to go, who to call, how to get something done.",
   h_lead="Don't know which office to visit, which form to fill, or who to call in Jhunjhunu? Ask us. We'll point you to the right official source or person.",
   h_note="We're not a government office, so we can't process applications or complaints ourselves. For official complaints, use Rajasthan Sampark (181).",
   h_q="Common questions", h_btn="Ask your question",
   apply_flow="How applying through Jhunjhunu Blog works", apply_steps=["We check every local job with the employer before listing it.", "You apply through the listing. We pass your details only to that employer.", "The employer contacts shortlisted candidates directly. We never charge job seekers."],
   rb_h="Jhunjhunu talent pool (resume bank)", rb_p="No matching job right now? Add your resume. When a local employer asks us for candidates that fit your profile, we'll contact you first, and we'll share your resume only after you agree.",
   rb_btn="Add your resume", services_h="Government services online", help_h="Emergency & helplines"),
 "hi": dict(
   eyebrow="आपका शहर, जुड़ा हुआ।", h1="झुंझुनू की हर ज़रूरी जानकारी, एक जगह।",
   sub="झुंझुनू ज़िले की नौकरियाँ, कार्यक्रम, स्थानीय कारोबार, घूमने की जगहें, सरकारी सेवाएँ और हेल्पलाइन। जाँची हुई और अपडेटेड।",
   search_ph="खोजें: नौकरी, जन आधार, मंडावा, 1930…", search_btn="खोजें",
   tiles=[("jobs", "नौकरी", "रिक्तियाँ और रिज़्यूमे बैंक"), ("events", "कार्यक्रम", "मेले और त्योहार"), ("businesses", "कारोबार", "मुफ़्त स्थानीय डायरेक्टरी"), ("explore", "घूमिए", "देखने लायक जगहें"),
          ("info", "सेवाएँ और हेल्पलाइन", "ई-मित्र, 181, 112, 1930"), ("facts", "जानिए झुंझुनू", "इतिहास और गौरव"), ("videos", "वीडियो", "इंटरव्यू और रील्स"), ("help", "मदद चाहिए?", "हमसे पूछिए")],
   hl_h="झुंझुनू हाइलाइट्स", hl_p="क्या चल रहा है और क्या जानना ज़रूरी है। हर ख़बर के साथ उसका स्रोत।",
   wx_h="झुंझुनू का मौसम", wx_loading="मौसम लोड हो रहा है…", wx_src="स्रोत: Open-Meteo",
   fact_h="जानिए झुंझुनू", fact_p="हर दिन ज़िले के बारे में एक नया तथ्य, स्रोत के साथ: इतिहास, विरासत और झुंझुनू का नाम रोशन करने वाले लोग।",
   jobs_h="झुंझुनू में काम ढूँढ रहे हैं?", jobs_p="सरकारी रिक्तियाँ आधिकारिक साइटों पर देखें, स्थानीय नौकरियों में हमारे ज़रिए आवेदन करें, या हमारे झुंझुनू टैलेंट पूल में अपना रिज़्यूमे जोड़ें। आपके लायक नौकरी आते ही हम आपसे संपर्क करेंगे।",
   jobs_b1="नौकरियाँ देखें", jobs_b2="रिज़्यूमे जोड़ें",
   svc_h="झुंझुनू ब्लॉग आपकी कैसे मदद करता है", svc=[("मुफ़्त बिज़नेस लिस्टिंग", "अपने कारोबार को स्थानीय लोगों तक पहुँचाइए।", "businesses"), ("नौकरी पोस्ट करें, मुफ़्त", "भर्ती कर रहे हैं? जाँच के बाद हम इसे शेयर करेंगे।", "jobs"),
          ("रिज़्यूमे बैंक", "आगे आने वाली नौकरियों के लिए अपना रिज़्यूमे हमारे पास छोड़िए।", "jobs"), ("अपना कार्यक्रम लिस्ट करें", "मेले, कैंप, लॉन्च, सामुदायिक कार्यक्रम।", "events"),
          ("मदद माँगिए", "पता नहीं कहाँ जाना है? हमसे पूछिए, हम सही रास्ता बताएँगे।", "help"), ("विज्ञापन", "साफ़ लेबल वाले कैंपेन से झुंझुनू तक पहुँचिए।", "advertise")],
   vid_h="देखिए: झुंझुनू ब्लॉग के वीडियो", vid_p="झुंझुनू के लोगों के साथ इंटरव्यू (झुंझुनू टॉक्स), छोटी रील्स और Instagram व Facebook पर रोज़ की अपडेट्स।", vid_b="वीडियो सेक्शन देखें",
   v_title="वीडियो और इंटरव्यू", v_desc="झुंझुनू ब्लॉग के झुंझुनू टॉक्स इंटरव्यू, रील्स और शॉर्ट्स, YouTube, Instagram और Facebook पर।",
   v_lead="वेबसाइट के साथ-साथ झुंझुनू ब्लॉग वीडियो भी बनाता है: लंबे इंटरव्यू, छोटी रील्स और ज़िले पर रोज़ की पोस्ट।",
   v_talks_h="झुंझुनू टॉक्स: इंटरव्यू", v_talks_p="झुंझुनू के लोगों के साथ लंबी बातचीत। पहले एपिसोड तैयार हो रहे हैं, प्रकाशित होते ही यहाँ और YouTube पर दिखेंगे।",
   v_reels_h="रील्स और रोज़ की पोस्ट", v_reels_p="Instagram पर छोटे वीडियो और झुंझुनू के रोज़ के तथ्य।", v_fb_h="Facebook", v_fb_p="हमारी Facebook कम्युनिटी के लिए अपडेट्स और क्लिप्स। लिंक जल्द।",
   v_yt_h="YouTube", v_yt_p="पूरे इंटरव्यू YouTube पर प्रकाशित होंगे। चैनल लिंक जल्द।",
   f_title="जानिए झुंझुनू", f_desc="झुंझुनू ज़िले के बारे में स्रोत सहित तथ्य: इतिहास, शेखावाटी विरासत, उद्योगपति और झुंझुनू का गौरव।",
   f_lead="झुंझुनू ज़िले के बारे में तथ्य, हर एक के साथ उसका स्रोत। हर दिन नए तथ्य जुड़ते हैं।", f_src="स्रोत", all="सभी",
   h_title="मदद चाहिए?", h_desc="झुंझुनू के बारे में झुंझुनू ब्लॉग से कुछ भी पूछिए: कहाँ जाना है, किसे कॉल करना है, काम कैसे होगा।",
   h_lead="पता नहीं झुंझुनू में किस दफ़्तर जाना है, कौन-सा फ़ॉर्म भरना है, या किसे कॉल करना है? हमसे पूछिए। हम आपको सही आधिकारिक स्रोत या व्यक्ति तक पहुँचाएँगे।",
   h_note="हम सरकारी दफ़्तर नहीं हैं, इसलिए आवेदन या शिकायत ख़ुद प्रोसेस नहीं कर सकते। आधिकारिक शिकायत के लिए राजस्थान संपर्क (181) का इस्तेमाल करें।",
   h_q="आम सवाल", h_btn="अपना सवाल पूछिए",
   apply_flow="झुंझुनू ब्लॉग के ज़रिए आवेदन कैसे होता है", apply_steps=["हर स्थानीय नौकरी को लिस्ट करने से पहले हम नियोक्ता से पुष्टि करते हैं।", "आप लिस्टिंग के ज़रिए आवेदन करते हैं। आपकी जानकारी सिर्फ़ उसी नियोक्ता को दी जाती है।", "नियोक्ता चुने गए उम्मीदवारों से सीधे संपर्क करता है। नौकरी ढूँढने वालों से हम कभी पैसे नहीं लेते।"],
   rb_h="झुंझुनू टैलेंट पूल (रिज़्यूमे बैंक)", rb_p="अभी आपके लायक नौकरी नहीं है? अपना रिज़्यूमे जोड़िए। जब कोई स्थानीय नियोक्ता आपकी प्रोफ़ाइल जैसे उम्मीदवार माँगेगा, हम पहले आपसे संपर्क करेंगे, और आपकी सहमति के बाद ही रिज़्यूमे साझा करेंगे।",
   rb_btn="रिज़्यूमे जोड़ें", services_h="ऑनलाइन सरकारी सेवाएँ", help_h="आपातकालीन और हेल्पलाइन"),
}

FAQ = {
 "en": [("How do I make a Jan Aadhaar card or update it?", "Use the Jan Aadhaar portal or any e-Mitra kiosk.", "https://janaadhaar.rajasthan.gov.in/"),
        ("Where do I get an income or domicile certificate?", "Apply on e-Mitra (online with your SSO ID) or at an e-Mitra kiosk.", "https://emitra.rajasthan.gov.in/"),
        ("A government office isn't responding to my problem.", "File a complaint on Rajasthan Sampark or call 181. You'll get a number to track it.", "https://sampark.rajasthan.gov.in/"),
        ("How do I check my land record (jamabandi)?", "Use Apna Khata, the state's land-records portal.", "https://apnakhata.rajasthan.gov.in/"),
        ("I lost money to an online fraud.", "Call 1930 immediately, or report at cybercrime.gov.in.", "info/1930-cyber-fraud-helpline/")],
 "hi": [("जन आधार कार्ड कैसे बनवाएँ या अपडेट करें?", "जन आधार पोर्टल या किसी भी ई-मित्र कियोस्क से।", "https://janaadhaar.rajasthan.gov.in/"),
        ("आय या मूल निवास प्रमाण पत्र कहाँ बनेगा?", "ई-मित्र पर (SSO ID से ऑनलाइन) या ई-मित्र कियोस्क पर आवेदन करें।", "https://emitra.rajasthan.gov.in/"),
        ("सरकारी दफ़्तर में मेरी समस्या पर सुनवाई नहीं हो रही।", "राजस्थान संपर्क पर शिकायत दर्ज करें या 181 पर कॉल करें। ट्रैक करने के लिए नंबर मिलेगा।", "https://sampark.rajasthan.gov.in/"),
        ("अपनी ज़मीन की जमाबंदी कैसे देखें?", "राज्य के भूमि रिकॉर्ड पोर्टल 'अपना खाता' पर।", "https://apnakhata.rajasthan.gov.in/"),
        ("ऑनलाइन धोखाधड़ी में पैसे चले गए।", "तुरंत 1930 पर कॉल करें, या cybercrime.gov.in पर शिकायत करें।", "info/1930-cyber-fraud-helpline/")],
}

TILE_ICON = {"jobs": "💼", "events": "📅", "businesses": "🏪", "explore": "🏰", "info": "☎️", "facts": "📜", "videos": "🎥", "help": "🙋"}

def form_or_dm(key, IG_DM):
    return FORMS.get(key) or IG_DM

def fact_card(lang, f):
    cat = FACT_CAT.get(f["cat"], (f["cat"], f["cat"]))[0 if lang == "en" else 1]
    return f'''<article class="card fact-card"><div class="card-top"><span class="card-cat">{e(cat)}</span></div><p class="fact-big">{e(f["big"])}</p>
<h3 class="card-title" lang="hi">{e(f["headline"])}</h3><p class="card-text" lang="hi">{e(f["body"])}</p><p class="small muted">{e(P[lang]["f_src"])}: {e(f["source"])}</p></article>'''

def home(lang, T, IG, IG_DM, explore_cards, info_cards):
    p, t = P[lang], T[lang]
    tiles = "".join(f'<li><a href="{k if k!="help" else "help"}/"><span class="tile-ic" aria-hidden="true">{TILE_ICON[k]}</span><span class="tile-t">{e(n)}</span><span class="tile-s">{e(s)}</span></a></li>' for k, n, s in p["tiles"])
    hls = sorted(HIGHLIGHTS, key=lambda h: h["date"], reverse=True)
    hl = "".join(f'''<article class="card hl-card"><div class="card-top"><span class="card-cat">{e(h["tag"][lang])}</span><span class="hl-date">{e(h["date"])}</span></div>
<h3 class="card-title">{e(h[lang][0])}</h3><p class="card-text">{e(h[lang][1])}</p><p class="small muted">{e(P[lang]["f_src"])}: <a href="{h["src"][1]}" target="_blank" rel="noopener">{e(h["src"][0])}</a></p></article>''' for h in hls)
    fs = facts()[:3]
    fcards = "".join(fact_card(lang, f) for f in fs)
    svc = "".join(f'<li><a href="{k}/"><strong>{e(a)}</strong><span>{e(b)}</span></a></li>' for a, b, k in p["svc"])
    IGsvg = '<svg class="icon icon-sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5Zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7Zm5 3.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9Zm0 2a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5ZM17.5 5.8a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"/></svg>'
    return f'''<section class="hero portal-hero"><div class="wrap">
  <p class="eyebrow">{e(p["eyebrow"])}</p><h1>{e(p["h1"])}</h1><p class="hero-sub">{e(p["sub"])}</p>
  <form class="site-search" role="search" action="search/" method="get"><label class="sr-only" for="q">{e(p["search_btn"])}</label>
    <input id="q" name="q" type="search" placeholder="{e(p["search_ph"])}" autocomplete="off"><button class="btn btn-primary" type="submit">{e(p["search_btn"])}</button></form>
  <ul class="tiles">{tiles}</ul></div></section>
<section class="band"><div class="wrap hl-wrap">
  <div><div class="section-head"><div><h2>{e(p["hl_h"])}</h2><p class="muted">{e(p["hl_p"])}</p></div></div><div class="grid grid-2">{hl}</div></div>
  <aside class="wx card" data-wx data-lang="{lang}"><h2 class="wx-h">{e(p["wx_h"])}</h2><div class="wx-body"><p class="muted">{e(p["wx_loading"])}</p></div><p class="small muted">{e(p["wx_src"])}</p></aside>
</div></section>
<section class="band band-tint"><div class="wrap"><div class="section-head"><div><h2>{e(p["fact_h"])}</h2><p class="muted">{e(p["fact_p"])}</p></div><a class="link-more" href="facts/">{e(P[lang]["all"])} <span aria-hidden="true">→</span></a></div><div class="grid grid-3">{fcards}</div></div></section>
<section class="band"><div class="wrap jobs-band"><div><h2>{e(p["jobs_h"])}</h2><p>{e(p["jobs_p"])}</p></div>
  <div class="btn-row"><a class="btn btn-primary" href="jobs/">{e(p["jobs_b1"])}</a><a class="btn btn-ghost" href="jobs/#resume-bank">{e(p["jobs_b2"])}</a></div></div></section>
{explore_cards}
<section class="band band-essentials"><div class="wrap"><div class="section-head"><div><h2>{e(t["info"])}</h2></div><a class="link-more" href="info/">{e(P[lang]["all"])} <span aria-hidden="true">→</span></a></div><div class="essentials">{info_cards}</div></div></section>
<section class="band band-tint"><div class="wrap"><h2>{e(p["svc_h"])}</h2><ul class="svc-list">{svc}</ul></div></section>
<section class="band"><div class="wrap"><div class="show-card"><h2>{e(p["vid_h"])}</h2><p>{e(p["vid_p"])}</p>
  <div class="btn-row"><a class="btn btn-gold" href="videos/">{e(p["vid_b"])} →</a><a class="btn btn-ghost btn-on-dark" href="{IG}" target="_blank" rel="noopener">{IGsvg} Instagram</a></div></div></div></section>
<script src="../js/portal.js" defer></script>'''

def build_portal(lang, page, T, IG, IG_DM, BASE, info_list, DIST):
    p = P[lang]
    # Videos
    page(lang, "videos", p["v_title"], p["v_desc"], f'''<div class="wrap page"><h1>{e(p["v_title"])}</h1><p class="lead detail-narrow">{e(p["v_lead"])}</p>
<div class="grid grid-2">
<article class="card"><h2 class="card-title">{e(p["v_talks_h"])}</h2><p class="card-text">{e(p["v_talks_p"])}</p><div class="empty"><p class="muted">{"Episodes coming soon." if lang=="en" else "एपिसोड जल्द।"}</p></div></article>
<article class="card"><h2 class="card-title">{e(p["v_reels_h"])}</h2><p class="card-text">{e(p["v_reels_p"])}</p><a class="btn btn-primary btn-small" href="{IG}" target="_blank" rel="noopener">Instagram @jhunjhunu_blog ↗</a></article>
<article class="card"><h2 class="card-title">{e(p["v_yt_h"])}</h2><p class="card-text">{e(p["v_yt_p"])}</p></article>
<article class="card"><h2 class="card-title">{e(p["v_fb_h"])}</h2><p class="card-text">{e(p["v_fb_p"])}</p></article>
</div></div>''', crumbs=[])
    # Facts archive with category filter (no JS needed: anchors per category)
    fs = facts()
    cats = []
    for f in fs:
        c = FACT_CAT.get(f["cat"], (f["cat"], f["cat"]))[0 if lang == "en" else 1]
        if c not in cats: cats.append(c)
    chips = f'<li><button class="chip is-on" data-filter="">{e(p["all"])}</button></li>' + "".join(f'<li><button class="chip" data-filter="{e(c)}">{e(c)}</button></li>' for c in cats)
    cards = "".join(fact_card(lang, f).replace('<article class="card fact-card">', f'<article class="card fact-card" data-cat="{e(FACT_CAT.get(f["cat"], (f["cat"], f["cat"]))[0 if lang=="en" else 1])}">') for f in fs)
    page(lang, "facts", p["f_title"], p["f_desc"], f'''<div class="wrap page"><h1>{e(p["f_title"])}</h1><p class="lead detail-narrow">{e(p["f_lead"])}</p>
<ul class="chips fact-filter">{chips}</ul><div class="grid grid-3 fact-grid">{cards}</div></div><script src="../../js/portal.js" defer></script>''', crumbs=[])
    # Help
    faq = "".join(f'<details class="faq"><summary>{e(q)}</summary><p>{e(a)} <a href="{("../" + u) if not u.startswith("http") else u}"{"" if not u.startswith("http") else " target=\"_blank\" rel=\"noopener\""}>{"Open ↗" if lang=="en" else "खोलें ↗"}</a></p></details>' for q, a, u in FAQ[lang])
    page(lang, "help", p["h_title"], p["h_desc"], f'''<div class="wrap page detail-narrow"><h1>{e(p["h_title"])}</h1><p class="lead">{e(p["h_lead"])}</p>
<a class="btn btn-primary" href="{form_or_dm("help", IG_DM)}" target="_blank" rel="noopener">{e(p["h_btn"])}</a><p class="notice notice-info">{e(p["h_note"])}</p>
<h2>{e(p["h_q"])}</h2>{faq}</div>''', crumbs=[])
    # Search page (client-side)
    page(lang, "search", p["search_btn"], p["search_ph"], f'''<div class="wrap page detail-narrow"><h1>{e(p["search_btn"])}</h1>
<form class="site-search" role="search" action="./" method="get"><input id="q" name="q" type="search" placeholder="{e(p["search_ph"])}"><button class="btn btn-primary" type="submit">{e(p["search_btn"])}</button></form>
<ol class="search-results" data-search data-lang="{lang}"></ol></div><script src="../../js/portal.js" defer></script>''', crumbs=[])

def gov_cards(lang, T):
    out = []
    for g in GOV:
        tel = f'<a class="btn btn-primary btn-small" href="tel:{g["tel"]}">{g["tel"]}</a>' if g.get("tel") else ""
        out.append(f'''<article class="info-item info-compact"><div class="info-main"><h3 class="card-title"><a href="{g["url"]}" target="_blank" rel="noopener">{e(g["name"])}</a></h3><p class="row-meta">{e(g[lang])}</p></div>
<div class="info-actions">{tel}<a class="btn btn-ghost btn-small" href="{g["url"]}" target="_blank" rel="noopener">{e(T[lang]["official"])}</a></div></article>''')
    return "".join(out)

def search_index(DIST, BASE):
    import re
    idx = {"hi": [], "en": []}
    for lang in idx:
        for root, _, files in os.walk(os.path.join(DIST, lang)):
            if "index.html" not in files: continue
            s = open(os.path.join(root, "index.html")).read()
            title = re.search(r"<title>(.*?)</title>", s).group(1)
            desc = re.search(r'name="description" content="(.*?)"', s)
            main = s[s.find("<main"): s.find("</main>")]
            text = re.sub(r"<[^>]+>", " ", main); text = re.sub(r"\s+", " ", html.unescape(text))[:1500]
            rel = os.path.relpath(root, os.path.join(DIST, lang)).replace(os.sep, "/")
            if rel in ("search",): continue
            idx[lang].append({"u": "" if rel == "." else rel + "/", "t": html.unescape(title.split(" | ")[0]), "d": html.unescape(desc.group(1)) if desc else "", "x": text})
    os.makedirs(os.path.join(DIST, "js"), exist_ok=True)
    json.dump(idx, open(os.path.join(DIST, "js", "search-index.json"), "w"), ensure_ascii=False)
