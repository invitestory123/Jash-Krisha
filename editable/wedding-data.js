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
    groomParents: "Son of Urmilaben & Jigneshbhai Harjibhai Patel",
    brideParents: "Daughter of Vaishaliben & Piyushbhai Karshanbhai Patel",
  },

  // Event Details (Engagement Ceremony)
  event: {
    title: "Engagement Ceremony",
    eventTitle: "Engagement of Jash & Krisha",
    dateLabel: "13.11.26",
    displayDate: "13 November 2026",
    dayLine: "Friday, 13th November 2026",
    timeLine: "9:00 AM",
    // Start and end ISO local time strings (IST +05:30) for countdown & calendar
    start: "2026-11-13T09:00:00",
    end: "2026-11-13T13:00:00",
    timeZoneOffset: "+05:30",
    invitationLine: "Cordially invite you to celebrate the Engagement Ceremony of",
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
      parents: "Urmilaben & Jigneshbhai Harjibhai Patel",
      location: "Manund",
    },
    brideSide: {
      name: "Krisha",
      relation: "Daughter of",
      parents: "Vaishaliben & Piyushbhai Karshanbhai Patel",
      location: "Balisana",
    },
  },

  // Invitation Notes & Closing
  invitation: {
    note: "With the divine blessings of family and elders, Urmilaben & Jigneshbhai Patel and Vaishaliben & Piyushbhai Patel families warmly invite you to grace the auspicious Engagement Ceremony of Jash and Krisha.",
    closing: "With best compliments from Patel Family",
  },

  // Venue Details
  venue: {
    name: "Khamalaimata Temple",
    address: "Manund, Gujarat 384260",
    city: "Manund",
    state: "Gujarat",
    pincode: "384260",
    query: "Khamalaimata Temple, Manund, Gujarat 384260",
    directionsUrl: "",
    mapSearchUrl: "",
  },

  // Image Assets
  images: {
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
