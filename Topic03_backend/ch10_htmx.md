# Ch10 Django + HTMX：提升開發效率與互動性

在現代 Web 開發中，我們常面臨一個抉擇：使用簡單的後端模板 (Server-side Templates) 還是複雜的前端框架 (SPA, 如 React)？**HTMX** 提供了一個完美的「中道」。
*   **極端一：傳統後端模板 (如 Django Template)**
    *   **優勢**：開發速度快，直接透過後端存取資料庫與渲染網頁，無需複雜的前端打包工具與 API 設計。
    *   **痛點**：每次與伺服器互動都必須「整頁重新載入」，互動體驗差，容易有白畫面，不符合現代使用者習慣。
*   **極端二：SPA 前端框架 (如 React, Vue)**
    *   **優勢**：非同步局部更新網頁，提供極佳的互動性與流暢感（類似 App 的體驗）。
    *   **痛點**：開發難度呈指數上升。開發者必須學會 npm、Vite/Webpack、狀態管理、前端路由等；且必須將專案拆成「前端」與「後端」兩套，額外設計大量的 RESTful API，並在前後端重寫兩套重複的資料驗證邏輯。
*   **HTMX 的解決方案（中道）**：
    它保留了**傳統後端模板的開發速度與簡約**（不需要手動寫複雜的 JS，不需要 npm/Vite 包裝工具，繼續在 Django 中撰寫原生的 Templates 與 Form），但同時為網頁注入了 **SPA 的流暢感與非同步局部更新**。這讓開發者能以極低的維護成本，打造出高互動性的現代網頁。


---

## 10.1 什麼是 HTMX？

HTMX 是一個輕量級的 JavaScript 庫，它讓你能夠直接在 HTML 標籤中使用屬性來存取 AJAX、CSS 過渡效能、WebSockets 和伺服器發送事件。
- **核心理念**：讓 HTML 具備「發送非同步請求」的能力，而不是強迫你寫一堆 JS 程式碼。

> [!NOTE]
> **💡 什麼是非同步請求（Asynchronous Request）？**
> * **同步請求 (Synchronous)**：傳統的網頁互動方式。當你點擊一個連結或送出表單，瀏覽器必須將整個網頁重新整理（Reload），等待伺服器回傳完整的 HTML 頁面。在此期間，使用者通常會看到短暫的白畫面，且無法進行其他操作。
> * **非同步請求 (Asynchronous, 常稱為 AJAX)**：瀏覽器在背景發送請求與接收資料，**完全不需要重新整理整個網頁**。當伺服器回傳資料後，只更新網頁中的某個特定區域。這使得網頁操作更為流暢、體驗更佳。

### 10.1.1 基本範例
```html
<!-- 當點擊按鈕時，發送 GET 請求到 /update/，並將回傳的內容放進 #result 中 -->
<button hx-get="/update/" hx-target="#result">
    更新內容
</button>
<div id="result">這裡將被替換</div>
```

#### 🔍 語法解析與傳統做法對比

1. **語法意義**：
   - `hx-get="/update/"`：宣告此按鈕在點擊時，會以非同步（AJAX）方式向伺服器發送 `GET` 請求。
     * 其中的 `/update/` 是後端伺服器的路由路徑（例如 Django 中的 `path('update/', ...)`），負責接收請求並回傳 HTML 片段。
   - `hx-target="#result"`：指定將伺服器回傳的 HTML 片段，放入 ID 為 `result` 的元素中（預設為替換其內部 HTML，即 `innerHTML` 模式）。

2. **HTMX 的底層運作原理（它是怎麼轉譯的？）**：
   * **本質是 JavaScript 程式庫**：網頁載入時，HTMX 的 JavaScript 程式碼會自動掃描整個 DOM，尋找所有帶有 `hx-` 開頭的屬性。
   * **事件監聽與攔截**：以本例來說，HTMX 會自動為該按鈕註冊一個點擊（`click`）事件監聽器，並攔截瀏覽器預設的跳轉行為。
   * **非同步傳輸 (AJAX)**：事件觸發後，HTMX 內部的 JS 會呼叫瀏覽器內建的 `fetch()` 或 `XMLHttpRequest`，在背景向 `/update/` 發送非同步請求。
   * **動態更新 DOM**：當接收到後端回傳的 HTML 內容時，HTMX 的 JS 會執行類似 `element.innerHTML = responseText` 的操作，將新內容無縫塞入 `#result` 中。因此，開發者不需要手動撰寫任何 JavaScript 程式碼，一切皆由 HTMX 核心庫自動完成。

3. **與傳統同步作法的差異**：
   * **傳統同步作法**：
     若要更新網頁中的某個區塊，傳統上必須使用超連結或表單，強制瀏覽器重新載入並渲染整個新頁面。
     * **HTML 範例**：
     ```html
     <!-- 點擊後，網頁會全頁重新整理並載入 /update/ 頁面 -->
     <a href="/update/">更新內容</a>
     ```
   * **傳統 JavaScript (AJAX) 作法**：
     若想在不重新整理網頁的情況下進行局部更新，傳統上開發者必須撰寫複雜的 JS 程式碼來處理。
     * **JavaScript 範例**：
     ```javascript
     // 必須手動監聽事件、發送請求、處理回應，最後再手動變更 DOM 內容
     document.querySelector('button').addEventListener('click', function(e) {
         e.preventDefault();
         fetch('/update/')
             .then(response => response.text())
             .then(html => {
                 document.getElementById('result').innerHTML = html;
             })
             .catch(err => console.error(err));
     });
     ```

> [!TIP]
> **💡 完整頁面範例實作**
> 本範例的 HTML/HTMX 完整示範網頁已放置於 [src/ch10_htmx_demo](src/ch10_htmx_demo) 資料夾中。
> * **完整示範與教學網頁**：[index.html](src/ch10_htmx_demo/index.html) (已將非同步按鈕、運作原理解析與本地 HTTP 伺服器啟動說明整合至單一檔案中)


---

## 10.2 為什麼 Django 適合搭配 HTMX？

Django 的優勢在於強大的伺服器端渲染 (Template System)。HTMX 與之結合後：
1.  **保持簡單**：你不需要管理複雜的前端狀態 (Store/Redux)。
2.  **局部更新**：你可以只回傳一小段 HTML (Template Fragment)，而不是重新載入整個頁面。
3.  **無縫整合**：可以直接使用 Django 的 Forms、Authentication 與 Context。

---

## 10.3 架構比較：Django+HTMX vs. Django+React

這是目前業界與學界最常討論的兩個方向：

| 比較維度 | Django + HTMX (LMPStack) | Django + React (SPA 架構) |
| :--- | :--- | :--- |
| **開發難度** | 低。只需懂 HTML/Django。 | 高。需精通 JS/TS, React, API 設計。 |
| **互動性** | 高 (適合 80% 的商業應用)。 | 極高 (適合地圖、編輯器、高度即時性應用)。 |
| **SEO 友善度** | 極佳 (天然伺服器渲染)。 | 較難 (需額外處理 SSR, 如 Next.js)。 |
| **維護成本** | 低。單一專案、單一邏輯。 | 高。需維護前端與後端兩個獨立專案。 |
| **學習曲線** | 緩慢、平易近人。 | 陡峭、需學習現代前端生態。 |

---

## 10.4 何時該選擇誰？

### 10.4.1 選擇 Django + HTMX (推薦初學者與快速原型)
-   大多數的資料管理系統 (Admin, Dashboard)。
-   內容驅動的網站 (Blog, Forum)。
-   希望快速交付、且不想被繁瑣的前端工具鏈 (npm, webpack) 困擾時。

### 10.4.2 選擇 Django + React (推薦大型複雜項目)
-   需要離線功能或極高度複雜的 UI 互動。
-   同一套 API 需要同時供給網頁、iOS、Android 使用。
-   團隊開發，前端與後端有明確分工時。

---

## 10.5 HTMX 官方精選 10 大常用設計模式 (Showcase)

以下精選了 [HTMX 官方範例庫 (Examples)](https://htmx.org/examples/) 中最常用且實用的 10 個設計模式，並提供中文解說與基本 HTML 結構示範：

### 10.5.1 Click to Edit (點擊編輯)
- **官方說明頁面**：[Click to Edit](https://htmx.org/examples/click-to-edit/)
- **應用場景**：在個人資料或單一物件檢視頁面，點擊「編輯」按鈕後直接在原地替換成輸入表單，修改完成點擊「儲存」後再原地替換回唯讀文字。
- **關鍵機制**：
  - `hx-get="/contact/1/edit"`：點擊編輯按鈕時發送 GET 請求取得編輯表單 HTML 片段。
  - `hx-swap="outerHTML"`：將原本唯讀的 DOM 節點完全替換為表單 HTML。
- **程式碼範例**：
```html
<div id="contact-details">
    <label>姓名: 王小明</label>
    <button hx-get="/contact/1/edit" hx-target="#contact-details" hx-swap="outerHTML">編輯</button>
</div>
```

---

### 10.5.2 Bulk Update (批次更新)
- **官方說明頁面**：[Bulk Update](https://htmx.org/examples/bulk-update/)
- **應用場景**：管理後台常見的批次操作。例如：核取多個使用者後，點擊按鈕一次性將他們設為「啟用」或「停用」狀態。
- **關鍵機制**：
  - `hx-post="/users/status"`：發送 POST 請求批次更新狀態。
  - `hx-include="[name='ids']"`：將外部核取方塊的選取狀態一同包進非同步請求中送出。
- **程式碼範例**：
```html
<form id="user-form">
    <button hx-post="/users/status/activate" hx-target="#user-table-body">批次啟用</button>
    <table>
        <tbody id="user-table-body">
            <tr><td><input type="checkbox" name="ids" value="1"></td><td>使用者 A</td></tr>
            <tr><td><input type="checkbox" name="ids" value="2"></td><td>使用者 B</td></tr>
        </tbody>
    </table>
</form>
```

---

### 10.5.3 Delete Row (刪除資料列)
- **官方說明頁面**：[Delete Row](https://htmx.org/examples/delete-row/)
- **應用場景**：在表格的每行資料最右側提供「刪除」按鈕，點擊後向後端送出 DELETE 請求，並伴隨淡出（Fade-out）的 CSS 動畫將該行 DOM 元素移除。
- **關鍵機制**：
  - `hx-delete="/contact/1"`：發送非同步 DELETE 請求。
  - `hx-target="closest tr"`：將要移除的目標指定為最近的 `<tr>` 標籤。
  - `hx-swap="outerHTML swap:1s"`：延遲 1 秒移除，提供 CSS 轉場動畫足夠的時間。
- **程式碼範例**：
```html
<tr id="row-1">
    <td>王小明</td>
    <td>
        <button hx-delete="/contact/1" hx-target="closest tr" hx-swap="outerHTML swap:1s">刪除</button>
    </td>
</tr>
```

---

### 10.5.4 Lazy Loading (延遲載入)
- **官方說明頁面**：[Lazy Loading](https://htmx.org/examples/lazy-loading/)
- **應用場景**：頁面加載時，先渲染主要架構與一個讀取指示器（Loading Spinner），隨後再非同步請求耗時較長的資料（例如圖表、複雜的統計報表），可大幅縮減首頁載入時間。
- **關鍵機制**：
  - `hx-trigger="load"`：網頁或容器載入完成後自動觸發請求。
  - `hx-get="/charts/stats"`：向後端請求圖表 HTML 片段並替換當前容器。
- **程式碼範例**：
```html
<div hx-get="/charts/stats" hx-trigger="load">
    <img class="htmx-indicator" src="/spinner.gif" alt="載入中...">
</div>
```

---

### 10.5.5 Inline Validation (即時欄位驗證)
- **官方說明頁面**：[Inline Validation](https://htmx.org/examples/inline-validation/)
- **應用場景**：註冊表單中，當使用者輸入完 Email 並將游標移開（Blur）時，立刻檢查該 Email 是否已被註冊，並在該欄位旁顯示紅色的錯誤訊息，無需等到整份表單送出。
- **關鍵機制**：
  - `hx-post="/validate/email"`：將當前欄位的值發送到後端進行即時驗證。
  - `hx-trigger="changed, delay:500ms"`：在內容改變且停止輸入 500 毫秒後觸發，防止使用者一邊敲擊鍵盤一邊送出大量請求。
- **程式碼範例**：
```html
<div>
    <label>電子信箱</label>
    <input type="email" name="email" 
           hx-post="/validate/email" 
           hx-trigger="change, delay:500ms" 
           hx-target="closest div">
</div>
```

---

### 10.5.6 Active Search (即時輸入搜尋)
- **官方說明頁面**：[Active Search](https://htmx.org/examples/active-search/)
- **應用場景**：搜尋輸入框中，使用者每打一個字，搜尋結果清單就即時篩選並呈現更新，免去手動點擊「搜尋」按鈕的步驟。
- **關鍵機制**：
  - `hx-trigger="keyup changed delay:500ms"`：按鍵放開且內容有變動，並在停止輸入 500 毫秒後觸發。
  - `hx-indicator="#search-indicator"`：載入中顯示指示器，提升使用者體驗。
- **程式碼範例**：
```html
<input type="search" name="search" placeholder="輸入關鍵字..."
       hx-post="/search" 
       hx-trigger="keyup changed delay:500ms" 
       hx-target="#search-results" 
       hx-indicator="#search-indicator">
<span id="search-indicator" class="htmx-indicator" style="display:none;">搜尋中...</span>
<div id="search-results">這裡將顯示搜尋結果</div>
```

---

### 10.5.7 Infinite Scroll (無限滾動載入)
- **官方說明頁面**：[Infinite Scroll](https://htmx.org/examples/infinite-scroll/)
- **應用場景**：社群媒體動態牆或商品清單，當使用者向下滑動到底部時，自動載入下一頁的資料並附加在清單尾端。
- **關鍵機制**：
  - `hx-trigger="revealed"`：當該元素出現在瀏覽器可視區域（Viewport）中時觸發。
  - `hx-swap="afterend"`：將回傳的下一頁內容插入到當前元素的後面。
- **程式碼範例**：
```html
<!-- 列表的最後一項 -->
<tr hx-get="/items?page=2" hx-trigger="revealed" hx-swap="afterend">
    <td>商品最後一筆 (滾動到此自動加載下一頁)</td>
</tr>
```

---

### 10.5.8 Value Select / Cascading Select (聯動式下拉選單)
- **官方說明頁面**：[Value Select](https://htmx.org/examples/value-select/)
- **應用場景**：選擇「國家」後，第二個下拉選單的「城市」清單會自動過濾並更新為該國家的城市列表。
- **關鍵機制**：
  - `hx-get="/cities"`：選擇國家後，發送 GET 請求取得對應城市的 HTML `<option>` 標籤。
  - `hx-target="#city-select"`：將回傳的城市 HTML 選項注入到城市下拉選單中。
- **程式碼範例**：
```html
<select name="country" hx-get="/cities" hx-target="#city-select">
    <option value="tw">台灣</option>
    <option value="us">美國</option>
</select>
<select id="city-select" name="city">
    <option>請先選擇國家</option>
</select>
```

---

### 10.5.9 Progress Bar (工作進度條)
- **官方說明頁面**：[Progress Bar](https://htmx.org/examples/progress-bar/)
- **應用場景**：觸發耗時長的工作（如匯出大型 Excel、發送大量電子郵件），系統會在後台處理，並在前端以進度條每秒輪詢（Polling）最新的處理進度。
- **關鍵機制**：
  - `hx-trigger="every 1s"`：每隔 1 秒自動發送一次請求，向後端查詢最新進度。
  - `hx-get="/job/status"`：查詢進度 API。
- **程式碼範例**：
```html
<div id="job-status" hx-get="/job/status" hx-trigger="every 1s">
    <h3>正在處理中...</h3>
    <div class="progress">
        <div class="progress-bar" style="width: 35%">35%</div>
    </div>
</div>
```

---

### 10.5.10 File Upload with Progress (檔案上傳與進度條)
- **官方說明頁面**：[File Upload](https://htmx.org/examples/file-upload/)
- **應用場景**：上傳大檔案時，使用 AJAX 送出，且無須第三方 JavaScript 庫，就能透過 HTMX 內建的監聽機制，在畫面上實時展示檔案上傳的百分比進度。
- **關鍵機制**：
  - `hx-encoding="multipart/form-data"`：指示該請求使用多部分表單編碼以傳輸檔案。
  - `htmx:xhr:progress` 事件：HTMX 觸發的事件，可搭配簡單的 JS 監聽器來更新進度條長度。
- **程式碼範例**：
```html
<form hx-encoding="multipart/form-data" hx-post="/upload"
      hx-on="htmx:xhr:progress(event) -> document.getElementById('upload-progress').setAttribute('value', event.detail.loaded/event.detail.total * 100)">
    <input type="file" name="file">
    <button>開始上傳</button>
    <progress id="upload-progress" value="0" max="100"></progress>
</form>
```

## 10.6 實作案例：網球俱樂部

* [readme.md 解說](https://github.com/nlhsueh/nlh_tennis_club/blob/htmx/readme.md)

Deploy in Render.com: [網球俱樂部網站](https://nlh-tennis-club.onrender.com/)