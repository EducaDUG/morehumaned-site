# Launch checklist

Run `grep -r TODO-LAUNCH .` (or the Grep tool) to find every item still open. Do not launch until the list is empty and the gate is clear.

## Gate
Diego reports the gate is clear (2026-10-19, document not reviewed by Claude). Keep a copy of the written permission or advice in a private folder, not in this repo.
- [x] Written answer from the employer on external teaching content, including paid workshops (per Diego, unseen)
- [x] Legal advice from an NZ contracts lawyer (per Diego, unseen)
- [ ] Trademark search for MoreHuman (NZ, AU, US, UK, EU, WIPO)

## Accounts (Diego does these)
- [x] Cloudflare account, domain bought (2026-10-19). 2FA: confirm email or app 2FA is on
- [ ] YouTube Brand Account channel "MoreHuman Ed", handle @morehumaned, phone verified, uploads default Unlisted
- [ ] GitHub repo morehumaned-site (keep PRIVATE until the gate clears)
- [x] Email forwarding hello@morehumaned.com to Gmail; sending via Brevo SMTP + Gmail Send-as (SPF/DKIM/DMARC pass)
- [ ] Booking tool (Cal.com). Mailing platform: Brevo account exists, needs PO Box address before newsletters
- [ ] Bot GitHub account, fine-grained token for this repo only, branch protection on main

## Content to replace (search TODO-LAUNCH)
- [x] Contact email and booking link (cal.com/morehumaned/talk)
- [x] Newsletter and Teacher Time Audit sign-up dropped for now (no mailing list, no PO Box needed)
- [x] Pilot price: decided to keep it off the site, 'on inquiry' (2026-10-19)
- [ ] YouTube playlist links
- [ ] About story and photo
- [x] noindex tags removed

## Go live
Stage 1 (done 2026-10-19): fully launched and open to search at https://educadug.github.io/morehumaned-site/ (Diego's decision). Canonical and sitemap use that address for now.
Stage 2 (done 2026-10-19): custom domain morehumaned.com connected (CNAME file, Cloudflare DNS, Pages custom domain). Remaining: Enforce HTTPS, Search Console, fill TODO-LAUNCH items.

- [x] Repo public, Pages on main, custom domain morehumaned.com, HTTPS enforced
- [x] Cloudflare DNS: four A records and a www CNAME, DNS only
- [x] Google Search Console: domain property verified, sitemap submitted, home page indexing requested (2026-10-19)
- [x] Sender authentication (SPF, DKIM, DMARC) for Brevo
- [ ] LinkedIn profile updated (headline, banner, About, Featured)
