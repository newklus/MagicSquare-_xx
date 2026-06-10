# /refactor-safe — validate_lines REFACTOR 안전 정리

MagicSquare_XX TDD 사이클 **Refine 2단계 — safe refactor**.  
**동작 변경 없이** 중복·이름·구조만 정리한다. 매 변경 후 `pytest` green 유지.

**추가 입력 없이 즉시 실행.** 사용자가 `/refactor-safe` 만 입력했다.  
(있으면) 직전 `/refactor-smell` P1 항목 또는 코드에서 자동 감지한 smell부터 **최소 diff**로 정리한다. 추가 질문·확인 요청 금지.

---

## Phase 선언 (필수)

```
[Phase: REFACTOR]
```

---

## Safe Refactor 절차

| 단계 | 할 일 |
|------|--------|
| 1 | `pytest tests/test_validate_lines.py -v` — 시작 시 green 확인 |
| 2 | **한 가지 smell**만 수정 (extract helper, 상수 정리, fixture 통합 등) |
| 3 | `pytest` 재실행 — green 유지 |
| 4 | 2~3 반복 (한 턴에 1~3 smell, 각각 pytest) |
| 5 | 보고 |

허용: private helper 추출, `LINE_NAMES` 순회 통합, golden fixture import, 변수명 개선.  
금지: API 시그니처·반환 키·status 의미 변경, 새 기능(풀이·UI).

---

## 리팩터 패턴 예시

```python
# Before: 10선 합산 중복
# After: _line_sum(grid, cells) helper — validate_lines 시그니처·ValidateResult 불변

def _cells_for_line(name: str) -> list[tuple[int, int]]:
    ...

def validate_lines(grid: list[list[int]]) -> ValidateResult:
    ...
```

```python
# tests: 인라인 grid → golden fixture import
from tests.fixtures.grids import PASS_GRID, FAIL_D1_GRID  # 경로는 프로젝트 구조에 맞게
```

---

## 보고 형식

```markdown
## REFACTOR Safe 보고

| # | Smell | 변경 요약 | pytest |
|---|-------|-----------|--------|
| 1 | Duplicated line logic | `_line_sum` 추출 | green ✓ |
| … | … | … | … |

- **최종 pytest**: `N passed`
- **의도적 보류**: (범위·위험으로 미적용)
- **다음 단계**: 새 RED 케이스 → `/red-test-plan` 또는 `/export-session`
```

---

## 금지 (refactor-safe)

| 금지 | 이유 |
|------|------|
| 테스트 assert·기대값 변경 | 동작 변경 |
| skip / xfail | 우회 |
| `validate_lines` API·`.cursorrules` 계약 변경 | SSOT |
| green 깨진 채 다음 smell | 즉시 revert 또는 수정 |
| 풀이·UI·일반화 | 범위 밖 |
| 사용자에게 리팩터 항목 질문 | smell·P1 자동 적용 |

---

## 참조

- SSOT: `.cursorrules`, `docs/PRD.md`
- 선행: `/refactor-smell` (권장), GREEN green
- 후속: `/red-test-plan`(다음 사이클), `/export-session`(세션 기록)
