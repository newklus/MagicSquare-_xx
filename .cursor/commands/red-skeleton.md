# /red-skeleton — validate_lines RED 테스트 골격

MagicSquare_XX `validate_lines` TDD 사이클 **RED 준비 2단계 — Red(skeleton)**.  
`tests/test_validate_lines.py`에 **AAA 골격**만 추가한다. assert는 **의도적 실패** 또는 `pytest.fail("RED: assert 미작성")` 수준까지.

**추가 입력 없이 즉시 실행.** 사용자가 `/red-skeleton` 만 입력했다.  
`.cursorrules`·기존 테스트·(있으면) 직전 `/red-test-plan` 계획표에서 **우선 1건**을 골라 skeleton을 작성한다. 추가 질문·확인 요청 금지.

---

## Phase 선언 (필수)

```
[Phase: RED — Skeleton]
```

---

## 절차 — AAA 골격

| 단계 | 할 일 |
|------|--------|
| **Arrange** | 4×4 `grid` fixture. `MAGIC_CONSTANT`·`LINE_NAMES`는 `validate_lines`에서 import |
| **Act** | `result = validate_lines(grid)` |
| **Assert** | `result["status"]`, `result["failed_lines"]` 검증 **자리**만 마련. 미완이면 반드시 실패하도록 작성 |

RED skeleton 완료: `pytest` 실행 시 **새 테스트가 FAILED** (NotImplementedError·AssertionError·명시적 fail).

---

## pytest 골격 예시

```python
from validate_lines import LINE_NAMES, MAGIC_CONSTANT, validate_lines


def test_fail_reports_d1_when_only_main_diagonal_wrong():
    # Arrange — golden fixture 또는 인라인 grid
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]
    grid[0][0] = 15  # D1 합만 MAGIC_CONSTANT에서 벗어남

    # Act
    result = validate_lines(grid)

    # Assert — RED: 구현 전이므로 실패해야 함
    assert result["status"] == "fail"
    assert "D1" in result["failed_lines"]
```

실행:

```bash
pytest tests/test_validate_lines.py -v -k test_fail_reports_d1
```

---

## 보고 형식

```markdown
## RED Skeleton 보고

- **대상 테스트**: `test_<이름>`
- **검증 의도**: (pass / fail / incomplete)
- **AAA 상태**: Arrange ✓ / Act ✓ / Assert (완료|골격)
- **Mom Test**: SC1 | SC2 | SC3
- **pytest 결과**: `1 failed, N passed` (한 줄)
- **다음 단계**: assert 보강·추가 케이스 → `/tdd-red` 또는 `/green-minimal` 전 `/tdd-red` 완료
```

---

## 금지 (red-skeleton)

| 금지 | 이유 |
|------|------|
| `src/` 수정 | GREEN까지 연기 |
| assert 완화·삭제·skip/xfail | RED 무효 |
| `34` 리터럴 | `MAGIC_CONSTANT` SSOT |
| `row_0`·`diag_main` 등 구 이름 | `R1`~`R4`, `C1`~`C4`, `D1`, `D2`만 |
| GREEN·REFACTOR 동시 | 사이클 분리 |
| 사용자에게 테스트명 질문 | 계획·갭에서 자동 선택 |

---

## 참조

- SSOT: `.cursorrules`, `docs/PRD.md`
- 선행: `/red-test-plan`, (선택) `/golden-master`
- 후속: `/tdd-red`(assert 확정) → `/green-minimal`
