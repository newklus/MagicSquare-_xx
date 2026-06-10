# MagicSquare_XX — ARRR / TDD 세션 체크리스트

| # | 체크 | SC | 완료 |
|---|------|-----|------|
| 1 | 주제가 **판정·확인**이지 풀이 앱이 아닌가? | — | [ ] |
| 2 | API가 `validate_lines` → `{status, failed_lines}` 인가? | SC2 | [ ] |
| 3 | 10선 `R1`~`R4`·`C1`~`C4`·`D1`·`D2` 모두 검사하는가? | SC1 | [ ] |
| 4 | `fail` 시 틀린 선 **전부** `failed_lines`에 있는가? | SC2 | [ ] |
| 5 | `incomplete` 시 `failed_lines`가 `[]` 인가? | SC3 | [ ] |
| 6 | `MAGIC_CONSTANT` import, `34` 리터럴 없음? | — | [ ] |
| 7 | pass / fail / incomplete 테스트 ≥3? | SC3 | [ ] |
| 8 | `pytest tests/test_validate_lines.py -v` green? | SC3 | [ ] |
| 9 | RED에서 `src/` 미수정, GREEN에서 assert 미완화? | — | [ ] |
| 10 | 풀이·UI·LLM·3×3 일반화 **제외**? | — | [ ] |

## ARRR 커맨드 추적

| Phase | 커맨드 | 실행 | pytest |
|-------|--------|------|--------|
| Arrange | `/red-test-plan` | [ ] | — |
| Arrange | `/golden-master` | [ ] | — |
| Red | `/red-skeleton` | [ ] | failed ✓ |
| Red | `/tdd-red` | [ ] | failed ✓ |
| Run Green | `/green-minimal` | [ ] | passed ✓ |
| Refine | `/refactor-smell` | [ ] | — |
| Refine | `/refactor-safe` | [ ] | passed ✓ |
| Export | `/export-session` | [ ] | — |

*템플릿: `.cursor/skills/magic-square-docs/templates/checklist.template.md`*
