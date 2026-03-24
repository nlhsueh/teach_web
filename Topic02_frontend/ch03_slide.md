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

## 3.1.2 瀏覽器 🌐

- **Evergreen Browsers**：自動更新，對 HTML5 支援度高。
- **渲染引擎 (Rendering Engine)**：
    - **Chromium (Blink)**: Chrome, Edge, Opera, Brave。
    - **WebKit**: Safari (及所有 iOS 瀏覽器)。
    - **Gecko**: Firefox。

> **工具**：[Can I Use](https://caniuse.com/) 查詢功能相容性。

---

## 3.1.3 瀏覽器大戰 ⚔️

1. **Netscape 崛起 (1994)**：早期市場霸主。
2. **微軟反擊 (1995)**：IE 捆綁 Windows 促銷。
3. **標準混亂**：不相容標籤（`<blink>` vs `<marquee>`）。
4. **結局**：微軟勝出，但促使 **Firefox** 誕生與 **W3C** 標準化。

---

## 高效開發：Emmet 語法 ⌨️

- `!` 或 `html:5` → 生成標準 HTML5 骨架。
- `div.container>ul>li*5` → 快速生成階層結構。
- `lorem` → 生成虛擬展示文本。

---

## 3.2 HTML5 標準骨架

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=html/demo-structure.html)

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

## 3.2.2 元素類型

- **非空元素 (Non-empty)**：
    - 有內容，必須有結尾標籤。
    - 例：`<p>...</p>`, `<div>...</div>`
- **空元素 (Empty)**：
    - 無內容，不可有結尾標籤。
    - 例：`<br>`, `<img>`, `<hr>`

---

## 3.2.3 核心文件元素

- **標題 (`<h1>` - `<h6>`)**：權重階層，`<h1>` 為最重要。
- **段落 (`<p>`)**：包裹成段文字。
- **強調**：
    - `<strong>`：加粗 (語意上的強調)。
    - `<em>`：斜體 (語氣上的強調)。

---

## 3.2.4 列表與連結

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=html/demo-list-link.html)

- **無序列表 (`<ul>` + `<li>`)**：點狀條列。
- **有序列表 (`<ol>` + `<li>`)**：數字編號。
- **超連結 (`<a>`)**：
    - `href`：目標位址。
    - `target="_blank"`：在新分頁開啟。

---

## 3.2.5 圖片 🖼️

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=html/demo-image.html)

- **圖片 (`<img>`)**：
    - `src`：來源路徑。
    - `alt`：替代文字 (SEO 關鍵)。
- **空元素**：沒有結尾標籤，`display: inline`。

---

## 3.2.6 標籤、屬性與內容

```html
<h1 style="color: blue;">逢甲共善樓</h1>
```
- **標籤名字**：`h1`
- **屬性 (Attribute)**：`style`
- **值 (Value)**：`"color: blue;"`
- **內容 (Content)**：`逢甲共善樓`

---

## 3.3 Block vs Inline 概念

1. **Block (區塊元素)**：
    - 佔滿整行，自動換行。例：`<div>`, `<p>`, `<h1>`。
2. **Inline (行內元素)**：
    - 只佔內容寬，併排顯示。例：`<span>`, `<a>`。
    - **無法**設定寬高。
3. **Inline-block**：
    - 不換行，但**可以**設定寬高。
    - 例：`<button>`, `<img>`。

---

## 3.3.3 版面置中 (Margin Auto) 🎯

將固定寬度的 **Block 元素** 水平置中：

- `margin-left: auto;` + `margin-right: auto;`
- 或簡寫：`margin: 0 auto;`

> **注意**：文字內容置中使用 `text-align: center;`。

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

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=html/demo-table.html)

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
- `border: 1px solid black;` (Shorthand):
    - width (1px) + style (solid) + color (black)
- `border-spacing`: Cell spacing.
- `padding`: Space between content and border.
- `tr:nth-child(even)`: Zebra striping.

> **Note**: `border-spacing` and `border-collapse` cannot be used together.

---

## 3.4.3 版面置中技巧 🎯

將「固定寬度」的 **Block 元素** 水平置中：

- **方法**：`margin-left: auto;` + `margin-right: auto;`
- **簡寫**：`margin: 0 auto;`

> **注意**：若是內容物（文字/圖片）置中，應在父容器設定 `text-align: center;`。

---

## 3.5 表單 (Form) 📝

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=html/demo-form.html)

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
