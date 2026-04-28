# Ch09 資料庫概論 (Database Introduction)

在 Web 開發中，資料庫 (Database) 是用來長期儲存、管理與檢索資料的核心組件。當你的軟體重新啟動，資料還能存在，就是因為有資料庫。

---

## 1. 為什麼需要資料庫？
-   **持久性 (Persistence)**：資料不會因程式結束或斷電而消失。
-   **效率 (Efficiency)**：能夠快速搜尋與過濾數百萬筆資料。
-   **共享性 (Sharing)**：多個使用者或應用程式可以同時存取同一組資料。
-   **完整性 (Integrity)**：透過約束 (Constraints) 確保資料的正確性。

---

## 2. 關係型 vs. 非關係型 (SQL vs. NoSQL)

### 關係型資料庫 (Relational, SQL)
-   **特點**：使用表格 (Table) 儲存，強調資料間的關聯。
-   **標準**：使用 SQL (Structured Query Language) 進行操作。
-   **代表**：MySQL, PostgreSQL, SQLite (Django 預設), SQL Server.
-   **優點**：強大的一致性 (ACID)、複雜查詢能力。

### 非關係型資料庫 (Non-Relational, NoSQL)
-   **特點**：使用文件 (Document)、鍵值 (Key-Value) 或圖形儲存。
-   **代表**：MongoDB, Redis (常用於快取), Cassandra.
-   **優點**：架構靈活 (Schema-less)、水平擴展性佳。

---

## 3. 關聯式資料庫的核心觀念：資料表、約束與關聯

為了銜接後續的 Django 開發，我們必須先理解關聯式資料庫如何描述現實世界的資料。我們以一個**學校系統**為例：

### 3.1 表格 (Table) 與欄位 (Column)
資料庫將資料儲存為「表格」，就像是 Excel 的試算表。每個表格有特定的「欄位」來定義資料的屬性。

### 3.2 約束 (Constraints)
為了確保資料的正確性與唯一性，我們會對欄位設定「約束」：
-   **Primary Key (主鍵)**：能**唯一識別**資料表中每一筆紀錄的欄位（例如：系統自動生成的 ID 編號）。一個資料表只能有一個主鍵。
-   **Unique (唯一約束)**：確保該欄位的值在整張表中不會重複（例如：學號或電子郵件）。
-   **Null (空值約束)**：決定該欄位是否允許為空 (`NULL`)。如果不允許為空 (`NOT NULL`)，則在新增資料時一定要提供這個值（例如：學生的姓名不能是空白的）。

**👇 模擬資料表：Student (學生表)**

| id <br>`(Primary Key)` | student_id <br>`(Unique)` | name <br>`(Not Null)` | email <br>`(Unique)` |
| :--- | :--- | :--- | :--- |
| 1 | B11001 | 彭于晏 | eddie@school.edu |
| 2 | B11002 | 林志玲 | chiling@school.edu |
| 3 | B11003 | 周杰倫 | jay@school.edu |

### 3.3 資料表之間的關聯 (Relationships)
現實世界的資料彼此都是有關聯的，關聯式資料庫主要透過**外鍵 (Foreign Key)** 來建立關聯。

#### 1. 一對多 / 多對一 (One-to-Many / Many-to-One, 1:N)
這是資料庫中最常見的關聯。我們通常在「多」的那一方加入「一」的主鍵作為**外鍵**。
-   **例子**：`系所 (Department)` 與 `學生 (Student)`。一個系所有多名學生，一名學生只屬於一個系所。

**Department (系所表)**
| id `(PK)` | name |
| :--- | :--- |
| 1 | 資訊工程學系 |
| 2 | 企業管理學系 |

**Student (學生表)**
| id `(PK)` | name | department_id `(Foreign Key)` |
| :--- | :--- | :--- |
| 1 | 彭于晏 | 1 *(對應資工系)* |
| 2 | 林志玲 | 2 *(對應企管系)* |
| 3 | 周杰倫 | 1 *(對應資工系)* |

#### 2. 一對一 (One-to-One, 1:1)
它其實是一種「特殊的一對多」，只是限制了外鍵不能重複。通常用來將欄位過多的資料表拆分為二，以提升效能或方便管理。
-   **例子**：`學生 (Student)` 與 `學生檔案 (StudentProfile)`。一名學生只有一個詳細的學生檔案。

**StudentProfile (學生詳細檔案表)**
| id `(PK)` | address | phone | student_id `(FK, Unique)` |
| :--- | :--- | :--- | :--- |
| 1 | 台北市信義區... | 0912-345-678 | 1 *(對應彭于晏)* |
| 2 | 台南市東區... | 0987-654-321 | 2 *(對應林志玲)* |

#### 3. 多對多 (Many-to-Many, M:N)
在關聯式資料庫底層，多對多關係通常需要透過建立一張額外的**「中介表 (Junction Table)」**來實現。
-   **例子**：`學生 (Student)` 與 `課程 (Course)`。一名學生可以修多門課，一門課可以被多名學生修讀。

**Course (課程表)**
| id `(PK)` | title | credits |
| :--- | :--- | :--- |
| 101 | Python 程式設計 | 3 |
| 102 | 資料庫系統 | 3 |

**Enrollment (選課紀錄中介表)**
| id `(PK)` | student_id `(FK)` | course_id `(FK)` | semester |
| :--- | :--- | :--- | :--- |
| 1 | 1 *(彭于晏)* | 101 *(Python)* | 112-1 |
| 2 | 1 *(彭于晏)* | 102 *(資料庫)* | 112-1 |
| 3 | 2 *(林志玲)* | 101 *(Python)* | 112-1 |

---

## 4. 基本 SQL 操作 (CRUD)
開發者最常做的四件事：
-   **C (Create)**: `INSERT INTO users (name) VALUES ('Nick');`
-   **R (Read)**: `SELECT * FROM users WHERE id = 1;`
-   **U (Update)**: `UPDATE users SET name = 'Nick H.' WHERE id = 1;`
-   **D (Delete)**: `DELETE FROM users WHERE id = 1;`

---

## 5. 進深觀念：ACID 特性
作為資工系學生，需理解資料庫如何保證交易的正確性：
-   **A (Atomicity) 原子性**：交易要嘛全部成功，要嘛全部失敗（不可切分）。
-   **C (Consistency) 一致性**：交易前後，資料庫都必須符合預定義的規則。
-   **I (Isolation) 隔離性**：多個交易同時執行時，彼此互不干擾。
-   **D (Durability) 持久性**：交易一旦完成，資料就是永久保存的。

---

## 6. ORM (Object-Relational Mapping)
在 Django 等現代框架中，我們很少直接寫 SQL，而是使用 **ORM**。
-   **定義**：將程式語言中的「物件」映射到資料庫中的「表格」。
-   **優點**：提高開發效率、防止 SQL 注入攻擊、易於維護。

> [!TIP]
> **💡 重點觀念**：學習資料庫不只是學 SQL 指令，更是學會如何「設計資料模型 (Data Modeling)」來反映現實世界的邏輯。
