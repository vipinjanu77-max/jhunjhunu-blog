"""Content + builders for Explore, Jobs, Events, Businesses, Advertise. Imported by build.py."""
import html
e = html.escape
CHECKED2 = {"en": "14 Nov 2026", "hi": "14 नवं॰ 2026"}

S = {
 "en": dict(explore="Explore Jhunjhunu", jobs="Jobs & Opportunities", events="Events", businesses="Businesses", advertise="Advertise with us",
   checked="Last checked", sources="Sources", visit_note="Timings and entry fees aren't listed because we haven't confirmed them yet. Check locally before you go.",
   official="Official site ↗", msg="Message us on Instagram", view="Read guide"),
 "hi": dict(explore="झुंझुनू घूमिए", jobs="नौकरी और अवसर", events="कार्यक्रम", businesses="कारोबार", advertise="हमारे साथ विज्ञापन",
   checked="अंतिम जाँच", sources="स्रोत", visit_note="समय और प्रवेश शुल्क यहाँ नहीं दिए गए हैं क्योंकि हमने उन्हें अभी पक्का नहीं किया है। जाने से पहले स्थानीय रूप से पता कर लें।",
   official="आधिकारिक साइट ↗", msg="Instagram पर मैसेज करें", view="गाइड पढ़ें"),
}

# ------------------------------------------------------------------ Explore
PLACES = [
 dict(slug="rani-sati-temple", area={"en": "Jhunjhunu city", "hi": "झुंझुनू शहर"}, cat={"en": "Temple", "hi": "मंदिर"},
   src=[("rajras.in", "https://rajras.in/ras/pre/rajasthan/districts/jhunjhunu/")],
   en=dict(name="Rani Sati Temple", short="Jhunjhunu's best-known temple and one of Rajasthan's major pilgrimage sites.",
     body="<p>The Rani Sati Dadi temple in Jhunjhunu city draws devotees from across India and from Marwari families around the world. It is the reason many visitors first come to Jhunjhunu.</p><p>The temple's annual fair, the Rani Sati Mela, is held on Bhadrapada Amavasya (the no-moon day of the Hindu month of Bhado) and brings large crowds to the city.</p>"),
   hi=dict(name="रानी सती मंदिर", short="झुंझुनू का सबसे प्रसिद्ध मंदिर और राजस्थान के बड़े तीर्थ स्थलों में से एक।",
     body="<p>झुंझुनू शहर का रानी सती दादी मंदिर पूरे भारत से और दुनिया भर में बसे मारवाड़ी परिवारों से श्रद्धालुओं को खींचता है। बहुत-से लोग पहली बार झुंझुनू इसी मंदिर की वजह से आते हैं।</p><p>मंदिर का वार्षिक मेला, रानी सती मेला, भादो अमावस्या को लगता है और इस दौरान शहर में भारी भीड़ रहती है।</p>")),
 dict(slug="khetri-mahal", area={"en": "Jhunjhunu city", "hi": "झुंझुनू शहर"}, cat={"en": "Heritage", "hi": "विरासत"},
   src=[("Wikivoyage: Jhunjhunu", "https://en.wikivoyage.org/wiki/Jhunjhunu")],
   en=dict(name="Khetri Mahal", short="An 18th-century 'wind palace' of open, pillared halls in Jhunjhunu's old town.",
     body="<p>Khetri Mahal, in the Kajiwada area of Jhunjhunu's old town, is known as the 'wind palace' for its open halls and pillars that let air move through the building.</p><p>It is often said to have inspired Jaipur's Hawa Mahal, built in 1799. Sources give different dates for Khetri Mahal itself, so we describe it simply as 18th century.</p>"),
   hi=dict(name="खेतड़ी महल", short="झुंझुनू के पुराने शहर में 18वीं सदी का खुले, खंभों वाले हॉल वाला 'हवा महल'।",
     body="<p>झुंझुनू के पुराने शहर के काज़ीवाड़ा इलाक़े में स्थित खेतड़ी महल अपने खुले हॉल और खंभों के कारण 'हवा महल' कहलाता है, जिनसे पूरी इमारत में हवा आती-जाती रहती है।</p><p>अक्सर कहा जाता है कि इसी से प्रेरित होकर जयपुर का हवा महल (1799) बनाया गया। खेतड़ी महल के निर्माण के साल को लेकर स्रोतों में अलग-अलग तारीख़ें हैं, इसलिए हम इसे सिर्फ़ 18वीं सदी का बता रहे हैं।</p>")),
 dict(slug="mandawa", area={"en": "Mandawa", "hi": "मंडावा"}, cat={"en": "Painted havelis", "hi": "चित्रित हवेलियाँ"},
   src=[("Wikipedia: Jhunjhunu district", "https://en.wikipedia.org/wiki/Jhunjhunu_district")],
   en=dict(name="Mandawa's painted havelis", short="A heritage town of fresco-covered merchant mansions, and a favourite film location.",
     body="<p>Mandawa is one of the best-known towns of Shekhawati, often called the 'open-air art gallery of Rajasthan'. Its streets are lined with havelis (merchant mansions) decorated with frescoes, built by trading families in the 19th and early 20th centuries.</p><p>The town's look has made it a popular film shooting location.</p>"),
   hi=dict(name="मंडावा की चित्रित हवेलियाँ", short="भित्तिचित्रों से सजी व्यापारी हवेलियों वाला विरासत क़स्बा, और फ़िल्मों की पसंदीदा लोकेशन।",
     body="<p>मंडावा शेखावाटी के सबसे जाने-माने क़स्बों में से है। शेखावाटी को अक्सर 'राजस्थान की खुली आर्ट गैलरी' कहा जाता है। यहाँ की गलियों में व्यापारी परिवारों की बनवाई भित्तिचित्रों से सजी हवेलियाँ हैं, जो 19वीं और 20वीं सदी की शुरुआत में बनीं।</p><p>अपनी इसी बनावट की वजह से यह क़स्बा फ़िल्मों की शूटिंग के लिए लोकप्रिय है।</p>")),
 dict(slug="nawalgarh", area={"en": "Nawalgarh", "hi": "नवलगढ़"}, cat={"en": "Painted havelis", "hi": "चित्रित हवेलियाँ"},
   src=[("Utsav (Govt of India): Shekhawati Festival", "https://utsav.gov.in/view-event/shekhawati-festival")],
   en=dict(name="Nawalgarh", short="A Shekhawati town known for its havelis, including a haveli museum.",
     body="<p>Nawalgarh is one of the main haveli towns of Shekhawati, with many painted merchant mansions. The Dr. Ramnath A. Podar Haveli Museum is among its best-known stops.</p><p>Nawalgarh has also hosted the Shekhawati Festival, organised by Rajasthan Tourism.</p>"),
   hi=dict(name="नवलगढ़", short="अपनी हवेलियों के लिए मशहूर शेखावाटी का क़स्बा, जहाँ एक हवेली संग्रहालय भी है।",
     body="<p>नवलगढ़ शेखावाटी के प्रमुख हवेली क़स्बों में से है, जहाँ कई चित्रित व्यापारी हवेलियाँ हैं। डॉ. रामनाथ ए. पोद्दार हवेली संग्रहालय यहाँ की सबसे जानी-मानी जगहों में है।</p><p>नवलगढ़ में राजस्थान पर्यटन द्वारा आयोजित शेखावाटी महोत्सव भी हो चुका है।</p>")),
 dict(slug="lohargal", area={"en": "Udaipurwati tehsil", "hi": "उदयपुरवाटी तहसील"}, cat={"en": "Pilgrimage", "hi": "तीर्थ"},
   src=[("Utsav (Govt of India): World Tourism Day, Jhunjhunu", "https://utsav.gov.in/view-event/world-tourism-day-2025-10"), ("IGNCA / ASI record: Panch Pandav Dham, Lohargal", "https://ignca.gov.in/asi_reports/rjjjn_1805.pdf")],
   en=dict(name="Lohargal Dham", short="A pilgrimage site in the Aravalli hills, and the district's 'Panch Gaurav' tourist place.",
     body="<p>Lohargal is a pilgrimage site in the Aravalli hills, about 68 km from Jhunjhunu. Its temples include the Panch Pandav Dham.</p><p>Rajasthan Tourism lists Lohargal Dham as Jhunjhunu district's tourist place under the state's 'Panch Gaurav' programme, which picks one tourist spot (along with a crop, product, plant species and sport) to promote in each district.</p>"),
   hi=dict(name="लोहार्गल धाम", short="अरावली की पहाड़ियों में तीर्थ स्थल, और ज़िले का 'पंच गौरव' पर्यटन स्थल।",
     body="<p>लोहार्गल अरावली की पहाड़ियों में बसा तीर्थ स्थल है, जो झुंझुनू से लगभग 68 किमी दूर है। यहाँ के मंदिरों में पंच पांडव धाम भी है।</p><p>राजस्थान पर्यटन विभाग लोहार्गल धाम को राज्य के 'पंच गौरव' कार्यक्रम के तहत झुंझुनू ज़िले का पर्यटन स्थल बताता है। इस कार्यक्रम में हर ज़िले से एक पर्यटन स्थल (और एक फ़सल, उत्पाद, वनस्पति प्रजाति और खेल) को बढ़ावा देने के लिए चुना गया है।</p>")),
 dict(slug="dundlod-fort", area={"en": "Dundlod", "hi": "डूंडलोद"}, cat={"en": "Fort", "hi": "क़िला"},
   src=[("Outlook Traveller", "https://www.outlooktraveller.com/News/all-about-the-upcoming-singing-sands-festival-in-rajasthan")],
   en=dict(name="Dundlod Fort", short="An 18th-century fort, now a heritage hotel, that hosts a folk music festival.",
     body="<p>Dundlod Fort is an 18th-century fort in the Shekhawati region that has been turned into a heritage hotel.</p><p>It has been the venue for the Singing Sands folk music festival, which features folk artists from the region.</p>"),
   hi=dict(name="डूंडलोद क़िला", short="18वीं सदी का क़िला, जो अब हेरिटेज होटल है और जहाँ लोक संगीत महोत्सव होता है।",
     body="<p>डूंडलोद क़िला शेखावाटी क्षेत्र का 18वीं सदी का क़िला है, जिसे अब हेरिटेज होटल में बदल दिया गया है।</p><p>यहाँ 'सिंगिंग सैंड्स' लोक संगीत महोत्सव हो चुका है, जिसमें क्षेत्र के लोक कलाकार प्रस्तुति देते हैं।</p>")),
 dict(slug="mertani-baori", area={"en": "Jhunjhunu city", "hi": "झुंझुनू शहर"}, cat={"en": "Stepwell", "hi": "बावड़ी"},
   src=[("rajasthantour4u.com", "https://www.rajasthantour4u.com/jhunjhunu.html")],
   en=dict(name="Mertani Baori", short="A historic stepwell in Jhunjhunu, with flights of steps descending through arches.",
     body="<p>Mertani Baori is one of Jhunjhunu's historic stepwells, built to store the region's most precious resource: water. Flights of steps descend through arches to the water level.</p><p>It is a reminder of how towns in this dry region managed water before piped supply.</p>"),
   hi=dict(name="मेड़तनी बावड़ी", short="झुंझुनू की ऐतिहासिक बावड़ी, जिसमें मेहराबों से होकर नीचे उतरती सीढ़ियाँ हैं।",
     body="<p>मेड़तनी बावड़ी झुंझुनू की ऐतिहासिक बावड़ियों में से है, जो इस क्षेत्र के सबसे क़ीमती संसाधन, पानी, को सहेजने के लिए बनाई गई थी। मेहराबों से होकर सीढ़ियाँ नीचे पानी तक जाती हैं।</p><p>यह याद दिलाती है कि नल का पानी आने से पहले इस सूखे इलाक़े के क़स्बे पानी का प्रबंधन कैसे करते थे।</p>")),
]

# ------------------------------------------------------------------ Jobs
JOB_SOURCES = [
 dict(url="https://sso.rajasthan.gov.in/", name="SSO Rajasthan: Recruitment Portal",
   en="Almost every Rajasthan government job application goes through your SSO ID. Log in, open the Recruitment Portal and complete One-Time Registration (OTR) early.",
   hi="राजस्थान सरकार की लगभग हर नौकरी का आवेदन SSO ID से होता है। लॉग इन करें, रिक्रूटमेंट पोर्टल खोलें और वन-टाइम रजिस्ट्रेशन (OTR) पहले से पूरा कर लें।"),
 dict(url="https://rssb.rajasthan.gov.in/", name="RSSB: Rajasthan Staff Selection Board",
   en="State-level recruitment, including the Common Eligibility Test (CET), patwari, teacher and junior engineer posts.",
   hi="राज्य स्तर की भर्तियाँ, जिनमें सामान्य पात्रता परीक्षा (CET), पटवारी, शिक्षक और जूनियर इंजीनियर जैसे पद शामिल हैं।"),
 dict(url="https://rpsc.rajasthan.gov.in/", name="RPSC: Rajasthan Public Service Commission",
   en="RAS and other gazetted and senior posts. Official advertisements are on the commission's website.",
   hi="RAS और दूसरे राजपत्रित व वरिष्ठ पद। आधिकारिक विज्ञापन आयोग की वेबसाइट पर होते हैं।"),
 dict(url="https://joinindianarmy.nic.in/", name="Indian Army: Join Indian Army (Agniveer and officer entries)",
   en="Jhunjhunu has a long tradition of service in the armed forces. Army recruitment notices and registration are on this official site.",
   hi="झुंझुनू की सेना में सेवा की लंबी परंपरा है। सेना भर्ती की सूचनाएँ और रजिस्ट्रेशन इस आधिकारिक साइट पर होते हैं।"),
 dict(url="https://www.ssjhunjhunu.com/", name="Sainik School Jhunjhunu: Recruitment tab",
   en="The school posts its teaching and non-teaching vacancies, and their application forms, in the Recruitment section of its website.",
   hi="स्कूल अपनी शिक्षण और गैर-शिक्षण रिक्तियाँ और आवेदन फ़ॉर्म वेबसाइट के 'Recruitment' सेक्शन में डालता है।"),
 dict(url="https://www.ncs.gov.in/", name="National Career Service (Government of India)",
   en="A free central-government portal for private and government jobs, job fairs and career counselling.",
   hi="निजी और सरकारी नौकरियों, रोज़गार मेलों और करियर काउंसलिंग के लिए केंद्र सरकार का मुफ़्त पोर्टल।"),
]
JOBS = {
 "en": dict(title="Jobs & Opportunities", desc="Where to find genuine jobs for Jhunjhunu: official recruitment portals, local openings checked by us, and how to avoid job scams.",
   lead="We don't copy job listings from other websites. We point you to the official source, and we list local openings only after checking them with the employer.",
   off_h="Where to check government jobs", off_p="These are the official websites. Always read the official notification before applying, especially the last date and fee.",
   local_h="Local openings in Jhunjhunu", local_empty="No local openings listed yet.", local_p="Hiring in Jhunjhunu? Listing a job is free. Send us the role, pay range, location and how to apply. We'll call you to confirm before it goes up.",
   scam_h="Stay safe from job scams", scam=["Never pay anyone to get a job. Official application fees are paid only through the official portal.", "Check the web address. Rajasthan government sites end in .rajasthan.gov.in, and central ones in .gov.in or .nic.in.", "Ignore WhatsApp or Telegram messages promising a 'guaranteed' or 'direct' government job.", "If you've lost money to a job scam, call 1930 or report it at cybercrime.gov.in."],
   scam_link="1930: cyber fraud helpline"),
 "hi": dict(title="नौकरी और अवसर", desc="झुंझुनू के लिए असली नौकरियाँ कहाँ देखें: आधिकारिक भर्ती पोर्टल, हमारे द्वारा जाँची गई स्थानीय नौकरियाँ, और नौकरी के नाम पर धोखाधड़ी से कैसे बचें।",
   lead="हम दूसरी वेबसाइटों से नौकरियों की लिस्ट कॉपी नहीं करते। हम आपको आधिकारिक स्रोत तक पहुँचाते हैं, और स्थानीय नौकरियाँ नियोक्ता से पुष्टि करने के बाद ही डालते हैं।",
   off_h="सरकारी नौकरियाँ कहाँ देखें", off_p="ये आधिकारिक वेबसाइटें हैं। आवेदन से पहले आधिकारिक अधिसूचना ज़रूर पढ़ें, ख़ासकर अंतिम तिथि और फ़ीस।",
   local_h="झुंझुनू में स्थानीय नौकरियाँ", local_empty="अभी कोई स्थानीय नौकरी लिस्ट नहीं है।", local_p="झुंझुनू में भर्ती कर रहे हैं? नौकरी लिस्ट करना मुफ़्त है। पद, वेतन, जगह और आवेदन का तरीक़ा हमें भेजें। लिस्ट करने से पहले हम आपको फ़ोन करके पुष्टि करेंगे।",
   scam_h="नौकरी के नाम पर धोखाधड़ी से बचें", scam=["नौकरी पाने के लिए किसी को पैसे न दें। आधिकारिक आवेदन शुल्क सिर्फ़ आधिकारिक पोर्टल पर ही भरा जाता है।", "वेब पता जाँचें। राजस्थान सरकार की साइटें .rajasthan.gov.in पर, और केंद्र सरकार की .gov.in या .nic.in पर ख़त्म होती हैं।", "'पक्की' या 'सीधी' सरकारी नौकरी का वादा करने वाले WhatsApp या Telegram मैसेज को नज़रअंदाज़ करें।", "अगर नौकरी के नाम पर ठगी हुई है, तो 1930 पर कॉल करें या cybercrime.gov.in पर शिकायत करें।"],
   scam_link="1930: साइबर धोखाधड़ी हेल्पलाइन"),
}

# ------------------------------------------------------------------ Events
EVENTS = [
 dict(src=("utsav.gov.in", "https://utsav.gov.in/view-event/shekhawati-festival"),
   en=dict(name="Shekhawati Festival (Shekhawati Utsav)", when="Held every year. 2027 dates not yet announced.", where="Shekhawati region (Jhunjhunu, Sikar, Churu)",
     body="Organised by Rajasthan's Department of Tourism with the district administrations. Past editions have included heritage walks, folk performances, traditional rural games and Rajasthani food. Past dates have varied between February and March."),
   hi=dict(name="शेखावाटी महोत्सव (शेखावाटी उत्सव)", when="हर साल होता है। 2027 की तारीख़ें अभी घोषित नहीं हुई हैं।", where="शेखावाटी क्षेत्र (झुंझुनू, सीकर, चूरू)",
     body="राजस्थान पर्यटन विभाग और ज़िला प्रशासन द्वारा आयोजित। पिछले आयोजनों में हेरिटेज वॉक, लोक प्रस्तुतियाँ, पारंपरिक ग्रामीण खेल और राजस्थानी खान-पान शामिल रहे हैं। पिछली तारीख़ें फ़रवरी से मार्च के बीच रही हैं।")),
 dict(src=("rajras.in", "https://rajras.in/ras/pre/rajasthan/districts/jhunjhunu/"),
   en=dict(name="Rani Sati Mela", when="Every year on Bhadrapada Amavasya (usually August or September). The 2027 date follows the Hindu calendar.", where="Rani Sati Temple, Jhunjhunu city",
     body="The annual fair at the Rani Sati Dadi temple draws pilgrims from across India and abroad."),
   hi=dict(name="रानी सती मेला", when="हर साल भादो अमावस्या को (आमतौर पर अगस्त या सितंबर में)। 2027 की तारीख़ हिंदू पंचांग के अनुसार होगी।", where="रानी सती मंदिर, झुंझुनू शहर",
     body="रानी सती दादी मंदिर का वार्षिक मेला, जिसमें देश-विदेश से श्रद्धालु आते हैं।")),
]
EV = {
 "en": dict(title="Events", desc="Festivals, fairs and community events in Jhunjhunu district, and how to get your event listed.",
   lead="Festivals, fairs and community events in Jhunjhunu district. We list an event only after checking it with the organiser or an official source.",
   annual_h="Annual festivals and fairs", up_h="Upcoming local events", up_empty="No upcoming local events listed yet.",
   up_p="Organising something in Jhunjhunu district? Listing is free. Send us the event name, date, time, venue, entry fee (if any) and an organiser contact. We'll confirm with you before it goes up.",
   when="When", where="Where"),
 "hi": dict(title="कार्यक्रम", desc="झुंझुनू ज़िले के त्योहार, मेले और सामुदायिक कार्यक्रम, और अपना कार्यक्रम लिस्ट कैसे करवाएँ।",
   lead="झुंझुनू ज़िले के त्योहार, मेले और सामुदायिक कार्यक्रम। हम कोई कार्यक्रम आयोजक या आधिकारिक स्रोत से पुष्टि के बाद ही डालते हैं।",
   annual_h="वार्षिक त्योहार और मेले", up_h="आने वाले स्थानीय कार्यक्रम", up_empty="अभी कोई आने वाला स्थानीय कार्यक्रम लिस्ट नहीं है।",
   up_p="झुंझुनू ज़िले में कोई कार्यक्रम कर रहे हैं? लिस्ट करना मुफ़्त है। कार्यक्रम का नाम, तारीख़, समय, जगह, प्रवेश शुल्क (अगर हो) और आयोजक का संपर्क भेजें। डालने से पहले हम आपसे पुष्टि करेंगे।",
   when="कब", where="कहाँ"),
}

# ------------------------------------------------------------------ Businesses
BIZ_CATS = {"en": ["Restaurants & sweets", "Shops & local products", "Doctors, clinics & pharmacies", "Schools & coaching", "Hotels & stays", "Home services", "Construction & interiors", "Automotive", "Professional services", "Weddings & events"],
            "hi": ["रेस्टोरेंट और मिठाई", "दुकानें और स्थानीय उत्पाद", "डॉक्टर, क्लिनिक और फ़ार्मेसी", "स्कूल और कोचिंग", "होटल और ठहरने की जगह", "घरेलू सेवाएँ", "निर्माण और इंटीरियर", "ऑटोमोबाइल", "प्रोफ़ेशनल सेवाएँ", "शादी और कार्यक्रम"]}
BIZ = {
 "en": dict(title="Businesses", desc="A free directory of Jhunjhunu businesses, each one checked directly with the business before it's listed.",
   lead="A free directory of businesses across Jhunjhunu district. We add a business only after confirming its name, address and phone number directly with the owner.",
   cats_h="Categories we're building", empty="We're adding the first verified businesses now.",
   how_h="How listing works", how=["Listing is free, and always will be.", "We confirm your details by phone or a visit before your listing goes live.", "'Verified' can't be bought. Paying for promotion never adds or keeps a verified badge.", "Any paid placement is clearly marked 'Sponsored'."],
   cta_h="Get your business listed", cta_p="Send us your business name, category, area, address, phone number and opening hours."),
 "hi": dict(title="कारोबार", desc="झुंझुनू के कारोबारों की मुफ़्त डायरेक्टरी। हर कारोबार को लिस्ट करने से पहले सीधे उससे पुष्टि की जाती है।",
   lead="पूरे झुंझुनू ज़िले के कारोबारों की मुफ़्त डायरेक्टरी। हम किसी कारोबार का नाम, पता और फ़ोन नंबर मालिक से सीधे पक्का करने के बाद ही उसे जोड़ते हैं।",
   cats_h="कौन-सी श्रेणियाँ बन रही हैं", empty="हम पहले सत्यापित कारोबार अभी जोड़ रहे हैं।",
   how_h="लिस्टिंग कैसे होती है", how=["लिस्टिंग मुफ़्त है, और हमेशा रहेगी।", "लिस्टिंग लाइव होने से पहले हम फ़ोन या मुलाक़ात से आपकी जानकारी पक्की करते हैं।", "'सत्यापित' ख़रीदा नहीं जा सकता। प्रमोशन के लिए भुगतान करने से सत्यापित बैज नहीं मिलता।", "हर भुगतान वाली जगह पर साफ़ 'प्रायोजित' लिखा होता है।"],
   cta_h="अपना कारोबार लिस्ट करवाएँ", cta_p="हमें अपने कारोबार का नाम, श्रेणी, इलाक़ा, पता, फ़ोन नंबर और खुलने का समय भेजें।"),
}

# ------------------------------------------------------------------ Advertise
AD = {
 "en": dict(title="Advertise with us", desc="Ways for Jhunjhunu businesses and organisations to work with Jhunjhunu Blog, with clear labelling.",
   lead="Jhunjhunu Blog is building a local audience in Jhunjhunu district. If you want to reach the people of Jhunjhunu, here's how we can work together.",
   ways_h="Ways to work with us", ways=[("Sponsored episode", "Support an episode of JHUNJHUNU TALKS. Your brand is credited as sponsor. The guest and the questions stay our choice."), ("Business spotlight", "A clearly labelled feature on your business: its story, its people, what it offers."), ("Event partnership", "Coverage and promotion for your event in Jhunjhunu district."), ("Social media package", "Labelled posts and Reels across our Instagram and Facebook.")],
   rules_h="Our rules for paid content", rules=["Every paid piece is labelled 'Sponsored'.", "We don't publish claims we can't check, such as 'best in Jhunjhunu' or 'guaranteed results'.", "Paying doesn't buy a positive story, an interview or a 'verified' badge.", "We may decline work that doesn't fit our editorial standards."],
   cta_h="Talk to us", cta_p="We'll share packages and pricing after understanding what you need. Send us your business name and what you'd like to promote."),
 "hi": dict(title="हमारे साथ विज्ञापन", desc="झुंझुनू के कारोबारों और संस्थाओं के लिए झुंझुनू ब्लॉग के साथ काम करने के तरीक़े, साफ़ लेबल के साथ।",
   lead="झुंझुनू ब्लॉग झुंझुनू ज़िले में एक स्थानीय दर्शक वर्ग बना रहा है। अगर आप झुंझुनू के लोगों तक पहुँचना चाहते हैं, तो हम ऐसे साथ काम कर सकते हैं।",
   ways_h="साथ काम करने के तरीक़े", ways=[("प्रायोजित एपिसोड", "झुंझुनू टॉक्स के किसी एपिसोड को प्रायोजित करें। आपके ब्रांड को प्रायोजक के रूप में श्रेय मिलेगा। मेहमान और सवाल हम तय करेंगे।"), ("बिज़नेस स्पॉटलाइट", "आपके कारोबार पर साफ़ लेबल वाला फ़ीचर: उसकी कहानी, उसके लोग, और वह क्या देता है।"), ("इवेंट पार्टनरशिप", "झुंझुनू ज़िले में आपके कार्यक्रम की कवरेज और प्रमोशन।"), ("सोशल मीडिया पैकेज", "हमारे Instagram और Facebook पर लेबल वाली पोस्ट और रील्स।")],
   rules_h="भुगतान वाली सामग्री के हमारे नियम", rules=["हर भुगतान वाली सामग्री पर 'प्रायोजित' लिखा होता है।", "हम ऐसे दावे नहीं छापते जिनकी जाँच न हो सके, जैसे 'झुंझुनू में सबसे अच्छा' या 'पक्के नतीजे'।", "पैसे से अच्छी कहानी, इंटरव्यू या 'सत्यापित' बैज नहीं ख़रीदा जा सकता।", "जो काम हमारे संपादकीय मानकों पर खरा न उतरे, उसे हम मना कर सकते हैं।"],
   cta_h="हमसे बात करें", cta_p="आपकी ज़रूरत समझने के बाद हम पैकेज और क़ीमत बताएँगे। अपने कारोबार का नाम और आप क्या प्रमोट करना चाहते हैं, हमें भेजें।"),
}


def place_card(lang, p, href):
    c = p[lang]
    return f'''<article class="card place-card"><div class="card-top"><span class="card-cat">{e(p["cat"][lang])}</span></div>
<h3 class="card-title"><a href="{href}">{e(c["name"])}</a></h3><p class="card-text">{e(c["short"])}</p><div class="card-foot"><span class="scope">{e(p["area"][lang])}</span></div></article>'''


def build_sections(lang, page, IG, IG_DM, BASE):
    s = S[lang]
    msg_btn = f'<a class="btn btn-primary" href="{IG_DM}" target="_blank" rel="noopener">{e(s["msg"])}</a>'
    # Explore list + places
    cards = "".join(place_card(lang, p, f'{p["slug"]}/') for p in PLACES)
    intro = {"en": "Heritage, temples and towns across Jhunjhunu district. Each guide lists its sources.", "hi": "पूरे झुंझुनू ज़िले की विरासत, मंदिर और क़स्बे। हर गाइड के साथ उसके स्रोत दिए गए हैं।"}[lang]
    page(lang, "explore", s["explore"], intro, f'<div class="wrap page"><h1>{e(s["explore"])}</h1><p class="lead detail-narrow">{e(intro)}</p><div class="grid grid-3">{cards}</div></div>', crumbs=[])
    for p in PLACES:
        c = p[lang]
        srcs = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{e(n)}</a></li>' for n, u in p["src"])
        page(lang, f'explore/{p["slug"]}', c["name"], c["short"], f'''<div class="wrap page detail-narrow"><div class="detail-badges"><span class="card-cat">{e(p["cat"][lang])}</span></div>
<h1>{e(c["name"])}</h1><p class="detail-scope"><span class="scope">{e(p["area"][lang])}</span></p><p class="lead">{e(c["short"])}</p>
<div class="prose">{c["body"]}</div><p class="notice notice-info">{e(s["visit_note"])}</p>
<div class="prose"><h2>{e(s["sources"])}</h2><ul>{srcs}</ul></div><p class="checked">{e(s["checked"])}: {CHECKED2[lang]}</p></div>''', crumbs=[(s["explore"], "explore")], og_type="article")
    # Jobs
    j = JOBS[lang]
    srcs = "".join(f'''<article class="info-item info-compact"><div class="info-main"><h3 class="card-title"><a href="{x["url"]}" target="_blank" rel="noopener">{e(x["name"])}</a></h3>
<p class="row-meta">{e(x[lang])}</p></div><div class="info-actions"><a class="btn btn-ghost btn-small" href="{x["url"]}" target="_blank" rel="noopener">{e(s["official"])}</a></div></article>''' for x in JOB_SOURCES)
    scam = "".join(f"<li>{e(t)}</li>" for t in j["scam"])
    page(lang, "jobs", j["title"], j["desc"], f'''<div class="wrap page"><h1>{e(j["title"])}</h1><p class="lead detail-narrow">{e(j["lead"])}</p>
<section class="info-group"><h2>{e(j["off_h"])}</h2><p class="muted">{e(j["off_p"])}</p><div class="essentials">{srcs}</div><p class="checked">{e(s["checked"])}: {CHECKED2[lang]}</p></section>
<section class="info-group"><h2>{e(j["local_h"])}</h2><div class="empty"><p class="empty-title">{e(j["local_empty"])}</p><p class="muted">{e(j["local_p"])}</p>{msg_btn}</div></section>
<section class="info-group detail-narrow"><h2>{e(j["scam_h"])}</h2><div class="prose"><ul>{scam}</ul></div><p><a href="../info/1930-cyber-fraud-helpline/">{e(j["scam_link"])} →</a></p></section></div>''', crumbs=[])
    # Events
    v = EV[lang]
    evs = "".join(f'''<article class="card"><h3 class="card-title">{e(x[lang]["name"])}</h3><dl class="facts"><div><dt>{e(v["when"])}</dt><dd>{e(x[lang]["when"])}</dd></div><div><dt>{e(v["where"])}</dt><dd>{e(x[lang]["where"])}</dd></div></dl>
<p class="card-text">{e(x[lang]["body"])}</p><p class="small muted">{e(s["sources"])}: <a href="{x["src"][1]}" target="_blank" rel="noopener">{e(x["src"][0])}</a></p></article>''' for x in EVENTS)
    page(lang, "events", v["title"], v["desc"], f'''<div class="wrap page"><h1>{e(v["title"])}</h1><p class="lead detail-narrow">{e(v["lead"])}</p>
<section class="info-group"><h2>{e(v["up_h"])}</h2><div class="empty"><p class="empty-title">{e(v["up_empty"])}</p><p class="muted">{e(v["up_p"])}</p>{msg_btn}</div></section>
<section class="info-group"><h2>{e(v["annual_h"])}</h2><div class="grid grid-2">{evs}</div><p class="checked">{e(s["checked"])}: {CHECKED2[lang]}</p></section></div>''', crumbs=[])
    # Businesses
    b = BIZ[lang]
    chips = "".join(f'<li><span class="chip">{e(t)}</span></li>' for t in BIZ_CATS[lang])
    how = "".join(f"<li>{e(t)}</li>" for t in b["how"])
    page(lang, "businesses", b["title"], b["desc"], f'''<div class="wrap page"><h1>{e(b["title"])}</h1><p class="lead detail-narrow">{e(b["lead"])}</p>
<section class="info-group"><h2>{e(b["cats_h"])}</h2><ul class="chips">{chips}</ul><div class="empty"><p class="empty-title">{e(b["empty"])}</p></div></section>
<div class="split"><section><h2>{e(b["how_h"])}</h2><div class="prose"><ul>{how}</ul></div></section>
<section class="invite-box" style="text-align:left;margin:0"><h2>{e(b["cta_h"])}</h2><p>{e(b["cta_p"])}</p>{msg_btn}</section></div></div>''', crumbs=[])
    # Advertise
    a = AD[lang]
    ways = "".join(f'<article class="card"><h3 class="card-title">{e(t)}</h3><p class="card-text">{e(d)}</p></article>' for t, d in a["ways"])
    rules = "".join(f"<li>{e(t)}</li>" for t in a["rules"])
    page(lang, "advertise", a["title"], a["desc"], f'''<div class="wrap page"><h1>{e(a["title"])}</h1><p class="lead detail-narrow">{e(a["lead"])}</p>
<section class="info-group"><h2>{e(a["ways_h"])}</h2><div class="grid grid-2">{ways}</div></section>
<section class="info-group detail-narrow"><h2>{e(a["rules_h"])}</h2><div class="prose"><ul>{rules}</ul></div></section>
<div class="invite-box"><h2>{e(a["cta_h"])}</h2><p>{e(a["cta_p"])}</p>{msg_btn}</div></div>''', crumbs=[])


def home_extra(lang):
    s = S[lang]
    cards = "".join(place_card(lang, p, f'explore/{p["slug"]}/') for p in PLACES[:3])
    head = {"en": ("Explore Jhunjhunu", "View all"), "hi": ("झुंझुनू घूमिए", "सब देखें")}[lang]
    sc = [("jobs", s["jobs"]), ("events", s["events"]), ("businesses", s["businesses"]), ("explore", s["explore"]), ("info", {"en": "Important contacts", "hi": "ज़रूरी संपर्क"}[lang])]
    shortcuts = "".join(f'<li><a href="{k}/"><span>{e(n)}</span></a></li>' for k, n in sc)
    return shortcuts, f'''<section class="band"><div class="wrap"><div class="section-head"><div><h2>{e(head[0])}</h2></div><a class="link-more" href="explore/">{e(head[1])} <span aria-hidden="true">→</span></a></div><div class="grid grid-3">{cards}</div></div></section>'''
