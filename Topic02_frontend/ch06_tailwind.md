# Tailwind CSS：實用優先的現代網頁設計

在傳統的 Web 開發中，我們習慣撰寫獨立的 CSS 檔案。然而，現代開發趨向於使用 **Tailwind CSS**，一種「實用優先 (Utility-first)」的 CSS 框架。

本章將帶領你透過建立一個「旅遊網站」，手把手掌握 Tailwind CSS 的核心觀念。

---

## 1. 基礎觀念：顏色、文字與間距

Tailwind 的核心是將 CSS 屬性映射到簡短的 Class 名稱。這不僅減少了命名困難，更建立了一套和諧的設計系統。

### 核心觀念
-   **顏色系統 (Color Palette)**：
    - 格式：`{property}-{color}-{level}`。例如 `bg-blue-500`。
    - 色階從 `50` (最淺) 到 `950` (最深)。通常 `500` 是主要色，`600` 以上適合文字，`50` 適合背景。
    - **任意值支援**：如果預設顏色不夠，可用 `bg-[#1da1f2]` 這種語法直接套用色碼。
-   **字體與排版 (Typography)**：
    - 大小：`text-xs` (12px) 到 `text-9xl` (128px)。
    - 粗細：`font-light`, `font-normal`, `font-bold`, `font-black`。
    - 行高與間距：`leading-tight` (行高), `tracking-wider` (字距)。
-   **間距系統 (Spacing)**：
    - `p-` (Padding), `m-` (Margin)。
    - 數字單位：`1` 代表 `0.25rem` (4px)。所以 `p-4` = 16px。
    - 定向間距：`pt-` (top), `px-` (水平), `py-` (垂直)。

### 📋 實測與範例
請查看範例檔：[demo_basics.html](./src/tailwind/demo_basics.html)

![demo_basics](./src/tailwind/demo_basics.png)

#### 📝 代碼片段講解
```html
<section class="bg-blue-600 text-white p-12 text-center">
    <h1 class="text-4xl font-extrabold mb-4 tracking-tight">探索未知的世界</h1>
    <p class="text-blue-100 mb-8 max-w-md mx-auto">
        準備好開啟一段奇妙的旅程了嗎？我們為你精選了全球最值得造訪的秘境。
    </p>
    <a href="#" class="bg-white text-blue-600 px-8 py-3 rounded-full font-bold hover:bg-blue-50 transition-all shadow-lg active:scale-95">
        立即開始
    </a>
</section>
```
- `font-extrabold` 比 `font-bold` 更具視覺衝擊力，適合 Hero Section 的大標題。
- `text-blue-100` 利用色階讓副標題與主標題產生層次感，而不是單調的純白。
- `max-w-md mx-auto` 限制文字寬度並置中，是處理長段落排版的必備技巧。

### 💡 觀念測驗
1. 如何使用 Tailwind 指定一個精密的背景顏色 `#ff5733`？
<details>
<summary>點擊查看答案</summary>
使用任意值語法：`bg-[#ff5733]`。
</details>

2. `px-4 py-2` 代表的實際像素是多少 (假設預設 16px)？
<details>
<summary>點擊查看答案</summary>
`px-4` = 16px 水平內距，`py-2` = 8px 垂直內距。
</details>

---

## 2. 佈局與排版：Flexbox 與 Grid

Tailwind 讓佈局變得極其直覺，通常透過最外層容器的 Class 就能決定內部的排列方式。

### 核心觀念
-   **Flexbox (一維排版)**：
    - `flex`: 啟動 Flex 模式。
    - `items-center`: 垂直居中；`justify-between`: 兩端對齊。
    - `flex-grow`: 讓特定元件佔滿剩餘空間。
-   **Grid (二維排版)**：
    - `grid`: 啟動 Grid 模式。
    - `grid-cols-{n}`: 定義欄數 (1~12)。
    - `gap-{n}`: 子元素間距。
    - `col-span-{n}`: 讓單一子元素跨越多欄。
-   **容器與居中**：
    - `container mx-auto`: 建立一個限寬且水平居中的區塊，這在寬螢幕顯示上非常重要。

### 📋 實測與範例
請查看範例檔：[demo_layout.html](src/tailwind/demo_layout.html)

![demo_layout](src/tailwind/demo_layout.png)

#### 📝 代碼片段講解
```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-8 container mx-auto px-4">
    <div class="bg-white p-6 border rounded-xl shadow-sm">
        <h3 class="font-bold underline">日本 東京</h3>
        <p class="text-gray-500 text-sm">現代與傳統的完美融合</p>
    </div>
    <div class="bg-white p-6 border rounded-xl shadow-sm md:col-span-2">
        <h3 class="font-bold underline">精選活動</h3>
        <p class="text-gray-500 text-sm">由於此區塊用了 md:col-span-2，它在中型螢幕會佔據兩倍寬度。</p>
    </div>
</div>
```
- `grid-cols-1`: 手機端預設為單欄，避免內容太擠。
- `md:grid-cols-3`: 桌機端自動轉為三欄。
- `col-span-2`: 透過跨欄設定，可以創造出「主從關係」的佈局視覺。

### 💡 觀念測驗
1. `items-center` 和 `justify-center` 在 Flex 容器中的差別？
<details>
<summary>點擊查看答案</summary>
`items-center` 是垂直軸居中，`justify-center` 是水平主軸居中。
</details>

2. 想在 Grid 中設定各元素間距為 20px，應該用哪個 Class？
<details>
<summary>點擊查看答案</summary>
`gap-5` (5 * 4px = 20px)。
</details>

---

## 3. 視覺精修：邊框、圓角與陰影

細節決定質感。Tailwind 提供的視覺修飾工具可以讓你輕鬆做出「現代感」介面。

### 核心觀念
-   **圓角 (Rounded)**：`rounded-...` 從 `sm` 到 `3xl` 和 `full`。建議卡片使用 `rounded-xl` 以上。
-   **陰影 (Shadow)**：`shadow-...` 營造深度感。`shadow-xl` 適合浮動卡片。
-   **光環與邊框 (Ring & Border)**：
    - `border-2`: 粗細。
    - `ring-2 ring-blue-500/50`: 建立一個帶有透明度的外圈，這在製作選中狀態時非常美觀。
-   **圖片比例 (Aspect Ratio)**：`aspect-video`, `aspect-square`。

### 📋 實測與範例
請查看範例檔：[demo_effects.html](src/tailwind/demo_effects.html)

![demo_effects](src/tailwind/demo_effects.png)

#### 📝 代碼片段講解
```html
<div class="bg-white rounded-3xl overflow-hidden shadow-2xl ring-1 ring-black/5 hover:ring-blue-500/50 transition-all duration-500">
    <div class="aspect-video bg-slate-200">
        <img src="tour.jpg" class="w-full h-full object-cover">
    </div>
    <div class="p-8">
        <span class="inline-block bg-green-100 text-green-700 font-bold px-3 py-1 rounded text-xs mb-3">特價中</span>
        <h4 class="text-xl font-bold">地中海巡航</h4>
    </div>
</div>
```
- `rounded-3xl` + `overflow-hidden`: 確保內部圖片不會超出卡片的超大圓角。
- `shadow-2xl`: 營造強烈的立體感。
- `ring-black/5`: 這是現在非常流行的 UI 技巧，使用極淡的黑色 Ring 取代實體邊框，看起來更輕盈。
- `object-cover`: 確保圖片在固定比例的容器中不會變形。

### 💡 觀念測驗
1. 如何讓圖片永遠保持 16:9 比例？
<details>
<summary>點擊查看答案</summary>
使用 `aspect-video`。
</details>

2. 如何在滑鼠移入時讓陰影變大？
<details>
<summary>點擊查看答案</summary>
使用 `hover:shadow-2xl` 並建議加上 `transition-shadow`。
</details>

---

## 4. 響應式設計 (Responsive Design)

現代網頁必須在手機、平板與桌面都有良好表現。Tailwind 採用 **Mobile First** (手機優先) 策略，這意味著不帶斷點前綴的 Class 會套用在所有螢幕，而 `md:` 等前綴則是「覆蓋」預設值。

### 核心觀念
-   **斷點標準 (Breakpoints)**：
    | 前綴 | 最小寬度 | 對應裝置 |
    | :--- | :--- | :--- |
    | `(無)` | 0px | 手機 (預設) |
    | `sm:` | 640px | 大手機 / 平板直向 |
    | `md:` | 768px | 平板橫向 |
    | `lg:` | 1024px | 筆電 / 電腦 |
    | `xl:` | 1280px | 大型螢幕 |

-   **常見模式**：
    - `w-full md:w-1/2`: 手機滿版，桌面端一半。
    - `hidden md:block`: 在行動端隱藏次要元件（如側邊欄），桌面端顯示。

### 📋 實測與範例
1. **元素隱藏 (Hiding)**：練習在小螢幕時隱藏次要資訊。
   👉 [demo_responsive.html](src/tailwind/demo_responsive.html)
2. **元件堆疊 (Stacking)**：練習在小螢幕時讓元件自動往下擠。
   👉 [demo_stacking.html](src/tailwind/demo_stacking.html)

![demo_stacking](src/tailwind/demo_stacking.png)

#### 📝 代碼片段講解 (響應式文字與佈局)
```html
<div class="p-4 md:p-10 flex flex-col md:flex-row items-center">
    <div class="w-full md:w-1/3 mb-4 md:mb-0">
        <img src="hero.jpg" class="rounded-lg">
    </div>
    <div class="w-full md:w-2/3 md:pl-8">
        <h2 class="text-xl md:text-3xl font-black">響應式標題</h2>
        <p class="text-sm md:text-base mt-2 text-gray-600">文字大小隨螢幕調整</p>
    </div>
</div>
```
- `flex-col md:flex-row`: 在手機端垂直堆疊，在平板以上水平排列。這是一切響應式佈局的起點。
- `mb-4 md:mb-0`: 手機端需要下邊距來隔開垂直堆疊的內容，但轉為水平排列後應取消邊距。

### 📋 實測與範例
1. **元素隱藏 (Hiding)**：練習在小螢幕時隱藏次要資訊。
   👉 [demo_responsive.html](src/tailwind/demo_responsive.html)
2. **元件堆疊 (Stacking)**：練習在小螢幕時讓元件自動往下擠。
   👉 [demo_stacking.html](src/tailwind/demo_stacking.html)

![demo_stacking](src/tailwind/demo_stacking.png)

#### 📝 代碼片段講解 (堆疊邏輯)
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- 當橫向空間不足時，元件會自動換行 -->
    <div>卡片 1</div>
    <div>卡片 2</div>
    <div>卡片 3</div>
</div>
```
- `grid-cols-1`: 手機端預設為單欄（自動堆疊）。
- `md:grid-cols-2`: 中型螢幕顯示兩欄。
- `lg:grid-cols-3`: 大型螢幕顯示三欄。

---

## 5. 互動與狀態 (States & Transitions)

Tailwind 讓動態效果變得像靜態排版一樣簡單，透過「修飾符」來定義不同狀態下的樣子。

### 核心觀念
-   **常用修飾符**：
    - `hover:`: 滑鼠懸停。
    - `focus:`: 輸入框選中。
    - `active:`: 正在點擊。
    - `group-hover:`: 讓父元素懸停時，子元素跟著變色（這對導覽列或卡片非常實用）。
-   **動畫過渡 (Transitions)**：
    - `transition-all`: 啟動過渡效果。
    - `duration-300`: 設定毫秒數。
    - `ease-in-out`: 設定運動曲線。

### 📋 實測與範例
請查看範例檔：[demo_states.html](src/tailwind/demo_states.html)

![demo_states](src/tailwind/demo_states.png)

#### 📝 代碼片段講解
```html
<div class="group bg-white p-6 rounded-xl hover:bg-slate-900 transition-colors duration-500">
    <h3 class="text-black group-hover:text-white transition-colors">卡片標題</h3>
    <p class="text-gray-500 group-hover:text-gray-300">懸停父元素，內容會跟著變色</p>
</div>
```
- `group`: 將容器標記為一組。
- `group-hover:text-white`: 當父容器被 hover 時，標題會變白。這是製作互動卡片的標準做法。

---

## 6. 案例探討：解決真實的問題

在掌握了基礎與響應式邏輯後，我們透過兩個真實場景來看看 Tailwind 如何處理複雜的 UI。

### 🎬 案例一：電影訂票系統 (Movie Booking)
這是一個黑暗風格的 UI，展示了 Grid 在處理「座椅矩陣」上的強大能力，以及桌面端「側邊欄固定」的響應式設計。

- **核心技術**：Grid 佈局、Glassmorphism (玻璃擬態)、Sticky 側邊欄。
- **原始碼**：👉 [demo_movie.html](src/tailwind/demo_movie.html)

![demo_movie](src/tailwind/demo_movie.png)

> **重點說明**：
> - 使用 `grid-cols-8` 輕鬆對齊 40+ 個座椅，並用 `hover:bg-blue-500` 處理選中互動。
> - `lg:sticky lg:top-8` 讓訂票按鈕在右側滾動時保持可見。

### 🍕 案例二：外送點餐設計 (Food Delivery)
模擬一個外送平台的主頁面，重點在於處理多層次的資訊架構：分類、廣告輪播與餐廳列表。

- **核心技術**：Flex-wrap、多斷點 Grid、漸層疊加圖片。
- **原始碼**：👉 [demo_delivery.html](src/tailwind/demo_delivery.html)

![demo_delivery](src/tailwind/demo_delivery.png)

> **重點說明**：
> - `bg-gradient-to-br from-orange-400 to-orange-600` 用簡單的一行 Class 做出高質感的廣告 Banner。
> - `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` 讓餐廳卡片隨螢幕寬度自動從 1 欄轉為 3 欄。

---

## 🛠️ 綜合練習：打造你的旅遊首頁

請在練習中組合以上觀念，實作以下功能：
1. 一個帶有背景色的 **Navigation Bar**。
2. 一個具有陰影與圓角的 **目的地卡片 (Destination Card)**。
3. 卡片在滑鼠懸停 (hover) 時，陰影要加深。
4. 在手機上顯示 1 欄卡片，桌機上顯示 3 欄。

> [!TIP]
> **💡 重點觀念**：Tailwind 的強大在於你「不需要離開 HTML」就能完成設計。這在進行 Django 或 HTMX 開發時，能極大地提升效率。
