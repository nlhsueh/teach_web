# 課程教材重整討論歷程 (Discussion History)

本文件摘要了課程教材從原始結構到現狀的重整歷程，記錄了主要的需求變更與決策點。

---

### 1. 教材結構重整與範例隔離
- **提問/需求**：希望將 `ch06_django` 資料夾內的「教學文件」與「範例程式碼」分開，避免結構混亂。
- **處理摘要**：建立 `tennis_project` 子目錄專門存放 Django 實作代碼，將 `.md` 教學檔保留在根部，並從 `Topic10_cases` 救回 `members` app。

### 2. 教學內容深度強化 (Ch01 Web 概觀)
- **提問/需求**：調整 `ch01_web.md`，納入更現代、與資工系相關的技術概念。
- **處理摘要**：增加了渲染策略 (CSR/SSR/SSG)、API 模式 (REST/GraphQL/gRPC)、DevOps 生態 (Docker/CI/CD) 以及技術里程碑 (AJAX/Wasm)，並補足了視覺化圖表、重點標註、測驗題與 Q&A。

### 3. 新增後端關鍵模組 (資料庫與 HTMX)
- **提問/需求**：需要增加關於資料庫基礎與 HTMX + Django 整合的教學。
- **處理摘要**：建立了 `ch09_db_intro.md` (涵蓋 SQL/NoSQL, ACID, ORM) 與 `ch10_htmx.md` (比較 Django+HTMX 與 Django+React 架構)。

### 4. 安全性審核 (Security Audit)
- **提問/需求**：擔心程式碼中是否存在敏感資訊或安全性風險。
- **處理摘要**：進行了全域掃描，確認 `SECRET_KEY` 為開發用預設值，無洩漏任何私人金鑰或外部 API Key。

### 5. 整合 Tailwind CSS
- **提問/需求**：計畫在 Frontend 章節加入 Tailwind CSS 的介紹。
- **處理摘要**：撰寫 `ch05_tailwind.md` (初稿為 `ch03c`)，解釋實用優先 (Utility-first) 的概念及其與 Django/HTMX 的配合優勢。

### 6. 全局章節順序重編 (Sequential Renaming)
- **提問/需求**：希望章節名稱不要出現 a, b, c，改為統一、連續的 `ch01` 至 `ch13` 編號。
- **處理摘要**：
    - 將所有目錄與檔案重新編號（例如 `ch03b_CCS` -> `ch04_CCS`）。
    - 修正了所有 Markdown 檔案內部的超連結與 `README.md` 路徑。
    - 確保章節與目錄名稱一致。

### 7. 課程評量與 AI 使用政策 (README 更新)
- **提問/需求**：(由使用者自行更新) 在 README 中加入課程評量標準，並訂定 AI 輔助作業的相關規範 (prompt 揭露原則)。
- **處理摘要**：確立了「可以使用 AI 但必須註明並提供 prompt」的學術準則。
