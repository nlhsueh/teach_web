###### tags: `Web`

Ch02 HTML
===

## Slide

:point_right: [nlh Slide](https://docs.google.com/presentation/d/1W6qQwzzvZQ0OH97TqwBSL6uNfpBtBWPv7fz05woE3z8/edit?usp=sharing)
* Development Tool
* HTML structure
* Basic HTML Tag
* Table
* FORM


:point_right: [W3School: HTML 教學](https://www.w3schools.com/html/default.asp)

# Appendix

## VS code and HTML

在 **VS Code (Visual Studio Code)** 開發 HTML 項目時，該編輯器提供了強大的功能和多種外掛支持，使開發過程變得更加高效和順暢。以下是一些介紹，包含 VS Code 的常見功能、外掛和技巧，幫助你在開發 HTML 項目時提高工作效率。

---

### 一、為什麼選擇 VS Code 開發 HTML

VS Code 是一款輕量級但功能強大的編輯器，適合用於多種編程語言的開發，特別是 Web 開發。對於 HTML 開發來說，VS Code 提供了以下優勢：
- **智能代碼補全**: 內建的代碼補全功能，能夠根據 HTML 標籤和屬性進行自動補全。
- **即時預覽**: 使用外掛可以即時查看 HTML 頁面的渲染效果。
- **擴展性強**: VS Code 支援各種外掛，這些外掛能顯著提升開發效率，涵蓋語法高亮、代碼格式化、錯誤檢查等功能。
- **輕量級**: 雖然功能強大，但 VS Code 是一個輕量級的編輯器，不會佔用過多的資源。

---

### 二、VS Code 常用外掛介紹

1. **HTML Snippets**:
   - **功能**: 提供常用 HTML 標籤的代碼片段。只需輸入簡短的關鍵字，就能插入完整的 HTML 標籤結構，極大提高開發速度。
   - **常用代碼片段**: 
     - `!` → 生成基本的 HTML 頁面結構。
     - `html:5` → 生成 HTML5 的基本框架。

2. **Auto Close Tag**:
   - **功能**: 自動閉合 HTML 標籤。當你輸入一個開放標籤（如 `<div>`）並按下閉合標籤時，插件會自動插入閉合標籤（`</div>`），避免手動輸入。
   
3. **Auto Rename Tag**:
   - **功能**: 當修改開放標籤或閉合標籤的名稱時，這個外掛會自動同步修改對應的閉合標籤，保持 HTML 結構的一致性。
   
4. **Live Server**:
   - **功能**: 這是一個非常流行的外掛，它能夠在開發過程中自動刷新瀏覽器頁面，讓你能夠即時看到 HTML 文件的更改。只需要右鍵點擊 `index.html` 文件並選擇 "Open with Live Server"，即可啟動本地開發伺服器。
   
5. **Prettier**:
   - **功能**: 用於格式化 HTML 代碼，根據統一的代碼風格自動調整縮排、空格等格式。這不僅有助於代碼的可讀性，也能保持團隊協作中的代碼風格一致。
   
6. **Emmet**:
   - **功能**: Emmet 是一個強大的代碼補全工具，可以極大提高編寫 HTML 的效率。它支持簡寫語法，能夠快速生成複雜的 HTML 結構。例如，輸入 `div.container>ul>li*5` 並按下 `Tab` 鍵，就會生成一個帶有五個 `li` 項目的 `ul`，並且該 `ul` 被包裹在一個 `div` 中。

7. **Bracket Pair Colorizer**:
   - **功能**: 用不同的顏色標示對應的括號和標籤，這對於 HTML 中的嵌套標籤尤為有用，能幫助快速識別匹配的開閉標籤。

---

### 三、常用的 Code Completion 和技巧

1. **使用 Snippets 提高效率**:
   - 在 HTML 文件中，VS Code 提供了代碼片段（Snippets），它能根據你的輸入提供自動補全建議。例如，輸入 `html:5` 或 `!`，會自動生成一個 HTML5 頁面的基本結構。
   - 你還可以自定義自己的代碼片段，將常用的 HTML 模板保存為 Snippets，這樣可以快速重用。

2. **自動補全**:
   - **HTML 標籤補全**: 當你開始輸入 HTML 標籤（如 `<div>` 或 `<h1>`）時，VS Code 會根據你已經輸入的文字提供補全建議。
   - **屬性補全**: 當你輸入標籤（如 `<img`）時，會自動補全這些標籤的常用屬性（如 `src`, `alt` 等）。

3. **快速導航**:
   - 使用 `Ctrl + P`（Windows/Linux）或 `Cmd + P`（Mac）可以快速搜尋並打開任何檔案。
   - 使用 `Ctrl + Shift + O` 可以快速導航到當前文件中的特定符號（如標籤或函數）。

4. **多光標編輯**:
   - 按下 `Alt`（Windows/Linux）或 `Option`（Mac）並點擊不同位置，你可以同時在多個位置編輯，這對於修改多個相似的標籤或屬性非常有用。

5. **即時預覽**:
   - 開啟 Live Server 後，VS Code 會在瀏覽器中即時顯示 HTML 的變更。這讓你無需手動刷新頁面，能夠直接看到改動結果。

6. **語法高亮和錯誤檢查**:
   - VS Code 自帶語法高亮，並且能夠檢查一些常見的錯誤。例如，缺少閉合標籤、未封閉的引號等問題，會在代碼中顯示警告。
   - 使用 **HTMLHint** 或 **HTML Lint** 外掛可以進行更嚴格的語法檢查，幫助發現潛在的問題。

7. **分屏模式**:
   - 使用 `Ctrl + \` 可以將編輯器分成多個窗格，方便同時查看多個文件，這對於同時編輯 HTML 文件和查看 CSS 或 JavaScript 非常有用。

---

### 四、總結

VS Code 是一個極為強大且靈活的工具，特別適合用來開發 HTML 項目。透過適當的外掛、代碼補全技巧和即時預覽功能，可以顯著提高開發效率並減少錯誤的產生。學會使用這些功能後，你會發現開發過程變得更加高效、簡單，也能更專注於創建出色的網站和應用程式。

## 初階 HTML 

以下是初階 HTML 標記的介紹，這些標記是構建網頁結構的基礎。了解這些標記將幫助你建立簡單的 HTML 頁面。

---

### 一、HTML 基本結構

每個 HTML 文件都必須有一個基本結構，通常如下所示：

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>頁面標題</title>
</head>
<body>
    <!-- 頁面內容在這裡 -->
</body>
</html>
```

- `<!DOCTYPE html>`：指定文件類型，告訴瀏覽器該文件是 HTML5 文檔。
- `<html>`：根元素，所有其他 HTML 元素都包含在此元素內。
- `<head>`：包含頁面的元數據（如標題、字符集、樣式等），不會顯示在頁面內容中。
- `<body>`：包含頁面的內容，顯示在瀏覽器中。

---

### 二、常見 HTML 標記介紹

#### 文本元素
- `<h1> 到 <h6>`：標題標籤，用來表示不同層級的標題（`<h1>` 是最高層級）。
    ```html
    <h1>這是主標題</h1>
    <h2>這是副標題</h2>
    ```

- `<p>`：段落標籤，包裹段落文本。
    ```html
    <p>這是一段文字。</p>
    ```

- `<strong>`：加粗文字，通常用來表示強調。
    ```html
    <strong>這是加粗文字</strong>
    ```

- `<em>`：斜體文字，通常用來表示強調語氣。
    ```html
    <em>這是斜體文字</em>
    ```

#### 列表元素
- `<ul>`：無序列表，通常配合 `<li>` 標籤使用，表示一組項目。
    ```html
    <ul>
        <li>項目一</li>
        <li>項目二</li>
        <li>項目三</li>
    </ul>
    ```

- `<ol>`：有序列表，與 `<ul>` 類似，但項目會按順序排列。
    ```html
    <ol>
        <li>第一項</li>
        <li>第二項</li>
        <li>第三項</li>
    </ol>
    ```

- `<li>`：列表項，無論是有序列表還是無序列表，都會使用 `<li>` 來定義每個項目。

#### 連結與媒體元素
- `<a>`：超連結標籤，通常用來創建頁面間的鏈接。
    ```html
    <a href="https://www.example.com">點擊這裡</a>
    ```

- `<img>`：圖片標籤，顯示圖片。使用 `src` 屬性指定圖片來源，並使用 `alt` 屬性提供替代文字。
    ```html
    <img src="image.jpg" alt="示範圖片">
    ```

#### 表單元素
- `<form>`：表單標籤，包含用戶輸入的所有元素。
    ```html
    <form action="/submit">
        <!-- 表單內容 -->
    </form>
    ```

- `<input>`：用來接受用戶輸入。可以設置不同的類型（如文本框、密碼框等）。
    ```html
    <input type="text" name="username" placeholder="輸入用戶名">
    ```

- `<textarea>`：多行文本框，讓用戶輸入長篇文字。
    ```html
    <textarea name="message" rows="4" cols="50"></textarea>
    ```

- `<button>`：按鈕，用來觸發表單提交或其他操作。
    ```html
    <button type="submit">提交</button>
    ```

#### 結構性元素
- `<div>`：區塊級元素，用來將頁面分為不同的區塊或區域。常用於佈局。
    ```html
    <div>
        <p>這是一個區塊級元素</p>
    </div>
    ```

- `<span>`：行內元素，用來包裹文本，通常用於樣式調整。
    ```html
    <span>這是行內元素</span>
    ```

#### 表格元素
- `<table>`：表格元素，用來創建表格。
    ```html
    <table>
        <tr>
            <th>標題1</th>
            <th>標題2</th>
        </tr>
        <tr>
            <td>資料1</td>
            <td>資料2</td>
        </tr>
    </table>
    ```

- `<tr>`：表格行，包含一組 `<td>` 或 `<th>` 標籤。
- `<th>`：表格標題單元格，通常用來表示表格的列標題。
- `<td>`：表格數據單元格，包含表格的內容。


### 三、元素的呈現

在 HTML 和 CSS 中，元素的顯示行為是由 **顯示屬性**（`display`）控制的。最常見的顯示行為類型包括 **block**、**inline**、**inline-block** 和 **none**。了解這些顯示屬性的差異是前端開發中非常重要的一部分，因為它們會直接影響元素的排列方式、佈局行為和相互關係。

#### 1. Block 元素

**Block 元素**（區塊級元素）是指佔據整個可用行的元素，並且會在其前後自動產生換行，將下一個元素推到下一行。這些元素通常會以全寬顯示，並且可以設置寬度和高度。

**常見的 Block 元素**
- `<div>`：常用的區塊容器元素。
- `<p>`：段落元素。
- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`：標題元素。
- `<ul>`, `<ol>`, `<li>`：列表元素。
- `<form>`：表單元素。

**特點**
- **佔滿整行**：Block 元素會自動佔據父容器的整個寬度。
- **會換行**：前後元素會自動換行，這意味著在 Block 元素前後會有換行。
- **可以設置寬高**：Block 元素可以明確設置寬度 (`width`) 和高度 (`height`)。

**範例**
```html
<div style="background-color: lightblue; width: 100%; height: 100px;">這是一個區塊元素</div>
```
在這個例子中，`<div>` 是一個區塊元素，它會佔據整個行的寬度，並且可以設定寬度和高度。

---

#### 2. Inline 元素

**Inline 元素**（行內元素）與 Block 元素不同，它們只佔據其內容的空間，不會自動換行，並且不能設定寬度和高度。這些元素通常是用來處理文字或小範圍的內容。

**常見的 Inline 元素**
- `<span>`：行內元素，通常用來包裹某些文本或其他內聯元素以便設置樣式。
- `<a>`：超鏈接元素。
- `<strong>`, `<em>`：強調文本，通常顯示為加粗或斜體。

**特點**
- **不佔滿整行**：Inline 元素只佔據其內容的空間，不會佔據整個行的寬度。
- **不會換行**：Inline 元素不會在前後換行，它們會與相鄰的 Inline 元素在同一行內顯示。
- **不能設置寬高**：Inline 元素無法設置寬度 (`width`) 或高度 (`height`)，它們的大小由其內容決定。

**範例**
```html
<p>這是段落中的一個 <span style="color: red;">紅色文字</span> 例子。</p>
```
在這個例子中，`<span>` 是一個行內元素，它不會導致文本換行，而是與其他文本同在一行。

---

#### 3. Inline-block 元素

**Inline-block 元素** 結合了 Block 和 Inline 元素的特點。它像 Inline 元素一樣不會換行，但像 Block 元素一樣可以設置寬度和高度。

**特點**
- **不會換行**：和 Inline 元素一樣，Inline-block 元素不會換行，它會在同一行內顯示。
- **可以設置寬高**：和 Block 元素一樣，Inline-block 元素可以設置寬度 (`width`) 和高度 (`height`)。
- **能夠與其他 Inline 元素一起排布**：可以在同一行顯示，並且設置不同的寬度和高度。

**範例**
```html
<div style="display: inline-block; width: 100px; height: 100px; background-color: blue;">區塊 1</div>
<div style="display: inline-block; width: 100px; height: 100px; background-color: red;">區塊 2</div>
```
在這個例子中，兩個 `<div>` 都是 Inline-block 元素，它們會排成一行並且可以設置寬度和高度。

---

#### 4. None 元素

**None 元素** 是一種特殊的顯示屬性，它會將元素從頁面中完全移除，並且不再佔用任何空間。當某個元素的顯示屬性被設置為 `display: none` 時，該元素會被隱藏。

**特點**
- **元素消失**：當設置為 `display: none` 時，該元素將不會顯示，並且不佔用頁面空間。
- **不同於 `visibility: hidden`**：`visibility: hidden` 會隱藏元素，但該元素仍然佔據頁面空間。而 `display: none` 則完全將元素從頁面佈局中移除。

**範例**
```html
<div style="display: none;">這個區塊不會顯示在頁面上。</div>
```
這段代碼中的 `<div>` 元素設置了 `display: none`，因此它不會顯示在頁面上，並且也不會佔據空間。

---

#### 5. 顯示屬性與 CSS 的應用

通過設置不同的顯示屬性，開發者可以靈活地控制網頁元素的排列方式。這些屬性不僅能影響佈局，還能用來創建複雜的網頁設計效果。常見的應用場景包括：

1. **製作響應式佈局**：通過設置元素為 `inline-block` 或 `block`，可以創建響應式網頁，根據屏幕大小調整顯示行為。
2. **製作導航條**：`inline` 和 `inline-block` 可以用來排列導航項目，使它們呈現為水平方向的鏈接。
3. **隱藏元素**：通過 `display: none` 可以動態顯示或隱藏頁面元素，這對於實現交互式頁面（如菜單的顯示與隱藏）非常有用。

---

#### 結語

`block`、`inline` 和 `inline-block` 是控制元素顯示行為的重要屬性，理解它們之間的區別能幫助開發者靈活地設計頁面的佈局。選擇合適的顯示屬性可以使頁面更加結構清晰並提升用戶體驗。

---

### 四、HTML 屬性
HTML 標籤可以包含屬性，用來控制元素的行為或顯示樣式。常見的屬性有：

- `id`：為元素指定唯一標識符。
    ```html
    <div id="container">內容</div>
    ```

- `class`：為元素指定一個或多個類別名，用於 CSS 樣式或 JavaScript 操作。
    ```html
    <div class="box">內容</div>
    ```

- `href`：用於超連結元素 `<a>`，指定目標 URL。
    ```html
    <a href="https://www.example.com">網站連結</a>
    ```

- `src`：用於圖片元素 `<img>`，指定圖片來源。
    ```html
    <img src="image.jpg" alt="描述">
    ```

- `alt`：用於圖片元素 `<img>`，提供圖片的替代文本。
    ```html
    <img src="image.jpg" alt="這是圖片的描述">
    ```

- `type`：用於表單元素 `<input>`，指定輸入類型，如文本框、密碼框等。
    ```html
    <input type="text">
    <input type="password">
    ```

### 練習一：自我介紹

做一個各人（或他人/動物/明星）的介紹網頁，包含
* 姓名等基本資訊的描述，用沒有排序的列表
* 照片至少兩張
* 連接，可以連接到個人有興趣的網頁，或是介紹明星的網頁
* 表格，至少包含三筆資料例如求學歷程或經歷。每筆資料至少有三個欄位，例如名稱、年份與敘述
* 使用大小標題來標示每一個區塊的名稱。（h1, h2, ...）; 每一個區塊採用 div 來設定，並且給予 id
* 使用 internal CSS 來設定
  * 段落文字，改為藍色; 
  * 表格的 padding, border space; 表格的表頭文字大小大一點; 
  * 照片的的寬度設為 400px; 照片的顯示設定為自動會換行

---

## 進階表格

### 一、進階 HTML 表格（`<table>`）介紹

HTML 中的表格 (`<table>`) 用於展示結構化數據。進階使用表格的時候，我們會利用 CSS 來控制其外觀，進行樣式的美化、調整表格的間距、邊框等。這些設置有助於提高表格的可讀性與可視化效果。以下是一些常見的進階技巧和樣式：

#### 1. **表格的基本結構**
HTML 表格的基本結構包括：
- `<table>`：表格元素，包裹整個表格。
- `<tr>`：表格行，用來定義表格中的一行數據。
- `<th>`：表格標題單元格，通常用於表格的表頭。
- `<td>`：表格數據單元格，用來展示表格中的數據。

一個簡單的表格範例如下：

```html
<table>
    <tr>
        <th>姓名</th>
        <th>年齡</th>
        <th>城市</th>
    </tr>
    <tr>
        <td>張三</td>
        <td>25</td>
        <td>台北</td>
    </tr>
    <tr>
        <td>李四</td>
        <td>30</td>
        <td>高雄</td>
    </tr>
</table>
```

### 二、表格的進階樣式

#### 1. **表格邊框（`border`）**
表格的邊框可以通過 CSS 的 `border` 屬性來設置，使表格顯得更加清晰。

- **CSS 樣式**：
    ```css
    table {
        border-collapse: collapse; /* 使邊框合併為單一邊框 */
        width: 100%; /* 設置表格寬度 */
    }

    th, td {
        border: 1px solid #ddd; /* 邊框樣式 */
        padding: 8px; /* 單元格內邊距 */
        text-align: left; /* 文字左對齊 */
    }
    ```

- **HTML 表格**：
    ```html
    <table>
        <tr>
            <th>姓名</th>
            <th>年齡</th>
            <th>城市</th>
        </tr>
        <tr>
            <td>張三</td>
            <td>25</td>
            <td>台北</td>
        </tr>
        <tr>
            <td>李四</td>
            <td>30</td>
            <td>高雄</td>
        </tr>
    </table>
    ```

在這個例子中，我們使用了 `border-collapse: collapse;` 來合併相鄰的邊框，這樣表格看起來會有單一邊框，並且設置了 `border: 1px solid #ddd;` 為表格的邊框顏色和樣式。

#### 2. **表格內邊距（`padding`）**
使用 CSS 的 `padding` 屬性可以控制表格單元格內部的空間，使表格內容不至於緊貼邊緣，讓視覺效果更佳。

- **CSS 樣式**：
    ```css
    th, td {
        padding: 12px; /* 增加內邊距 */
    }
    ```

`padding` 屬性可以控制單元格內部的空間，讓表格看起來更加寬敞。你可以根據需要設置不同的值來調整表格的顯示效果。

#### 3. **Zebra Striped Table（斑馬表格）**
斑馬表格是一種常見的樣式，能夠通過交替的背景顏色來提高表格的可讀性。這樣的表格在每一行之間交替使用不同的背景色，讓讀者更容易區分每行的數據。

- **CSS 樣式**：
    ```css
    table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        padding: 12px;
        text-align: left;
        border: 1px solid #ddd;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2; /* 偶數行的背景色 */
    }
    ```

- **HTML 表格**：
    ```html
    <table>
        <tr>
            <th>姓名</th>
            <th>年齡</th>
            <th>城市</th>
        </tr>
        <tr>
            <td>張三</td>
            <td>25</td>
            <td>台北</td>
        </tr>
        <tr>
            <td>李四</td>
            <td>30</td>
            <td>高雄</td>
        </tr>
        <tr>
            <td>王五</td>
            <td>22</td>
            <td>台中</td>
        </tr>
    </table>
    ```

在這個例子中，使用了 `tr:nth-child(even)` 選擇器來選擇偶數行並將其背景顏色設置為 `#f2f2f2`，這樣就實現了斑馬表格效果。這樣的樣式有助於使表格更具可讀性，尤其是在顯示大量數據時。

#### 4. **表格邊框圓角（`border-radius`）**
可以使用 CSS 的 `border-radius` 屬性來為表格或單元格添加圓角，這樣表格的邊框就會變得更加圓滑。

- **CSS 樣式**：
    ```css
    table {
        border-collapse: separate; /* 允許單元格有間隙 */
        border-spacing: 0; /* 設置間隙 */
        border-radius: 10px; /* 為整個表格添加圓角 */
        overflow: hidden; /* 隱藏圓角外的部分 */
    }
    ```

- **HTML 表格**：
    ```html
    <table>
        <tr>
            <th>姓名</th>
            <th>年齡</th>
            <th>城市</th>
        </tr>
        <tr>
            <td>張三</td>
            <td>25</td>
            <td>台北</td>
        </tr>
        <tr>
            <td>李四</td>
            <td>30</td>
            <td>高雄</td>
        </tr>
    </table>
    ```

這樣的效果使得表格看起來更加現代，並且能夠增加頁面的視覺吸引力。

#### 5. **表格對齊與自適應**
有時候你需要調整表格的對齊方式或讓表格根據瀏覽器大小自動調整大小，這可以通過 CSS 的 `text-align`、`width`、`max-width` 等屬性來實現。

- **CSS 樣式**：
    ```css
    table {
        width: 100%; /* 使表格寬度自適應 */
        max-width: 800px; /* 限制表格最大寬度 */
        margin: auto; /* 使表格水平居中 */
    }

    th, td {
        text-align: center; /* 使表格內容居中 */
    }
    ```

- **HTML 表格**：
    ```html
    <table>
        <tr>
            <th>姓名</th>
            <th>年齡</th>
            <th>城市</th>
        </tr>
        <tr>
            <td>張三</td>
            <td>25</td>
            <td>台北</td>
        </tr>
        <tr>
            <td>李四</td>
            <td>30</td>
            <td>高雄</td>
        </tr>
    </table>
    ```

這樣的設置可以讓表格在不同大小的屏幕上保持良好的顯示效果，並且將其居中顯示。

---

### 三、結語

進階的表格設計不僅能提升頁面美觀，還能增強用戶體驗，尤其是在顯示大量資料時。利用 CSS，我們可以進行以下調整：
- **邊框設置**：為表格和單元格設置邊框，提升視覺效果。
- **內邊距調整**：讓表格中的數據不會擠在邊緣。
- **斑馬表格**：交替顯示不同的背景色來提高可讀性。
- **圓角設置**：使表格邊緣更加柔和，增強現代感。

通過這些 CSS 設置，我們能夠創建出既美觀又易於操作的表格，並在各種設備上保持良好的顯示效果。

---

這是一份完整的 HTML `<form>` 介紹，包括各種輸入元件及其屬性，適合作為教材內容。

---

## 進階表單

HTML `<form>`（表單）用於收集使用者輸入的資料，並可透過 `GET` 或 `POST` 方法提交到伺服器。表單內的主要元素是 `<input>`、`<select>`、`<textarea>`、`<button>` 及其他表單相關標籤。

### `<form>` 標籤
表單的基本語法如下：
```html
<form action="submit.php" method="post">
    <!-- 表單內容 -->
</form>
```
**屬性：**
- `action`：指定資料提交的目標 URL。
- `method`：
  - `GET`：將資料附加在 URL 末端（適合搜尋）。
  - `POST`：將資料作為請求主體（適合敏感資料）。
- `autocomplete`：`on` / `off`（是否啟用自動填寫）。
- `novalidate`：取消瀏覽器的表單驗證。

---

### `<input>` 標籤
`<input>` 是最常用的表單元素，有多種類型。

#### 常見的 `type` 屬性
| 類型             | 說明                          | 範例                                                    |
| ---------------- | ----------------------------- | ------------------------------------------------------- |
| `text`           | 單行文字輸入                  | `<input type="text" name="username">`                   |
| `password`       | 密碼輸入                      | `<input type="password" name="password">`               |
| `email`          | 電子郵件輸入                  | `<input type="email" name="email">`                     |
| `url`            | 網址輸入                      | `<input type="url" name="website">`                     |
| `tel`            | 電話號碼輸入                  | `<input type="tel" name="phone">`                       |
| `number`         | 數字輸入                      | `<input type="number" name="age" min="1" max="100">`    |
| `search`         | 搜尋框                        | `<input type="search" name="query">`                    |
| `date`           | 日期選擇                      | `<input type="date" name="birthdate">`                  |
| `time`           | 時間選擇                      | `<input type="time" name="appointment">`                |
| `datetime-local` | 日期+時間                     | `<input type="datetime-local" name="meeting">`          |
| `month`          | 選擇月份                      | `<input type="month" name="exp_month">`                 |
| `week`           | 選擇週數                      | `<input type="week" name="exp_week">`                   |
| `checkbox`       | 核取方塊（可多選）            | `<input type="checkbox" name="hobby" value="reading">`  |
| `radio`          | 單選按鈕（需搭配相同 `name`） | `<input type="radio" name="gender" value="male">`       |
| `file`           | 檔案上傳                      | `<input type="file" name="resume">`                     |
| `hidden`         | 隱藏輸入欄位                  | `<input type="hidden" name="session_id" value="12345">` |
| `color`          | 顏色選擇                      | `<input type="color" name="favcolor">`                  |
| `range`          | 範圍滑桿                      | `<input type="range" name="volume" min="0" max="100">`  |
| `submit`         | 送出按鈕                      | `<input type="submit" value="提交">`                    |
| `reset`          | 重設按鈕                      | `<input type="reset" value="重設">`                     |
| `button`         | 一般按鈕                      | `<input type="button" value="點擊我">`                  |

---

### 其他表單元素

#### `<textarea>`
用於輸入多行文字：
```html
<textarea name="message" rows="4" cols="50"></textarea>
```
**屬性：**
- `rows`：設定顯示的行數。
- `cols`：設定寬度（通常不建議使用，改用 CSS）。
- `maxlength`：最大字數。

---

#### `<select>`（下拉選單）
提供多個選項，允許使用者選擇：
```html
<select name="country">
    <option value="tw">台灣</option>
    <option value="us">美國</option>
    <option value="jp">日本</option>
</select>
```
**屬性：**
- `multiple`：允許多選。
- `size`：顯示多少個選項（適用於 `multiple`）。

多選範例：
```html
<select name="fruits" multiple size="3">
    <option value="apple">蘋果</option>
    <option value="banana">香蕉</option>
    <option value="cherry">櫻桃</option>
</select>
```

---

#### `<button>`
比起 `<input type="submit">`，`<button>` 提供更靈活的內容：
```html
<button type="submit">送出表單</button>
<button type="reset">重設</button>
<button type="button" onclick="alert('Hello!')">點我</button>
```

---

### 表單驗證屬性
HTML 提供多種內建驗證屬性：
| 屬性          | 說明           | 範例                                      |
| ------------- | -------------- | ----------------------------------------- |
| `required`    | 必填           | `<input type="text" required>`            |
| `maxlength`   | 最大字數       | `<input type="text" maxlength="10">`      |
| `min` / `max` | 數字範圍       | `<input type="number" min="1" max="100">` |
| `pattern`     | 自訂正規表達式 | `<input type="tel" pattern="[0-9]{10}">`  |
| `step`        | 數值間距       | `<input type="number" step="5">`          |

---

### 使用 `fieldset` & `legend` 組織表單
```html
<fieldset>
    <legend>個人資料</legend>
    <label>姓名: <input type="text" name="name"></label><br>
    <label>Email: <input type="email" name="email"></label>
</fieldset>
```
- `fieldset`：用於分組表單內容。
- `legend`：設定標題。

---

### `datalist`（自動完成選項）
提供輸入建議：
```html
<input list="browsers" name="browser">
<datalist id="browsers">
    <option value="Chrome">
    <option value="Firefox">
    <option value="Edge">
    <option value="Safari">
</datalist>
```

---

### 表單的 JavaScript 處理
```html
<form onsubmit="return validateForm()">
    <input type="text" id="username" required>
    <input type="submit" value="提交">
</form>

<script>
function validateForm() {
    let name = document.getElementById("username").value;
    if (name == "") {
        alert("姓名不能為空！");
        return false;
    }
}
</script>
```

### 練習二：線上註冊表單

**目標：**  
練習各種 `<form>` 元件，包括 `<input>`（不同 `type`）、`<select>`、`<textarea>`、`<datalist>`，並應用表單驗證屬性。

---

#### **題目：設計一個線上註冊表單**
請根據以下要求，設計一個完整的線上註冊表單，並確保所有欄位都有適當的驗證規則。

**表單欄位要求：**
1. **姓名 (`text`)**  
   - 必填，最大長度 50。
2. **電子郵件 (`email`)**  
   - 必填，格式須符合 Email 規範。
3. **密碼 (`password`)**  
   - 必填，至少 8 碼，且需包含大小寫字母和數字。
4. **性別 (`radio`)**  
   - 男 / 女 / 其他（三選一）。
5. **生日 (`date`)**  
   - 必填，須選擇過去的日期。
6. **電話號碼 (`tel`)**  
   - 必填，格式應為 10 碼數字（可用 `pattern`）。
7. **國家 (`select`)**  
   - 必填，提供「台灣、美國、日本、其他」選項。
8. **興趣 (`checkbox`，可多選)**  
   - 閱讀 / 運動 / 旅行 / 音樂 / 電影。
9. **個人網站 (`url`)**  
   - 選填，須符合網址格式。
10. **喜愛的瀏覽器 (`datalist`)**  
    - 讓使用者從「Chrome、Firefox、Safari、Edge、其他」中選擇。
11. **個人簡介 (`textarea`)**  
    - 選填，最多 200 字。
12. **設定通知 (`range`)**  
    - 設定接收通知頻率（0-100%）。
13. **上傳個人大頭照 (`file`)**  
    - 限定上傳圖片 (`accept="image/*"`)。
14. **同意條款 (`checkbox`)**  
    - 必須勾選才能提交表單。

---

#### 範例解答
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>註冊表單練習</title>
    <style>
        label {
            display: block;
            margin: 5px 0;
        }
    </style>
</head>
<body>

    <h2>線上註冊表單</h2>

    <form action="submit.php" method="post">
        <label>姓名：
            <input type="text" name="fullname" required maxlength="50">
        </label>

        <label>電子郵件：
            <input type="email" name="email" required>
        </label>

        <label>密碼：
            <input type="password" name="password" required minlength="8" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}">
        </label>

        <label>性別：
            <input type="radio" name="gender" value="male" required> 男
            <input type="radio" name="gender" value="female"> 女
            <input type="radio" name="gender" value="other"> 其他
        </label>

        <label>生日：
            <input type="date" name="birthdate" required max="2023-12-31">
        </label>

        <label>電話號碼：
            <input type="tel" name="phone" required pattern="[0-9]{10}">
        </label>

        <label>國家：
            <select name="country" required>
                <option value="">請選擇</option>
                <option value="tw">台灣</option>
                <option value="us">美國</option>
                <option value="jp">日本</option>
                <option value="other">其他</option>
            </select>
        </label>

        <label>興趣：
            <input type="checkbox" name="hobby" value="reading"> 閱讀
            <input type="checkbox" name="hobby" value="sports"> 運動
            <input type="checkbox" name="hobby" value="travel"> 旅行
            <input type="checkbox" name="hobby" value="music"> 音樂
            <input type="checkbox" name="hobby" value="movies"> 電影
        </label>

        <label>個人網站：
            <input type="url" name="website">
        </label>

        <label>喜愛的瀏覽器：
            <input list="browsers" name="browser">
            <datalist id="browsers">
                <option value="Chrome">
                <option value="Firefox">
                <option value="Safari">
                <option value="Edge">
                <option value="其他">
            </datalist>
        </label>

        <label>個人簡介：
            <textarea name="bio" rows="4" cols="40" maxlength="200"></textarea>
        </label>

        <label>通知頻率：
            <input type="range" name="notification" min="0" max="100">
        </label>

        <label>上傳個人大頭照：
            <input type="file" name="profile_pic" accept="image/*">
        </label>

        <label>
            <input type="checkbox" name="terms" required> 我同意條款與細則
        </label>

        <input type="submit" value="提交">
        <input type="reset" value="重設">
    </form>

</body>
</html>
```

---

#### **進階挑戰**
1. **前端驗證**：  
   - 使用 `pattern` 和 `required` 屬性驗證輸入內容格式。
   - 密碼至少 8 碼，且包含大小寫字母與數字。
   - 生日不得選擇未來日期。

2. **JavaScript 驗證**（可選）：  
   - 若 `電話號碼` 欄位不是 10 碼，則阻止提交並顯示錯誤訊息。
   - 當 `密碼` 不符合要求時，提供即時錯誤提示。

3. **CSS 美化**：  
   - 使用 CSS 讓表單更易讀。
   - 加入 `:focus` 效果來提升輸入框的可視性。
   - 使用 `flexbox` 或 `grid` 讓佈局更整齊。

---
### **HTML Form 練習題：棒球球員報名表單**  

**目標：**  
讓學生練習 `<form>` 的各種輸入元件，包括 `<input>`（不同 `type`）、`<select>`、`<textarea>`、`<datalist>`，並應用表單驗證屬性。

---

### 練習三：棒球比賽球員報名表單
請根據以下要求，設計一個完整的 **棒球球員報名表單**，並確保所有欄位都有適當的驗證規則。

**表單欄位要求**
1. **球員姓名 (`text`)**  
   - 必填，最大長度 50。
2. **電子郵件 (`email`)**  
   - 必填，格式須符合 Email 規範。
3. **年齡 (`number`)**  
   - 必填，範圍需介於 10-50 歲之間。
4. **守備位置 (`select`)**  
   - 必填，提供「投手、捕手、一壘手、二壘手、三壘手、游擊手、外野手」選項。
5. **打擊習慣 (`radio`)**  
   - 右打 / 左打 / 兩側都能打（三選一）。
6. **慣用手 (`radio`)**  
   - 右手 / 左手。
7. **球衣號碼 (`number`)**  
   - 必填，範圍 1-99，不能重複（假設後端驗證）。
8. **個人球技 (`textarea`)**  
   - 選填，最多 300 字。
9. **球隊經驗 (`checkbox`，可多選)**  
   - 國小球隊 / 國中球隊 / 高中球隊 / 大學球隊 / 職業隊。
10. **最快投球時速 (`range`)**  
    - 0-180 km/h，顯示投球速度。
11. **球棒品牌 (`datalist`)**  
    - 讓使用者從「Mizuno、Wilson、Easton、Louisville Slugger、Rawlings」中選擇或自行輸入其他品牌。
12. **球員照片 (`file`)**  
    - 限定上傳圖片 (`accept="image/*"`)。
13. **報名條款 (`checkbox`)**  
    - 必須勾選「我同意比賽規則與條款」才能提交表單。

---

## 其他進階

進階的 HTML 標記介紹將涵蓋更複雜的標籤、屬性和用法，這些對於構建現代網頁應用程序和網站至關重要。進一步的學習將幫助你在開發過程中更靈活地處理多樣化的需求，並能與 CSS 和 JavaScript 更好地協作。

---

### 一、HTML5 新標籤

HTML5 引入了多種新的元素，使得網頁結構更加語義化，便於搜尋引擎優化（SEO）及可訪問性設計。

#### 1. **語義元素 (Semantic Elements)**
語義元素指的是那些明確表達其內容意圖的標籤，使得 HTML 文檔更加易讀，對 SEO 和無障礙設計更友好。

- `<header>`：定義頁面的頭部區域，通常包含導航鏈接、網站標誌等。
    ```html
    <header>
        <h1>網站標題</h1>
        <nav>...</nav>
    </header>
    ```

- `<footer>`：定義頁面的底部區域，通常包含版權信息、聯繫方式等。
    ```html
    <footer>
        <p>版權所有 &copy; 2025</p>
    </footer>
    ```

- `<article>`：表示一個獨立的內容區塊，通常是可以單獨重用的部分，如博客文章、新聞報導等。
    ```html
    <article>
        <h2>文章標題</h2>
        <p>文章內容</p>
    </article>
    ```

- `<section>`：定義文檔中的區域或段落，通常用來劃分不同的主題部分。
    ```html
    <section>
        <h2>區塊標題</h2>
        <p>這是區塊的內容。</p>
    </section>
    ```

- `<nav>`：表示網頁中的導航部分，通常包含頁面導航的鏈接。
    ```html
    <nav>
        <ul>
            <li><a href="#home">首頁</a></li>
            <li><a href="#about">關於我們</a></li>
        </ul>
    </nav>
    ```

- `<aside>`：用於表示與主內容相關的附加內容，如側邊欄、廣告等。
    ```html
    <aside>
        <h3>相關文章</h3>
        <ul>
            <li><a href="#">文章一</a></li>
            <li><a href="#">文章二</a></li>
        </ul>
    </aside>
    ```

#### 2. **表單元素進階**
HTML5 引入了多種新的表單元素，增強了表單的可用性和交互性。

- `<input type="email">`：用於輸入電子郵件地址，並會進行基本的格式驗證。
    ```html
    <input type="email" placeholder="請輸入電子郵件">
    ```

- `<input type="url">`：用於輸入網址，並進行格式驗證。
    ```html
    <input type="url" placeholder="請輸入網址">
    ```

- `<input type="date">`：用於選擇日期，瀏覽器會顯示日期選擇器。
    ```html
    <input type="date">
    ```

- `<input type="range">`：用於創建滑動條，讓用戶選擇範圍中的數值。
    ```html
    <input type="range" min="1" max="100" value="50">
    ```

- `<input type="tel">`：用於輸入電話號碼，適用於移動端設備。
    ```html
    <input type="tel" placeholder="輸入電話號碼">
    ```

- `<textarea>`：多行文本框，支持用戶輸入長篇文本。
    ```html
    <textarea placeholder="輸入長篇文本"></textarea>
    ```

#### 3. **多媒體元素**
HTML5 增加了對音頻和視頻的支持，方便開發者直接在頁面中嵌入媒體內容。

- `<audio>`：用於嵌入音頻文件，支持多種格式（如 MP3、OGG、WAV）。
    ```html
    <audio controls>
        <source src="audio.mp3" type="audio/mp3">
        您的瀏覽器不支持音頻元素。
    </audio>
    ```

- `<video>`：用於嵌入視頻文件，支持多種格式（如 MP4、WebM、OGG）。
    ```html
    <video width="320" height="240" controls>
        <source src="video.mp4" type="video/mp4">
        您的瀏覽器不支持視頻元素。
    </video>
    ```

- `<picture>`：用於根據不同的設備和條件（如屏幕大小、網絡狀況等）提供不同版本的圖像。
    ```html
    <picture>
        <source srcset="image-large.jpg" media="(min-width: 800px)">
        <source srcset="image-small.jpg" media="(max-width: 799px)">
        <img src="image-default.jpg" alt="圖片">
    </picture>
    ```

#### 4. **進階表格標籤**
- `<thead>`、`<tbody>`、`<tfoot>`：這些標籤用來區分表格的不同部分，讓表格結構更加語義化，有助於表格的可讀性和維護性。
    ```html
    <table>
        <thead>
            <tr>
                <th>姓名</th>
                <th>年齡</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>張三</td>
                <td>25</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td>總計</td>
                <td>25</td>
            </tr>
        </tfoot>
    </table>
    ```

---

### 二、進階 HTML 屬性

#### 1. **自定義數據屬性 (Data Attributes)**
HTML5 引入了 `data-*` 屬性，允許開發者在元素上儲存自定義數據。這些屬性不會影響頁面的外觀，但可以用來在 JavaScript 中進行交互。

```html
<div data-user-id="12345" data-role="admin">
    這是用戶資訊區塊
</div>
```

在 JavaScript 中可以使用 `dataset` 來訪問這些數據：
```javascript
const element = document.querySelector('div');
console.log(element.dataset.userId);  // 12345
console.log(element.dataset.role);    // admin
```

#### 2. **ARIA 屬性 (Accessible Rich Internet Applications)**
ARIA 屬性用來提升網頁的無障礙性，特別是對於使用輔助技術（如屏幕閱讀器）的用戶。

- `aria-label`：為元素提供可讀的描述。
    ```html
    <button aria-label="關閉" onclick="closeWindow()">X</button>
    ```

- `aria-hidden`：指定元素是否對輔助技術可見。
    ```html
    <div aria-hidden="true">這是隱藏的內容</div>
    ```

#### 3. **進階超鏈接屬性**
- `target="_blank"`：使得鏈接在新窗口或新標籤頁中打開。
    ```html
    <a href="https://www.example.com" target="_blank">訪問外部網站</a>
    ```

- `rel="noopener noreferrer"`：當使用 `target="_blank"` 時，這個屬性能提高安全性，防止新的頁面可以訪問原頁面的 `window` 對象。
    ```html
    <a href="https://www.example.com" target="_blank" rel="noopener noreferrer">安全的外部鏈接</a>
    ```

---

### 三、結語

進階的 HTML 標籤和屬性能夠讓你在開發更複雜的網頁時提供更多的控制和靈活性。HTML5 的引入改變了網頁結構的設計，讓開發者能夠創建更語義化、響應式、且對用戶友好的網站。隨著對這些標籤和屬性的理解加深，你將能夠編寫出更高效、結構清晰且具備良好可訪問性的 HTML 代碼。

## CSS

### 一、CSS (Cascading Style Sheets) 的用途

**CSS (層疊樣式表)** 是用來描述 HTML 或 XML（包括 SVG 和 XML 文檔）中的內容如何呈現和格式化的語言。它決定了網頁元素的佈局、顏色、字體、邊框、間距、對齊等樣式。換句話說，CSS 是設計網頁外觀的工具。

#### 1. **CSS 的主要用途**
- **控制佈局**：CSS 使得開發者能夠控制網頁元素的位置，實現不同設備上的響應式設計。
- **設置樣式**：包括顏色、字體、背景、邊框等，可以根據需要調整不同元素的樣式，使頁面更加美觀和一致。
- **排版設計**：CSS 能夠精確控制文字的顯示，包括字體、字重、字距、行距等。
- **響應式設計**：通過 CSS 媒體查詢（Media Queries）來設計能夠在不同大小設備（如手機、平板、桌面）上自適應的網頁。
- **動畫與過渡**：CSS 也支持基本的動畫和過渡效果，能夠讓頁面更具動態感。

---

### 二、在 HTML 中引用 CSS 的三種方法

在 HTML 頁面中，可以通過三種方式來引用 CSS，它們各自有不同的用途和優點。

#### 1. **內聯樣式 (Inline CSS)**
內聯樣式是將 CSS 直接寫在 HTML 元素的 `style` 屬性中，這種方式只適用於單個元素，且它會覆蓋其他的 CSS 樣式。

- **語法**：
    ```html
    <h1 style="color: red; text-align: center;">這是紅色標題</h1>
    ```

- **特點**：
    - 這種方式很方便，但只適用於少數的元素，不適合大規模使用。
    - 由於將樣式和內容混合在一起，會使 HTML 文件變得不易維護。

#### 2. **內部樣式表 (Internal CSS)**
內部樣式表是將 CSS 代碼放在 HTML 文件的 `<head>` 標籤內的 `<style>` 標籤中，適用於在單個頁面中為多個元素設置樣式。

- **語法**：
    ```html
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>內部樣式表範例</title>
        <style>
            h1 {
                color: blue;
                text-align: center;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <h1>這是藍色標題</h1>
        <p>這是一段文字，會顯示在頁面上。</p>
    </body>
    </html>
    ```

- **特點**：
    - 適合為單個 HTML 文件提供樣式，避免重複定義。
    - 不同於內聯樣式，內部樣式表能夠為多個元素設置樣式。
    - 不適合大規模網站，因為樣式仍然是嵌入在每個 HTML 文件中。

#### 3. **外部樣式表 (External CSS)**
外部樣式表是將 CSS 代碼寫在一個單獨的 `.css` 文件中，然後在 HTML 文件的 `<head>` 部分通過 `<link>` 標籤來引用它。這是最常見且最佳的做法，尤其在處理大型網站時，能夠實現樣式的統一和重用。

- **語法**：
    1. **CSS 文件**（如 `styles.css`）：
        ```css
        h1 {
            color: green;
            text-align: center;
        }
        p {
            font-size: 16px;
            color: gray;
        }
        ```

    2. **HTML 文件**：
        ```html
        <!DOCTYPE html>
        <html lang="zh-Hant">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>外部樣式表範例</title>
            <link rel="stylesheet" href="styles.css">
        </head>
        <body>
            <h1>這是綠色標題</h1>
            <p>這是一段文字，會顯示在頁面上。</p>
        </body>
        </html>
        ```

- **特點**：
    - **樣式與內容分離**：將樣式和內容分開，保持 HTML 結構清晰，易於維護和管理。
    - **重用性**：一個外部 CSS 文件可以被多個 HTML 文件共享，減少重複代碼。
    - **最佳實踐**：對於大型網站或多頁面項目，這是最有效且可擴展的方案。

---

### 三、總結

- **內聯樣式**：將樣式直接寫在 HTML 標籤中，適用於簡單、單個元素的樣式修改，便於快速測試，但不建議大量使用。
- **內部樣式表**：將樣式寫在 HTML 文件的 `<style>` 標籤中，適用於單一頁面的樣式設置，較為清晰，但不適合大規模項目。
- **外部樣式表**：將 CSS 寫在獨立的 `.css` 文件中，並在 HTML 文件中引用，適用於所有規模的網站，能保持樣式和內容的分離，並且便於重用和維護。

在實際開發中，**外部樣式表** 是最推薦的方式，尤其是對於大型網站，這樣可以提高頁面的加載效率、減少重複代碼並便於維護。