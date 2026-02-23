# 第 2 章：HTTP 協定 (HyperText Transfer Protocol)

HTTP 是網際網路的基石，它定義了客戶端（例如你的瀏覽器）與伺服器之間交換資料的規則。理解 HTTP 是開發 Web 應用程式、API 以及進行網路排錯的最核心職責。

---

## 2.1 HTTP 基本概念

HTTP 是一種基於文本的協議。作為資工系學生，我們通常將它視為客戶端和伺服器之間通訊的主要協議。

### 1. HTTP 方法 (HTTP Methods)
HTTP 協議定義了多種方法來與伺服器進行交互，最常見的有：
- **GET**: 用於請求資源，通常用來讀取資料。
- **POST**: 用於提交資料，通常用來創建或修改伺服器上的資料。
- **PUT**: 用於更新資料。
- **DELETE**: 用於刪除資料。
- **HEAD**: 像 GET 方法，但不返回消息體，僅返回標頭。
- **PATCH**: 用於對資料進行部分修改。

> [!TIP]
> **💡 重點觀念**：HTTP 是一種「請求-回應 (Request-Response)」模式。除非客戶端發起請求，否則伺服器通常不會主動傳送資料給客戶端。

> [!WARNING]
> **⚠️ 小提示**：GET 請求的參數會顯示在網址 (URL) 中，因此不適合用來傳輸密碼等敏感資訊。雖然 POST 相對安全，但若不配合 HTTPS，資料仍可能被截獲。

### 2. URL (Uniform Resource Locator)
這是用來指定要訪問資源的地址。URL 通常包括協議（如 HTTP 或 HTTPS）、主機名稱、路徑、查詢參數等。

---

## 2.2 HTTP 請求與回應結構

### 1. HTTP 請求 (Request)
當客戶端向伺服器發送請求時，它會包含以下內容：
- **方法**: 如 GET、POST 等。
- **URL**: 用於指向資源的地址。
- **HTTP 標頭**: 附加的元數據，如 User-Agent, Accept, Cookie 等。
- **請求正文 (Body)**: 只有在使用 POST、PUT 等方法時才會有，通常是用戶輸入的資料或 JSON。

### 2. HTTP 回應 (Response)
伺服器會返回回應，通常包括：
- **狀態碼**: 用來表示請求的處理結果。
- **HTTP 標頭**: 提供有關回應的元數據，例如 Content-Type, Content-Length 等。
- **回應正文**: 包含實際數據，如 HTML、JSON 或圖片。

---

## 2.3 HTTP 狀態碼 (Status Codes)

你可以透過首位數字快速判斷請求的結果：
- **1xx (Informational)**: 正在處理中。
- **2xx (Success)**: 請求成功。 (例如：200 OK)
- **3xx (Redirection)**: 搬家了，請去別的地方。 (例如：301 Moved Permanently)
- **4xx (Client Error)**: 你的錯！(例如：404 Not Found, 400 Bad Request)
- **5xx (Server Error)**: 我的錯 (伺服器噴錯)。(例如：500 Internal Error)

> [!IMPORTANT]
> **⚠️ 常見面試題**：404 (Not Found) 與 500 (Internal Server Error) 的區別？404 通常是網址打錯；500 則是伺服器程式碼執行時發生錯誤 (Crash)。

---

## 2.4 HTTPS 與傳輸安全

- **HTTP**: 不加密，數據以純文本傳輸。
- **HTTPS**: 使用 **TLS/SSL** 加密，保護隱私與完整性。

> [!NOTE]
> **💡 重點觀念**：HTTPS 透過「數位憑證 (Certificate)」確認網站身分，這需要「憑證頒發機構 (CA)」簽發。

---

## 2.5 現代化與效能：HTTP/1.1 vs. HTTP/2

- **HTTP/1.1**: 請求是順序處理的，一次只能發一個，容易導致延遲（線頭阻塞）。
- **HTTP/2**: 引入了**多路複用 (Multiplexing)**，允許在單一連接並行傳輸多個請求，顯著提高效能。

---

## 2.6 HTTP 請求的完整生命週期

當你在瀏覽器輸入網址後，會經歷以下階段：
1. **DNS 查詢**: 將域名轉換為 IP 地址。
2. **TCP 連接**: 三次握手 (SYN -> SYN-ACK -> ACK)。
3. **TLS 握手** (如果是 HTTPS): 密鑰交換。
4. **傳送請求**: 客戶端發送 HTTP Data。
5. **伺服器處理**: 程式碼運算與資料庫查詢。
6. **傳送回應**: 伺服器回傳資料。
7. **瀏覽器渲染**: 解析 HTML, CSS, JS 並顯示頁面。

---

## ✍️ 自我測驗 (Self-Test)

<details>
<summary>▶️ 點擊查看測驗問題與解答</summary>

**Q1: 下列哪個 HTTP 狀態碼表示「資源未找到」？**
- C) 404

**Q2: GET 方法與 POST 方法的主要差異為何？**
- B) GET 參數放在 URL，POST 參數放在 Body

**Q3: HTTP/2 相較於 HTTP/1.1 之所以更快，主要原因為何？**
- B) 多路複用 (Multiplexing) 技術

</details>

---

## 🛠️ 實作演練 (Practical Exercises)

1. **DevTools 觀察員**: 打開 Chrome Network Tab，觀察 [google.com](https://google.com) 的請求 Headers。
2. **終端機大師**: 嘗試執行 `curl -I https://www.google.com` 看看標頭長什麼樣子。
3. **API 實戰**: 到 [httpbin.org](https://httpbin.org) 練習模擬發送 GET/POST 請求。
