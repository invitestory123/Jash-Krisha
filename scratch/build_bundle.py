# scratch/build_bundle.py
import re

with open('assets/index-2d1L6cXj.js.bak', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update $ definition to include events, images, audio, invitationLine, romanticQuote, monogram
old_dollar = 'closing:_wi.closing??_w.closing??`See you there`}'
new_dollar = (
    'closing:_wi.closing??_w.closing??`See you there`,'
    'events:_w.events||[],'
    'images:_wm,'
    'audio:_w.audio||{},'
    'invitationLine:_we.invitationLine||`Together with their families, invite you to celebrate the wedding of`,'
    'romanticQuote:_we.romanticQuote||`Two lives, two hearts, joined together in friendship, united forever in love.`,'
    'monogram:_wc.monogram||((_wc.bride||_w.bride||"D")[0]+" & "+(_wc.groom||_w.groom||"D")[0])||"D & D"}'
)

assert old_dollar in content, "Could not find old_dollar"
content = content.replace(old_dollar, new_dollar, 1)

# 2. Update __ (wax seal monogram and names)
old_monogram = ',i=`${$.groom[0]}${$.bride[0]}`;'
new_monogram = ',i=$.monogram||"D & D";'
assert old_monogram in content, "Could not find old_monogram"
content = content.replace(old_monogram, new_monogram, 1)

# In envelope text: $.groom,` & `,$.bride -> $.bride,` & `,$.groom
old_env_names = '[$.groom,` & `,$.bride]'
new_env_names = '[$.bride,` & `,$.groom]'
assert old_env_names in content, "Could not find old_env_names"
content = content.replace(old_env_names, new_env_names, 1)

# 3. Update b_ (Hero section):
old_hero_line = 'children:`Join us for the engagement party of`'
new_hero_line = 'children:$.invitationLine||`Together with their families, invite you to celebrate the wedding of`'
assert old_hero_line in content, "Could not find old_hero_line"
content = content.replace(old_hero_line, new_hero_line, 1)

# In hero heading: names order: Diya first, then Debanu
old_hero_names = '[(0,O.jsx)(Zg,{text:$.groom,delay:.85,trigger:l}),(0,O.jsx)(`span`,{className:`mx-3 text-gold sm:mx-5`,children:`&`}),(0,O.jsx)(Zg,{text:$.bride,delay:1.2,trigger:l})]'
new_hero_names = '[(0,O.jsx)(Zg,{text:$.bride,delay:.85,trigger:l}),(0,O.jsx)(`span`,{className:`mx-3 text-gold sm:mx-5`,children:`&`}),(0,O.jsx)(Zg,{text:$.groom,delay:1.2,trigger:l})]'
assert old_hero_names in content, "Could not find old_hero_names"
content = content.replace(old_hero_names, new_hero_names, 1)

# In hero couple image alt text:
old_hero_alt = 'alt:`Illustration of ${$.groom} and ${$.bride} holding photo frames`'
new_hero_alt = 'alt:`Illustration of ${$.bride} and ${$.groom}`'
assert old_hero_alt in content, "Could not find old_hero_alt"
content = content.replace(old_hero_alt, new_hero_alt, 1)

# 4. In S_ (Footer): names order: Diya & Debanu
old_footer_names = '[(0,O.jsx)(Zg,{text:$.groom}),(0,O.jsx)(`span`,{className:`mx-3 text-gold`,children:`&`}),(0,O.jsx)(Zg,{text:$.bride,delay:.3})]'
new_footer_names = '[(0,O.jsx)(Zg,{text:$.bride}),(0,O.jsx)(`span`,{className:`mx-3 text-gold`,children:`&`}),(0,O.jsx)(Zg,{text:$.groom,delay:.3})]'
assert old_footer_names in content, "Could not find old_footer_names"
content = content.replace(old_footer_names, new_footer_names, 1)

# 5. In D_ (Venue): enhance to show main venue + All 3 Event Venues Directory
old_venue = '''function D_(){return(0,O.jsxs)(`section`,{className:`px-6 pb-20 text-center sm:pb-28`,children:[(0,O.jsxs)(Xg,{children:[(0,O.jsx)(Yg,{className:`mb-10`}),(0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive`,children:`The venue`}),(0,O.jsx)(`h2`,{className:`script mt-4 text-4xl text-ink sm:text-5xl`,children:$.venue.name}),(0,O.jsx)(`p`,{className:`mx-auto mt-3 max-w-xs text-base leading-relaxed text-sepia`,children:$.venue.address})]}),(0,O.jsx)(Xg,{delay:.15,children:(0,O.jsx)(Q.a,{href:Vg,target:`_blank`,rel:`noreferrer`,onClick:E_,whileTap:{scale:.985},className:`grain group mx-auto mt-8 block max-w-md overflow-hidden rounded-sm border border-border shadow-[0_20px_40px_-34px_rgba(60,45,25,0.75)]`,children:(0,O.jsxs)(`div`,{className:`relative`,children:[(0,O.jsx)(`img`,{src:T_,alt:`Map showing the location of ${$.venue.name}`,width:1024,height:768,loading:`lazy`,className:`h-52 w-full object-cover transition-transform duration-[1.2s] ease-out group-hover:scale-[1.04] sm:h-60`}),(0,O.jsx)(Q.span,{"aria-hidden":`true`,className:`absolute left-1/2 top-1/2 size-3 -translate-x-1/2 -translate-y-1/2 rounded-full bg-gold ring-8 ring-gold/20`,animate:{scale:[1,1.35,1],opacity:[1,.75,1]},transition:{duration:2.4,repeat:1/0,ease:`easeInOut`}}),(0,O.jsx)(`span`,{className:`caps absolute bottom-3 left-1/2 flex min-h-11 -translate-x-1/2 items-center rounded-full bg-paper/85 px-5 text-[0.5rem] text-ink backdrop-blur-sm`,children:`Open in maps`})]})})}),(0,O.jsx)(Xg,{delay:.25,children:(0,O.jsx)(Q.a,{href:Hg,target:`_blank`,rel:`noreferrer`,onClick:E_,whileTap:{scale:.96},className:`caps mt-6 inline-flex min-h-14 items-center gap-2 rounded-full border border-ink/25 px-8 text-[0.55rem] text-ink transition-colors duration-500 hover:border-ink hover:bg-ink hover:text-paper`,children:`Get directions`})})]})}'''

new_venue = '''function D_(){
  return(0,O.jsxs)(`section`,{id:`venue-section`,className:`px-6 pb-20 text-center sm:pb-28 max-w-4xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-10`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive`,children:`The Wedding Venue`}),
      (0,O.jsx)(`h2`,{className:`script mt-4 text-4xl text-ink sm:text-5xl`,children:$.venue.name}),
      (0,O.jsx)(`p`,{className:`mx-auto mt-3 max-w-xs text-base leading-relaxed text-sepia`,children:$.venue.address}),
      (0,O.jsx)(`p`,{className:`caps mt-1 text-[0.52rem] text-gold tracking-widest font-semibold`,children:`AGARTALA, TRIPURA`})
    ]}),
    (0,O.jsx)(Xg,{delay:.15,children:(0,O.jsx)(Q.a,{
      href:Vg,
      target:`_blank`,
      rel:`noopener noreferrer`,
      onClick:E_,
      whileTap:{scale:.985},
      className:`grain group mx-auto mt-8 block max-w-md overflow-hidden rounded-2xl border border-gold/40 shadow-[0_20px_45px_-30px_rgba(60,45,25,0.7)] transition-all duration-500 hover:border-gold`,
      children:(0,O.jsxs)(`div`,{className:`relative`,children:[
        (0,O.jsx)(`img`,{src:T_,alt:`Map showing the location of ${$.venue.name}`,width:1024,height:768,loading:`lazy`,className:`h-56 w-full object-cover transition-transform duration-[1.2s] ease-out group-hover:scale-[1.04] sm:h-64`}),
        (0,O.jsx)(Q.span,{"aria-hidden":`true`,className:`absolute left-1/2 top-1/2 size-3.5 -translate-x-1/2 -translate-y-1/2 rounded-full bg-gold ring-8 ring-gold/25`,animate:{scale:[1,1.4,1],opacity:[1,.7,1]},transition:{duration:2.4,repeat:1/0,ease:`easeInOut`}}),
        (0,O.jsx)(`span`,{className:`caps absolute bottom-4 left-1/2 flex min-h-11 -translate-x-1/2 items-center rounded-full bg-paper/90 px-6 text-[0.52rem] text-ink shadow-md backdrop-blur-md border border-gold/30`,children:`View on Google Maps`})
      ]})
    })}),
    (0,O.jsx)(Xg,{delay:.22,children:(0,O.jsx)(Q.a,{
      href:Hg,
      target:`_blank`,
      rel:`noopener noreferrer`,
      onClick:E_,
      whileTap:{scale:.96},
      className:`caps mt-6 inline-flex min-h-14 items-center gap-2 rounded-full bg-ink px-9 text-[0.55rem] text-paper shadow-md transition-all duration-500 hover:opacity-90 hover:scale-[1.02]`,
      children:`Get Directions to Manikya Enclave`
    })}),
    /* All 3 Event Venues Directory */
    (0,O.jsxs)(Xg,{delay:.3,children:[
      (0,O.jsx)(`div`,{className:`mt-14 pt-8 border-t border-gold/25`,children:(0,O.jsx)(`p`,{className:`caps text-[0.58rem] text-olive tracking-[0.2em] font-medium`,children:`All Celebration Venues`})}),
      (0,O.jsx)(`div`,{className:`mt-6 grid grid-cols-1 sm:grid-cols-3 gap-4 text-left`,children:($.events||[]).map(e=>(
        (0,O.jsxs)(`div`,{key:e.id,className:`venue-mini-card relative flex flex-col justify-between p-4 rounded-xl border border-gold/30 bg-paper/60 backdrop-blur-sm`,children:[
          (0,O.jsxs)(`div`,{children:[
            (0,O.jsx)(`span`,{className:`caps text-[0.48rem] text-gold tracking-widest font-semibold block`,children:e.dateLabel}),
            (0,O.jsx)(`h4`,{className:`caps text-[0.65rem] font-bold text-ink mt-1 tracking-wider`,children:e.name}),
            (0,O.jsx)(`p`,{className:`script text-xl text-sepia mt-1`,children:e.venueName}),
            (0,O.jsx)(`p`,{className:`text-xs text-sepia/75 mt-0.5`,children:e.venueCity||`Agartala, Tripura`}),
            (0,O.jsx)(`p`,{className:`caps text-[0.48rem] text-olive mt-1.5`,children:e.time})
          ]}),
          (0,O.jsx)(`a`,{
            href:e.directionsUrl||Hg,
            target:`_blank`,
            rel:`noopener noreferrer`,
            className:`caps mt-3 inline-flex items-center justify-center min-h-9 rounded-full border border-ink/20 px-3 text-[0.46rem] text-ink hover:bg-ink hover:text-paper transition-colors`,
            children:`Get Directions`
          })
        ]})
      ))})
    ]})
  ]})
}'''

assert old_venue in content, "Could not find old_venue"
content = content.replace(old_venue, new_venue, 1)

# 6. Additional components: RoseNode_, Timeline_, PhotoSection_, MusicButton_
additional_components = '''
/* Rose Floral Icon node for Wedding event on vertical timeline (inspired by Reference 1) */
function RoseNode_({className="size-10"}){
  return(0,O.jsxs)(`svg`,{
    viewBox:`0 0 64 64`,
    fill:`none`,
    className:`${className} timeline-node-rose shrink-0`,
    "aria-hidden":`true`,
    children:[
      (0,O.jsx)(`circle`,{cx:`32`,cy:`32`,r:`28`,fill:`#FBF7F0`,stroke:`#D4AF37`,strokeWidth:`1.2`,opacity:`0.95`}),
      (0,O.jsx)(`circle`,{cx:`32`,cy:`32`,r:`24`,fill:`#FDF2F4`,opacity:`0.9`}),
      (0,O.jsx)(`path`,{d:`M32 14 C39 14 47 20 47 29 C47 38 39 46 32 48 C25 46 17 38 17 29 C17 20 25 14 32 14Z`,fill:`#ECA4AD`,opacity:`0.85`}),
      (0,O.jsx)(`path`,{d:`M20 25 C14 31 16 41 24 45 C32 49 42 45 45 37 C48 29 42 21 34 19`,fill:`#E28C96`,opacity:`0.75`}),
      (0,O.jsx)(`path`,{d:`M32 20 C37 20 43 25 43 32 C43 38 37 44 32 45 C27 44 21 38 21 32 C21 25 27 20 32 20Z`,fill:`#D86F7D`,opacity:`0.9`}),
      (0,O.jsx)(`path`,{d:`M32 24 C35 24 39 27.5 39 32 C39 36 35 39.5 32 40 C29 39.5 25 36 25 32 C25 27.5 29 24 32 24Z`,fill:`#BF4D5C`}),
      (0,O.jsx)(`circle`,{cx:`32`,cy:`32`,r:`3.5`,fill:`#8E2434`}),
      (0,O.jsx)(`path`,{d:`M19 37 C15 39 11 37 9 33 C11 29 15 31 17 33`,stroke:`#7A8B68`,strokeWidth:`1.5`,fill:`#9FB28B`,opacity:`0.95`}),
      (0,O.jsx)(`path`,{d:`M45 37 C49 39 53 37 55 33 C53 29 49 31 47 33`,stroke:`#7A8B68`,strokeWidth:`1.5`,fill:`#9FB28B`,opacity:`0.95`})
    ]
  })
}

/* Schedule of Events Vertical Timeline Component (Customer Reference 1 inspired) */
function Timeline_(){
  let events = $.events && $.events.length ? $.events : [
    {
      id:`ashirbad`,
      name:`ASHIRBAD CEREMONY`,
      dateLabel:`14 DECEMBER 2026`,
      time:`11:00 AM – 5:00 PM`,
      venueName:`Swarnabhumi Banquet`,
      venueCity:`Agartala, Tripura`,
      badge:`Blessings & Rituals`,
      isMain:false,
      directionsUrl:`https://www.google.com/maps/search/?api=1&query=Swarnabhumi+Banquet+Agartala+Tripura`
    },
    {
      id:`wedding`,
      name:`WEDDING`,
      dateLabel:`26 JANUARY 2027`,
      time:`7:00 PM onwards`,
      venueName:`The Manikya Enclave`,
      venueCity:`Agartala, Tripura`,
      badge:`The Sacred Union`,
      isMain:true,
      directionsUrl:`https://maps.app.goo.gl/WpkDsBzRRQDXwznP8?g_st=iw`
    },
    {
      id:`reception`,
      name:`RECEPTION PARTY`,
      dateLabel:`29 JANUARY 2027`,
      time:`7:00 PM onwards`,
      venueName:`Malancha Niwas`,
      venueCity:`Agartala, Tripura`,
      badge:`Grand Celebration`,
      isMain:false,
      directionsUrl:`https://www.google.com/maps/search/?api=1&query=Malancha+Niwas+Agartala+Tripura`
    }
  ];

  return(0,O.jsxs)(`section`,{id:`schedule-of-events`,className:`px-5 py-20 text-center sm:py-28 max-w-3xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-8`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive tracking-[0.25em]`,children:`Celebration Itinerary`}),
      (0,O.jsxs)(`div`,{className:`mt-3 flex items-center justify-center gap-3 sm:gap-4`,children:[
        (0,O.jsx)(f_,{className:`w-20 sm:w-28 text-gold/60 rotate-180 shrink-0`}),
        (0,O.jsx)(`h2`,{className:`script text-4xl sm:text-6xl text-ink leading-tight`,children:`Schedule of Events`}),
        (0,O.jsx)(f_,{className:`w-20 sm:w-28 text-gold/60 shrink-0`})
      ]}),
      (0,O.jsx)(`p`,{className:`caps mt-2 text-[0.5rem] tracking-[0.22em] text-sepia/80`,children:`THREE DAYS OF LOVE, LAUGHTER & AUSPICIOUS MOMENTS`})
    ]}),

    (0,O.jsx)(Xg,{delay:.18,children:(0,O.jsxs)(`div`,{
      className:`timeline-card mt-12 sm:mt-16 rounded-3xl p-6 sm:p-12 relative overflow-hidden text-left`,
      children:[
        (0,O.jsx)(u_,{className:`absolute top-2 left-2 size-12 text-gold/30 pointer-events-none`}),
        (0,O.jsx)(u_,{className:`absolute top-2 right-2 size-12 -scale-x-100 text-gold/30 pointer-events-none`}),
        (0,O.jsx)(u_,{className:`absolute bottom-2 left-2 size-12 -scale-y-100 text-gold/30 pointer-events-none`}),
        (0,O.jsx)(u_,{className:`absolute bottom-2 right-2 size-12 -scale-100 text-gold/30 pointer-events-none`}),

        (0,O.jsx)(`div`,{className:`timeline-spine`}),

        (0,O.jsx)(`div`,{className:`space-y-12 sm:space-y-16 relative z-10`,children:events.map((ev, idx)=>(
          (0,O.jsxs)(`div`,{
            key:ev.id||idx,
            className:`relative flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 sm:gap-8 group`,
            children:[
              (0,O.jsxs)(`div`,{
                className:`sm:w-[42%] text-left sm:text-right pl-12 sm:pl-0`,
                children:[
                  (0,O.jsx)(`p`,{className:`caps text-[0.58rem] sm:text-[0.62rem] text-gold tracking-widest font-bold`,children:ev.dateLabel}),
                  (0,O.jsx)(`p`,{className:`font-serif text-lg sm:text-2xl text-ink font-semibold mt-0.5 tracking-tight`,children:ev.time}),
                  (0,O.jsx)(`p`,{className:`text-xs italic text-sepia/75 mt-0.5`,children:ev.dayLine||``})
                ]
              }),

              (0,O.jsx)(`div`,{
                className:`absolute sm:relative left-1 sm:left-auto top-1 sm:top-auto flex items-center justify-center z-20`,
                children: ev.isMain ? (
                  (0,O.jsx)(RoseNode_,{className:`size-11 sm:size-12`})
                ) : (
                  (0,O.jsx)(`span`,{
                    className:`size-4 rotate-45 border-2 border-gold bg-paper shadow-sm transition-transform duration-300 group-hover:scale-125`
                  })
                )
              }),

              (0,O.jsxs)(`div`,{
                className:`timeline-event-box sm:w-[42%] pl-12 sm:pl-0 text-left rounded-2xl ${ev.isMain ? `p-4 sm:p-5 border border-gold/45 bg-paper/80 shadow-md` : `p-2`}`,
                children:[
                  ev.badge && (0,O.jsx)(`span`,{
                    className:`caps inline-block rounded-full px-2.5 py-0.5 text-[0.45rem] font-semibold tracking-widest ${ev.isMain ? `bg-gold/20 text-ink border border-gold/40` : `bg-olive/15 text-olive`}`,
                    children:ev.badge
                  }),
                  (0,O.jsx)(`h3`,{
                    className:`caps text-base sm:text-lg font-bold text-ink mt-1 tracking-wider`,
                    children:ev.name
                  }),
                  (0,O.jsx)(`p`,{
                    className:`script text-2xl sm:text-3xl text-sepia mt-1`,
                    children:ev.venueName
                  }),
                  (0,O.jsx)(`p`,{
                    className:`text-xs text-sepia/80 mt-0.5`,
                    children:ev.venueCity||`Agartala, Tripura`
                  }),
                  ev.description && (0,O.jsx)(`p`,{
                    className:`text-xs italic text-ink/70 mt-2 max-w-xs leading-relaxed`,
                    children:ev.description
                  }),
                  (0,O.jsx)(`a`,{
                    href:ev.directionsUrl||Hg,
                    target:`_blank`,
                    rel:`noopener noreferrer`,
                    onClick:E_,
                    className:`caps mt-3 inline-flex items-center gap-1.5 text-[0.48rem] font-medium text-gold hover:text-ink transition-colors`,
                    children:[`View on Maps →`]
                  })
                ]
              })
            ]
          })
        ))})
      ]
    })})
  ]});
}

/* Dedicated Couple Story & Photo Placeholders Section */
function PhotoSection_(){
  let images = $.images || {};
  let bridePhoto = images.bridePhoto || ``;
  let groomPhoto = images.groomPhoto || ``;

  return(0,O.jsxs)(`section`,{id:`couple-story`,className:`px-6 py-20 text-center sm:py-28 max-w-4xl mx-auto`,children:[
    (0,O.jsxs)(Xg,{children:[
      (0,O.jsx)(Yg,{className:`mb-8`}),
      (0,O.jsx)(`p`,{className:`caps text-[0.6rem] text-olive tracking-[0.25em]`,children:`Moments of Love & Devotion`}),
      (0,O.jsx)(`h2`,{className:`script mt-3 text-4xl sm:text-6xl text-ink leading-tight`,children:`Two Hearts, One Journey`}),
      (0,O.jsx)(`p`,{
        className:`mx-auto mt-4 max-w-lg text-base sm:text-lg leading-relaxed text-sepia italic`,
        children:$.romanticQuote || `Two lives, two hearts, joined together in friendship, united forever in love.`
      })
    ]}),

    (0,O.jsx)(Xg,{delay:.18,children:(0,O.jsxs)(`div`,{
      className:`mt-12 grid grid-cols-1 sm:grid-cols-2 gap-8 items-stretch`,
      children:[
        /* Bride Portrait Card */
        (0,O.jsxs)(`div`,{
          className:`photo-card rounded-2xl border border-gold/40 bg-paper-deep/50 p-6 sm:p-8 text-center shadow-lg relative overflow-hidden flex flex-col justify-between transition-all duration-500 hover:shadow-xl`,
          children:[
            (0,O.jsx)(`span`,{className:`caps text-[0.52rem] text-gold tracking-[0.25em] font-semibold block mb-2`,children:`THE BRIDE`}),
            (0,O.jsx)(`h3`,{className:`script text-3xl sm:text-4xl text-ink mb-4`,children:$.bride}),
            (0,O.jsx)(`div`,{
              className:`photo-slot-border aspect-[4/5] rounded-xl flex flex-col items-center justify-center p-4 relative overflow-hidden group`,
              children: bridePhoto ? (
                (0,O.jsx)(`img`,{
                  src:bridePhoto,
                  alt:`Portrait of ${$.bride}`,
                  className:`size-full object-cover rounded-lg transition-transform duration-700 group-hover:scale-105`
                })
              ) : (
                (0,O.jsxs)(`div`,{
                  className:`flex flex-col items-center justify-center text-sepia/70 p-4`,
                  children:[
                    (0,O.jsxs)(`svg`,{
                      className:`size-14 text-gold/75 mb-3 transition-transform duration-500 group-hover:scale-110`,
                      viewBox:`0 0 24 24`,
                      fill:`none`,
                      stroke:`currentColor`,
                      strokeWidth:`1.2`,
                      children:[
                        (0,O.jsx)(`rect`,{x:`3`,y:`3`,width:`18`,height:`18`,rx:`4`}),
                        (0,O.jsx)(`circle`,{cx:`12`,cy:`10`,r:`3`}),
                        (0,O.jsx)(`path`,{d:`M7 21v-2a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v2`})
                      ]
                    }),
                    (0,O.jsx)(`p`,{className:`caps text-[0.56rem] text-ink/80 font-bold tracking-wider`,children:`Bride Portrait Slot`}),
                    (0,O.jsx)(`p`,{className:`text-xs italic text-sepia/65 mt-1 max-w-[210px]`,children:`Reserved for Diya Saha's photograph`}),
                    (0,O.jsx)(`span`,{className:`caps mt-3 inline-block rounded-full border border-gold/40 px-3 py-1 text-[0.45rem] text-gold tracking-widest`,children:`Photo arriving soon`})
                  ]
                })
              )
            }),
            (0,O.jsx)(`p`,{className:`caps text-[0.5rem] text-sepia/70 mt-4 tracking-widest`,children:`Diya Saha`})
          ]
        }),

        /* Groom Portrait Card */
        (0,O.jsxs)(`div`,{
          className:`photo-card rounded-2xl border border-gold/40 bg-paper-deep/50 p-6 sm:p-8 text-center shadow-lg relative overflow-hidden flex flex-col justify-between transition-all duration-500 hover:shadow-xl`,
          children:[
            (0,O.jsx)(`span`,{className:`caps text-[0.52rem] text-gold tracking-[0.25em] font-semibold block mb-2`,children:`THE GROOM`}),
            (0,O.jsx)(`h3`,{className:`script text-3xl sm:text-4xl text-ink mb-4`,children:$.groom}),
            (0,O.jsx)(`div`,{
              className:`photo-slot-border aspect-[4/5] rounded-xl flex flex-col items-center justify-center p-4 relative overflow-hidden group`,
              children: groomPhoto ? (
                (0,O.jsx)(`img`,{
                  src:groomPhoto,
                  alt:`Portrait of ${$.groom}`,
                  className:`size-full object-cover rounded-lg transition-transform duration-700 group-hover:scale-105`
                })
              ) : (
                (0,O.jsxs)(`div`,{
                  className:`flex flex-col items-center justify-center text-sepia/70 p-4`,
                  children:[
                    (0,O.jsxs)(`svg`,{
                      className:`size-14 text-gold/75 mb-3 transition-transform duration-500 group-hover:scale-110`,
                      viewBox:`0 0 24 24`,
                      fill:`none`,
                      stroke:`currentColor`,
                      strokeWidth:`1.2`,
                      children:[
                        (0,O.jsx)(`rect`,{x:`3`,y:`3`,width:`18`,height:`18`,rx:`4`}),
                        (0,O.jsx)(`circle`,{cx:`12`,cy:`10`,r:`3`}),
                        (0,O.jsx)(`path`,{d:`M7 21v-2a4 4 0 0 1 4-4h2a4 4 0 0 1 4 4v2`})
                      ]
                    }),
                    (0,O.jsx)(`p`,{className:`caps text-[0.56rem] text-ink/80 font-bold tracking-wider`,children:`Groom Portrait Slot`}),
                    (0,O.jsx)(`p`,{className:`text-xs italic text-sepia/65 mt-1 max-w-[210px]`,children:`Reserved for Debanu Das's photograph`}),
                    (0,O.jsx)(`span`,{className:`caps mt-3 inline-block rounded-full border border-gold/40 px-3 py-1 text-[0.45rem] text-gold tracking-widest`,children:`Photo arriving soon`})
                  ]
                })
              )
            }),
            (0,O.jsx)(`p`,{className:`caps text-[0.5rem] text-sepia/70 mt-4 tracking-widest`,children:`Debanu Das`})
          ]
        })
      ]
    })})
  ]});
}

/* Floating Audio / Music Player Component (Reference 1 inspired) */
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
    "aria-label":isPlaying ? `Pause background melody` : `Play wedding melody`,
    className:`floating-music-btn`,
    title:isPlaying ? `Pause wedding music` : `Play wedding music`,
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

# 7. Update I_() to include PhotoSection_, Timeline_, and MusicButton_
old_I = '''function I_(){M_();let[e,t]=(0,b.useState)(!1);return(0,O.jsxs)(O.Fragment,{children:[(0,O.jsx)(__,{onOpen:()=>t(!0)}),(0,O.jsx)(w_,{}),(0,O.jsxs)(`main`,{className:`grain relative min-h-screen bg-paper text-ink`,style:{backgroundImage:`url(${ua})`,backgroundSize:`480px`},children:[(0,O.jsx)(b_,{ready:e}),(0,O.jsx)(C_,{}),(0,O.jsx)(r_,{}),(0,O.jsx)(D_,{}),(0,O.jsx)($g,{}),(0,O.jsx)(S_,{})]}),(0,O.jsx)(Jg,{})]})}'''

new_I = additional_components + '''
function I_(){
  M_();
  let[e,t]=(0,b.useState)(!1);
  return(0,O.jsxs)(O.Fragment,{children:[
    (0,O.jsx)(__,{onOpen:()=>t(!0)}),
    (0,O.jsx)(w_,{}),
    (0,O.jsxs)(`main`,{className:`grain relative min-h-screen bg-paper text-ink`,style:{backgroundImage:`url(${ua})`,backgroundSize:`480px`},children:[
      (0,O.jsx)(b_,{ready:e}),
      (0,O.jsx)(C_,{}),
      (0,O.jsx)(PhotoSection_,{}),
      (0,O.jsx)(r_,{}),
      (0,O.jsx)(Timeline_,{}),
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

print("SUCCESS: assets/index-2d1L6cXj.js has been completely updated!")
