# scratch/build_clean.py
with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update $ global object
old_dollar = 'closing:_wi.closing??_w.closing??`See you there`}'
new_dollar = (
    'closing:_wi.closing??`With best compliments from Patel Family`,'
    'closingGu:_wi.closingGu??`સ્નેહાધીન: પટેલ પરિવાર`,'
    'family:_w.family||{},'
    'event:_w.event||_w.wedding||{},'
    'images:_wm,'
    'audio:_w.audio||{},'
    'invitationLine:_we.invitationLine??`Cordially invite you to celebrate the Engagement Ceremony of`,'
    'invitationLineGu:_we.invitationLineGu??`આપ સર્વે સ્નેહીજનોને સગાઈ મહોત્સવ પ્રસંગે સહર્ષ આમંત્રણ પાઠવીએ છીએ`,'
    'eventType:_we.title??`Engagement Ceremony`,'
    'eventTypeGu:_we.titleGu??`સગાઈ મહોત્સવ`,'
    'monogram:_wc.monogram||"J & K"}'
)
assert old_dollar in content, "Could not find old_dollar"
content = content.replace(old_dollar, new_dollar, 1)

# 2. Update wax seal monogram in function __
old_monogram = ',i=`${$.groom[0]}${$.bride[0]}`;'
new_monogram = ',i=$.monogram||"J & K";'
assert old_monogram in content, "Could not find old_monogram"
content = content.replace(old_monogram, new_monogram, 1)

# In envelope text on seal:
old_seal_header = 'children:`Save the date`}),(0,O.jsx)(f_,{className:`mt-3 w-32 text-gold/70`}),(0,O.jsx)(`p`,{className:`script mt-4 text-[3rem] leading-tight text-ink sm:text-[3.75rem]`,children:`You\'re invited`})'
new_seal_header = 'children:`Engagement Ceremony`}),(0,O.jsx)(f_,{className:`mt-3 w-32 text-gold/70`}),(0,O.jsx)(`p`,{className:`script mt-4 text-[3rem] leading-tight text-ink sm:text-[3.75rem]`,children:`You\'re invited`})'
assert old_seal_header in content, "Could not find old_seal_header"
content = content.replace(old_seal_header, new_seal_header, 1)

# 3. Update hero alt text
old_hero_alt = 'alt:`Illustration of ${$.groom} and ${$.bride} holding photo frames`'
new_hero_alt = 'alt:`Illustration of Jash & Krisha holding photo frames`'
assert old_hero_alt in content, "Could not find old_hero_alt"
content = content.replace(old_hero_alt, new_hero_alt, 1)

# 4. Update hero invitation line
old_hero_line = 'children:`Join us for the engagement party of`'
new_hero_line = 'children:$.invitationLine||`Cordially invite you to celebrate the Engagement Ceremony of`'
assert old_hero_line in content, "Could not find old_hero_line"
content = content.replace(old_hero_line, new_hero_line, 1)

# 5. Update countdown text in function r_
old_countdown_label = 'children:`Counting down to the evening`'
new_countdown_label = 'children:`Counting down to the Engagement Ceremony`'
assert old_countdown_label in content, "Could not find old_countdown_label"
content = content.replace(old_countdown_label, new_countdown_label, 1)

# 6. Replace C_
old_C = '''function C_(){return(0,O.jsxs)(`section`,{className:`px-7 py-20 text-center sm:py-28`,children:[(0,O.jsx)(Xg,{children:(0,O.jsx)(Yg,{className:`mb-10`})}),(0,O.jsx)(Xg,{delay:.1,children:(0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive`,children:`With the blessings of our families`})}),(0,O.jsx)(Xg,{delay:.2,children:(0,O.jsx)(`p`,{className:`mx-auto mt-7 max-w-md text-lg leading-[1.9] text-ink/85 sm:text-xl`,children:$.invitationNote})}),(0,O.jsxs)(Xg,{delay:.3,children:[(0,O.jsx)(`p`,{className:`script mt-8 text-3xl text-sepia`,children:$.dayLine}),(0,O.jsx)(`p`,{className:`caps mt-4 text-[0.6rem] text-sepia`,children:$.timeLine})]})]})}'''

new_C = '''function C_(){
  let lang=useLang_();
  let isGu=lang==="gu";
  let noteText = isGu ? ($.invitationNoteGu || $.invitationNote) : $.invitationNote;
  let dayText = isGu ? ($.dayLineGu || `શુક્રવાર, ૧૩ નવેમ્બર ૨૦૨૬`) : ($.dayLine || `Friday, 13th November 2026`);
  let timeText = isGu ? ($.timeLineGu || `સવારે ૯:૦૦ કલાકે`) : ($.timeLine || `9:00 AM`);
  let venueName = isGu ? ($.venue.nameGu || `શ્રી ખમાલાઈ માતાજી મંદિર`) : ($.venue.name || `Khamalaimata Temple`);
  let venueAddr = isGu ? ($.venue.addressGu || `મણુંદ, ગુજરાત ૩૮૪૨૬૦`) : ($.venue.address || `Manund, Gujarat 384260`);

  return (0,O.jsxs)(`section`,{id:`invitation-details`,className:`px-6 py-16 text-center sm:py-24 max-w-3xl mx-auto`,children:[
    (0,O.jsx)(Xg,{children:(0,O.jsx)(Yg,{className:`mb-8`})}),
    (0,O.jsx)(Xg,{delay:.1,children:(0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive tracking-[0.25em] font-semibold`,children: isGu ? `કુળદેવી શ્રી ખમાલાઈ માતાજીના આશીર્વાદ સાથે` : `With the blessings of our families & elders`})}),
    (0,O.jsx)(Xg,{delay:.18,children:(0,O.jsx)(`p`,{className:`mx-auto mt-6 max-w-lg text-lg leading-[1.9] text-ink/90 font-serif sm:text-xl`,children:noteText})}),
    (0,O.jsxs)(Xg,{delay:.26,children:[
      (0,O.jsxs)(`div`,{className:`event-card mt-10`,children:[
        (0,O.jsx)(`span`,{className:`family-badge`,children: isGu ? `શુભ મુહૂર્ત અને સ્થળ` : `EVENT DETAILS`}),
        (0,O.jsx)(`h3`,{className:`script text-3xl sm:text-4xl text-ink mt-2`,children:dayText}),
        (0,O.jsx)(`p`,{className:`caps mt-3 text-[0.62rem] text-gold font-bold tracking-widest sm:text-xs`,children:timeText}),
        (0,O.jsx)(`div`,{className:`my-4 mx-auto w-24 border-t border-gold/30`}),
        (0,O.jsx)(`p`,{className:`script text-2xl sm:text-3xl text-ink`,children:venueName}),
        (0,O.jsx)(`p`,{className:`text-xs text-sepia/80 mt-1 font-sans`,children:venueAddr})
      ]})
    ]})
  ]});
}'''
assert old_C in content, "Could not find old_C"
content = content.replace(old_C, new_C, 1)

# 7. Replace D_ (Venue section)
old_venue = '''function D_(){return(0,O.jsxs)(`section`,{className:`px-6 pb-20 text-center sm:pb-28`,children:[(0,O.jsxs)(Xg,{children:[(0,O.jsx)(Yg,{className:`mb-10`}),(0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive`,children:`The venue`}),(0,O.jsx)(`h2`,{className:`script mt-4 text-4xl text-ink sm:text-5xl`,children:$.venue.name}),(0,O.jsx)(`p`,{className:`mx-auto mt-3 max-w-xs text-base leading-relaxed text-sepia`,children:$.venue.address})]}),(0,O.jsx)(Xg,{delay:.15,children:(0,O.jsx)(Q.a,{href:Vg,target:`_blank`,rel:`noreferrer`,onClick:E_,whileTap:{scale:.985},className:`grain group mx-auto mt-8 block max-w-md overflow-hidden rounded-sm border border-border shadow-[0_20px_40px_-34px_rgba(60,45,25,0.75)]`,children:(0,O.jsxs)(`div`,{className:`relative`,children:[(0,O.jsx)(`img`,{src:T_,alt:`Map showing the location of ${$.venue.name}`,width:1024,height:768,loading:`lazy`,className:`h-52 w-full object-cover transition-transform duration-[1.2s] ease-out group-hover:scale-[1.04] sm:h-60`}),(0,O.jsx)(Q.span,{"aria-hidden":`true`,className:`absolute left-1/2 top-1/2 size-3 -translate-x-1/2 -translate-y-1/2 rounded-full bg-gold ring-8 ring-gold/20`,animate:{scale:[1,1.35,1],opacity:[1,.75,1]},transition:{duration:2.4,repeat:1/0,ease:`easeInOut`}}),(0,O.jsx)(`span`,{className:`caps absolute bottom-3 left-1/2 flex min-h-11 -translate-x-1/2 items-center rounded-full bg-paper/85 px-5 text-[0.5rem] text-ink backdrop-blur-sm`,children:`Open in maps`})]})})}),(0,O.jsx)(Xg,{delay:.25,children:(0,O.jsx)(Q.a,{href:Hg,target:`_blank`,rel:`noreferrer`,onClick:E_,whileTap:{scale:.96},className:`caps mt-6 inline-flex min-h-14 items-center gap-2 rounded-full border border-ink/25 px-8 text-[0.55rem] text-ink transition-colors duration-500 hover:border-ink hover:bg-ink hover:text-paper`,children:`Get directions`})})]})}'''

new_venue = '''function D_(){
  let lang=useLang_();
  let isGu=lang==="gu";
  let venueName = isGu ? ($.venue.nameGu || `શ્રી ખમાલાઈ માતાજી મંદિર`) : ($.venue.name || `Khamalaimata Temple`);
  let venueAddr = isGu ? ($.venue.addressGu || `મણુંદ, ગુજરાત ૩૮૪૨૬૦`) : ($.venue.address || `Manund, Gujarat 384260`);

  return (0,O.jsxs)(`section`,{id:`venue-section`,className:`px-6 pb-20 text-center sm:pb-28 max-w-4xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-10`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive tracking-widest font-semibold`,children: isGu ? `શુભ સ્થળ` : `The Auspicious Venue`}),
      (0,O.jsx)(`h2`,{className:`script mt-4 text-4xl text-ink sm:text-5xl`,children:venueName}),
      (0,O.jsx)(`p`,{className:`mx-auto mt-3 max-w-sm text-base leading-relaxed text-sepia font-serif`,children:venueAddr}),
      (0,O.jsx)(`p`,{className:`caps mt-1 text-[0.52rem] text-gold tracking-widest font-bold`,children: isGu ? `મણુંદ, ગુજરાત ૩૮૪૨૬૦` : `MANUND, GUJARAT 384260`})
    ]}),
    (0,O.jsx)(Xg,{delay:.15,children:(0,O.jsx)(Q.a,{
      href:Vg,
      target:`_blank`,
      rel:`noopener noreferrer`,
      onClick:E_,
      whileTap:{scale:.985},
      className:`grain group mx-auto mt-8 block max-w-md overflow-hidden rounded-2xl border border-gold/40 shadow-[0_20px_45px_-30px_rgba(60,45,25,0.7)] transition-all duration-500 hover:border-gold`,
      children:(0,O.jsxs)(`div`,{className:`relative`,children:[
        (0,O.jsx)(`img`,{src:T_,alt:`Map showing location of ${$.venue.name}`,width:1024,height:768,loading:`lazy`,className:`h-56 w-full object-cover transition-transform duration-[1.2s] ease-out group-hover:scale-[1.04] sm:h-64`}),
        (0,O.jsx)(Q.span,{"aria-hidden":`true`,className:`absolute left-1/2 top-1/2 size-3.5 -translate-x-1/2 -translate-y-1/2 rounded-full bg-gold ring-8 ring-gold/25`,animate:{scale:[1,1.4,1],opacity:[1,.7,1]},transition:{duration:2.4,repeat:1/0,ease:`easeInOut`}}),
        (0,O.jsx)(`span`,{className:`caps absolute bottom-4 left-1/2 flex min-h-11 -translate-x-1/2 items-center rounded-full bg-paper/90 px-6 text-[0.52rem] text-ink shadow-md backdrop-blur-md border border-gold/30 font-semibold`,children: isGu ? `ગૂગલ મેપ્સમાં જુઓ` : `Open in Google Maps`})
      ]})
    })}),
    (0,O.jsx)(Xg,{delay:.22,children:(0,O.jsx)(Q.a,{
      href:Hg,
      target:`_blank`,
      rel:`noopener noreferrer`,
      onClick:E_,
      whileTap:{scale:.96},
      className:`caps mt-6 inline-flex min-h-14 items-center gap-2 rounded-full bg-ink px-9 text-[0.55rem] text-paper shadow-md transition-all duration-500 hover:opacity-90 hover:scale-[1.02] font-semibold`,
      children: isGu ? `સ્થળ જુઓ (View Location)` : `View Location`
    })})
  ]});
}'''
assert old_venue in content, "Could not find old_venue"
content = content.replace(old_venue, new_venue, 1)

# 8. Define additional components before I_
additional_components = '''
/* Language State Management (English + Gujarati) */
function useLang_(){
  let [lang, setLang] = (0,b.useState)(()=>{
    try { return window.localStorage?.getItem("inv_lang") || "en"; } catch(e){ return "en"; }
  });
  (0,b.useEffect)(()=>{
    let handler = (e)=>{ setLang(e.detail); };
    window.addEventListener("langchange", handler);
    return ()=>window.removeEventListener("langchange", handler);
  },[]);
  return lang;
}

function switchLang_(newLang){
  try { window.localStorage?.setItem("inv_lang", newLang); } catch(e){}
  window.dispatchEvent(new CustomEvent("langchange", {detail: newLang}));
}

/* Floating Language Toggle Pill [ EN | ગુજરાતી ] */
function LanguageToggle_(){
  let lang = useLang_();
  let toggle = ()=>{
    let next = lang === "gu" ? "en" : "gu";
    switchLang_(next);
    E_();
  };

  return (0,O.jsxs)(`button`,{
    type:`button`,
    onClick:toggle,
    className:`lang-toggle-btn`,
    "aria-label":`Switch Language English / Gujarati`,
    title:`Switch Language / ભાષા બદલો`,
    children:[
      (0,O.jsx)(`span`,{className:`lang-pill-item ${lang === "en" ? "lang-pill-active" : ""}`,children:`EN`}),
      (0,O.jsx)(`span`,{className:`text-gold/50 text-xs`,children:`|`}),
      (0,O.jsx)(`span`,{className:`lang-pill-item ${lang === "gu" ? "lang-pill-active" : ""}`,children:`ગુજરાતી`})
    ]
  });
}

/* Family Section: Jash (Son of Jigneshbhai Harjibhai Patel & Urmilaben) & Krisha (Daughter of Piyushbhai Karshanbhai Patel & Vaishaliben) */
function FamilySection_(){
  let lang = useLang_();
  let isGu = lang === "gu";

  return (0,O.jsxs)(`section`,{id:`family-section`,className:`px-6 py-14 text-center sm:py-20 max-w-4xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-8`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive tracking-[0.25em] font-semibold`,children: isGu ? `કુટુંબ સ્નેહ અને આશીર્વાદ` : `With Family Blessings`}),
      (0,O.jsx)(`h2`,{className:`script mt-3 text-4xl sm:text-5xl text-ink leading-tight`,children: isGu ? `પરિવાર પરિચય` : `The Families`}),
      (0,O.jsx)(`p`,{className:`caps mt-2 text-[0.52rem] tracking-[0.2em] text-sepia/80`,children: isGu ? `શુભ સગાઈ સમારોહ • પટેલ પરિવાર` : `Patel Family Blessings & Greetings`})
    ]}),

    (0,O.jsx)(Xg,{delay:.18,children:(0,O.jsxs)(`div`,{
      className:`mt-10 grid grid-cols-1 sm:grid-cols-2 gap-6 sm:gap-8 items-stretch text-center`,
      children:[
        /* Groom Family Card */
        (0,O.jsxs)(`div`,{
          className:`family-card flex flex-col justify-between`,
          children:[
            (0,O.jsxs)(`div`,{children:[
              (0,O.jsx)(`span`,{className:`family-badge`,children: isGu ? `વરપક્ષ` : `GROOM'S FAMILY`}),
              (0,O.jsx)(`h3`,{className:`script text-3xl sm:text-4xl text-ink mt-2`,children: isGu ? `જશ` : `Jash`}),
              (0,O.jsx)(`p`,{className:`caps mt-3 text-[0.54rem] text-gold font-bold tracking-widest`,children: isGu ? `સુપુત્ર` : `SON OF`}),
              (0,O.jsx)(`p`,{className:`mt-2 text-base sm:text-lg text-ink/90 font-serif leading-relaxed`,children: isGu ? `જીગ્નેશભાઈ હરજીભાઈ પટેલ અને ઉર્મિલાબેન` : `Jigneshbhai Harjibhai Patel & Urmilaben`})
            ]}),
            (0,O.jsx)(`p`,{className:`caps text-[0.48rem] text-sepia/65 mt-5 tracking-widest`,children:`Patel Family • Manund`})
          ]
        }),

        /* Bride Family Card */
        (0,O.jsxs)(`div`,{
          className:`family-card flex flex-col justify-between`,
          children:[
            (0,O.jsxs)(`div`,{children:[
              (0,O.jsx)(`span`,{className:`family-badge`,children: isGu ? `કન્યાપક્ષ` : `BRIDE'S FAMILY`}),
              (0,O.jsx)(`h3`,{className:`script text-3xl sm:text-4xl text-ink mt-2`,children: isGu ? `ક્રિશા` : `Krisha`}),
              (0,O.jsx)(`p`,{className:`caps mt-3 text-[0.54rem] text-gold font-bold tracking-widest`,children: isGu ? `સુપુત્રી` : `DAUGHTER OF`}),
              (0,O.jsx)(`p`,{className:`mt-2 text-base sm:text-lg text-ink/90 font-serif leading-relaxed`,children: isGu ? `પિયુષભાઈ કરશનભાઈ પટેલ અને વૈશાલીબેન` : `Piyushbhai Karshanbhai Patel & Vaishaliben`})
            ]}),
            (0,O.jsx)(`p`,{className:`caps text-[0.48rem] text-sepia/65 mt-5 tracking-widest`,children:`Patel Family • Gujarat`})
          ]
        })
      ]
    })})
  ]});
}

/* Photo Section: Contextual customer photos + Replaceable couple photo slot */
function PhotoSection_(){
  let lang = useLang_();
  let isGu = lang === "gu";
  let images = $.images || {};
  let couplePhoto = images.couplePhoto || "";

  return (0,O.jsxs)(`section`,{id:`photo-gallery`,className:`px-6 py-14 text-center sm:py-20 max-w-4xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-8`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive tracking-[0.25em] font-semibold`,children: isGu ? `યાદગાર ક્ષણો` : `Cherished Glimpses`}),
      (0,O.jsx)(`h2`,{className:`script mt-3 text-4xl sm:text-5xl text-ink leading-tight`,children: isGu ? `તસવીરો અને સ્મૃતિઓ` : `Photographs & Memories`}),
      (0,O.jsx)(`p`,{className:`caps mt-2 text-[0.5rem] tracking-[0.22em] text-sepia/80`,children: isGu ? `સુંદર પળોનો સંગ્રહ` : `Moments of Joy & Celebration`})
    ]}),

    (0,O.jsx)(Xg,{delay:.18,children:(0,O.jsxs)(`div`,{
      className:`mt-10 grid grid-cols-1 sm:grid-cols-3 gap-6 items-stretch`,
      children:[
        /* 1. Couple Photo Slot (Ready for replacement, never fake) */
        (0,O.jsxs)(`div`,{
          className:`photo-card flex flex-col justify-between`,
          children:[
            couplePhoto ? (
              (0,O.jsx)(`div`,{className:`photo-image-wrapper`,children:
                (0,O.jsx)(`img`,{src:couplePhoto,alt:`Jash & Krisha`,className:`size-full object-cover`})
              })
            ) : (
              (0,O.jsxs)(`div`,{className:`photo-slot-replaceable`,children:[
                (0,O.jsxs)(`svg`,{className:`size-12 text-gold/75 mb-3`,viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`1.3`,children:[
                  (0,O.jsx)(`rect`,{x:`3`,y:`3`,width:`18`,height:`18`,rx:`4`}),
                  (0,O.jsx)(`circle`,{cx:`8.5`,cy:`8.5`,r:`1.5`}),
                  (0,O.jsx)(`path`,{d:`M21 15l-5-5L5 21`})
                ]}),
                (0,O.jsx)(`p`,{className:`caps text-[0.58rem] font-bold text-ink tracking-wider`,children: isGu ? `દંપતી તસવીર સ્લોટ` : `Couple Photo Slot`}),
                (0,O.jsx)(`p`,{className:`text-xs italic text-sepia/75 mt-1 max-w-[190px] leading-relaxed`,children: isGu ? `જશ અને ક્રિશાની તસવીર માટે આરક્ષિત` : `Reserved for Jash & Krisha's photograph`}),
                (0,O.jsx)(`span`,{className:`caps mt-3 inline-block rounded-full border border-gold/50 px-3 py-1 text-[0.45rem] font-semibold text-gold tracking-widest`,children: isGu ? `તસવીર ઉમેરવા માટે તૈયાર` : `Ready for replacement`})
              ]})
            ),
            (0,O.jsx)(`p`,{className:`caps text-[0.5rem] font-semibold text-sepia/80 mt-3 tracking-widest`,children: isGu ? `જશ & ક્રિશા` : `Jash & Krisha`})
          ]
        }),

        /* 2. Customer Photo 1 (Baby boy with toy tiger - NOT labeled as Jash) */
        (0,O.jsxs)(`div`,{
          className:`photo-card flex flex-col justify-between`,
          children:[
            (0,O.jsx)(`div`,{className:`photo-image-wrapper`,children:
              (0,O.jsx)(`img`,{
                src:`./editable/assets/customer-photo-1.jpg`,
                alt:`Cherished Moments`,
                loading:`lazy`,
                className:`size-full object-cover`
              })
            }),
            (0,O.jsxs)(`div`,{className:`mt-3`,children:[
              (0,O.jsx)(`p`,{className:`caps text-[0.54rem] font-bold text-ink tracking-wider`,children: isGu ? `સ્મૃતિ પળો` : `Cherished Moments`}),
              (0,O.jsx)(`p`,{className:`text-[0.48rem] text-sepia/70 mt-0.5 tracking-wide`,children: isGu ? `પારિવારિક યાદો` : `Family Memories`})
            ]})
          ]
        }),

        /* 3. Customer Photo 2 (Baby girl in magenta - NOT labeled as Krisha) */
        (0,O.jsxs)(`div`,{
          className:`photo-card flex flex-col justify-between`,
          children:[
            (0,O.jsx)(`div`,{className:`photo-image-wrapper`,children:
              (0,O.jsx)(`img`,{
                src:`./editable/assets/customer-photo-2.jpg`,
                alt:`Sweet Memories`,
                loading:`lazy`,
                className:`size-full object-cover`
              })
            }),
            (0,O.jsxs)(`div`,{className:`mt-3`,children:[
              (0,O.jsx)(`p`,{className:`caps text-[0.54rem] font-bold text-ink tracking-wider`,children: isGu ? `મીઠી યાદો` : `Sweet Memories`}),
              (0,O.jsx)(`p`,{className:`text-[0.48rem] text-sepia/70 mt-0.5 tracking-wide`,children: isGu ? `પારિવારિક સ્નેહ` : `Family Moments`})
            ]})
          ]
        })
      ]
    })})
  ]});
}

/* Floating Audio / Music Player Component */
function MusicButton_(){
  let audioData = $.audio || {};
  let audioUrl = audioData.url || `./editable/assets/music.mp3`;
  let [isPlaying, setIsPlaying] = (0,b.useState)(false);
  let audioRef = (0,b.useRef)(null);

  (0,b.useEffect)(()=>{
    let audio = new Audio(audioUrl);
    audio.loop = true;
    audio.preload = `auto`;
    audioRef.current = audio;
    return ()=>{
      audio.pause();
      audio.src = "";
    };
  },[audioUrl]);

  let toggleMusic = ()=>{
    E_();
    if(audioRef.current){
      if(isPlaying){
        audioRef.current.pause();
        setIsPlaying(false);
      } else {
        audioRef.current.play().then(()=>setIsPlaying(true)).catch(()=>{
          setIsPlaying(false);
        });
      }
    }
  };

  return(0,O.jsx)(`button`,{
    type:`button`,
    onClick:toggleMusic,
    "aria-label":isPlaying ? `Pause background music` : `Play celebration melody`,
    className:`floating-music-btn`,
    title:isPlaying ? `Pause music` : `Play celebration melody`,
    children: isPlaying ? (
      (0,O.jsxs)(`svg`,{className:`size-5 text-paper animate-pulse`,viewBox:`0 0 24 24`,fill:`currentColor`,children:[
        (0,O.jsx)(`rect`,{x:`6`,y:`5`,width:`4`,height:`14`,rx:`1`}),
        (0,O.jsx)(`rect`,{x:`14`,y:`5`,width:`4`,height:`14`,rx:`1`})
      ]})
    ) : (
      (0,O.jsx)(`svg`,{className:`size-5 text-paper`,viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`2`,strokeLinecap:`round`,strokeLinejoin:`round`,children:[
        (0,O.jsx)(`path`,{d:`M9 18V5l12-2v13`}),
        (0,O.jsx)(`circle`,{cx:`6`,cy:`18`,r:`3`}),
        (0,O.jsx)(`circle`,{cx:`18`,cy:`16`,r:`3`})
      ]})
    )
  });
}
'''

# 9. Update I_() to assemble all engagement sections cleanly
old_I = '''function I_(){M_();let[e,t]=(0,b.useState)(!1);return(0,O.jsxs)(O.Fragment,{children:[(0,O.jsx)(__,{onOpen:()=>t(!0)}),(0,O.jsx)(w_,{}),(0,O.jsxs)(`main`,{className:`grain relative min-h-screen bg-paper text-ink`,style:{backgroundImage:`url(${ua})`,backgroundSize:`480px`},children:[(0,O.jsx)(b_,{ready:e}),(0,O.jsx)(C_,{}),(0,O.jsx)(r_,{}),(0,O.jsx)(D_,{}),(0,O.jsx)($g,{}),(0,O.jsx)(S_,{})]}),(0,O.jsx)(Jg,{})]})}'''

new_I = additional_components + '''
function I_(){
  M_();
  let[e,t]=(0,b.useState)(!1);
  return(0,O.jsxs)(O.Fragment,{children:[
    (0,O.jsx)(__,{onOpen:()=>t(!0)}),
    (0,O.jsx)(w_,{}),
    (0,O.jsx)(LanguageToggle_,{}),
    (0,O.jsxs)(`main`,{className:`grain relative min-h-screen bg-paper text-ink`,style:{backgroundImage:`url(${ua})`,backgroundSize:`480px`},children:[
      (0,O.jsx)(b_,{ready:e}),
      (0,O.jsx)(FamilySection_,{}),
      (0,O.jsx)(C_,{}),
      (0,O.jsx)(r_,{}),
      (0,O.jsx)(PhotoSection_,{}),
      (0,O.jsx)(D_,{}),
      (0,O.jsx)($g,{}),
      (0,O.jsx)(S_,{})
    ]}),
    (0,O.jsx)(Jg,{}),
    (0,O.jsx)(MusicButton_,{})
  ]});
}
'''

assert old_I in content, "Could not find old_I"
content = content.replace(old_I, new_I, 1)

with open('assets/index-2d1L6cXj.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Jash & Krisha Engagement Bundle successfully built!")
