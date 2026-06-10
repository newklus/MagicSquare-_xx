# /green-minimal — validate_lines GREEN 최소 구현

MagicSquare_XX `validate_lines` TDD 사이클 **GREEN 전용 — Run Green**.  
`src/validate_lines.py`만 수정해 **현재 실패 중인 테스트를 통과**시킨다. 최소 코드만.

**추가 입력 없이 즉시 실행.** 사용자가 `/green-minimal` 만 입력했다.  
`pytest tests/test_validate_lines.py -v` 결과에서 **실패 테스트**를 읽고, 통과시키는 최소 구현만 `src/`에 추가한다. 추가 질문·확인 요청 금지.

---

## Phase 선언 (필수)

```
[Phase: GREEN]
```

---

## GREEN 절차

| 단계 | 할 일 |
|------|--------|
| 1. 실패 확인 | `pytest tests/test_validate_lines.py -v` — 실패 목록·메시지 파악 |
| 2. 최소 구현 | `src/validate_lines.py`의 `validate_lines` 본문만 추가·수정 |
| 3. 재실행 | 전체 `pytest` — **all passed** 확인 |
| 4. 보고 | 통과 수·변경 요약·REFACTOR 후보 한 줄 |

GREEN 원칙: **테스트가 요구하는 것만** 구현. 미래 케이스·일반화·헬퍼 남발 금지.

---

## 구현 가이드 (SSOT)

```python
# 반환 계약 — .cursorrules
{
    "status": "pass" | "fail" | "incomplete",
    "failed_lines": [...],  # fail일 때만 채움, 그 외 []
}
```

| status | 조건 |
|--------|------|
| `incomplete` | 격자에 `0`(빈칸) 존재 → `failed_lines: []`, 10선 합 검사 생략 가능 |
| `fail` | 빈칸 없음, 10선 중 하나 이상 합 ≠ `MAGIC_CONSTANT` |
| `pass` | 빈칸 없음, 1~16 각 1회, 10선 합 모두 `MAGIC_CONSTANT` |

- 10선: `LINE_NAMES` 순회 — `R1`~`R4`, `C1`~`C4`, `D1`, `D2`
- `MAGIC_CONSTANT` import·사용 (34 하드코딩 금지)
- `fail` 시 틀린 선 **전부** `failed_lines`에 포함

---

## pytest 확인

```bash
pytest tests/test_validate_lines.py -v
```

기대: **all passed**. 하나라도 실패면 GREEN 미완 — 테스트 수정 금지, `src/`만 조정.

---

## 보고 형식

```markdown
## GREEN 보고

- **해결한 실패**: `test_<이름>` (N건)
- **구현 요약**: (한 줄 — 예: 10선 합 검사 + incomplete 조기 반환)
- **pytest 결과**: `N passed`
- **의도적 미구현**: (없음 / 다음 RED에서 다룰 항목)
- **다음 단계**: `/refactor-smell` — green 유지 리팩터 검토
```

---

## 금지 (GREEN)

| 금지 | 이유 |
|------|------|
| `tests/` assert 완화·삭제 | 요구사항 변경 아님 |
| skip / xfail | 우회 |
| REFACTOR성 대규모 구조 변경 | `/refactor-safe`에서 |
| 풀이·자동 채우기·UI | 범위 밖 |
| 사용자에게 구현 방식 질문 | 실패 메시지·SSOT로 결정 |

---

## 참조

- SSOT: `.cursorrules`, `docs/PRD.md`
- 선행: `/tdd-red` 또는 완전한 RED assert
- 후속: `/refactor-smell` → `/refactor-safe`
