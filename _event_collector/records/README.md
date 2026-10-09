# Canonical editorial event registry

This directory is reserved for one canonical JSON record per event, named with its
stable event ID and conforming to `../schema/event.schema.json`. There are currently
no real canonical records. Development examples are fixtures, not editorial decisions.

The local reconciliation command reads this directory without writing it. Suggested
changes live under ignored `../local/`; they require human review through the implemented
GitHub proposal workflow before becoming canonical. The explicit review-package `--apply`
command can copy integrity-checked changes into a local checkout without a Git operation.
Existing website Markdown events are kept separately. The Pages workflow validates and
exports only approved records before building the public community page.

Keep rejected and hidden records so reminders and additional sources can respect
exclusions. Preserve identity aliases, source provenance, manual origin, field overrides
and real editorial history. Publication requires approval for the current revision and
a matching content seal, with warnings acknowledged. The private
pending identity ledger is not a substitute for this shared editorial registry.
