# Web 應用程式開發 (Web Application Development)


## 🚀 課程目標 (Course Objectives)

本課程旨在引導學生建立完整的 Web 專案開發認知，不僅學習撰寫程式碼，更深入理解網路架構、資料通訊與工程實務。

-   **核心基礎**：掌握 HTTP 協定、瀏覽器渲染機制。
-   **前端技術**：精通 HTML5, CSS3 與現代 JavaScript。
-   **後端架構**：使用 Python Django 框架建立穩健的應用程式。
-   **現代化開發**：探索 HTMX 與 React 的差異，理解 DevOps、Docker 與資料庫設計。
-   **使用者體驗**：探討良好使用體驗的網頁設計。

---


## 📁 教材目錄 (Table of Contents)

### [Topic 01] Web 與 HTTP 基礎
-   **Ch01: Web 概觀 ([ch01_web.md](Topic01_Intro/ch01_web.md))**：從 Web 1.0 到 3.0，AJAX、WebAssembly 等關鍵技術突破。
-   **Ch02: HTTP 協定 ([ch02_http.md](Topic01_Intro/ch02_http.md))**：請求/回應結構、狀態碼、HTTPS 與 HTTP/2。

### [Topic 02] 前端開發 (Frontend)
-   **Ch03: HTML 結構 ([ch03_html.md](Topic02_frontend/ch03_html.md))**：語義化標籤與頁面架構。
-   **Ch04: CSS 樣式與設計 ([css.md](Topic02_frontend/ch04_CCS/css.md))**：Flexbox, Grid 與視覺設計。
-   **Ch05: Tailwind CSS ([ch05_tailwind.md](Topic02_frontend/ch05_tailwind.md))**：實用優先 (Utility-first) 現代化開發。
-   **Ch06: JavaScript 動態互動 ([js.md](Topic02_frontend/ch06_Javascript/js.md))**：DOM 操控與非同步程式設計。

### [Topic 03] 後端系統與框架 (Backend)
-   **Ch07: Python 基礎 ([python.md](Topic03_backend/ch07_Python/python.md))**：語言特性、常用語法與 Web 開發應用。
-   **Ch08: Django 應用基礎 ([ch08_django.md](Topic03_backend/ch08_django/ch08_django.md))**：MVT 架構實務，網球俱樂部專案。
-   **Ch09: 資料庫概論 ([ch09_db_intro.md](Topic03_backend/ch08_django/ch09_db_intro.md))**：SQL vs NoSQL、ACID 特性與資料模型設計。
-   **Ch10: HTMX 深入探討 ([ch10_htmx.md](Topic03_backend/ch08_django/ch10_htmx.md))**：比較 Django+HTMX 與 Django+React 的架構抉擇。

### [Topic 04] 框架與進階實務 (Frameworks)
-   **Ch11: UX 設計 (Topic03_framework/ch11_UX/)**
-   **Ch12: Bootstrap 實務 (Topic03_framework/ch12_BS/)**
-   **Ch13: Vue 框架 ([readme.md](Topic03_framework/ch13_Vue/readme.md))**

---

## 💡 教材特色

為了提升教學效果，我們在教材中加入了多種互動與強化元素：

-   **💡 重點觀念 (Key Points)**：標註核心考點與開發必備知識。
-   **⚠️ 小提示 (Warnings)**：提醒常見陷阱與安全性建議。
-   **✍️ 自我測驗 (Self-Tests)**：隨堂練習與解答，幫助學生自我檢核。
-   **🛠️ 實作演練 (Practical Exercises)**：手把手的 Lab 練習，強調「做中學」。
-   **🖼️ 視覺化圖表**：包含架構圖與流程圖，輔助理解抽象概念。

---

## 🛠️ 開發環境與組織

本倉庫採用的組織方式旨在分離「教學內容」與「實際範例程式碼」：

-   **教學文件**：位於各個 `Topic/` 目錄下的 `.md` 檔案。
-   **範例專案**：例如 `Topic03_backend/ch08_django/tennis_project/`，包含完整的 Django 專案結構。


## 🤖 AI 應用：你的最佳助教

我們鼓勵每位同學積極運用 AI（如 ChatGPT, Claude, GitHub Copilot）作為學習夥伴。**相信自己，每個人都有能力學好 Web 開發！** 我們的目標是全班 **All Pass**，一起跨越技術門檻。

### 💡 為什麼要用 AI？
AI 不只是用來產出答案，更是幫助你「跨越卡關」的教練。透過 AI，你可以更快速地理解抽象概念（如非同步處理、MVT 架構），並在遇到 Bug 時獲得即時的解法提示。

### 🛠️ 推薦的 AI 學習方法
1.  **解釋觀念**：遇到不懂的標籤或邏輯，可以問：「請用淺顯易懂的方式解釋 HTML 的 `flexbox` 佈局。」
2.  **解讀程式碼**：將看不懂的範例貼給 AI，要求它「逐行解釋這段程式碼的邏輯與用途」。
3.  **錯誤偵修**：執行出現紅字時，貼上錯誤訊息問：「為什麼我的 Django 畫面出現 `TemplateDoesNotExist`？該如何處理？」
4.  **練習生成**：要求 AI 為你產出練習題：「請給我三個關於 CSS 選擇器的基礎練習題。」

### 為什麼不能只會用AI？
1. AI 產出的程式碼不一定正確，除錯可能更花時間
2. AI 或許會貴到你用不起
3. 資工系除了工具，更需知道核心，也要保持手感

### ⚠️ 重要提醒
-   **學習過程儘量用 AI**：它是你最強大的輔助，能幫你節省大量的摸索時間。
-   **考試展現真本事**：作業可以 AI 輔助，但考試時（特別是觀念與程式題）需要展現你具備「手寫 Code」與「理解架構」的核心能力。
-   **理解大於複製**：別只是複製貼上。請確保你搞懂 AI 給你的每一行程式碼，因為未來的開發者，比的是「誰能更好地調教 AI」，而不是誰會打字。

**加油！讓我們一起利用現代工具，把 Web 開發學到手！🚀**