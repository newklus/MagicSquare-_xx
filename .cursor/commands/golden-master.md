# /golden-master — validate_lines Golden Fixture

MagicSquare_XX TDD **Arrange — 참조 격자(fixture) 정의**.  
`tests/`에 **golden master** 4×4 격자 상수·헬퍼를 추가한다. `src/`는 수정하지 않는다.

**추가 입력 없이 즉시 실행.** 사용자가 `/golden-master` 만 입력했다.  
`.cursorrules`·Mom Test SC1~3·(있으면) `/red-test-plan` 계획에서 **pass / fail / incomplete** 각 1개 이상 fixture를 `tests/`에 추가한다. 추가 질문·확인 요청 금지.

---

## Phase 선언 (필수)

```
[Phase: RED — Arrange (Golden)]
```

---

## Golden Master란

| 유형 | 용도 | status 기대 |
|------|------|-------------|
| **PASS_GRID** | 완성 마방진 — 10선=34, 1~16 각 1회 | pass |
| **FAIL_*_GRID** | 완성 격자, 특정 선만 깨짐 | fail + `failed_lines` |
| **INCOMPLETE_*_GRID** | `0` 빈칸 포함 | incomplete, `failed_lines: []` |

테스트·구현·리뷰가 **동일 격자**를 재사용하도록 SSOT fixture로 둔다.

---

## 절차

| 단계 | 할 일 |
|------|--------|
| 1 | `tests/test_validate_lines.py` 상단 또는 `tests/fixtures/grids.py`에 상수 정의 |
| 2 | PASS 1개 + FAIL(D1 등 SC1 연결) 1개 + INCOMPLETE 1개 이상 |
| 3 | 각 fixture에 **한 줄 주석**: 어떤 선·SC를 검증하는지 |
| 4 | `MAGIC_CONSTANT`는 import — 격자 숫자는 리터럴 OK, assert에서 `34` 금지 |
| 5 | (선택) `pytest` — fixture만 추가했으면 기존 테스트 수집 변화 없음 확인 |

---

## fixture 예시

```python
# tests/test_validate_lines.py (또는 tests/fixtures/grids.py)

from validate_lines import MAGIC_CONSTANT, LINE_NAMES, validate_lines

# Golden PASS — 4×4 완성 마방진, 10선 = MAGIC_CONSTANT
PASS_GRID: list[list[int]] = [
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1],
]

# Golden FAIL — D1만 깨짐 (SC1: 대각선 검사)
FAIL_D1_GRID: list[list[int]] = [row[:] for row in PASS_GRID]
FAIL_D1_GRID[0][0] = 15

# Golden INCOMPLETE — 빈칸 2개 (SC3: incomplete 경로)
INCOMPLETE_GRID: list[list[int]] = [row[:] for row in PASS_GRID]
INCOMPLETE_GRID[0][0] = 0
INCOMPLETE_GRID[3][3] = 0
```

---

## 보고 형식

```markdown
## Golden Master 보고

| Fixture | status 기대 | failed_lines (fail만) | Mom Test |
|---------|-------------|------------------------|----------|
| `PASS_GRID` | pass | — | SC3 |
| `FAIL_D1_GRID` | fail | `["D1"]` | SC1 |
| `INCOMPLETE_GRID` | incomplete | `[]` | SC3 |

- **파일**: `tests/...`
- **다음 단계**: `/red-skeleton` 또는 `/tdd-red`에서 import 재사용
```

---

## 금지 (golden-master)

| 금지 | 이유 |
|------|------|
| `src/` 수정 | fixture는 tests/만 |
| assert 없는 테스트 대량 추가 | `/red-skeleton`·`/tdd-red` 역할 |
| `row_0`·`diag_main` 이름 | `R1`~`D2` enum만 |
| GREEN·REFACTOR | Arrange 단계 |
| 사용자에게 격자 값 질문 | SSOT·표준 마방진 예시 사용 |

---

## 참조

- SSOT: `.cursorrules`, `docs/PRD.md`
- 후속: `/red-skeleton`, `/tdd-red`, `/green-minimal`(fixture 재사용)
