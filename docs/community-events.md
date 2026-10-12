# Community event review and publication

The collector in [Antonio-Rago/EuroLFT-Event-Scraper](https://github.com/Antonio-Rago/EuroLFT-Event-Scraper)
prepares one website-ready JSON file per event. This website holds the data, human
review PRs and Jekyll calendar. Its Actions workflow runs Ruby/Jekyll only.

## Review an event

Each event PR changes `_data/community_events/EVENT_ID.json`. Inspect the title,
dates, location, deadlines, organiser/source links and the warnings in its summary.

- Merge the PR into main to publish the event.
- Close without merging to reject it; the collector remembers that decision.
- Edit the JSON before merging for corrections. Advance its revision on updates.

Title, dates and other facts are top-level fields. Unknown values remain null and
are shown as unconfirmed. The remaining metadata preserves evidence, matching
identities, warnings and historic edits. The old pending marker is retained for
compatibility; no approval field or terminal command needs changing before merge.
Jekyll displays main's records except those explicitly hidden or rejected.

To remove an unwanted published event, submit a correction PR setting
`decision.status` to `hidden`, give a reason, and advance the revision. Retain the file
and stable ID so later scraping cannot accidentally re-add it. Relations are linked
only when their target is also published; duplicate redirects preserve surviving links.

For a missing event, use the website Issue form or the collector's manual-entry
command with [the facts template](manual-event.template.json). Review and merge the
resulting event PR in the same way.

## Build

Jekyll reads `_data/community_events/*.json` directly, sorts the calendar by date,
and renders `/events/community/`. Events with unknown dates remain visible with an
unconfirmed date label. Local date/type/country filters work without affecting the
server-rendered cards; the calendar is readable without JavaScript.

There is no aggregate event JSON generation, collector checkout, Python package
installation, scraping or Gemini extraction in website Actions. Ordinary Pages
builds run after pushes to main. Raw collector caches, prompts, credentials and model
replies stay in the separate collector checkout. Metadata in `_data` is not copied
as public assets; the calendar renders only the selected event facts and source links.
The pre-existing institution utility is unrelated to event publication.

## Transition of existing proposals

After merging this website migration, run the collector's `migrate --open-prs`
command before merging remaining old-format event PRs. It retains their PR numbers,
final reviewer-edited content and notes, and converts each file to the new data path.
It refuses concurrent branch edits and never merges or closes proposals. Already
accepted events in this migration retain their facts and identities.
