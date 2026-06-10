# /red-test-plan — validate_lines RED 테스트 계획

MagicSquare_XX `validate_lines` TDD 사이클 **RED 준비 1단계 — Arrange(계획)**.  
테스트 **계획표만** 작성한다. `tests/`·`src/` 코드는 아직 수정하지 않는다.

**추가 입력 없이 즉시 실행.** 사용자가 `/red-test-plan` 만 입력했다.  
현재 채팅·`.cursorrules`·`docs/PRD.md`(있으면)·`tests/test_validate_lines.py` import 상태에서 SSOT를 읽고 계획을 만든다. 추가 질문·확인 요청 금지.

---

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 선언:

```
[Phase: RED — Arrange]
```

---

## 절차

| 단계 | 할 일 |
|------|--------|
| 1. SSOT 확인 | `.cursorrules` API 계약·10선 이름·`MAGIC_CONSTANT` SSOT·3방향 케이스(pass/fail/incomplete) |
| 2. 갭 점검 | `tests/test_validate_lines.py`에 이미 있는 테스트·누락 케이스 파악 |
| 3. 계획표 작성 | 아래 **테스트 계획표** 형식으로 **다음에 쓸 테스트** 목록 확정 |
| 4. Mom Test 연결 | 각 행에 SC1~SC3 중 해당 증거 매핑 |
| 5. 보고 | 계획표 + 다음 커맨드(`/red-skeleton` 또는 `/golden-master`) 한 줄 |

---

## 테스트 계획표 (출력 형식)

```markdown
## RED 테스트 계획

| # | 테스트 함수명(예정) | status | failed_lines 기대 | 격자 요약 | Mom Test |
|---|---------------------|--------|-------------------|-----------|----------|
| 1 | `test_pass_...` | pass | `[]` | 완성 4×4, 10선=34 | SC3 |
| 2 | `test_fail_...` | fail | `["D1", ...]` | 완성, D1만 깨짐 | SC1 |
| 3 | `test_incomplete_...` | incomplete | `[]` | 0(빈칸) 1개 이상 | SC3 |
| … | … | … | … | … | … |

- **우선 작성 1건**: (다음 `/red-skeleton` 대상)
- **golden fixture 필요**: (예/아니오 — 필요 시 `/golden-master` 선행)
- **금지 확인**: 34 리터럴·`row_0` 등 구 이름·`line_sums` 필드 사용 없음
```

최소 **3방향**(pass / fail·failed_lines / incomplete) 각 1건 이상 계획에 포함한다.

---

## 10선·격자 규칙 (계획 시 SSOT)

| 선 | 이름 | 좌표 (0-indexed row, col) |
|----|------|---------------------------|
| 행 | R1~R4 | row 0~3 전체 |
| 열 | C1~C4 | col 0~3 전체 |
| 주대각 | D1 | (0,0)(1,1)(2,2)(3,3) |
| 부대각 | D2 | (0,3)(1,2)(2,1)(3,0) |

- 마법상수: `MAGIC_CONSTANT`(34) — 계획서에 `34` 단독 기재 지양, `MAGIC_CONSTANT`로 표기
- `fail` 케이스: 틀린 선 **전부** `failed_lines`에 나열할 것을 계획에 명시

---

## 금지 (red-test-plan)

| 금지 | 이유 |
|------|------|
| `tests/`·`src/` 수정 | 계획 단계 — 코드는 `/red-skeleton` 이후 |
| pytest 실행 | 아직 테스트 없음 |
| 사용자에게 케이스 선택 질문 | SSOT·갭 분석으로 자동 결정 |
| GREEN·REFACTOR 동시 계획 | Phase 분리 |

---

## 참조

- SSOT: `.cursorrules`, `docs/PRD.md`, `src/validate_lines.py` (`LINE_NAMES`, `MAGIC_CONSTANT`)
- 다음: `/golden-master`(fixture) → `/red-skeleton` → `/tdd-red`
- Mom Test SC: SC1 대각선·10선, SC2 failed_lines, SC3 pytest 3케이스
