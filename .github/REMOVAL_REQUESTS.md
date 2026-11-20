# 🛡 Removal requests & legal notices (policy)

Short version: **copyright claims go through GitHub's official DMCA process** (not through
us directly) — GitHub validates them, forwards them to us, and publishes redacted copies
at [github/dmca](https://github.com/github/dmca). Other legal claims (trademark, privacy/
GDPR, court orders) can be filed via the **"Removal request" issue template** in this
repo. We acknowledge within **48 h** and decide/act within **7 days**, and we log every
action in [REMOVAL_LOG.md](REMOVAL_LOG.md).

> ⚠️ This page describes our process; it is **not legal advice**.

## 1 · What this repo contains (and why the risk is low)

- **Links** to third-party sites. Merely linking to a webpage is generally not copyright
  infringement, and we do not copy their content.
- **Hosted files** only from sources with an *explicit redistribution permission* (currently:
  lichess exports under **CC0**) — proof in [`licenses/`](licenses/).
- Our own texts are **CC0** ([LICENSE](LICENSE)).

Nevertheless, disputes can arise (e.g. a *database-right* claim on game collections, a
trademark in a linked name/logo, or a **GDPR erasure request** because a player's username
appears in a hosted PGN sample). Here is how to reach us.

## 2 · Channels — please use the right one

| Type of claim | Channel | Notes |
|---|---|---|
| **Copyright infringement (DMCA)** | GitHub DMCA form: https://github.com/contact/dmca — policy: https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy | GitHub checks the notice for completeness, **contacts us as repo owner**, gives us a chance to remove the content or dispute it, and publishes a redacted copy of valid notices at https://github.com/github/dmca. If we file a counter-notice, GitHub re-enables the content within **10–14 business days** unless you sue (guide: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-counter-notice). |
| **Trademark / defamation / court order / other legal** | "Removal request" issue template in this repo, or GitHub content-removal request: https://docs.github.com/en/site-policy/content-removal-policies/submitting-content-removal-requests | Please do **not** post personal data in the public issue — see §4. |
| **Privacy / personal data (GDPR, doxxing)** — e.g. your username in a hosted PGN | GitHub private-information removal: https://docs.github.com/en/site-policy/content-removal-policies/github-private-information-removal-policy — or the issue template with minimal data | We process erasure requests under **GDPR Art. 17** within one month. |
| **Abuse / spam / malware** | GitHub "Report abuse": https://docs.github.com/en/communities/maintaining-your-safety-on-github/reporting-abuse-or-spam | — |

## 3 · What a request must contain

1. **Exact content**: file path / line in this repo, or the full URL of the link.
2. **Basis of the claim**: which right is infringed (work, trademark, personal data …).
3. **Proof of standing**: that you hold the right (or are authorized to act).
4. **Contact** for follow-up.
5. **Good-faith statement** that the claim is accurate (required for DMCA notices).

For copyright, use the DMCA form — it enforces exactly these requirements
(guide: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice).

## 4 · How we handle requests (process & SLAs)

1. **Acknowledge** within **48 hours**.
2. **Review** within **7 days**: we check whether the claim is plausible and whether a
   license/permission exists (see `licenses/`). We do not remove CC0-licensed or purely
   linked content based on informal requests without a valid legal basis — but once we
   are **aware of illegal content, we act expeditiously** (EU Digital Services Act,
   Regulation (EU) 2022/2065, Art. 16 notice-and-action; no general monitoring duty,
   Art. 8 — we react to concrete notices).
3. **Action**: remove/replace the specific link or file, restrict it, or — in the worst
   case — archive the repository. We prefer the *smallest effective* action.
4. **Log** the action in [REMOVAL_LOG.md](REMOVAL_LOG.md) (without personal data).
5. **Counter-notice / restore**: if content was removed by mistake or a license applies,
   we restore it (for DMCA, via GitHub's counter-notice process; re-enable after
   10–14 business days unless the claimant sues). GitHub terminates **repeat infringers**.
6. **Records**: requests are kept only as long as needed to handle them and to document
   our compliance, then deleted. Requester data is never published; GitHub redacts
   personal information in published DMCA notices.

## 5 · Data protection note for requesters

Public issues are public — **never include passwords, ID documents or other sensitive
personal data** in an issue. Use the DMCA form or GitHub's private channels for anything
sensitive. Player usernames inside the CC0-licensed lichess PGN samples are personal data
under GDPR; if you want yours removed from a hosted sample, say so in a removal request
(type: privacy) and we will replace the sample with an anonymized one.

## 6 · Legal background (for the curious)

- **US:** DMCA 17 U.S.C. § 512(c)/(g) — notice & takedown with safe harbor for hosting
  providers, counter-notice, repeat-infringer policy. GitHub is the designated agent.
- **EU:** Digital Services Act (Regulation (EU) 2022/2065) Art. 16 (electronic
  notice-and-action mechanism), Art. 6/8 (no general monitoring; act expeditiously once
  aware); GDPR Art. 17 (erasure). Raw chess moves are facts and generally not
  copyrightable, but *curated collections* can be protected by the EU *sui generis*
  database right — which is why we link instead of mirroring (see
  [licenses/link-only-sources.md](licenses/link-only-sources.md)).
