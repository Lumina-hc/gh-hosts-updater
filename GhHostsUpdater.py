import ctypes
import os
import re
import subprocess
import sys
import time
import urllib.request

HOSTS_PATH = os.path.join(os.environ["SystemRoot"], "System32", "drivers", "etc", "hosts")
URL = "https://raw.hellogithub.com/hosts"
LOG_DIR = os.path.join(os.environ["LOCALAPPDATA"], "GitHubHosts")
LOG_FILE = os.path.join(LOG_DIR, "update.log")


def setup_console():
    os.system("chcp 65001 >nul")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def is_admin():
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        return False


def elevate():
    if is_admin():
        return True
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, '"%s"' % sys.argv[0], None, 1
        )
        return False
    except Exception as e:
        print("提权失败:%s" % e)
        return False


def log(msg):
    os.makedirs(LOG_DIR, exist_ok=True)
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 1024 * 1024:
        try:
            os.replace(LOG_FILE, LOG_FILE + ".old")
        except Exception:
            pass
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("%s  %s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), msg))


def fetch():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1")


def merge(content):
    if "GitHub520 Host Start" not in content or "GitHub520 Host End" not in content:
        raise RuntimeError("下载内容缺少 GitHub520 标记,已跳过")
    with open(HOSTS_PATH, "r", encoding="utf-8", errors="ignore") as f:
        cur = f.read()
    stripped = re.sub(
        r"[\r\n]*# GitHub520 Host Start.*?# GitHub520 Host End[\r\n]*",
        "\r\n",
        cur,
        flags=re.S,
    )
    new = stripped.rstrip() + "\r\n\r\n" + content.rstrip() + "\r\n"
    ok = False
    for _ in range(10):
        try:
            with open(HOSTS_PATH, "w", encoding="utf-8") as f:
                f.write(new)
            ok = True
            break
        except PermissionError:
            time.sleep(0.5)
    if not ok:
        raise RuntimeError("无法写入 hosts 文件(被占用)")
    subprocess.run(["ipconfig", "/flushdns"], capture_output=True)


def main():
    try:
        merge(fetch())
        log("OK: hosts updated")
        print("完成! 已合并最新规则并刷新 DNS")
    except Exception as e:
        log("ERROR: %s" % e)
        print("出错:%s" % e)


if __name__ == "__main__":
    setup_console()
    if not elevate():
        sys.exit(0)
    main()
    try:
        input("按回车退出...")
    except EOFError:
        pass