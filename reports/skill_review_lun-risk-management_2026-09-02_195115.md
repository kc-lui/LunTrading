# Dual-Axis Skill Review

- Generated at: 2026-09-02 19:51:15
- Selected skill: `lun-risk-management`
- Skill file: `skills/lun-risk-management/SKILL.md`
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
1. [AUTO|LOW] `skills/lun-risk-management/SKILL.md:8` - Reference paths use full project paths instead of relative paths.
2. [LLM|LOW] `skills/lun-risk-management/SKILL.md:91` - Four (transcript)-labelled quotes carry no video id on their own line — the two 倉位公式 quotes 「那個Formula,就是你的資金再乘以0.01…」and 「你就要用你可以虧損的金額,再除以你的止损點」at SKILL.md:91 and again at references/evidence.md:53-54. The id is inferable only from the section headers (Step 4 — 倉位計算公式（hkCvRoLc3Nk） and evidence §3). I confirmed both quotes exist verbatim in data/transcripts/hkCvRoLc3Nk.txt, so the content and the (transcript) label are both correct; the attribution simply is not checkable from the line itself, unlike the other 38 transcript-labelled quotes.

## Test Verification (Auto Axis)
- Status: `not_applicable`
- Command: `None`
