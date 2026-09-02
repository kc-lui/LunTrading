# Dual-Axis Skill Review

- Generated at: 2026-09-02 19:04:16
- Selected skill: `lun-backtesting-method`
- Skill file: `skills/lun-backtesting-method/SKILL.md`
- Skill type: `knowledge_only`
- Selection mode: `manual`
- Seed: `None`
- Auto score: **80 / 100**
- LLM score: **96 / 100**
- Final score: **90 / 100**

## Auto Score Breakdown
- metadata_use_case: 20
- workflow_coverage: 25
- execution_safety_reproducibility: 14
- supporting_artifacts: 9
- test_health: 12

## Score Weights
- auto_weight: 0.35
- llm_weight: 0.65

## Findings (Combined)
1. [AUTO|LOW] `skills/lun-backtesting-method/SKILL.md:8` - Reference paths use full project paths instead of relative paths.
2. [LLM|LOW] `skills/lun-backtesting-method/SKILL.md:41` - The vocabulary quick-table's 樣本量門檻 row quotes only the 100/200-trade backtest caliber, with no signal that Step 4 layers three more purpose-specific tiers (10/100 before small-capital, 50-100 before prop exams, 100-per-unit for the probability model). A reader stopping at the quick table sees a single number — the exact merge the skill's own Limitation 6 forbids.
3. [LLM|LOW] `skills/lun-backtesting-method/SKILL.md:60` - Step 2 states 「bar-by-bar 唔睇後市（B7rumsOw6_U 全片示範）」 without the provenance caveat that evidence.md line 20 carries (筆記歸納，非引文) — the claim is a summary of an entire demo video, not a quotable rule, but SKILL.md presents it with the same weight as quoted rules.

## Test Verification (Auto Axis)
- Status: `not_applicable`
- Command: `None`
