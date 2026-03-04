# 此目錄之投影片，由 Gemini AI 依據各章節內容，使用 Marp 語法生成。

```mermaid
graph LR
    Source[chXX_web.md] -- "Gemini AI" --> Marp[chXX_slide.md<br/>(Marp 語法)]
    Marp -- "Marp Tool<br/>(marp-cli)" --> PDF[chXX_slide.pdf]
```

- **chXX_web.md**：各章節的原始教材內容。
- **chXX_slide.md**：透過 AI 產生的投影片原始檔，符合 Marp 格式。
- **chXX_slide.pdf**：透過 Marp 工具轉出的最終投影片檔案。