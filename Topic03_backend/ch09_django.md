# Ch09 Django Application

## Django 簡介與背景

Django 是一個基於 Python 的高階 Web 開發框架，最初於 2003 年由 Lawrence Journal-World 報社的 Web 開發團隊所設計，並於 2005 年以開源形式釋出。Django 遵循「快速開發 (Rapid Development)」與「不要重複自己 (DRY, Don't Repeat Yourself)」的原則，旨在讓開發者能以最快的速度將專案概念轉化為實體網站。

### 核心優點
* **功能完備 (Batteries-Included)**：內建了極為強大的管理後台 (Admin Page)、物件關係映射 (ORM)、使用者認證系統 (Auth)、Session 管理與表單驗證等功能，開發者不需自行組裝繁瑣的基礎架構。
* **安全防護健全 (Highly Secure)**：預設提供了高水準的安全防護，自動防範了常見的網路攻擊（如 SQL 注入、跨站指令碼 XSS、跨站請求偽造 CSRF 以及網頁劫持 Clickjacking），避免開發者因疏忽留下資安漏洞。
* **極佳的擴展性 (Scalable)**：採用高度模組化的「App」概念設計，不僅便於團隊分工，更被證實能輕鬆應對數億級別的超高流量。
* **強大的 Python 生態系支援**：以 Python 為核心，能夠與數據分析、人工智慧、機器學習（如 Pandas, TensorFlow 等）無縫整合，非常適合作為智慧型應用的後端支撐。

### 發展趨勢
* **AI 服務的核心後台**：在人工智慧（AI）浪潮下，Python 成為絕對的核心語言。Django 作為 Python 生態中最穩定、最成熟的 Web 框架，正被大量用於搭建 AI 系統的 API 平台與管理控制後台。
* **前後端分離與 API 化**：搭配 Django REST Framework (DRF) 或高效的 Django Ninja，Django 已演進為強大的「Headless API 服務」，與前端現代框架（React, Vue, Next.js）相得益彰。

### 現有使用狀況
Django 在全球被廣泛應用於許多高流量的科技巨頭與新創平台，其中包含：
* **Instagram**：全球規模最大的 Django 部署實例，處理每日數十億的動態牆與相片分享。
* **Spotify**：大量使用 Django 處理後台的數據流程、分析與音樂推薦系統。
* **Pinterest**、**Disqus**、**YouTube**、**Bitbucket** 等網站，在其系統架構或核心管理功能中皆高度仰賴 Django。

---

## 本章節拆分導覽

本章內容已依據小節拆分為以下檔案，供同學依序學習：

* [9.1 基礎操作與環境安裝](ch09.1_setup.md)
* [9.2 網球俱樂部 (I) - 專案與視界設計](ch09.2_mvt.md)
* [9.3 網球俱樂部 (II) - 資料庫、表單與主版頁面](ch09.3_app.md)
* [9.4 網球俱樂部 (III) - 認證、靜態檔、上傳與關聯綁定](ch09.4_adv.md)
* [9.5 HW/Quiz (作業與測驗)](ch09.5_django.md)
* [9.x 附錄：資料庫概論 (Database Introduction)](ch09.x_db.md)
