###### tags: `Web`

# Ch03 HTML 結構與基礎應用 🏗️

本章節介紹 HTML 的核心結構與常用標記，這是構建現代 Web 應用程式的基礎。

---

## 3.1 開發環境與基本結構 🛠️

### 3.1.1 VS Code 開發技巧
*   **Emmet 快速輸入**：輸入 `!` 並按 `Tab` 鍵，可快速生成 HTML5 標準骨架。
*   **Live Server**：安裝此擴充套件後，右鍵點擊 "Open with Live Server" 即可即時預覽變更。
*   **Auto Rename Tag**：自動同步修改成對的標籤。

### 3.1.2 HTML5 標準骨架
```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3.1.2 標題範例</title>
</head>
<body>
    <!-- 網頁內容寫在這裡 -->
</body>
</html>
```

---

## 3.2 常用標記與屬性 🏷️

### 3.2.1 文本元素 (Text)
*   `<h1>` ~ `<h6>`: 用於設定標題層級，SEO 的關鍵。
*   `<p>`: 定義文字段落。
*   `<strong>` / `<em>`: 加粗或斜體，強調語氣。

### 3.2.2 媒體與連結 (Media)
*   `<a href="...">`: 建立超連結。
*   `<img src="..." alt="...">`: 顯示圖片，`alt` 屬性有利於無障礙閱讀。

### 3.2.3 容器與排版 (Layout)
*   `<div>` (Block): 區塊級元素，佔據整行。
*   `<span>` (Inline): 行內元素，只佔據其內容寬度。
*   **語意化標籤**: `<header>`, `<nav>`, `<main>`, `<article>`, `<footer>`。

---

## 3.3 進階組件：表格與表單 📝

### 3.3.1 表格結構 (Table)
使用 `<table>`, `<tr>` (行), `<th>` (標題) 與 `<td>` (內容)。
> [!TIP]
> 建議使用 `border-collapse: collapse;` 讓邊距重合，視覺更簡潔。

### 3.3.2 表單與輸入 (Form)
*   **基本屬性**: `<form action="..." method="POST">`。
*   **輸入控制**:
    - `<input type="text">`: 文字
    - `<input type="password">`: 密碼
    - `<input type="radio">` 與 `<input type="checkbox">`: 選擇題
    - `<input type="date">` / `<input type="file">`: 日期與檔案
*   **下拉選單**: `<select>` 與 `<option>`。

---

## 3.4 自我測驗 ✍️

請先閱讀上述內容後，再嘗試回答以下問題：

1. **HTML 文檔的根元素是什麼？**
   <details>
   <summary>點擊查看答案</summary>
   答案：`<html>`
   </details>

2. **哪一個屬性用於為圖片提供替代文字？**
   <details>
   <summary>點擊查看答案</summary>
   答案：`alt`
   </details>

3. **Block 元素與 Inline 元素最大的差別在於？**
   <details>
   <summary>點擊查看答案</summary>
   答案：Block 元素會佔據整個可用寬度並自動換行；Inline 元素則只佔據內容空間。
   </details>

---

## 3.5 實作演練 🛠️

### 練習一：個人名片網頁
1. 建立一個包含 `<div>` 容器的頁面。
2. 使用 `<h1>` 標註姓名，並放入一張個人/明星頭像 (`<img>`)。
3. 利用 `<ul>` 列出 3 項興趣。
4. 加入一個 `<table>` 列出你的學習歷程（學校、時間、專業）。

### 練習二：棒球球員報名表
1. 實作一個包含 `姓名` (text)、`守備位置` (select) 的表單。
2. 加入 `打擊習慣` 的單選鈕 (`radio`)。
3. 加入 `慣用手` 的核取方塊 (`checkbox`)。
4. 最終需有一個「提交」按鈕。

---

> [!NOTE]
> **💡 重點摘要**：HTML 負責網頁的「骨架」，好的結構與語意化標籤（Semantic tags）能提升網站的搜尋排名與維權性。