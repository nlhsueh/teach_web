---
marp: true
theme: default
paginate: true
header: '第 3 章：HTML 結構與基礎應用'
footer: '逢甲大學資工系 - Web 前端開發'
backgroundColor: #fff
---

# 第 3 章：HTML 結構與基礎應用
## (HTML Foundations)

深入探討 HTML 核心結構、開發工具，以及功能豐富的標記應用。

---

## 3.1 開發工具：VS Code 🛠️

- **智能補全**：代碼提示與自動完成。
- **輕量高效**：開啟速度快，資源占用低。

### 必備外掛 🔌
1. **Auto Close/Rename Tag**：自動閉合與同步更名。
2. **Live Server**：本地伺服器，存檔即預覽。 🚀
3. **Prettier**：自動格式化與美化代碼。

---

## 高效開發：Emmet 語法 ⌨️

- `!` 或 `html:5` → 生成標準 HTML5 骨架。
- `div.container>ul>li*5` → 快速生成階層結構。
- `lorem` → 生成虛擬展示文本。

---

## 3.2 HTML5 標準骨架

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

---

## 3.2.2 核心文本元素

- **標題 (`<h1>` - `<h6>`)**：權重階層，`<h1>` 為最重要。
- **段落 (`<p>`)**：包裹成段文字。
- **強調**：
    - `<strong>`：加粗 (語意上的強調)。
    - `<em>`：斜體 (語氣上的強調)。

---

## 3.2.3 列表與連結

- **無序列表 (`<ul>` + `<li>`)**：點狀條列。
- **有序列表 (`<ol>` + `<li>`)**：數字編號。
- **超連結 (`<a>`)**：
    - `href`：目標位址。
    - `target="_blank"`：在新分頁開啟。

---

## 3.2.4 圖片與樣式 🖼️

- **圖片 (`<img>`)**：
    - `src`：來源路徑。
    - `alt`：替代文字 (SEO 關鍵)。
- **行內樣式 (`style`)**：直接加入 CSS。
    - 範例：`<h1 style="color: blue;">`

---

## 3.3 Block vs Inline 概念

1. **Block (區塊元素)**：
    - 佔滿整行，自動換行。
    - 可設寬高。
    - 例：`<div>`, `<p>`, `<h1>`, `<ul>`。
2. **Inline (行內元素)**：
    - 只佔內容寬，併排顯示。
    - 無法設寬高。
    - 例：`<span>`, `<a>`, `<strong>`。

---

## 3.3.2 語意化標籤 (Semantic)

讓搜尋引擎 (SEO) 與輔助技術更好地理解內容：

- `<header>`：頁頭與導航。
- `<nav>`：導航列。
- `<main>`：主要內容區。
- `<article>` / `<section>`：獨立文章或主題區。
- `<footer>`：頁尾資訊。

---

## 3.4 表格 (Table) 📊

```html
<table>
  <thead>
    <tr> <th>姓名</th> <th>守備位置</th> </tr>
  </thead>
  <tbody>
    <tr> <td>大谷翔平</td> <td>投手</td> </tr>
  </tbody>
</table>
```

- `border-collapse`: 合併邊框。
- `padding`: 內邊距，增加易讀性。
- `nth-child(even)`: 斑馬紋效果。

---

## 3.4.3 版面置中技巧 🎯

將「固定寬度」的 **Block 元素** 水平置中：

- **方法**：`margin-left: auto;` + `margin-right: auto;`
- **簡寫**：`margin: 0 auto;`

> **注意**：若是內容物（文字/圖片）置中，應在父容器設定 `text-align: center;`。

---

## 3.5 表單 (Form) 📝

與使用者互動的最主要途徑。

```html
<form action="/submit" method="POST">
  <label for="name">姓名：</label>
  <input type="text" id="name" name="user_name" required>
  <input type="submit" value="送出">
</form>
```

---

## 3.5.1 `<input>` 的多樣類型

- `text` / `password`：文字與密碼。
- `email` / `url`：格式驗證。
- `radio`：單選題 (相同 `name`)。
- `checkbox`：多選題。
- `date` / `time`：內建挑選器。
- `file`：檔案上傳。

---

## 3.5.2 其他表單元件

- **`<select>`**：下拉選單。
- **`<textarea>`**：多行文字輸入。
- **表單驗證**：
    - `required`: 必填。
    - `pattern`: 正規表達式。
    - `min` / `max`: 數值範圍。

---

# Q & A

下一章：CSS 網頁美化與排版
