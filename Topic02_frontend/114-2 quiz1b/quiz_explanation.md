# 114-2 Web Programming Quiz Explanation / 114-2 網頁程式設計小考解析

本文件說明 114-2 期中小考兩大實作題的核心觀念與實作要點。
This document explains the core concepts and implementation details of the two major practical questions in the 114-2 midterm quiz.

---

## Q1: Flexbox Travel Cards / Flexbox 旅遊卡片

### 題目目標 (Goal)
練習使用 CSS Flexbox 進行佈局，將卡片水平排列並保持等寬與間距。
Practice using CSS Flexbox for layout to arrange cards horizontally with equal width and consistent spacing.

### 關鍵技術點 (Key Concepts)

1.  **啟用 Flex 佈局 (Enable Flexbox)**
    - 在外層容器 `.card-container` 使用 `display: flex;`。
    - 使用 `gap: 24px;` 設定卡片之間的固定間距，這比傳統使用 `margin` 更簡潔。

2.  **平均分配寬度 (Equal Width Distribution)**
    - 在子元素 `.card` 使用 `flex: 1;`。
    - 當所有子元素都設為 `flex: 1` 時，它們會自動填滿剩餘空間並保持相同的寬度。

3.  **互動效果 (Hover Effects)**
    - 使用 `:hover` 虛擬類別（Pseudo-class）。
    - 透過修改 `box-shadow` 讓卡片在滑鼠懸停時感覺「浮起來」，提升使用者體驗（UX）。

```css
/* 核心實作代碼片段 */
.card-container {
  display: flex;
  gap: 24px;
}

.card {
  flex: 1;
}

.card:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
}
```

---

## Q2: Fruit Shopping Cart / 水果鮮選購物車

### 題目目標 (Goal)
結合 Tailwind CSS 進行 UI 設計，並使用 JavaScript 處理動態資料計算與 DOM 操作。
Combine Tailwind CSS for UI design and use JavaScript for dynamic data calculation and DOM manipulation.

### 關鍵技術點 (Key Concepts)

#### 1. Tailwind CSS 介面設計 (UI Design)
- **佈局與間距**：使用 `flex`, `items-center`, `justify-center` 處理置中；`p-4`, `m-8` 處理內外距。
- **視覺美感**：`rounded-3xl` (圓角), `shadow-2xl` (深陰影), `bg-blue-50` (柔和背景色)。
- **微互動**：`transition-all`, `active:scale-95` 讓按鈕按下時有縮小效果，增加回饋感。

#### 2. JavaScript 資料處理 (Data Logic)
- **物件映射 (Object Mapping)**：
  使用 `fruitPrices` 物件來儲存水果名稱與價格的對應關係。
  ```javascript
  const fruitPrices = { "蘋果": 50, "香蕉": 20, "櫻桃": 80 };
  ```
- **輸入驗證 (Input Validation)**：
  在處理資料前先檢查 `qty`（數量）是否在 1-10 之間，確保程式強健性。

#### 3. 動態 DOM 操作 (Dynamic DOM)
- **讀取數值**：透過 `document.getElementById('...').value` 獲取使用者選取的水果與數量。
- **新增清單項**：
  1. `document.createElement('li')`：建立新元素。
  2. `li.innerHTML = ...`：使用模板字串（Template Literals）動態填入內容。
  3. `list.appendChild(li)`：將新項目掛載到現有的 HTML 清單中。
- **自動捲動**：`list.scrollTop = list.scrollHeight` 確保使用者新增項目後能立刻看到結果。

### 常見錯誤提醒 (Common Mistakes)
- **忘記將字串轉數字**：`input.value` 取得的是字串，計算前應使用 `parseInt()`。
- **全域與區域變數混淆**：累計總金額 `currentTotal` 必須宣告在函式外，否則每次點擊都會重置。

---
