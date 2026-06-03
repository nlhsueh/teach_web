# Ch10 HTMX 基礎非同步範例 (Basic Asynchronous Demo)

這個目錄包含了一個純 HTML 的極簡範例，展示了 HTMX 如何透過 `hx-get` 屬性發送非同步（AJAX）請求並局部替換頁面內容。

This directory contains a pure static HTML demo demonstrating how HTMX uses `hx-get` to perform asynchronous (AJAX) requests and swap content dynamically.

---

## ⚠️ 重要提醒 (Crucial Note: CORS Policy)

由於瀏覽器的**安全性政策 (CORS)**，直接雙擊打開 `index.html` (使用 `file://` 協定) 會導致 HTMX 無法正常讀取 `update.html`。您必須使用簡單的 HTTP 伺服器來載入此範例。

Due to browser **CORS Security Policies**, double-clicking `index.html` (using `file://` protocol) will block HTMX requests. You must host it using a local HTTP server.

---

## 🚀 如何執行 (How to Run)

### 方法一：使用 Python 內建伺服器 (Method 1: Python Built-in Server)
1. 開啟終端機 (Terminal) 並切換至本目錄：
   ```bash
   cd Topic03_backend/src/ch10_htmx_demo
   ```
2. 啟動 Python 內建 HTTP 伺服器：
   ```bash
   python -m http.server 8000
   ```
3. 在瀏覽器中開啟：[http://localhost:8000/](http://localhost:8000/)

### 方法二：使用 VS Code Live Server 擴充套件 (Method 2: VS Code Live Server)
1. 安裝 VS Code 的 **Live Server** 擴充套件。
2. 在 `index.html` 上按滑鼠右鍵，選擇 **"Open with Live Server"**。

---

## 📂 檔案說明 (Files Description)
* [index.html](file:///Users/nickhsueh/Library/Mobile%20Documents/com~apple~CloudDocs/TEACH/teach_web/Topic03_backend/src/ch10_htmx_demo/index.html): 主頁面，載入 HTMX CDN，並使用 `hx-get="update.html"`。
* [update.html](file:///Users/nickhsueh/Library/Mobile%20Documents/com~apple~CloudDocs/TEACH/teach_web/Topic03_backend/src/ch10_htmx_demo/update.html): 被非同步載入的 HTML 局部片段（Fragment）。
