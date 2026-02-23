
# Ch5. Python 快速入門

以下是針對已經學過 JavaScript 的人準備的 Python 講義，包含解說、程式碼和與 JavaScript 的比較：

## 5.1. 基礎語法與資料型別

### 5.1.1 變數宣告

**Python:**

```python
name = "Alice"
age = 30
is_student = False
height = 1.75
```

**JavaScript:**

```javascript
let name = "Alice";
const age = 30;
let isStudent = false;
let height = 1.75;
```

**比較:**

* Python 不需要顯式宣告變數型別，型別是動態推斷的。
* Python 沒有 `const` 關鍵字來宣告不可變的變數，但有命名慣例（全大寫）表示常量。
* Python 使用 `=` 進行賦值。

### 5.1.2 資料型別

**Python 主要資料型別:**

* **整數 (int):** `10`, `-5`
* **浮點數 (float):** `3.14`, `-0.5`
* **布林值 (bool):** `True`, `False` (注意大小寫)
* **字串 (str):** `"hello"`, `'world'` (單引號和雙引號都可以)
* **列表 (list):** `[1, 2, "three"]` (類似 JavaScript 的陣列，但更靈活)
* **元組 (tuple):** `(1, 2, "three")` (不可變的列表)
* **集合 (set):** `{1, 2, 3}` (不重複元素的集合)
* **字典 (dict):** `{"name": "Bob", "age": 25}` (鍵值對應，類似 JavaScript 的物件)
* **None:** 表示空值或不存在 (類似 JavaScript 的 `null` 或 `undefined`)

**JavaScript 主要資料型別:**

* `Number` (包含整數和浮點數)
* `Boolean` (`true`, `false`)
* `String`
* `Array`
* `Object`
* `null`
* `undefined`
* `Symbol`
* `BigInt`

**比較:**

* Python 的資料型別更加明確和細分，例如區分了列表和元組。
* Python 的字典與 JavaScript 的物件概念相似，但語法略有不同。
* Python 有 `None`，類似於 JavaScript 的 `null` 和 `undefined`，但通常 `None` 更常用。

### 5.1.3 註解

**Python:**

```python
# 單行註解

"""
多行註解
可以使用三個雙引號
"""
```

**JavaScript:**

```javascript
// 單行註解

/*
多行註解
可以使用星號和斜線
*/
```

**比較:**

* Python 使用 `#` 作為單行註解，使用三個雙引號 `"""` 或三個單引號 `'''` 作為多行註解。
* JavaScript 使用 `//` 作為單行註解，使用 `/* ... */` 作為多行註解。

## 5.2. 運算子

### 5.2.1 算術運算子

| 運算子 | Python | JavaScript | 描述                |
| :----- | :----- | :--------- | :------------------ |
| `+`    | `+`    | `+`        | 加法                |
| `-`    | `-`    | `-`        | 減法                |
| `*`    | `*`    | `*`        | 乘法                |
| `/`    | `/`    | `/`        | 除法 (結果為浮點數) |
| `//`   | `//`   | 無         | 整除 (向下取整)     |
| `%`    | `%`    | `%`        | 取餘數              |
| `**`   | `**`   | 無         | 冪運算              |

**比較:**

* Python 提供了整除運算符 `//` 和冪運算符 `**`，JavaScript 沒有直接對應的運算符。

### 5.2.2 比較運算子

| 運算子   | Python   | JavaScript    | 描述                              |
| :------- | :------- | :------------ | :-------------------------------- |
| `==`     | `==`     | `==` 或 `===` | 等於                              |
| `!=`     | `!=`     | `!=` 或 `!==` | 不等於                            |
| `>`      | `>`      | `>`           | 大於                              |
| `<`      | `<`      | `<`           | 小於                              |
| `>=`     | `>=`     | `>=`          | 大於等於                          |
| `<=`     | `<=`     | `<=`          | 小於等於                          |
| `is`     | `is`     | 無            | 物件識別 (判斷是否是同一個物件)   |
| `is not` | `is not` | 無            | 物件識別 (判斷是否不是同一個物件) |

**比較:**

* Python 的 `is` 和 `is not` 用於比較物件的身份（記憶體位址），而不是值。在 JavaScript 中，`===` 和 `!==` 除了比較值之外，還比較型別。Python 的 `==` 和 `!=` 只比較值。

### 5.2.3 邏輯運算子

| 運算子 | Python | JavaScript | 描述   |
| :----- | :----- | :--------- | :----- |
| AND    | `and`  | `&&`       | 邏輯與 |
| OR     | `or`   | `\|\|`     | 邏輯或 |
| NOT    | `not`  | `!`        | 邏輯非 |

**比較:**

* Python 使用英文單字 `and`, `or`, `not` 作為邏輯運算符，而 JavaScript 使用 `&&`, `||`, `!`。

好的，這份講義將延續之前的內容，專門介紹 Python 的字串處理，並與 JavaScript 進行比較：


### 5.2.4 字串的基本操作

**Python:**

```python
single_quoted = 'hello'
double_quoted = "world"
multi_line = """
This is a
multi-line string.
"""
```

**JavaScript:**

```javascript
const singleQuoted = 'hello';
const doubleQuoted = "world";
const backticks = `This is also a
multi-line string using
template literals.`;
```

**比較:**

* Python 使用單引號 `'` 或雙引號 `"` 來創建字串，兩者沒有本質區別。
* Python 使用三個單引號 `'''` 或三個雙引號 `"""` 來創建多行字串。
* JavaScript 除了單引號和雙引號外，還提供了模板字面量 (backticks ``)，可以更方便地進行字串插值和創建多行字串。


#### 5.2.4.1 字串長度

**Python:**

```python
text = "Python"
length = len(text)
print(length)  # 輸出: 6
```

**JavaScript:**

```javascript
const text = "JavaScript";
const length = text.length;
console.log(length); // 輸出: 10
```

**比較:**

* Python 使用內建函數 `len()` 來獲取字串的長度。
* JavaScript 的字串物件有一個 `length` 屬性。

#### 5.2.4.2 字串連接

**Python:**

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # 輸出: Hello World

# 使用 f-string (Python 3.6+)
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)  # 輸出: Hello, Alice!
```

**JavaScript:**

```javascript
const str1 = "Hello";
const str2 = "World";
const result = str1 + " " + str2;
console.log(result); // 輸出: Hello World

// 使用模板字面量 (ES6+)
const name = "Alice";
const greeting = `Hello, ${name}!`;
console.log(greeting); // 輸出: Hello, Alice!
```

**比較:**

* Python 和 JavaScript 都使用 `+` 運算符來連接字串。
* Python 的 f-string (formatted string literals) 提供了更簡潔的字串插值方式，類似於 JavaScript 的模板字面量。

#### 5.2.4.3 字串索引

**Python:**

```python
text = "Python"
first_char = text[0]  # 索引從 0 開始
print(first_char)  # 輸出: P
last_char = text[-1] # 負索引表示從尾部開始
print(last_char)   # 輸出: n
```

**JavaScript:**

```javascript
const text = "JavaScript";
const firstChar = text[0];
console.log(firstChar); // 輸出: J
const lastChar = text[text.length - 1];
console.log(lastChar);  // 輸出: t
```

**比較:**

* Python 和 JavaScript 都使用方括號 `[]` 來存取字串中的字元，索引都從 0 開始。
* Python 支援負索引，可以方便地從字串的尾部開始存取字元。

#### 5.2.4.4 字串切片

**Python:**

```python
text = "Python"
substring1 = text[1:4]  # 從索引 1 開始到索引 4 (不包含)
print(substring1)  # 輸出: yth
substring2 = text[:3]   # 從開始到索引 3 (不包含)
print(substring2)  # 輸出: Pyt
substring3 = text[2:]   # 從索引 2 開始到結束
print(substring3)  # 輸出: thon
substring4 = text[:]    # 複製整個字串
print(substring4)  # 輸出: Python
substring5 = text[::2]  # 每隔一個字元取一個 (步長切片)
print(substring5)  # 輸出: Pto
substring6 = text[::-1] # 反轉字串
print(substring6)  # 輸出: nohtyP
```

**JavaScript:**

```javascript
const text = "JavaScript";
const substring1 = text.slice(1, 4); // 從索引 1 開始到索引 4 (不包含)
console.log(substring1); // 輸出: ava
const substring2 = text.slice(0, 3); // 從開始到索引 3 (不包含)
console.log(substring2); // 輸出: Jav
const substring3 = text.slice(2);    // 從索引 2 開始到結束
console.log(substring3); // 輸出: vaScript
const substring4 = text.slice();   // 複製整個字串
console.log(substring4); // 輸出: JavaScript
// JavaScript 沒有直接的步長切片語法或反轉語法
```

**比較:**

* Python 的字串切片功能非常強大，可以指定起始索引、結束索引和步長。
* JavaScript 使用 `slice()` 方法來實現類似的功能，但不直接支援步長。要實現類似步長或反轉的效果，通常需要結合其他方法（例如 `split()`, `reverse()`, `join()`）。

#### 5.2.7 常用的字串方法

Python 的字串物件提供了許多內建方法來進行各種操作。以下是一些常用的方法，並與 JavaScript 的類似方法進行比較：

| Python 方法          | JavaScript 方法                | 描述                                        |
| :------------------- | :----------------------------- | :------------------------------------------ |
| `lower()`            | `toLowerCase()`                | 將字串轉換為小寫                            |
| `upper()`            | `toUpperCase()`                | 將字串轉換為大寫                            |
| `strip()`            | `trim()`                       | 移除字串頭尾的空白字元                      |
| `lstrip()`           | `trimStart()` 或 `trimLeft()`  | 移除字串開頭的空白字元                      |
| `rstrip()`           | `trimEnd()` 或 `trimRight()`   | 移除字串結尾的空白字元                      |
| `startswith(prefix)` | `startsWith(prefix)`           | 檢查字串是否以指定的前綴開始                |
| `endswith(suffix)`   | `endsWith(suffix)`             | 檢查字串是否以指定的後綴結束                |
| `find(substring)`    | `indexOf(substring)`           | 查找子字串第一次出現的索引，找不到返回 -1   |
| `rfind(substring)`   | `lastIndexOf(substring)`       | 查找子字串最後一次出現的索引，找不到返回 -1 |
| `replace(old, new)`  | `replace(old, new)`            | 將字串中的舊子字串替換為新子字串            |
| `split(separator)`   | `split(separator)`             | 將字串按指定分隔符分割成列表/陣列           |
| `join(iterable)`     | `join(array)`                  | 將可迭代對象（如列表/陣列）中的字串連接起來 |
| `count(substring)`   | (需要使用其他方法組合)         | 計算子字串在字串中出現的次數                |
| `isdigit()`          | (需要使用正則表達式或自訂邏輯) | 檢查字串是否只包含數字                      |
| `isalpha()`          | (需要使用正則表達式或自訂邏輯) | 檢查字串是否只包含字母                      |
| `isalnum()`          | (需要使用正則表達式或自訂邏輯) | 檢查字串是否只包含字母和數字                |

**範例:**

**Python:**

```python
text = "  Python is fun  "
lower_text = text.lower()
print(lower_text)  # 輸出:   python is fun

upper_text = text.upper()
print(upper_text)  # 輸出:   PYTHON IS FUN

stripped_text = text.strip()
print(stripped_text) # 輸出: Python is fun

print(text.startswith("  P")) # 輸出: True
print(text.endswith("fun  ")) # 輸出: True

index = text.find("is")
print(index)       # 輸出: 9

replaced_text = text.replace("fun", "awesome")
print(replaced_text) # 輸出:   Python is awesome

words = stripped_text.split(" ")
print(words)       # 輸出: ['Python', 'is', 'fun']

joined_text = "-".join(words)
print(joined_text) # 輸出: Python-is-fun

count = text.count("n")
print(count)       # 輸出: 1

number_str = "12345"
print(number_str.isdigit()) # 輸出: True

alpha_str = "HelloWorld"
print(alpha_str.isalpha())  # 輸出: True
```

**JavaScript:**

```javascript
const text = "  JavaScript is cool  ";
const lowerText = text.toLowerCase();
console.log(lowerText); // 輸出:   javascript is cool

const upperText = text.toUpperCase();
console.log(upperText); // 輸出:   JAVASCRIPT IS COOL

const trimmedText = text.trim();
console.log(trimmedText); // 輸出: JavaScript is cool

console.log(text.startsWith("  J")); // 輸出: True
console.log(text.endsWith("cool  ")); // 輸出: True

const index = text.indexOf("is");
console.log(index);      // 輸出: 13

const replacedText = text.replace("cool", "amazing");
console.log(replacedText); // 輸出:   JavaScript is amazing

const words = trimmedText.split(" ");
console.log(words);      // 輸出: [ 'JavaScript', 'is', 'cool' ]

const joinedText = "-".join(words);
console.log(joinedText); // 輸出: JavaScript-is-cool

// JavaScript 沒有直接的 count 方法
const count = text.split("o").length - 1;
console.log(count);      // 輸出: 2

const numberStr = "12345";
console.log(/^[0-9]+$/.test(numberStr)); // 輸出: true

const alphaStr = "HelloWorld";
console.log(/^[a-zA-Z]+$/.test(alphaStr)); // 輸出: true
```

**比較:**

* Python 和 JavaScript 都提供了許多常用的字串處理方法，功能上有很多相似之處。
* Python 的字串方法通常直接作為字串物件的方法調用。
* JavaScript 的某些功能可能需要使用正則表達式或其他方法組合來實現。
* Python 在字串處理方面提供了更多內建的便利方法，例如 `count`, `isdigit`, `isalpha`, `isalnum` 等。

---
### 5.2.5 Exercise

####  5.2.5.1 長打率

**基礎運算練習題：計算球員的長打率 (Slugging Percentage)**

**題目：**

長打率是棒球中衡量打者長打能力的指標。它的計算公式如下：

```
長打率 = (一壘安打數 + 二壘安打數 * 2 + 三壘安打數 * 3 + 全壘打數 * 4) / 總打數
```

假設你已知一位棒球員的以下數據：

* 一壘安打數 (`singles`) = 80
* 二壘安打數 (`doubles`) = 30
* 三壘安打數 (`triples`) = 5
* 全壘打數 (`home_runs`) = 25
* 總打數 (`at_bats`) = 400

請使用 Python 的基礎算術運算符計算這位球員的長打率，並將結果印出（保留三位小數）。

**請直接在下面的程式碼中完成計算和印出：**

```python
singles = 80
doubles = 30
triples = 5
home_runs = 25
at_bats = 400

# 在這裡計算長打率
slugging_percentage = ...

# 印出長打率
print(f"這位球員的長打率為: {slugging_percentage:.3f}")
```

---
#### 5.2.5.2 先發投手

```python
# 提示使用者輸入投球局數
innings_pitched_str = input("請輸入這位投手的投球局數（例如：5.1）：")

# 提示使用者輸入自責分
earned_runs_str = input("請輸入這位投手的自責分：")

try:
    innings_pitched = float(innings_pitched_str)
    earned_runs = int(earned_runs_str)
except ValueError:
    print("輸入格式錯誤，請確保投球局數為數字，自責分為整數。")
else:
    print(f"這位投手投了 {innings_pitched} 局，自責分為 {earned_runs} 分。")

    # 在這裡進行判斷
    if innings_pitched ... 5:
        print("這位投手是合格的先發投手。")
        if innings_pitched ... 6 and earned_runs ... 3:
            print("這是一場優質先發！")
        else:
            print("這是一場普通的先發。")
    else:
        print("這位投手不是合格的先發投手。")
        if earned_runs ... 0:
            print("這可能是佈局投手或關門投手的出色表現。")
        else:
            print("這場表現為非合格先發。")
```            

## 5.3. 邏輯控制

### 5.3.1 條件語句 (if, elif, else)

**Python:**

```python
age = 20
if age >= 18:
    print("成年人")
elif age >= 13:
    print("青少年")
else:
    print("兒童")
```

**JavaScript:**

```javascript
let age = 20;
if (age >= 18) {
  console.log("成年人");
} else if (age >= 13) {
  console.log("青少年");
} else {
  console.log("兒童");
}
```

**比較:**

* Python 使用 `if`, `elif` (else if 的縮寫), `else` 關鍵字。
* Python 沒有像 JavaScript 那樣使用花括號 `{}` 來包圍程式碼塊，而是使用**縮排**來表示程式碼塊的層次。這是 Python 語法中非常重要的一部分。
* 條件判斷後的冒號 `:` 是 Python 語法的一部分。

### 5.3.2 迴圈語句 (for, while)

**Python - for 迴圈 (迭代):**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):  # 產生 0 到 4 的序列
    print(i)

for i in range(2, 6): # 產生 2 到 5 的序列
    print(i)

for i in range(0, 10, 2): # 產生 0, 2, 4, 6, 8 的序列 (帶步長)
    print(i)
```

**JavaScript - for 迴圈:**

```javascript
const fruits = ["apple", "banana", "cherry"];
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

for (const fruit of fruits) { // ES6 的 for...of 迴圈
  console.log(fruit);
}

for (const key in fruits) { // 迭代索引 (不常用於陣列)
  console.log(key);
}
```

**比較:**

* Python 的 `for` 迴圈主要用於迭代序列 (如列表、元組、字串) 或其他可迭代對象。
* Python 的 `range()` 函數用於生成數字序列，類似於 JavaScript 中手動控制的 `for` 迴圈。
* Python 的 `for...in` 迴圈類似於 JavaScript 的 `for...of` 迴圈，用於迭代元素。

**Python - while 迴圈:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**JavaScript - while 迴圈:**

```javascript
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}
```

**比較:**

* Python 和 JavaScript 的 `while` 迴圈語法結構相似，但 Python 仍然使用縮排來定義程式碼塊。

## 5.4. 資料結構

### 5.4.1 列表 (list)

**Python:**

```python
my_list = [1, "hello", 3.14, True]
print(my_list[0])  # 存取第一個元素 (索引從 0 開始)

my_list.append("world")  # 在列表末尾添加元素
my_list.insert(1, "inserted") # 在指定索引處插入元素
del my_list[2]  # 刪除指定索引的元素
my_list.remove("hello") # 刪除指定值的元素
print(len(my_list))  # 取得列表長度
```

**JavaScript:**

```javascript
let myArray = [1, "hello", 3.14, true];
console.log(myArray[0]); // 存取第一個元素

myArray.push("world"); // 在陣列末尾添加元素
myArray.splice(1, 0, "inserted"); // 在指定索引處插入元素
myArray.splice(2, 1); // 刪除指定索引的一個元素
myArray.splice(myArray.indexOf("hello"), 1); // 刪除指定值的元素
console.log(myArray.length); // 取得陣列長度
```

**比較:**

* Python 的列表非常靈活，可以包含不同型別的元素。
* Python 提供了許多內建的方法來操作列表，例如 `append`, `insert`, `del`, `remove`, `len` 等。JavaScript 的陣列也有類似的方法，但語法可能不同。


### 5.4.2 元組 (tuple)

**Python:**

```python
my_tuple = (1, "hello", 3.14)
print(my_tuple[0])
# my_tuple[0] = 10  # 錯誤！元組是不可變的
```

**JavaScript:**

* JavaScript 沒有內建的不可變列表 (類似元組) 的資料結構，但可以使用 `Object.freeze()` 來凍結陣列或物件，使其屬性不可修改。

**比較:**

* Python 的元組是一個不可變的序列，一旦創建就不能修改。這在需要保護資料不被意外修改時很有用。

### 5.4.3 集合 (set)

**Python:**

```python
my_set = {1, 2, 2, 3, 4}  # 重複的元素會被自動移除
print(my_set)  # 輸出: {1, 2, 3, 4}
my_set.add(5)
my_set.remove(2)
print(3 in my_set)  # 檢查元素是否存在
```

**JavaScript:**

```javascript
let mySet = new Set([1, 2, 2, 3, 4]);
console.log(mySet); // 輸出: Set(4) { 1, 2, 3, 4 }
mySet.add(5);
mySet.delete(2);
console.log(mySet.has(3)); // 檢查元素是否存在
```

**比較:**

* Python 的集合和 JavaScript 的 `Set` 都用於儲存不重複的元素。它們都提供了類似的方法來添加、刪除和檢查元素。

### 5.4.4 字典 (dict)

**Python:**

```python
my_dict = {"name": "Alice", "age": 30, "city": "Taichung"}
print(my_dict["name"])
my_dict["occupation"] = "Engineer"
del my_dict["age"]
print(my_dict.keys())   # 取得所有鍵
print(my_dict.values()) # 取得所有值
print(my_dict.items())  # 取得所有鍵值對
```

**JavaScript:**

```javascript
let myObject = { name: "Alice", age: 30, city: "Taichung" };
console.log(myObject.name);
myObject.occupation = "Engineer";
delete myObject.age;
console.log(Object.keys(myObject));   // 取得所有鍵
console.log(Object.values(myObject)); // 取得所有值
console.log(Object.entries(myObject)); // 取得所有鍵值對
```

**比較:**

* Python 的字典和 JavaScript 的物件都是用於儲存鍵值對的資料結構。它們在概念上非常相似，但語法略有不同。
* Python 使用花括號 `{}` 來定義字典，並使用冒號 `:` 分隔鍵和值。
* JavaScript 也使用花括號 `{}` 來定義物件，並使用冒號 `:` 分隔鍵和值。

好的，這是一份關於 Python 列舉型態 (Enumeration Type) 的介紹：

### 5.4.5 Check

1.  下列哪一個敘述 **錯誤**？
    A) `list` 是可變的序列，可以使用索引進行存取和修改。
    B) `tuple` 是不可變的序列，一旦創建後就不能修改其元素。
    C) `set` 是無序且元素唯一的集合，支援索引存取其元素。
    D) `dict` 是鍵值對應的資料結構，可以使用鍵來存取值。

2.  給定兩個 `set` 如下：
    ```python
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    ```
    下列哪個運算式會產生 `{1, 2}` 這個結果？
    A) `set1 & set2`
    B) `set1 | set2`
    C) `set1 - set2`
    D) `set2 - set1`

3.  考慮以下程式碼片段：
    ```python
    my_tuple = (10, 20, [30, 40])
    my_tuple[2].append(50)
    ```
    執行完這段程式碼後，`my_tuple` 的值會是什麼？
    A) `(10, 20, [30, 40])`
    B) `(10, 20, [30, 40, 50])`
    C) 會因為 `tuple` 不可變而產生錯誤。
    D) `(10, 50, [30, 40])`

4.  下列哪個操作對於 `dict` 是 **不允許** 的或會導致錯誤？
    A) 使用一個 `tuple` 作為鍵。
    B) 使用一個 `list` 作為鍵。
    C) 使用一個字串作為鍵。
    D) 使用一個整數作為鍵。

5.  給定一個 `list` 如下：
    ```python
    data = [('Alice', 25), ('Bob', 30), ('Charlie', 20)]
    ```
    下列哪個程式碼片段可以將這個 `list` 轉換為一個 `dict`，其中鍵是人名，值是年齡？
    A) `dict(data)`
    B) `{name: age for name, age in data}`
    C) `{item[0]: item[1] for item in data}`
    D) 以上皆是。

---

**答案與解析：**

1.  **C)** 錯誤。`set` 是無序且元素唯一的集合，**不支援** 索引存取其元素。

2.  **C)** `set1 - set2` 會回傳存在於 `set1` 但不存在於 `set2` 的元素，即 `{1, 2}`。
    * `A)` `set1 & set2` (交集) 會產生 `{3, 4}`。
    * `B)` `set1 | set2` (聯集) 會產生 `{1, 2, 3, 4, 5, 6}`。
    * `D)` `set2 - set1` 會產生 `{5, 6}`。

3.  **B)** `(10, 20, [30, 40, 50])`。雖然 `tuple` 本身是不可變的，但如果 `tuple` 內的元素是可變的（例如 `list`），則可以修改該可變元素內部的內容。

4.  **B)** 使用一個 `list` 作為鍵。`dict` 的鍵必須是不可變的 (immutable) 型別，例如 `int`, `float`, `str`, `tuple` (且 `tuple` 的元素也必須是不可變的)。`list` 是可變的 (mutable)，因此不能作為 `dict` 的鍵。

5.  **D)** 以上皆是。
    * `A)` `dict(data)` 可以直接將包含鍵值對的 `list` 轉換為 `dict`。
    * `B)` `{name: age for name, age in data}` 是一個字典推導式，可以有效地創建所需的 `dict`。
    * `C)` `{item[0]: item[1] for item in data}` 也是一個字典推導式，透過索引存取 `tuple` 中的姓名和年齡來創建 `dict`。

---

6.  考慮以下程式碼片段：
    ```python
    my_list = [1, 2, 2, 3, 4, 4, 5]
    result_set = set(my_list)
    result_list = list(result_set)
    ```
    執行完這段程式碼後，`result_list` 的元素個數會是多少？
    A) 7
    B) 5
    C) 4
    D) 3

7.  下列哪個方法可以用於在 `list` 的指定索引位置插入一個元素？
    A) `append()`
    B) `extend()`
    C) `insert()`
    D) `add()`

8.  給定一個字典 `inventory = {'apples': 10, 'bananas': 20, 'cherries': 15}`。下列哪個程式碼片段可以正確地將 'bananas' 的數量減少 5？
    A) `inventory['bananas'] -= 5`
    B) `inventory.remove('bananas', 5)`
    C) `inventory['bananas'] = inventory['bananas'] - 5`
    D) A) 和 C) 都是正確的。

9.  假設你有兩個 `tuple`：`tuple1 = (1, 2, 3)` 和 `tuple2 = (4, 5)`。下列哪個運算式會產生 `(1, 2, 3, 4, 5)` 這個新的 `tuple`？
    A) `tuple1.append(tuple2)`
    B) `tuple1 + tuple2`
    C) `tuple1.extend(tuple2)`
    D) `tuple1.union(tuple2)`

10. 考慮以下程式碼片段：
    ```python
    data = ['a', 'b', 'c', 'b', 'd', 'a']
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    ```
    執行完這段程式碼後，`frequency` 字典的內容會是什麼？
    A) `{'a': 1, 'b': 1, 'c': 1, 'd': 1}`
    B) `{'a': 2, 'b': 2, 'c': 1, 'd': 1}`
    C) `{'a': 2, 'b': 2, 'c': 1, 'd': 1, None: 0}`
    D) 會因為重複的鍵而產生錯誤。

---

**答案與解析：**

6.  **B)** 5。
    * `set(my_list)` 會移除重複元素，產生 `{1, 2, 3, 4, 5}`。
    * `list(result_set)` 將這個 `set` 轉換為 `list`，其元素個數為 5。

7.  **C)** `insert()`。
    * `append()` 用於在列表末尾添加元素。
    * `extend()` 用於將另一個可迭代對象的元素添加到列表末尾。
    * `add()` 是 `set` 的方法，用於添加元素。

8.  **D)** A) 和 C) 都是正確的。這兩種寫法都實現了將字典中 'bananas' 鍵對應的值減少 5 的操作。

9.  **B)** `tuple1 + tuple2`。`tuple` 是不可變的，不能使用 `append()` 或 `extend()` 直接添加元素。可以使用 `+` 運算符將兩個 `tuple` 連接成一個新的 `tuple`。`union()` 是 `set` 的方法，不適用於 `tuple`。

10. **B)** `{'a': 2, 'b': 2, 'c': 1, 'd': 1}`。這段程式碼用於統計列表中每個元素的出現次數。
    * `frequency.get(item, 0)` 會檢查 `item` 是否已存在於 `frequency` 中，如果存在則返回其值，否則返回預設值 0。
    * 然後將該值加 1 並賦值給 `frequency[item]`，從而實現計數。


### 5.4.6 Exercise

#### 5.4.6.1 List 練習題：球員單場得分統計

**題目：**

你有一份列表 `scores`，記錄了某位棒球員在一個系列賽中每場比賽的得分。

```python
scores = [0, 1, 2, 0, 3, 1, 0, 2]
```

請根據這個列表完成以下操作：

1.  計算這位球員在這個系列賽中的總得分。
2.  計算這位球員得分的總場次（得分大於 0 的場次）。
3.  找出這位球員單場最高的得分。
4.  將這個系列賽的得分由低到高排序，並印出排序後的列表。
5.  印出這位球員在第三場和第五場的得分。

**請直接在下面的程式碼中完成操作：**

```python
scores = [0, 1, 2, 0, 3, 1, 0, 2]

# 1. 計算這位球員在這個系列賽中的總得分
total_score = 0
for score in scores:
    total_score = ...
print(f"總得分: {total_score}")

# 2. 計算這位球員得分的總場次
scoring_games = 0
for score ...:
    if ...:
        scoring_games = ...
print(f"得分場次: {scoring_games}")

# 3. 找出這位球員單場最高的得分
highest_score = 0
for score in scores:
    if ...:
        highest_score = ...
print(f"最高得分: {highest_score}")

# 4. 將這個系列賽的得分由低到高排序，並印出排序後的列表
sorted_scores = ...
print(f"排序後得分: {sorted_scores}")

# 5. 印出這位球員在第三場和第五場的得分
third_game_score = ...
fifth_game_score = ...
print(f"第三場得分: {third_game_score}")
print(f"第五場得分: {fifth_game_score}")
```

---

#### 4.6.2 Dict 練習題：球員打擊數據分析

**題目：**

你現在有一個字典 `player_stats`，儲存了某位棒球員在一個球季的累計打擊數據。字典的鍵是數據的名稱（字串），值是對應的數字（整數）。

```python
player_stats = {
    "打數": 150,
    "安打": 50,
    "全壘打": 10,
    "保送": 20,
    "三振": 30
}
```

請根據這個字典完成以下操作：

1.  計算這位球員的打擊率（安打數除以打數）。
2.  計算這位球員的上壘率。上壘率的計算公式是：(安打 + 保送) 除以 (打數 + 保送 + 被觸身球)。在這個簡化的數據中，我們沒有被觸身球的數據，所以只計算 (安打 + 保送) 除以 (打數 + 保送)。
3.  印出字典中所有的打擊數據項目（鍵和值），格式為："數據名稱：數據值"。
4.  檢查字典中是否包含 "盜壘" 這個鍵，如果沒有，印出 "沒有盜壘數據"。
5.  將這個球員的全壘打數更新為 12。

**請直接在下面的程式碼中完成操作：**

```python
player_stats = {
    "打數": 150,
    "安打": 50,
    "全壘打": 10,
    "保送": 20,
    "三振": 30
}

# 1. 計算這位球員的打擊率
at_bats = player_stats["打數"]
hits = player_stats["安打"]
batting_average = ...
print(f"打擊率: {batting_average:.3f}")

# 2. 計算這位球員的上壘率
walks = player_stats["保送"]
on_base_percentage = ...
print(f"上壘率: {on_base_percentage:.3f}")

# 3. 印出字典中所有的打擊數據項目
for key, value in ...:
    print(...)

# 4. 檢查字典中是否包含 "盜壘" 這個鍵
if ...:
    pass
else:
    print(...)

# 5. 將這個球員的全壘打數更新為 12
player_stats["全壘打"] = ...
print(f"更新後全壘打數: {player_stats['全壘打']}")
```

---


## 5.5. 函式 (Function)

**Python:**

```python
def greet(name):
    """這是一個簡單的問候函式"""
    print(f"Hello, {name}!")

greet("Bob")

def add(x, y):
    return x + y

result = add(5, 3)
print(result)
```

**JavaScript:**

```javascript
function greet(name) {
  /** 這是一個簡單的問候函式 */
  console.log(`Hello, ${name}!`);
}

greet("Bob");

function add(x, y) {
  return x + y;
}

let result = add(5, 3);
console.log(result);

// ES6 箭頭函式
const multiply = (a, b) => a * b;
let product = multiply(2, 4);
console.log(product);
```

**比較:**

* Python 使用 `def` 關鍵字來定義函式。
* Python 的函式參數不需要指定型別。
* Python 使用縮排來定義函式的程式碼塊。
* Python 的函式可以使用文檔字串 (docstring，用三個引號包圍) 來描述函式的功能。
* JavaScript 有傳統的 `function` 關鍵字和 ES6 引入的箭頭函式。Python 沒有類似的簡潔箭頭函式語法。

### 5.5.1 函式的定義與呼叫

**定義:**

```python
def function_name(parameters):
    """文檔字串 (docstring)，描述函式的功能"""
    # 函式體 (程式碼區塊)
    return value  # 可選的回傳值
```

* **`def` 關鍵字:** 用於開始函式定義。
* **`function_name`:** 函式的名稱，應具有描述性。
* **`parameters`:** 函式可以接收零個或多個參數，用逗號分隔。參數是在函式被呼叫時傳遞給函式的值。
* **`:`:** 函式定義行的結尾需要冒號。
* **`文檔字串 (docstring)`:** 放在函式體的第一行，用三個單引號 `'''` 或三個雙引號 `"""` 包圍，用於描述函式的功能、參數和回傳值等。可以使用 `help(function_name)` 或 `function_name.__doc__` 來查看文檔字串。
* **`函式體`:** 包含函式的實際程式碼，需要縮排。
* **`return value`:** 可選的 `return` 語句用於從函式回傳一個值。如果沒有 `return` 語句，函式會隱式地回傳 `None`。

**呼叫:**

要執行一個函式，你需要使用函式的名稱後跟括號 `()`，並在括號內傳遞任何必要的參數。

```python
def greet(name):
    """問候指定的人"""
    print(f"Hello, {name}!")

greet("Alice")  # 呼叫 greet 函式，傳遞 "Alice" 作為參數

def add(x, y):
    """回傳兩個數字的和"""
    return x + y

sum_result = add(5, 3)  # 呼叫 add 函式，接收回傳值
print(sum_result)      # 輸出: 8
```

### 5.5.2 函式的參數

Python 提供了非常靈活的參數處理機制，包括以下幾種類型：

#### 5.5.2.1 必要參數 (Positional Arguments)

這些參數在函式定義中指定了順序，並且在呼叫函式時必須按照相同的順序提供對應的值。

```python
def describe_pet(animal_type, pet_name):
    """描述寵物的種類和名字"""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", "Buddy")    # 正確的呼叫方式
# describe_pet("Buddy", "dog")  # 錯誤！參數順序不對
```

#### 5.5.2.2 關鍵字參數 (Keyword Arguments)

在呼叫函式時，可以通過 `parameter_name=value` 的形式指定參數的值，這樣可以不按照參數定義的順序傳遞值，並且可以使函式呼叫更具可讀性。

```python
def describe_pet(animal_type, pet_name):
    """描述寵物的種類和名字"""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="cat", pet_name="Lucy")
describe_pet(pet_name="Max", animal_type="hamster")
```

**注意:** 如果同時使用必要參數和關鍵字參數，必要參數必須在關鍵字參數之前。

```python
def greet(greeting, name):
    print(f"{greeting}, {name}!")

greet("Hello", name="Bob")  # 正確
# greet(name="Alice", "Hi")  # 錯誤！必要參數在關鍵字參數之後
```

#### 5.5.2.3 預設參數值 (Default Argument Values)

在函式定義時，可以為參數指定預設值。如果在呼叫函式時沒有提供該參數的值，則會使用預設值。

```python
def power(base, exponent=2):
    """計算底數的指定次方，預設為平方"""
    return base ** exponent

print(power(5))       # 使用預設的 exponent=2，輸出: 25
print(power(5, 3))    # 覆蓋預設值，輸出: 125
```

**注意:** 具有預設值的參數必須放在參數列表的最後面。

```python
# def invalid_function(a=1, b):  # 錯誤！沒有預設值的參數 b 在有預設值的參數 a 之後
#     pass

def valid_function(b, a=1):
    pass
```

#### 5.5.2.4 可變長度參數 (*args)

如果你不確定函式最終需要多少個參數，可以使用 `*args` 來接收任意數量的**位置參數**。這些參數會被收集到一個元組 (tuple) 中。

```python
def sum_all(*args):
    """計算所有傳入數字的和"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))       # 輸出: 6
print(sum_all(10, 20, 30, 40)) # 輸出: 100
print(sum_all())             # 輸出: 0 (空元組)
```

#### 5.5.2.5 可變長度關鍵字參數 (**kwargs)

如果你需要接收任意數量的**關鍵字參數**，可以使用 `**kwargs`。這些參數會被收集到一個字典 (dictionary) 中，其中鍵是參數名，值是參數值。

```python
def print_info(**kwargs):
    """列印所有傳入的關鍵字參數"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Charlie", age=35, city="New York")
# 輸出:
# name: Charlie
# age: 35
# city: New York
```

#### 5.5.2.6 強制關鍵字參數 (Keyword-Only Arguments) (Python 3+)

在參數列表中，可以將某些參數放在 `*` 之後，這樣這些參數就必須在呼叫時使用關鍵字參數的形式傳遞。

```python
def process_data(a, b, *, log_level='INFO', output_file=None):
    """處理數據，並可選記錄日誌和輸出到檔案"""
    print(f"Processing with a={a}, b={b}, log_level={log_level}, output_file={output_file}")
    # ... 處理數據的程式碼 ...

process_data(1, 2)                      # 正確
process_data(1, 2, log_level='DEBUG')  # 正確
process_data(1, 2, output_file='data.txt') # 正確
# process_data(1, 2, 'WARNING')        # 錯誤！'WARNING' 只能作為關鍵字參數傳遞
```

### 5.5.3 參數的傳遞

在 Python 中，參數的傳遞方式既不是完全的值傳遞 (pass-by-value)，也不是完全的引用傳遞 (pass-by-reference)。Python 使用的是所謂的 **"call-by-object-reference"** 或 **"pass-by-assignment"**。理解這一點對於預測函式內對參數的修改是否會影響到函式外部的變數非常重要。

* **不可變物件 (Immutable Objects):** 例如數字 (int, float)、字串 (str)、布林值 (bool)、元組 (tuple)。當這些物件作為參數傳遞給函式時，函式內部創建的是一個新的局部變數，它指向與原始變數相同的物件。如果在函式內部修改這個局部變數，實際上是讓它指向一個新的物件，原始變數的值不會受到影響。

```python
def modify_immutable(x):
    print(f"Inside function, before modification: x = {x}, id(x) = {id(x)}")
    x = 10  # 創建一個新的整數物件並賦值給局部變數 x
    print(f"Inside function, after modification: x = {x}, id(x) = {id(x)}")

num = 5
print(f"Outside function, before call: num = {num}, id(num) = {id(num)}")
modify_immutable(num)
print(f"Outside function, after call: num = {num}, id(num) = {id(num)}")

# 輸出結果會顯示函式內外的變數 id 不同，且外部 num 的值沒有改變
```

* **可變物件 (Mutable Objects):** 例如列表 (list)、字典 (dict)、集合 (set)。當這些物件作為參數傳遞給函式時，函式內部接收到的是原始物件的引用。因此，如果在函式內部修改了這個可變物件，這些修改會直接反映到函式外部的原始物件上。

```python
def modify_mutable(my_list):
    print(f"Inside function, before modification: my_list = {my_list}, id(my_list) = {id(my_list)}")
    my_list.append(4)  # 修改了傳入的列表物件
    print(f"Inside function, after modification: my_list = {my_list}, id(my_list) = {id(my_list)}")

data = [1, 2, 3]
print(f"Outside function, before call: data = {data}, id(data) = {id(data)}")
modify_mutable(data)
print(f"Outside function, after call: data = {data}, id(data) = {id(data)}")

# 輸出結果會顯示函式內外的變數 id 相同，且外部 data 的列表被修改了
```

**避免意外修改可變物件:**

如果你不希望函式內部對可變物件的修改影響到外部的原始物件，可以考慮在函式內部創建該物件的副本：

* **列表:** 使用切片 `[:]` 或 `list()` 創建副本。
* **字典:** 使用 `dict()` 創建副本。
* **集合:** 使用 `set()` 創建副本。

```python
def modify_list_safely(my_list):
    copied_list = my_list[:]  # 創建列表的副本
    copied_list.append(4)
    print(f"Inside function, modified list: {copied_list}")
    print(f"Inside function, original list: {my_list}")

data = [1, 2, 3]
print(f"Outside function, before call: {data}")
modify_list_safely(data)
print(f"Outside function, after call: {data}")

# 輸出結果會顯示外部 data 的列表沒有被修改
```

### 5.5.4 lambda function

### 5.5.4.1 lambda 函式簡介

`lambda` 函式是一種匿名的小型函式。它可以在需要一個簡單函式作為參數的地方使用，而無需顯式地定義一個具名的函式。

**Python lambda 函式語法:**

```python
lambda arguments: expression
```

* `lambda`: 關鍵字，表示定義一個匿名函式。
* `arguments`: 函式的參數列表，可以有多個，用逗號分隔。
* `:`: 分隔參數列表和函式體。
* `expression`: 函式的返回值表達式。這個表達式會被求值並返回。`lambda` 函式的表達式必須是單一的。

```python
# 定義一個 lambda 函式，接收一個參數 x，並回傳 x 的平方
square = lambda x: x ** 2

# 呼叫這個 lambda 函式
result = square(5)
print(result)  # 輸出: 25

# 你也可以直接在需要函式的地方使用 lambda 而不賦值給變數
another_result = (lambda y: y * 3)(10)
print(another_result)  # 輸出: 30
```

**JavaScript 類似概念 (箭頭函式):**

```javascript
(arguments) => expression
arguments => expression // 如果只有一個參數，括號可以省略
```

JavaScript 的箭頭函式也提供了一種更簡潔的方式來定義小型匿名函式。

### 5.5.4.2 在 `sort()` 方法中使用 lambda 函式

`list.sort(key=None, reverse=False)` 方法用於對列表進行原地排序。`key` 參數可以接收一個函式，該函式會應用於列表中的每個元素，並根據函式返回的值進行排序。`lambda` 函式非常適合在這裡提供一個簡單的排序依據。

**範例 1: 根據字串長度排序**

**Python:**

```python
words = ["apple", "banana", "kiwi", "strawberry"]
words.sort(key=lambda word: len(word))
print(words)  # 輸出: ['kiwi', 'apple', 'banana', 'strawberry']
```

在這裡，`lambda word: len(word)` 接收一個字串 `word`，並返回它的長度。`sort()` 方法會根據這些長度對 `words` 列表進行排序。

**JavaScript:**

```javascript
const words = ["apple", "banana", "kiwi", "strawberry"];
words.sort((a, b) => a.length - b.length);
console.log(words); // 輸出: [ 'kiwi', 'apple', 'banana', 'strawberry' ]
```

JavaScript 的 `sort()` 方法接收一個比較函式。箭頭函式 `(a, b) => a.length - b.length` 實現了根據字串長度比較的邏輯。

**範例 2: 根據物件列表中的特定屬性排序**

**Python:**

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
people.sort(key=lambda person: person["age"])
print(people)
# 輸出: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

`lambda person: person["age"]` 從每個字典 `person` 中提取 `age` 屬性作為排序的依據。

**JavaScript:**

```javascript
const people = [
    { name: "Alice", age: 30 },
    { name: "Bob", age: 25 },
    { name: "Charlie", age: 35 }
];
people.sort((a, b) => a.age - b.age);
console.log(people);
// 輸出: [ { name: 'Bob', age: 25 }, { name: 'Alice', age: 30 }, { name: 'Charlie', age: 35 } ]
```

### 5.5.4.3 在 `filter()` 函數中使用 lambda 函式

`filter(function, iterable)` 函數用於過濾序列，返回一個迭代器，其中包含使 `function` 返回 `True` 的所有元素。`lambda` 函式非常適合在這裡提供一個簡單的過濾條件。

**範例: 過濾出列表中的偶數**

**Python:**

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 輸出: [2, 4, 6]
```

`lambda x: x % 2 == 0` 接收一個數字 `x`，並返回它是否為偶數的布林值。`filter()` 函數根據這個條件過濾 `numbers` 列表。

**JavaScript:**

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evenNumbers = numbers.filter(x => x % 2 === 0);
console.log(evenNumbers); // 輸出: [ 2, 4, 6 ]
```

JavaScript 的 `filter()` 方法接收一個回調函式，該函式對每個元素進行測試，並返回一個包含所有通過測試的元素的新陣列。

**範例: 過濾出長度大於 5 的字串**

**Python:**

```python
words = ["apple", "banana", "kiwi", "strawberry"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  # 輸出: ['banana', 'strawberry']
```

**JavaScript:**

```javascript
const words = ["apple", "banana", "kiwi", "strawberry"];
const longWords = words.filter(word => word.length > 5);
console.log(longWords); // 輸出: [ 'banana', 'strawberry' ]
```

### 5.5.4.4 在 `map()` 函數中使用 lambda 函式

`map(function, iterable, ...)` 函數用於將 `function` 應用於 `iterable` 中的每一個元素，並返回一個迭代器，其中包含應用後的結果。`lambda` 函式非常適合在這裡提供一個簡單的轉換邏輯。

**範例: 將列表中的每個數字平方**

**Python:**

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # 輸出: [1, 4, 9, 16, 25]
```

`lambda x: x ** 2` 接收一個數字 `x`，並返回它的平方。`map()` 函數將這個平方操作應用於 `numbers` 列表中的每個元素。

**JavaScript:**

```javascript
const numbers = [1, 2, 3, 4, 5];
const squaredNumbers = numbers.map(x => x ** 2);
console.log(squaredNumbers); // 輸出: [ 1, 4, 9, 16, 25 ]
```

JavaScript 的 `map()` 方法接收一個回調函式，該函式對每個元素進行轉換，並返回一個包含轉換後結果的新陣列。

**範例: 將字串列表轉換為大寫**

**Python:**

```python
words = ["apple", "banana", "kiwi"]
upper_words = list(map(lambda word: word.upper(), words))
print(upper_words)  # 輸出: ['APPLE', 'BANANA', 'KIWI']
```

**JavaScript:**

```javascript
const words = ["apple", "banana", "kiwi"];
const upperWords = words.map(word => word.toUpperCase());
console.log(upperWords); // 輸出: [ 'APPLE', 'BANANA', 'KIWI' ]
```

### 5.5.4.5 組合使用 `lambda`, `map`, 和 `filter`

`lambda` 函式可以與 `map()` 和 `filter()` 組合使用，以實現更複雜的列表處理邏輯。

**範例: 過濾出偶數後再平方**

**Python:**

```python
numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # 輸出: [4, 16, 36]
```

這個例子首先使用 `filter()` 找出偶數，然後使用 `map()` 對這些偶數進行平方。

**JavaScript:**

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const result = numbers.filter(x => x % 2 === 0).map(x => x ** 2);
console.log(result); // 輸出: [ 4, 16, 36 ]
```

JavaScript 中可以通過鏈式調用 `filter()` 和 `map()` 方法來實現相同的效果，語法上可能更為直觀。

### 5.5.5 與 JavaScript 的比較

JavaScript 的參數傳遞方式通常被描述為 "pass-by-value" for primitive types (例如 number, string, boolean, null, undefined, symbol, bigint) 和 "pass-by-reference" for objects (包括 arrays 和 functions)。

* **原始型別 (Primitives):** 在 JavaScript 中，當原始型別的值作為參數傳遞時，函式接收到的是該值的一個副本。在函式內部對參數的修改不會影響到函式外部的原始變數。這與 Python 中不可變物件的行為類似。

* **物件 (Objects):** 在 JavaScript 中，當物件作為參數傳遞時，函式接收到的是指向該物件的引用。因此，如果在函式內部修改了物件的屬性，這些修改會反映到函式外部的原始物件上。這與 Python 中可變物件的行為類似。

**總結:**

Python 的 "call-by-object-reference" 行為在概念上與 JavaScript 的參數傳遞方式有相似之處，但需要更精確地理解可變和不可變物件的區別，以及函式內部對這些物件的操作如何影響外部變數。理解這些細節對於編寫可靠且易於理解的 Python 程式至關重要。

### 5.6 Check

1.  下列哪個關於 Python 函式參數的敘述是**錯誤**的？
    A) 函式可以沒有任何參數。
    B) 函式可以有多個必要參數（positional arguments）。
    C) 函式定義中，帶有預設值的參數必須放在沒有預設值的參數前面。
    D) 函式可以使用 `*args` 接收任意數量的位置參數。

2.  考慮以下函式定義：
    ```python
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    ```
    下列哪個函式呼叫會產生錯誤？
    A) `greet("Alice")`
    B) `greet(name="Bob")`
    C) `greet("Charlie", greeting="Hi")`
    D) `greet(greeting="Welcome", "David")`

3.  關於 Python 函式的參數傳遞，下列敘述何者正確？
    A) 不可變物件（如整數、字串）總是通過引用傳遞。
    B) 可變物件（如列表、字典）總是通過值傳遞。
    C) Python 使用的是 "call-by-object-reference" 或 "pass-by-assignment"。
    D) 函式內部對參數的修改永遠不會影響到函式外部的原始變數。

4.  下列哪個是有效的 Python `lambda` 函式定義？
    A) `lambda x where x > 5: x * 2`
    B) `def lambda(x): return x + 1`
    C) `(x) => x ** 2`
    D) `lambda x: x % 2 == 0`

5.  給定一個列表 `numbers = [3, 1, 4, 1, 5, 9, 2, 6]`，下列哪個程式碼片段會使用 `lambda` 函式將其排序為降序？
    A) `numbers.sort()`
    B) `sorted(numbers)`
    C) `numbers.sort(key=lambda x: -x)`
    D) `sorted(numbers, key=lambda x: x, reverse=False)`

6.  給定一個列表 `words = ["apple", "banana", "kiwi", "strawberry"]`，下列哪個程式碼片段會使用 `filter` 和 `lambda` 函式篩選出長度大於 5 的單字？
    A) `filter(lambda w: len(w) > 5, words)`
    B) `words.filter(lambda w: len(w) > 5)`
    C) `[w for w in words if len(w) > 5]`
    D) A) 和 C) 都是正確的。

7.  考慮以下函式定義：
    ```python
    def process_data(a, b, *args, **kwargs):
        return f"a={a}, b={b}, args={args}, kwargs={kwargs}"
    ```
    下列哪個函式呼叫會產生 `a=1, b=2, args=(3, 4), kwargs={'x': 5, 'y': 6}` 的輸出？
    A) `process_data(1, 2, 3, 4, x=5, y=6)`
    B) `process_data(a=1, b=2, 3, 4, x=5, y=6)`
    C) `process_data(1, b=2, args=[3, 4], kwargs={'x': 5, 'y': 6})`
    D) `process_data(1, 2, (3, 4), {'x': 5, 'y': 6})`

8.  關於 Python 函式的回傳值，下列敘述何者正確？
    A) 函式只能回傳一個值。
    B) 如果函式沒有 `return` 語句，它會隱式地回傳 `None`。
    C) 使用 `return a, b` 可以回傳多個值，這些值會被封裝成一個列表。
    D) 函式中 `return` 語句後的程式碼一定會被執行。

9.  給定一個列表 `items = [{'name': 'apple', 'price': 2}, {'name': 'banana', 'price': 1}, {'name': 'cherry', 'price': 3}]`，下列哪個程式碼片段會使用 `sort` 和 `lambda` 函式根據價格降序排序這個列表？
    A) `items.sort(key=lambda item: item['price'])`
    B) `sorted(items, key=lambda item: item['price'], reverse=True)`
    C) `items.sort(key=lambda item: -item['price'])`
    D) B) 和 C) 都是正確的。

10. 考慮以下函式定義：
    ```python
    def apply_operation(func, x):
        return func(x)
    ```
    下列哪個呼叫會將 `y` 的值設為 25？
    A) `y = apply_operation(def square(z): return z * z, 5)`
    B) `y = apply_operation(square(5))`
    C) `y = apply_operation(lambda z: z * z, 5)`
    D) `y = apply_operation((z) => z * z, 5)`

---

**答案與解析：**

1.  **C)** 錯誤。帶有預設值的參數**必須**放在沒有預設值的參數**後面**。

2.  **D)** `greet(greeting="Welcome", "David")` 會產生錯誤，因為在關鍵字參數之後不能再有位置參數。

3.  **C)** 正確。Python 使用 "call-by-object-reference" 或 "pass-by-assignment"。對於可變物件，函式內部的修改可能會影響到外部的原始物件。

4.  **D)** `lambda x: x % 2 == 0` 是有效的 `lambda` 函式定義。A) 使用了 `where` 關鍵字，這是不正確的 `lambda` 語法。B) 使用了 `def` 關鍵字，這不是匿名函式。C) 是 JavaScript 的箭頭函式語法。

5.  **C)** `numbers.sort(key=lambda x: -x)` 會使用 `lambda` 函式返回元素的負值作為排序的依據，從而實現降序排序（直接修改原列表）。B) 的 `sorted()` 函式也可用，但 C) 是直接使用 `sort()` 方法實現降序。

6.  **D)** A) 和 C) 都是正確的。A) 使用 `filter` 函式搭配 `lambda` 函式返回一個迭代器，包含長度大於 5 的單字。C) 使用列表推導式實現了相同的篩選功能。

7.  **A)** `process_data(1, 2, 3, 4, x=5, y=6)` 會將 `1` 賦值給 `a`，`2` 賦值給 `b`，`3` 和 `4` 收集到 `args` 元組中，`x=5` 和 `y=6` 收集到 `kwargs` 字典中。

8.  **B)** 正確。如果函式沒有顯式的 `return` 語句，Python 會隱式地回傳 `None`。A) 函式可以使用 `return a, b` 回傳多個值，這些值會被封裝成一個元組。D) `return` 語句會終止函式的執行，其後的程式碼不會被執行。

9.  **D)** B) 和 C) 都是正確的。B) 使用 `sorted()` 函式搭配 `lambda` 函式和 `reverse=True` 實現降序排序並返回一個新的列表。C) 使用 `sort()` 方法搭配 `lambda` 函式返回價格的負值作為鍵，直接對原列表進行降序排序。

10. **C)** `y = apply_operation(lambda z: z * z, 5)` 是正確的。`apply_operation` 接收一個函式和一個參數，然後呼叫該函式並傳遞參數。`lambda z: z * z` 定義了一個計算平方的匿名函式，傳遞給 `apply_operation` 後，會計算 `5` 的平方。


### 5.5.7 Exercise

#### 5.5.7.1 函式練習題 (一)：計算投手勝敗投

**題目：**

編寫一個名為 `determine_pitcher_result(innings_pitched, earned_runs, total_runs, is_winning_team)` 的 Python 函式。這個函式接收四個參數：

* `innings_pitched` (浮點數)：投手投球局數。
* `earned_runs` (整數)：投手自責分。
* `total_runs` (整數)：該隊總得分。
* `is_winning_team` (布林值)：一個布林值，表示該投手所屬的球隊是否贏得比賽。

函式應該根據以下規則判斷投手的勝敗投，並回傳一個字串：

* 如果投手投滿 5 局（含）以上，且其所屬球隊贏得比賽，則回傳 `"勝投"`。
* 如果投手投滿 5 局（含）以上，且其所屬球隊輸掉比賽，則回傳 `"敗投"`。
* 如果投手投球未滿 5 局，無論勝敗，都回傳 `"中繼"`。

**請完成以下函式：**

```python
def determine_pitcher_result(innings_pitched, earned_runs, total_runs, is_winning_team):
    result = ""
    # 在這裡填寫你的程式碼來判斷投手的勝敗投
    return result

# 測試你的函式
print(determine_pitcher_result(6.0, 2, 5, True))   # 預期輸出: 勝投
print(determine_pitcher_result(7.0, 1, 3, False))  # 預期輸出: 敗投
print(determine_pitcher_result(4.2, 0, 2, True))   # 預期輸出: 中繼
print(determine_pitcher_result(3.0, 3, 1, False))  # 預期輸出: 中繼
```

#### 5.5.7.2 函式練習題 (二)：格式化球員打擊數據

**題目：**

編寫一個名為 `format_batting_stats(name, at_bats, hits, home_runs)` 的 Python 函式。這個函式接收四個參數：

* `name` (字串)：球員的姓名。
* `at_bats` (整數)：球員的打數。
* `hits` (整數)：球員的安打數。
* `home_runs` (整數)：球員的全壘打數。

函式應該計算球員的打擊率（安打數除以打數，保留三位小數），並回傳一個格式化的字串，包含球員的姓名、打數、安打數、全壘打數和打擊率，格式如下：

```
[球員姓名] 的打擊數據：
打數: [打數]
安打: [安打]
全壘打: [全壘打]
打擊率: [打擊率]
```

**請完成以下函式：**

```python
def format_batting_stats(name, at_bats, hits, home_runs):
    batting_average = 0.0
    # 在這裡計算打擊率
    formatted_string = f"{name} 的打擊數據：\n"
    # 在這裡格式化字串
    return formatted_string

# 測試你的函式
stats = format_batting_stats("陳金鋒", 450, 150, 30)
print(stats)
# 預期輸出 (打擊率可能因計算精度略有不同):
# 陳金鋒 的打擊數據：
# 打數: 450
# 安打: 150
# 全壘打: 30
# 打擊率: 0.333
```

## 5.6. Python 物件導向設計 (Object-Oriented Design)

物件導向程式設計 (OOP) 是一種強大的程式設計範式，它基於「物件」的概念，將資料（屬性）和操作資料的程式碼（方法）組織在一起。Python 是一門支援物件導向的語言，本講義將深入探討 Python 中的物件設計。

### 5.6.1. 物件導向的基本概念

物件導向程式設計的核心思想是將程式中的一切都視為物件。每個物件都具有：

* **屬性 (Attributes):** 物件的特性或狀態，是儲存在物件中的資料。
* **方法 (Methods):** 物件可以執行的操作或行為，是定義在類別中的函式。

物件是類別 (Class) 的實例 (Instance)。類別是創建物件的藍圖或模板，它定義了物件將擁有的屬性和方法。

**主要物件導向原則：**

* **封裝 (Encapsulation):** 將資料（屬性）和操作資料的方法捆綁在一起，並控制對內部細節的存取。
* **繼承 (Inheritance):** 允許一個類別（子類別）繼承另一個類別（父類別）的屬性和方法，實現程式碼重用和擴展。
* **多型 (Polymorphism):** 允許不同類別的物件對相同的方法呼叫做出不同的響應，提高了程式碼的靈活性和可擴展性。

### 5.6.2. 類別 (Class) 的定義

在 Python 中，使用 `class` 關鍵字來定義類別。

```python
class MyClass:
    """這是一個簡單的類別"""
    class_attribute = "我是類別屬性"  # 類別層級的屬性

    def __init__(self, instance_attribute):
        """建構子，初始化物件的屬性"""
        self.instance_attribute = instance_attribute  # 實例層級的屬性

    def instance_method(self):
        """實例方法，操作物件的屬性"""
        return f"我的實例屬性是: {self.instance_attribute}"

    @classmethod
    def class_method(cls):
        """類別方法，操作類別屬性"""
        return f"我的類別屬性是: {cls.class_attribute}"

    @staticmethod
    def static_method():
        """靜態方法，與類別或實例無直接關聯"""
        return "我是一個靜態方法"

# 創建 MyClass 的實例（物件）
obj1 = MyClass("物件一")
obj2 = MyClass("物件二")

# 存取類別屬性
print(MyClass.class_attribute)  # 輸出: 我是類別屬性
print(obj1.class_attribute)   # 輸出: 我是類別屬性 (透過實例存取)

# 存取實例屬性
print(obj1.instance_attribute) # 輸出: 物件一
print(obj2.instance_attribute) # 輸出: 物件二

# 呼叫實例方法
print(obj1.instance_method())  # 輸出: 我的實例屬性是: 物件一

# 呼叫類別方法
print(MyClass.class_method()) # 輸出: 我的類別屬性是: 我是類別屬性

# 呼叫靜態方法
print(MyClass.static_method()) # 輸出: 我是一個靜態方法
```

* **類別屬性 (Class Attribute):** 在類別定義中，但在任何方法之外定義的屬性。所有該類別的實例共享相同的類別屬性。
* **建構子 (`__init__`)**: 一個特殊的方法，在創建類別的新實例時自動調用。它通常用於初始化物件的屬性。`self` 參數指向被創建的物件本身。
* **實例屬性 (Instance Attribute):** 在 `__init__` 方法（或其他實例方法）中使用 `self.attribute_name = value` 創建的屬性。每個物件實例都擁有自己的一組實例屬性。
* **實例方法 (Instance Method):** 以 `self` 作為第一個參數的方法。實例方法可以存取和修改物件的實例屬性。
* **類別方法 (Class Method):** 使用 `@classmethod` 裝飾器標記的方法。它的第一個參數是 `cls`，指向類別本身，而不是實例。類別方法可以存取和修改類別屬性。
* **靜態方法 (Static Method):** 使用 `@staticmethod` 裝飾器標記的方法。它沒有 `self` 或 `cls` 參數，它只是在類別的命名空間中組織的普通函式，與類別或實例的狀態沒有直接關聯。

### 5.6.3. 物件屬性的取得與修改

創建物件後，可以使用點號 `.` 來存取和修改其屬性。

**取得屬性:**

```python
my_object = MyClass("我的物件")
print(my_object.instance_attribute) # 輸出: 我的物件
print(my_object.class_attribute)  # 輸出: 我是類別屬性
```

**修改屬性:**

```python
my_object.instance_attribute = "修改後的物件"
print(my_object.instance_attribute) # 輸出: 修改後的物件

MyClass.class_attribute = "修改後的類別屬性"
print(my_object.class_attribute)  # 輸出: 修改後的類別屬性 (所有實例都會受到影響)
```

**注意事項:**

* 直接存取和修改屬性有時可能違反封裝原則。為了更好地控制屬性的存取和修改，可以使用 `property`。

### 5.6.4. 使用 `property` 控制屬性存取

`property` 是一種內建的函式，用於創建**受管理的屬性 (Managed Attributes)**。它可以讓我們在存取、修改或刪除物件屬性時執行額外的程式碼（例如驗證、計算等），同時保持使用點號 `.` 存取屬性的語法不變。

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # 使用單底線表示這是一個「受保護的」屬性

    def get_radius(self):
        """取得半徑"""
        return self._radius

    def set_radius(self, value):
        """設定半徑，並進行驗證"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("半徑不能為負數")

    def delete_radius(self):
        """刪除半徑屬性"""
        del self._radius

    radius = property(get_radius, set_radius, delete_radius, "圓的半徑屬性")

    def area(self):
        return 3.14159 * self.radius ** 2  # 使用 property 名稱存取

my_circle = Circle(5)

# 取得半徑 (實際上呼叫了 get_radius 方法)
print(my_circle.radius)  # 輸出: 5

# 設定半徑 (實際上呼叫了 set_radius 方法)
my_circle.radius = 10
print(my_circle.radius)  # 輸出: 10

# 嘗試設定無效的半徑
try:
    my_circle.radius = -1
except ValueError as e:
    print(e)  # 輸出: 半徑不能為負數

# 刪除半徑屬性 (實際上呼叫了 delete_radius 方法)
del my_circle.radius
# print(my_circle.radius) # 會拋出 AttributeError: 'Circle' object has no attribute '_radius'

print(my_circle.area()) # 如果半徑存在，會計算面積
```

**使用裝飾器 (@property) 的簡潔語法:**

更常見且更 Pythonic 的方式是使用裝飾器來定義 `property`。

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        """取得寬度"""
        return self._width

    @width.setter
    def width(self, value):
        """設定寬度，並進行驗證"""
        if value >= 0:
            self._width = value
        else:
            raise ValueError("寬度不能為負數")

    @property
    def height(self):
        """取得高度"""
        return self._height

    @height.setter
    def height(self, value):
        """設定高度，並進行驗證"""
        if value >= 0:
            self._height = value
        else:
            raise ValueError("高度不能為負數")

    def area(self):
        return self.width * self.height  # 使用 property 名稱存取

my_rectangle = Rectangle(10, 5)
print(my_rectangle.width)   # 輸出: 10
my_rectangle.height = 8
print(my_rectangle.area())  # 輸出: 80

try:
    my_rectangle.width = -2
except ValueError as e:
    print(e)  # 輸出: 寬度不能為負數
```

* `@property`: 將一個方法（通常是 `get_attribute`）轉換為一個屬性。當你存取 `my_rectangle.width` 時，實際上是呼叫了 `width()` 方法。
* `@width.setter`: 將一個方法（通常是 `set_attribute`）與 `@property` 定義的 `width` 屬性關聯起來，用於設定屬性的值。當你執行 `my_rectangle.width = value` 時，實際上是呼叫了 `width(self, value)` 方法。
* `@width.deleter`: (可選) 將一個方法與 `@property` 定義的 `width` 屬性關聯起來，用於刪除屬性。

使用 `property` 可以更好地實現封裝，並在屬性存取時添加額外的邏輯，而不會改變使用者存取屬性的方式。

### 5.6.5. 繼承 (Inheritance)

繼承是一種機制，允許一個類別（子類別或衍生類別）繼承另一個類別（父類別或基底類別）的屬性和方法。子類別可以重用父類別的程式碼，並可以擴展或修改父類別的功能。

**基本語法:**

```python
class ParentClass:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} 發出聲音。")

class ChildClass(ParentClass):
    def __init__(self, name, sound):
        super().__init__(name)  # 呼叫父類別的建構子
        self.sound = sound

    def speak(self):
        super().speak()  # 呼叫父類別的 speak 方法
        print(f"{self.name} 發出 {self.sound} 的聲音。")

parent = ParentClass("父類別")
child = ChildClass("子類別", "汪汪")

parent.speak()  # 輸出: 父類別 發出聲音。
child.speak()   # 輸出:
                # 子類別 發出聲音。
                # 子類別 發出 汪汪 的聲音。

print(child.name)  # 子類別繼承了父類別的屬性
```

* **`class ChildClass(ParentClass):`**: 表示 `ChildClass` 繼承自 `ParentClass`。
* **`super().__init__(name)`**: 使用 `super()` 函數呼叫父類別的 `__init__` 方法，確保父類別的初始化邏輯被執行。
* **方法覆寫 (Method Overriding):** 子類別可以定義與父類別中同名的方法，從而修改或擴展父類別的功能。在 `ChildClass` 中，`speak()` 方法被覆寫。
* **`super().speak()`**: 在子類別的 `speak()` 方法中，可以使用 `super()` 呼叫父類別的 `speak()` 方法，以重用父類別的行為。

**繼承的優點：**

* **程式碼重用 (Code Reusability):** 子類別可以繼承父類別的屬性和方法，避免重複編寫相同的程式碼。
* **擴展性 (Extensibility):** 子類別可以在不修改父類別的情況下，添加新的屬性和方法，或者修改繼承的方法。
* **可維護性 (Maintainability):** 繼承使得類別的層次結構更清晰，易於理解和維護。
* **多型 (Polymorphism):** 允許使用父類別的引用來操作子類別的物件，並根據物件的實際類型執行相應的方法。

**多重繼承 (Multiple Inheritance):**

Python 支援一個類別繼承多個父類別。語法如下：

```python
class Mother:
    def say_hello(self):
        print("Hello from Mother")

class Father:
    def say_hi(self):
        print("Hi from Father")

class Child(Mother, Father):
    pass

child = Child()
child.say_hello() # 輸出: Hello from Mother
child.say_hi()    # 輸出: Hi from Father
```

多重繼承需要謹慎使用，因為它可能導致命名衝突（當多個父類別具有相同名稱的屬性或方法時）和複雜的繼承關係。Python 使用方法解析順序 (Method Resolution Order, MRO) 來決定當呼叫一個繼承自多個父類別的方法時，應該執行哪個父類別的方法。可以使用 `Child.mro()` 來查看 MRO。

### 5.6.6. 物件導向設計的應用

物件導向設計廣泛應用於各種軟體開發領域：

* **GUI 應用程式 (例如 Tkinter, PyQt)：** 視窗、按鈕、文本框等 UI 元素通常被設計為物件。
* **Web 框架 (例如 Django, Flask)：** 模型 (Models) 代表資料庫中的資料，視圖 (Views) 處理使用者請求，這些通常都使用類別和物件來實現。
* **遊戲開發 (例如 Pygame)：** 遊戲角色、場景、道具等都是物件。
* **資料庫互動 (例如 SQLAlchemy)：** 物件可以用來映射資料庫中的表格和記錄。
* **科學計算和資料分析 (例如 NumPy, Pandas)：** 雖然這些庫的核心是用 C 或 Fortran 編寫的，但它們在 Python 中的介面通常使用物件來表示陣列、資料框等資料結構。

總之，掌握 Python 的物件導向設計對於編寫組織良好、可重用、易於維護和擴展的程式碼至關重要。理解類別、物件、屬性、方法、`property` 和繼承等概念是成為一名高效 Python 開發者的基礎。

### 5.6.7 Check

**Python 物件設計選擇題**

1.  下列關於 Python 類別定義的敘述，何者正確？
    A) 類別使用關鍵字 `struct` 定義。
    B) 類別中定義的變數一定是物件屬性。
    C) 類別可以使用 `pass` 關鍵字來定義一個空類別。
    D) 類別名稱必須以小寫字母開頭。

2.  關於類別屬性 (Class Attribute) 和物件屬性 (Instance Attribute) 的差異，下列敘述何者正確？
    A) 類別屬性在每個物件實例中都是不同的，而物件屬性在所有實例中共享相同的值。
    B) 類別屬性屬於類別本身，而物件屬性屬於物件實例。
    C) 物件屬性在類別定義時被賦值，而類別屬性在物件創建時被賦值。
    D) 兩者在使用上沒有本質區別，只是定義的位置不同。

3.  在 Python 中，如何存取物件的屬性？
    A) 使用 `object->attribute` 的箭頭符號。
    B) 直接使用屬性名稱。
    C) 使用點號 `.` 後跟屬性名稱。
    D) 將屬性名稱作為字串傳遞給物件的 `get()` 方法。

4.  關於 Python 類別的建構方法 `__init__(self, ...)`，下列敘述何者正確？
    A) 它是一個可選的方法，類別不一定需要定義。
    B) 它在創建類別時自動被呼叫。
    C) 它的主要作用是定義類別的方法。
    D) 它的第一個參數 `self` 可以被替換為其他名稱。

5.  `self` 參數在 Python 的類別方法中代表什麼？
    A) 代表類別本身。
    B) 代表呼叫該方法的物件實例。
    C) 代表父類別。
    D) 代表模組的全域命名空間。

6.  `property` 在 Python 物件設計中的主要作用是什麼？
    A) 用於定義類別的靜態方法。
    B) 用於實現多重繼承。
    C) 用於控制對物件屬性的存取和修改。
    D) 用於定義類別的建構子。

7.  考慮以下程式碼片段：
    ```python
    class Parent:
        def method(self):
            print("Parent method")

    class Child(Parent):
        def method(self):
            print("Child method")

    obj = Child()
    obj.method()
    ```
    程式碼的輸出將會是什麼？
    A) `Parent method`
    B) `Child method`
    C) `Parent method` 和 `Child method` 都會被印出。
    D) 會產生錯誤。

8.  在 Python 的繼承中，如果子類別想要呼叫父類別中被覆寫的方法，應該使用哪個函數？
    A) `super()`
    B) `self()`
    C) `parent()`
    D) `base()`

9. 下列哪個關於 Python 物件設計的原則最能提高程式碼的重用性？
    A) 封裝 (Encapsulation)
    B) 抽象化 (Abstraction)
    C) 繼承 (Inheritance)
    D) 多型 (Polymorphism)

10. 在 Python 中，使用雙底線開頭的屬性名稱 (例如 `__private_attribute`) 具有什麼特殊意義？
    A) 它表示該屬性是唯讀的，不能在類別外部修改。
    B) 它會觸發 Python 的名稱修飾 (name mangling) 機制，使其難以在類別外部直接存取。
    C) 它表示該屬性是類別屬性，而不是物件屬性。
    D) 它會使該屬性在繼承時不會被子類別繼承。

---

**答案與解析：**

1.  **C)** 正確。可以使用 `pass` 關鍵字定義一個不包含任何屬性和方法的空類別。A) 類別使用 `class` 關鍵字定義。B) 在類別中定義的變數可以是類別屬性或在方法中定義的局部變數。D) 類別名稱通常遵循駝峰命名法，首字母大寫。

2.  **B)** 正確。類別屬性是屬於類別本身的，所有實例共享；物件屬性是屬於每個物件實例的，每個實例可以有不同的值。

3.  **C)** 正確。使用點號 `.` 後跟屬性名稱來存取物件的屬性。

4.  **B)** 正確。`__init__` 是建構子，在物件創建後會自動被呼叫以初始化物件。A) 如果沒有定義 `__init__`，物件會使用預設的建構行為。C) `__init__` 的主要作用是初始化屬性。D) `self` 是慣例名稱，雖然可以替換，但不建議。

5.  **B)** 正確。`self` 指向呼叫該方法的物件實例。

6.  **C)** 正確。`property` 用於創建受管理的屬性，可以控制屬性的讀取、設定和刪除行為。

7.  **B)** `Child method`。子類別 `Child` 覆寫了父類別 `Parent` 的 `method`，當呼叫子類別物件的 `method` 時，會執行子類別的版本。

8.  **A)** `super()`。`super()` 函數用於呼叫父類別的方法。

9. **C)** 繼承允許子類別重用父類別的程式碼，從而提高程式碼的重用性。

10. **B)** 正確。以雙底線開頭的屬性名稱會觸發 Python 的名稱修飾機制，將屬性名稱改為 `_ClassName__attributeName` 的形式，使其在類別外部難以直接存取，但並非完全不能存取。

### 5.6.8 Exercise

#### 5.6.8.1 棒球員
請設計一個名為 `BaseballPlayer` 的類別，用於表示一位棒球員。這個類別應該包含以下屬性：

* `name` (字串)：球員的姓名。
* `number` (整數)：球員的背號。
* `position` (字串)：球員守備位置（例如："投手", "捕手", "一壘手" 等）。
* `batting_average` (浮點數)：球員的打擊率（初始值為 0.0）。
* `home_runs` (整數)：球員的全壘打數（初始值為 0）。

這個類別應該包含以下方法：

1.  `__init__(self, name, number, position)`：建構子，用於初始化球員的姓名、背號和守備位置。打擊率和全壘打數應初始化為預設值。
2.  `display_info(self)`：顯示球員的所有資訊，包括姓名、背號、守備位置、打擊率和全壘打數。
3.  `increase_batting_record(self, hits, at_bats)`：更新球員的打擊紀錄。這個方法接收本次打擊的安打數 (`hits`) 和打數 (`at_bats`)，並根據這些資訊更新球員的 `batting_average`。請注意，打擊率的計算方式是總安打數除以總打數。
4.  `hit_home_run(self)`：當球員擊出全壘打時呼叫此方法，將球員的 `home_runs` 增加 1。

**操作要求：**

1.  創建至少三位 `BaseballPlayer` 物件，並賦予他們不同的姓名、背號和守備位置。
2.  針對其中一位球員，呼叫 `display_info()` 方法顯示其初始資訊。
3.  讓其中一位球員進行兩次打擊紀錄更新：
    * 第一次打擊：2 安打，3 打數。
    * 第二次打擊：1 安打，4 打數。
    每次更新後，都呼叫 `display_info()` 方法查看該球員的最新資訊。
4.  讓其中一位球員擊出一支全壘打，並呼叫 `display_info()` 方法查看其全壘打數是否已更新。

**進階挑戰：**

* 為 `BaseballPlayer` 類別添加一個 `__str__(self)` 方法，使其在使用 `print()` 函數列印球員物件時，能以更友好的格式顯示球員資訊。
* 創建一個球隊 (Team) 類別，該類別可以儲存多個 `BaseballPlayer` 物件，並提供方法來新增球員、顯示球隊所有球員資訊，以及計算球隊的平均打擊率。

## 5.7 列舉型態

列舉 (Enumeration) 是一種將一組具名的常數綁定在一起的方式。它可以使程式碼更具可讀性和可維護性，因為它使用有意義的名稱來代替隨機的數值或字串。Python 從 3.4 版本開始引入了 `enum` 模組來支援列舉型態。

### 5.7.1 為什麼需要列舉型態？

在沒有列舉型態的情況下，我們可能會使用常數變數來表示一組相關的值：

```python
STATUS_PENDING = 1
STATUS_PROCESSING = 2
STATUS_COMPLETED = 3
STATUS_FAILED = 4

def process_order(status):
    if status == STATUS_PENDING:
        print("Order is pending.")
    elif status == STATUS_PROCESSING:
        print("Order is being processed.")
    elif status == STATUS_COMPLETED:
        print("Order is completed.")
    elif status == STATUS_FAILED:
        print("Order failed.")
    else:
        print("Invalid status code.")
```

這樣做有一些潛在的問題：

* **可讀性差:** 數字的意義不明確，需要查看常數的定義才能理解。
* **易出錯:** 可以傳入任意整數值，即使這些值不是有效的狀態。
* **命名衝突:** 常數變數可能與其他變數名稱衝突。

列舉型態可以有效地解決這些問題。

### 5.7.2 定義列舉型態

要使用列舉型態，首先需要導入 `enum` 模組中的 `Enum` 類別，然後通過繼承 `Enum` 來創建自己的列舉類別。

```python
from enum import Enum

class Status(Enum):
    PENDING = 1
    PROCESSING = 2
    COMPLETED = 3
    FAILED = 4

# 你也可以使用字串作為值
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
```

* `Status` 和 `Color` 是我們定義的列舉類別，它們繼承自 `Enum`。
* `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`, `RED`, `GREEN`, `BLUE` 是列舉的成員 (members)，它們是 `Status` 和 `Color` 的實例。
* 等號右邊的值是與每個成員關聯的值。這些值可以是整數、字串或其他不可變的型別。

### 5.7.3 存取列舉成員和值

可以使用點號 `.` 來存取列舉的成員：

```python
print(Status.PENDING)     # 輸出: Status.PENDING
print(Status.COMPLETED)   # 輸出: Status.COMPLETED
```

要獲取成員的值，可以使用 `.value` 屬性：

```python
print(Status.PENDING.value)   # 輸出: 1
print(Color.RED.value)      # 輸出: red
```

也可以通過成員的名稱（字串）來存取列舉成員：

```python
print(Status['PROCESSING'])  # 輸出: Status.PROCESSING
print(Color['BLUE'])        # 輸出: Color.BLUE
```

### 5.7.4 列舉成員的特性

* **唯一性:** 在同一個列舉中，成員的名稱必須是唯一的。
* **不可變性:** 列舉成員是常數，一旦定義就不能修改它們的值。
* **可迭代性:** 列舉類別是可迭代的，可以遍歷其所有成員（不包括別名，見後續說明）。

```python
for status in Status:
    print(f"{status.name} -> {status.value}")
# 輸出:
# PENDING -> 1
# PROCESSING -> 2
# COMPLETED -> 3
# FAILED -> 4
```

* **比較:** 可以使用 `==` 和 `!=` 來比較列舉成員是否相等（比較的是成員本身，而不是它們的值）。

```python
if Status.PENDING == Status.PENDING:
    print("They are the same status.")

if Status.PENDING != Status.PROCESSING:
    print("They are different statuses.")

# 不能將列舉成員與其值直接比較
# if Status.PENDING == 1:  # 會得到 False
#     pass
```

### 5.7.5 別名 (Aliases)

預設情況下，如果多個成員具有相同的值，那麼只有第一個定義的成員會被視為主要的成員，其他的會成為它的別名。當迭代列舉時，別名不會被包含在內。

```python
class ErrorCode(Enum):
    OK = 0
    SUCCESS = 0  # SUCCESS 是 OK 的別名
    WARNING = 1
    ERROR = 2

print(ErrorCode.OK)       # 輸出: ErrorCode.OK
print(ErrorCode.SUCCESS)  # 輸出: ErrorCode.OK
print(ErrorCode.OK is ErrorCode.SUCCESS) # 輸出: True

for code in ErrorCode:
    print(code)
# 輸出:
# ErrorCode.OK
# ErrorCode.WARNING
# ErrorCode.ERROR
```

如果你希望允許多個成員具有相同的值並且都被視為獨立的成員，可以使用 `@enum.unique` 裝飾器。如果發現重複的值，它會拋出 `ValueError`。

```python
import enum

@enum.unique
class UniqueErrorCode(Enum):
    OK = 0
    # SUCCESS = 0  # 會拋出 ValueError: Duplicate value found: 0
    WARNING = 1
    ERROR = 2
```

### 5.7.6 在程式中使用列舉

使用列舉可以使程式碼更清晰和安全：

```python
def process_order_with_enum(status: Status):
    if status == Status.PENDING:
        print("Order is pending (using enum).")
    elif status == Status.PROCESSING:
        print("Order is being processed (using enum).")
    elif status == Status.COMPLETED:
        print("Order is completed (using enum).")
    elif status == Status.FAILED:
        print("Order failed (using enum).")
    else:
        print("Invalid status (using enum).")

process_order_with_enum(Status.PROCESSING)  # 安全且易讀
# process_order_with_enum(2)                # 會觸發類型提示警告 (如果使用了類型檢查工具)
# process_order_with_enum("PROCESSING")     # 會觸發類型提示警告
```

### 5.7.7 與 JavaScript 的比較

JavaScript 在語言核心中沒有內建的列舉型態。在 JavaScript 中，通常會使用物件來模擬列舉：

```javascript
const Status = {
  PENDING: 1,
  PROCESSING: 2,
  COMPLETED: 3,
  FAILED: 4
};

function processOrder(status) {
  if (status === Status.PENDING) {
    console.log("Order is pending (in JS).");
  } else if (status === Status.PROCESSING) {
    console.log("Order is being processed (in JS).");
  } // ...
}

processOrder(Status.PROCESSING);
```

或者使用立即調用函式表達式 (IIFE) 來創建更嚴格的列舉模擬：

```javascript
const Color = (() => {
  const RED = "red";
  const GREEN = "green";
  const BLUE = "blue";
  return Object.freeze({ RED, GREEN, BLUE });
})();

console.log(Color.RED);
```

**比較:**

* Python 提供了專門的 `enum` 模組，具有內建的語法和特性來支援列舉型態，例如成員的唯一性、可迭代性等。
* JavaScript 需要使用物件或函數來模擬列舉，缺乏語言層面的直接支援。雖然可以實現類似的功能，但可能不如 Python 的 `enum` 模組那麼方便和安全。
* TypeScript 是 JavaScript 的一個超集，它引入了 `enum` 關鍵字，提供了與 Python 列舉型態更接近的功能。

### 5.7.8 Check

1.  下列關於 Python 列舉型態 (`enum`) 的敘述，何者正確？
    A) 列舉成員的值必須是唯一的整數。
    B) 可以使用比較運算符（如 `>`、`<`）直接比較不同列舉的成員。
    C) 列舉類別是可迭代的，可以遍歷其所有成員。
    D) 列舉成員的名稱在定義後可以被修改。

2.  考慮以下列舉定義：
    ```python
    from enum import Enum

    class Status(Enum):
        PENDING = 1
        RUNNING = 2
        COMPLETED = 1
    ```
    當執行 `print(Status.PENDING is Status.COMPLETED)` 時，輸出會是什麼？
    A) `True`
    B) `False`
    C) 會因為重複的值而產生 `ValueError`。
    D) 無法預測。

3.  給定以下列舉定義：
    ```python
    from enum import Enum

    class Color(Enum):
        RED = "red"
        GREEN = "green"
        BLUE = "blue"
    ```
    下列哪個存取列舉成員的方式是正確的？
    A) `Color[0]`
    B) `Color.1`
    C) `Color('red')`
    D) `Color.RED.name`

---

**答案與解析：**

1.  **C)** 正確。列舉類別是可迭代的，可以遍歷其所有成員。
    * A) 列舉成員的值可以是整數、字串或其他不可變的型別。
    * B) 不建議直接比較不同列舉的成員，通常只比較相同列舉內的成員是否相等。
    * D) 列舉成員的名稱在定義後是不可修改的。

2.  **A)** `True`。在預設情況下，如果多個列舉成員具有相同的值，那麼它們會被視為彼此的別名，`is` 運算符會判斷它們是否是同一個物件。因此，`Status.PENDING` 和 `Status.COMPLETED` 在這個例子中指向同一個成員。**注意：** 如果在定義列舉時使用了 `@enum.unique` 裝飾器，則會因為重複的值而拋出 `ValueError`。

3.  **D)** `Color.RED.name` 是正確的。
    * A) 列舉不支援像列表一樣的數字索引存取。
    * B) 列舉成員名稱不能以數字開頭。
    * C) 可以使用列舉值來存取成員，例如 `Color("red")` 會回傳 `Color.RED`。`Color.RED.name` 則會回傳成員的名稱字串 `"RED"`。


## 5.8. 模組的引入

### 5.8.1 引入模組（Module）

在 Python 中，模組是一個包含 Python 定義和語句的文件，通常以 `.py` 結尾。引入模組可以讓你使用該模組中定義的函式、類別和變數。以下是常見的引入模組的方法：

**1. 使用 `import module_name`**

這是最基本的引入模組的方式。它會將整個模組引入到當前的命名空間中，但你需要使用模組名作為前綴來存取其中的內容。

```python
import math

# 使用 math 模組中的函式
result = math.sqrt(16)
print(result)  # 輸出: 4.0

pi_value = math.pi
print(pi_value)  # 輸出: 3.141592653589793
```

**2. 使用 `import module_name as alias`**

你可以為引入的模組指定一個別名，這樣在存取模組內容時可以使用更簡短或更具描述性的名稱。

```python
import datetime as dt

# 使用 dt 別名存取 datetime 模組
now = dt.datetime.now()
print(now)
```

**3. 使用 `from module_name import name1, name2, ...`**

這種方式可以從指定的模組中引入特定的名稱（函式、類別、變數）。引入的名稱會直接加入到當前的命名空間中，可以直接使用，無需模組名前綴。

```python
from os import path, getcwd

# 直接使用 path 和 getcwd 函式
file_path = path.join(getcwd(), "my_file.txt")
print(file_path)
```

**4. 使用 `from module_name import name as alias`**

你可以為從模組中引入的特定名稱指定別名。

```python
from collections import defaultdict as dd

# 使用 dd 別名存取 defaultdict 類別
my_dict = dd(int)
my_dict['a'] += 1
print(my_dict)  # 輸出: defaultdict(<class 'int'>, {'a': 1})
```

**5. 使用 `from module_name import *`**

這種方式會將模組中所有**公開的**名稱（不以單個底線 `_` 開頭的名稱）都引入到當前的命名空間中。**然而，這種做法通常被認為是不好的實踐，因為它可能導致命名衝突，使得程式碼難以理解和維護。**

```python
# 不推薦使用
from math import *

result = sqrt(25)
print(result)  # 輸出: 5.0
```

### 5.8.2 引入類別（Class）

類別通常定義在模組中，所以引入類別的方法與引入模組中的其他名稱（如函式）相同。

**1. 使用 `import module_name` 後，透過模組名存取類別**

```python
import my_module

# 假設 my_module.py 中定義了 MyClass
obj = my_module.MyClass()
obj.some_method()
```

**2. 使用 `from module_name import ClassName` 直接引入類別**

```python
from my_module import MyClass

# 直接使用 MyClass
obj = MyClass()
obj.some_method()
```

**3. 使用 `from module_name import ClassName as alias` 為類別指定別名**

```python
from my_module import MyClass as MC

# 使用 MC 別名存取 MyClass
obj = MC()
obj.some_method()
```

### 5.8.3 整理

| 引入方式                                    | 描述                                 | 優點                                       | 缺點                                                 | 適用場景                                                                 |
| ------------------------------------------- | ------------------------------------ | ------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------------------ |
| `import module_name`                        | 引入整個模組，使用時需要模組名前綴。 | 命名空間清晰，不易衝突。                   | 存取模組內容時較冗長。                               | 引入大型模組或需要頻繁使用多個模組時。                                   |
| `import module_name as alias`               | 引入整個模組並指定別名。             | 簡化模組名稱，命名空間清晰。               | 仍然需要使用別名前綴。                               | 當模組名稱較長或想使用更具描述性的名稱時。                               |
| `from module_name import name1, name2, ...` | 從模組中引入特定名稱，可以直接使用。 | 直接存取，程式碼更簡潔。                   | 可能導致命名衝突。                                   | 當只需要使用模組中的少數幾個名稱時。                                     |
| `from module_name import name as alias`     | 從模組中引入特定名稱並指定別名。     | 簡化特定名稱，程式碼更簡潔，避免命名衝突。 |                                                      | 當模組中的名稱較長或與當前命名空間中的名稱衝突時。                       |
| `from module_name import *`                 | 引入模組中所有公開名稱（不推薦）。   | 最簡潔的引入方式。                         | 極易導致命名衝突，程式碼可讀性差，難以追蹤名稱來源。 | 通常應避免使用。只有在非常清楚模組內容且不會造成衝突的小範圍內偶爾使用。 |

在實際編程中，推薦使用 `import module_name` 或 `from module_name import specific_names` 的方式，以保持程式碼的清晰度和可維護性。避免使用 `from module_name import *`。

# Exercise

## BMI

1. 設計一個函式輸入為字串型態的身高與體重，輸出 BMI
2. 設計一個函式，輸入為 BMI, 輸出為健康狀態

```python=
def getBMI(h: str, w: str)-> float: # type hint
    h = float(h)/100
    bmi = round(w/(h*h), 2)
    return bmi

def evaBMI(bmi): # function
  if bmi > 20: # logic control
    print ("Too fat")
  elif bmi < 10:
    print ("Too light")
  else:
    print ("Fit")

h = 1.7 # variable
w = 60

bmi = getBMI(h, w) # call function
print ('bmi', bmi)
evaBMI (bmi)
```

<iframe src="https://player.soundon.fm/embed/?podcast=4dc5f80a-7107-47d1-b55d-249fd94fe577&episode=0f6cb72d-860d-43f1-af37-ef69a24f7933" style="height: 140px; width: 100%; border: none; border-radius: 4px; box-shadow: 0 1px 8px rgba(0, 0, 0, .2);"></iframe>

## 陣列練習

有三個陣列，儲存四個人的姓名，身高與體重。呼叫上述的函式，輸出他們的 BMI 與健康狀態

```python=
names = ['John', 'Mary', 'Nick', 'Albert'] # list
heights = [170, 172, 160, 165]
weights = [60, 62, 90, 76]

for i in range(len(names)): # for range
  name, h, w = names[i], float(heights[i]), int(weights[i])

  # python f-string
  print (f'Name: {names[i]}, {h}m, {w}kg , bmi={getBMI(h, w)}')
```

## 字串輸出
* `print (f'{n} 的身高 {h}m, 體重{w}kg')` 其中 b, h, w 為變數
* `print ('{} 的身高 {}m, 體重 {}kg'.format(n, m, w)` 其中 b, h, w 為變數

<iframe src="https://player.soundon.fm/embed/?podcast=4dc5f80a-7107-47d1-b55d-249fd94fe577&episode=bb7547d8-ac5c-4608-99e7-bfdf0e8417d7" style="height: 140px; width: 100%; border: none; border-radius: 4px; box-shadow: 0 1px 8px rgba(0, 0, 0, .2);"></iframe>

## dict 練習

同上，資料由 dict 來儲存，而不是陣列。

```python
# dict
group = {'john': ('John', 172, 68),
        'nick': ('Nick', 180, 58),
        'mary': ('Mary', 160, 90),}
```

dic 的結構，其中 'john' 是 `key`, ('John', 172, 68) 是 `value`。

請用迴圈讀取 group 內的資料，計算出他們的 bmi 後列出

```python=
for p_id in group:
    p_value = group[p_id]
    n, h, w = p_value[0], p_value[1], p_value[2]
    print(f"The weight, height and BMI of {n} is {h}, {w} and {getBMI(h, w)}")
```

也可以直接用 `.items()` 直接獲取 key 與 value

```python=
for p_id, p_value in group.items():
    n, h, w = p_value[0], p_value[1], p_value[2]
    print(f"The weight, height and BMI of {n} is {h}, {w} and {getBMI(h, w)}")
```