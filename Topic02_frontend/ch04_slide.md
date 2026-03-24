---
marp: true
theme: default
paginate: true
header: '第 4 章：CSS 網頁樣式'
footer: '逢甲大學資工系 - Web 前端開發'
backgroundColor: #fff
---

# 第 4 章：CSS 網頁樣式
## (Cascading Style Sheets)

CSS 負責定義網頁的視覺展現。HTML 決定「內容與結構」，CSS 決定「外觀與佈局」。

---

## 4.1 CSS 核心組成

- **選擇器 (Selector)**：指定 HTML 元素。
- **屬性 (Property)**：定義樣式行為（顏色、大小等）。
- **值 (Value)**：具體的設定參數。

```css
p {
  color: red;    /* 屬性: 值 */
}
```

---

## 4.1 隨堂測驗 👋

**Q: 以下哪一個 CSS 宣告能正確將文字顏色設為黑色？**

A. `text-color: black;`
B. `color: #000;`
C. `font-style: black;`
D. `color-style: black;`

---

## 4.1 隨堂測驗 (解答)

**解答：B. `color: #000;`**

- 設定文字顏色必須使用 `color` 屬性。
- `#000` 為黑色的十六進位色碼簡寫（等於 `#000000`）。

---

## 4.2 CSS 選擇器大觀園

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=css/demo-selectors.html)

CSS 提供多種選擇器，讓開發者能精確選取 HTML 元素。這部分是 CSS 的核心靈魂。

---

## 4.2.1 簡單選擇器 (Simple Selectors)

根據名稱、ID 或類別 (Class) 選取元素。

- **元素選擇器**: `p { ... }` (全部段落)
- **ID 選擇器**: `#header { ... }` (唯一 ID)
- **類別選擇器**: `.btn { ... }` (一組元件)
- **群組選擇器**: `h1, h2, p { ... }` (同時選多個)

---

## 4.2.1 隨堂測驗 👋

**Q: 哪一個選擇器代表「類別為 note 的 p 元素」？**

A. `#note p`
B. `p.note`
C. `p > note`
D. `p, .note`

---

## 4.2.1 隨堂測驗 (解答)

**解答：B. `p.note`**

- `p.note` 代表同時具備 `p` 標籤且 Class 為 `note` 的元素（選擇器之間沒有空格）。
- `#note p` 是後代選擇器；`p > note` 是子選擇器；`p, .note` 是群組選擇器。

---

## 4.2.2 組合選擇器 (Combinators)

根據元素間的結構關係來選取。

| 符號 | 名稱 | 說明 (範例: `div ? p`) |
| :--- | :--- | :--- |
| **(空格)** | 後代選擇器 | `div` 內的所有 `p` (不限層級) |
| **>** | 子元素選擇器 | 僅限 `div` 下的第一層 `p` |
| **+** | 相鄰兄弟 | 緊接在 `div` 後的第一個 `p` |
| **~** | 一般兄弟 | `div` 後的所有同層 `p` |

---

## 4.2.2 隨堂測驗 👋

**Q: 在以下結構中，`div > p` 會選中哪些顏色？**

```html
<div>
  <p>紅色</p>
  <section>
    <p>藍色</p>
  </section>
</div>
```

---

## 4.2.2 隨堂測驗 (解答)

**解答：紅色**

- `>` 是**子元素選擇器**，只會選取 `div` 的「第一層」直系子元素。
- 「藍色」的 `<p>` 標籤被包在 `<section>` 內，屬於 `div` 的孫元素，所以不會被選中。

---

## 4.2.3 屬性選擇器 (Attribute Selectors)

根據 HTML 屬性或屬性值選取。

- **`[target]`**: 有 `target` 屬性的元素。
- **`[type="text"]`**: 類型精確匹配。
- **匹配模式**:
  - `^=`: 開頭匹配 (例: `a[href^="https"]`)
  - `$=`: 結尾匹配 (例: `a[href$=".pdf"]`)
  - `*=`: 包含匹配 (例: `[title*="flower"]`)

---

## 4.2.3 隨堂測驗 👋

**Q: 如何選取所有「連結到內部錨點 (以 # 開頭)」的 `<a>` 標籤？**

A. `a[href="#"]`
B. `a[href^="#"]`
C. `a[href$="#"]`
D. `a:link`

---

## 4.2.3 隨堂測驗 (解答)

**解答：B. `a[href^="#"]`**

- `^=` 符號代表「開頭匹配」。這會選中所有 `href` 屬性值以 `#` 作為開頭的 `<a>` 標籤。
- 補充：`$=` 是結尾匹配，`*=` 是包含匹配。

---

## 4.2.4 偽類 (Pseudo-classes)

描述元素的**特定狀態**或**結構位置**。

- **動態狀態**: `:hover`, `:active`, `:focus`
- **結構位置**:
  - `:first-child` / `:last-child`
  - `:nth-child(n)` (例: `even`, `odd`, `3n`)
- **表單狀態**: `:checked`, `:disabled`
- **否定**: `:not(.special)`

---

## 4.2.4 隨堂測驗 👋

**Q: 若要將清單中「第 3 個項目以後」的所有項目變淡，可以使用哪個選擇器？**

A. `li:nth-child(3)`
B. `li:nth-child(n+4)`
C. `li:last-child`
D. `li:not(:first-child)`

---

## 4.2.4 隨堂測驗 (解答)

**解答：B. `li:nth-child(n+4)`**

- `n` 是從 `0` 開始帶入的變數。當 `n=0` 時結果為第 4 項；`n=1` 時結果為第 5 項，以此類推。
- 這個選擇器能精確選取「第 4 個 (也就是第 3 個之後)」開始的所有同層同類型項目！

---

## 4.2.5 偽元素 (Pseudo-elements)

選取元素的**特定部分**，通常用於裝飾。

- **`::before` / `::after`**: 在內容前後插入裝飾 (必須搭配 `content: "";`)。
- **`::first-letter`**: 首字放大。
- **`::selection`**: 選取文字時的背景色。
- **`::placeholder`**: 輸入框提示文字樣式。

---

## 4.2.5 隨堂測驗 👋

**Q: 使用 `::before` 插入裝飾符號時，哪一個屬性是「絕對必要」的？**

A. `display`
B. `content`
C. `position`
D. `background`

---

## 4.2.5 隨堂測驗 (解答)

**解答：B. `content`**

- `::before` 和 `::after` 必須有 `content` 屬性才能在畫面上產生出真正的偽元素。
- 即便只是想要產生一個背景色形狀，也至少要給予 `content: "";` (空字串)。

---

## 4.3 尺寸單位 (Units)

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=css/demo-units.html)

| 單位 | 基準點 | 適用情境 |
| :--- | :--- | :--- |
| **px** | 固定像素 | 邊框、極小細節 |
| **em** | 父元素字級 | 元件內部的相對比例 |
| **rem** | 根元素 (`<html>`) | **文字大小 (RWD 首選)** |
| **vw/vh** | 視窗寬/高 | 滿版背景、大標題 |

> **💡 提示 (TIP):**
> **公式**：Target Px / Root Px (16) = **rem**

---

## 4.3 隨堂測驗 👋

**Q: 在根元素為 16px 的情況下，`2.5rem` 等於多少像素？**

A. 32px
B. 40px
C. 48px
D. 20px

---

## 4.3 隨堂測驗 (解答)

**解答：B. 40px**

- `rem` 是相對於 `<html>` 根元素字級的單位。
- 對於 16px 的根元素，1 rem = 16px。因此 `2.5rem` = 16px × 2.5 = 40px。

---

## 4.4 盒模型 (Box Model)

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=css/demo-box-model.html)

- **Content**: 實際內容。
- **Padding**: 內邊距 (內容與邊框間)。
- **Border**: 邊框。
- **Margin**: 外邊距 (元素與元素間)。

### box-sizing 關鍵設定
- `content-box` (預設): 寬度不含 Padding/Border。
- `border-box`: **總寬度**包含 Padding/Border。

---

## 4.4.2 彈性盒佈局 (Flexbox)

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=css/demo-flexbox.html)

一維佈局神器，輕鬆處理對齊與空間分配。

- **容器 (Container)**: `display: flex;`, `justify-content`, `align-items`
- **項目 (Items)**: `flex-grow`, `order`

---

## 4.4 隨堂測驗 👋

**Q: 若要讓 Flex 容器內的子元素「垂直水平皆置中」，應如何設定？**

```css
.container {
  display: flex;
  justify-content: _______;
  align-items: _______;
}
```

---

## 4.4 隨堂測驗 (解答)

**解答：`justify-content: center;` 與 `align-items: center;`**

- `justify-content: center;` 負責主軸（預設為水平）置中。
- `align-items: center;` 負責交錯軸（預設為垂直）置中。

---

## 4.5 樣式特效與動態

👉 [查看互動 Demo 與原始碼](https://nlhsueh.github.io/web2026/viewer.html?file=css/demo-dynamics.html)

- **Typography**: `line-height`, `font-family`, `columns`
- **Decoration**: `box-shadow`, `border-radius`, `gradients`
- **Positioning**: `relative`, `absolute`, `fixed`, `sticky`
- **Dynamics**: `transition`, `transform`, `keyframes`

---

## 4.5 隨堂測驗 👋

**Q: 以下哪兩者結合可以實作「滑鼠移入時，按鈕平滑變大」的效果？**

A. `transform` & `transition`
B. `position` & `z-index`
C. `display: block` & `opacity`
D. `margin` & `padding`

---

## 4.5 隨堂測驗 (解答)

**解答：A. `transform` & `transition`**

- `transform: scale(1.1);` 可以達成變大（縮放）的效果。
- 搭配 `transition: transform 0.3s;` 可以讓這個變大的過程有平滑的過渡動畫。

---

## 4.6 實用工具

- **假圖產生器 (Picsum Photos)**
  - `https://picsum.photos/300/200`
- **假文字產生器 (Lorem Ipsum)**
  - VS Code 內建 Emmet: `lorem10`, `p*3>lorem`
  - 中文假文字: `ctlorem` (需外掛)

---

## 4.7 綜合實作：ShowMovie 影城系統

1. **電影牆**: Flexbox + Card Design.
2. **互動強化**: Hover effects + Scale transitions.
3. **座位面板**: Grid Layout + State selectors (`:not(.taken)`).

---

# Q & A

準備好用 CSS 妝點你的網頁了嗎？
