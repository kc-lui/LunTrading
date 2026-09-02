# LLM Skill Review Request

Please perform a deep review of the following skill, including:
- SKILL.md instruction quality and consistency
- helper scripts for correctness/risk
- tests and coverage gaps
- practical usability for operators

## Skill
- Name: `lun-prop-firm-playbook`
- SKILL.md: `skills/lun-prop-firm-playbook/SKILL.md`

## Files to inspect
- Scripts:
  - (none)
- Tests:
  - (none)
- References:
  - `skills/lun-prop-firm-playbook/references/evidence.md`

## Auto-axis baseline (for reference only; verify independently)
- Auto score: 80/100
- Auto findings:
  - [low] Reference paths use full project paths instead of relative paths.

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
