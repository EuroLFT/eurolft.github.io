# Community event collector: operating guide

The first release uses the public Lattice News archive and INSPIRE conferences. Both
produce pending records for GitHub review. Editors retain control of relevance,
corrections, manual additions, removals and restoration. The website builds from
reviewed canonical JSON; collection and Gemini extraction never run in a website build.

## Install and collect

Use Python 3.9 or newer, with a private local environment:

```sh
python3 -m venv _event_collector/local/venv
_event_collector/local/venv/bin/python -m pip install -r tools/event_collector/requirements.txt
```

Routine mailing-list ingestion selects exactly one UTC archive month. The current
month is the default; `--month-window previous` selects the last completed month.
Older frozen development samples are separate. First inspect the preflight:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.ingest
```

After configuring a Gemini key with the existing hidden-input credentials helper,
permit extraction explicitly:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.ingest --live --wait
```

Use a Free-tier project with billing disabled. The collector does not verify the
account's billing settings. The existing 20-attempt rolling-day cap and 60-second
request pacing remain in force. `--wait` paces a batch; without it, later messages
are deferred visibly. Cache hits do not consume attempts. Parsed validation failures
can still yield review candidates with warnings; API failures and malformed responses
remain operational items. Failed requests are not retried automatically. Private
sources/caches and the quota ledger stay on the operator's machine. The production
command has no dependency on case labels or evaluation splits.

For INSPIRE, structured metadata needs no model call:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.inspire
```

The default reproduces the user's upcoming Theory-HEP selection. Optional `--query
lattice` and `--subject lattice` support narrower comparisons. Keep broad candidates
for relevance review. Defaults bound collection to six pages, 25 records/page and
100 records; a limit or outage produces a partial status, never cancellation/deletion.
Titles, complete dates, an unambiguous catalogue location and a single organiser URL
are mapped directly. Type classification is provisional. Missing fields stay unknown;
descriptions, contact details and automatic attendance guesses are omitted.

Every adapter prints the private review-bundle path. Reconcile that directory:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.reconcile BUNDLE_DIRECTORY
_event_collector/local/venv/bin/python -m tools.event_collector.review_changes PLAN_DIRECTORY
```

The second command prepares a readable PR description and minimal JSON changes. It
excludes unchanged, excluded and unresolved identity items. It rechecks canonical
state, strips contact/access details from pending evidence with a warning and blocks
unsafe public links. It does not send a PR. The private summary remains a snapshot.
If a match is ambiguous, use `reconcile --matches choices.json`, mapping candidate IDs
to canonical IDs or `"new"` after inspection. A strongly matched exclusion cannot be
bypassed by allocating another ID.

## Editor workflow

The public “Suggest an event or correction” route opens the GitHub Issue form. An
editor transfers the suggestion into the canonical facts template and prepares a
reviewable record. Issue submission does not publish or invoke a model. Use your
GitHub handle as `--actor`; the examples below use a placeholder, not a real approval.

For a missing event, copy `_event_collector/manual-event.template.json` into private
storage, fill title/type/dates and any known fields, then run:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.moderate manual FACTS.json \
  --actor YOUR_GITHUB_HANDLE --output _event_collector/local/editor
```

For a correction, supply a JSON object containing only changed facts, such as
`{"location":{"city":"Verified city"}}`:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.moderate edit RECORD.json \
  --patch CORRECTION.json --protect /facts/location/city \
  --actor YOUR_GITHUB_HANDLE --output _event_collector/local/editor
```

Manual records protect all facts from collection. Selected overrides protect
collected records. Corrections invalidate approval; edits to hidden/rejected records
keep their exclusion until an explicit restoration. Unknown incoming values cannot
erase an editor's known facts.

Inspect every proposed fact and source, including unflagged fields, before approval:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.moderate approve RECORD.json \
  --actor YOUR_GITHUB_HANDLE --acknowledge-all --output _event_collector/local/editor
```

Approval requires a supported type, event start date, valid chronology, safe URLs and
an IANA timezone for each published clock time. Unknown clock timezone: verify it or
remove the clock time while retaining the date. The course pilot's deadline therefore
needs correction before approval. Deadline labels/purposes and recurring course
timetables still need semantic review. The content seal covers facts, provenance,
relationships, aliases, warnings and overrides: editing any of these invalidates
approval even if someone forgets to increment the revision.

To exclude a candidate or remove a published event, use `reject` or `hide`, with
`--reason`. To reverse an exclusion, use `restore` explicitly, acknowledging warnings.
The same ID, aliases and real editorial history survive these operations. A cancelled
approved event remains visible with a cancellation label unless an editor hides it.

For duplicate events:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.moderate merge SURVIVOR.json \
  --duplicate DUPLICATE.json --actor YOUR_GITHUB_HANDLE --output _event_collector/local/editor
```

This produces a pending survivor and a hidden duplicate with a redirect. Inspect the
combined facts/sources and approve the survivor before merging both files. Future
reminders follow the redirect; manual facts and field overrides stay protected.

Prepare explicit editor records for GitHub:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.review_changes _event_collector/local/editor
```

The package contains `changes/_event_collector/records/*.json`, `review.md` and a
minimal manifest. Copy an integrity-checked package into a local checkout with
`review_changes PACKAGE_DIRECTORY --apply`, then review the Git diff and submit a PR.
Applying a package performs no commit, push or remote operation. It refuses changed
canonical state or altered package contents; prepare a new package after editing.

Canonical records in a merge-ready PR must have an explicit approved/rejected/hidden
decision. Pending drafts stay on the proposal branch. Merge exclusion records too:
closing a PR alone means deferred and does not create durable exclusion memory.
Do not delete a canonical JSON to hide an event. PR checks compare with the base branch
and enforce retained identities, advancing revisions and explicit restoration.

## Website and preview

`/events/community/` is linked from Events. It shows chronological dates, type,
location/attendance, deadlines, organiser/source links and satellite relationships.
Type, country and upcoming/ongoing/past filters run locally in the browser. Day
classification uses the UTC date and inclusive end date; an unknown end falls back
to the start. Filters refresh after midnight. Without JavaScript, all reviewed events
remain visible. Existing EuroLFT event Markdown pages are preserved separately.

The publication workflow validates canonical decisions and generates
`_data/community_events.json` immediately before the Jekyll build. Only sealed approved
records are exported. No raw messages, model responses, evidence excerpts, reviewer
identities or API credentials enter this public dataset. A build privacy check runs
before upload. Failed validation leaves the existing public dataset untouched.

For a private preview of pending data, without making any approval decision:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.preview PLAN_DIRECTORY
bundle exec jekyll build --config _config.yml,_event_collector/local/preview.yml
```

Serve `_event_collector/local/site-preview/` locally. Its page carries an unapproved
preview banner. Do not deploy it. Production still starts with an empty approved
dataset until editors approve events.

## GitHub operation and activation

`Check community events` runs software tests, terminal-decision checks, revision and
deletion checks, a deterministic export, Jekyll build and privacy audit on PRs.
The existing Pages workflow uses the same publication/export checks on main.
Neither workflow performs model extraction.

`Prepare community event review` is manual-only and uses INSPIRE. The preparation
job has read access and uploads only the minimal public review package. Its optional
draft-PR job receives write permissions only when explicitly selected. It creates a
single `automation/community-events` branch and refuses to overwrite an existing
proposal branch, including a closed but unresolved proposal. Resolve the PR, merge any
durable exclusions and remove the resolved proposal branch before another run. Current
main-state integrity is rechecked before applying the package. Nothing auto-approves,
auto-merges or changes main. Partial collection blocks remote proposal creation.

The public GitHub workflow deliberately does not run Gemini or cache raw mailing-list
material: the local runner owns its private input/cache/quota state. It can prepare
mailing-list review packages locally and submit them through the same PR route. Do
not move raw caches or keys into publicly accessible Actions caches/artifacts.

Before production activation, a repository administrator must verify the review
settings: require human review and the `Check community events` status check on main,
dismiss outdated approvals, and designate actual event reviewers. CODEOWNERS names
cannot be invented. If opening draft PRs through Actions, enable the repository's
permitted PR-creation setting or supply an approved GitHub App credential. Verify that
the draft's checks run and that an editor's merge deploys correctly; token-created
events may require additional approval. No settings or credentials are changed by
this implementation. No recurring schedule is enabled.

Use the manual pilot before scheduling: observe omissions, false positives, corrections,
duplicates and review time over 2–4 weeks. The current software tests are not measured
Gemini accuracy. Independent label adjudication and a held-out evaluation remain a
quality-assessment task; the broad review pipeline does not wait for perfect extraction.
Automatic organiser-page enrichment, further sources and ICS subscriptions remain
optional extensions rather than prerequisites for this first release.

## Backup, failures and recovery

Canonical editorial state belongs in Git. Preserve the private pending identity and
quota ledgers on the local operator's machine; runner caches are not authoritative.
The following backup includes canonical decisions and pending IDs, excluding keys,
raw sources and model responses:

```sh
_event_collector/local/venv/bin/python -m tools.event_collector.backup save \
  _event_collector/local/backups/editorial.json
_event_collector/local/venv/bin/python -m tools.event_collector.backup restore \
  _event_collector/local/backups/editorial.json --destination _event_collector/local/recovered
```

Restore verifies integrity and writes a separate new directory for inspection. It
never overwrites the current registry. Back up the quota ledger separately as private
operator state; restoring editorial data must not reset provider/request allowances.

Source outages, quotas, missing credentials, invalid facts and unparseable responses
produce visible failure/repair items. They do not cancel an event, undo exclusions or
replace the published website. Inspect partial bundles and repair messages before
proceeding. Reruns preserve edited bundles/snapshot reports. Reconcile again when
canonical decisions change, and review the Git diff before any PR or deployment.
