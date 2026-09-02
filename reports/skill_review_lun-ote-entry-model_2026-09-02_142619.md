# Dual-Axis Skill Review

- Generated at: 2026-09-02 14:26:19
- Selected skill: `lun-ote-entry-model`
- Skill file: `skills/lun-ote-entry-model/SKILL.md`
- Skill type: `knowledge_only`
- Selection mode: `manual`
- Seed: `None`
- Auto score: **80 / 100**
- LLM score: `not provided`
- Final score: **80 / 100**

## Auto Score Breakdown
- metadata_use_case: 20
- workflow_coverage: 25
- execution_safety_reproducibility: 14
- supporting_artifacts: 9
- test_health: 12

## Score Weights
- auto_weight: 1.00
- llm_weight: 0.00

## Findings (Combined)
1. [AUTO|LOW] `skills/lun-ote-entry-model/SKILL.md:8` - Reference paths use full project paths instead of relative paths.

## Test Verification (Auto Axis)
- Status: `not_applicable`
- Command: `None`

## LLM Prompt File
- `/Users/lui/workspace/LunTrading/reports/skill_review_prompt_lun-ote-entry-model_2026-09-02_142619.md`

## Improvement Items (Final Score < 90)
1. Reference paths use full project paths instead of relative paths. -> Use relative paths like `references/...` instead of `skills/lun-ote-entry-model/references/...` — SKILL.md is loaded in the skill directory context.
