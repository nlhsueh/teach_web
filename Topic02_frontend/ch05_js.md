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

### 5.1.3 實戰應用：旅遊網站歡迎訊息
當我們把這個概念套用到旅遊網站上，就可以在訪客進站時跳出歡迎訊息，或是點擊按鈕時替換首頁的促銷標題。

👉 **[Demo 5.1: 旅遊網歡迎訊息](src/js/demo_basics.html)**

#### 💡 5.1 隨堂測驗
1. 想在瀏覽器開發者工具查看變數值，而不干擾使用者介面，應該用哪個方法？
<details>
<summary>點擊查看解答</summary>
`console.log()`
</details>

2. 開發大型網站時，JS 都直接包在 `.html` 裡面嗎？
<details>
<summary>點擊查看解答</summary>
通常使用「外部引用」，例如 `<script src="app.js"></script>`，這樣可以把結構 (HTML) 跟邏輯 (JS) 乾淨地分離。
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
1. `let` 與 `const` 的主要差別是什麼？
<details>
<summary>點擊查看解答</summary>
`let` 宣告後可以重新賦值，而 `const` 的值固定，不可更改。
</details>

2. 請問執行 `x = 10; x += 5; x *= 2;` 後，`x` 的值為多少？
<details>
<summary>點擊查看解答</summary>
30。 (10 + 5 = 15，然後 15 * 2 = 30)
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

### 5.3.2 實戰應用：訂單折扣碼檢查
當使用者在旅遊網輸入折扣碼時，常常會不小心多打空白、或是沒切換大小寫。我們就利用字串方法來幫使用者自動修正，並且判斷有沒有打對！

👉 **[Demo 5.3: 訂單字串處理](src/js/demo_datatypes.html)**

#### 💡 5.3 隨堂測驗
1. 為什麼要用 `parseInt()` 把 `"100"` 轉成數字？如果有變數 `a="10"`, `b="20"` 執行 `a+b` 會怎樣？
<details>
<summary>點擊查看解答</summary>
如果不轉型，執行 `"10" + "20"` 會發生「字串串接」，結果變成 `"1020"`，而不是數學上的 `30`。
</details>

2. `10 == "10"` 與 `10 === "10"` 哪個會回傳 true？
<details>
<summary>點擊查看解答</summary>
`10 == "10"` 為 true (自動轉型)；`10 === "10"` 為 false (嚴格相等，型別不同，常被推薦使用以避免 bug)。
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
1. 想從迴圈強制中途結束，應該使用哪個關鍵字？
<details>
<summary>點擊查看解答</summary>
`break`
</details>

2. `if (0)` 這個大括號內的邏輯會執行嗎？
<details>
<summary>點擊查看解答</summary>
不會，因為 `0` 在 JavaScript 中被視為 `falsy` (假值)，等同於 `false`。
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
1. 函式若沒有寫 `return`，呼叫它的結果會是什麼？
<details>
<summary>點擊查看解答</summary>
會得到預設的 `undefined`。
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

### 5.6.2 實戰應用：目的地清單管理
旅遊網有幾十個目的地，我們會將它們統整到陣列裡。還能用進階的方法（如 `filter()`）快速找出符合特定關鍵字的行程。

👉 **[Demo 5.6: 陣列與熱門目的地管理](src/js/demo_arrays.html)**

#### 💡 5.6 隨堂測驗
1. 如何取得陣列裡面總共有幾個元素？
<details>
<summary>點擊查看解答</summary>
使用 `array.length` 屬性。
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

### 5.7.2 實戰應用：旅遊套裝包裹
一個旅遊行程不單單只有名稱，它還包含了天數、價錢、是否還有名額等。用物件把它們封裝在一起，是現代網頁與伺服器溝通的標準格式。

👉 **[Demo 5.7: 物件與行程資料包裹](src/js/demo_objects.html)**

#### 💡 5.7 隨堂測驗
1. 如果要將 JavaScript 物件傳送給伺服器，通常會使用什麼方法將其轉為字串？
<details>
<summary>點擊查看解答</summary>
使用 `JSON.stringify(obj)`。
</details>

#### 📝 5.7 實作練習：Lab 5.7 定義你的個人頁面
**目標：** 操作物件結構。
1. 建立一個包含 `name`, `age`, 與布林值 `isStudent` 的物件代表你自己。
2. 加上一個名為 `skills` 的屬性，裡面放一個陣列 `["HTML", "CSS"]`。
3. 把所有的內容利用字串串接或 Console 完整印出來。

---

## 5.8 檔案物件模型 (DOM) 與事件：讓網頁活起來

📚 [W3Schools 參考：JS HTML DOM](https://www.w3schools.com/js/js_htmldom.asp) | [JS Events](https://www.w3schools.com/js/js_events.asp)

有了以上的 JS 基礎，我們終於準備好去觸摸 HTML 畫面上的標籤了。

### 5.8.1 基礎概念：尋找元素與綁定事件
JavaScript 把整個網頁視作一棵樹，我們稱為 **DOM (Document Object Model)**。
我們可以使用 JS 這個「夾子」去網頁上找出特定按鈕，並在其上安裝「監聽器」(Event Listener)。

```html
<button id="myBtn">點我</button>
<p id="message"></p>

<script>
    // 1. 抓取按鈕元素
    let btn = document.getElementById("myBtn");
    
    // 2. 安裝點擊事件監聽器
    btn.addEventListener("click", () => {
        document.getElementById("message").innerHTML = "你點了按鈕！";
    });
</script>
```

### 5.8.2 實戰應用：旅遊購物車與互動清單
把先前的變數計數器，跟網頁上的結帳按鈕綁在一起，這就是現代電商最核心的「加入購物車」行為！

👉 **[Demo 5.8: DOM 操作與加入購物車](src/js/demo_dom.html)**

#### 📝 5.8 綜合演練：Lab 5.8 旅遊網站購物車介面 (期中統整)
這是一個把陣列、DOM 節點繪製、按鈕事件監聽結合在一起的純前端實戰專案：

👉 **[Lab: 旅遊願望清單完整實作](src/js/lab_travel_booking.html)**

**實作目標：**
1. 練習在畫面上輸入字串，按下按鈕後將字串存入 JS 的陣列中。
2. 每次陣列更新，用 JS 把陣列裡的資料生出成一堆 `<li>` 並插回畫面上。
3. 即時修改畫面右上角的購物車徽章 (`Badge`) 數字。

---

## 參考資源與延伸閱讀
* [MDN Web Docs - JavaScript 指南](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Guide)
* [JavaScript HTML DOM (W3Schools)](https://www.w3schools.com/js/js_htmldom.asp)
* 透過不斷地組合基本的 `if / for / Array`，並呼叫 DOM API 去改變 Tailwind 的排版 class，你就能做出看起來酷炫、且能順暢運作的現代化網頁了！