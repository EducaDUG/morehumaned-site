# Launch checklist

Run `grep -r TODO-LAUNCH .` (or the Grep tool) to find every item still open. Do not launch until the list is empty and the gate is clear.

## Gate
Diego reports the gate is clear (2026-10-19, document not reviewed by Claude). Keep a copy of the written permission or advice in a private folder, not in this repo.
- [x] Written answer from the employer on external teaching content, including paid workshops (per Diego, unseen)
- [x] Legal advice from an NZ contracts lawyer (per Diego, unseen)
- [ ] Trademark search for MoreHuman (NZ, AU, US, UK, EU, WIPO)

## Accounts (Diego does these)
- [ ] Cloudflare account with 2FA, domain bought, auto-renew on
- [ ] YouTube Brand Account channel "MoreHuman Ed", handle @morehumaned, phone verified, uploads default Unlisted
- [ ] GitHub repo morehumaned-site (keep PRIVATE until the gate clears)
- [ ] Email forwarding hello@morehumaned.com to Gmail
- [ ] Booking tool (Cal.com) and mailing platform with double opt-in
- [ ] Bot GitHub account, fine-grained token for this repo only, branch protection on main

## Content to replace (search TODO-LAUNCH)
- [ ] Contact email and booking link
- [ ] Mailing form URL
- [ ] Pilot price
- [ ] YouTube playlist links
- [ ] About story and photo
- [ ] Remove `noindex` meta tags from every page

## Go live
Stage 1 (done 2026-10-19): live at the GitHub Pages address in link-only mode, noindex kept, no custom domain yet.
Stage 2: buy domain, add CNAME file and DNS, fill the TODO-LAUNCH items, remove noindex and the robots.txt Disallow line.

- [ ] Repo public, Settings > Pages > main, custom domain morehumaned.com, Enforce HTTPS
- [ ] Cloudflare DNS: four A records and a www CNAME, DNS only
- [ ] Google Search Console: domain property, submit sitemap.xml
- [ ] Mailing platform sender authentication (SPF, DKIM, DMARC)
- [ ] LinkedIn profile updated (headline, banner, About, Featured)
