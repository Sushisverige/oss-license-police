import requests
import sys

# 許可するライセンス（ホワイトリスト）
ALLOWED_LICENSES = ["MIT", "Apache Software License", "BSD", "ISC"]
# 禁止するライセンス（ブラックリスト - 感染するライセンス）
FORBIDDEN_LICENSES = ["GPL", "AGPL", "General Public License"]

def get_package_license(package_name):
    # PyPIのAPIを叩いて情報を取得
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # classifiersからライセンス情報を探す
            classifiers = data["info"].get("classifiers", [])
            for c in classifiers:
                if c.startswith("License ::"):
                    return c.split("::")[-1].strip()
            return data["info"].get("license", "Unknown")
    except:
        return "Error"
    return "Unknown"

def main():
    print("👮‍♀️ Scanning dependencies for license compliance...")
    
    # requirements.txt を読み込む
    try:
        with open("requirements.txt", "r") as f:
            packages = [line.split("==")[0].strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("requirements.txt not found.")
        return

    violations = []
    
    for pkg in packages:
        license_name = get_package_license(pkg)
        print(f"📦 {pkg}: {license_name}")
        
        # 判定ロジック
        is_allowed = any(allowed in license_name for allowed in ALLOWED_LICENSES)
        is_forbidden = any(forbidden in license_name for forbidden in FORBIDDEN_LICENSES)
        
        if is_forbidden:
            violations.append(f"❌ {pkg} uses FORBIDDEN license: {license_name}")
        elif not is_allowed:
            print(f"⚠️  {pkg} has unverified license: {license_name} (Manual check required)")

    if violations:
        print("\n🚫 COMPLIANCE CHECK FAILED!")
        for v in violations:
            print(v)
        sys.exit(1)  # GitHub Actionsを「失敗」させる
    else:
        print("\n✅ All dependencies are compliant.")
        sys.exit(0)  # 成功

if __name__ == "__main__":
    main()
