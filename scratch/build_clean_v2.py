# scratch/build_clean_v2.py
import re

with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update $ definition
s_dollar = c.find('closing:_wi.closing??_w.closing??`See you there`}')
assert s_dollar != -1, "s_dollar not found"
e_dollar = s_dollar + len('closing:_wi.closing??_w.closing??`See you there`}')
new_dollar = (
    'closing:_wi.closing??`With best compliments from Patel Family`,'
    'family:_w.family||{},'
    'event:_w.event||_w.wedding||{},'
    'images:_wm,'
    'audio:_w.audio||{},'
    'invitationLine:_we.invitationLine??`Cordially invite you to celebrate the Engagement Ceremony of`,'
    'eventType:_we.title??`Engagement Ceremony`,'
    'monogram:_wc.monogram||"J & K"}'
)
c = c[:s_dollar] + new_dollar + c[e_dollar:]

# 2. Update countdown label
c = c.replace('children:`Counting down to the evening`', 'children:`Counting down to the Engagement Ceremony`', 1)

# 3. Replace function __ (Image 1: larger fonts, royal crest logo, auto-play music)
s_seal = c.find('function __({onOpen:e}){')
e_seal = c.find('function v_(e,t,n=[', s_seal)
assert s_seal != -1 and e_seal != -1, "seal boundaries not found"

new_cover_fn = '''function __({onOpen:e}){
  let t=Bg(),[n,r]=(0,b.useState)(`sealed`);
  (0,b.useEffect)(()=>(c_(),()=>l_()),[]);

  let a=()=>{
    try { window.__playInvitationAudio && window.__playInvitationAudio(); } catch(err){}
    n===`sealed`&&(r(`breaking`),navigator.vibrate&&navigator.vibrate([12,40,18]),window.setTimeout(()=>{r(`gone`),l_(),e?.()},t?200:1600));
  };

  let o=n!==`sealed`,s={backgroundImage:`url(${ua})`,backgroundSize:`480px`};
  let c=e=>(0,O.jsxs)(Q.div,{className:`absolute inset-x-0 h-1/2 overflow-hidden ${e===`top`?`top-0`:`bottom-0`}`,initial:!1,animate:o?{y:e===`top`?`-102%`:`102%`,rotate:e===`top`?-1.2:1.2}:{y:`0%`,rotate:0},transition:{duration:t?.2:1.3,ease:g_,delay:o&&!t?.4:0},children:[
    (0,O.jsxs)(`div`,{className:`grain absolute inset-x-0 h-[100svh] bg-paper`,style:{...s,[e===`top`?`top`:`bottom`]:0},children:[
      (0,O.jsx)(`div`,{"aria-hidden":`true`,className:`absolute inset-0`,style:{background:`radial-gradient(58% 40% at 50% 50%, color-mix(in oklab, var(--gold) 16%, transparent) 0%, transparent 70%), radial-gradient(120% 90% at 50% 50%, transparent 55%, color-mix(in oklab, var(--sepia) 22%, transparent) 100%)`}}),
      (0,O.jsxs)(`div`,{"aria-hidden":`true`,className:`absolute inset-4 sm:inset-6`,children:[
        (0,O.jsx)(`div`,{className:`absolute inset-0 border border-gold/45`}),
        (0,O.jsx)(`div`,{className:`absolute inset-[6px] border border-gold/20`}),
        (0,O.jsx)(u_,{className:`absolute -top-px -left-px size-16 text-gold/60 sm:size-20`}),
        (0,O.jsx)(u_,{className:`absolute -top-px -right-px size-16 -scale-x-100 text-gold/60 sm:size-20`}),
        (0,O.jsx)(u_,{className:`absolute -bottom-px -left-px size-16 -scale-y-100 text-gold/60 sm:size-20`}),
        (0,O.jsx)(u_,{className:`absolute -right-px -bottom-px size-16 -scale-100 text-gold/60 sm:size-20`})
      ]}),
      (0,O.jsxs)(`div`,{className:`relative flex h-full flex-col items-center justify-center px-8 text-center select-none`,children:[
        (0,O.jsx)(`p`,{className:`caps text-[0.82rem] sm:text-[0.95rem] font-bold text-sepia tracking-[0.28em]`,children:`Engagement Ceremony`}),
        (0,O.jsx)(f_,{className:`mt-3 w-36 text-gold/80`}),
        (0,O.jsx)(`p`,{className:`script mt-4 text-[3.25rem] leading-tight text-ink sm:text-[4rem]`,children:`You're invited`}),
        (0,O.jsxs)(`p`,{className:`caps mt-3 text-[0.88rem] sm:text-[1rem] font-bold text-ink/90 tracking-[0.24em]`,children:[$.groom,` & `,$.bride]}),
        (0,O.jsx)(f_,{className:`my-4 w-28 rotate-180 text-gold/60`}),
        (0,O.jsx)(`p`,{className:`caps text-[0.95rem] sm:text-base font-bold text-ink/90 tracking-[0.28em] font-sans`,children:$.dateLabel}),
        (0,O.jsx)(`p`,{className:`caps mt-2 text-[0.75rem] sm:text-[0.85rem] font-bold text-sepia tracking-[0.22em]`,children:$.venue.name}),
        (0,O.jsx)(`p`,{className:`caps mt-1.5 text-[0.7rem] sm:text-[0.8rem] font-semibold text-sepia/85 tracking-[0.25em]`,children:$.venue.city||`Manund`}),
        (0,O.jsxs)(`div`,{className:`caps mt-7 flex items-center justify-center gap-3 text-[0.62rem] font-semibold text-sepia tracking-widest`,children:[
          (0,O.jsx)(`span`,{className:`h-px w-8 bg-gold/70`}),
          `Tap to open`,
          (0,O.jsx)(`span`,{className:`h-px w-8 bg-gold/70`})
        ]})
      ]})
    ]}),
    (0,O.jsx)(`div`,{"aria-hidden":`true`,className:`absolute inset-x-0 h-8 ${e===`top`?`bottom-0 bg-gradient-to-b from-transparent to-ink/10`:`top-0 bg-gradient-to-t from-transparent to-ink/6`}`})
  ]});

  return (0,O.jsx)(Gp,{children:n!==`gone`&&(0,O.jsxs)(Q.div,{onClick:a,role:`button`,"aria-label":`Tap to open the invitation`,tabIndex:0,className:`fixed inset-0 z-50 cursor-pointer select-none`,exit:{opacity:0},transition:{duration:.35},children:[
    c(`top`),
    c(`bottom`),
    !t&&n===`sealed`&&(0,O.jsx)(`div`,{className:`pointer-events-none absolute inset-0 opacity-70`,children:(0,O.jsx)(h_,{count:9})}),
    n===`breaking`&&!t&&(0,O.jsx)(m_,{count:44,spread:340,seed:3})
  ]})})}'''
c = c[:s_seal] + new_cover_fn + c[e_seal:]

# 4. Replace function b_ (Hero section: date not cursive, couple holding child frames)
s_b = c.find('function b_({ready:e=!0}){')
e_b = c.find('var x_=_wm.footerBg', s_b)
assert s_b != -1 and e_b != -1, "b_ boundaries not found"

new_b_fn = '''function b_({ready:e=!0}){
  let t=(0,b.useRef)(null),n=Bg(),{y:r,progress:i}=v_(t,[0,70]),a=Fg(i,[0,.75],[1,0]),[o,s]=(0,b.useState)([]),c=[.22,.61,.36,1],l=e?`show`:`hidden`;

  let u=(0,b.useCallback)(e=>{
    if(n)return;
    let r=t.current?.getBoundingClientRect();
    if(!r)return;
    let i=Date.now();
    s(t=>[...t.slice(-2),{id:i,x:e.clientX-r.left,y:e.clientY-r.top}]);
    navigator.vibrate&&navigator.vibrate(8);
    window.setTimeout(()=>s(e=>e.filter(e=>e.id!==i)),2600);
  },[n]);

  let d=()=>{
    let e=t.current?.nextElementSibling;
    if(!e)return;
    let n=s_();
    n?n.scrollTo(e,{duration:1.4,offset:-20}):e.scrollIntoView({behavior:`smooth`});
  };

  return (0,O.jsxs)(`section`,{ref:t,onPointerDown:u,className:`relative flex min-h-[100svh] flex-col items-center justify-center overflow-hidden px-6 py-16 text-center select-none`,children:[
    (0,O.jsx)(h_,{}),
    o.map(e=>(0,O.jsx)(m_,{x:e.x,y:e.y,count:14,spread:130,seed:e.id%11},e.id)),
    (0,O.jsx)(Q.p,{className:`caps text-[0.68rem] text-gold tracking-[0.25em] font-bold sm:text-xs`,initial:{opacity:0,y:12},animate:e?{opacity:1,y:0}:{opacity:0,y:12},transition:{duration:1,ease:c},children:`ENGAGEMENT CEREMONY`}),
    /* Date on Hero: NOT CURSIVE (Item 5) */
    (0,O.jsx)(Q.p,{className:`font-serif mt-3 text-3xl sm:text-5xl font-semibold tracking-wide text-ink`,initial:{opacity:0,y:16},animate:e?{opacity:1,y:0}:{opacity:0,y:16},transition:{duration:1.1,delay:.15,ease:c},children:$.displayDate||`13 November 2026`}),
    (0,O.jsx)(Q.p,{className:`caps mt-2 text-xs sm:text-sm text-sepia tracking-widest font-bold`,initial:{opacity:0},animate:e?{opacity:1}:{opacity:0},transition:{duration:1,delay:.2},children:`9:00 AM`}),
    /* Couple holding child frames (Item 2) */
    (0,O.jsx)(Q.div,{style:{y:r,opacity:a},className:`mt-6 w-full max-w-sm sm:max-w-md`,children:(0,O.jsx)(Q.img,{src:y_,alt:`Illustration of Jash & Krisha holding photo frames`,width:1024,height:1024,draggable:!1,className:`mx-auto w-full select-none`,initial:{opacity:0,scale:.96},animate:e?{opacity:1,scale:1}:{opacity:0,scale:.96},transition:{duration:1.4,delay:.3,ease:c}})}),
    (0,O.jsx)(Q.p,{className:`caps mt-6 max-w-md text-[0.65rem] leading-[2] text-olive font-semibold sm:text-xs`,initial:{opacity:0},animate:e?{opacity:1}:{opacity:0},transition:{duration:1,delay:.7},children:$.invitationLine||`Cordially invite you to celebrate the Engagement Ceremony of`}),
    (0,O.jsxs)(Q.h1,{className:`script mt-3 text-[3.25rem] leading-[1.05] text-ink sm:text-7xl`,initial:`hidden`,animate:l,children:[
      (0,O.jsx)(Zg,{text:$.groom,delay:.85,trigger:l}),
      (0,O.jsx)(`span`,{className:`mx-3 text-gold sm:mx-5`,children:`&`}),
      (0,O.jsx)(Zg,{text:$.bride,delay:1.2,trigger:l})
    ]}),
    (0,O.jsx)(`p`,{className:`caps mt-3 text-[0.58rem] text-sepia/85 tracking-[0.2em] font-semibold`,children:`Khamalaimata Temple, Manund, Gujarat`}),
    (0,O.jsxs)(Q.button,{type:`button`,onClick:e=>{e.stopPropagation(),d()},"aria-label":`Scroll to the invitation`,className:`mt-8 flex min-h-14 flex-col items-center justify-end gap-2 px-8 pb-1`,initial:{opacity:0},animate:e?{opacity:1}:{opacity:0},transition:{duration:1,delay:1.8},whileTap:{scale:.95},children:[
      (0,O.jsx)(`span`,{className:`caps text-[0.5rem] tracking-[0.25em] text-sepia`,children:`Scroll`}),
      (0,O.jsx)(Q.span,{"aria-hidden":`true`,className:`size-2 rotate-45 border-b border-r border-sepia`,animate:{y:[0,4,0]},transition:{duration:1.6,repeat:1/0,ease:`easeInOut`}})
    ]})
  ]});
}'''
c = c[:s_b] + new_b_fn + c[e_b:]

# 5. Replace function C_ (Event Details: date not cursive, 9:00 AM lit bit bigger, temple in normal letter like manund, gujarat)
s_c = c.find('function C_(){')
e_c = c.find('function w_()', s_c)
assert s_c != -1 and e_c != -1, "C_ boundaries not found"

new_c_fn = '''function C_(){
  let noteText = $.invitationNote;
  let dayText = $.dayLine || `Friday, 13th November 2026`;
  let timeText = $.timeLine || `9:00 AM`;
  let venueName = ($.venue && $.venue.name) || `Khamalaimata Temple`;
  let venueAddr = ($.venue && $.venue.address) || `Manund, Gujarat 384260`;

  return (0,O.jsxs)(`section`,{id:`invitation-details`,className:`px-6 py-16 text-center sm:py-24 max-w-3xl mx-auto`,children:[
    (0,O.jsx)(Xg,{children:(0,O.jsx)(Yg,{className:`mb-8`})}),
    (0,O.jsx)(Xg,{delay:.1,children:(0,O.jsx)(`p`,{className:`caps text-[0.62rem] text-olive tracking-[0.25em] font-bold`,children:`With the blessings of our families & elders`})}),
    (0,O.jsx)(Xg,{delay:.18,children:(0,O.jsx)(`p`,{className:`mx-auto mt-6 max-w-lg text-lg leading-[1.9] text-ink/90 font-serif sm:text-xl`,children:noteText})}),
    (0,O.jsxs)(Xg,{delay:.26,children:[
      (0,O.jsxs)(`div`,{className:`event-card mt-10`,children:[
        (0,O.jsx)(`span`,{className:`family-badge`,children:`EVENT DETAILS`}),
        /* Image 3 Date: NOT CURSIVE (Item 5) */
        (0,O.jsx)(`h3`,{className:`font-serif text-2xl sm:text-3xl font-semibold text-ink mt-2 tracking-wide`,children:dayText}),
        /* Image 3 Time: 9:00 AM LIT BIT BIGGER (Item 9) */
        (0,O.jsx)(`p`,{className:`caps mt-3 text-[0.95rem] sm:text-base text-gold font-bold tracking-[0.25em]`,children:timeText}),
        (0,O.jsx)(`div`,{className:`my-4 mx-auto w-24 border-t border-gold/30`}),
        /* Image 3 Venue: KHAMALAIMATA TEMPLE in normal letter like manund, gujarat (Item 9) */
        (0,O.jsx)(`p`,{className:`text-xl sm:text-2xl font-serif font-semibold text-ink mt-2 tracking-wide`,children:venueName}),
        /* Image 3 Address: Manund, Gujarat 384260 */
        (0,O.jsx)(`p`,{className:`text-sm sm:text-base text-sepia/85 mt-1 font-sans`,children:venueAddr})
      ]})
    ]})
  ]});
}'''
c = c[:s_c] + new_c_fn + c[e_c:]

# 6. Replace function D_ (Venue section)
s_d = c.find('function D_(){')
e_d = c.find('var O_=', s_d)
assert s_d != -1 and e_d != -1, "D_ boundaries not found"

new_d_fn = '''function D_(){
  let venueName = ($.venue && $.venue.name) || `Khamalaimata Temple`;
  let venueAddr = ($.venue && $.venue.address) || `Manund, Gujarat 384260`;

  return (0,O.jsxs)(`section`,{id:`venue-section`,className:`px-6 pb-20 text-center sm:pb-28 max-w-4xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-10`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.62rem] text-olive tracking-widest font-bold`,children:`The Auspicious Venue`}),
      (0,O.jsx)(`h2`,{className:`font-serif mt-4 text-3xl sm:text-4xl text-ink font-semibold tracking-wide`,children:venueName}),
      (0,O.jsx)(`p`,{className:`mx-auto mt-3 max-w-sm text-base leading-relaxed text-sepia font-serif`,children:venueAddr}),
      (0,O.jsx)(`p`,{className:`caps mt-1 text-[0.55rem] text-gold tracking-widest font-bold`,children:`MANUND, GUJARAT 384260`})
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
        (0,O.jsx)(`span`,{className:`caps absolute bottom-4 left-1/2 flex min-h-11 -translate-x-1/2 items-center rounded-full bg-paper/90 px-6 text-[0.54rem] text-ink shadow-md backdrop-blur-md border border-gold/30 font-semibold`,children:`Open in Google Maps`})
      ]})
    })}),
    (0,O.jsx)(Xg,{delay:.22,children:(0,O.jsxs)(Q.a,{
      href:Hg,
      target:`_blank`,
      rel:`noopener noreferrer`,
      onClick:E_,
      whileTap:{scale:.97},
      className:`view-location-btn`,
      children:[
        (0,O.jsx)(`svg`,{className:`size-4 text-gold shrink-0`,viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`2`,children:(0,O.jsxs)(O.Fragment,{children:[
          (0,O.jsx)(`path`,{d:`M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z`}),
          (0,O.jsx)(`circle`,{cx:`12`,cy:`10`,r:`3`})
        ]})}),
        `VIEW LOCATION`
      ]
    })})
  ]});
}'''
c = c[:s_d] + new_d_fn + c[e_d:]

# 7. Additional components: Global Audio, FamilySection_, PhotoSection_, MusicButton_, I_()
additional_components = '''
/* Global Auto-Play Audio Controller (Item 6) */
var __invAudio = null;
var __invAudioStarted = false;

function getGlobalAudio(){
  if(__invAudio) return __invAudio;
  var audioData = (window.WEDDING_DATA && window.WEDDING_DATA.audio) || {};
  var audioUrl = audioData.url || `./editable/assets/music.mp3`;
  __invAudio = new Audio(audioUrl);
  __invAudio.loop = true;
  __invAudio.preload = `auto`;
  return __invAudio;
}

window.__playInvitationAudio = function(){
  var audio = getGlobalAudio();
  if(!audio) return;
  audio.play().then(function(){
    __invAudioStarted = true;
    window.dispatchEvent(new CustomEvent(`musicstatus`, {detail: true}));
  }).catch(function(){});
};

/* Attach first-interaction listener to start music immediately if browser blocked unmuted autoplay */
if(typeof window !== `undefined`){
  var __startMusicOnInteraction = function(){
    window.__playInvitationAudio();
    window.removeEventListener(`click`, __startMusicOnInteraction);
    window.removeEventListener(`touchstart`, __startMusicOnInteraction);
  };
  window.addEventListener(`click`, __startMusicOnInteraction, {once: true, passive: true});
  window.addEventListener(`touchstart`, __startMusicOnInteraction, {once: true, passive: true});
  window.setTimeout(function(){
    window.__playInvitationAudio();
  }, 100);
}

/* Family Section: Mom's name first (Item 3), Balisana location (Item 4), marked fonts MUCH BIGGER (Item 8) */
function FamilySection_(){
  let groomParents = ($.family && $.family.groomSide && $.family.groomSide.parents) || `Urmilaben & Jigneshbhai Harjibhai Patel`;
  let brideParents = ($.family && $.family.brideSide && $.family.brideSide.parents) || `Vaishaliben & Piyushbhai Karshanbhai Patel`;

  return (0,O.jsxs)(`section`,{id:`family-section`,className:`px-6 py-14 text-center sm:py-20 max-w-4xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-8`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.65rem] text-olive tracking-[0.25em] font-bold`,children:`With Family Blessings`}),
      (0,O.jsx)(`h2`,{className:`script mt-3 text-4xl sm:text-5xl text-ink leading-tight`,children:`The Families`}),
      (0,O.jsx)(`p`,{className:`caps mt-2 text-[0.54rem] tracking-[0.2em] text-sepia/80`,children:`Patel Family Blessings & Greetings`})
    ]}),

    (0,O.jsx)(Xg,{delay:.18,children:(0,O.jsxs)(`div`,{
      className:`mt-10 grid grid-cols-1 sm:grid-cols-2 gap-6 sm:gap-8 items-stretch text-center`,
      children:[
        /* Groom Family Card */
        (0,O.jsxs)(`div`,{
          className:`family-card flex flex-col justify-between`,
          children:[
            (0,O.jsxs)(`div`,{children:[
              (0,O.jsx)(`span`,{className:`family-badge`,children:`GROOM'S FAMILY`}),
              (0,O.jsx)(`h3`,{className:`script text-3xl sm:text-4xl text-ink mt-2`,children:`Jash`}),
              (0,O.jsx)(`p`,{className:`caps mt-3 text-[0.56rem] text-gold font-bold tracking-widest`,children:`SON OF`}),
              /* Mom's name first, then father (Item 3) */
              (0,O.jsx)(`p`,{className:`mt-2 text-base sm:text-lg text-ink/90 font-serif leading-relaxed`,children:groomParents})
            ]}),
            /* Image 2 marked sentence: Patel Family • Manund (MUCH BIGGER, Item 8) */
            (0,O.jsx)(`p`,{className:`caps text-[0.82rem] sm:text-[0.92rem] font-bold text-sepia/90 mt-5 tracking-[0.2em]`,children:`Patel Family • Manund`})
          ]
        }),

        /* Bride Family Card */
        (0,O.jsxs)(`div`,{
          className:`family-card flex flex-col justify-between`,
          children:[
            (0,O.jsxs)(`div`,{children:[
              (0,O.jsx)(`span`,{className:`family-badge`,children:`BRIDE'S FAMILY`}),
              (0,O.jsx)(`h3`,{className:`script text-3xl sm:text-4xl text-ink mt-2`,children:`Krisha`}),
              (0,O.jsx)(`p`,{className:`caps mt-3 text-[0.56rem] text-gold font-bold tracking-widest`,children:`DAUGHTER OF`}),
              /* Mom's name first, then father (Item 3) */
              (0,O.jsx)(`p`,{className:`mt-2 text-base sm:text-lg text-ink/90 font-serif leading-relaxed`,children:brideParents})
            ]}),
            /* Image 2 marked sentence: Patel Family • Balisana (MUCH BIGGER, Items 4 & 8) */
            (0,O.jsx)(`p`,{className:`caps text-[0.82rem] sm:text-[0.92rem] font-bold text-sepia/90 mt-5 tracking-[0.2em]`,children:`Patel Family • Balisana`})
          ]
        })
      ]
    })})
  ]});
}

/* Photo Section: Contextual customer photos without blank couple placeholder */
function PhotoSection_(){
  return (0,O.jsxs)(`section`,{id:`photo-gallery`,className:`px-6 py-14 text-center sm:py-20 max-w-4xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-8`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.65rem] text-olive tracking-[0.25em] font-bold`,children:`Cherished Glimpses`}),
      (0,O.jsx)(`h2`,{className:`script mt-3 text-4xl sm:text-5xl text-ink leading-tight`,children:`Photographs & Memories`}),
      (0,O.jsx)(`p`,{className:`caps mt-2 text-[0.52rem] tracking-[0.22em] text-sepia/80`,children:`Moments of Joy & Celebration`})
    ]}),

    (0,O.jsx)(Xg,{delay:.18,children:(0,O.jsxs)(`div`,{
      className:`mt-10 grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-2xl mx-auto items-stretch`,
      children:[
        /* 1. Customer Photo 1 (Baby Jash) */
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
              (0,O.jsx)(`p`,{className:`caps text-[0.56rem] font-bold text-ink tracking-wider`,children:`Cherished Moments`}),
              (0,O.jsx)(`p`,{className:`text-[0.5rem] text-sepia/70 mt-0.5 tracking-wide`,children:`Family Memories`})
            ]})
          ]
        }),

        /* 2. Customer Photo 2 (Baby Krisha) */
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
              (0,O.jsx)(`p`,{className:`caps text-[0.56rem] font-bold text-ink tracking-wider`,children:`Sweet Memories`}),
              (0,O.jsx)(`p`,{className:`text-[0.5rem] text-sepia/70 mt-0.5 tracking-wide`,children:`Family Moments`})
            ]})
          ]
        })
      ]
    })})
  ]});
}

/* Floating Audio / Music Player Component (Item 6) */
function MusicButton_(){
  let [isPlaying, setIsPlaying] = (0,b.useState)(false);

  (0,b.useEffect)(()=>{
    let handler = (e)=>{ setIsPlaying(e.detail); };
    window.addEventListener(`musicstatus`, handler);
    let audio = getGlobalAudio();
    if(audio && !audio.paused){
      setIsPlaying(true);
    }
    return ()=>window.removeEventListener(`musicstatus`, handler);
  },[]);

  let toggleMusic = ()=>{
    E_();
    let audio = getGlobalAudio();
    if(audio){
      if(!audio.paused){
        audio.pause();
        setIsPlaying(false);
      } else {
        audio.play().then(()=>setIsPlaying(true)).catch(()=>{});
      }
    }
  };

  return (0,O.jsx)(`button`,{
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

/* Assemble sections cleanly without LanguageToggle_ (Item 1) */
function I_(){
  M_();
  let[e,t]=(0,b.useState)(!1);
  return(0,O.jsxs)(O.Fragment,{children:[
    (0,O.jsx)(__,{onOpen:()=>t(!0)}),
    (0,O.jsx)(w_,{}),
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

s_i = c.find('function I_(){')
e_i = c.find('var L_={IndexRoute:', s_i)
assert s_i != -1 and e_i != -1, "I_ boundaries not found"
c = c[:s_i] + additional_components + c[e_i:]

# Ensure any route or fallback renders the invitation page I_ without 404
c = c.replace('notFoundComponent:oa', 'notFoundComponent:I_')

# Bypass missing lenis module so there are no unhandled promise rejections
c = c.replace('function M_(){', 'function M_(){return; /* lenis bypassed */ ')

with open('assets/index-2d1L6cXj.js', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: Clean v2 bundle successfully generated!")
