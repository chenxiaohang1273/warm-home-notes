# Warm Home Notes

A buildless English-language home information website for US readers. The first collection covers candle warmer lamps and candle care. Production origin: **https://www.whychooseme.me**. Repository: **chenxiaohang1273/warm-home-notes**.

This edition has no affiliate shopping links, merchant relationships, invented ratings, hands-on testing claims, analytics, advertising pixels, newsletter service, contact form, accounts or backend. Fonts, styles and illustrations are local. The original SVG illustrations and PNG sharing card are conceptual drawings, not product photos.

## Modified and added files

Updated existing files: `index.html`, `README.md`. Added files:

```text
about.html
contact.html
privacy-policy.html
affiliate-disclosure.html
terms.html
404.html
guides/
  index.html
  candle-warmer-lamp-guide.html
  candle-warmer-vs-burning.html
  candle-jar-size-guide.html
  candle-warmer-safety.html
  candle-warmer-features.html
  candle-warmer-placement.html
  candle-warmer-troubleshooting.html
  candle-warmer-gift-guide.html
  candle-care-guide.html
  candle-warmer-faq.html
assets/
  css/styles.css
  js/main.js
  js/site-config.js
  images/lamp.svg
  images/comparison.svg
  images/measure.svg
  images/safety.svg
  images/controls.svg
  images/placement.svg
  images/care.svg
  images/gift.svg
  images/social-card.png
favicon.svg
robots.txt
sitemap.xml
_headers
.gitignore
tools/
  preview.py
  validate.py
```

There are 17 normal content pages plus a custom error page. The homepage contains six featured guides, editorial principles, eight checklist items, three topic entrances, six FAQ answers and a website introduction. The library links all ten articles. Navigation and footer links are present in each page's HTML and work without JavaScript. Articles include a contents list, related links, reading time, truthful preparation/revision dates and Article/BreadcrumbList JSON-LD. All pages have individual titles, descriptions, canonical URLs and Open Graph tags. Policy pages are drafts describing the current source functionality.

## The ten articles

Cloudflare Pages redirects `.html` paths to extensionless routes. Canonical URLs, links and sitemap entries use those clean routes; the source remains ordinary HTML. These are the intended production addresses. Check the deployed domain to confirm the currently published version.

| Title | Production URL | Approximate body words |
| --- | --- | ---: |
| How to Choose a Candle Warmer Lamp | https://www.whychooseme.me/guides/candle-warmer-lamp-guide | 1,102 |
| Candle Warmer Lamp vs. Burning a Candle: Key Differences | https://www.whychooseme.me/guides/candle-warmer-vs-burning | 974 |
| How to Check Candle Jar Size and Lamp Clearance | https://www.whychooseme.me/guides/candle-jar-size-guide | 957 |
| Candle Warmer Lamp Safety: Practical Tips for Everyday Use | https://www.whychooseme.me/guides/candle-warmer-safety | 980 |
| Candle Warmer Lamp Features Explained: Timer, Dimmer and Adjustable Height | https://www.whychooseme.me/guides/candle-warmer-features | 970 |
| Where to Place a Candle Warmer Lamp at Home | https://www.whychooseme.me/guides/candle-warmer-placement | 1,022 |
| Common Candle Warmer Lamp Problems and How to Troubleshoot Them | https://www.whychooseme.me/guides/candle-warmer-troubleshooting | 953 |
| Is a Candle Warmer Lamp a Good Gift? What to Consider | https://www.whychooseme.me/guides/candle-warmer-gift-guide | 937 |
| Candle Care Basics: Storage, Cleaning and Everyday Maintenance | https://www.whychooseme.me/guides/candle-care-guide | 1,012 |
| Candle Warmer Lamp FAQ: Answers to Common Questions | https://www.whychooseme.me/guides/candle-warmer-faq | 1,037 |

Content prioritizes distinct useful advice over extending every page to an arbitrary word count. Examples are illustrative; exact limits must be checked against the lamp and candle makers' instructions.

## Local preview and checks

From the repository root, using Python 3:

```sh
python tools/preview.py --port 8000
```

Open **http://127.0.0.1:8000/** and stop with Ctrl+C. The local-only server maps clean routes to HTML files, redirects `.html` addresses and prevents directory listings. Do not double-click HTML for preview: root-relative links intentionally match deployment at the origin root. Python is only a local convenience; Cloudflare needs no runtime or build step.

Run the standard-library source validator and available syntax checks:

```sh
python tools/validate.py
node --check assets/js/main.js
git diff --check
```

The validator checks local references/fragments, unique titles/descriptions, image attributes, OG image existence, canonical URLs, JSON-LD syntax, sitemap coverage, article count, replacement characters and selected credential patterns. Pattern scanning cannot prove every possible secret is absent. Never store credentials in public files. `robots.txt` is not access control or a way to protect private information.

## Cloudflare Pages deployment

Keep the existing GitHub integration and settings:

| Setting | Value |
| --- | --- |
| Framework preset | None |
| Build command | Leave blank |
| Build output directory | `.` |

No dependency install or generator is required to deploy the supplied files. Edit the HTML/CSS/JS directly. Commit through your normal GitHub workflow when ready; a push to the connected production branch may automatically deploy. This upgrade changes website source only; no remote repository settings, Cloudflare settings, DNS records or third-party account configuration are changed. Existing Git history is preserved. Verify deployment status after pushing through the existing integration.

`_headers` adds basic security headers without long-lived custom caching. `404.html` provides a genuine error response on Pages instead of its default single-page-app fallback; it is excluded from the sitemap and marked noindex. All linked content exists. The preview server is not a full emulator of Cloudflare caching, headers or edge behavior.

See [Cloudflare serving-pages documentation](https://developers.cloudflare.com/pages/configuration/serving-pages/) for route and error-page behavior. Keep canonical, OG and sitemap URLs on `www.whychooseme.me`. Check preview-domain indexing behavior before public promotion.

## Real information required before promotion

1. **A working site inbox.** In `assets/js/site-config.js`, replace only `CONTACT_EMAIL_TO_CONFIGURE` with your real email. Main JavaScript creates a safe email link only for a valid configured address. The current contact page explicitly says the channel is being configured, has no fake form and does not display the placeholder as an address. Also update the static status block in `contact.html` for users without JavaScript, and revise policies that currently say no channel is available. If adding a form instead, implement real message delivery and accurate data disclosures.
2. **Actual operator identity.** Supply the real operator details required for your location and activities. Do not invent a company, founder biography, team or address. Review the privacy/terms drafts against actual operations and obtain suitable advice where needed.
3. **Actual hosting data practices.** Check production requests, cookies, Cloudflare security/analytics settings and access-log handling. The privacy page describes supplied source, not independently verified account settings. Explain contact-message use and retention when email becomes available.
4. **Human editorial review.** Review all ten articles for English, usefulness and technical accuracy before promotion. Content was drafted with AI assistance and does not claim first-hand testing. Preserve manufacturer-specific limits and delete unsupported performance claims.
5. **Real publication dates.** Article text currently says Written/Updated October 12, 2026; JSON-LD uses `dateCreated`/`dateModified`. It does not invent `datePublished` for a public release that has not occurred. On release, add the actual publication date to the text and Article JSON-LD. Change revision dates and sitemap `lastmod` only when real changes occur.

`WHN_CONFIG` is public convenience configuration, not a secret store. Policy drafts need updating when missing information or new features are supplied.

## Validation in this development session

- Source checks passed: 18 HTML files, 10 articles, 678 local references, 17 sitemap URLs matching canonicals, unique titles/descriptions, no missing local resources/fragments and no selected credential-pattern matches.
- Chrome headless: all 17 normal routes at 1440, 768, 390 and 320 CSS pixels; 68 checks with no page overflow, JavaScript errors or failed requests. Axe WCAG 2 A/AA and 2.1 AA scans reported no automated violations. Menu, Esc focus restoration, mobile links, FAQ, checklist and contact configuration worked. Navigation and ten library cards also worked without JavaScript.
- Edge headless: all 17 routes at 1440 and 390 pixels; 34 checks passed. Keyboard skip-link and FAQ operations passed. Tested local loads made no external requests and left cookies/localStorage/sessionStorage empty.
- Mobile Lighthouse HTML/JSON reports were generated for the homepage and buying guide, delivered beside the repository. They measure localhost with simulated mobile throttling, not live Cloudflare performance. Consult the reports for scores, metrics and remaining diagnostics.
- Desktop/phone homepage and desktop article screenshots were inspected. Exact repeated body paragraphs were checked. Primary guidance was consulted for relevant safety, disclosure and hosting claims; human editorial sign-off remains required.

Automated accessibility checks do not replace a full screen-reader review. Firefox, Safari, physical iOS/Android devices, production redirects/headers, live hosting cookies, indexing and affiliate/ad account reviews were not tested. No approval or comprehensive legal compliance is promised.

## Primary guidance consulted

- [Candle Warmers Etc. FAQ](https://www.candlewarmers.com/faq/) — top-down operation and manufacturer-dependent requirements; its model claims are not universal specifications.
- [National Candle Association safety tips](https://candles.org/candle-safety-tips/) — burning-candle guidance, distinguished from electrical warmer use.
- [Cloudflare Privacy Policy](https://www.cloudflare.com/privacypolicy/) — provider processing context, not proof of this account's configuration.
- [FTC endorsement guidance](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking) — disclosure of real material connections.
- [Google Ads original-content policy](https://support.google.com/adspolicy/answer/16427718?hl=en) — useful destinations; no acceptance guarantee.

## Before release

- [ ] Configure and test real contact information, including the no-JavaScript version.
- [ ] Supply real operator details and finalize policy drafts against actual activity.
- [ ] Complete human editorial/technical review of every guide.
- [ ] Add the actual public release date; keep revision dates truthful.
- [ ] Re-run local checks after edits.
- [ ] Review keyboard, screen-reader, Safari, Firefox and physical phone behavior.
- [ ] After deployment, verify all content routes, HTTPS, clean-route redirects and the custom error page on the official domain.
- [ ] Inspect production cookies/scripts and synchronize the privacy notice.
- [ ] Run Lighthouse on the live domain and verify sitemap/canonical/structured-data discovery.
- [ ] Keep affiliate links absent until an actual eligible relationship exists. When added, disclose near relevant content and update policies/consent controls as applicable.
- [ ] Before paid search, separately verify merchant permission, brand/trademark rules and current advertising requirements.

Design and SEO improvements cannot guarantee affiliate-platform or Google Ads acceptance.
