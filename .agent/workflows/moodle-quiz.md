---
description: 建立 Moodle 雙語題庫 (ZH/EN) 並符合教學規範
---

# 建立 Moodle 題庫工作流 (Moodle Quiz Workflow)

當使用者要求建立新題目或修改現有 Moodle XML 題庫時，必須嚴格遵守以下步驟：

## 1. 讀取現有規範
讀取位於 `exam/114-2 quiz/moodle_quiz_rules.md` 的最新出題規範。

## 2. 產出 XML 內容 (Generation)
- **分類**：一律使用 `examA/chXX` 或 `examB/chXX`。
- **雙語**：敘述採 `中文 (English)` 格式。
- **純代碼**：CSS 選項、JS 關鍵字、SQL 語句等誘答選項，一律維持純英文代碼，**禁止翻譯**。
- **標註語言**：題幹開頭必須加上「在 [技術名稱] 中，...」。

## 3. 代碼安全 (CDATA)
- 確保所有包含 HTML 的 `<text>` 區塊皆被 `<![CDATA[ ... ]]>` 包裹。

## 4. 執行預覽驗證 (Verification)
// turbo
1. 在終端機執行 `node preview_quiz.js` 以產生 `quiz_preview.html`。
2. 檢查產出的 HTML 以確認選項與題幹符合規範。

## 5. 完成交付
告知使用者已更新 XML 並提供 `quiz_preview.html` 連結。
