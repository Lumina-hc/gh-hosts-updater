# gh-hosts-updater

One-click Windows hosts updater for faster GitHub access.

[English](#english) | [中文](#chinese)

---

<h2 id="english">English</h2>

Fetches the latest [GitHub520](https://github.com/521xueweihan/GitHub520) hosts,
merges it into the system hosts file (Windows), and flushes the DNS cache.
Double-click to run; it elevates itself automatically.

### Features

- Downloads the newest GitHub hosts from `https://raw.hellogithub.com/hosts`
- Validates the payload before applying
- Replaces only the previous GitHub520 block, keeping your custom entries
- Auto-elevates via UAC when needed
- Flushes the DNS cache after writing
- Logs results to `%LOCALAPPDATA%\GitHubHosts\update.log`

### Usage

```powershell
python GhHostsUpdater.py
```

Or just double-click the file. If you are not an administrator, a UAC prompt
will appear; the script keeps running elevated.

Linux users can use [GhHostsUpdater-linux.py](GhHostsUpdater-linux.py)
(`sudo python3 GhHostsUpdater-linux.py`).

### Requirements

- Windows or Linux
- Python 3.x (no third-party dependencies)

### Note

GitHub access from some networks is unstable, and hosts entries only help when
the mapped IP is reachable. For a reliable connection, use a proxy or mirror.

---

<h2 id="chinese">中文</h2>

自动拉取最新 [GitHub520](https://github.com/521xueweihan/GitHub520) hosts 规则，
合并进系统 hosts 文件（Windows）并刷新 DNS 缓存。双击即可运行，自动提权。

### 特性

- 从 `https://raw.hellogithub.com/hosts` 获取最新 GitHub hosts
- 写入前校验内容合法性
- 只替换上一次的 GitHub520 区块，保留你的自定义条目
- 需要权限时自动触发 UAC 提权
- 写入后自动刷新 DNS 缓存
- 运行日志记录到 `%LOCALAPPDATA%\GitHubHosts\update.log`

### 使用

```powershell
python GhHostsUpdater.py
```

或直接双击运行文件。当前不是管理员时会出现 UAC 提示，提权后继续执行。

Linux 用户可使用 [GhHostsUpdater-linux.py](GhHostsUpdater-linux.py)
(`sudo python3 GhHostsUpdater-linux.py`)。

### 环境要求

- Windows 或 Linux
- Python 3.x（无第三方依赖）

### 说明

部分网络环境下访问 GitHub 不稳定，hosts 仅在映射 IP 可达时有效。
如需稳定连接，请使用代理或镜像。

---

## License / 许可证

[Apache License 2.0](LICENSE), Copyright 2026 Lumina-hc.