# Number Converter — Team Process Documentation

Purpose
- Provide a clear, repeatable process for a 5‑person team to develop, test, review and release the Number Converter app (c:\Users\ADIX.C\main.py).

Team & Responsibilities (5 members)
- Product Owner (PO)
  - Define features, acceptance criteria, prioritize backlog.
  - Validate UI/UX and sign off on releases.
- Tech Lead
  - Architecture, design decisions, approve major refactors.
  - Final code reviewer for complex PRs.
- Developer A
  - Implement new features and UI changes.
  - Create unit tests for implemented logic.
- Developer B
  - Refactor, extract conversion logic to testable modules.
  - Maintain code quality and linting.
- QA / DevOps
  - Write/execute test plans, run automated tests.
  - Configure CI, releases, and environment docs.

Workflow
- Issue tracking: create an issue per task with acceptance criteria.
- Branching:
  - feature/<issue-id>-short-desc
  - bugfix/<issue-id>-short-desc
  - release/vX.Y.Z
  - main is protected; PRs required to merge.
- PR rules:
  - Link issue, list changes, include screenshots if UI changed.
  - Must have 1 developer reviewer + Tech Lead for major changes.
  - CI green, unit tests passing, linter passing.
  - Update CHANGELOG.md entry for visible changes.

Code & Testing Standards
- Keep conversion logic pure and testable (suggest: convert_number(value, from_sys, to_sys) -> str).
- Use type hints and simple docstrings.
- Write unit tests with pytest under tests/.
- Linting with flake8/black (team decides formatter); run before PR.
- Minimum test coverage: add tests for main conversion paths and edge cases.

Local Setup & Run (Windows PowerShell)
- Create venv and activate:
  python -m venv .venv
  .venv\Scripts\Activate.ps1
- Install deps:
  pip install kivy pytest
- Run app:
  python c:\Users\ADIX.C\main.py
- Run tests:
  pytest -q

CI & Releases
- CI jobs:
  - Install deps, run linter, run pytest.
  - Build artifact if needed (wheel, executable).
- Release:
  - Create release branch, QA sign‑off, tag vX.Y.Z, merge to main, publish artifact or share script.

Code Review Checklist
- Does it meet acceptance criteria?
- Is conversion logic separated and covered by tests?
- No sensitive data or hardcoded secrets.
- UI changes accessible and documented.
- Commit messages clear and follow pattern: <type>(<scope>): short description

Communication & Meetings
- Daily standup (10–15 min).
- Sprint length: 1 or 2 weeks (team choice).
- Use a shared channel (Slack/Teams) for ad‑hoc coordination.

Notes / Next Improvements
- Add input validation per base and better error messages.
- Add copy-to-clipboard, history, and keyboard shortcuts.
- Consider packaging (PyInstaller) for easier distribution.
