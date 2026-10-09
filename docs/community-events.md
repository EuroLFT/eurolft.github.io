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

The collector submits **one event per PR** and retains other candidates in its
private queue. Review the readable PR summary, organiser/source links, dates,
deadlines, location and warnings, then use GitHub:

- **Accept:** merge the event PR after review. A teammate can approve it first.
  If the collector submitted under your own account, review and merge your PR.
- **Reject:** close it without merging. The collector uses human closure receipts
  to remember the event and its aliases. Reopen the rejected PR to reconsider it.
- **Correct:** edit the event JSON or request changes in the PR before merging.
  For an existing record, advance its revision when changing it.

No local approve/reject scripts, per-event status edits or approval seals are needed
for this flow. GitHub's human merge is the authoritative acceptance receipt. Source
JSON can retain its pending proposal marker even on main; publication derives an
approved copy using the real merger and merge time. It does not rewrite main or
add a bot commit to the reviewed PR. Legacy explicit approved/rejected/hidden records
and advanced moderation tools remain supported.

Do not merge an event you do not want published. Proposal CI validates publication
facts, including date/type/chronology, safe public links and IANA zones for clock times.
A missing zone is a fact correction, not a request to run an approval script. Set an
unverified clock value to null if its date is known but its time cannot be established.
Warnings are displayed for human review; merging accepts those reviewed warnings.

Related events can be accepted independently. A relationship is displayed publicly
only once its target event has also been accepted. Keep identities rather than deleting
accepted records; hide an unwanted published record in a new reviewed PR.

## Review and publication checks

The review and Pages workflows check out a pinned 40-character scraper commit into
temporary `.event-tools` working storage. That code is ignored by Git and excluded
from Jekyll. Proposal CI checks schema, publishability, revisions and protected identities.
Publication additionally verifies a matching human-merged PR into website main, that
its merge SHA is an ancestor of the build, and that the committed event content matches.
A review on an unmerged PR or a later unreviewed edit cannot grant publication.
The workflow exports accepted public facts and audits the built site.
Changing the tools version requires a PR updating the pin in both workflows.

Only accepted facts, public source/organiser links and accepted related events enter
`_data/community_events.json`. Raw announcements, model responses, evidence excerpts,
reviewer identities and credentials do not enter the public calendar data. Collection
and Gemini never run in a website build. Validation failure blocks publication.

`/events/community/` displays dates, locations, deadlines and satellite relationships,
with local type/country/date filters and readable cards without JavaScript. The first
accepted dataset is empty until a reviewer merges a real event PR. Existing EuroLFT event
pages are preserved separately.

## Activation

Review the scraper-code PR and the website integration PR, designate actual event
reviewers, and require human review plus the event validation check on main. Verify
one editorial merge and Pages deployment. No collection workflow or schedule belongs
to this website repository; ingestion runs from the separate scraper repository.
