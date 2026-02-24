###### tags: `Web`

# Ch03 HTML 結構與基礎應用 🏗️

本章節將深入探討 HTML 的核心結構、開發工具的使用技巧，以及如何利用各種標記構建功能豐富的網頁。

---

## Slide

[nlh Slide](https://docs.google.com/presentation/d/1W6qQwzzvZQ0OH97TqwBSL6uNfpBtBWPv7fz05woE3z8/edit?usp=sharing)
* Development Tool
* HTML structure
* Basic HTML Tag
* Table
* FORM

[W3School: HTML 教學](https://www.w3schools.com/html/default.asp)


---

## 3.1 開發工具：VS Code 與 HTML 🛠️

在 VS Code 開發 HTML 時，強大的功能與外掛能顯著提升效率。

### 3.1.1 為什麼選擇 VS Code？
*   **智能代碼補全**：內建代碼提示，自動完成標籤與屬性。
*   **擴展性強**：支援多種外掛，涵蓋即時預覽、格式化等。 
*   **輕量化**：資源占用低，開啟速度快。

### 3.1.2 必備外掛推薦 🔌
1.  **HTML Snippets**: 提供常用標籤的代碼片段。
2.  **Auto Close Tag**: 輸入 `<div>` 後自動補全 `</div>`。
3.  **Auto Rename Tag**: 修改起始標籤時，自動同步修改結尾標籤。
4.  **Live Server**: 建立本地伺服器，存檔後瀏覽器自動刷新即時預覽。 🚀
5.  **Prettier**: 自動美化縮排與代碼格式。

### 3.1.3 高效開發技巧 ⌨️
*   **Emmet 語法**：
    - `!` 或 `html:5` → 生成標準 HTML5 骨架。
    - `div.container>ul>li*5` → 快速生成嵌套結構。
*   **多光標編輯**：按住 `Alt` (Windows) / `Option` (Mac) 並點擊，可同時編輯多處。
*   **快速導航**：使用 `Ctrl+P` (Windows) / `Cmd+P` (Mac) 快速搜尋並開啟檔案。

---

## 3.2 HTML 基礎結構與常用標記 🏷️

### 3.2.1 HTML5 標準骨架
```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的網頁</title>
</head>
<body>
    <!-- 網頁內容寫在這裡 -->
</body>
</html>
```

### 3.2.2 核心文本元素
*   **標題 (`<h1>` - `<h6>`)**：代表權重，`<h1>` 為最高層級（通常一頁一個）。
*   **段落 (`<p>`)**：用於包裹成段的文字。
*   **強調 (`<strong>`, `<em>`)**：分別代表「加粗」與「斜體」，語意上表示強調。

### 3.2.3 列表與連結
*   **無序列表 (`<ul>` + `<li>`)**：用於點狀條列。
*   **有序列表 (`<ol>` + `<li>`)**：用於數字編號條列。
*   **超連結 (`<a>`)**：使用 `href` 屬性導向目標，`target="_blank"` 可在新分頁開啟。

---

## 3.3 元素的呈現行為與佈局 🏗️

網頁元素的排列方式主要由其顯示屬性（Display）決定。

### 3.3.1 Block vs Inline 概念
1.  **Block (區塊元素)**：
    - 佔滿整行寬度。
    - 前後會自動換行。
    - 可設定寬度 (`width`) 與高度 (`height`)。
    - 範例：`<div>`, `<p>`, `<h1>`, `<ul>`。
2.  **Inline (行內元素)**：
    - 只佔據內容所需的寬度。
    - 不會自動換行，與其他文字併排。
    - 無法設定寬高。
    - 範例：`<span>`, `<a>`, `<strong>`。
3.  **Inline-block**：結合兩者特色，不換行但可設定寬高。

### 3.3.2 語意化標籤 (Semantic HTML)
為了讓搜尋引擎 (SEO) 與輔助技術更好地理解內容，應使用具備意義的標籤：
*   `<header>`：頁頭（標誌或導航）。
*   `<nav>`：主導航列。
*   `<main>`：主要內容區。
*   `<article>` / `<section>`：獨立文章或主題區塊。
*   `<footer>`：頁尾資訊。

---

## 3.4 進階組件：表格 (Table) 📊

表格用於展示結構化數據。

### 3.4.1 基本結構
包含 `<table>`, `<tr>` (行), `<th>` (標題單元格), `<td>` (資料單元格)。

### 3.4.2 樣式美化技巧
利用 CSS 加強可讀性：
*   **合併邊框**：`border-collapse: collapse;`。
*   **斑馬紋效果**：利用 `tr:nth-child(even)` 設置背景色。
*   **內邊距**：增加 `padding` 讓文字不擠迫。

---

## 3.5 進階組件：表單 (Form) 📝

表單是與使用者互動的最主要途徑。

### 3.5.1 `<input>` 的多樣類型
| 類型 | 用途 | 範例 |
| :--- | :--- | :--- |
| `text` / `password` | 文字與密碼 | `<input type="password">` |
| `email` / `url` | 格式驗證 | `<input type="email">` |
| `radio` | 單選題 | 需搭配相同 `name` |
| `checkbox` | 多選題 | 可選取多個項 |
| `date` / `time` | 日期與時間 | 顯示內建挑選器 |
| `file` | 檔案上傳 | `accept="image/*"` 限定格式 |

### 3.5.2 下拉選單與多行文字
*   **`<select>`**：建立下拉選單，搭配 `<option>`。
*   **`<textarea>`**：用於輸入長篇訊息，可自訂行數 `rows`。
*   **`<button>`**：比起 `<input type="submit">` 更具自訂彈性，可包含圖示。

### 3.5.3 表單驗證屬性
*   `required`: 必填。
*   `pattern`: 使用正確表達式驗證格式。
*   `min` / `max`: 數值範圍。

---

## 3.6 自我測驗 ✍️

1. **哪一種標籤最適合用來建立網站的主要導覽列？**
   <details>
   <summary>點擊查看答案</summary>
   答案：`<nav>`
   </details>

2. **如果想要讓連結在新視窗開啟，應該加上什麼屬性？**
   <details>
   <summary>點擊查看答案</summary>
   答案：`target="_blank"`
   </details>

3. **如何讓 `<div>` 標籤在不換行的情況下設定寬高？**
   <details>
   <summary>點擊查看答案</summary>
   答案：將其 CSS 設定為 `display: inline-block;`。
   </details>

---

## 3.7 實作演練 🛠️

### 練習一：個人介紹網頁
1. 建立包含大標題、個人照與基本資訊的頁面。
2. 表格要求：三筆求學經歷，需有邊框與 Zebra Stripped 樣式。
3. 採用 `<div>` 規劃區塊並設定唯一 `id`。

### 練習二：註冊表單設計
製作一個虛構的會員註冊頁：
*   包含姓名、密碼（需 8 碼）、生日、慣用瀏覽器 (`datalist`)。
*   設置「同意條款」的核取方塊。

### 練習三：棒球球員報名表
*   包含守備位置 (select)、打擊習慣 (radio)、最快時速 (range)。
*   球員照片上傳功能。

---

> [!NOTE]
> **💡 重點摘要**：HTML 決定了網頁的「結構與內容」，使用語意化標籤與標準屬性，是邁向專業開發者的第一步。