# Editorial event registry

This website directory stores event records and stable identities. A human merge
of an event PR accepts its content; closing a collector event PR without merging
rejects it. It contains event data only. Collector and moderation tools are
in Antonio-Rago/EuroLFT-Event-Scraper; run them there with --site pointing to this
website checkout. See ../../docs/community-events.md for review and publication.

Records may retain their pending proposal marker after merge. Publication verifies
the exact content against a human-merged website PR and derives approval metadata
privately during export. No local per-event approval commands are required.
Keep record IDs and history when hiding, rejecting, restoring or merging duplicates.
