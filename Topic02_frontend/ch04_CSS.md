
Ch04 CSS
===

## 投影片
:point_right: [nlh Slide- CSS](https://docs.google.com/presentation/d/1bFOmxDbSbIGHRwrFITqlc3SdZB33QmQ5dMBe2lVSPq0/edit?usp=sharing) 
* Basic CSS
* CSS Selectors
    * Simple; Combinator; Pseudo-class; Pseudo-element; Attribute selector
* Layout and Box model
* Style and Effects
* Responsive Design and Advanced Topics


:point_right: [W3school CSS](https://www.w3schools.com/css/default.asp)

:point_right: [nlh GitHub www-js](https://github.com/nlhsueh/www-js)
* **CSS demo**
* Bootstrap demo
* Javascript demo

## CSS 介紹

CSS（Cascading Style Sheets）是用來控制網頁樣式和佈局的技術。它允許開發者定義網頁元素的外觀，如顏色、字體、間距、佈局等。CSS 可以與 HTML 一起使用，通過選擇器將樣式應用於特定的 HTML 元素。簡單來說，HTML 用於結構化內容，而 CSS 則負責讓這些內容更具視覺吸引力和可讀性。

CSS 主要由三部分組成：
1. **選擇器**：指定要應用樣式的 HTML 元素。
2. **屬性**：定義樣式的具體行為（例如顏色、大小等）。
3. **值**：屬性的具體設置（例如顏色值、像素大小等）。

例如，下面的 CSS 代碼將一個段落文字的顏色設為紅色：

```css
p {
  color: red;
}
```

## 4.1 CSS 的五大主要選擇器

CSS 提供多種選擇器，讓開發者能夠根據不同條件精確地選擇和設置 HTML 元素的樣式。這裡介紹五個主要的選擇器。

---

### **範例程式 (自我介紹頁面)**

在接下來的練習中，我們可以使用這個簡單的「自我介紹」 HTML 結構作為練習的基礎。你可以將這段代碼複製到你的編譯器中運行，然後嘗試套用不同的選擇器。

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>我的自我介紹</title>
    <style>
        /* 基礎樣式 */
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            border: 1px solid #ddd;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 id="main-title">大家好，我是 [你的名字]</h1>
        
        <p class="intro">我是一名正在學習網頁前端開發的學生，對 <strong>CSS 選擇器</strong> 非常感興趣。</p>

        <h2>我的興趣</h2>
        <ul>
            <li>閱讀技術部落格</li>
            <li class="active">撰寫網頁專案</li>
            <li>參加技術研討會</li>
        </ul>

        <h2>聯絡我</h2>
        <p>你可以透過以下方式找到我：</p>
        <a href="https://github.com" target="_blank" title="我的 GitHub">GitHub 首頁</a>
        <a href="mailto:example@fcu.edu.tw">發送郵件</a>
    </div>
</body>
</html>
```

---

### 4.1.1. **簡單選擇器 (Simple Selector)**

簡單選擇器根據元素的名稱、ID、類名來選擇元素。常見的簡單選擇器有三種類型：

- **元素選擇器**：根據 HTML 元素的標籤名稱選擇元素。

| 符號 | 名稱 | 範例 | 說明 |
| :--- | :--- | :--- | :--- |
| **#** | **id selector** | `#ssn { background-color: yellow; }` | `<div id="ssn"> B123456789 </div>`<br>全文應只有一個地方 id 為 ssn |
| **.** | **class selector** | `.note { background-color: yellow; }` | `<div class="note"> I am a note </div>` |
| | | `p.note { background-color: yellow; }` | `<p class="note"> This is a note under p </p>` |
| **,** | **group selector** | `p, h1, h2 { background-color: yellow; }` | 標記為 p, h1, h2 的背景設為黃色 |

  ```css
  p {
    color: blue;
  }
  ```
  這樣的選擇器會選擇所有 `<p>` 標籤的元素，並將它們的文字顏色設為藍色。

- **ID 選擇器**：根據元素的 `id` 屬性選擇單一元素。`id` 必須是唯一的。
  ```css
  #header {
    background-color: gray;
  }
  ```
  這樣的選擇器會選擇 ID 為 `header` 的元素，並設置它的背景顏色為灰色。

- **類選擇器**：根據元素的 `class` 屬性選擇一組元素。可以應用於多個元素。
  ```css
  .button {
    padding: 10px;
    background-color: green;
  }
  ```
  這樣的選擇器會選擇所有具有 `button` 類名的元素，並設置內邊距和背景顏色。

**小練習：簡單選擇器**
請基於「自我介紹範例程式」，嘗試完成以下練習：
1. 使用 **ID 選擇器** 將主標題 (`#main-title`) 的文字顏色改為綠色。
2. 使用 **類控制選擇器** 將簡介段落 (`.intro`) 的文字大小改為 `1.2rem` 並加粗。
3. 使用 **元素選擇器** 將所有 `<h2>` 的下方補上 10px 的間距 (`margin-bottom: 10px`)。

---

### 4.1.2. **組合選擇器 (Combinator)**

組合選擇器根據元素之間的結構關係來選擇元素。這些選擇器可以是直接或間接關係的元素。

| 符號 | 名稱 | 範例 | 說明 |
| :--- | :--- | :--- | :--- |
| **(空格)** | **descendant** | `div p { background-color: yellow; }` | `div` 下的所有 `p` |
| **>** | **child** | `div > p { background-color: yellow; }` | `div` 下第一層的 `p` |
| **+** | **Adjcent sibling Selector** | `div + p { background-color: yellow; }` | `div` 同層鄰居的 `p` |
| **~** | **General sibling Selector** | `div ~ p { background-color: yellow; }` | `div` 同層的 `p` |

- **子元素選擇器 (`>`)**：選擇直接嵌套在某個元素內的子元素。
  ```css
  div > p {
    color: red;
  }
  ```
  這樣的選擇器會選擇所有直接位於 `div` 元素內的 `<p>` 元素。

- **後代元素選擇器 (空格)**：選擇所有嵌套在某個元素內的後代元素。
  ```css
  div p {
    font-size: 16px;
  }
  ```
  這樣的選擇器會選擇所有位於 `div` 元素內的 `<p>` 元素。

- **相鄰兄弟選擇器 (`+`)**：選擇緊接在某個元素後面的相鄰兄弟元素。
  ```css
  h1 + p {
    margin-top: 20px;
  }
  ```
  這樣的選擇器會選擇位於 `<h1>` 元素後面的第一個 `<p>` 元素。

- **一般兄弟選擇器 (`~`)**：選擇所有緊跟在某個元素後的兄弟元素。
  ```css
  h1 ~ p {
    color: green;
  }
  ```
  這樣的選擇器會選擇所有位於 `<h1>` 元素後的 `<p>` 元素。

**小練習：組合選擇器**
請基於「自我介紹範例程式」，嘗試完成以下練習：
1. 使用 **子元素選擇器 (`>`)** 僅將 `.container` 下的首層 `<h2>` 顏色改為藍色。
2. 使用 **後代選擇器** 將所有 `<ul>` 中的 `<li>` 加上圓點符號 (`list-style-type: circle`)。
3. 使用 **相鄰兄弟選擇器 (`+`)** 讓緊接在 `<h2>` 後方的段落文字加粗。

  ---

  小練習：
  請同學練習看看，使用以下這些屬性選擇器會對元素產生什麼樣的效果？

| Selector | Example | Example description |
| :--- | :--- | :--- |
| **`[attribute]`** | `[target]` | 有特定屬性的元素 |
| **`[attribute=value]`** | `[target="_blank"]` | 屬性有特定值的元素 |
| **`[attribute~=value]`** | `[title~="flower"]` | 屬性值包含特定字的元素 (空白分隔) |
| **`[attribute\|=value]`** | `[lang\|="en"]` | 屬性值以特定字開頭， `-` 分隔的元素 (或沒有) |
| **`[attribute^=value]`** | `a[href^="https"]` | 屬性值以特定字開頭的元素 |
| **`[attribute$=value]`** | `a[href$=".pdf"]` | 屬性值以特定字結尾的元素 |
| **`[attribute*=value]`** | `a[href*="w3schools"]` | 屬性值包含特定字的元素 |

**小練習：屬性選擇器**
請基於「自我介紹範例程式」，嘗試完成以下練習：
1. 使用 **`[target="_blank"]`** 選擇器，將外連連結的後方加上一個小圖標或標記（例如 `(EXT)`）。
2. 使用 **`[title]`** 選擇器，將所有擁有 `title` 屬性的元素加上下虛線。
3. 使用 **`[href^="mailto:"]`** 選擇器，將郵件連結的文字設為紅色。

---

### 4.1.3. **偽類選擇器 (Pseudo-class)**

偽類選擇器根據元素的**狀態**或**位置**選擇元素，常用於處理用戶交互或元素的狀態。

- **`:hover`**：當元素被鼠標懸停時觸發。
  ```css
  a:hover {
    color: red;
  }
  ```
  這樣的選擇器會讓 `<a>` 元素在鼠標懸停時變成紅色。

- **`:first-child`**：選擇某元素是其父元素的第一個子元素。
  ```css
  p:first-child {
    font-weight: bold;
  }
  ```
  這樣的選擇器會讓每個父元素的第一個 `<p>` 元素加粗。

- **`:nth-child()`**：選擇某元素是其父元素中的第幾個子元素。
  ```css
  li:nth-child(2) {
    color: blue;
  }
  ```
  這樣的選擇器會選擇父元素中的第二個 `<li>` 元素並將其文字顏色設為藍色。

- **`:active`**：當元素被激活（點擊）時觸發。
  ```css
  button:active {
    transform: scale(0.98);
  }
  ```

- **`:focus`**：當元素獲得焦點（如點擊輸入框）時觸發。
  ```css
  input:focus {
    border-color: blue;
    outline: none;
  }
  ```

- **`:checked`**：當單選框 (radio) 或複選框 (checkbox) 被勾選時觸發。
  ```css
  input:checked + label {
    font-weight: bold;
    color: red;
  }
  ```

- **`:not(selector)`**：選擇不符合括號內條件的元素。
  ```css
  li:not(.special) {
    color: gray;
  }
  ```


**小練習：偽類選擇器**
請基於「自我介紹範例程式」，嘗試完成以下練習：
1. 使用 **`:hover`** 讓滑鼠移到聯絡連結 (`<a>`) 上時，背景色變為淡黃色。
2. 使用 **`:nth-child(even)`** 將興趣列表中的偶數項目背景改為灰色。
3. 使用 **`:active`** 讓點擊連結時有稍微縮小的動畫效果 (`transform: scale(0.95)`)。

---

### 4.1.4. **偽元素選擇器 (Pseudo-element)**

偽元素選擇器允許開發者選擇元素的一部分並設置樣式。常見的偽元素包括：

- **`::before`**：在元素內容之前插入內容。
  ```css
  p::before {
    content: "Note: ";
    font-weight: bold;
  }
  ```
  這樣的選擇器會在每個 `<p>` 元素的內容前插入 "Note: "。

- **`::after`**：在元素內容之後插入內容。
  ```css
  p::after {
    content: " (end)";
  }
  ```
  這樣的選擇器會在每個 `<p>` 元素的內容後插入 "(end)"。

- **`::first-letter`**：選擇元素的第一個字母。
  ```css
  p::first-letter {
    font-size: 2em;
    color: red;
  }
  ```
  這樣的選擇器會使每個 `<p>` 元素的第一個字母變大並顯示為紅色。

- **`::selection`**：選擇用戶正在選取的文字部分。
  ```css
  ::selection {
    background: yellow;
    color: black;
  }
  ```

- **`::placeholder`**：選擇輸入元素的提示文字 (placeholder)。
  ```css
  input::placeholder {
    color: #ccc;
    font-style: italic;
  }
  ```

- **`::first-line`**：選擇元素內容的第一行。
  ```css
  p::first-line {
    font-variant: small-caps;
    color: darkblue;
  }
  ```

**小練習：偽元素選擇器**
請基於「自我介紹範例程式」，嘗試完成以下練習：
1. 使用 **`::selection`** 讓使用者選取網頁文字時，背景變為紫色，文字變為白色。
2. 使用 **`::first-line`** 將自我介紹段落的第一行設為粗體。
3. 使用 **`::after`** 在每個 `<h2>` 的標題後方加上一個符號 `🔗` (`content: " 🔗"`)。



---

### 4.1.5. **屬性選擇器 (Attribute Selector)**


屬性選擇器讓你能根據元素的屬性來選擇元素。

| Selector | Example | Example description |
| :--- | :--- | :--- |
| **`[attribute]`** | `[target]` | 有特定屬性的元素 |
| **`[attribute=value]`** | `[target="_blank"]` | 屬性有特定值的元素 |
| **`[attribute~=value]`** | `[title~="flower"]` | 屬性值包含特定字的元素 (空白分隔) |
| **`[attribute\|=value]`** | `[lang\|="en"]` | 屬性值以特定字開頭， `-` 分隔的元素 (或沒有) |
| **`[attribute^=value]`** | `a[href^="https"]` | 屬性值以特定字開頭的元素 |
| **`[attribute$=value]`** | `a[href$=".pdf"]` | 屬性值以特定字結尾的元素 |
| **`[attribute*="value"]`** | `a[href*="w3schools"]` | 屬性值包含特定字的元素 |

> [!TIP]
> **屬性選擇器差異詳解：**
> 這些選擇器在處理「部分匹配」時非常有用，特別是當屬性包含多個值或特定格式時：
> - **`[attr~="val"]`** (包含單字)：選擇屬性值中包含 `val` 這個 **完整單字**（以空格分隔）的元素。
>   - 範例：`<div class="btn primary">` 會被 `[class~="btn"]` 匹配。
> - **`[attr|="val"]`** (特定開頭)：選擇屬性值是 `val` 或以 `val-` **開頭** 的元素（常用於語言標籤）。
>   - 範例：`<p lang="en-US">` 會被 `[lang|="en"]` 匹配。
> - **`[attr^="val"]`** (開頭)：選擇屬性值以 `val` **開頭** 的元素。
>   - 範例：`<a href="https://example.com">` 會被 `[href^="https"]` 匹配。
> - **`[attr$="val"]`** (結尾)：選擇屬性值以 `val` **結尾** 的元素。
>   - 範例：`<img src="cover.jpg">` 會被 `[src$=".jpg"]` 匹配。
> - **`[attr*="val"]`** (包含字串)：選擇屬性值中包含 `val` **任何片段** 的元素。
>   - 範例：`<a href="news-2024.html">` 會被 `[href*="2024"]` 匹配。

- **`[attr]`**：選擇擁有指定屬性的元素。
  ```css
  input[type="text"] {
    border: 1px solid blue;
  }
  ```
  這樣的選擇器會選擇所有 `type` 屬性為 `text` 的 `<input>` 元素並為其添加邊框。

- **`[attr="value"]`**：選擇屬性值等於指定值的元素。
  ```css
  a[href="https://example.com"] {
    color: green;
  }
  ```
  這樣的選擇器會選擇所有 `href` 屬性為 `https://example.com` 的 `<a>` 元素，並設置其顏色為綠色。

---

### 4.1 測驗題

1. 哪個 CSS 選擇器會選擇所有 `<div>` 標籤的元素？
   - A. `.div`
   - B. `#div`
   - C. `div`
   - D. `*`

2. 如何選擇 `id="header"` 的元素？
   - A. `header`
   - B. `.header`
   - C. `#header`
   - D. `*header`

3. `a:hover` 是哪種類型的選擇器？
   - A. 簡單選擇器
   - B. 組合選擇器
   - C. 偽類選擇器
   - D. 偽元素選擇器

4. 以下哪一個選擇器會選擇父元素中的第三個 `<p>` 元素？
   - A. `p:nth-child(3)`
   - B. `p:nth-of-type(3)`
   - C. `p:first-child`
   - D. `p:last-child`

5. 什麼 CSS 選擇器可以根據元素的 `type` 屬性選擇所有 `text` 類型的輸入框？
   - A. `[type="text"]`
   - B. `input[type="text"]`
   - C. `.text`
   - D. `input`

**4.1 測驗題答案：**
<details>
<summary>點擊展開看解答</summary>

1. **C** (元素選擇器直接使用標籤名)
2. **C** (`#` 代表 ID)
3. **C** (描述元素狀態的是偽類)
4. **A** (`nth-child(n)` 選擇第 n 個子元素)
5. **B** (結合元素與屬性選擇器最為精確)

</details>

---

### 4.1 練習題

#### 練習一
1. 使用 `::before` 偽元素在每個 `<h2>` 標題前添加 "Chapter: "。
2. 使用 `:nth-child()` 選擇器將每個父元素中的奇數項 `<li>` 文字顏色設為紅色。
3. 使用屬性選擇器，選擇所有 `type="checkbox"` 的 `<input>` 元素並設置它們的背景顏色為黃色。

#### 練習二
4. **課表應用**：使用 `:first-child` 選擇器，將課表表格中每一行的第一個儲存格（時段欄位）背景顏色設為 `#f2f2f2`，並將字體加粗。

5. **課表應用**：使用 **後代選擇器 (Descendant Selector)**，將課表中所有包含在 `<td>` 內的超連結 (`<a>`) 顏色設為橘色 (`orange`)，並移除下標線 (`text-decoration: none`)。

## 4.2 尺寸單位

### 單位定義與特性表

| 單位 | 類型 | 基準點 (Reference) | 特點 |
| --- | --- | --- | --- |
| **px** | 絕對 | 螢幕像素 (Pixel) | 固定大小，最精確但不具備彈性。 |
| **em** | 相對 | **父元素** 的字體大小 | 會產生「複利效應」，層級愈深計算愈複雜。 |
| **rem** | 相對 | **根元素 (`<html>`)** 的字體大小 | 全域統一基準，目前網頁設計的主流建議。 |
| **vw** | 相對 | **視窗寬度 (Viewport Width)** | 隨瀏覽器視窗大小即時縮放。 |

---

**px (Pixels)**

* **本質**：它是最直覺的單位。如果你設 `20px`，無論在什麼裝置上它就是 20 個像素點。
* **缺點**：不利於**無障礙設計 (Accessibility)**。如果使用者在瀏覽器設定「大字體」，使用 `px` 的網頁文字不會隨之放大。

**em (Relative to Parent)**

* **邏輯**：如果父元素是 `16px`，子元素設 `2em` 就會變成 `32px`。
* **風險**：如果在嵌套結構中使用（例如多層列表），每一層都會乘以父層的大小，導致字體縮放失控。

**rem (Root em)**

* **邏輯**：`rem` 的 `r` 代表 **Root**。它永遠只參考 `<html>` 標籤的大小（預設通常是 `16px`）。
* **優點**：它解決了 `em` 的複利問題，同時又保有彈性。當使用者調整瀏覽器字級時，整個網頁會成比例縮放。
* **公式**：
$$Target\ Px / Root\ Px = rem$$


（例如：$24px / 16px = 1.5rem$）

**vw (Viewport Width)**

* **邏輯**：`1vw` 等於視窗寬度的 **1%**。
* **應用**：常用於製作「大標題」或「滿版佈局」，確保在手機或超大螢幕上，元素比例都能維持一致。

---

### 該選哪一個？

1. **文字與間距**：優先使用 **`rem`**（Tailwind 預設也是 `rem`）。這對 RWD 響應式設計最友善。
2. **邊框與細微偏移**：使用 **`px`**。因為 1 像素的邊框不需要隨字體縮放。
3. **大區塊佈局**：使用 **`vw`** 或 **`vh`** (Viewport Height)，可以輕鬆做出滿版效果。

---

### 練習題

> 「如果 `<html>` 是 `16px`，父元素是 `2rem`，子元素是 `1.5em`，請問子元素實際是多少像素？」

**答案解析：**

* 父元素 = $16 \times 2 = 32px$
* 子元素 = $32 \times 1.5 = 48px$


## 4.3 CSS 排版與盒模型

在 CSS 中，**佈局 (Layout)** 和 **盒模型 (Box Model)** 是設計網頁結構和樣式的基礎概念。理解這些概念有助於更有效地控制網頁元素的顯示和排列。

---

### **1. CSS Box Model (盒模型)**

盒模型是 CSS 中用來描述元素如何在頁面上呈現的框架結構。每個元素都被視為一個矩形框，它由以下四個部分組成：

- **Content (內容區域)**：元素的實際內容，如文字或圖片，這部分的大小由元素的 `width` 和 `height` 設定決定。
- **Padding (內邊距)**：內容區域與邊框之間的間距，內邊距不影響元素的總寬度或總高度，但會增加元素的可視區域。這部分的大小可用 `padding` 屬性設定。
- **Border (邊框)**：包圍內容和內邊距的邊框，邊框的寬度、樣式和顏色可以通過 `border` 屬性進行設定。
- **Margin (外邊距)**：元素外部與其他元素之間的空白區域。外邊距不會影響元素的寬度或高度，但會影響元素之間的間距。這部分的大小可以用 `margin` 屬性設定。

#### Box Model 範例：
```css
div {
  width: 200px;
  height: 100px;
  padding: 20px;
  border: 5px solid black;
  margin: 10px;
}
```
在這個例子中，`div` 的實際顯示區域會是：
- 實際內容區域寬度：200px
- 內邊距：20px
- 邊框：5px
- 外邊距：10px

這樣，`div` 的總寬度會是：`200px (內容) + 20px (左內邊距) + 20px (右內邊距) + 5px (左邊框) + 5px (右邊框) = 250px`。

---

### **2. CSS Layout (佈局)**

CSS 佈局控制著元素在頁面上的排列方式。這裡介紹三種常用的佈局方式：

- **Normal Flow (常規文檔流)**：
  在常規文檔流中，元素依照它們在 HTML 中的順序進行排列。大多數元素（如 `<div>` 和 `<p>`）會以塊級元素顯示，從上到下排列，並占據整個行的寬度。

- **Flexbox (彈性盒模型)**：
  Flexbox 是一種強大的佈局工具，專門用於一維佈局。它允許容器內的元素按指定的方式排列，並自動調整大小以適應容器。Flexbox 的常用屬性包括 `display: flex`、`justify-content`、`align-items` 等。

  **Flexbox 範例：**
  ```css
  .container {
    display: flex;
    justify-content: space-between;
  }
  .item {
    width: 30%;
  }
  ```
  這個例子會將 `.container` 內的 `.item` 元素按水平方向排列，並使它們均勻分佈。

- **Grid (網格佈局)**：
  CSS Grid 允許建立二維佈局，即同時控制行和列的排列。這使得複雜的網頁佈局變得更簡單，並且能夠精確控制每個區域的大小。

  **Grid 範例：**
  ```css
  .container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: 10px;
  }
  .item {
    background-color: lightblue;
  }
  ```
  在這個例子中，`.container` 會被分成三列，第一列和第三列寬度相同，第二列的寬度是第一列和第三列的兩倍，並且元素間有 10px 的間隔。

---

### 3. `box-sizing` 屬性介紹

在 CSS 中，`box-sizing` 屬性控制著如何計算元素的寬度和高度。它決定了元素的總寬度和高度是否包含內邊距（`padding`）和邊框（`border`）的尺寸。`box-sizing` 有兩個主要的值：

---

#### **1. `content-box` (預設值)**

這是 CSS 的預設值。當 `box-sizing` 設置為 `content-box` 時，`width` 和 `height` 只會計算元素的內容區域，不包括內邊距和邊框的大小。也就是說，元素的總寬度和總高度是由內容區域的寬高，加上內邊距和邊框來確定的。

##### 例子：
```css
div {
  width: 200px;
  padding: 20px;
  border: 5px solid black;
  box-sizing: content-box;
}
```

在這個例子中：
- **內容區域寬度**是 200px
- **內邊距**是 20px
- **邊框**是 5px

元素的總寬度將是：`200px (內容) + 20px (左內邊距) + 20px (右內邊距) + 5px (左邊框) + 5px (右邊框) = 250px`。

---

#### **2. `border-box`**

當 `box-sizing` 設置為 `border-box` 時，`width` 和 `height` 會包括元素的內容區域、內邊距和邊框的大小。也就是說，元素的總寬度和總高度將等於設置的 `width` 和 `height`，並且內邊距和邊框的尺寸會從內容區域的寬高中扣除。

##### 例子：
```css
div {
  width: 200px;
  padding: 20px;
  border: 5px solid black;
  box-sizing: border-box;
}
```

在這個例子中：
- **總寬度**是 200px（包含了內邊距和邊框）
- **內邊距**和**邊框**會在內容區域內扣除，所以內容區域的實際寬度會減少。

元素的內容區域寬度會是：`200px - 20px (左內邊距) - 20px (右內邊距) - 5px (左邊框) - 5px (右邊框) = 150px`。

---

使用場景

- **`content-box`**：當你希望確保元素的內容區域具有固定的寬度和高度，並且不關心內邊距和邊框的尺寸對元素總尺寸的影響時，使用 `content-box`。
  
- **`border-box`**：當你希望元素的總寬度或總高度固定，並且想要內邊距和邊框包含在內時，使用 `border-box`。這對於設計響應式佈局特別有用，因為它能確保元素在調整尺寸時保持一致。

---

通常的做法

為了避免每次都手動調整元素的寬度和高度，許多開發者會將 `box-sizing` 設置為 `border-box`，並將此設定應用於所有元素。這樣能確保所有元素的總寬度和高度不會被內邊距和邊框的大小所影響，簡化布局計算。

```css
* {
  box-sizing: border-box;
}
```

這行代碼會將所有元素的 `box-sizing` 設置為 `border-box`，這樣每個元素的寬度和高度將包含內邊距和邊框的尺寸。

---

#### 小結

- **`content-box`**：寬度和高度只計算內容區域，不包括內邊距和邊框。
- **`border-box`**：寬度和高度計算包含內邊距和邊框，內容區域的寬度和高度會減少。

使用 `border-box` 能使佈局更加簡單和直觀，這也是許多現代 CSS 框架（如 Bootstrap）推薦的做法。


---

### 測驗題

1. 哪個 CSS 屬性用來設定元素的內邊距？
   - A. `border`
   - B. `padding`
   - C. `margin`
   - D. `width`

2. 若一個元素有 `width: 100px`，`padding: 10px`，`border: 5px solid black`，那麼該元素的總寬度是多少？
   - A. 100px
   - B. 120px
   - C. 130px
   - D. 150px

3. 在 Flexbox 佈局中，哪個屬性用來設置元素之間的對齊方式？
   - A. `justify-content`
   - B. `align-items`
   - C. `flex-wrap`
   - D. `align-content`

4. 當 CSS 屬性 `box-sizing` 設為 `border-box` 時，元素的總寬度會包含以下哪一項？
   - A. 內容區域的寬度
   - B. 內邊距和邊框的尺寸
   - C. 內邊距和邊框的尺寸會被排除在外
   - D. 僅內容區域的寬度，邊框會扣除

5. 在 `box-sizing: content-box` 的情況下，元素的寬度計算會：
   - A. 包含內邊距和邊框的寬度
   - B. 只計算內容區域的寬度，內邊距和邊框不包括在內
   - C. 只包含內邊距
   - D. 只包含邊框

---

### 練習題

1. 使用 Flexbox 將三個 `.item` 元素放在一行，並使它們均勻分佈，且每個元素的寬度相等。
2. 使用 CSS Grid 創建一個三列的佈局，第一列的寬度為 `1fr`，第二列的寬度為 `2fr`，第三列的寬度為 `1fr`。並且給每個元素設定 10px 的間距。
3. 設計一個包含兩個區塊的頁面，使用 CSS 盒模型確保其中一個區塊有 20px 的內邊距，5px 的邊框，並且與另一個區塊保持 10px 的外邊距。

---

## 4.4 CSS 樣式與效果

CSS（層疊樣式表）是用來控制 HTML 元素的外觀和排版的技術。透過 CSS，我們可以設計出美觀的網頁佈局、特效和動畫。以下是 CSS 中一些常用的樣式與效果，這些技巧將幫助你創建富有吸引力的網頁。

---

### **文字樣式 (Text Style)**

文字樣式屬性可以控制文字的外觀，從字體到字距、顏色等，都可以透過 CSS 進行設置。

- **字體家族 (`font-family`)**：設定文字所使用的字型。
  ```css
  p {
    font-family: "Arial", sans-serif;
  }
  ```

- **字型大小 (`font-size`)**：設定文字的大小。
  ```css
  p {
    font-size: 16px;
  }
  ```

- **字重 (`font-weight`)**：控制文字的粗細。
  ```css
  p {
    font-weight: bold;
  }
  ```

- **字母間距 (`letter-spacing`)**：調整字母間的距離。
  ```css
  p {
    letter-spacing: 2px;
  }
  ```

- **行高 (`line-height`)**：設置行間距，使文字更易讀。
  ```css
  p {
    line-height: 1.5;
  }
  ```

---

### **背景樣式 (Background)**

CSS 背景屬性讓你能為網頁元素設置背景顏色或背景圖片。

- **背景顏色 (`background-color`)**：設定元素的背景顏色。
  ```css
  div {
    background-color: lightblue;
  }
  ```

- **背景圖片 (`background-image`)**：設定背景圖片，並可調整其顯示方式。
  ```css
  div {
    background-image: url("image.jpg");
    background-size: cover; /* 覆蓋整個元素 */
    background-position: center; /* 背景置中 */
  }
  ```

---

### **位置與浮動 (Position and Floating)**

CSS 位置屬性控制元素在頁面上的位置，而浮動則控制元素如何與其他元素排列。

- **定位 (`position`)**：控制元素的定位方式。
  - `static`：預設值，元素按正常文檔流排列。
  - `relative`：相對於元素的正常位置移動。
  - `absolute`：相對於最近的已定位祖先元素定位。
  - `fixed`：相對於視窗固定位置。
  ```css
  div {
    position: relative;
    top: 10px;
    left: 20px;
  }
  ```

- **浮動 (`float`)**：使元素浮動，並且文字或其他元素會圍繞它。
  ```css
  img {
    float: left;
    margin-right: 10px;
  }
  ```

- **清除浮動 (`clear`)**：防止元素與浮動元素重疊。
  ```css
  .clear {
    clear: both;
  }
  ```

---

### **溢出與流 (Overflow and Flow)**

溢出和流控制元素內部內容如何顯示，特別是當內容超出容器時。

- **溢出 (`overflow`)**：控制元素內容超出範圍時的顯示方式。
  ```css
  div {
    overflow: hidden; /* 隱藏超出部分 */
  }
  ```

- **自動換行 (`word-wrap`)**：控制長單字是否自動換行。
  ```css
  p {
    word-wrap: break-word;
  }
  ```

---

### **過渡效果 (Transitions)**

過渡效果讓元素的屬性變化在一定時間內平滑過渡，這樣可以創建動態效果。

- **過渡屬性 (`transition`)**：控制屬性變化的時間、延遲及方式。
  ```css
  div {
    transition: all 0.5s ease;
  }
  div:hover {
    background-color: yellow;
  }
  ```

在這個範例中，當滑鼠懸停在元素上時，背景顏色會在 0.5 秒內平滑變化。

---

### **動畫 (Animations)**

CSS 動畫比過渡效果更強大，允許元素在一段時間內進行多個屬性變化。

- **關鍵幀 (`@keyframes`)**：定義動畫的每一幀，決定動畫的起始和結束狀態。
  ```css
  @keyframes example {
    0% {
      background-color: red;
    }
    100% {
      background-color: blue;
    }
  }

  div {
    animation: example 3s infinite;
  }
  ```

這個例子讓元素的背景顏色在 3 秒鐘內從紅色過渡到藍色，並且無限循環。

---

### **變形 (Transformations)**

變形屬性使元素進行旋轉、縮放、平移或傾斜。

- **旋轉 (`rotate`)**：旋轉元素。
  ```css
  div {
    transform: rotate(45deg);
  }
  ```

- **縮放 (`scale`)**：縮放元素的大小。
  ```css
  div {
    transform: scale(1.5);
  }
  ```

- **平移 (`translate`)**：移動元素。
  ```css
  div {
    transform: translate(50px, 100px);
  }
  ```

---

### **陰影與邊框 (Shadows and Borders)**

- **陰影 (`box-shadow`)**：給元素添加陰影效果。
  ```css
  div {
    box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.5);
  }
  ```

- **文本陰影 (`text-shadow`)**：給文本添加陰影。
  ```css
  h1 {
    text-shadow: 2px 2px 5px gray;
  }
  ```

- **邊框 (`border`)**：設定元素的邊框。
  ```css
  div {
    border: 2px solid black;
  }
  ```

---

### **排版與列 (Typography and Columns)**

- **字體大小與行高**：透過 `font-size` 和 `line-height` 屬性設置文字的大小和行間距。
  ```css
  p {
    font-size: 18px;
    line-height: 1.6;
  }
  ```

- **多欄布局 (`columns`)**：將文本分成多欄顯示。
  ```css
  article {
    columns: 2;
    column-gap: 20px;
  }
  ```

---

### 測驗題

1. 以下哪個 CSS 屬性可以用來設定元素的背景顏色？
   - A. `color`
   - B. `background-color`
   - C. `border-color`
   - D. `font-color`

2. 使用 `transition` 時，若希望元素背景顏色在 1 秒內平滑變化，應使用以下哪個屬性？
   - A. `transition-duration`
   - B. `transition-property`
   - C. `transition-timing-function`
   - D. `transition`

3. 在 CSS 動畫中，`@keyframes` 用來設定：
   - A. 動畫的持續時間
   - B. 動畫的屬性
   - C. 動畫的起始和結束狀態
   - D. 動畫的方向

4. 如何給文本添加陰影？
   - A. `box-shadow`
   - B. `text-shadow`
   - C. `shadow`
   - D. `color-shadow`

5. 在 `box-sizing: border-box` 佈局中，`width` 屬性會包括：
   - A. 內容區域、內邊距和邊框
   - B. 內容區域
   - C. 內邊距和邊框
   - D. 內容區域和內邊距

---

### 練習題

1. 設計一個 `div` 元素，當滑鼠懸停時，背景顏色從紅色變為綠色，並且這個過渡效果持續 0.7 秒。
2. 創建一個 3 欄的文本布局，每欄的寬度各自為 `33%`，並設置每欄之間的間距為 `20px`。
3. 使用 `transform` 屬性將一個 `div` 元素旋轉 45 度，並使它縮放至 1.2 倍大小。


## 4.5 其他

### picsum and lorem

假圖產生器
* Install “picsum” plugin
* 只要打 picsum 就會跳出選項
```html
<img src="https://picsum.photos/200">
<img src="https://picsum.photos/300/200">
<img src="https://picsum.photos/200?random=1">
```

假文字產生器

* In visual studio editor
* install lorem
* install ctlorem
* 只要打 lorem200 => 產生 200 個英文字
* 只要打 ctlorem10 => 產生 10 個中文字

---

### Flex box

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, 
                                   initial-scale=1.0">
    <title>Flex box demo</title>
</head>
<style>
    .flex-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        flex-wrap: wrap;
        align-items: start;
    }

    .item {
        border: 1px solid red;
        width: 50px;
        height: 50px;
        background-color: antiquewhite;
        margin: 10px;
        text-align: center;
    }

    .wide {
        width: 70px;
    }

    .long {
        height: 70px;
    }
</style>

<body>

    <div class="flex-container">
        <div class="item"></div>
        <div class="item long"></div>
        <div class="item wide"></div>
        <div class="item long wide"></div>
        <div class="item"></div>
        <div class="item long"></div>
        <div class="item wide"></div>
        <div class="item long wide"></div>
    </div>

</body>

</html>
```
![](https://hackmd.io/_uploads/rJltxwcl6.png)

## 綜合練習

### 練習 4.1
:basketball: Exercise01 :basketball:

* 整體內容置中，寬度 800px
* h1 變顏色置中，前面會自動加上報紙符號 (emoji 🗞️)
* 圖片可以設定 class 為 R 或 L, 表示 float 為 right/left; 邊框圓潤; 滑鼠移過去時清晰度加強 (原 opacity 低); 有設定 margin 所以圖和字不會黏在一起。
* 標記 boy 或 girl; 個有不同的顏色及後置符號（👦👧）。

![image](https://hackmd.io/_uploads/S1gwfk8R6.png)

[ccc](https://www.icloud.com/iclouddrive/0d6K8_AQmRS4Rt8ZUOrLhd6Xg#CCS)

---

### 練習 4.2

:basketball: Exercise02 :basketball:

同上，當滑鼠移動時會有互動
* 宣告一個 container，內放置圖片與名字。當滑鼠移到照片時，照片變清晰; 框也會出現。
* 使用 position 來進行文字在圖中的定位。
* 當滑鼠移到名字時，名字變大。
* [參考: style image](https://www.w3schools.com/css/css3_images.asp)

<img src="https://hackmd.io/_uploads/r1xJLUUAp.png" width="200px">
<img src="https://hackmd.io/_uploads/Hy9m88L0a.png" width="200px">

---
### 練習 4.3

:basketball: Exercise03 :basketball:
* 到 [道奇官網](http://www.mlb.com/dodgers/roster) 獲取球員訊息。
* 設計一個球員卡的展覽頁面。
* 版面設為 85% 寬。
* 使用 float left 來做球員卡的排版。
* 為球員姓名及編號設計 player 及 pno 等 class, 前者名字加粗，後者加上底線。參考 font-weight 及 text-decoration。
* 移到球員時，邊框會出現。
* 點擊球員照片時，會跳到該球員的官網。
* 使用 box-sizing 避免可能的跑版。

![image](https://hackmd.io/_uploads/H1zC4uIR6.png)

---

### 練習 4.4

:basketball: Exercise04 :basketball:

請選擇一個應用系統，並應用 [此版面](https://www.w3schools.com/css/css_website_layout.asp) 設計其首頁：
* 大谷翔平個人官網
* 逢甲大學資工系首頁
* Ace 網球會員管理系統
* HappyBear 訂餐系統
* ezGo 旅遊規劃網
* 喀嚓相機租借系統
* ShowShow 電影訂位系統

:point_right: 請說明你的設計巧思與應用 :point_left: