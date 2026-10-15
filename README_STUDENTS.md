# CNT 4182 — Smart Building IoT Security Assessment

**Purpose:** Investigate the security of a simulated IoT building management application. All data and devices are fictitious. **Do not deploy publicly.**

## Environment
- Python 3.10 or later
- Flask (see requirements.txt)
- Source code is intentionally imperfect and may contain security and functional defects.

## Local setup
1. Extract the ZIP into a folder you control.
2. Open a terminal in that folder.
3. Create a virtual environment: `python -m venv .venv`.
4. Activate: Windows PowerShell `.venv\Scripts\Activate.ps1`; macOS/Linux `source .venv/bin/activate`.
5. Install dependencies: `python -m pip install -r requirements.txt`.
6. Optional smoke test: `python -m unittest discover -s tests`.
7. Optional local-only app run: `python run.py`. Visit `http://127.0.0.1:5055/`.

## Group A: Traditional security tool (Semgrep)
1. Install Semgrep: `python -m pip install semgrep` (or follow semgrep.dev official install instructions).
2. Confirm installation: `semgrep --version`.
3. In the project root, run `semgrep scan --config semgrep-rules/classroom.yml app/`.
4. Save a machine-readable report: `semgrep scan --config semgrep-rules/classroom.yml --json --output semgrep-results.json app/`.
5. If internet access and class policy allow, optionally run broader rules: `semgrep scan --config auto app/`. This downloads rules and can behave differently across dates.
6. Inspect every finding. Rule matches are leads, not automatically proven vulnerabilities. Record file, line, CWE (if supported), evidence, and remediation.
7. Submit the JSON report and completed findings worksheet. Do not use AI assistance.

## Group B: ChatGPT only
1. Open the same source files in a text editor. Provide all `app/*.py` files and `run.py` to ChatGPT (upload the student ZIP if available).
2. Use the common prompt in `GROUP_B_PROMPT.txt`.
3. Do not run Semgrep or other security scanners.
4. Verify that each reported finding corresponds to an actual code path. Record exact file and line evidence.
5. Submit the findings worksheet and complete ChatGPT conversation/prompt history.

## Both groups
- Time limit set by instructor; do not share findings across groups.
- Do not view the other group's outputs until submissions close.
- Do not attack other systems or use public deployment.
- Identify security weaknesses and, if noticed, functional defects separately.
- Severity ratings require explanation; avoid inventing CVSS scores.

## Troubleshooting
- If `semgrep` is not recognized, activate the same Python environment where it was installed or try `python -m semgrep --version`.
- If Semgrep reports a YAML parsing error, check the local rules file and Semgrep version; use the current official CLI instructions.
- For consistent grading, the instructor should record the Semgrep version and exact rules used.
