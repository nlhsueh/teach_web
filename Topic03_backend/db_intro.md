# 資料庫概論 (Database Introduction)

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

## 3. 基本 SQL 操作 (CRUD)
開發者最常做的四件事：
-   **C (Create)**: `INSERT INTO users (name) VALUES ('Nick');`
-   **R (Read)**: `SELECT * FROM users WHERE id = 1;`
-   **U (Update)**: `UPDATE users SET name = 'Nick H.' WHERE id = 1;`
-   **D (Delete)**: `DELETE FROM users WHERE id = 1;`

---

## 4. 進深觀念：ACID 特性
作為資工系學生，需理解資料庫如何保證交易的正確性：
-   **A (Atomicity) 原子性**：交易要嘛全部成功，要嘛全部失敗（不可切分）。
-   **C (Consistency) 一致性**：交易前後，資料庫都必須符合預定義的規則。
-   **I (Isolation) 隔離性**：多個交易同時執行時，彼此互不干擾。
-   **D (Durability) 持久性**：交易一旦完成，資料就是永久保存的。

---

## 5. ORM (Object-Relational Mapping)
在 Django 等現代框架中，我們很少直接寫 SQL，而是使用 **ORM**。
-   **定義**：將程式語言中的「物件」映射到資料庫中的「表格」。
-   **優點**：提高開發效率、防止 SQL 注入攻擊、易於維護。

> [!TIP]
> **💡 重點觀念**：學習資料庫不只是學 SQL 指令，更是學會如何「設計資料模型 (Data Modeling)」來反映現實世界的邏輯。
