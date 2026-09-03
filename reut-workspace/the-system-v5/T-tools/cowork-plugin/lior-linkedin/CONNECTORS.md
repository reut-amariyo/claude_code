# Connectors

## Browser control, needed for two skills

`linkedin-comments` and `linkedin-benchmark` read LinkedIn pages from a browser that is
already signed in as Lior. They are strictly read-only: they never react, follow, comment or
click any engagement control.

Without browser access both skills still work in manual mode. Paste the profile headline,
follower count and recent posts with their engagement, and the analysis and drafting run
unchanged. Never estimate numbers that were not read.

The other three skills, `linkedin-post`, `linkedin-prepublish` and `linkedin-followers`,
need no connectors at all.
