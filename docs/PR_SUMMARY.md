# PR Summary

## Overview
This PR stabilizes the app entrypoint and package import structure for the Text in Shape project.

## What changed
- Standardized the main execution path in `main.py`
- Resolved inconsistent package imports between `text_in_shape` and `sgape_in_text`
- Kept compatibility shims for both package names to avoid runtime breakage
- Added a regression test for the main import/entrypoint path
- Verified the Flask page responds successfully with HTTP 200
- Updated the project documentation to reflect the active app setup and execution flow

## Verification
- `python -m pytest -q` -> 7 passed
- Flask app root page -> HTTP 200 OK

## Suggested PR title
`refactor: standardize package imports and clean app entrypoint`

## Suggested PR description
### Summary
This PR fixes the app entrypoint and package import mismatch that prevented the project from running cleanly under the expected Python environment.

### Changes
- align the app startup path with the active package layout
- fix mixed package-name references for runtime stability
- add regression coverage for the app entrypoint
- verify the web UI loads successfully
- refresh project documentation

### Validation
- pytest: 7 passed
- local Flask app responds successfully on the default route
