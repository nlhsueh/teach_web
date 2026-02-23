###### tags: `Web`

Javascript
===

:::success
學習重點
* 了解 JS 能做什麼
* 了解 JS 與 HTML 的基礎整合應用
* 了解並應用 JS 基本的程式語法，包含
* 了解陣列、物件、類別的差異與應用
* 了解函式及其各種寫法
* 了解 JS 與 HTML 的進階應用 - DOM 物件操作
:::

## 4.0 Slides

:point_right: [nlh slides- javascript](https://docs.google.com/presentation/d/1JMaa9aSBGomS85OtSDdcQZlwuajNgdmKFtrb3WR-nSI/edit?usp=sharing)
* Basic
* Number and String
* Array
* Object
* Iterator
* DOM

:point_right: [W3school- javascript](
https://www.w3schools.com/js/default.asp)

:point_right: [nlh GitHub www-js](https://github.com/nlhsueh/www-js)
* CSS demo
* **Javascript demo**
* Bootstrap demo


## 4.1 基礎

#### JS 能做什麼？
* JavaScript 可以改變 HTML 內容
* JavaScript 可以更改 HTML 屬性值
* JavaScript 可以更改 HTML 樣式 (CSS)
* JavaScript 可以隱藏 HTML 元素
* JavaScript 可以顯示 HTML 元素


#### JS 與 HTML

HTML 裏面
```javascript
<head>
   <script>
       function myFunction() {
 	    ...
 }
   </script>
</head>
<body>
   <h2>Demo JavaScript in Head</h2>

   <p id="demo">A Paragraph</p>
   <button type="button" onclick="myFunction()">Try it</button>

</body>

```

#### HTML 外部引用 JS 

```javascript
<script src="myScript.js"></script>
```

> 輸出

```javascript
innerHTML         // 修改 HTML 元件內容 (常用)
document.write()  // 輸出 HTML 文件 (通常測試用)
window.alert()    // 跳出來的警訊
console.log()     // 寫到瀏覽器的 console (debug用)
````

### [變數](https://www.w3schools.com/js/js_variables.asp)

在 JavaScript 中，您可以使用以下方式來宣告變數：

> 使用 `var` 關鍵字（ES5 之前）
```javascript
var x = 10;
```

> 使用 `let` 關鍵字（推薦，ES6+）
```javascript
let y = 20;
```

> 使用 `const` 關鍵字（用於宣告常數）
```javascript
const PI = 3.14;
```

> 變數命名規則：

1. 變數名稱必須以字母、底線（_）或美元符號（$）開頭。
2. 變數名稱可以包含字母、數字、底線和美元符號。
3. 變數名稱區分大小寫，例如 `myVar` 和 `MyVar` 是不同的變數。
4. 變數名稱不應該使用 JavaScript 保留字或關鍵字，例如 `let`、`const`、`var` 等。
5. 命名慣例通常是使用駝峰命名法（camelCase），例如 `myVariableName`。
6. 變數名稱應該具有描述性，以便他人閱讀程式碼時易於理解。

> 正確的變數命名範例：

```javascript
let firstName = "John";
let lastName = "Doe";
let userAge = 30;
let totalAmount = 100.50;
```

> 不良的變數命名範例：

```javascript
let x1 = 10; // 不具描述性的名稱
let $value = 20; // 使用美元符號開頭，通常應保留給程式庫使用
let 123abc = "Hello"; // 變數名稱不能以數字開頭
let var = 5; // 使用 JavaScript 保留字作為變數名稱
```

遵循這些變數命名規則和慣例將有助於編寫更清晰、易讀且易於維護的程式碼。

#### 常數
宣告 const 就一定要給值，而且不能在變更

```javascript
const PI = 3.141592653589793;
PI = 3.14; //ERROR
```

正確說法：固定參考 (constant reference)
可改變 物件/陣列 內的元素值

```javascript
const cars = ["Saab", "Volvo", "BMW"];
cars[0] = "Toyota";         //OK
cars.push("Audi");          //OK
cars = ["Toyota", "Volvo"]; //ERROR

const car = { model: "500", color: "white" };
car.color = "red";          //OK
```

### [運算元](https://www.w3schools.com/js/js_operators.asp)

以下是針對 JavaScript 中的各種 operator 的介紹，以 markdown 表格的方式呈現：

| Operator     | 描述           | 範例                                                                              |
| ------------ | -------------- | --------------------------------------------------------------------------------- |
| `+`          | 加法           | `a + b` 返回 `a` 和 `b` 的和                                                      |
| `-`          | 減法           | `a - b` 返回 `a` 減去 `b` 的差                                                    |
| `*`          | 乘法           | `a * b` 返回 `a` 和 `b` 的乘積                                                    |
| `/`          | 除法           | `a / b` 返回 `a` 除以 `b` 的商                                                    |
| `%`          | 取餘數         | `a % b` 返回 `a` 除以 `b` 的餘數                                                  |
| `++`         | 遞增           | `a++` 或 `++a` 將 `a` 的值增加 1                                                  |
| `--`         | 遞減           | `a--` 或 `--a` 將 `a` 的值減少 1                                                  |
| `=`          | 賦值           | `a = b` 將 `b` 的值賦給 `a`                                                       |
| `+=`         | 加法賦值       | `a += b` 相當於 `a = a + b`                                                       |
| `-=`         | 減法賦值       | `a -= b` 相當於 `a = a - b`                                                       |
| `*=`         | 乘法賦值       | `a *= b` 相當於 `a = a * b`                                                       |
| `/=`         | 除法賦值       | `a /= b` 相當於 `a = a / b`                                                       |
| `%=`         | 取餘數賦值     | `a %= b` 相當於 `a = a % b`                                                       |
| `==`         | 相等比較       | `a == b` 檢查 `a` 是否等於 `b`                                                    |
| `===`        | 嚴格相等比較   | `a === b` 檢查 `a` 是否等於 `b` 且類型相同                                        |
| `!=`         | 不相等比較     | `a != b` 檢查 `a` 是否不等於 `b`                                                  |
| `!==`        | 嚴格不相等比較 | `a !== b` 檢查 `a` 是否不等於 `b` 或類型不同                                      |
| `>`          | 大於比較       | `a > b` 檢查 `a` 是否大於 `b`                                                     |
| `<`          | 小於比較       | `a < b` 檢查 `a` 是否小於 `b`                                                     |
| `>=`         | 大於等於比較   | `a >= b` 檢查 `a` 是否大於或等於 `b`                                              |
| `<=`         | 小於等於比較   | `a <= b` 檢查 `a` 是否小於或等於 `b`                                              |
| `&&`         | 邏輯與         | `a && b` 如果 `a` 和 `b` 都為真則返回真                                           |
| `\|\|`       | 邏輯或         | `a \|\| b` 如果 `a` 或 `b` 任一為真則返回真                                       |
| `!`          | 邏輯非         | `!a` 如果 `a` 為假則返回真，否則返回假                                            |
| `? :`        | 條件運算符     | `condition ? expr1 : expr2` 如果 `condition` 為真則返回 `expr1`，否則返回 `expr2` |
| `typeof`     | 類型運算符     | `typeof variable` 返回 `variable` 的類型                                          |
| `instanceof` | 實例運算符     | `object instanceof type` 檢查 `object` 是否屬於 `type` 的實例                     |

這些是 JavaScript 中最常用的 operator，它們用於執行各種算術、比較和邏輯操作。


### [資料型態](https://www.w3schools.com/js/js_datatypes.asp)

JavaScript has 8 Datatypes
* String: `"abc"`   `'abc'`
* Number: `123`   `123.45`
* Boolean: `true`   `false`
* Bigint
* Undefined: 已宣告未給值
* Null: `null`
* Symbol
* Object

The Object Datatype
* An object
* An array
* A date

```javascript
// Numbers:
let length = 16;
let weight = 7.5;

// Strings:
let color = "Yellow";
let lastName = "Johnson";

// Booleans
let x = true;
let y = false;

// Object:
const person = {firstName:"John", lastName:"Doe"};

// Array object:
const cars = ["Saab", "Volvo", "BMW"];

// Date object:
const date = new Date("2022-03-25");
```


### 字串

以下是 JavaScript 中常用的字串方法，包括 `slice`：

* `slice(startIndex, endIndex)`
從字串中提取指定範圍的字符，並返回一個新的字串。`startIndex` 是起始索引（包含），`endIndex` 是結束索引（不包含）。

```javascript
let str = "Hello, world!";
let slicedStr = str.slice(0, 5); // 提取從索引 0 到索引 5 之間的字符（不包括索引 5）
console.log(slicedStr); // 輸出："Hello"
```

* `substring(startIndex, endIndex)`
與 `slice` 方法類似，但是 `substring` 不接受負數作為索引，並且當 `startIndex` 大於 `endIndex` 時，會自動交換這兩個值。

```javascript
let str = "Hello, world!";
let subStr = str.substring(7, 12); // 提取從索引 7 到索引 12 之間的字符
console.log(subStr); // 輸出："world"
```

* `substr(startIndex, length)`
從指定的起始索引開始，提取指定長度的字符。

```javascript
let str = "Hello, world!";
let substr = str.substr(7, 5); // 從索引 7 開始，提取 5 個字符
console.log(substr); // 輸出："world"
```

* `charAt(index)`
返回給定索引處的字符。

```javascript
let str = "Hello, world!";
let char = str.charAt(1); // 返回索引為 1 的字符
console.log(char); // 輸出："e"
```

* `indexOf(searchValue, startIndex)`
返回指定字符或子字串第一次出現的索引。可選的 `startIndex` 參數表示開始搜索的位置。

```javascript
let str = "Hello, world!";
let index = str.indexOf("world"); // 查找 "world" 第一次出現的位置
console.log(index); // 輸出：7
```

* `toUpperCase()` 將字串轉換為大寫。

```javascript
let str = "hello";
let upperStr = str.toUpperCase();
console.log(upperStr); // 輸出："HELLO"
```
* `toLowerCase()` 將字串轉換為小寫。

```javascript
let str = "HELLO";
let lowerStr = str.toLowerCase();
console.log(lowerStr); // 輸出："hello"
```

#### 字串轉換

> 字串轉換為數字
您可以使用兩種方法將字串轉換為數字：`parseInt()` 和 `parseFloat()`。
- `parseInt()`: 將字串轉換為整數。
- `parseFloat()`: 將字串轉換為浮點數。

```javascript
let strNumber = "123";
let intNumber = parseInt(strNumber); // 將字串轉換為整數
console.log(intNumber); // 輸出：123

let strFloat = "3.14";
let floatNumber = parseFloat(strFloat); // 將字串轉換為浮點數
console.log(floatNumber); // 輸出：3.14
```

> 數字轉換為字串

您可以使用 `toString()` 方法將數字轉換為字串。

```javascript
let number = 123;
let strNumber = number.toString(); // 將數字轉換為字串
console.log(strNumber); // 輸出："123"
```


### 測驗題 (test4.1)

1. 以下哪個變數宣告方式可以讓變數的值無法重新賦值？  
A) `var`  
B) `let`  
C) `const`  
D) `function`  

2. 以下哪個運算結果為 `true`？  
A) `0 == false`  
B) `null === undefined`  
C) `"5" + 5 === 10`  
D) `NaN == NaN`  

3. JavaScript 中哪個資料型態可以存放多種不同類型的值？  
A) `String`  
B) `Boolean`  
C) `Array`  
D) `Number`  

4. 以下哪個選項正確表示 JavaScript 的 `typeof` 運算？  
A) `typeof null` 回傳 `"null"`  
B) `typeof []` 回傳 `"array"`  
C) `typeof 42` 回傳 `"number"`  
D) `typeof function() {}` 回傳 `"method"`  

5. 關於 JavaScript 字串處理，以下哪個方法可以將 `"Hello World"` 轉為全小寫？  
A) `toUpperCase()`  
B) `toLowerCase()`  
C) `trim()`  
D) `slice()`  

6. 以下哪個選項可以正確取得字串 `"JavaScript"` 中索引 `4` 的字元？  
A) `"JavaScript".charAt(4)`  
B) `"JavaScript"[4]`  
C) `"JavaScript".substring(4,5)`  
D) 以上皆正確  

---

解答：
1. **C)** `const`  
2. **A)** `0 == false`（因為 `==` 會進行類型轉換）  
3. **C)** `Array`  
4. **C)** `typeof 42` 回傳 `"number"`  
5. **B)** `toLowerCase()`  
6. **D)** 以上皆正確


### 練習題 (lab4.1)

:::success
:basketball: 3.1.1 乘法除法 

輸入兩個輸字，選擇乘法或除法的按鈕，輸出結果 (小數點下兩位）。
:::

- 輸入：應用 form-> input 進行輸入; `document.getElementById()` 來取得值
- 輸出：應用 `console.log` 來做輸出
- 小數點下兩位：`num.toFix(2)` 


:::success
:basketball: lab4.1.01 三角形面積

輸入三個邊長，判斷是否 (1) 符合三角形規範 (2) 正三角形 (3) 等腰三角形。
:::

- 輸入：應用 form-> input 進行輸入; `document.getElementById().value` 來取得值
- 進階：宣告一個二維陣列，放一群三邊長，迴圈式的讀取與判斷
- 輸出：應用 `document.getElementById()` 做輸出
- JS logic 判斷

:::success
:basketball: lab4.1.02 費柏納西

輸入一個數字，求 Fibonacci 的值。
:::
- JS while 判斷
- or JS 遞迴呼叫

:::success
:basketball: lab4.1.03 質數一 

輸入一個數字，回傳是否為質數。
:::
- JS 邏輯判斷
- break

:::success
:basketball: lab4.1.04 質數二 

輸入一個數字，列出所有不大於此數的質數。
:::
- 雙層迴圈
- 邏輯判斷
- break

:::success
:basketball: lab4.1.05 字串環

寫一個程式，每按一下 button 第一個字符就會跑到該字串的最後面。
:::
- 字串處理
- IECS FCU => ECS FCUI => CS FCUIE => …
- str.slice() or str.substr()


:::success
:basketball: lab4.1.06 猜數字 

系統產生一個 1-100 的隨意整數，使用者猜，提示太高或太低。猜出後提示共猜了幾次。
:::
- logic
- Math.random() 會會傳 [0..1) 的小數


:::success
:basketball: lab4.1.07 副檔名 

輸入一個檔名，輸出副檔名名稱。例如 memberList.txt ⇒ txt
:::
- 字串處理


## 4.2 陣列 

在 JavaScript 中，**陣列（Array）** 是一種特殊的物件，可用來儲存**多個值**。它們可以包含不同類型的數據，例如數字、字串、物件甚至其他陣列。  

### **建立陣列的方法**
```javascript
// 方法 1: 使用中括號 []
let numbers = [10, 20, 30, 40];

// 方法 2: 使用 new Array()
let fruits = new Array("Apple", "Banana", "Cherry");

// 方法 3: 建立空陣列後再賦值
let colors = [];
colors[0] = "Red";
colors[1] = "Green";
colors[2] = "Blue";
```

### **存取陣列元素**
陣列的索引（index）從 `0` 開始：
```javascript
let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]); // Apple
console.log(fruits[1]); // Banana
console.log(fruits[2]); // Cherry
```

### **修改陣列元素**
```javascript
let fruits = ["Apple", "Banana", "Cherry"];
fruits[1] = "Orange"; // 將 Banana 改為 Orange
console.log(fruits); // ["Apple", "Orange", "Cherry"]
```

---

### 陣列的常見方法

#### 新增與移除元素

**push() - 在陣列尾部新增元素**
```javascript
let arr = [1, 2, 3];
arr.push(4); 
console.log(arr); // [1, 2, 3, 4]
```

**pop() - 移除陣列尾部元素**
```javascript
let arr = [1, 2, 3];
let lastElement = arr.pop();
console.log(arr); // [1, 2]
console.log(lastElement); // 3
```

**unshift() - 在陣列前端新增元素**
```javascript
let arr = [1, 2, 3];
arr.unshift(0);
console.log(arr); // [0, 1, 2, 3]
```

**shift() - 移除陣列前端元素**
```javascript
let arr = [1, 2, 3];
let firstElement = arr.shift();
console.log(arr); // [2, 3]
console.log(firstElement); // 1
```

---

#### 修改與切割

**splice() - 插入、刪除或替換**
語法：`arr.splice(起始索引, 刪除個數, 插入值1, 插入值2, ...)`
```javascript
let arr = ["A", "B", "C", "D"];
arr.splice(1, 2, "X", "Y"); 
console.log(arr); // ["A", "X", "Y", "D"]
```

**slice() - 擷取陣列的一部分（不影響原陣列）**
```javascript
let arr = ["A", "B", "C", "D"];
let newArr = arr.slice(1, 3); 
console.log(newArr); // ["B", "C"]
console.log(arr); // ["A", "B", "C", "D"]
```

---

#### 陣列搜尋

**indexOf() - 找出元素的索引**
```javascript
let arr = ["Apple", "Banana", "Cherry"];
console.log(arr.indexOf("Banana")); // 1
console.log(arr.indexOf("Mango")); // -1 （找不到）
```

**includes() - 判斷是否包含某個元素**
```javascript
let arr = ["Apple", "Banana", "Cherry"];
console.log(arr.includes("Banana")); // true
console.log(arr.includes("Mango")); // false
```

---

#### 陣列轉換
**join() - 陣列轉字串**
```javascript
let arr = ["Apple", "Banana", "Cherry"];
console.log(arr.join(", ")); // "Apple, Banana, Cherry"
```

**split() - 字串轉陣列**
```javascript
let str = "Red-Blue-Green";
let arr = str.split("-");
console.log(arr); // ["Red", "Blue", "Green"]
```

---

### 陣列的高階方法
#### map() - 產生新陣列
```javascript
let numbers = [1, 2, 3, 4];
let doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6, 8]
```

#### filter() - 過濾符合條件的元素
```javascript
let numbers = [1, 2, 3, 4, 5];
let evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2, 4]
```

#### reduce() - 累加陣列數值
```javascript
let numbers = [1, 2, 3, 4];
let sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum); // 10
```

---

### 陣列的迴圈
#### forEach() - 遍歷陣列
```javascript
let fruits = ["Apple", "Banana", "Cherry"];
fruits.forEach(fruit => console.log(fruit));
/*
Apple
Banana
Cherry
*/
```

#### for...of 迴圈
```javascript
let colors = ["Red", "Green", "Blue"];
for (let color of colors) {
    console.log(color);
}
/*
Red
Green
Blue
*/
```

---


### 測驗題 test4.2

1. 以下哪個方法可以用來新增元素到陣列的 **最後一個位置**？  
A) `push()`  
B) `unshift()`  
C) `pop()`  
D) `shift()`  

2. 若有以下程式碼，執行後 `arr` 的內容為何？  
```javascript
let arr = [1, 2, 3];
arr.pop();
```
A) `[1, 2]`  
B) `[1, 2, 3, undefined]`  
C) `[2, 3]`  
D) `[1, 3]`  

3. `splice()` 方法的主要功能是什麼？  
A) 刪除陣列中指定範圍的元素，並可選擇性插入新元素  
B) 回傳新陣列，不影響原陣列  
C) 只用來替換陣列內的元素  
D) 只會刪除最後一個元素  

4. 關於 `map()` 方法，以下哪個敘述是正確的？  
A) `map()` 會修改原陣列的內容  
B) `map()` 會回傳一個新的陣列，並對每個元素應用指定函式  
C) `map()` 只適用於數字陣列  
D) `map()` 會回傳 `undefined`  

5. 以下哪個方法可以合併兩個陣列並回傳新的陣列？  
A) `concat()`  
B) `join()`  
C) `slice()`  
D) `split()`  

---

解答
1. A `push()`（在陣列最後新增元素）  
2. A `[1, 2]`（`pop()` 會移除最後一個元素）  
3. A `splice()`（可刪除、插入或替換陣列元素）  
4. B `map()`（回傳新陣列並對每個元素應用函式）  
5. A `concat()`（用來合併陣列）  


### 練習題 lab4.2

:::success
:basketball: lab4.2.01 解析字串1

`"eng:20;phy:90;math:100"`。請透過 split 先以`;`形成一個陣列，再以 `:`切割，最終形成一個二維陣列。注意數字的部分要轉為整數型態。使用者要求輸入科目名稱，系統輸出此科目的分數
:::
Hint:

```javascript
// 先分割 ; 再分割 : 
str.split(";") 
str.split(":")
```

:::success
:basketball: lab4.2.02 星期幾

2021/1/1 是星期五，輸入月份和日期（一樣是2021年），輸出是星期幾。請用一個陣列記錄每個月的天數，並應用之。
:::
- logic
- array

:::success
:basketball: lab4.2.03 成績

有一個二維陣列 grade，儲存 三個人三科的成績（請隨機產生）; 一個一維陣列 names 儲存三個人的姓名; 一個一維陣列儲存三科的名稱。請算出 (1)  各科平均 (2) 每個人的平均 (3) 各科最高分予該學生姓名。
:::
- random generation
- 二維陣列
- 邏輯判斷

:::success
:basketball: lab4.2.04 溫度 

一個陣列儲存一群溫度，請使用 short function (=>) 做一個攝氏轉華氏溫度的功能，輸出到另一個陣列，並印出。
:::
- function
- array map function

:::success
:basketball: lab4.2.04 平方和

一個陣列儲存一群數字，透過 forEach() 回傳此平方和。`dis = [12, 13, 14] ⇒ (12**2 + 13**2 + 14**2)`
:::
- forEach, map function


:::success
:basketball: lab4.2.05 信箱 

輸入一個信箱，輸出是否為合格的信箱。nlhsueh@gmail ⇒ 合格。nlhsueh.gmail.com ⇒ 錯誤。
:::
- 字串處理
- reg expression

## 4.3 物件

在 JavaScript 中，**物件（Object）** 是一種儲存鍵值對（key-value pairs）的資料結構。它類似於 Python 的字典（dictionary）或 JSON 格式，允許使用 `key` 來存取對應的 `value`。  

#### 建立物件的方法
```javascript
// 方法 1: 物件字面值（Object Literal）
let person = {
    name: "Alice",
    age: 25,
    isStudent: false
};

// 方法 2: 使用 new Object()
let car = new Object();
car.brand = "Toyota";
car.year = 2022;

// 方法 3: 物件建構函式（Constructor Function）
function Animal(type, legs) {
    this.type = type;
    this.legs = legs;
}
let dog = new Animal("Mammal", 4);

// 方法 4: 使用 Object.create()（建立原型繼承物件）
let baseObject = { greet: "Hello" };
let newObject = Object.create(baseObject);
console.log(newObject.greet); // Hello
```

---

###  存取與修改物件屬性
#### 存取屬性
```javascript
let person = {
    name: "Alice",
    age: 25
};

// 點記法（Dot Notation）
console.log(person.name); // Alice

// 中括號記法（Bracket Notation）
console.log(person["age"]); // 25
```

#### 修改屬性
```javascript
person.age = 26;
person["name"] = "Bob";
console.log(person); // { name: "Bob", age: 26 }
```

#### 新增屬性
```javascript
person.city = "New York";
console.log(person); // { name: "Bob", age: 26, city: "New York" }
```

#### 刪除屬性
```javascript
delete person.age;
console.log(person); // { name: "Bob", city: "New York" }
```

---

### 物件方法
物件中的函式（Function）稱為 **方法（Method）**。

#### 定義物件方法
```javascript
let person = {
    name: "Alice",
    greet: function() {
        return `Hello, my name is ${this.name}.`;
    }
};

console.log(person.greet()); // Hello, my name is Alice.
```

#### ES6 簡化寫法
```javascript
let person = {
    name: "Alice",
    greet() {  // 省略 `function` 關鍵字
        return `Hello, my name is ${this.name}.`;
    }
};
console.log(person.greet()); // Hello, my name is Alice.
```

---

###  迭代物件
JavaScript 物件沒有索引（不像陣列），但可以透過 `for...in` 來遍歷屬性。

#### `for...in` 迴圈
```javascript
let person = {
    name: "Alice",
    age: 25,
    city: "New York"
};

for (let key in person) {
    console.log(`${key}: ${person[key]}`);
}
/*
輸出：
name: Alice
age: 25
city: New York
*/
```

---

### 物件的方法與應用
#### 取得物件的所有鍵、值、鍵值對
```javascript
let person = {
    name: "Alice",
    age: 25,
    city: "New York"
};

console.log(Object.keys(person));   // ["name", "age", "city"]
console.log(Object.values(person)); // ["Alice", 25, "New York"]
console.log(Object.entries(person)); 
// [["name", "Alice"], ["age", 25], ["city", "New York"]]
```

#### 檢查物件是否有某個屬性
```javascript
console.log(person.hasOwnProperty("age")); // true
console.log("city" in person); // true
console.log("gender" in person); // false
```

---

### 物件的淺拷貝與深拷貝
#### 淺拷貝（Shallow Copy）
淺拷貝只複製第一層，內部的巢狀物件仍指向原本的記憶體位置。

```javascript
let obj1 = { name: "Alice", age: 25 };
let obj2 = Object.assign({}, obj1); // 或 let obj2 = { ...obj1 };

obj2.age = 30;
console.log(obj1.age); // 25
console.log(obj2.age); // 30
```

#### 深拷貝（Deep Copy）
使用 `JSON.parse(JSON.stringify())` 或 `structuredClone()`（適用於新瀏覽器）。

```javascript
let obj1 = { name: "Alice", details: { city: "NY" } };
let obj2 = JSON.parse(JSON.stringify(obj1));

obj2.details.city = "LA";
console.log(obj1.details.city); // "NY"
console.log(obj2.details.city); // "LA"
```

---

### 物件與 JSON
JavaScript 物件與 JSON（JavaScript Object Notation）格式類似，但 JSON 是純文字格式，必須用 `JSON.stringify()` 和 `JSON.parse()` 來轉換。

#### 物件轉 JSON
```javascript
let person = { name: "Alice", age: 25 };
let jsonString = JSON.stringify(person);
console.log(jsonString); // '{"name":"Alice","age":25}'
```

#### JSON 轉回物件
```javascript
let newPerson = JSON.parse(jsonString);
console.log(newPerson); // { name: "Alice", age: 25 }
```

---

### 物件的應用範例
#### 陣列中的物件
```javascript
let users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" },
    { id: 3, name: "Charlie" }
];

let userNames = users.map(user => user.name);
console.log(userNames); // ["Alice", "Bob", "Charlie"]
```

#### 根據屬性篩選物件
```javascript
let adults = users.filter(user => user.id > 1);
console.log(adults); // [{ id: 2, name: "Bob" }, { id: 3, name: "Charlie" }]
```

#### 物件陣列排序
```javascript
let products = [
    { name: "Laptop", price: 1200 },
    { name: "Phone", price: 800 },
    { name: "Tablet", price: 600 }
];

products.sort((a, b) => a.price - b.price);
console.log(products); 
// [
//   { name: "Tablet", price: 600 },
//   { name: "Phone", price: 800 },
//   { name: "Laptop", price: 1200 }
// ]
```

### 測驗題 (test4.3)

1. 哪一個語法正確地建立一個 JavaScript 物件？

A) `let obj = object();`  
B) `let obj = new Object[];`  
C) `let obj = { name: "Alice", age: 25 };`  
D) `let obj = (name = "Alice", age = 25);`


2. 關於 JavaScript 中物件的屬性（properties），下列何者敘述錯誤？

A) 物件的屬性可以用點記號（dot notation）存取  
B) 屬性名稱只能是字串  
C) 屬性可以是函式  
D) 可以用中括號（bracket notation）動態存取屬性

3. 假設有以下物件：

```javascript
let person = {
  name: "John",
  age: 30
};
```

哪一種方式可以正確新增一個 `gender` 屬性並設定為 `"male"`？

A) `person.gender = "male";`  
B) `person["gender"] = "male";`  
C) `person->gender = "male";`  
D) 以上皆可

4. 關於 JavaScript 中物件的參照行為（reference behavior），下列哪一項是正確的？

A) 物件是以值傳遞（pass by value）的方式傳遞  
B) 兩個物件內容相同就是同一個物件  
C) 物件是以參照（reference）傳遞的  
D) 物件不能被指定給另一個變數

5. 使用 `for...in` 迴圈可以做什麼？

A) 遍歷陣列中的每一個元素  
B) 遍歷物件的每一個方法  
C) 遍歷物件的每一個鍵（key）  
D) 遍歷物件的每一個值（value）


**解答**
1. C  
2. B （屬性名稱可以是 Symbol，不一定是字串）  
3. A 和 B 都可以 → 正確答案為 **D 錯誤**，**應為 "A) 和 B)" 這類選項設計**，這題應改選項以避免誤導  
4. C  
5. C

### 練習題 (lab4.3)

:::success 
:basketball: lab03.01 解析字串

使用物件陣列儲存三個人的三科成績資料 (math, phy, eng)。透過程式計算出 (1) 各科的平均 (2) 每個人的平均。
:::

:::success
:basketball: lab03.02 過濾人口

使用 array.filter 挑選出人口小於 300 萬的都市

```javascript    
let cities = [
    {name: 'Los Angeles', population: 3792621},
    {name: 'New York', population: 8175133},
    {name: 'Chicago', population: 2695598},
    {name: 'Houston', population: 2099451},
    {name: 'Philadelphia', population: 1526006}
];
```

Hint
- Object
- array filter function

:::


:::success
:basketball: lab03.03 排序人口

同上，使用 filter, sort, map 印出人口小於 300 萬，由人口少到多排序印出 都市名與人口數。
:::

## 4.4 文件物件模型 DOM

**DOM（Document Object Model）** 是一種用來表示 HTML 或 XML 文件的 **樹狀資料結構**，它把整份網頁看成是一個由節點（nodes）組成的樹。

簡單來說：

> **HTML 文件會被瀏覽器轉換成一棵樹狀結構，我們可以透過 JavaScript 來存取、修改、刪除這棵樹的內容。**

[W3School DOM](https://www.w3schools.com/js/js_htmldom.asp)

### DOM 的結構

舉個例子：

```html
<html>
  <body>
    <h1>Hello</h1>
    <p>World</p>
  </body>
</html>
```

這會被轉換成一棵類似這樣的 DOM 樹：

```
document
 └── html
     └── body
         ├── h1
         └── p
```

---

### 常見的 DOM 操作

#### 1. **取得元素**
```js
document.getElementById("myDiv");
document.querySelector(".myClass");
document.getElementsByTagName("p");
```

#### 2. **修改內容**
```js
let el = document.getElementById("title");
el.textContent = "新的標題";
```

#### 3. **修改屬性**
```js
el.setAttribute("class", "highlight");
```

#### 4. **修改樣式**
```js
el.style.color = "red";
```

#### 5. **新增或刪除元素**
```js
let newP = document.createElement("p");
newP.textContent = "新增段落";
document.body.appendChild(newP);

let oldP = document.querySelector("p");
oldP.remove();
```

#### 6. **加入事件處理**
```js
let btn = document.getElementById("clickMe");
btn.addEventListener("click", function() {
  alert("你點了按鈕！");
});
```

---

### DOM 的應用場景

| 場景         | 說明                                              |
| ------------ | ------------------------------------------------- |
| 表單驗證     | 檢查使用者輸入是否正確，並即時顯示錯誤訊息。      |
| 動態內容     | 依據使用者動作，新增/修改頁面上的內容。           |
| 製作互動效果 | 點擊按鈕展開/收合區塊、切換主題、表單即時回饋等。 |
| 製作簡單動畫 | 配合 CSS 做動畫切換（ex: 顯示/隱藏、淡入淡出）。  |


### 小結

- DOM 是 JavaScript 操作 HTML 文件的橋樑。
- 所有的 HTML 元素都可以透過 DOM 存取並操作。
- 常見操作包括：查找元素、修改內容、設定屬性、加事件、創建/刪除元素。
- DOM 操作讓網頁能夠具有互動性與動態更新的能力。

---

如果你想要範例練習題、互動範例或教學簡報版本，也可以跟我說，我可以幫你補充！

### 測驗題 (test4.4)

### 練習題 (lab4.4)
:::success
:basketball: lab04.01 身分證

設計一個 HTML可以輸入身分證與 email。(1) 當按下 提交 時會檢查身分證是否正確 (2) 切換到 email 時也會檢查身分證。
:::
- onclick(), onchange()
- 字串處理: 身分證第一碼為英文 a-z or A-Z; 第二碼 1 or 2, 其餘為數字


:::success
:basketball: lab04.02 平均與最高的 

設計一個 form 讓我們輸入姓名和三個科目的成績。按下「添增」後欄位會清掉，下方出現剛剛輸入的資料。按下「最高分」會呈現最高分者的資料。按下「平均」會呈現每個人的平均分數。
:::


## 4.5 綜合練習

### 4.Ex01
:::success

:basketball: :basketball: :basketball: BMI Example
* 設計一個介面可以輸入多個人的身高體重。可以點選統計按鈕，依據BMI 正常、過重、過低分類列出人的資訊。可以點選輸入返回輸入介面。

<img src="https://hackmd.io/_uploads/SJKYSr8yC.png" width=400>

<img src="https://hackmd.io/_uploads/SJHiBBL10.png" width=400>


:::


### 4.Ex02
:::success
:basketball: 重複檢查

新增人員體重時，如果名字一樣表示體重的變化，就會呈現出 xxx 的體重由 yyy 變成 zzz; BMI 也從 ppp 變成 qqq 的訊息。
:::


### 4.Ex03
:::success
:basketball: 運動去

擴充上面的應用，新增一個運動的 button, 每次運動後就會減重，重新計算 bmi 後呈現

- (a) 每次運動就會減 0.1kg
- (b) 可以選擇運動，例如瑜伽就減 0.1kg, 打籃球就減 0.2kg
:::

---

### 4.Ex04

:::success
:football: 加碼券

一、加碼券開獎 HTML 版 (35%)
如下方加碼券的畫面，請以 HTML/CSS 設計該畫面，並進行以下修改：
* 移除「點一下開獎囉」按鈕，直接呈現獎項內容。
* 標題和獎項內容整體風格置中左右有 margin，獎項條列仍為置左。
* 獎項名稱（如國旅券）的字體稍大，顏色改為藍色。
* 游標移到號碼（例如21) 時，底色會變成黃底。
* （資料如第二題，可取用使用）

二：修改以下的程式碼，點擊後會出現如下的畫面 (35%)

<img src=https://hackmd.io/_uploads/S1ADG2WNp.png width=500>

三、加碼券開獎圖片版 (35%)
* 圖片可由 [這裡](https://drive.google.com/drive/folders/1Gd9Gt1jdhg7e_xUW_ubzoPK42ON7VP-W?usp=sharing) 取得
* 請使用 HTML/CSS 排版以完成下方畫面
* 亦可修改第二題 JS code 完成

<img src=https://hackmd.io/_uploads/B1O90hbVp.png width=500>


```javascript
<!DOCTYPE html>

<head>
<script>
let winNo1 = {
  "domesticTravel": ["21", "32", "98", "67", "97", "410"],
  "iYuan": ["64", "85"],
  "agriculture": ["89", "32", "54", "597", "453", "152"],
  "artFunE": ["96", "15", "07", "30", "73", "98", "19", "11"],
  "artFunP": ["39", "37", "23", "36", "79", "08", "14", "75"],
  "sports": ["97", "13", "19", "55", "71", "93", "381", "734", "644",   "453", "985"],
  "hakka": ["81", "900"],
  "rgionalRevitalization": ["081", "105", "594", "188", "089", "396", "521", "467", "912", "798", "358", "441", "367", "941", "335"]
};

let name_mapping = {
   "domesticTravel": "國旅劵",
   "iYuan": "i 原劵",
   "agriculture": "農遊劵",
   "artFunE": "藝Fun劵 數位",
   "artFunP": "旅遊劵 紙本",
   "sports": "動滋劵",
   "hakka": "客庄劵",
   "rgionalRevitalization": "地方創生劵"
};

function show() {
    let s = "<ul>";




    document.getElementById("#result").innerHTML = s;
}
</script>
</head>

<body>
   <h1> 加碼劵開獎 </h1>
   <input type="button" value="點一下開獎囉" onclick="show()">
   <div id="#result"></div>
</body>
```
:::

Sol-2 Hint
```javascript
function show() {
    let s = "<ul>";
    for (let n in name_mapping) {
        s += "<li>" + name_mapping[n];
        s += ": ";
        s += winNo1[n].join(', ');
        console.log(s);
    }
    s = s + "</ul>";
    document.getElementById("#result").innerHTML = s;
}
```

Sol-1 Hint
```javascript
<!-- add the style -->
<style>
    .prizeName {
        font-size: larger;
        color: blue;
    }

    .prizeNum:hover {
        background-color: yellow;
    }
</style>


// add the class to the element
function show01() {
    let s = "<ul>";

    for (let n in name_mapping) {
        s += '<li><idv class="prizeName">' + name_mapping[n] + '</idv>';
        s += ": ";
        ss = winNo1[n].map((x) => '<idv class="prizeNum">' + x + '</idv>')
        s += ss.join(', ');
        console.log(s);
    }
    s = s + "</ul>";
    document.getElementById("#result01").innerHTML = s;
        }
```

Sol-3: Hint
```javascript
function showAllWinner() {
    let s = "";
    for (let prize in winNo1) {
        s += ... ;
        s += '<div class="logo div">';
        let logo = logo_mapping[prize];
        s += `<img src="img/${logo}" alt="" class="img-fluid">`;
        s += "</div>";

        s += ... ;
        let prize_name = name_mapping[prize];
        let winner = winNo1[prize];
        s += `<p>${prize_name}</p>`;
        let winner_div = winner.map(x => `<div class="winner"> ${x} </div>`);
        s += winner_div.join("");
        s += "</div></div>";
    }

```

---

## 參考解答

[Github](https://github.com/nlhsueh/www-js)

#### grade
```javascript
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script>
        let a = [
            [98, 95, 98], // 學生 1 的三科成績
            [89, 22, 99], // 學生 2 的三科成績
            [70, 55, 72]  // 學生 3 的三科成績
        ];
        let names = [];
        let subjects = [];

        function setNameSubject() {
            names = document.forms["grade"]["names"].value.split(" ");
            console.log(names);
            subjects = document.forms["grade"]["subjs"].value.split(" ");
            console.log(subjects);
        }

        // 印出各科最高者
        function highest() {
            let st_len = a.length;
            let sj_len = a[0].length;
            let hList = [];
            for (let j = 0; j < sj_len; j++) { //for each subject
                console.log("Highest score of " + subjects[j]);
                let max_index = 0;
                let max = a[max_index][j];
                for (let i = 0; i < st_len; i++) {
                    if (a[i][j] > max) {
                        max = a[i][j];
                        max_index = i;
                    }
                }
                // console.log(subjects[j] + ", " + max.toString() + " by " + names[max_index]);
                hList.push({ 'subject': subjects[j], 'max': max, 'name': names[max_index] });
                console.log(`${subjects[j]}: the highest score is ${max}, by ${names[max_index]}`);
            }
            console.log(hList);
            return (hList);
        }

        // 回傳學生各科的平均
        function average() {
            let st_av = [];
            for (let gg of a) {
                sum = 0;
                for (let g of gg) {
                    sum += g;
                }
                st_av.push(Math.round(sum / gg.length, 2));
            }
            console.log(st_av)
            return st_av;
        }
    </script>
    <style>
        .center {
            max-width: 600px;
            margin: auto;
            width: 60%;
            padding: 10px;
        }

        label,
        input {
            display: block;
        }

        label,
        fieldset {
            margin-bottom: 10px;
        }
    </style>

</head>

<body class="center">

    <h1>Grade system</h1>

    <form name="grade" id="grade" action="">
        <fieldset>
            <label for="names">Names</label>
            <input id="names" name="names" type="text" value="John Nick Albert">
            <label for="subjs"></label>
            <input id="subjs" name="subjs" type="text" value="Math Phy Eng">

            <input type="button" value="Set value" onclick="setNameSubject()">
            <input type="button" value="average" onclick="average()">
            <input type="button" value="highest" onclick="highest()">
        </fieldset>
    </form>

</body>

</html>
```

## 歷屆考題

### 112-1 期中考

#### 一、加碼券開獎 HTML 版 (35%)
* 如下方加碼券的畫面，請以 HTML/CSS 設計該畫面，並進行以下修改：
    * 標題和獎項內容整體風格置中左右有 margin，獎項條列仍為置左。
    * 獎項名稱（如國旅券）的字體稍大，顏色改為藍色。
    * 游標移到號碼（例如 21) 時，底色會變成黃底。
    * 「點一下開獎囉」不用有動作。
    * （資料如第二題，可取用使用）

<img src="https://hackmd.io/_uploads/r14dms8kA.png" width="400">

#### 二、加碼券開獎 JS 版 (35%)
同上，但這次會有動作。修改以下的程式碼，點擊後會出現上面的畫面（獎項名稱和號碼）

```html
<!DOCTYPE html>

<head>
<script>
let winNo1 = {
  "domesticTravel": ["21", "32", "98", "67", "97", "410"],
  "iYuan": ["64", "85"],
  "agriculture": ["89", "32", "54", "597", "453", "152"],
  "artFunE": ["96", "15", "07", "30", "73", "98", "19", "11"],
  "artFunP": ["39", "37", "23", "36", "79", "08", "14", "75"],
  "sports": ["97", "13", "19", "55", "71", "93", "381", "734", "644",   "453", "985"],
  "hakka": ["81", "900"],
  "rgionalRevitalization": ["081", "105", "594", "188", "089", "396", "521", "467", "912", "798", "358", "441", "367", "941", "335"]
};

let name_mapping = {
   "domesticTravel": "國旅劵",
   "iYuan": "i 原劵",
   "agriculture": "農遊劵",
   "artFunE": "藝Fun劵 數位",
   "artFunP": "旅遊劵 紙本",
   "sports": "動滋劵",
   "hakka": "客庄劵",
   "rgionalRevitalization": "地方創生劵"
};

function show() {
    let s = "<ul>";




    document.getElementById("#result").innerHTML = s;
}
</script>

</head>

<body>
   <h1> 加碼劵開獎 </h1>
   <input type="button" value="點一下開獎囉" onclick="show()">
   <div id="#result"></div>
</body>
```

#### 三、加碼券開獎圖片版 (35%)
* 圖片可由 [這裡](https://drive.google.com/drive/folders/1Gd9Gt1jdhg7e_xUW_ubzoPK42ON7VP-W?usp=sharing) 取得
* 請使用 HTML/CSS 排版以完成下方畫面
* 亦可修改第二題 JS code 完成
* (超過 100 分以 100 分計)

<img src="https://hackmd.io/_uploads/rkl-SiUk0.png" width="400">

### 112-2 期中考

#### 一、七龍珠 (35%)

七龍珠是鳥山明所創作、廣受喜愛的日本漫畫。以下是一個簡介網頁 (下方條列與圖中編號對應）
1. 元件置中，寬度設為 700px; 左右留相同大小的間隔。
2. h1 元件，請改為標題置中。
3. 圖片的透明度預設為 0.7, 游標移過去時變為 1.0。
4. p 元件，顏色請改為藍色。
5. 圖片漂浮於右側。
6. 寬度請改為原來的 0.8; 置中綠底白字。高度限定為 100px; 超出的部分請用 scroll 捲軸呈現。
7. 條列元件，請用順序條列。


See [完整考題](https://docs.google.com/document/d/1SfoXPxjsjOnfxrVOzgZ7ouyhyXEwzq8p3CTC22I4yg4/edit#heading=h.tu8h3uvts1wb)

#### 二、人物 (35%)

想要呈現上述的效果，部分程式碼如下：

```javascript
<div class="gallery">
    <img src="http://img.yes-news.com/201502/ffef4eda.jpg">
    <div class="desc">孫悟空-少年期</div>
</div>
```


請參考 CSS 講義，image gallery 的做法，div gallery 的寬與高分別設定為 180px, 220px。各圖片的原始網址與描述如下：

```javascript
characters = ["孫悟空-少年期", "龜仙人", "孫悟飯", "桃白白", "孫悟空-前期", "孫悟空-中期"];
img_urls = ["http://img.yes-news.com/201502/ffef4eda.jpg",
            "http://img.yes-news.com/201502/b9461ecb.jpg",
            "http://img.yes-news.com/201502/c0e2da6f.jpg",
            "http://img.yes-news.com/201502/03b96611.jpg",
            "http://img.yes-news.com/201502/e079dd22.jpg",
            "http://img.yes-news.com/201502/c6812f95.jpg",
            ];
```

See [完整考題](https://docs.google.com/document/d/1SfoXPxjsjOnfxrVOzgZ7ouyhyXEwzq8p3CTC22I4yg4/edit#heading=h.tu8h3uvts1wb)

#### 三、人物- JS 版本 (35%)

同上，但一開始資料是空的，如下 img 的 src 和 desc 都是空的，但有 id：

```html
<div class="gallery">
    <img id="img0" src="">
    <div id="desc0" class="desc"></div>
</div>

<div class="gallery">
    <img id="img1" src="">
    <div id="desc1" class="desc"></div>
</div>
    ...
```    

請透過上述陣列的資料 (characters, img_urls)，動態的產生資料。當我們按下「人物上場」時
* 透過 console.log() 印出兩個陣列的內容
* 透過 document.getElementById() 來做資料的設定，產生和第二題一樣的畫面。

See [完整考題](https://docs.google.com/document/d/1SfoXPxjsjOnfxrVOzgZ7ouyhyXEwzq8p3CTC22I4yg4/edit#heading=h.tu8h3uvts1wb)