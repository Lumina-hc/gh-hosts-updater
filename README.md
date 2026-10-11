# gh-hosts-updater

One-click Windows hosts updater for faster GitHub access.

Fetches the latest [GitHub520](https://github.com/521xueweihan/GitHub520) hosts,
merges it into the system hosts file (Windows), and flushes the DNS cache.
Double-click to run; it elevates itself automatically.

## Features

- Downloads the newest GitHub hosts from `https://raw.hellogithub.com/hosts`
- Validates the payload before applying
- Replaces only the previous GitHub520 block, keeping your custom entries
- Auto-elevates via UAC when needed
- Flushes the DNS cache after writing
- Logs results to `%LOCALAPPDATA%\GitHubHosts\update.log`

## Usage

```powershell
python GhHostsUpdater.py
```

Or just double-click the file. If you are not an administrator, a UAC prompt
will appear; the script keeps running elevated.

## Requirements

- Windows
- Python 3.x (no third-party dependencies)

## Note

GitHub access from some networks is unstable, and hosts entries only help when
the mapped IP is reachable. For a reliable connection, use a proxy or mirror.

## License

[MIT](LICENSE)