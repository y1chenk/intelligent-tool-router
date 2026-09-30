# Changelog

## Unreleased — 文件更新 / Documentation

- 將雙語首頁改為面向新使用者的介紹，加入問題導向開場、功能情境與實際評測邀請；開發者步驟改為折疊顯示。
  Rework both homepages with a stronger opening, practical use cases, and an evaluation invitation; collapse developer instructions.
- 重新設計 GitHub 首頁，加入雙語導覽、徽章、流程圖與可複製範例。
  Redesign the GitHub homepage with language navigation, badges, a workflow diagram, and copyable examples.
- 新增 `README_EN.md` 英文文件，並將其納入安裝 ZIP。
  Add English documentation in `README_EN.md` and include it in installation ZIPs.

## 0.2.1 — 私人發布（2026-09-30）

- 統一四個 Skill 的繁體中文介面，為研究、開發、驗證與核心路由各自客製啟動提示。
- 補上八個中英文關鍵字。
- 新增套件 README 與 CHANGELOG；公開授權尚未指定，因此未加入 LICENSE。
- 新增 `scripts/build_package.py`：以根 manifest 為共同 metadata 唯一來源，提供 `--check` 差異檢查及 `--output` 相容 manifest 同步與可重現 ZIP 建構。
- 明訂 ledger 的 `0.2.x` 核心相容政策，新增可選的命名空間 `extensions` 與 `ledger-versioning.md`；核心欄位變更需升 minor version。
- 將 manifest、README 與四個 Skill 的套件版本標示同步為 0.2.1。Ledger 資料格式版本獨立於套件版本，範例仍使用 `schema_version: "0.2.0"`。

## 0.2.0 — 草稿

- 將核心路由、開發、研究、驗證的責任與跨檔案引用整理一致。
- 開發流程加入只還原本次變更的回復規則，保留使用者同時進行的修改。
- 研究流程加入結構化 ledger、分支關閉及探索未嘗試路徑的回溯規則。
- 驗證清單允許 N/A，依實際證據區分完成狀態及合理的後續操作。
- 加入 12 個正反例，將能力對照與環境差異移至按需載入的參考資料。

## 0.1.0

- 提供工具路由、開發、深度研究、驗證與停止四個 Skill 的初始私人版本。
