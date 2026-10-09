# Community event review and publication

EuroLFT/eurolft.github.io owns the event records, human editorial decisions and the
community calendar. All collector and editorial-tool code lives separately in
[Antonio-Rago/EuroLFT-Event-Scraper](https://github.com/Antonio-Rago/EuroLFT-Event-Scraper).
Its operating guide describes ingestion and command setup.

## Website-owned records

`_event_collector/records/*.json` contains canonical event identities and approved,
rejected or hidden decisions. The historical folder name denotes editorial data here;
there are no source adapters, Python modules, prompts or model caches in this repository.
The facts-only template `_event_collector/manual-event.template.json` helps manual additions.
The website Issue form also accepts event suggestions and corrections.

Collection prepares pending records for draft PRs. Editors inspect facts, sources,
dates, deadlines, relevance and related events, including fields without warnings.
Use the separate scraper's moderation tools to correct/approve/reject/hide records,
then prepare a package with `--site` pointing to this checkout. Its package application
writes event JSON only; it performs no Git commit, push or publication.

Merge-ready records require explicit approved/rejected/hidden decisions. Each approved
record must seal its current revision/content and acknowledge warnings. Clock times
need verified IANA timezones. Corrections invalidate approval. Retain rejected/hidden
IDs and merge exclusions so later ingestion remembers them; closing a PR alone means
deferred. Restoration requires an explicit editorial action. Duplicate redirects and
manual field protections are preserved. Never delete a record merely to remove it from view.

## Review and publication checks

The review and Pages workflows check out a pinned 40-character scraper commit into
temporary `.event-tools` working storage. That code is ignored by Git and excluded
from Jekyll. It validates website records, checks revisions/restoration/deletions
against website Git history, exports approved public facts and audits the built site.
Changing the tools version requires a PR updating the pin in both workflows.

Only approved facts, public source/organiser links and approved related events enter
`_data/community_events.json`. Raw announcements, model responses, evidence excerpts,
reviewer identities and credentials do not enter the public calendar data. Collection
and Gemini never run in a website build. Validation failure blocks publication.

`/events/community/` displays dates, locations, deadlines and satellite relationships,
with local type/country/date filters and readable cards without JavaScript. The first
approved dataset is empty until editors approve real events. Existing EuroLFT event
pages are preserved separately.

## Activation

Review the scraper-code PR and the website integration PR, designate actual event
reviewers, and require human review plus the event validation check on main. Verify
one editorial merge and Pages deployment. No collection workflow or schedule belongs
to this website repository; ingestion runs from the separate scraper repository.
