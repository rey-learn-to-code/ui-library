# Heading + body font pairing ideas (with Vietnamese diacritics)

Every font below is **free** on Google Fonts (OFL/Apache license — commercial use allowed) and **has been checked for Vietnamese diacritics**: it has the `vietnamese` subset in `google-fonts/fonts-index.json`, and the actual font file contains all of the letters ạ ắ ằ ẳ ẵ ặ ơ ư ữ đ ẫ ể ỹ ỵ Ạ Ắ Ự Đ (checked with fontTools).

This list was put together for this library. Fontshare fonts aren't included yet because they couldn't be downloaded to check their diacritics (see `fontshare/NOTES.md`).

How to use: copy the `<link>` snippet into the `<head>` of your HTML file, and copy the CSS snippet into your CSS file. For Next.js, use the names in the `next/font/google` line (see `README.md` section 3).

Test sentence: *Tiếng Việt có dấu — Quý khách vui lòng đặt hàng trước 17 giờ. Ửng hồng, ngỡ ngàng, Đặng Thị Kỳ Duyên.* ("Vietnamese with diacritics — Customers, please order before 5 p.m. Blushing pink, astonished, Đặng Thị Kỳ Duyên [a personal name].")

## 1. Be Vietnam Pro + Inter

- Style: Modern, neutral. Good for: Company websites, SaaS, dashboards.
- Heading: Be Vietnam Pro (sans_serif, weight 700) — `google-fonts/repo/ofl/bevietnampro`
- Body: Inter (sans_serif) — `google-fonts/repo/ofl/inter`
- Next.js: `import { Be_Vietnam_Pro, Inter } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@700&family=Inter:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Be Vietnam Pro", sans-serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Inter", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 2. Playfair Display + Source Sans 3

- Style: Elegant, editorial. Good for: Blogs, magazines, restaurants.
- Heading: Playfair Display (serif, weight 700) — `google-fonts/repo/ofl/playfairdisplay`
- Body: Source Sans 3 (sans_serif) — `google-fonts/repo/ofl/sourcesans3`
- Next.js: `import { Playfair_Display, Source_Sans_3 } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Sans+3:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Playfair Display", serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Source Sans 3", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 3. Lora + Open Sans

- Style: Classic, long-form reading. Good for: Personal blogs, long articles.
- Heading: Lora (serif, weight 700) — `google-fonts/repo/ofl/lora`
- Body: Open Sans (sans_serif) — `google-fonts/repo/ofl/opensans`
- Next.js: `import { Lora, Open_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:wght@700&family=Open+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Lora", serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Open Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 4. Merriweather + Merriweather Sans

- Style: Newspaper. Good for: News sites, online magazines.
- Heading: Merriweather (serif, weight 900) — `google-fonts/repo/ofl/merriweather`
- Body: Merriweather Sans (sans_serif) — `google-fonts/repo/ofl/merriweathersans`
- Next.js: `import { Merriweather, Merriweather_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Merriweather:wght@900&family=Merriweather+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Merriweather", serif; font-weight: 900; line-height: 1.2; }
body { font-family: "Merriweather Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 5. Space Grotesk + IBM Plex Sans

- Style: Tech. Good for: Startups, technical products.
- Heading: Space Grotesk (sans_serif, weight 700) — `google-fonts/repo/ofl/spacegrotesk`
- Body: IBM Plex Sans (sans_serif) — `google-fonts/repo/ofl/ibmplexsans`
- Next.js: `import { Space_Grotesk, IBM_Plex_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&family=IBM+Plex+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Space Grotesk", sans-serif; font-weight: 700; line-height: 1.2; }
body { font-family: "IBM Plex Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 6. Nunito + Nunito Sans

- Style: Friendly. Good for: Education, children, community.
- Heading: Nunito (sans_serif, weight 800) — `google-fonts/repo/ofl/nunito`
- Body: Nunito Sans (sans_serif) — `google-fonts/repo/ofl/nunitosans`
- Next.js: `import { Nunito, Nunito_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@800&family=Nunito+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Nunito", sans-serif; font-weight: 800; line-height: 1.2; }
body { font-family: "Nunito Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 7. Oswald + Roboto

- Style: Bold, eye-catching. Good for: Sports, events, landing pages.
- Heading: Oswald (sans_serif, weight 600) — `google-fonts/repo/ofl/oswald`
- Body: Roboto (sans_serif) — `google-fonts/repo/ofl/roboto`
- Next.js: `import { Oswald, Roboto } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&family=Roboto:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Oswald", sans-serif; font-weight: 600; line-height: 1.2; }
body { font-family: "Roboto", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 8. Cormorant Garamond + Montserrat

- Style: Premium minimalist. Good for: Fashion, cosmetics, weddings.
- Heading: Cormorant Garamond (serif, weight 600) — `google-fonts/repo/ofl/cormorantgaramond`
- Body: Montserrat (sans_serif) — `google-fonts/repo/ofl/montserrat`
- Next.js: `import { Cormorant_Garamond, Montserrat } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Montserrat:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Cormorant Garamond", serif; font-weight: 600; line-height: 1.2; }
body { font-family: "Montserrat", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 9. EB Garamond + Noto Sans

- Style: Academic. Good for: Books, research, libraries.
- Heading: EB Garamond (serif, weight 600) — `google-fonts/repo/ofl/ebgaramond`
- Body: Noto Sans (sans_serif) — `google-fonts/repo/ofl/notosans`
- Next.js: `import { EB_Garamond, Noto_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@600&family=Noto+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "EB Garamond", serif; font-weight: 600; line-height: 1.2; }
body { font-family: "Noto Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 10. Plus Jakarta Sans + Manrope

- Style: Bright startup. Good for: Apps, fintech, landing pages.
- Heading: Plus Jakarta Sans (sans_serif, weight 800) — `google-fonts/repo/ofl/plusjakartasans`
- Body: Manrope (sans_serif) — `google-fonts/repo/ofl/manrope`
- Next.js: `import { Plus_Jakarta_Sans, Manrope } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@800&family=Manrope:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Plus Jakarta Sans", sans-serif; font-weight: 800; line-height: 1.2; }
body { font-family: "Manrope", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 11. Lexend (one font for both headings and body text)

- Style: Maximum readability. Good for: Education, content for all ages.
- Heading: Lexend (sans_serif, weight 600) — `google-fonts/repo/ofl/lexend`
- Body: Lexend (sans_serif) — `google-fonts/repo/ofl/lexend`
- Next.js: `import { Lexend } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;600;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Lexend", sans-serif; font-weight: 600; line-height: 1.2; }
body { font-family: "Lexend", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 12. Fraunces + Work Sans

- Style: Modern editorial. Good for: Creative brands, studios.
- Heading: Fraunces (serif, weight 700) — `google-fonts/repo/ofl/fraunces`
- Body: Work Sans (sans_serif) — `google-fonts/repo/ofl/worksans`
- Next.js: `import { Fraunces, Work_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:wght@700&family=Work+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Fraunces", serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Work Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 13. Bricolage Grotesque + Public Sans

- Style: Distinctive. Good for: Agencies, portfolios.
- Heading: Bricolage Grotesque (sans_serif, weight 800) — `google-fonts/repo/ofl/bricolagegrotesque`
- Body: Public Sans (sans_serif) — `google-fonts/repo/ofl/publicsans`
- Next.js: `import { Bricolage_Grotesque, Public_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@800&family=Public+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Bricolage Grotesque", sans-serif; font-weight: 800; line-height: 1.2; }
body { font-family: "Public Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 14. Crimson Pro + Literata

- Style: Literary. Good for: Stories, e-books, literary blogs.
- Heading: Crimson Pro (serif, weight 600) — `google-fonts/repo/ofl/crimsonpro`
- Body: Literata (serif) — `google-fonts/repo/ofl/literata`
- Next.js: `import { Crimson_Pro, Literata } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@600&family=Literata:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Crimson Pro", serif; font-weight: 600; line-height: 1.2; }
body { font-family: "Literata", serif; font-weight: 400; line-height: 1.65; }
```

## 15. Noto Serif + Noto Sans

- Style: Serious, trustworthy. Good for: Banks, legal, government agencies.
- Heading: Noto Serif (serif, weight 700) — `google-fonts/repo/ofl/notoserif`
- Body: Noto Sans (sans_serif) — `google-fonts/repo/ofl/notosans`
- Next.js: `import { Noto_Serif, Noto_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif:wght@700&family=Noto+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Noto Serif", serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Noto Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 16. Quicksand + Mulish

- Style: Soft. Good for: Spas, wellness, mother & baby.
- Heading: Quicksand (sans_serif, weight 700) — `google-fonts/repo/ofl/quicksand`
- Body: Mulish (sans_serif) — `google-fonts/repo/ofl/mulish`
- Next.js: `import { Quicksand, Mulish } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Quicksand:wght@700&family=Mulish:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Quicksand", sans-serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Mulish", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 17. IBM Plex Serif + IBM Plex Sans

- Style: Engineering. Good for: Technical documentation, businesses.
- Heading: IBM Plex Serif (serif, weight 600) — `google-fonts/repo/ofl/ibmplexserif`
- Body: IBM Plex Sans (sans_serif) — `google-fonts/repo/ofl/ibmplexsans`
- Next.js: `import { IBM_Plex_Serif, IBM_Plex_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:wght@600&family=IBM+Plex+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "IBM Plex Serif", serif; font-weight: 600; line-height: 1.2; }
body { font-family: "IBM Plex Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 18. Inter (one font for both headings and body text)

- Style: Developer docs. Good for: Docs, tech blogs (code: JetBrains Mono).
- Heading: Inter (sans_serif, weight 700) — `google-fonts/repo/ofl/inter`
- Body: Inter (sans_serif) — `google-fonts/repo/ofl/inter`
- Next.js: `import { Inter } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Inter", sans-serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Inter", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 19. Prata + Lato

- Style: Graceful. Good for: Hotels, real estate.
- Heading: Prata (serif, weight 400) — `google-fonts/repo/ofl/prata`
- Body: Lato (sans_serif) — `google-fonts/repo/ofl/lato`
- Next.js: `import { Prata, Lato } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Prata:wght@400&family=Lato:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Prata", serif; font-weight: 400; line-height: 1.2; }
body { font-family: "Lato", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 20. Archivo + Barlow

- Style: Energetic. Good for: Sports, logistics, industry.
- Heading: Archivo (sans_serif, weight 800) — `google-fonts/repo/ofl/archivo`
- Body: Barlow (sans_serif) — `google-fonts/repo/ofl/barlow`
- Next.js: `import { Archivo, Barlow } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@800&family=Barlow:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Archivo", sans-serif; font-weight: 800; line-height: 1.2; }
body { font-family: "Barlow", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 21. Alegreya + Alegreya Sans

- Style: Warm. Good for: Bookshops, cafés, culture.
- Heading: Alegreya (serif, weight 700) — `google-fonts/repo/ofl/alegreya`
- Body: Alegreya Sans (sans_serif) — `google-fonts/repo/ofl/alegreyasans`
- Next.js: `import { Alegreya, Alegreya_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:wght@700&family=Alegreya+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Alegreya", serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Alegreya Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 22. Roboto Slab + Roboto

- Style: Quick news reading. Good for: News, aggregator blogs.
- Heading: Roboto Slab (serif, weight 700) — `google-fonts/repo/apache/robotoslab`
- Body: Roboto (sans_serif) — `google-fonts/repo/ofl/roboto`
- Next.js: `import { Roboto_Slab, Roboto } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@700&family=Roboto:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Roboto Slab", serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Roboto", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 23. Spectral + Raleway

- Style: Refined. Good for: Photography and architecture portfolios.
- Heading: Spectral (serif, weight 600) — `google-fonts/repo/ofl/spectral`
- Body: Raleway (sans_serif) — `google-fonts/repo/ofl/raleway`
- Next.js: `import { Spectral, Raleway } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:wght@600&family=Raleway:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Spectral", serif; font-weight: 600; line-height: 1.2; }
body { font-family: "Raleway", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 24. Newsreader + Source Sans 3

- Style: Big magazine. Good for: Long-running features, longform.
- Heading: Newsreader (serif, weight 600) — `google-fonts/repo/ofl/newsreader`
- Body: Source Sans 3 (sans_serif) — `google-fonts/repo/ofl/sourcesans3`
- Next.js: `import { Newsreader, Source_Sans_3 } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:wght@600&family=Source+Sans+3:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Newsreader", serif; font-weight: 600; line-height: 1.2; }
body { font-family: "Source Sans 3", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 25. Baloo 2 + Quicksand

- Style: Playful. Good for: Food, drinks, youthful products.
- Heading: Baloo 2 (display, weight 700) — `google-fonts/repo/ofl/baloo2`
- Body: Quicksand (sans_serif) — `google-fonts/repo/ofl/quicksand`
- Next.js: `import { Baloo_2, Quicksand } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@700&family=Quicksand:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Baloo 2", sans-serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Quicksand", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 26. Onest (one font for both headings and body text)

- Style: Soft modern. Good for: Apps, online services.
- Heading: Onest (sans_serif, weight 700) — `google-fonts/repo/ofl/onest`
- Body: Onest (sans_serif) — `google-fonts/repo/ofl/onest`
- Next.js: `import { Onest } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Onest", sans-serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Onest", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 27. Josefin Sans + Lora

- Style: Geometric. Good for: Cafés, vintage brands.
- Heading: Josefin Sans (sans_serif, weight 700) — `google-fonts/repo/ofl/josefinsans`
- Body: Lora (serif) — `google-fonts/repo/ofl/lora`
- Next.js: `import { Josefin_Sans, Lora } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@700&family=Lora:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Josefin Sans", sans-serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Lora", serif; font-weight: 400; line-height: 1.65; }
```

## 28. Unbounded + Inter

- Style: Futuristic. Good for: Web3, tech, digital events.
- Heading: Unbounded (sans_serif, weight 700) — `google-fonts/repo/ofl/unbounded`
- Body: Inter (sans_serif) — `google-fonts/repo/ofl/inter`
- Next.js: `import { Unbounded, Inter } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@700&family=Inter:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Unbounded", sans-serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Inter", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 29. Dancing Script + Montserrat

- Style: Cards & invitations. Good for: Wedding cards, gifts, flower shops.
- Heading: Dancing Script (handwriting, weight 700) — `google-fonts/repo/ofl/dancingscript`
- Body: Montserrat (sans_serif) — `google-fonts/repo/ofl/montserrat`
- Next.js: `import { Dancing_Script, Montserrat } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Dancing Script", cursive; font-weight: 700; line-height: 1.2; }
body { font-family: "Montserrat", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 30. Anton + Work Sans

- Style: Extra-bold headings. Good for: Posters, promotions, banners.
- Heading: Anton (display, weight 400) — `google-fonts/repo/ofl/anton`
- Body: Work Sans (sans_serif) — `google-fonts/repo/ofl/worksans`
- Next.js: `import { Anton, Work_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton:wght@400&family=Work+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Anton", sans-serif; font-weight: 400; line-height: 1.2; }
body { font-family: "Work Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

## 31. Be Vietnam Pro + Noto Serif

- Style: Vietnamese business. Good for: Company profiles, reports.
- Heading: Be Vietnam Pro (sans_serif, weight 800) — `google-fonts/repo/ofl/bevietnampro`
- Body: Noto Serif (serif) — `google-fonts/repo/ofl/notoserif`
- Next.js: `import { Be_Vietnam_Pro, Noto_Serif } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@800&family=Noto+Serif:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Be Vietnam Pro", sans-serif; font-weight: 800; line-height: 1.2; }
body { font-family: "Noto Serif", serif; font-weight: 400; line-height: 1.65; }
```

## 32. Bitter + Fira Sans

- Style: Classic editorial. Good for: How-to blogs, study materials.
- Heading: Bitter (serif, weight 700) — `google-fonts/repo/ofl/bitter`
- Body: Fira Sans (sans_serif) — `google-fonts/repo/ofl/firasans`
- Next.js: `import { Bitter, Fira_Sans } from "next/font/google"` with `subsets: ["vietnamese", "latin"]`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bitter:wght@700&family=Fira+Sans:wght@400;700&display=swap">
```

```css
h1, h2, h3 { font-family: "Bitter", serif; font-weight: 700; line-height: 1.2; }
body { font-family: "Fira Sans", sans-serif; font-weight: 400; line-height: 1.65; }
```

---

**Font pairing tips:**

- One serif font (with little "feet" on the letters) + one sans-serif font (without them) is the safest combination.
- Use at most 2 font families per website; use weights (400/600/700) to create contrast.
- Vietnamese body text should have a `line-height` of 1.6–1.75, because the diacritics take up extra height.
- Handwriting/decorative fonts (Dancing Script, Anton) are only for short headings, not for paragraphs.
