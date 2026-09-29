/**
 * wedding-data.js — Editable data layer for Marigold Bhavan
 * Configured for Jash & Krisha Engagement Ceremony
 * 
 * VERIFIED DETAILS:
 * Names: Jash & Krisha
 * Event: Engagement Ceremony
 * Date: 13 November 2026
 * Time: 9:00 AM
 * Venue: Khamalaimata Temple, Manund, Gujarat 384260
 * 
 * Jash: Son of Jigneshbhai Harjibhai Patel & Urmilaben
 * Krisha: Daughter of Piyushbhai Karshanbhai Patel & Vaishaliben
 * Languages: English + Gujarati
 */

window.WEDDING_DATA = {
  // Couple Details
  couple: {
    groom: "Jash",
    bride: "Krisha",
    groomShort: "Jash",
    brideShort: "Krisha",
    monogram: "J & K",
    groomParents: "Son of Jigneshbhai Harjibhai Patel & Urmilaben",
    brideParents: "Daughter of Piyushbhai Karshanbhai Patel & Vaishaliben",

    // Gujarati details
    groomGu: "જશ",
    brideGu: "ક્રિશા",
    groomParentsGu: "સુપુત્ર: જીગ્નેશભાઈ હરજીભાઈ પટેલ અને ઉર્મિલાબેન",
    brideParentsGu: "સુપુત્રી: પિયુષભાઈ કરશનભાઈ પટેલ અને વૈશાલીબેન",
  },

  // Event Details (Engagement Ceremony)
  event: {
    title: "Engagement Ceremony",
    titleGu: "સગાઈ મહોત્સવ",
    eventTitle: "Engagement of Jash & Krisha",
    eventTitleGu: "જશ અને ક્રિશાનો સગાઈ મહોત્સવ",
    dateLabel: "13.11.26",
    displayDate: "13 November 2026",
    displayDateGu: "૧૩ નવેમ્બર ૨૦૨૬",
    dayLine: "Friday, 13th November 2026",
    dayLineGu: "શુક્રવાર, ૧૩ નવેમ્બર ૨૦૨૬",
    timeLine: "9:00 AM",
    timeLineGu: "સવારે ૯:૦૦ કલાકે",
    // Start and end ISO local time strings (IST +05:30) for countdown & calendar
    start: "2026-11-13T09:00:00",
    end: "2026-11-13T13:00:00",
    timeZoneOffset: "+05:30",
    invitationLine: "Cordially invite you to celebrate the Engagement Ceremony of",
    invitationLineGu: "આપ સર્વે સ્નેહીજનોને સગાઈ મહોત્સવ પ્રસંગે સહર્ષ આમંત્રણ પાઠવીએ છીએ",
  },

  // Backward compatibility alias for wedding block
  wedding: {
    eventTitle: "Engagement of Jash & Krisha",
    dateLabel: "13.11.26",
    displayDate: "13 November 2026",
    dayLine: "Friday, 13th November 2026",
    timeLine: "9:00 AM",
    start: "2026-11-13T09:00:00",
    end: "2026-11-13T13:00:00",
    timeZoneOffset: "+05:30",
    invitationLine: "Cordially invite you to celebrate the Engagement Ceremony of",
  },

  // Family Details
  family: {
    groomSide: {
      name: "Jash",
      relation: "Son of",
      parents: "Jigneshbhai Harjibhai Patel & Urmilaben",
      nameGu: "જશ",
      relationGu: "સુપુત્ર",
      parentsGu: "જીગ્નેશભાઈ હરજીભાઈ પટેલ અને ઉર્મિલાબેન",
    },
    brideSide: {
      name: "Krisha",
      relation: "Daughter of",
      parents: "Piyushbhai Karshanbhai Patel & Vaishaliben",
      nameGu: "ક્રિશા",
      relationGu: "સુપુત્રી",
      parentsGu: "પિયુષભાઈ કરશનભાઈ પટેલ અને વૈશાલીબેન",
    },
  },

  // Invitation Notes & Closing
  invitation: {
    note: "With the divine blessings of family and elders, Jigneshbhai Patel & Piyushbhai Patel families warmly invite you to grace the auspicious Engagement Ceremony of Jash and Krisha.",
    noteGu: "શ્રી ગણેશાય નમઃ || કુળદેવી શ્રી ખમાલાઈ માતાજીના પરમ આશીર્વાદથી, પટેલ પરિવાર આપ સર્વે સ્નેહીજનોને જશ અને ક્રિશાના શુભ સગાઈ મહોત્સવ પ્રસંગે પધારવા ભાવભર્યું આમંત્રણ પાઠવે છે.",
    closing: "With best compliments from Patel Family",
    closingGu: "સ્નેહાધીન: પટેલ પરિવાર",
  },

  // Venue Details
  venue: {
    name: "Khamalaimata Temple",
    nameGu: "શ્રી ખમાલાઈ માતાજી મંદિર",
    address: "Manund, Gujarat 384260",
    addressGu: "મણુંદ, ગુજરાત ૩૮૪૨૬૦",
    city: "Manund",
    cityGu: "મણુંદ",
    state: "Gujarat",
    stateGu: "ગુજરાત",
    pincode: "384260",
    query: "Khamalaimata Temple, Manund, Gujarat 384260",
    // Configurable Google Maps URL (keep empty until exact customer link is provided)
    directionsUrl: "",
    mapSearchUrl: "",
  },

  // Image Assets & Replaceable Slots
  images: {
    // Couple photo slot - left empty until customer provides couple photograph
    couplePhoto: "",
    // Customer supplied photographs with respectful, contextual captions
    customerPhotos: [
      {
        id: "photo-1",
        url: "./editable/assets/customer-photo-1.jpg",
        caption: "Cherished Moments",
        captionGu: "સ્મૃતિ પળો",
      },
      {
        id: "photo-2",
        url: "./editable/assets/customer-photo-2.jpg",
        caption: "Sweet Memories",
        captionGu: "મીઠી યાદો",
      },
    ],
    // Replaceable template assets
    couple: "./editable/assets/couple.png",
    footerBg: "./editable/assets/footer-bg.jpg",
    map: "./editable/assets/map.jpg",
  },

  // Music Configuration - replaceable source, generic celebration melody
  audio: {
    enabled: true,
    url: "./editable/assets/music.mp3",
    title: "Background Music",
  },
};
