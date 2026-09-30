<div align="center">

# 🧭 Intelligent Tool Router

## 🔥 你的 AI 還在說謊嗎？

**它說「完成了」——你看過證據嗎？**<br>
*Your AI says “Done.” Where is the evidence?*

把 **Intelligent Tool Router** 加進你的 AI 工作流程，讓選工具、查來源和完成宣稱接受檢查。

[![Version: v0.2.1](https://img.shields.io/badge/version-v0.2.1-7c3aed?style=flat-square)](plugin.json)
[![Four skills](https://img.shields.io/badge/skills-4-0ea5e9?style=flat-square)](#skills)
[![Skills-only design](https://img.shields.io/badge/design-skills%20only-14b8a6?style=flat-square)](#about)
[![Bilingual documentation](https://img.shields.io/badge/docs-ZH%20%7C%20EN-f59e0b?style=flat-square)](README_EN.md)

**繁體中文** · [English](README_EN.md)

[快速開始](#quick-start) · [使用範例](#examples) · [取得與建構](#packaging) · [深入文件](#references)

</div>

---

<a name="about"></a>

AI 說已經安裝，結果只是產生 ZIP。說找到三個來源，結果三篇都轉載同一則消息。工具報錯之後，還是反覆嘗試同一條路。

**如果你也厭倦這些狀況，試試加入這套工具使用指引。**

Intelligent Tool Router 把選工具、深度研究、開發除錯與完成驗證整理成四個按需載入的 Skills，為模型提供明確的檢查與恢復流程。

> 💡 少一點「相信我」，多一點「這是證據」。

## ⚡ 你想改善哪一種 AI 壞習慣？

| 常見狀況 | 這套 Skills 要求模型怎麼處理 |
| --- | --- |
| 🗣️ 沒做完，卻先說「完成了」。 | 檢查實際狀態，區分已建立、已儲存、已部署與實際驗證。 |
| 🔁 工具失敗，還一直重複呼叫。 | 依錯誤類型修正、有限重試或換路徑；結果不明的寫入先查狀態。 |
| 🔎 搜了很多，卻沒有可信來源。 | 追查原始來源、版本與日期，去除重複轉載，交代證據缺口。 |
| 🛠️ 修一個 bug，順便弄壞你的其他修改。 | 先檢查現有程式，保留其他修改，安全可行時只還原本次失敗變更。 |

這些是工作流程的設計目標，實際效果可以用你的任務來測試。

核心指令使用英文，介面與啟動提示使用繁體中文。外掛本身不新增 MCP 伺服器或 API 金鑰；實際工具與帳號授權由使用環境提供。

<a name="skills"></a>

## 🧩 四個 Skills，一套工作流程

| Skill | 負責什麼 | 工作重點 |
| --- | --- | --- |
| 🧭 [智慧工具路由](skills/intelligent-tool-routing/SKILL.md) | 理解任務，選擇可用工具與專門流程。 | 利用已有證據；只為具體缺口增加呼叫。 |
| 🔎 [深度研究路由](skills/deep-research-routing/SKILL.md) | 追蹤來源、識別碼、日期與搜尋分支。 | 三次不同搜尋無新證據時關閉該分支，探索有價值的替代路徑。 |
| 🛠️ [開發工具路由](skills/development-routing/SKILL.md) | 檢查程式、版本與紀錄，診斷、修正、驗證。 | 保留其他修改；安全可行時，只還原本次失敗變更。 |
| ✅ [驗證與停止](skills/verification-and-stop/SKILL.md) | 核對完成宣稱，判斷是否仍有必要工作。 | 依實際證據區分已儲存、已部署與實際驗證。 |

```mermaid
flowchart TD
    R["🧭 工具路由"]
    S["🔎 深度研究"]
    D["🛠️ 開發與除錯"]
    V["✅ 驗證與繼續判斷"]
    R -->|研究任務| S
    R -->|開發任務| D
    R -->|操作完成檢查| V
    S --> V
    D --> V
    V -.->|仍有必要工作| R
```

按任務載入需要的 Skill；一般對話或簡單算術可以直接回答。

<a name="quick-start"></a>

## 🚀 快速開始

1. 依你的 AI 用戶端支援的流程，匯入此外掛或 `skills/` 下的四個完整 Skill 資料夾，保留其 `agents/` 與 `references/`。
2. 在支援外掛提及的聊天中，選擇 **@Intelligent Tool Router**；也可直接呼叫對應 Skill。
3. 交代目標、限制與完成標準，要求模型用證據回報結果。

在支援直接呼叫 Skills 的環境中，可複製以下範本：

```text
使用 $intelligent-tool-routing 處理以下任務：
目標：【你要完成的工作】
限制：【預算、範圍、時間或禁止更動的項目】
完成標準：【需要的成果、來源或驗證方法】
```

也可直接選擇 `$deep-research-routing`、`$development-routing` 或 `$verification-and-stop`，處理對應的工作。

<a name="examples"></a>

## 🎯 可直接使用的範例

<details>
<summary>🧭 選工具與執行任務</summary>

```text
使用 $intelligent-tool-routing 完成【任務】。
先確認可用能力與已有證據，再選擇適合的工具。
完成後提供成果，以及能核對完成狀態的證據。
```

</details>

<details>
<summary>🔎 深挖與來源查證</summary>

```text
使用 $deep-research-routing，deep dig【主題】。
優先官方與原始來源，追蹤識別碼、版本和日期。
附完整來源網址、證據等級，以及尚未覆蓋的範圍。
```

</details>

<details>
<summary>🛠️ 除錯與程式修復</summary>

```text
使用 $development-routing 查明【錯誤】的原因。
先讀相關程式、版本與執行紀錄，再依授權範圍修正。
保留我的其他修改，驗證原本的問題與受影響介面。
```

</details>

<details>
<summary>✅ 檢查是否真的完成</summary>

```text
使用 $verification-and-stop 檢查【結果】的完成宣稱。
依現有證據區分已建立、已儲存、已部署與實際驗證。
指出證據不足的部分，以及仍有必要執行的檢查。
```

</details>

更多情境與反例：[12 個路由案例](skills/intelligent-tool-routing/references/examples.md)。

<a name="packaging"></a>

## 📦 取得原始碼與建構

想研究、修改或協助改進專案？你可以使用 **Code → Download ZIP**，或用 Git 下載原始碼。

<details>
<summary>🧑‍💻 開發者指引：下載、檢查與封裝</summary>

以下步驟用於取得與檢查來源套件；日常使用已安裝的外掛，不需要反覆執行。

```sh
git clone https://github.com/y1chenk/intelligent-tool-router.git
cd intelligent-tool-router
python3 scripts/build_package.py --check
```

封裝腳本僅使用 Python 標準函式庫。Windows 若沒有 `python3`，可改用 `python` 或 `py -3`。使用 Download ZIP 時，請將解壓後的根目錄命名為 `intelligent-tool-router`。

產生可匯入的 ZIP：

```sh
python3 scripts/build_package.py --output ../intelligent-tool-router-0.2.1.zip
```

| 指令 | 處理內容 |
| --- | --- |
| `--check` | 唯讀檢查雙 manifest 一致性與基本套件條件。 |
| `--output` | 同步相容 manifest，將雙語 README、四個 Skills 與參考資料封裝到根目錄外的 ZIP。 |

共同 metadata 以根目錄的 `plugin.json` 為準，`.codex-plugin/plugin.json` 保存相容設定。依用戶端支援的外掛或 Skills 匯入流程安裝，並保留完整的 `agents/` 與 `references/` 資料。

</details>

<a name="references"></a>

## 📚 深入文件

| 文件 | 內容 |
| --- | --- |
| [路由案例](skills/intelligent-tool-routing/references/examples.md) | 12 個正反例與完成宣稱的界線。 |
| [能力對照](skills/intelligent-tool-routing/references/capability-routes.md) | 依需求選擇資料來源與工具能力。 |
| [使用環境參考](skills/intelligent-tool-routing/references/host-profile.md) | 不同產品與環境的條件式範例。 |
| [研究紀錄 Schema](skills/deep-research-routing/references/ledger.schema.json) | 來源、識別碼與搜尋分支的結構化格式。 |
| [研究紀錄版本政策](skills/deep-research-routing/references/ledger-versioning.md) | 核心相容性、擴充與版本遷移。 |
| [版本紀錄](CHANGELOG.md) | 已發布版本與後續修改。 |

## 💬 回饋與改進

可透過 [Issues](https://github.com/y1chenk/intelligent-tool-router/issues) 提供實際使用案例：任務目標、可用工具、預期結果、實際結果與可重現步驟。選工具錯誤、不必要的重複呼叫，以及缺少證據的完成宣稱，都是有用的改進線索。

## 🧪 帶著你的真實任務來挑戰它

找一個你熟悉的任務，分別在使用與未使用 Router 的新對話中執行。比較結果是否正確、來源能否查證、完成宣稱是否有依據，以及工具呼叫與耗時。把失敗案例帶回來，讓下一次改進有根據。

<details>
<summary>📝 版本、效果與授權說明</summary>

目前套件版本為 **v0.2.1**。Skills 提供模型行為指引，不是強制攔截器，也不保證消除錯誤或幻覺。自動觸發、遵循率與效能改善需要實際任務評測；封裝檢查不等同模型可靠性測試，也不代替完整 manifest 或 JSON Schema 驗證。公開開源授權尚未指定，會在正式公開前確定。

</details>

---

<div align="center">

🧭 **Intelligent Tool Router** · [English](README_EN.md) · [Changelog](CHANGELOG.md)

</div>
