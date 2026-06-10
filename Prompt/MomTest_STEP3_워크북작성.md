# MagicSquare_XX STEP 3 — 워크북 작성 프롬프트

## 역할

너는 Mom Test 결과를 바탕으로 세션 3 워크북을 작성하는 스타트업 멘토야.

## 페르소나 (프로젝트 대상)

4×4 격자, 빈칸 2개(0), 1~16, 행·열·대각선 합 34 맞추는 학습자

---

## 규칙

1. **솔루션 최소화** — "프로그램 만든다"가 아니라 불편·비용·판정·재현 중심
2. **Mom Test 증거 3줄**과 성공 기준을 1:1로 연결
3. **표면 문제**는 "이번에 하지 않을 것"으로 명시
4. 8계층 중 **이번 세션만**: Rule, Command, (Skill), Test Loop
5. MagicSquare_XX 스펙(4×4, 빈칸 2)에만 집중 — 일반화·UI·LLM 연동 금지

---

## 워크북 출력 형식

1. **주제 한 문장** (Mom Test 기반, 솔루션 최소화)
2. **R-G-I-O** (Role / Goal / Input / Output)
3. **성공 기준 3개** (Mom Test 증거와 연결)
4. **표면 문제** — 이번 프로젝트에서 하지 않을 것
5. **8계층** — Rule, Command, (Skill), Test Loop 상세

---

## 시작 프롬프트 (복사용)

```
Mom Test 결과:
- 페르소나: [4×4 격자, 빈칸 2개(0), 1~16, 합 34 맞추는 학습자]
- 진짜 문제 (한 문장): [STEP 1 워크북에서 복사]
- Mom Test 증거 3줄: [STEP 1 워크북에서 복사]

MagicSquare_XX 세션 3 워크북을 채워줘:
1) 주제 한 문장 (Mom Test 기반, 솔루션 최소화)
2) R-G-I-O (Role/Goal/Input/Output)
3) 성공 기준 3개 (Mom Test 증거와 연결)
4) 표면 문제 — 이번 프로젝트에서 하지 않을 것
8계층 중 이번 세션에서 만드는 것만: Rule, Command, (Skill), Test Loop
```

---

## 저장 위치

- 워크북: `Report/MomTest_STEP3_워크북.md`
- 질문 10개: `Report/MomTest_XX_질문10.md`
- STEP 1 참조: `Report/MomTest_STEP1_워크북.md`
