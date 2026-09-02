# LLM Skill Review Request

Please perform a deep review of the following skill, including:
- SKILL.md instruction quality and consistency
- helper scripts for correctness/risk
- tests and coverage gaps
- practical usability for operators

## Skill
- Name: `lun-ict-pd-arrays`
- SKILL.md: `skills/lun-ict-pd-arrays/SKILL.md`

## Files to inspect
- Scripts:
  - (none)
- Tests:
  - (none)
- References:
  - (none)

## Auto-axis baseline (for reference only; verify independently)
- Auto score: 27/100
- Auto findings:
  - [medium] Missing section: `## When to Use`.
  - [medium] Missing section: `## Prerequisites`.
  - [medium] Missing section: `## Workflow`.
  - [medium] Missing section: `## Output`.
  - [medium] Missing section: `## Resources`.
  - [medium] No runnable bash examples found.
  - [medium] No markdown reference files found in `references/`.
  - [medium] No executable helper scripts found in `scripts/`.
  - [medium] No `test_*.py` tests found for skill scripts.

## Output format (strict JSON only)
```json
{
  "score": 0,
  "summary": "one-paragraph overall assessment",
  "findings": [
    {
      "severity": "high|medium|low",
      "path": "skills/.../file.ext",
      "line": 0,
      "message": "problem statement",
      "improvement": "concrete fix"
    }
  ]
}
```

Scoring rule: 0-100. If score < 90, include concrete improvements.
