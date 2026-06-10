# /refactor-smell — validate_lines REFACTOR Smell 리뷰

MagicSquare_XX TDD 사이클 **Refine 1단계 — smell 감사**.  
`src/validate_lines.py`·`tests/test_validate_lines.py`를 **읽기만** 하고 smell 목록을 표로 보고한다. **파일 수정 금지.**

**추가 입력 없이 즉시 실행.** 사용자가 `/refactor-smell` 만 입력했다.  
현재 코드·테스트·`.cursorrules`를 읽고 smell을 분류한다. 추가 질문·확인 요청 금지.

---

## Phase 선언 (필수)

```
[Phase: REFACTOR — Smell Review]
```

---

## 절차

| 단계 | 할 일 |
|------|--------|
| 1 | `pytest tests/test_validate_lines.py -v` — **green 전제** 확인 (실패 시 GREEN 먼저 안내) |
| 2 | `src/validate_lines.py`·`tests/test_validate_lines.py` 정독 |
| 3 | 아래 smell 체크리스트로 **표만** 출력 |
| 4 | `/refactor-safe` 우선순위 1~3건 제안 |

---

## Smell 체크리스트

| # | Smell | 질문 | 심각도 |
|---|-------|------|--------|
| 1 | **Magic number** | `34` 리터럴이 `MAGIC_CONSTANT` 밖에 있는가? | 높음 |
| 2 | **Duplicated line logic** | 10선 합산 코드가 반복되는가? | 중간 |
| 3 | **Long function** | `validate_lines`가 한 함수에 모든 분기를 담는가? | 중간 |
| 4 | **Dead code** | 미사용 import·변수·분기 | 낮음 |
| 5 | **Weak test names** | `test_1` 등 의도 불명 | 중간 |
| 6 | **Fixture duplication** | 동일 grid가 여러 테스트에 복붙 | 낮음 |
| 7 | **Contract drift** | `.cursorrules`와 `failed_lines`·status 불일치 | 높음 |
| 8 | **Premature abstraction** | 케이스 3개 미만인데 과도한 클래스 계층 | 낮음 |

---

## 보고 형식 (출력만 — 파일 생성 없음)

```markdown
## REFACTOR Smell 보고

**pytest**: `N passed` (green ✓ | red ✗ — red면 `/green-minimal` 선행)

| # | 위치 | Smell | 설명 | 권장 조치 | 우선순위 |
|---|------|-------|------|-----------|----------|
| 1 | `src/...` | Magic number | … | `MAGIC_CONSTANT` 사용 | P1 |
| … | … | … | … | … | … |

- **P1 즉시**: (최대 3건, `/refactor-safe` 입력)
- **보류**: (동작 변경 위험·범위 밖)
- **다음 단계**: `/refactor-safe`
```

---

## 금지 (refactor-smell)

| 금지 | 이유 |
|------|------|
| 코드·테스트 수정 | smell **리뷰**만 |
| assert 완화 | REFACTOR 아님 |
| 범위 밖 리팩터(3×3 일반화 등) | `.cursorrules` 범위 |
| 사용자에게 smell 선택 질문 | 체크리스트로 자동 분류 |

---

## 참조

- SSOT: `.cursorrules`, `docs/PRD.md`
- 선행: GREEN all passed
- 후속: `/refactor-safe`
