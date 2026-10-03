# Customer Editing Guide — Marigold Bhavan (Jash & Krisha Engagement Ceremony)

This template is an elegant Indian engagement invitation with an interactive wax seal gate opener, bilingual English + Gujarati support, family details, event countdown, customer photo memories with replaceable photo slots, venue directions, and an action bar.

---

## Verified Customer Configuration

All customer data is managed in:
→ [editable/wedding-data.js](file:///e:/invate%20%20story/works/Debanu%20Das/editable/wedding-data.js)

### 1. Couple Details
- `couple.groom`: `"Jash"`
- `couple.bride`: `"Krisha"`
- `couple.monogram`: `"J & K"`

### 2. Family Details
- **Groom Side**:
  - `Jash` — `Son of Urmilaben & Jigneshbhai Harjibhai Patel` (Patel Family • Manund)
- **Bride Side**:
  - `Krisha` — `Daughter of Vaishaliben & Piyushbhai Karshanbhai Patel` (Patel Family • Balisana)

### 3. Event Date & Time (Engagement Ceremony)
- Date: `13 November 2026` (Gujarati: `૧૩ નવેમ્બર ૨૦૨૬`)
- Day: `Friday, 13th November 2026` (Gujarati: `શુક્રવાર, ૧૩ નવેમ્બર ૨૦૨૬`)
- Time: `9:00 AM` (Gujarati: `સવારે ૯:૦૦ કલાકે`)
- ISO Start/End: `2026-11-13T09:00:00` / `2026-11-13T13:00:00` (IST +05:30)

### 4. Venue & Directions
- Venue: `Khamalaimata Temple` (Gujarati: `શ્રી ખમાલાઈ માતાજી મંદિર`)
- Address: `Manund, Gujarat 384260` (Gujarati: `મણુંદ, ગુજરાત ૩૮૪૨૬૦`)
- Query: `"Khamalaimata Temple, Manund, Gujarat 384260"`
- `venue.directionsUrl`: Configurable link (empty by default until customer supplies exact link; falls back safely to address search without fake links).

### 5. Photographs & Replaceable Slots
- **Couple Photo**: `images.couplePhoto` in `editable/wedding-data.js` (empty by default, displaying a clean "Ready for replacement" card until customer provides couple photo).
- **Customer Photos**:
  - `editable/assets/customer-photo-1.jpg`: Customer supplied photo (toddler with toy), respectfully labeled "Cherished Moments".
  - `editable/assets/customer-photo-2.jpg`: Customer supplied photo (toddler in magenta), respectfully labeled "Sweet Memories".
- Additional customer photos can be added directly into `images.customerPhotos` array.

### 6. Music / Audio
- `audio.enabled`: `true`
- `audio.url`: `"./editable/assets/music.mp3"`
- `audio.title`: `"Background Music"` (replaceable with any customer audio file)

---

## Languages
- Guests can toggle between **English** and **ગુજરાતી** using the floating `[ EN | ગુજરાતી ]` pill at the top right of the page.
- All headings, titles, family relations, notes, and dates update dynamically.
