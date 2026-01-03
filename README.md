# 👮‍♀️ OSS License Police

[![License Compliance Check](https://github.com/Sushisverige/oss-license-police/actions/workflows/license-check.yml/badge.svg)](https://github.com/Sushisverige/oss-license-police/actions/workflows/license-check.yml)

**"GPL Contamination Prevention System" for Supply Chain Security.**

開発プロジェクトの依存ライブラリ（`requirements.txt`）をスキャンし、企業のコンプライアンスポリシー（OSSライセンス）に違反するパッケージを自動検知・排除するCIツールです。

## 🚀 Key Features

* **Automated Scanning**: GitHub Actions上で、Pull Requestごとに自動実行。
* **Legal Risk Management**: コピーレフト（GPL/AGPL）などの「感染するライセンス」を未然にブロック。
* **PyPI Integration**: 公式PyPI APIと連携し、最新のライセンス情報を取得。

## 🛠 Tech Stack

* **Language**: Python 3.10
* **CI/CD**: GitHub Actions
* **Data Source**: PyPI JSON API

## 📦 Policy (Default)

| Type | Status | Licenses |
| :--- | :--- | :--- |
| **Allowed** | ✅ OK | MIT, Apache 2.0, BSD, ISC |
| **Forbidden** | 🚫 Block | GPL, AGPL, General Public License |

## 👨‍💻 Author

Developed by **Sushisverige** as a portfolio project for DevSecOps & Governance.
