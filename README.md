# Project Zepton

A modular, msfconsole-style security toolkit built for **Termux** on Android.
Pure Python standard library — no pip dependencies for the core framework.

> **Legal:** Zepton is for testing devices and networks you own or have
> explicit written permission to test. Unauthorized access is illegal.
> You are responsible for how you use this tool.

## Features

- Interactive `msfconsole`-style console: `use`, `set`, `run`, `search`, `show options`
- Dynamic module loader — drop a `.py` file in `modules/` and it's a module
- Android tooling (APK payload generation via msfvenom, ADB enumeration)
- Metasploit integration (auto-generated multi/handler resource scripts)
- Network recon (threaded port scanner, ping sweep)
- Ctrl-C safe prompt, partial module name matching, colored output

## Requirements

- [Termux](https://termux.dev/) (F-Droid build recommended)
- Python 3.8+ (`pkg install python`)
- Optional: `pkg install metasploit` (payloads/handlers), `pkg install android-tools` (ADB)

## Install

```bash
pkg install python git
git clone https://github.com/YOUR-USERNAME/zepton.git
cd zepton
python zepton.py
```

Or run the installer (offers Metasploit + android-tools):

```bash
bash install.sh
```

## Quick start

```text
zepton > show modules
zepton > use network/port_scanner
zepton (network/port_scanner) > set RHOST 192.168.1.1
zepton (network/port_scanner) > set PORTS 1-1024,8080
zepton (network/port_scanner) > run
```

`use` accepts partial names (`use port` works if the match is unique).

## Included modules

| Path | What it does |
|------|--------------|
| `android/apk_payload` | Builds an Android Meterpreter APK via msfvenom |
| `android/adb_enum` | Lists ADB devices + model/Android version |
| `metasploit/handler` | Generates an .rc script and launches multi/handler |
| `network/port_scanner` | Threaded TCP connect() scanner |
| `network/ping_sweep` | ICMP sweep of a CIDR subnet |

## Project layout

```text
zepton/
├── zepton.py            # entry point
├── install.sh           # Termux installer
├── core/                # console, module loader, banner, colors
├── modules/             # your modules live here (auto-loaded)
│   ├── android/
│   ├── metasploit/
│   └── network/
├── templates/           # copy module_template.py to write your own
├── docs/USAGE.md        # full command reference + module authoring
└── data/                # scratch space for wordlists, captures, etc.
```

## Writing your own modules

Copy `templates/module_template.py` into `modules/<category>/`, fill in the
metadata, options, and `run()` — it shows up in `show modules` on next launch.
See `docs/USAGE.md` for the full walkthrough.

## Roadmap

- [ ] Session management (background jobs, `sessions -i`)
- [ ] Global options (`setg`)
- [ ] Payload encoder/obfuscation helpers
- [ ] Wi-Fi recon modules (termux-wifi-scaninfo)
- [ ] Tab completion for module paths and option names

## License

MIT — see [LICENSE](LICENSE).
