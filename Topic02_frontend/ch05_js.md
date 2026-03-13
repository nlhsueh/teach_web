Javascript
===

本章將帶領你深入了解 JavaScript，如何讓網頁從靜態的內容轉變為具有互動性的動態應用程式。

## 5.1 JavaScript 基礎

:point_right: [Demo: JS Basics](src/js/demo_basics.html)

### 5.1.1 JS 能做什麼？
* **改變內容**：修改 HTML 的文字或構造。
* **更改屬性**：動態調整圖片來源（src）或連結（href）。
* **控制樣式**：直接修改 CSS 屬性。
* **顯示與隱藏**：控制元素的出現與消失。

### 5.1.2 JS 與 HTML 整合
JavaScript 可以寫在 `<head>` 或 `<body>` 中，或是引用外部檔案。

**內部腳本：**
```html
<script>
    function sayHello() {
        alert("Hello JavaScript!");
    }
</script>
```

**外部引用：**
```html
<script src="main.js"></script>
```

### 5.1.3 輸出方法
* `innerHTML`: 修改 HTML 內容。
* `document.write()`: 用於測試輸出。
* `window.alert()`: 跳出對話框。
* `console.log()`: 開發者工具輸出的除錯利器。

#### 💡 5.1 觀念測驗
1. 想在瀏覽器開發者工具查看變數值，應該用哪個方法？
<details>
<summary>解答</summary>
`console.log()`
</details>

2. `<script src="app.js"></script>` 是哪種引用方式？
<details>
<summary>解答</summary>
外部引用 (External JS)
</details>

#### 📝 5.1 練習題
1. 建立一個按鈕，點擊後會顯示 `alert` 訊息。
2. 使用 `innerHTML` 將一個 `<p>` 標籤的文字改為「你好，JavaScript！」。
3. 在 Console 中印出你的名字並附帶一條訊息。

---

## 5.2 變數、常數與運算元

:point_right: [Demo: Variables & Operators](src/js/demo_vars_ops.html)

### 5.2.1 變數宣告 (var, let, const)
* `let`: 宣告可變變數（推薦使用）。
* `const`: 宣告常數（不可重新賦值）。
* `var`: 舊式的宣告方式（不建議使用）。

```javascript
let count = 10;
const PI = 3.14;
```

### 5.2.2 運算元 (Operators)
包含算術運算 (`+`, `-`, `*`, `/`)、賦值運算 (`=`, `+=`) 與比較運算 (`==`, `===`)。

| 運算元 | 描述 | 範例 |
| :--- | :--- | :--- |
| `===` | 嚴格相等 | `5 === "5"` (false) |
| `++` | 遞增 | `x++` |
| `%` | 取餘數 | `10 % 3` (結果為 1) |

#### 💡 5.2 觀念測驗
1. `let` 與 `const` 的主要差別是什麼？
<details>
<summary>解答</summary>
`let` 宣告後可以重新賦值，而 `const` 的值固定，不可更改。
</details>

2. `10 == "10"` 與 `10 === "10"` 哪個會回傳 true？
<details>
<summary>解答</summary>
`10 == "10"` 為 true (自動轉型)；`10 === "10"` 為 false (嚴格相等，型別不同)。
</details>

#### 📝 5.2 練習題
1. 宣告一個常數存儲半徑，計算圓面積。
2. 使用 `+=` 運算子將變數的值增加 5。
3. 比較兩個變數的大小並將結果輸出至 Console。

---

## 5.3 資料型態與字串處理

:point_right: [Demo: Data Types & Strings](src/js/demo_datatypes.html)

### 5.3.1 基本型態
JavaScript 擁有 8 種資料型態：
* `String`: 文字，如 `"Hello"`。
* `Number`: 數字，如 `123`, `3.14`。
* `Boolean`: 布林值，`true` 或 `false`。
* `Undefined`: 變數已宣告但未給值。
* `Null`: 代表「空」或「無」。
* `Object`: 物件、陣列與日期。

### 5.3.2 字串常用方法
* `slice(start, end)`: 擷取字串片段。
* `toUpperCase()` / `toLowerCase()`: 大小寫轉換。
* `indexOf()`: 尋找子字串位置。
* `parseInt()` / `parseFloat()`: 字串轉數字。

#### 💡 5.3 觀念測驗
1. 如何將字串 `"100"` 轉換為整數？
<details>
<summary>解答</summary>
使用 `parseInt("100")`。
</details>

2. `typeof null` 的回傳值是什麼？
<details>
<summary>解答</summary>
`"object"` (這是 JS 的一個歷史遺留問題)。
</details>

#### 📝 5.3 練習題
1. 撰寫一個功能，接收使用者輸入的名稱，並回傳首字母大寫的版本。
2. 輸入一個包含數字的字串（如 `"3.14"`），將其轉換為浮點數並乘以 2。
3. 判斷一個字串是否包含 `@` 符號（簡單的信箱判定）。

---

## 5.4 流程控制

:point_right: [Demo: Control Flow](src/js/demo_logic.html)

### 5.4.1 條件判斷 (if / switch)
```javascript
if (age >= 18) {
    console.log("成年");
} else {
    console.log("未成年");
}
```

### 5.4.2 迴圈 (for / while)
* `for`: 用於已知次數的迭代。
* `while`: 用於當條件成立時持續執行。

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

#### 💡 5.4 觀念測驗
1. 想要手動跳出迴圈，應該使用哪個關鍵字？
<details>
<summary>解答</summary>
`break`
</details>

2. `if (0)` 會執行嗎？
<details>
<summary>解答</summary>
不會，因為 `0` 在 JavaScript 中被視為 `falsy` (假)。
</details>

#### 📝 5.4 練習題
1. 使用迴圈計算 1 到 100 的總和。
2. 撰寫一個判斷「閏年」的功能。
3. 使用迴圈在頁面上產生一個 9x9 乘法表。

---

## 5.5 函式 (Functions)

:point_right: [Demo: Functions](src/js/demo_functions.html)

### 5.5.1 函式宣告與呼叫
```javascript
function greet(name) {
    return "Hello " + name;
}
console.log(greet("Alice"));
```

### 5.5.2 箭頭函式 (Arrow Functions)
ES6 引入的簡化語法。
```javascript
const add = (a, b) => a + b;
```

#### 💡 5.5 觀念測驗
1. 函式若沒有寫 `return`，會回傳什麼？
<details>
<summary>解答</summary>
`undefined`
</details>

2. 箭頭函式中，如果要回傳一個物件，需要注意什麼？
<details>
<summary>解答</summary>
需要用小括號包住物件，例如 `() => ({ name: 'Alice' })`。
</details>

#### 📝 5.5 練習題
1. 寫一個函式計算矩形面積。
2. 使用箭頭函式將一個溫度數值從攝氏轉為華氏。
3. 寫一個遞迴函式計算階乘 (Factorial)。

---

## 5.6 陣列 (Arrays)

:point_right: [Demo: Arrays](src/js/demo_arrays.html)

### 5.6.1 建立與存取
```javascript
let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]); // Apple
```

### 5.6.2 常用方法
* `push()` / `pop()`: 尾部增減。
* `shift()` / `unshift()`: 頭部增減。
* `splice()`: 刪除或插入。
* `map()` / `filter()`: 迭代與過濾。

#### 💡 5.6 觀念測驗
1. 如何取得陣列的長度？
<details>
<summary>解答</summary>
使用 `array.length` 屬性。
</details>

2. `map()` 方法會改變原本的陣列嗎？
<details>
<summary>解答</summary>
不會，它會回傳一個加工後的新陣列。
</details>

#### 📝 5.6 練習題
1. 建立一個包含 5 個城市的陣列，並用 `forEach` 印出。
2. 使用 `filter` 挑選出陣列中所有大於 50 的數字。
3. 使用 `join` 將陣列 `["HTML", "CSS", "JS"]` 轉為字串 `"HTML-CSS-JS"`。

---

## 5.7 物件 (Objects)

:point_right: [Demo: Objects](src/js/demo_objects.html)

### 5.7.1 物件宣告與 JSON
```javascript
let person = {
    name: "John",
    age: 20,
    greet: function() { return "Hi!"; }
};
```

### 5.7.2 物件遍歷 (for...in)
```javascript
for (let key in person) {
    console.log(key + ": " + person[key]);
}
```

#### 💡 5.7 觀念測驗
1. 如何將一個 JS 物件轉換成 JSON 字串？
<details>
<summary>解答</summary>
使用 `JSON.stringify(obj)`。
</details>

2. 修改物件常數 `const user = { name: 'A' }` 的屬性 `user.name = 'B'` 會報課嗎？
<details>
<summary>解答</summary>
不會，`const` 指的是「參考」不可變，物件內容是可以修改的。
</details>

#### 📝 5.7 練習題
1. 建立一個物件代表「手機」，包含品牌、型號與價格。
2. 撰寫一個功能，將物件陣列依據其中的「價格」屬性從小到大排序。
3. 使用 `Object.keys()` 取得並印出物件的所有鍵值。

---

## 5.8 檔案物件模型 (DOM)

:point_right: [Demo: DOM Manipulation](src/js/demo_dom.html)

### 5.8.1 選取與操作
* `document.getElementById()`: 根據 ID 選取。
* `textContent` / `innerHTML`: 更改文字或構造。
* `style.property`: 更改 CSS 樣式。

### 5.8.2 事件監聽 (Events)
```javascript
let btn = document.querySelector("button");
btn.addEventListener("click", () => {
    alert("Clicked!");
});
```

#### 💡 5.8 觀念測驗
1. 想在使用者輸入完畢按下鍵盤時觸發事件，應監聽哪個事件？
<details>
<summary>解答</summary>
`keyup` 或 `keydown`。
</details>

2. `querySelector` 與 `getElementById` 的主要差別？
<details>
<summary>解答</summary>
`querySelector` 使用 CSS 選擇器語法，彈性較大；`getElementById` 專門找 ID，效能稍好。
</details>

#### 📝 5.8 練習題
1. 點擊按鈕後，切換頁面背景顏色。
2. 建立一個輸入框，當字數超過 10 個字時，邊框變紅。
3. 動態建立一個 `<li>` 並加入到現有的 `<ul>` 清單中。

---

## 參考資源
* [W3Schools JavaScript Tutorial](https://www.w3schools.com/js/)
* [MDN Web Docs - JavaScript](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript)