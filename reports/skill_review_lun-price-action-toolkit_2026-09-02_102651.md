# Dual-Axis Skill Review

- Generated at: 2026-09-02 10:26:51
- Selected skill: `lun-price-action-toolkit`
- Skill file: `skills/lun-price-action-toolkit/SKILL.md`
- Skill type: `knowledge_only`
- Selection mode: `manual`
- Seed: `None`
- Auto score: **80 / 100**
- LLM score: **93 / 100**
- Final score: **88 / 100**

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
1. [AUTO|HIGH] `skills/lun-price-action-toolkit/SKILL.md:160` - Hardcoded absolute user path detected (potential PII leak).
2. [LLM|MEDIUM] `skills/lun-price-action-toolkit/SKILL.md:160` - The path note hardcodes the absolute user path /Users/lui/workspace/LunTrading (single occurrence, verified by grep). This embeds the username in the skill file (mild PII), breaks if the project moves, and triggers the auto-axis high finding. The intent of the note (clarify project-root-relative paths) is good but the literal home-directory path is unnecessary to achieve it.
3. [AUTO|LOW] `skills/lun-price-action-toolkit/SKILL.md:8` - Reference paths use full project paths instead of relative paths.
4. [LLM|LOW] `skills/lun-price-action-toolkit/SKILL.md:106` - The harmonic table compresses the Bat B-point into '50%，「可以超過50%，但是不可以碰到61.8%」', dropping the speaker's other same-video statement 「我們要等待50%的回調，那一定要是50%，不可以超過」. evidence.md line 140 correctly preserves both contradictory phrasings, but a reader using only the SKILL.md table sees a single reconciled rule.
5. [LLM|LOW] `skills/lun-price-action-toolkit/SKILL.md:148` - Limitation 2 lists example unverified R-multiples (1對4.8、一對七、1:22.45) but omits the Triple Test 「一对二十」 claim quoted in evidence.md line 57, which is the largest single self-reported multiple in this skill's corpus and the most likely to be over-trusted.

## Test Verification (Auto Axis)
- Status: `not_applicable`
- Command: `None`

## Improvement Items (Final Score < 90)
1. Hardcoded absolute user path detected (potential PII leak). -> Replace with a relative path or dynamic resolution like `Path(__file__).resolve().parents[N]`.
2. The path note hardcodes the absolute user path /Users/lui/workspace/LunTrading (single occurrence, verified by grep). This embeds the username in the skill file (mild PII), breaks if the project moves, and triggers the auto-axis high finding. The intent of the note (clarify project-root-relative paths) is good but the literal home-directory path is unnecessary to achieve it. -> Replace the literal path with a generic anchor, e.g. 路徑係相對於 LunTrading 項目根目錄（即本 skill 所在 .claude/ 目錄嘅上一層）, so the note stays self-locating without any absolute user path. Apply the same wording to the sibling skill lun-ict-pd-arrays SKILL.md line 149 which uses the identical pattern.
3. Reference paths use full project paths instead of relative paths. -> Use relative paths like `references/...` instead of `skills/lun-price-action-toolkit/references/...` — SKILL.md is loaded in the skill directory context.
4. The harmonic table compresses the Bat B-point into '50%，「可以超過50%，但是不可以碰到61.8%」', dropping the speaker's other same-video statement 「我們要等待50%的回調，那一定要是50%，不可以超過」. evidence.md line 140 correctly preserves both contradictory phrasings, but a reader using only the SKILL.md table sees a single reconciled rule. -> Add a footnote marker in the table cell pointing to evidence.md section 11's dual phrasing (strict-50% vs may-exceed-but-below-61.8), consistent with the skill's own 矛盾口徑照錄 policy in limitation 3.
5. Limitation 2 lists example unverified R-multiples (1對4.8、一對七、1:22.45) but omits the Triple Test 「一对二十」 claim quoted in evidence.md line 57, which is the largest single self-reported multiple in this skill's corpus and the most likely to be over-trusted. -> Add 一对二十（VjSB-VRyxWI，Triple Test） to the example list in limitation 2.
