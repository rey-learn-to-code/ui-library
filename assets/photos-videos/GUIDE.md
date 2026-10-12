# Free photos & videos: Unsplash, Pexels, Pixabay — how to use them (links only)

Status in this library: **link-only**. We don't bulk-download photos or videos into the library, because all 3 sites forbid copying their collections to build a similar service, and their APIs forbid bulk downloading. The right way: search for and download one image at a time when you need it, or call the API directly from your website.

The license pages and API docs were checked on 2026-10-09. This is a summary for reference, not legal advice. Only the full license text on the original site is legally binding.

---

## 1. Unsplash — https://unsplash.com/

### Finding photos
- Type English keywords into the search box (e.g. `office workspace`, `vietnam street`). Filter by orientation (landscape/portrait/square) and color, and sort by Relevance/Newest.
- **Avoid photos labeled Unsplash+**: these belong to the paid plan and use a separate license (the Unsplash+ License), not the free one.
- Click "Download free" to get the original; you can pick a size.

### License (https://unsplash.com/license)
- Allowed: download and use **for free**, for both commercial and non-commercial work; **no permission needed**; credit is not required but is appreciated.
- Not allowed: **selling photos without significant changes**; **collecting photos from Unsplash to build a similar or competing service**.
- Example credit: `Photo by <Author name> on Unsplash`.

### Using the Unsplash API on a website
(An "API" is a way for your website to ask another service for data, like ordering from a menu.)
1. Sign up for a developer account at https://unsplash.com/developers, go to **Your apps → New Application**, and accept the API terms. You'll get an **Access Key**.
2. New apps start in **Demo mode: 50 requests/hour**. When you want to go to Production, click "Apply for Production". If approved, the limit rises to **1,000 requests/hour** (per the API docs).
3. Calling the API: header `Authorization: Client-ID <ACCESS_KEY>`, for example `GET https://api.unsplash.com/search/photos?query=coffee&per_page=12`.
4. **Mandatory rules** (Unsplash API Guidelines):
   - **Hotlinking**: you must use the image URLs the API returns in `photo.urls.*` directly. Don't download the images and host them yourself. You can add resize parameters such as `&w=1200&q=80`.
   - When a user "uses" a photo (sets it as a cover, inserts it into a post…), you must send a request to `photo.links.download_location` so the download is counted.
   - **Credit**: show the author's name and Unsplash, with a link to the author's page. The links must include `?utm_source=<ten_app>&utm_medium=referral`.
   - **Keep the Access Key/Secret Key private**. If you call the API from the browser, go through a server-side proxy (e.g. a Next.js API route).
   - Don't use the name "Unsplash" as your app's name. Don't sell unedited photos. Don't copy Unsplash's core experience (wallpaper apps, unofficial clients). Don't abuse the API.

```html
<!-- Example credit -->
Photo by <a href="https://unsplash.com/@user?utm_source=my_app&utm_medium=referral">Author name</a>
on <a href="https://unsplash.com/?utm_source=my_app&utm_medium=referral">Unsplash</a>
```

---

## 2. Pexels — https://www.pexels.com/

### Finding photos/videos
- Search by keyword and choose the Photos or Videos tab. Filter by orientation, size and color. Download each file with the "Free download" button.
- Pexels videos work very well as **hero background videos** (compress them and host the optimized version yourself).

### License (https://www.pexels.com/license/)
- Allowed: use **for free**; **credit is not required** (but appreciated); editing is allowed. You can use them on websites, blogs, apps, ads, printed materials, social media, and even in templates you sell.
- Not allowed:
  - showing identifiable people in a bad or offensive light;
  - selling unedited copies (posters, prints, printed on physical products);
  - implying that the people or brands in the photo endorse your product;
  - redistributing or reselling them on other stock-photo or wallpaper platforms;
  - using them as a trademark, business name or logo.

### Using the Pexels API
1. Create a Pexels account (free) and go to https://www.pexels.com/api/ to request an API key. The page may also ask what you'll use it for; this step wasn't checked because we didn't log in. The key is free.
2. Calling the API: header `Authorization: <API_KEY>`, for example `GET https://api.pexels.com/v1/search?query=people&per_page=15`. Videos use the endpoint `https://api.pexels.com/v1/videos/...`; the old path `https://api.pexels.com/videos/` is being phased out. There is an official `pexels` library (npm).
3. **Default limits: 200 requests/hour and 20,000 requests/month.** You can ask for a free increase if you can show that you credit properly.
4. **Mandatory rules** (Guidelines in the API docs):
   - Whenever you use the API, you must show a **prominent link to Pexels** (e.g. "Photos provided by Pexels", or use their logo).
   - Credit the photographer when possible, e.g. "Photo by Name on Pexels", with a link to the photo's page.
   - Don't copy Pexels' core features (e.g. making a wallpaper app). Don't abuse or work around the request limits.
   - Keep the API key on the server side.

```html
<a href="https://www.pexels.com">Photos provided by Pexels</a>
```

---

## 3. Pixabay — https://pixabay.com/

### Finding photos/videos/music
- Has photos, vectors, illustrations, videos, music, sound effects, GIFs and 3D models. Pick the content type in the search box, then filter by orientation, size, color, or Editor's Choice.
- **Watch out for sponsored content**: search results may include paid stock photos from partners. Those are not covered by the Pixabay license.

### License (https://pixabay.com/service/license-summary/, per the Content License)
- Allowed: use **for free**, **no credit required** (but appreciated), and you may edit or combine it into new work.
- Not allowed:
  - selling or distributing content in **"standalone"** form (nearly unchanged, without added creativity);
  - using content with **identifiable trademarks, logos or brands** for commercial purposes related to goods/services (e.g. printing it on merchandise to sell);
  - using it in unethical or illegal ways (especially when identifiable people appear), or in a misleading way;
  - using it as a trademark or business name.
- Some content may still carry third-party rights (trademarks, privacy…). Users must check this themselves.

### Using the Pixabay API (https://pixabay.com/api/docs/)
1. Create a Pixabay account (free). Once logged in, your API key appears right on the API docs page.
2. Calling the API: `GET https://pixabay.com/api/?key=<KEY>&q=yellow+flowers&image_type=photo`. Videos use `https://pixabay.com/api/videos/?key=...`. There is a `lang=vi` parameter to search in Vietnamese.
3. **Limit: 100 requests / 60 seconds** (per key). You **must cache results for 24 hours**. The API is meant for requests from real people; **systematic bulk downloading is forbidden**.
4. **Hotlinking**: the image URLs returned may only be used to **temporarily show search results**. **Permanent hotlinking is forbidden**. If you want to use an image, download it to your own server first. Videos may be embedded directly, but Pixabay recommends storing them yourself.
5. When showing search results, you must tell users the photos/videos come from Pixabay.

---

## Quick comparison

| | Unsplash | Pexels | Pixabay |
|---|---|---|---|
| Cost | Free (except Unsplash+) | Free | Free (except sponsored images) |
| Credit when downloading by hand | Not required | Not required | Not required |
| Credit when using the API | **Required** (author + Unsplash + UTM) | **Required** (Pexels link; author name when possible) | Must state that the source is Pixabay |
| Hotlinking via API | **Hotlinking required** | Allowed | **Permanent hotlinking forbidden**, must download |
| Default API limits | 50/hour (demo), 1,000/hour (production) | 200/hour, 20,000/month | 100/minute, 24h cache |
| Forbidden | Selling unedited photos; building a competing service | Selling unedited copies; reposting to stock platforms; use as a trademark | Selling/distributing standalone; commercial use of content with logos; bulk downloading |

## Example AI prompt: adding live photos through an API

```text
Add an API route /api/photos?q=... to my Next.js project that calls the <Unsplash | Pexels | Pixabay> API, with the key in the env var <UNSPLASH_ACCESS_KEY | PEXELS_API_KEY | PIXABAY_API_KEY> (never exposed to the browser).
- Cache responses for <Pixabay: 24 hours | others: 1 hour>.
- A <PhotoGrid> component renders results with next/image lazy loading and shows the author name with an attribution link that follows the chosen provider's guidelines (Unsplash: add utm_source=<app_name>&utm_medium=referral and hit download_location when a user selects a photo; Pexels: a "Photos provided by Pexels" link; Pixabay: credit Pixabay and download the selected image to my own storage instead of hotlinking).
- Handle HTTP 429 (rate limit) with a friendly message.
```
