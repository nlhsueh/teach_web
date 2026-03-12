# Tailwind CSS：實用優先的現代網頁設計

在傳統的 Web 開發中，我們習慣撰寫獨立的 CSS 檔案。然而，現代開發趨向於使用 **Tailwind CSS**，一種「實用優先 (Utility-first)」的 CSS 框架。

本章將帶領你透過建立一個「旅遊網站」，手把手掌握 Tailwind CSS 的核心觀念。

---

## 1. 基礎觀念：顏色、文字與間距

Tailwind 的核心是將 CSS 屬性映射到簡短的 Class 名稱。

### 核心觀念
-   **顏色 (Colors)**：`bg-{color}-{level}` (背景), `text-{color}-{level}` (文字)。
-   **字體 (Typography)**：`text-{size}` (大小), `font-{weight}` (粗細)。
-   **間距 (Spacing)**：`p-{size}` (Padding), `m-{size}` (Margin)。

### 📋 實測與範例
請查看範例檔：[demo_basics.html](./src/tailwind/demo_basics.html)

### 💡 觀念測驗
1. 如何設定文字為紅色且加粗？
<details>
<summary>點擊查看答案</summary>
使用 `text-red-500 font-bold` (level 可調整)。
</details>

2. `p-4` 和 `m-4` 的差別是什麼？
<details>
<summary>點擊查看答案</summary>
`p-4` 是內距 (Padding)，`m-4` 是外距 (Margin)。
</details>

---

## 2. 佈局與排版：Flexbox 與 Grid

旅遊網站需要展示「熱門目的地」，這時佈局 Class 就派上用場了。

### 核心觀念
-   **Flexbox**：`flex`, `flex-row`, `items-center`, `justify-between`。
-   **Grid**：`grid`, `grid-cols-{n}`, `gap-{n}`。
-   **容器置中**：`container mx-auto`。

### 📋 實測與範例
請查看範例檔：[demo_layout.html](src/tailwind/demo_layout.html)

### 💡 觀念測驗
1. `grid-cols-3` 的作用是什麼？
<details>
<summary>點擊查看答案</summary>
將網格佈局設定為三等份的欄位。
</details>

2. 如何讓一個元素在父容器中水平居中？
<details>
<summary>點擊查看答案</summary>
使用 `mx-auto` (通常需要配合 `block` 或寬度設定)。
</details>

---

## 3. 視覺精修：邊框、圓角與陰影

要讓你的旅遊卡片看起來「很高級」，需要加入深度的視覺效果。

### 核心觀念
-   **圓角 (Border Radius)**：`rounded`, `rounded-lg`, `rounded-full`。
-   **陰影 (Box Shadow)**：`shadow-sm`, `shadow-md`, `shadow-xl`。
-   **邊框 (Borders)**：`border`, `border-2`, `border-gray-200`。

### 📋 實測與範例
請查看範例檔：[demo_effects.html](src/tailwind/demo_effects.html)

### 💡 觀念測驗
1. 想製作一個圓形的按鈕，應該用哪個 Class？
<details>
<summary>點擊查看答案</summary>
`rounded-full`。
</details>

---

## 4. 響應式設計 (Responsive Design)

現代網頁必須在手機、平板與桌面都有良好表現。Tailwind 採用 **Mobile First** (手機優先) 策略。

### 核心觀念
-   **斷點 (Breakpoints)**：
    -   `sm:` (640px)
    -   `md:` (768px)
    -   `lg:` (1024px)
-   **範例**：`w-full md:w-1/2` (手機滿版，平板一半)。

### 📋 實測與範例
請查看範例檔：[demo_responsive.html](src/tailwind/demo_responsive.html)

---

## 5. 互動與狀態 (States & Transitions)

讓按鈕點起來有反應，表單選取時發光。

### 核心觀念
-   **互動修飾符**：`hover:`, `focus:`, `active:`。
-   **動畫過渡**：`transition`, `duration-300`。

### 📋 實測與範例
請查看範例檔：[demo_states.html](src/tailwind/demo_states.html)

---

## 🛠️ 綜合練習：打造你的旅遊首頁

請在練習中組合以上觀念，實作以下功能：
1. 一個帶有背景色的 **Navigation Bar**。
2. 一個具有陰影與圓角的 **目的地卡片 (Destination Card)**。
3. 卡片在滑鼠懸停 (hover) 時，陰影要加深。
4. 在手機上顯示 1 欄卡片，桌機上顯示 3 欄。

> [!TIP]
> **💡 重點觀念**：Tailwind 的強大在於你「不需要離開 HTML」就能完成設計。這在進行 Django 或 HTMX 開發時，能極大地提升效率。
