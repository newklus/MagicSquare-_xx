# /tdd-red — validate_lines RED 단계

MagicSquare_XX `validate_lines` TDD 사이클의 **RED** 전용.  
`tests/`만 수정한다. `src/`·`pyproject.toml`·`.cursorrules`는 건드리지 않는다.

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 선언:

```
[Phase: RED]
```

---

## RED 절차 — AAA

| 단계 | 할 일 |
|------|--------|
| **Arrange** | 4×4 격자 fixture 준비. `MAGIC_CONSTANT`·`LINE_NAMES`는 `validate_lines`에서 import (34 하드코딩 금지). |
| **Act** | `result = validate_lines(grid)` 호출. |
| **Assert** | `result["status"]`, `result["failed_lines"]`를 API 계약대로 검증. 실패 원인이 **구현 부재**인지 확인. |

RED 완료 조건: `pytest` 실행 시 **새 테스트가 실패**한다 (NotImplementedError·AssertionError 등).  
통과하면 RED가 아니다 — assert를 완화하지 말고 기대값을 유지한다.

---

## pytest 예시

`tests/test_validate_lines.py`에 추가하는 실패 테스트 예시:

```python
from validate_lines import MAGIC_CONSTANT, validate_lines


def test_fail_reports_d1_when_only_main_diagonal_wrong():
    # Arrange: D1만 합이 MAGIC_CONSTANT가 아닌 완성 격자
    grid = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1],
    ]
    grid[0][0] = 15  # D1 합만 깨뜨림

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "fail"
    assert "D1" in result["failed_lines"]
```

실행:

```bash
pytest tests/test_validate_lines.py -v
```

기대: **FAILED** (현재 `validate_lines`는 미구현이므로 RED 성공).

---

## 보고 형식

RED 작업 후 아래 형식으로 보고한다:

```markdown
## RED 보고

- **대상 테스트**: `test_<이름>`
- **검증 의도**: (pass / fail / incomplete 중 무엇을 검증하는지 한 줄)
- **Mom Test 연결**: (SC1 대각선 / SC2 failed_lines / SC3 pytest 루프 중 해당)
- **pytest 결과**: `1 failed, N passed` (실패 메시지 한 줄 인용)
- **다음 단계**: GREEN — `src/validate_lines.py` 최소 구현
```

---

## 금지 (RED)

| 금지 | 이유 |
|------|------|
| `src/` 수정 | GREEN까지 구현 연기 |
| assert 완화·삭제·주석 처리 | 실패를 숨기면 RED가 무효 |
| `@pytest.mark.skip` / `xfail` | 우회 금지 |
| `pass`만 있는 테스트 | 검증 없음 = RED 아님 |
| `34` 리터럴 | `MAGIC_CONSTANT` SSOT 위반 |
| GREEN·REFACTOR 동시 수행 | 사이클 분리 위반 |

---

## 참조

- API: `validate_lines(grid) -> {status: pass\|fail\|incomplete, failed_lines: [...]}`
- 10선: `R1`~`R4`, `C1`~`C4`, `D1`, `D2`
- 상세 규칙: 프로젝트 루트 `.cursorrules`
