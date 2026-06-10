---
name: magic-square-tdd
description: >-
  MagicSquare_XX validate_lines TDD ARRR 사이클(Arrange→Red→Run Green→Refine)을
  슬래시 커맨드로 실행한다. red-test-plan, red-skeleton, golden-master, tdd-red,
  green-minimal, refactor-smell, refactor-safe 사용 시 또는 마방진 검증 TDD·10선·
  pytest RED-GREEN-REFACTOR 언급 시 적용.
---

# MagicSquare_XX TDD (ARRR)

## 범위

- 4×4 부분 마방진 **검증 + 테스트**만 (`validate_lines`)
- 풀이·UI·LLM·3×3/5×5 일반화 **금지**
- SSOT: `.cursorrules` > `docs/PRD.md` > `.cursor/commands/*.md`

## ARRR 사이클

| 단계 | 약어 | 커맨드 | 수정 대상 | 산출 |
|------|------|--------|-----------|------|
| **A**rrange | 계획·fixture | `/red-test-plan` | 없음(계획표) | 테스트 계획표 |
| **A**rrange | golden | `/golden-master` | `tests/` | PASS/FAIL/INCOMPLETE fixture |
| **R**ed | skeleton | `/red-skeleton` | `tests/` | AAA 골격, 실패 |
| **R**ed | assert | `/tdd-red` | `tests/` | 완전한 실패 assert |
| **R**un Green | 구현 | `/green-minimal` | `src/` | all passed |
| **R**efine | smell | `/refactor-smell` | 없음(리뷰) | smell 표 |
| **R**efine | safe | `/refactor-safe` | `src/`·`tests/` | green 유지 정리 |

한 턴에 **한 Phase**만. 응답 첫 줄: `[Phase: RED]`, `[Phase: GREEN]`, `[Phase: REFACTOR]` 등.

## API 계약 (요약)

```python
validate_lines(grid) -> {
    "status": "pass" | "fail" | "incomplete",
    "failed_lines": ["R1", "D2", ...],  # fail만 채움, 그 외 []
}
```

- 10선: `R1`~`R4`, `C1`~`C4`, `D1`, `D2`
- `MAGIC_CONSTANT = 34` — import SSOT, 리터럴 `34` 금지
- `incomplete`: `0` 빈칸 존재 → `failed_lines: []`

## Mom Test ↔ 테스트

| SC | 증거 | 테스트 방향 |
|----|------|-------------|
| SC1 | 대각선 빼먹어 20분 낭비 | fail + `D1`/`D2` in `failed_lines` |
| SC2 | 처음부터 다시 | fail + `failed_lines` 구체적 |
| SC3 | LLM 대신 pytest | pass / fail / incomplete ≥3, `pytest -v` |

## TDD 금지 (전 Phase)

- assert 완화·skip·xfail·`pass`만 있는 테스트
- RED에서 `src/` 수정 / GREEN에서 테스트 기대값 변경
- git commit·push (사용자 명시 요청 시만)
- 추가 입력·질문 — **슬래시만으로 즉시 실행**

## 권장 한 사이클

```
/red-test-plan → /golden-master → /red-skeleton → /tdd-red
  → /green-minimal → /refactor-smell → /refactor-safe
```

세션 마무리: `/export-session` (별칭 `/export`)

## 커맨드 위치

- `.cursor/commands/red-test-plan.md`
- `.cursor/commands/red-skeleton.md`
- `.cursor/commands/golden-master.md`
- `.cursor/commands/tdd-red.md`
- `.cursor/commands/green-minimal.md`
- `.cursor/commands/refactor-smell.md`
- `.cursor/commands/refactor-safe.md`
