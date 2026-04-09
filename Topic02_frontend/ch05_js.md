# Ch05 JavaScript：為網頁注入靈魂

在本章中，我們將學習 JavaScript 的基礎語法，並一步步將這些生硬的程式碼，應用到上一章完成的「探索世界」旅遊網站中，讓靜態版型轉變為具備互動性的應用程式。

> **「HTML 給了網頁骨架，CSS 賦予了美麗的外觀，而 JavaScript 則是網頁的肌肉與神經，讓它能對使用者的操作做出反應。」**

[nlh slides- javascript](https://docs.google.com/presentation/d/1JMaa9aSBGomS85OtSDdcQZlwuajNgdmKFtrb3WR-nSI/edit?usp=sharing)


---

## 5.1 JavaScript 基礎引導

📚 [W3Schools 參考：JS Introduction & Output](https://www.w3schools.com/js/js_intro.asp)

在學習用 JS 做出酷炫的購物車前，我們先來看看 JS 到底怎麼寫、它能改變什麼。

### 5.1.1 認識與安裝 Node.js
在正式開始寫 JavaScript 之前，我們需要先認識一個重要的開發工具：**Node.js**。

雖然瀏覽器（如 Chrome, Edge）本身就可以執行 JavaScript，但在現代的網頁開發流程中，我們通常會在電腦上安裝 [Node.js](https://nodejs.org/)。它是一個能夠讓 JavaScript 在**瀏覽器之外**（也就是你的作業系統上）獨立運作的執行環境。

安裝 Node.js 後，我們不僅可以方便地在終端機測試短篇的 JS 程式碼，更重要的是它包含了 **npm (Node Package Manager)**。它是由全世界開發者貢獻的套件庫，讓我們能輕鬆下載各種強大的擴充工具。

**🛠️ 安裝步驟：**
1. 前往 [Node.js 官方網站](https://nodejs.org/)。
2. 點擊下載 **LTS (Long Term Support, 長期維護版)** 版本（最穩定，推薦初學者使用）。
3. 執行下載的安裝程式，並依循預設選項，一路點擊「下一步 / Next」完成安裝。
4. 安裝完成後，在 VS Code 中打開你的終端機 (Terminal)，輸入以下指令測試：
   ```bash
   node -v
   ```
   如果終端機能夠回傳版本號（例如 `v20.12.0`），代表 Node.js 已經成功安裝到你的電腦囉！

### 5.1.2 基礎概念：引入與輸出
JavaScript 可以直接寫在 HTML 的 `<script>` 標籤中：

```html
<script>
    // 1. 彈出對話框
    alert("Hello World!");

    // 2. 開發者除錯用 (按 F12 打開 Console 標籤才看的到)
    console.log("這是一行隱藏的訊息");
</script>
```

除了單純印文字，JS 最強大的地方在於它可以控制 HTML。例如：
* `document.getElementById('title').innerHTML = "新標題"`：將 ID 為 `title` 的標籤內容換掉。

### 5.1.3 基礎概念：JS 載入位置與執行順序

在網頁中，我們有幾種常見的方式來引入 JavaScript，最推薦的是**外部引入 (External)**：
將 JS 寫在獨立的 `.js` 檔案中，透過 `<script src="app.js"></script>` 將其連結到 HTML。這可以讓 HTML (骨架) 與 JS (肌肉) 乾淨分離，方便日後維護。

**💡 放在 HTML 的哪裡？執行順序的經典陷阱**

瀏覽器在讀取 HTML 時，是**由上往下 (Top-Down)** 依序解析的。當瀏覽器遇到 `<script>` 標籤時，會暫停讀取 HTML，先去執行 JS 程式碼，執行完才繼續往下畫出剩餘的畫面。

這個特性常常導致初學者遇到一個經典錯誤：**「JS 執行了，但找不到 HTML 元素」**。

❌ **錯誤的載入案例 (放在 `<head>` 裡)：**
如果把操作畫面的 JS 寫在 `<head>`：
```html
<head>
    <script>
        // ❌ 報錯：TypeError: Cannot read properties of null (reading 'innerHTML')
        // 因為程式執行到這行時，瀏覽器還沒讀到 <body> 裡的 <h1>，所以找不到 ID 為 title 的元素！
        document.getElementById('title').innerHTML = "新標題"; 
    </script>
</head>
<body>
    <h1 id="title">舊標題</h1>
</body>
```

✅ **正確的載入位置 (放在 `<body>` 底部)：**
最保險且傳統的做法，是將 `<script>` 放在 `</body>` 標籤的上一行。確保瀏覽器已經把所有的 HTML 畫完，JS 才能順利找到元素去操作。
```html
<body>
    <h1 id="title">舊標題</h1>
    
    <!-- ✅ 放在 body 底部：此時 <h1> 已經存在畫面上了，JS 順利抓取並修改成功 -->
    <script>
        document.getElementById('title').innerHTML = "新標題"; 
    </script>
</body>
```

*(補充：現代開發中，常見的做法是將 `<script>` 寫在 `<head>`，並加上 `defer` 屬性，例如 `<script src="app.js" defer></script>`。這會告訴瀏覽器「在背景先下載 JS，但等 HTML 全部畫完再來執行」，這也是官方最推薦的新式做法。)*

### 5.1.4 實戰應用：BMI 計算機 (表單取值與按鈕事件)

在網頁中最常見的互動之一，就是使用者在表單輸入資料後，按下按鈕讓程式進行運算並顯示結果。我們以「BMI 計算機」為例，來了解 JavaScript 如何取得輸入框的值，以及如何透過 `onclick` 事件觸發計算。

**💡 核心觀念：**
1. **取得輸入值 (`.value`)**：使用 `document.getElementById('id').value` 可以拿到使用者在 `<input>` 內輸入的內容。
2. **設定輸出值 (`.value`)**：同樣地，若想把計算結果放回畫面上的 `<input>`，也是直接將值賦予給它的 `.value`。
3. **按鈕事件 (`onclick`)**：在 HTML 的 `<button>` 加上 `onclick="函式名稱()"`，就能告訴瀏覽器「按鈕被點擊時，請去執行指定的 JS 程式碼區塊」。

**📝 BMI 實作範例：**
```html
<!-- HTML 表單區域 -->
<div>
    <label>身高 (公分):</label>
    <input type="number" id="heightInput" placeholder="例如: 175">
    <br><br>
    
    <label>體重 (公斤):</label>
    <input type="number" id="weightInput" placeholder="例如: 70">
    <br><br>
    
    <!-- 點擊按鈕時，觸發名為 calculateBMI 的 JS 程式區塊 (函式) -->
    <button onclick="calculateBMI()">計算 BMI</button>
    <br><br>
    
    <label>你的 BMI:</label>
    <!-- 使用 readonly 讓此輸入框只能觀看，無法手動打字 -->
    <input type="text" id="resultInput" readonly>
</div>

<!-- JS 邏輯區域 -->
<script>
    // 將程式「打包」成一個名叫 calculateBMI 的區塊，等待按鈕點擊才執行
    function calculateBMI() {
        // 1. 抓取身高與體重的數值 (取得 .value)
        let h = document.getElementById('heightInput').value;
        let w = document.getElementById('weightInput').value;
        
        // 2. 進行數學計算 (身高先轉為公尺)
        let heightInMeters = h / 100;
        let bmi = w / (heightInMeters * heightInMeters);
        
        // 3. 將算出來的結果塞回結果輸入框中 (設定 .value)
        // toFixed(2) 可以讓數字自動四捨五入到小數點後兩位
        document.getElementById('resultInput').value = bmi.toFixed(2);
    }
</script>
```

> **⚠️ 經典陷阱提醒**：
> 絕對不要在一開網頁時，就直接在最外層抓取 `<input>.value` 進行運算！因為網頁剛載入時，使用者根本還沒輸入任何字，你只會抓到空值。**我們必須把「抓取數值」與「計算」的動作，確實包裝在「按鈕被點擊時才觸發」的函式區塊裡。**

### 5.1.5 實戰應用：旅遊網站歡迎訊息
當我們把這個概念套用到旅遊網站上，就可以在訪客進站時跳出歡迎訊息，或是點擊按鈕時替換首頁的促銷標題。

👉 **[Demo 5.1: 旅遊網歡迎訊息](src/js/demo_basics.html)**

#### 💡 5.1 隨堂測驗

1️⃣ 在開發網頁時，若想在不干擾使用者介年的情況下查看變數內容或進行除錯，最推薦使用哪種方法？

🇦 `alert()`🇧 `prompt()`🇨 `console.log()`🇩 `document.write()`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`console.log()` 會將訊息輸出至瀏覽器開發者工具（Console）中，不會彈出視窗干擾使用者流程，是現代網頁開發最核心的除錯工具。
</details>

2️⃣ 關於引入 JavaScript 的位置與方式，下列敘述何者正確？

🇦 將 JS 寫在 `<head>` 中且不加任何屬性，能確保抓到所有 body 元素  🇧 為了方便管理，應該將所有 JS 硬編碼（Hard-code）在 HTML 標籤內  🇨 外部引入（External）如 `<script src="app.js"></script>` 能讓結構與邏輯分離，利於維護  🇩 瀏覽器讀取 HTML 時是由下往上的，所以腳本應該放最上面

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：外部引入是開發大型網站的標準做法，能讓 HTML 專注於結構，JS 專注於邏輯。若 JS 放在 `<head>` 且未加 `defer`，常會發生找不到 HTML 元素的錯誤。
</details>

3️⃣ 現代開發中，若要將 `<script>` 放在 `<head>` 卻又希望它在 HTML 解析完後才執行，應加上哪個屬性？

🇦 `async`  🇧 `defer`  🇨 `wait`  🇩 `hold`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：`defer` 屬性會告訴瀏覽器在背景下載腳本，並等到整個 HTML 文件解析完成後才執行。
</details>
    
4️⃣ 安裝 Node.js 後，主要能為網頁開發者帶來什麼便利？

🇦 讓網頁可以在沒有網路的情況下運行  🇧 提供 npm 套件管理工具，輕鬆下載各種開發工具與套件  🇨 自動幫你把 HTML 轉換為 CSS  🇩 強制瀏覽器使用更快的渲染引擎

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：Node.js 讓我們能在本機環境執行 JS，其附帶的 npm 是全球最大的程式碼套件庫。
</details>

#### 📝 5.1 實作練習：Lab 5.1 歡迎訊息
**目標：** 熟悉基本的輸出與 DOM 內容替換。
1. 建立一個按鈕，點擊後會顯示 `alert` 訊息「查看今日特惠行程！」。
2. 使用 `innerHTML` 將網頁上一個 `<h2 id="promo">` 標籤的文字改為「限量：日本賞櫻 8 折起」。
3. 在 Console 中印出你的名字並附帶測試訊息。

---

## 5.2 變數、常數與運算元

📚 [W3Schools 參考：JS Variables](https://www.w3schools.com/js/js_variables.asp) | [JS Operators](https://www.w3schools.com/js/js_operators.asp)

要讓網頁具備「計算」的能力（例如計算總得分、計算總金額），就必須要有容器來儲存這些數字。

### 5.2.1 基礎概念：宣告與數學運算
* `let`: 宣告**可變變數**。裡面的值隨時可以被覆寫。
* `const`: 宣告**常數**。裡面的值一旦寫入就不能再被更改。

```javascript
// 宣告
const PI = 3.14; // 常數（圓周率）
let score = 90;  // 變數（分數）

// 算術運算 (+, -, *, /)
score = score + 5; 

// 賦值運算縮寫
score += 5; // 同上，這是一樣的意思
```

### 5.2.2 實戰應用：旅遊總價計算機
在旅遊網站中，機位與房價的計算就是運用這些基礎數學運算。我們可以把機票設為 `const`，而使用者的天數設為 `let` 來進行總價計算。

👉 **[Demo 5.2: 旅費計算機](src/js/demo_vars_ops.html)**

#### 💡 5.2 隨堂測驗

1️⃣ 關於 `let` 與 `const` 的宣告方式，下列敘述何者正確？

🇦 `const` 宣告的變數可以隨時用等號重新賦值  🇧 `let` 用於宣告「常數」，一旦給定初始值就不能更改  🇨 圓周率 PI 或航空公司代號等不會變動的值，應優先使用 `const` 宣告  🇩 兩者功能完全一樣，在現代 JavaScript 中可以隨意互換

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`const` 用於宣告不可變的常數，`let` 用於宣告可變的變數。使用 `const` 能避免程式碼在不經意間被修改，增加程式健壯性。
</details>

2️⃣ 執行以下程式碼後：`let x = 10; x += 5; x *= 2;`，變數 `x` 的最終數值為何？

🇦 15  🇧 30  🇨 25  🇩 20

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：首先 `10 + 5 = 15`，接著 `15 * 2 = 30`。
</details>

3️⃣ 在 JavaScript 中，下列哪一個變數名稱是「合法」且符合規範的？

🇦 `let 1stPlace = "Win";`  🇧 `let my-variable = 10;`  🇨 `let _userAge = 25;`  🇩 `let let = 100;`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：變數名不能以數字開頭 (🇦)，不能包含橫線 (🇧)，且不能使用保留字如 `let` (🇩)。底線或錢字號 `$ `開頭是合法的。
</details>

4️⃣ 運算式 `10 % 3` 的結果為何？

🇦 3  🇧 1  🇨 0.33  🇩 3.33

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：`%` 是取餘數符號。10 除以 3 等於 3 餘 1，因此結果為 1。
</details>

#### 📝 5.2 實作練習：Lab 5.2 總價計算
**目標：** 透過變數運算算出包含服務費的總旅費。
1. 宣告常數 `FLIGHT_PRICE` 為 12000，以及 `HOTEL_NIGHT_PRICE` 為 3000。
2. 宣告變數 `stayNights` 為 4。
3. 計算總價 `FLIGHT_PRICE + (HOTEL_NIGHT_PRICE * stayNights)`。
4. 使用 `+=` 將剛剛算出的總價加上 5% 服務費，並將結果輸出至 Console。

---

## 5.3 資料型態與字串處理

📚 [W3Schools 參考：JS Data Types](https://www.w3schools.com/js/js_datatypes.asp) | [JS String Methods](https://www.w3schools.com/js/js_string_methods.asp)

JavaScript 的變數不只能裝數字，還能裝文字、真假值。

### 5.3.1 基礎概念：型態與字串方法
有三種最基本的資料型態：
* `Number` (數字): 如 `123`, `3.14`。
* `String` (字串): 如 `"Hello"`。字串必須被引號包圍。
* `Boolean` (布林值): 只有 `true` (真) 或 `false` (假)。

**字串是非常常被處理的東西，我們常藉由各種「方法 (Methods)」來提取或轉換字串：**

> [!IMPORTANT]
> **字串是不可變的 (Immutable)**：在 JavaScript 中，任何針對字串的操作（如切割、轉大寫）都**不會改變原本的字串**，而是會**回傳一個全新的字串**。你必須用變數去接住這個新結果，不然等於白做！

#### 1. 字串切割三兄弟（擷取部分字串）
JavaScript 提供了三種常見的切割方法，雖然長得很像，但行為略有不同：
- `.slice(start, end)`：從 `start` 切到 `end` (不包含 end)。**支援負數**（從後面數過來）。**(最推薦使用)**
- `.substring(start, end)`：和 `slice` 一樣，但**不支援負數**（會直接把負數當作 `0`），且如果 `start > end` 它會自動對調。
- `.substr(start, length)`：從 `start` 開始，**往後連取 `length` 個字元**。（⚠️ 注意：此方法已逐漸被現代開發淘汰，官方建議改用 `slice`）。

```javascript
// 💡 以下用一個範例來闡述這三者的差異
let text = "Hello World";

// slice() 支援負號：把最後 5 個字切下來！
console.log(text.slice(-5));     // 輸出："World"

// substring() 不支援負號：把 -5 當作 0 放棄處理，從頭印到尾！
console.log(text.substring(-5)); // 輸出："Hello World"
// 偷偷幫你對調大於小於：
console.log(text.substring(5, 0)); // 輸出："Hello" (自動變成 0, 5)

// ✨ 以上操作完，原本的 text 有變嗎？
// 證明字串 Immutable 的特性：
console.log(text); // 依舊是 "Hello World"！剛剛的處理只是回傳了「新產物」
```

#### 2. 常用的實用加工：去空白與轉陣列

除了切割，我們還經常需要將使用者輸入的字串進行**資料清洗**與**陣列化**：

- `.trim()`：去除字串「頭尾」的多餘空白（處理使用者建立帳號或搜尋表單時必用！避免他手滑多按了空白鍵）。
- `.split(separator)`：用指定的符號字串，把一長串文字狠狠劈開，並**轉換成一個真實的陣列 (Array)**。

```javascript
// trim 應用：去除多餘空格
let inputStr = "   日本旅遊  ";
let cleanInput = inputStr.trim(); 
console.log(cleanInput); // 輸出乾淨的："日本旅遊"

// split 應用：把逗號拆成多個標籤
let tags = "溫泉,美食,泡湯";
let tagArray = tags.split(","); 
// 登愣！字串瞬間變成可以跑 map 或 for 迴圈的陣列了：
console.log(tagArray); // 輸出：["溫泉", "美食", "泡湯"]

// 補充：如果要把純數字的字串轉成正規數學數字
let numberStr = "50";
let trueNumber = parseInt(numberStr); // 變成可以加減乘除的數字 50
```

#### 3. 樣板字串 (Template Literals)：字串與變數的完美混搭

在開發網頁時，常常需要把「純文字」跟「變數」串接在一起（例如：顯示「您好，王小明！您的餘額是 100 元」）。
過去我們只能使用加號 (`+`) 辛苦地把字串和變數拼湊起來，遇到需要換行或包含 HTML 標籤時非常容易寫錯或漏寫雙引號：

```javascript
let userName = "王小明";
let balance = 100;

// ❌ 傳統寫法：充滿加號與引號，而且換行還要補上 \n
let msgOld = "您好，" + userName + "！\n您的餘額是 " + balance + " 元。";
```

現代 JavaScript 提供了一個超強大的功能：**樣板字串 (Template Literals)**。
只要把文字最外層的引號換成**反引號 (`` ` ``，位於鍵盤左上角 Esc 下方)**，你就可以直接在字串裡面利用 `${變數名稱}` 來挖洞並塞入變數！這不僅語法更直覺，還天然支援程式碼的直接換行：

```javascript
// ✅ 現代寫法：使用反引號 (`) 與 ${變數} 來挖洞
let msgNew = `您好，${userName}！
您的餘額是 ${balance} 元。`; 
// 可以直接按 Enter 換行，寫起來超乾淨！

console.log(msgNew);
```

> **💡 實戰小技巧：** 未來我們在用 JS 動態產生 HTML 標籤（例如用程式碼畫出好幾個 `<div class="card">` 行程卡片）時，使用樣板字串是前端開發中最常被選擇的方式，它能讓 HTML 結構在 JS 檔案中依舊保持極佳的閱讀性！

### 5.3.2 實戰應用：訂單折扣碼檢查
當使用者在旅遊網輸入折扣碼時，常常會不小心多打空白、或是沒切換大小寫。我們就利用字串方法來幫使用者自動修正，並且判斷有沒有打對！

👉 **[Demo 5.3: 訂單字串處理](src/js/demo_datatypes.html)**

#### 💡 5.3 隨堂測驗

1️⃣ 如果有變數 `let a = "10"; let b = 20;`，執行 `a + b` 的結果為何？

🇦 30  🇧 `"1020"`  🇨 `NaN`  🇩 報錯（Error）

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：當「字串」與「數字」使用 `+` 號時，JavaScript 會進行「字串串接（Concatenation）」，將數字轉為字串後拼在一起。若要進行數學加法，需先用 `parseInt()` 將字串轉為數字。
</details>

2️⃣ 關於相等比較子 `==` 與 `===` 的敘述，下列何者正確？

🇦 `10 == "10"` 會回傳 `false`  🇧 `10 === "10"` 會回傳 `true`，因為兩者值相同  🇨 `===` 稱為嚴格相等，會同時檢查「數值」與「型別」是否一致  🇩 在現代開發中，為了方便自動轉型，應盡量使用 `==`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`==` 會自動轉型（Loose Equality），因此 `10 == "10"` 為 true。而 `===` 不會轉型，因此 `10 === "10"` 為 false。為了避免隱藏 bug，現代開發強烈建議使用 `===`。
</details>

3️⃣ 在 JavaScript 中，字串具有「不可變性（Immutable）」。執行以下程式碼後：`let s = "hello"; s.toUpperCase();`，變數 `s` 的值為何？

🇦 `"HELLO"`  🇧 `"hello"`  🇨 `undefined`  🇩 拋出錯誤

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：字串方法如 `toUpperCase()` 會回傳一個「全新」的字串，而不會改變原本的變數。若要更新 `s`，必須寫成 `s = s.toUpperCase();`。
</details>

4️⃣ 使用樣板字串（Template Literals）時，應使用哪種符號包裹字串？

🇦 雙引號 `"`  🇧 單引號 `'`  🇨 反引號 `` ` ``  🇩 大括號 `{}`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：樣板字串必須使用反引號（Backticks）包裹，才能在內部使用 `${}` 語法嵌入變數與表達式。
</details>

#### 📝 5.3 實作練習：Lab 5.3 字串加工與解構
**目標 1：機票代碼擷取 (`slice` 的應用)**
1. 宣告一組包含航空公司代號與航班編號的字串：`let flight = "BR-2132";`。
2. 請使用 `.slice()` 方法，將前兩個字元的航空公司代號（`"BR"`）切出來。
3. 再切出後面的編號（`"2132"`），並分別印在 Console 中，例如輸出："航空代碼：BR，航班編號：2132"。

**目標 2：景點標籤陣列化 (`split` 與 `trim` 的應用)**
1. 宣告一組使用者常常亂打多餘空白的標籤輸入：`let userInput = "  溫泉, 美食, 海景   ";`。
2. 先使用 `.trim()` 一次性去掉字串最外圍頭尾沒必要的隱藏空白。
3. 再使用 `.split(",")` 把這串文字依照逗號「劈開」成獨立的陣列。
4. 將最後得到的乾淨陣列印出來，觀察結果！

---

## 5.4 流程控制

📚 [W3Schools 參考：JS If...Else](https://www.w3schools.com/js/js_if_else.asp) | [JS For Loop](https://www.w3schools.com/js/js_loop_for.asp)

程式如果只會從上往下執行是不夠的，我們需要讓他在不同的情況「轉彎」(If)，或是重覆做無聊的事 (For)。

### 5.4.1 基礎概念：條件判斷 (if / else)
```javascript
let passScore = 60;
let myScore = 75;

if (myScore >= passScore) {
    console.log("考試及格！");
} else {
    console.log("考試被當了...");
}
```

### 5.4.2 基礎概念：迴圈 (for)
如果要印出 1 到 5：
```javascript
// i 的起始值是 1；只要 i <= 5 迴圈就繼續；每次做完 i 加 1
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

### 5.4.3 實戰應用：購票規則與優惠表
在購票系統中，我們利用 `if / else` 判斷大人與兒童票價；同時，我們也能利用 `for` 迴圈，一口氣算出旅客住 1 到 5 晚分別要付多少錢。

👉 **[Demo 5.4: 購票規則與迴圈佈局](src/js/demo_logic.html)**

#### 💡 5.4 隨堂測驗

1️⃣ 在 `for` 或 `while` 迴圈中，若想在特定條件下「直接跳出並終止」整個迴圈，應使用哪個關鍵字？

🇦 `continue`  🇧 `exit`  🇨 `break`  🇩 `stop`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`break` 會立刻終止迴圈；`continue` 則是跳過本次回合，直接開始下一輪。
</details>

2️⃣ 判斷式 `if (0) { ... }` 裡面的程式碼會被執行嗎？

🇦 會，因為 0 代表程式開始  🇧 不會，因為 0 在布林判定中被視為「假值（Falsy）」  🇨 會，只要有數字就會執行  🇩 不一定，視瀏覽器而定

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：在 JavaScript 中，數字 `0`、空字串 `""`、`null`、`undefined` 與 `NaN` 都會被視為 `false`。
</details>

3️⃣ 關於 `for` 迴圈的語法 `for (A; B; C)`，下列敘述何者正確？

🇦 A 位置放置的是「迴圈繼續的條件」  🇧 B 位置放置的是「每回合結束後的變動」  🇨 C 位置放置的是「計數器的起始設定」  🇩 B 位置若條件為 `false`，迴圈就會停止

<details>
<summary>按此查看答案與解析</summary>
**答案：🇩**  
解析：正確結構為 `for (起始設定; 繼續條件; 每回合變動)`。只有當條件 B 為 `true` 時，迴圈才會執行。
</details>

4️⃣ 執行 `true && false` 的布林運算結果為何？

🇦 `true`  🇧 `false`  🇨 `undefined`  🇩 `error`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：`&&` (AND) 運算必須兩邊皆為 `true` 結果才會是 `true`。
</details>

#### 📝 5.4 實作練習：Lab 5.4 票價試算表
**目標：** 結合變數與迴圈。
1. 使用 `for` 迴圈產生並印出加總的 1 到 100 的數字總和。
2. （進階）利用迴圈在 Console 產生一個簡單的 9x9 乘法表。

---

## 5.5 函式 (Functions)

📚 [W3Schools 參考：JS Functions](https://www.w3schools.com/js/js_functions.asp) | [JS Arrow Function](https://www.w3schools.com/js/js_arrow_function.asp)

當同樣的程式碼要在不同地方寫好幾次時，我們就可以把它「包裝」起來變成函式。

### 5.5.1 基礎概念：宣告函式與回傳 (`return`)
每次呼叫函式，你都可以丟不同的「參數」給它，它運算完後可以丟回「結果」(Return)。
```javascript
function addNumbers(a, b) {
    let result = a + b;
    return result;
}

console.log( addNumbers(5, 10) ); // 印出 15
console.log( addNumbers(100, 200) ); // 印出 300
```

ES6 標準之後，更流行一種超級簡化的寫法叫做「箭頭函式」：
```javascript
// 連大括號跟 return 都省了
const addNumbers = (a, b) => a + b;
```

### 5.5.2 實戰應用：會員折扣計算模組
旅遊系統中，結帳時有一大串計算營業稅、手續費、會員折扣的邏輯。如果把這些寫成函式，主程式看起來就會非常的乾淨又好維護！

👉 **[Demo 5.5: 自訂函式與會員折扣](src/js/demo_functions.html)**

#### 💡 5.5 隨堂測驗

1️⃣ 若一個 JavaScript 函式在執行完畢後沒有撰寫 `return` 關鍵字，則呼叫該函式的回傳結果會是什麼？

🇦 `null`  🇧 `0`  🇨 `undefined`  🇩 拋出語法錯誤

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：JS 函式預設若無回傳值，會自動回傳 `undefined`。
</details>

2️⃣ 關於「箭頭函式 (Arrow Functions)」的語法，下列何者「錯誤」？

🇦 `const greet = () => "Hello";` 是正確的簡寫  🇧 箭頭函式比傳統 `function` 語法更簡潔  🇨 如果只有一個參數，可以省略小括號  🇩 箭頭函式一定要寫 `return`，不能省略

<details>
<summary>按此查看答案與解析</summary>
**答案：🇩**  
解析：若箭頭函式內部只有一行運算式，可以省略大括號與 `return` 關鍵字，它會自動回傳運算結果。
</details>

3️⃣ 為什麼要在程式中使用「函式」？

🇦 為了讓程式跑得更快  🇧 為了封裝重複邏輯，增加程式碼的重用性（Reusable）與可讀性  🇨 為了強制瀏覽器使用特定的記憶體區塊  🇩 為了讓 HTML 檔案變大

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：函式能將一段特定的邏輯打包，未來只需呼叫函式名稱即可重複執行，方便維護。
</details>

4️⃣ 呼叫函式時傳入的東西（例如 `addNumbers(5, 10)` 裡的 5 和 10）在術語上稱為什麼？

🇦 選項 (Options)  🇧 參數 (Parameters / Arguments)  🇨 指令 (Commands)  🇩 標籤 (Tags)

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：傳入函式的數值稱為「參數」，函式內部會透過定義好的變數名來接收並運算這些值。
</details>

#### 📝 5.5 實作練習：Lab 5.5 折扣計算器函式
**目標：** 練習撰寫不同回傳條件的函式。
1. 寫一個標準函式 `getDiscount(price, level)`。
2. 如果 `level` 是 `"VIP"`，回傳打 8 折的金額；若是 `"Normal"` 回傳 95 折。
3. 嘗試把同一個邏輯改寫成箭頭函式。

---

## 5.6 陣列 (Arrays)

📚 [W3Schools 參考：JS Arrays](https://www.w3schools.com/js/js_arrays.asp) | [JS Array Methods](https://www.w3schools.com/js/js_array_methods.asp)

遇到大量的資料，如果每個都要宣告變數（`let a=1, b=2, c=3...`）會非常麻煩，此時我們用陣列 (Array) 把他們裝成一排。

### 5.6.1 基礎概念：陣列宣告與存取
用中括號 `[]` 包起來的東西就是陣列，陣列的索引是從 `0` 開始算的！
```javascript
let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]); // 印出 Apple

fruits.push("Mango"); // push() 是把新東西推到陣列的最後一格
```

### 5.6.2 基礎概念：陣列常用操作方法 (Methods)

JavaScript 提供了非常多內建的方法來幫助我們操作陣列，這裡整理最基礎且開發上最常用的幾項：

* **特徵值 `.length`**：取得這條陣列裡的總數量。（注意：因為它是「特徵」而非「動作」，所以不用加小括號）。
* **新增與移除 `.push() / .pop()`**：
  * `.push(值)`：將新元素推入到陣列的**最後面**。
  * `.pop()`：把陣列**最後面**的元素拔除。
* **重組與轉換 `.toString() / .join()`**：
  * `.toString()`：將陣列轉為純文字字串（預設會用逗號隔開）。
  * `.join("自訂符號")`：類似 `toString()`，但威力更強，可以讓你自訂字串中間的「連接符號」。
* **排序 `.sort()`**：將陣列內容進行排序。（⚠️ 注意陷阱：預設會將內容視作「字串」並依照字母順序排列。如果要拿來排數字，會發生 `10` 排在 `2` 前面的狀況，數字排序需要另外給予判斷規則）。

```javascript
let cars = ["Toyota", "Honda", "BMW"];
console.log(cars.length); // 3 (總共三個廠牌)

cars.push("Benz"); // 從後面推進去 -> ["Toyota", "Honda", "BMW", "Benz"]
cars.pop();        // 從後面拔走一個 -> 又回到原本的 3 個

// 使用 join() 輸出漂亮乾淨的字串
console.log(cars.join(" - ")); // 轉換成字串："Toyota - Honda - BMW"

// 依字母順序重新排列
cars.sort(); 
console.log(cars); // 字母排序："B"MW, "H"onda, "T"oyota
```

> **💡 進階補充：`.sort()` 與現代新語法 `.toSorted()` 的關鍵差異**
> 
> 回想一下前面對字串所做的加工（字串是不可變的 Immutable）。但你有沒有發現，執行 `cars.sort()` 後，**原本的 `cars` 陣列直接被破壞並改變了**？這種會影響原本陣列的方法稱為「破壞性操作 (Mutating)」。
> 
> 在現代開發（例如近年很紅的 React 框架）中，非常強調資料的「不可變性 (Immutability)」，也就是極度不喜歡原本的資料被偷偷修改。
> 
> 為此，最新的 JavaScript 推出了一系列「非破壞性」的新方法，其中最實用的就是 **`.toSorted()`**。
> 它與 `.sort()` 的功能完全相同，但它**「絕不更動原本的陣列」**，而是**「回傳一個全新的、已經排好序的陣列」**：
> 
> ```javascript
> let original = [3, 1, 2];
> 
> // 使用現代的 toSorted() 來排序，並用一個新變數接住它
> let sortedArray = original.toSorted(); 
> 
> console.log(original);    // [3, 1, 2] (原本的陣列平安無事！)
> console.log(sortedArray); // [1, 2, 3] (拿到一份嶄新的結果陣列)
> ```

### 5.6.3 進階觀念：回呼函式 (Callback Function) 與 forEach

在撰寫網頁時（尤其是綁定按鈕事件或進階陣列操作），我們會非常頻繁地聽到「**Callback Function (回呼函式)**」這個詞。
**什麼是 Callback？** 簡單來說，就是「**把一小段程式碼 (函式)，當成包裹 (參數) 傳給別人，請別人在適當的時機幫你執行**」。

陣列中最好用的 `.forEach()` 方法，就是 Callback 最經典的應用。過去我們要印出所有資料得寫一大串 `for(let i=0...)` 迴圈，現在只要呼叫 `forEach`，並把「你希望每一回合做什麼動作」包裝成函數（Callback），丟給它就好了：

```javascript
let colors = ["Red", "Green", "Blue"];

// ❌ 傳統的 for 迴圈寫法：
for (let i = 0; i < colors.length; i++) {
    console.log("傳統印出: " + colors[i]);
}

// ✅ 現代 forEach 搭配 Callback：
// 我們宣告了一個只執行一次的「匿名函式」丟進去給 forEach 重覆呼叫
colors.forEach(function(color) {
    console.log("forEach印出: " + color);
});

// 🔥 更常見的做法：搭配前面學過的「箭頭函式」讓語法極致簡化！
colors.forEach((color) => {
    console.log(`箭頭 Callback: ${color}`);
});
```

**💡 Callback 的另一個經典應用：自訂 `.sort()` 排序規則**
前面我們提過 `.sort()` 預設會把陣列內容當作字串、依照字母順序排。如果是數字，這會導致 `10` 排在 `2` 前面。
為了解決這個問題，我們可以丟一個 Callback 函式（比較器）給 `.sort()`，教它如何判斷誰大誰小！

舉例來說，我們有一群學生，想要改為**「依據體重做排序」**：

```javascript
let students = [
    { name: "John", weight: 70 },
    { name: "Alice", weight: 55 },
    { name: "Bob", weight: 85 }
];

// 我們丟入一個比較函式 (Callback)，每次挑兩個學生 (x, y) 出來比體重。
// 規則：若 x.weight - y.weight 為負數，代表 x 比較輕，x 就會被排在前面（升冪排序由輕到重）！
students.sort((x, y) => x.weight - y.weight);

// (如果是要「降冪排序」由重到輕，只要改成 y.weight - x.weight 即可)

console.log(students); 
// 原陣列已重新排序，結果依序為：Alice (55), John (70), Bob (85)
```
*(備註：剛學過的現代語法 `.toSorted()` 也完全支援同樣的 Callback 比較器寫法唷！)*

### 5.6.4 進階觀念：陣列高階方法 (map, filter, reduce)

學會了 Callback 之後，JavaScript 提供了三個被譽為「陣列三劍客」的強大高階方法。它們全部都依賴 Callback 運作，並且**都不會改變原本的陣列**（非破壞性），而是回傳全新的結果。這在開發複雜的網頁資料處理與畫面繪製時超級實用！

#### 1. `.map()`：陣列元素的一對一加工
當你想把陣列裡的「每一個東西」都經過某種加工，並收集成另一個長度相同的全新陣列時使用。
```javascript
let prices = [100, 200, 300];

// 把每個價格都打 8 折 (產生新陣列)
let discountedPrices = prices.map(price => price * 0.8);

console.log(discountedPrices); // [80, 160, 240]
```

#### 2. `.filter()`：陣列元素的過濾器
當你想從陣列中「篩選」出符合條件的元素，拋棄不符合的，並把它們集中成一個新陣列時使用。Callback 內部必須提供一個條件，它會被判定為 `true`（保留）或 `false`（丟棄）。
```javascript
let scores = [45, 80, 60, 30, 95];

// 只保留大於等於 60 分的及格分數
let passScores = scores.filter(score => score >= 60);

console.log(passScores); // [80, 60, 95]
```

#### 3. `.reduce()`：陣列元素的收斂與總計算
當你想把陣列裡的所有東西「累積」成一個單一結果（例如總和加總）時使用。
它的 Callback 會接收兩個核心參數：`accumulator`（負責記憶到目前為止的總累積值）與 `currentValue`（目前回合被拿出來處理的元素）。
```javascript
let expenses = [150, 60, 800, 20];

// total 負責記憶目前的總和，expense 則是每一次拿出來的開銷
// 結尾拋出的 `, 0` 代表「總和起點從 0 開始算」
let totalExpense = expenses.reduce((total, expense) => total + expense, 0);

console.log(`總花費：${totalExpense} 元`); // 1030 
```

> **💡 實戰小技巧：連鎖技 (Chaining)**
> 因為 `map` 與 `filter` 執行完畢後都會回傳全新的「陣列」，所以你可以把它們像火車車廂一樣無窮盡地串接起來！
> 例如：你可以先呼叫 `.filter()` 濾出及格的成績，後面直接加一個 `.map()` 把這些成績加上十分。這種寫法能用一行程式碼取代過去落落長的 `for` 迴圈與 `if` 邏輯！

### 5.6.5 實戰應用：目的地清單管理
旅遊網有幾十個目的地，我們會將它們統整到陣列裡。還能用進階的方法（如 `filter()`）快速找出符合特定關鍵字的行程。

👉 **[Demo 5.6: 陣列與熱門目的地管理](src/js/demo_arrays.html)**

#### 💡 5.6 隨堂測驗

1️⃣ 如何取得一個 JavaScript 陣列中總共包含多少個元素？

🇦 `array.size()`  🇧 `array.count`  🇨 `array.length`  🇩 `array.index`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`.length` 是陣列的內建屬性（注意不是方法，不用加括號），用來讀取陣列的長度。
</details>

2️⃣ 下列哪一個陣列運作會將新元素加入到陣列的「最後面」？

🇦 `push()`  🇧 `pop()`  🇨 `shift()`  🇩 `unshift()`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇦**  
解析：`push()` 從後方推入元素；`pop()` 從後方拔出；`unshift()` 從前方塞入；`shift()` 從前方拔出。
</details>

3️⃣ 關於陣列的高階方法 `.map()`，下列敘述何者正確？

🇦 它會直接更改原本的舊陣列，不產生新陣列  🇧 它會篩選掉不符合條件的元素  🇨 它會對每一個元素進行加工，並回傳一個長度相同的新陣列  🇩 它會將陣列收斂計算成一個單一的數值

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`map()` 是對應加工；`filter()` 是條件篩選；`reduce()` 是收斂加總。這三者皆為非破壞性方法（回傳新結果）。
</details>

4️⃣ 想從一個包含 100 筆資料的陣列中，快速過濾出「分數大於 60 分」的資料建立新陣列，應優先使用哪種方法？

🇦 `forEach()`  🇧 `map()`  🇨 `filter()`  🇩 `sort()`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`filter()` 專門用於篩選出符合條件的子集合。
</details>

#### 📝 5.6 實作練習：Lab 5.6 簡易陣列操作
**目標：** 基本陣列處理。
1. 建立一個陣列包含三個都市：`["台北", "台中", "高雄"]`。
2. 使用 `for` 迴圈找出所有的值，並在 Console 每行印出 `📍 前往: XXX`。
3. 將陣列使用 `join("-")` 轉為字串並印出。

---

## 5.7 物件 (Objects)

📚 [W3Schools 參考：JS Objects](https://www.w3schools.com/js/js_objects.asp) | [JS JSON](https://www.w3schools.com/js/js_json_intro.asp)

陣列只能裝單一維度的資料，但如果一筆資料包含了很多個「特徵」呢？這時候需要用物件。

### 5.7.1 基礎概念：大括號與屬性
物件使用 `{}` 包裹，裡面的東西由 `屬性: 值` 所構成。這也是 JavaScript 最重要的資料結構 (JSON 格式的基礎)。
```javascript
let person = {
    name: "John",
    age: 20
};

// 用「點」來取出特徵
console.log(person.name); // John
// 賦予新名字
person.name = "Alice"; 
```

### 5.7.2 為什麼需要物件？陣列與物件的資料結構比較

當我們要儲存一群使用者的詳細資料（例如：姓名、身高、體重）時，如果只用前面學過的「陣列」，很快就會遇到管理上的災難。我們用三個人的資料（Nick, Jie, Albert）來比較各種寫法：

**❌ 寫法一：多個一維陣列 (散落的資料)**
```javascript
let names = ['Nick', 'Jie', 'Albert'];
let heights = [172, 177, 176];
let weights = [67, 65, 72];
```
* **痛點**：資料徹底散落。如果我們要找「Jie 的體重」，必須先知道 Jie 在 `names` 的索引是 `1`，再去 `weights[1]` 尋找。若是未來有人被刪除而沒同步改到另一個陣列，體重就會冠到錯的人身上！

**❌ 寫法二：二維陣列 (失去可讀性的神秘數字)**
```javascript
let people = [
    ['Nick', 172, 67],
    ['Jie', 177, 65],
    ['Albert', 176, 72]
];
```
* **痛點**：雖然資料總算被綁在一起了，但我們必須用 `people[1][2]` 才能拿到 Jie 的體重。未來的開發者只看程式碼根本猜不到這個 `[2]` 到底代表體重、還是年紀、還是考績？

**✅ 寫法三：陣列結合物件 (現代標準做法)**
物件最強大的地方在於：它能為每個數值標上明確的「屬性名稱 (Key)」。
```javascript
let nick = { name: 'Nick', height: 172, weight: 67 };
let jie = { name: 'Jie', height: 177, weight: 65 };
let albert = { name: 'Albert', height: 176, weight: 72 };

// 用一個大陣列把它們裝起來！
let people = [nick, jie, albert];

// 或是更常見的實戰縮寫方式：
/*
let people = [
    { name: 'Nick', height: 172, weight: 67 },
    { name: 'Jie', height: 177, weight: 65 },
...
]
*/

// 🎯 超直覺的取值方式：
console.log(people[1].weight);  // 印出 65

/* === 🚀 進階挑戰：結合陣列找最大值，找出這群人中 BMI 最高的人 === */
// 先拿第一個人的 BMI 當作預設的「目前最高紀錄」
let maxBmiPerson = people[0];
let maxBmi = maxBmiPerson.weight / ((maxBmiPerson.height/100) ** 2);

// 使用前面學過的 forEach 去巡過每一個陣列裡的人
people.forEach(person => {
    let currentBmi = person.weight / ((person.height/100) ** 2);
    // 如果這個人的 BMI 比最高紀錄還高，就把它替換成最高紀錄！
    if (currentBmi > maxBmi) {
        maxBmi = currentBmi;
        maxBmiPerson = person; // 記住這整個人(物件)的資料，非常方便
    }
});

console.log(`BMI 最高的是 ${maxBmiPerson.name}，他的 BMI 為 ${maxBmi.toFixed(2)}`);
// (運算結果會是 Albert 的 BMI 最高，數值為 23.24)
```
* **完美解法**：`people[1].weight` 這種寫法就像在讀英文句子一樣自然 ——「找出陣列裡的第 2 個人，接著拿他的體重」。它兼具了陣列方便跑迴圈篩選的優點，以及物件能清楚標示意義的高可讀性，這就是未來你最常遇到的 JSON 資料結構！

### 5.7.3 進階觀念：物件的內建技能 (Method)

在上面找最高 BMI 的挑戰裡，我們每次都需要把 `person.weight` 跟 `person.height` 拉出來重新進行數學運算，稍微有點麻煩。
但其實，**物件除了可以存文字、數字特徵之外，還能把「函式 (Function)」存進去當作自己的專屬技能！** 當一個函式被綁在物件裡時，我們在術語上將其稱為這個物件的「**方法 (Method)**」。

如果我們讓這些名單資料自帶「結算這筆資料 BMI」的技能呢？

```javascript
let albert = {
    name: 'Albert', 
    height: 176, 
    weight: 72,
    
    // 把一段函式存入，成為專屬於這個物件的方法 (Method)
    getBMI: function() {
        // 👉 在物件的方法裡，我們使用特殊的關鍵字 `this` 
        // `this` 代表「呼叫這個方法的物件自己」
        // 所以這行可以翻譯成：拿「我自己」的 height 除以 100
        let hInMeters = this.height / 100;
        let bmi = this.weight / (hInMeters * hInMeters);
        
        return bmi;
    }
};

// 呼叫起來就像變魔術！要查 Albert 的 BMI 不用再幫他算了，請他「發動技能」回答你！
console.log( albert.getBMI().toFixed(2) ); // 印出 23.24
```
> **💡 `this` 關鍵字的威力**：
> 當你在物件的函式中使用 `this`，它就代表「擁有這個方法的物件」。`this.weight` 直接等於「拿我自己的體重」。未來用這種寫法來封裝資料，在開發動態表單時會省下大量拉扯變數的心力！

> **ℹ️ 語法補充：直接使用 `{}` (物件字面值) 與 `class` (類別) 的差異**
> 我們現在這樣直接寫出 `{ name: 'Albert' }`，稱為「由物件字面值 (Object Literal) 直接生成」。這適合用作產生一次性、單一獨立的資料。
> 如果在遊戲開發中，你需要量產 100 個屬性結構一模一樣的史萊姆怪物，我們就會改用 **`class (類別)`** 作為藍圖範本，再透過藍圖去把這 100 個物件實體化 (Instances) 製造出來。

**💡 進階觀念：物件裡面還可以包物件 (Nested Objects)**
物件的屬性值並不僅限於數字或字串，它也可以是「另一個物件」！這種像俄羅斯娃娃一樣的寫法非常普遍，能幫助我們建立非常立體的資料層級：
```javascript
let order = {
    orderId: "A101",
    customer: {         // 屬性 customer 的值，又是另外一層獨立的物件！
        name: "Nick",
        phone: "0912-345-678"
    },
    total: 500
};

// 想抓到這筆訂單客人的電話？直接利用連續的「點」來抓取即可！
console.log(order.customer.phone); // 印出 0912-345-678
```

### 5.7.4 走訪物件：for...in 迴圈

前面學過陣列可以用 `forEach` 輕鬆從頭跑到尾。但如果我們遇到一個「物件」，想要把裡面的每一個「屬性 (Key)」與「值 (Value)」都反覆印出來，就要使用專門對付物件的 `for...in` 迴圈：

```javascript
let infoObj = {
    name: 'Albert', 
    height: 176, 
    weight: 72
};

// 使用 for...in 將 infoObj 裡的屬性 (Key) 一個個抓出來
for (let prop in infoObj) {
    // prop 此時會依序變成 'name', 'height', 'weight' 這些字串
    // 我們利用中括號 [prop] 的方式來取得動態的對應「值」
    console.log(`屬性名：${prop}，數值：${infoObj[prop]}`);
}
```

> **⚠️ 經典陷阱提醒：`for...of` 與 `for...in` 的關鍵差異**
> 這兩個迴圈長得很像，但請記得它們處理的主戰場天差地遠：
> - **`for...of`**：專門用來走訪**陣列裡面的「值 (元素)」**。針對陣列使用，可以正確拿出身高、體重等資料本身。
> - **`for...in`**：專門用來走訪**物件裡面的「屬性名 (Keys)」**。如果你不小心把 `for...in` 拿去跑陣列，它抓出來的將會是陣列背後隱藏的「索引序號 (Indexes，即 0, 1, 2)」，而不是你想要的陣列數值！切記別搞混！

### 5.7.5 現代資料結構：Set 與 Map

在 ES6 之後，JavaScript 引入了兩種非常實用的全新資料結構：**`Set`** 與 **`Map`**。它們分別解決了傳統陣列與物件在某些情境下的痛點。

#### 1. Set：不會重複的特殊陣列
**`Set`** 就像是一個「**絕對不能有重複元素**」的陣列。
- **與 Array 的差異**：陣列可以容納無限多個一樣的值，但 `Set` 內部擁有極嚴格的管控，會**自動剃除重複的資料**。
- **常見應用**：非常適合拿來做「購物車清單去重」、「搜尋歷史唯一值過濾」。

```javascript
// 宣告一個 Set，並嘗試放入重複的 "溫泉"
let uniqueTags = new Set(["溫泉", "美食", "溫泉", "海景"]);

// 登愣！它自動幫你過濾掉第二個 "溫泉" 了！
console.log(uniqueTags); // Set(3) {'溫泉', '美食', '海景'} 

// 🎯 常見存取方法
uniqueTags.add("購物");      // 新增元素
uniqueTags.delete("美食");   // 移除元素
console.log(uniqueTags.has("海景"));  // 檢查是否存在 (回傳 true)
console.log(uniqueTags.size);         // 取得總數量 (對標陣列的 length)

// 🏃 走訪 Set (像陣列一樣使用 for...of)
for (let tag of uniqueTags) {
    console.log(`標籤：${tag}`);
}
```

#### 2. Map：打破限制的進階物件
傳統的物件 (`{}`) 雖然好用，但它的「屬性名稱 (Key)」**硬性規定只能是字串**。而 **`Map`** 則允許你使用**任何資料型態（甚至可以直接把另一個物件，或是 HTML DOM 元素當作 Key）**來建立關聯表！
- **與 Object 的差異**：Key 的型態不受限制、內建計算數量的 `size` 屬性，且會精準記憶你塞入資料的「絕對順序」。
- **常見應用**：當你需要把「某個按鈕元件」與「一段特定的隱藏資料」死死綁在一起時極度強大。

```javascript
let userCart = new Map();

// 🎯 存取方法：set(建立關聯) 與 get(拿取資料)
userCart.set("A101", { item: "東京機票", qty: 2 });
userCart.set("B202", { item: "京都住宿", qty: 3 });

console.log(userCart.get("A101").qty); // 輕鬆印出 2
console.log(userCart.has("C303"));     // 檢查有沒有這個 Key (回傳 false)
console.log(userCart.size);            // 查看裡面有幾組對應資料 (結果：2)

// 🏃 走訪 Map (使用 for...of 可以同時把 Key 和 Value 拆解出來)
for (let [orderId, data] of userCart) {
    console.log(`訂單 ${orderId}: ${data.item}`);
}
```

#### 💡 實戰範例：用 Map 記憶 HTML 按鈕的獨立點擊次數
這是一個完美體現 `Map` 威力的場景，我們直接把畫面上的「HTML 元素本體」當作 Key，去對應它各自被按了幾次！

```html
<!-- HTML 區域 -->
<button id="btnLike">👍 讚</button>
<button id="btnShare">🔗 分享</button>
<p id="statusDisplay">尚未點擊</p>
```

```javascript
// JS 邏輯區域
// 1. 抓出畫面上的 HTML 節點
let btnL = document.getElementById('btnLike');
let btnS = document.getElementById('btnShare');
let display = document.getElementById('statusDisplay');

// 2. 建立一個專屬於紀錄次數的 Map
let clickRecords = new Map();

// 👉 直接拿 HTML 節點 (DOM) 本身當作 Key！幫它們各自設定初始次數 0
clickRecords.set(btnL, 0); 
clickRecords.set(btnS, 0);

// 3. 撰寫一個共用的點擊發動技能
function handleClick(event) {
    let clickedBtn = event.target; // event.target 可以抓到「這次究竟是哪一個按鈕被點了」
    
    // 從 Map 中精準抓出這個按鈕目前的次數，加 1 後重新存回去
    let currentCount = clickRecords.get(clickedBtn);
    clickRecords.set(clickedBtn, currentCount + 1);
    
    // 即時更新畫面狀態！
    display.innerHTML = `${clickedBtn.innerHTML} 總共被點了 ${clickRecords.get(clickedBtn)} 次！`;
}

// 掛載監聽器：當特定按鈕被點擊時，就去執行 handleClick 函式
btnL.addEventListener('click', handleClick);
btnS.addEventListener('click', handleClick);
```

### 5.7.6 實戰應用：旅遊套裝包裹
一個旅遊行程不單單只有名稱，它還包含了天數、價錢、是否還有名額等。用物件把它們封裝在一起，是現代網頁與伺服器溝通的標準格式。

👉 **[Demo 5.7: 物件與行程資料包裹](src/js/demo_objects.html)**

#### 💡 5.7 隨堂測驗

1️⃣ 如果要將 JavaScript 物件傳送給伺服器，通常會使用什麼方法將其轉為 JSON 字串？

🇦 `JSON.parse()`  🇧 `JSON.toText()`  🇨 `JSON.stringify()`  🇩 `Object.toString()`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`JSON.stringify()` 將物件轉為字串（序列化）；`JSON.parse()` 則是將字串轉回物件。
</details>

2️⃣ 關於 `for...of` 與 `for...in` 的敘述，下列何者正確？

🇦 `for...of` 用來走訪物件的屬性名，`for...in` 用來走訪陣列的數值  🇧 `for...in` 適合用來取得物件的屬性名稱 (Keys)，`for...of` 則專用於陣列的數值內容 (Values)  🇨 兩者功能完全相同，可以隨意互換  🇩 `for...of` 被設計來取代所有的 `forEach` 語法

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：`for...in` 抓取的是 Keys（或 Index）；`for...of` 抓取的是實際的元素 Value。對於物件建議使用 `for...in`。
</details>

3️⃣ 關於 `Set` 與 `Map` 的特性，下列哪一個敘述是「錯誤」的？

🇦 `Set` 內部擁有極嚴格的管控，會自動剃除重複的元素  🇧 `Map` 允許你使用任何資料型態（包含 HTML 節點）作為 Key  🇨 物件 (Object) 的 Key 預設只能是字串，而 `Map` 則沒有此限制  🇩 `Set` 只能裝數字，不能裝字串 or 物件

<details>
<summary>按此查看答案與解析</summary>
**答案：🇩**  
解析：`Set` 可以存放任何型別的資料，不僅限於數字，只要內容不重複即可。
</details>

4️⃣ 在物件的方法 (Method) 中，若要存取該物件自己內部的其他屬性，應使用哪個關鍵字？

🇦 `self`  🇧 `this`  🇨 `me`  🇩 `target`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：在物件方法中，`this` 指向當前調用該方法的物件實體。
</details>

#### 📝 5.7 實作練習：Lab 5.7 物件結構與現代資料操作
**目標 1：定義個人巢狀頁面**
1. 建立一個包含 `name`, `age` 的物件代表你自己。
2. 加上一個名為 `skills` 的屬性，裡面放一個陣列 `["HTML", "CSS"]`。
3. 加上一個名為 `contact` 的屬性，裡面「放另外一個物件」，包含你的 `phone` 與 `email`。建立完成後，試著用連續的 `.` 把你的電話單獨印出來。

**目標 2：具備自我計算技能的購物車**
1. 建立一個叫 `myCart` 的物件，裡面給予 `appleQty: 3` 與 `bananaQty: 2` 這兩個水果數量屬性。
2. 在該物件內加入一個名為 `getTotal()` 的方法 (Method)。
3. 在裡面使用 `this` 關鍵字，讓 `getTotal()` 把自己的蘋果與香蕉數量相加，並使用 `return` 丟出數學結果。
4. 使用 `console.log(myCart.getTotal())` 測試看看它是否能順利印出總數量 `5`。

**目標 3：不重複的 Set 景點清單**
1. 定義一個全新的 `Set`，並試著塞入這批資料：`["阿里山", "日月潭", "阿里山", "太魯閣"]`。
2. 利用 `console.log` 觀察這組 Set 的 `.size` 與裡面的內容，看看多餘的阿里山是不是真的被過濾掉而剩下 3 個了！

---

## 5.8 檔案物件模型 (DOM) 與事件：讓網頁活起來

📚 [W3Schools 參考：JS HTML DOM](https://www.w3schools.com/js/js_htmldom.asp) | [JS Events](https://www.w3schools.com/js/js_events.asp)

有了以上的 JS 基礎，我們終於準備好去觸摸 HTML 畫面上的標籤了。

### 5.8.1 基礎概念：尋找元素與綁定事件
JavaScript 把整個網頁視作一棵樹，我們稱為 **DOM (Document Object Model，檔案物件模型)**。在這棵樹上的每一種 HTML 標籤（例如 `<h1>`, `<button>`, `<div>`），對 JS 來說都是一個能夠被操控的「物件 (Object)」。

我們能使用 JavaScript 提供的主人公 `document` 作為夾子，去網頁上找出特定的標籤，並在上面修改文字、調整樣式，或是安裝「監聽器」(Event Listener)。

```html
<button id="myBtn">點我</button>
<p id="message"></p>

<script>
    // 1. 抓取按鈕元素 (就像用雷達抓怪物一樣鎖定它)
    let btn = document.getElementById("myBtn");
    
    // 2. 安裝事件監聽器！這裡設定「當按鈕被 click 時」，去執行後方那段函式
    btn.addEventListener("click", () => {
        document.getElementById("message").innerHTML = "你點了按鈕！";
    });
</script>
```

### 5.8.2 必備武器清單：DOM 常見的尋找方法與屬性
在前端實戰開發中，你 90% 的工作會是這三步：「找到標籤 ➔ 修改長相 ➔ 掛上事件」。以下是我們在現代開發中最常用到的語法清單：

**🕵️‍♂️ 尋找元素的方法 (Methods)**
* `document.getElementById('id名稱')`：最基本也最常用的夾子，專門精準鎖定單一的 ID 元素。
* `document.querySelector('CSS選擇器')`：現在**最推薦**的終極武器！支援用大家熟悉的 CSS 語法來抓取（例如抓 class：`.btn`，抓結構：`div > p`）。它會回傳抓到符合條件的「第一個」元素。
* `document.querySelectorAll('CSS選擇器')`：和上面相似，但威力更大！它會把畫面上「所有」符合條件的元素，全部打包成一個類似陣列的 NodeList 給你。實務上常常搭配 `.forEach()` 一次幫十個按鈕綁上事件！

**✍️ 操控元素的屬性 (Properties)**
一旦你把元素抓起來存成變數後，就可以讀寫它的以下屬性：
* `.innerHTML`：替換標籤內的內容（支援寫入 HTML 語法，例如可以塞入 `<strong style="color:red">嗨</strong>`）。
* `.value`：專屬表單元件！用來取得使用者在 `<input>` 或 `<textarea>` 裡面輸入的字串。
* `.style`：用來直接改變行內 CSS 樣式。例如 `btn.style.color = "red"`。（⚠️ 需注意特例：像 `font-size` 等有橫線的 CSS 屬性，在 JS 裡面全部要改成駝峰式命名 `fontSize`）。
* `.classList`：操控標籤 class 的超級好幫手！這在切換版型特效時極度實用：
  * `.classList.add('active')`：幫元素動態掛上一個新的 class。
  * `.classList.remove('hidden')`：幫元素拔掉特定的 class。
  * `.classList.toggle('dark-mode')`：像開關一樣！如果元素原本沒有這個 class 就加上去，有的話就拔掉。（實作深夜模式的絕佳神器！）

### 5.8.3 豐富的互動：常見的滑鼠與鍵盤事件 (Events)
剛才你看到了在 `addEventListener` 裡面填入的第一個參數 `"click"` 就是事件名稱。網頁之所以生動，就是因為我們能在各種千奇百怪的時機點去觸發效果：

| 事件名稱 (Events) | 什麼時候會發動 (觸發時機)？ | 實戰常見應用場景 |
|------------------|---------------------------|----------------|
| `click` | 滑鼠左鍵點擊元素時 | 傳送表單、開啟 / 關閉彈出視窗 (Modal) |
| `mouseenter` / `mouseleave` | 滑鼠游標「進入」與「離開」元素時 | 製作進階的懸停動畫 (Hover) 或是顯示 tooltip 提示框文字 |
| `keydown` / `keyup` | 在鍵盤上「按下」或是「放開」按鍵時 | 製作網頁闖關小遊戲的方向鍵控制，或是偵測使用者按下 Enter 鍵直接發送聊天訊息 |
| `input` | 在 `<input>` 欄位裡面每次打字改變內容時 | 即刻檢查密碼長度是否符合規範、或是做 Google 的「輸入即自動搜尋字詞建議」功能 |
| `scroll` | 當使用者在視窗或是特定區塊滾動頁面時 | 當畫面往下滑超過 500px，右下角浮現一個「回到頂端」的按鈕 |

### 5.8.4 實戰應用：旅遊購物車與互動清單
把先前的變數計數器，跟網頁上的結帳按鈕綁在一起，這就是現代電商最核心的「加入購物車」行為！

👉 **[Demo 5.8: DOM 操作與加入購物車](src/js/demo_dom.html)**

#### 📝 5.8 綜合演練：Lab 5.8 旅遊網站購物車介面 (期中統整)
這是一個把陣列、DOM 節點繪製、按鈕事件監聽結合在一起的純前端實戰專案：

👉 **[Lab: 旅遊願望清單完整實作](src/js/lab_travel_booking.html)**

**實作目標：**
1. 練習在畫面上輸入字串，按下按鈕後將字串存入 JS 的陣列中。
2. 每次陣列更新，用 JS 把陣列裡的資料生出成一堆 `<li>` 並插回畫面上。
3. 即時修改畫面右上角的購物車徽章 (`Badge`) 數字。

#### 💡 5.8 隨堂測驗

1️⃣ 在 JavaScript 術語中，將整個網頁視為一棵可以被操控的樹狀結構，稱為什麼？

🇦 CSS (Cascading Style Sheets)  🇧 DOM (Document Object Model)  🇨 JSON (JavaScript Object Notation)  🇩 API (Application Programming Interface)

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：DOM 是網頁的程式介面，讓 JS 能夠存取並改變 HTML 的內容與結構。
</details>

2️⃣ 在現代開發中，若要使用 CSS 選擇器（如 `.btn`）來抓取畫面上「第一個」符合條件的元素，應優先使用哪種方法？

🇦 `document.getElementById()`  🇧 `document.getElementsByClassName()`  🇨 `document.querySelector()`  🇩 `document.querySelectorAll()`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`querySelector` 是一把終極武器，允許開發者直接套用熟悉的 CSS 選擇器語法來鎖定元素。
</details>

3️⃣ 關於 `.innerHTML` 與 `.value` 的差異，下列論述何者正確？

🇦 `.innerHTML` 專門拿來抓取 `<input>` 裡的文字內容  🇧 `.value` 用來替換標籤內的 HTML 語法（如 `<strong>`）  🇨 抓取輸入框（Input）內的資料應使用 `.value`，修改一般容器標籤內容應使用 `.innerHTML`  🇩 二者完全一樣，可以隨時互換

<details>
<summary>按此查看答案與解析</summary>
**答案：🇨**  
解析：`.value` 僅限表單控制項使用；`.innerHTML` 則用於一般標籤的內部 HTML 內容。
</details>

4️⃣ 若想讓按鈕具有互動性，為其「安裝」一個事件監聽器的標準建議語法是什麼？

🇦 `btn.onclick = function() { ... }`  🇧 `btn.addEventListener("click", () => { ... })`  🇨 `btn.setEvent("click")`  🇩 `document.watch(btn)`

<details>
<summary>按此查看答案與解析</summary>
**答案：🇧**  
解析：`addEventListener` 是標準作法，能讓同一個元素監聽多個事件，且程式結構更清晰。
</details>

---

## 參考資源與延伸閱讀
* [MDN Web Docs - JavaScript 指南](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Guide)
* [JavaScript HTML DOM (W3Schools)](https://www.w3schools.com/js/js_htmldom.asp)
* 透過不斷地組合基本的 `if / for / Array`，並呼叫 DOM API 去改變 Tailwind 的排版 class，你就能做出看起來酷炫、且能順暢運作的現代化網頁了！