# 第八章 Python 快速入門 (精簡版)

> **目標**：專為具備 JavaScript 基礎的資工系學生設計，聚焦於進入 Django 開發所需的 Python 核心語法。
> **時間安排**：1 小時講授 + 2 小時練習。

---

## 8.1 課程導引：為什麼是 Python？

對於習慣 JavaScript 的開發者來說，Python 的哲學是「顯式優於隱式」(Explicit is better than implicit)。
在 Django 中，你會發現 Python 讓後端邏輯變得非常結構化且易於維護。

- **JS**: 多種寫法，靈活但容易混亂（Callback hell, `this` 指向問題）。
- **Python**: 規定嚴格（縮排即區塊），代碼如散文。

---

## 8.2 開發環境與套件管理 (10 分鐘)

在 Django 開發中，隔離環境是基本功。這相當於 JS 世界中的 `node_modules` 隔離。

### 8.2.1 虛擬環境 (Virtual Environment)
Python 使用 `venv` 來建立獨立的開發空間。

```bash
# 1. 建立虛擬環境 (在專案目錄下)
python -m venv venv

# 2. 啟動環境
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 啟動後，你的終端機提示字元會出現 (venv) 字樣
```

### 8.2.2 套件管理 (Pip vs NPM)
| 功能 | Python (pip) | JavaScript (npm) |
| :--- | :--- | :--- |
| 安裝套件 | `pip install django` | `npm install django` |
| 列出已安裝 | `pip freeze` | `npm list` |
| 依賴檔案 | `requirements.txt` | `package.json` |
| 批量安裝 | `pip install -r requirements.txt` | `npm install` |

### 8.2.3 模組匯入 (Module Import)
在 Python 中，匯入模組的方式比 JS 更直覺，但也有幾種常見變體：

| 語法 | 說明 | JS 對照 |
| :--- | :--- | :--- |
| `import math` | 匯入整個模組 | `import * as math from 'math'` |
| `from math import sqrt` | 匯入特定功能 | `import { sqrt } from 'math'` |
| `import pandas as pd` | 匯入並取別名 | `import * as pd from 'pandas'` |
| `from django.urls import path` | 從子套件匯入 | `import { path } from 'django/urls'` |

**注意：**
1. **路徑符號**：Python 使用點號 `.` 作為路徑分隔符（例如 `django.db.models`），而非斜線 `/`。
2. **`__init__.py`**：如果你看到一個目錄下有這個檔案，代表 Python 將該目錄視為一個「套件 (Package)」。在 Django 中，這讓你可以跨目錄匯入 Model 或 View。

---

## 8.3 Python vs JavaScript 語法對照 (15 分鐘)

### 8.3.1 核心差異速查
| 特性 | Python | JavaScript |
| :--- | :--- | :--- |
| **區塊定義** | **強制縮排 (Indentation)** | 花括號 `{ }` |
| **語句結尾** | 換行 | 分號 `;` (非強制) |
| **空值** | `None` | `null` / `undefined` |
| **邏輯運算** | `and`, `or`, `not` | `&&`, `||`, `!` |
| **布林值** | `True`, `False` (首字母大寫) | `true`, `false` |

### 8.3.2 基礎資料結構
Python 的資料結構非常直覺，但有些細微差別：

```python
# 1. List (類似 JS Array)
fruits = ["apple", "banana"]
fruits.append("cherry")  # JS: push()

# 2. Dictionary (類似 JS Object/JSON)
# 注意：Key 必須是字串或不可變物件，且存取需用 ["key"]
user = {"name": "Alice", "age": 20}
print(user["name"])      # JS: user.name 或 user["name"]

# 3. Tuple (不可變清單) - JS 無直接對應
# 用於確保資料不被修改，如資料庫連線資訊
point = (10, 20)

# 4. Set (集合)
unique_ids = {1, 2, 2, 3} # 結果為 {1, 2, 3}
```

### 8.3.3 字串處理 (f-strings)
Python 3.6+ 的 f-string 效能極佳且易讀，類似於 JS 的 Template Literals。

```python
name = "Django"
# Python:
print(f"Hello, {name}!")

# JS:
# console.log(`Hello, ${name}!`);
```

---

1️⃣ 在 Python 中，下列哪一個邏輯運算式的結果與 JavaScript 的 `! (a && b)` 邏輯上最接近？
- (A) `not a and b`
- (B) `not (a and b)`
- (C) `a and not b`
- (D) `! (a && b)`

<details>
<summary>解答</summary>
(B)。
說明：Python 使用 `not`, `and`, `or` 作為關鍵字，並使用小括號來控制優先權。
</details>

---

## 8.4 進階函式與裝飾器 (10 分鐘)

### 8.4.1 型別暗示 (Type Hints)
現代 Python (及 Django) 強烈建議加上型別暗示，這類似於 TypeScript，能增加程式碼可讀性。

```python
def add_score(current: int, bonus: int) -> int:
    return current + bonus
```

### 8.4.2 參數解構 (*args, **kwargs)
在 Django 的原始碼中，你會頻繁看到 `*args` 和 `**kwargs`。它們用於接收不定數量的參數。

- `*args`: 接收多個「位置參數」，包裝成 **Tuple**。
- `**kwargs`: 接收多個「關鍵字參數」，包裝成 **Dictionary**。

```python
def create_user(username, **kwargs):
    print(f"Creating {username}...")
    if "email" in kwargs:
        print(f"Email: {kwargs['email']}")

create_user("nick", email="nick@example.com", age=25)
```

### 8.4.3 裝飾器 (Decorators)
裝飾器是 Django 的靈魂（例如 `@login_required`）。它本質上是一個「包裝函式」，在不修改原函式程式碼的情況下增加功能。

```python
def my_decorator(func):
    def wrapper():
        print("--- 執行前 ---")
        func()
        print("--- 執行後 ---")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

---

## 8.5 物件導向 (OOP for Django) (25 分鐘)

Django 的 Models 與 Views 高度依賴類別繼承。

### 8.5.1 基本語法與 `self`
Python 的 `self` 相當於 JS 的 `this`，但它必須顯式寫在方法的第一個參數。

```python
class Post:
    def __init__(self, title, content):
        self.title = title       # 實例屬性
        self.content = content

    def __str__(self):           # Dunder Method: 控制 print(obj) 的結果
        return f"文章標題: {self.title}"

p = Post("Django 入門", "Python 很棒")
print(p)  # 觸發 __str__
```

### 8.5.2 繼承 (Inheritance)
這是 Django 開發最常用的部分：

```python
class BaseModel:
    def save(self):
        print("儲存到資料庫")

class User(BaseModel):  # 繼承 BaseModel
    def save(self):
        print("驗證資料中...")
        super().save()  # 呼叫父類別方法
```

---

2️⃣ 關於 Python 的 `self` 關鍵字，下列敘述何者 **正確**？
- (A) `self` 是關鍵字，在方法中可以省略。
- (B) `self` 必須是類別方法的第一個參數，用來代表實例對象。
- (C) `self` 的名稱是固定的，不能改成其他名稱。
- (D) `self` 相當於 JavaScript 的 `static`。

<details>
<summary>解答</summary>
(B)。
說明：雖然慣例上使用 `self`（且強烈建議遵循），但技術上它只是方法的第一個參數；它代表的是被呼叫的實例本身。
</details>


## 8.6 實作練習：Python 實戰演練 (2 小時)

### Lab 1: 資料轉換器 (30 分鐘)
**情境**：你從資料庫取得了一份使用者清單（List of Dictionaries），請撰寫一個函式 `get_adult_emails`，過濾出年齡大於等於 18 歲的使用者，並回傳他們的 Email 列表。

```python
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 16, "email": "bob@example.com"},
    {"name": "Charlie", "age": 30, "email": "charlie@example.com"},
]

def get_adult_emails(user_list):
    # 在此實作邏輯
    pass

# 預期輸出: ["alice@example.com", "charlie@example.com"]
print(get_adult_emails(users))
```

### Lab 2: 列表推導式 (List Comprehension) (30 分鐘)
**練習**：將 Lab 1 的邏輯改用 Python 最著名的「列表推導式」一行完成。並嘗試將所有 Email 轉換為大寫。

```python
# 範例語法: [item.upper() for item in list if condition]
adult_emails_upper = [ ... ]
print(adult_emails_upper)
```

### Lab 3: 模擬 Django 權限系統 (60 分鐘)
**情境**：請實作一個裝飾器 `@require_admin`。
1. 定義一個 `current_user` 字典，包含 `username` 和 `is_admin` 欄位。
2. 如果 `is_admin` 為 `True`，則執行被裝飾的函式。
3. 如果為 `False`，則印出 "Permission Denied!"。

```python
current_user = {"username": "guest_user", "is_admin": False}

def require_admin(func):
    # 在此實作裝飾器
    pass

@require_admin
def delete_database():
    print("資料庫已刪除！")

# 測試呼叫
delete_database()
```

---

3️⃣ 在 Python 的列表推導式 `[x**2 for x in range(5) if x % 2 == 0]` 中，最後生成的列表為何？
- (A) `[0, 1, 4, 9, 16]`
- (B) `[0, 4, 16]`
- (C) `[1, 9]`
- (D) `[0, 2, 4]`

<details>
<summary>解答</summary>
(B)。
說明：`range(5)` 產生 `0, 1, 2, 3, 4`。`if x % 2 == 0` 過濾出偶數 `0, 2, 4`。最後執行 `x**2` (平方)，得到 `0, 4, 16`。
</details>

---
