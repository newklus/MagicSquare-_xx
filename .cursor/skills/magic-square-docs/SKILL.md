---
name: magic-square-docs
description: >-
  MagicSquare_XX 세션 보고서·Transcript·ARRR 체크리스트를 Report/·Prompting/에
  생성한다. export-session, /export, 세션 export, REPORT, Transcript, 체크리스트
  요청 시 적용. .cursor/commands/export-session.md 형식 준수.
---

# MagicSquare_XX Docs Export

## 범위

- `Report/NN.REPORT.md` — 세션 요약
- `Prompting/NN.Export-Transcript.md` — 대화 전문
- (선택) ARRR 체크리스트 — 템플릿 기반 채팅 출력 또는 `Report/` 저장

SSOT: `.cursorrules`, `docs/PRD.md`, `.cursor/commands/export-session.md`

## /export-session (즉시 실행)

**추가 입력·질문 금지.** 슬래시만으로:

1. `Report/`·`Prompting/`에서 `NN.*` 최대 번호 + 1 (2자리)
2. **현재 채팅 전체**에서 주제·산출물·User/Cursor 턴 추출
3. 템플릿으로 **2파일 직접 생성**
4. 짧게 보고: 번호, 경로, 주제 한 줄

별칭: `/export`

## 번호 규칙

- `01`, `02`, … — 기존 파일 **덮어쓰기 금지**
- `REPORT.md` 단독명 금지 → 반드시 `NN.REPORT.md`

## 템플릿

| 용도 | 파일 |
|------|------|
| 보고서 | [templates/report.template.md](templates/report.template.md) |
| Transcript | [templates/transcript.template.md](templates/transcript.template.md) |
| ARRR 체크리스트 | [templates/checklist.template.md](templates/checklist.template.md) |

`{…}` placeholder를 세션 내용으로 치환. 프로젝트명은 **MagicSquare_XX** (보고서 제목·메타).

## 보고서 필수 섹션

1. **요약** — 2~4문장
2. **핵심 결정·산출물** — 표 (결정 / 파일 / ARRR Phase)
3. **다음 단계** — 번호 목록 + 다음 커맨드

Transcript: User/Cursor **전문** (요약 아님), 마지막에 파일 목록 표.

## 체크리스트 사용

- TDD·ARRR 세션 종료 또는 `/refactor-safe` 후
- [templates/checklist.template.md](templates/checklist.template.md) 항목을 채팅에 표로 출력
- 미완 `[ ]` 항목 → 다음 `/red-test-plan` 등 제안 (질문 없이)

## 금지

- 세션 주제·번호 **사용자에게 질문**
- Transcript만 / 보고서만 생성
- Transcript 요약본 (전문 필수)
- git commit·push (명시 요청 시만)

## 참조 예시

- `Report/01.REPORT.md`
- `Prompting/01.Export-Transcript.md`
- `.cursor/commands/export-session.md` (동일 톤)
