# Reviewed calendar data

One file per event, named EVENT_ID.json. The collector prepares the complete file.
A human merge into website main accepts it for publication. Jekyll reads these files
directly; no Python runs during publication. Hidden/rejected records retain their
IDs but are omitted from the calendar. See ../../docs/community-events.md.
