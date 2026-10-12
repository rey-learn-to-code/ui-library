# UI Library: setup guide

This guide takes you from a brand-new computer to a working UI Library, step by step. You don't need any programming experience. Just follow the steps in order.

**Where the library lives online:** https://github.com/rey-learn-to-code/ui-library (private: only you can see it)

---

## Contents

1. [How it works (1-minute overview)](#1-how-it-works-1-minute-overview)
2. [First-time setup on a new Mac](#2-first-time-setup-on-a-new-mac)
3. [Everyday use: get updates, save changes](#3-everyday-use-get-updates-save-changes)
4. [Fonts: download when you need them](#4-fonts-download-when-you-need-them)
5. [3D materials: download when you need them](#5-3d-materials-download-when-you-need-them)
6. [Using a Windows computer](#6-using-a-windows-computer)
7. [Troubleshooting](#7-troubleshooting)
8. [Cheat sheet](#8-cheat-sheet)

---

## 1. How it works (1-minute overview)

Think of GitHub as a **locker on the internet** for this library:

- **Clone** = copy the library from the locker onto a computer (done once per computer).
- **Pull** = get the newest version from the locker (do it whenever you start working).
- **Push** = put your changes back into the locker (do it when you add something new).

The library is split into three parts:

| Part | Size | Where it is |
|---|---|---|
| Components, effects, icons, themes, prompts, the lookup page, guides | about 1.1 GB | **On GitHub.** You get it when you clone |
| Font files | up to 2.7 GB | **Not on GitHub.** Download only the fonts you need (section 4) |
| 3D materials | up to 19 GB | **Not on GitHub.** Download single items from the website, or whole collections with a script (section 5) |

---

## 2. First-time setup on a new Mac

Do this **once on each computer**. It takes about 15–30 minutes, mostly waiting for the download.

### Step 1: Open Terminal

Terminal is a window where you type commands.

1. Press **Command (⌘) + Space** to open Spotlight search.
2. Type `Terminal` and press **Return**.
3. A window with a blinking cursor appears. You type (or paste) commands there and press **Return** to run them.

> Tip: to paste a command, copy it from this guide, click inside Terminal, and press **⌘ + V**.

### Step 2: Make sure Git and Python are installed

Git is the program that talks to GitHub. Python runs the library's small tools. Paste this and press Return:

```bash
git --version && python3 --version
```

- If you see two lines like `git version 2.x` and `Python 3.x`, you're ready. Go to Step 3.
- If a pop-up says **"The git command requires the command line developer tools"**, click **Install**, accept, and wait (5–15 minutes). Then run the command again.

### Step 3: Download (clone) the library

Because the library is **private**, GitHub needs to know it's you. Pick **one** of the two options.

#### Option A (easiest, no typing): GitHub Desktop

1. Go to https://desktop.github.com, download **GitHub Desktop**, open the downloaded file, and drag the app into **Applications**.
2. Open GitHub Desktop, click **Sign in to GitHub.com**, and sign in **as `rey-learn-to-code`** in the browser window that opens. Click **Authorize**.
3. In GitHub Desktop: menu **File → Clone Repository…**
4. On the **GitHub.com** tab, select **`rey-learn-to-code/ui-library`**.
5. In **Local Path**, click **Choose…** and pick your **Documents** folder. The path should end with `/Documents/ui-library`.
6. Click **Clone**. Wait until it finishes (about 1.1 GB).

#### Option B: Terminal with GitHub CLI

1. Install Homebrew, a tool that installs other tools (skip this if you already have it). Paste the line from https://brew.sh into Terminal, press Return, and follow the instructions it prints (it may ask for your Mac password; typing it shows nothing on screen, which is normal).
2. Install GitHub CLI:
   ```bash
   brew install gh
   ```
3. Log in. Choose **GitHub.com → HTTPS → Yes → Login with a web browser**, then copy the one-time code, press Return, paste the code in the browser, and sign in **as `rey-learn-to-code`**:
   ```bash
   gh auth login
   ```
4. Clone the library into your Documents folder:
   ```bash
   gh repo clone rey-learn-to-code/ui-library ~/Documents/ui-library
   ```

### Step 4: Run the installer

The installer tells Claude Code where the library is and gets the lookup page ready. In Terminal:

```bash
cd ~/Documents/ui-library
```

```bash
bash install.sh
```

You should see `Installed Claude skill -> .../.claude/skills/ui-library/SKILL.md` and `Done.`

> Want the 543 Vietnamese-capable fonts right away (about 1 GB)? Run `bash install.sh --fonts` instead.

> If you cloned somewhere other than `Documents`, `cd` into that folder instead. The installer works from any location.

### Step 5: Restart Claude Code

Quit and reopen Claude Code (or the Claude desktop app) so it loads the new **ui-library** skill. From now on, when you ask Claude to build a website, it checks this library first.

### Step 6: Open the lookup page (optional check)

In Finder, open `Documents → ui-library` and double-click **`OPEN_TOOL.command`**. The lookup page opens in your browser.

- First time only: if macOS says it **can't be opened because it is from an unidentified developer**, right-click the file → **Open** → **Open**.
- Keep the Terminal window that appears open while you use the page. Close it when you're done.

✅ Setup is complete.

---

## 3. Everyday use: get updates, save changes

### Before you start working: get the newest version (pull)

You may have added things on another computer. Get them first:

- **GitHub Desktop:** open it, click **Fetch origin**, then **Pull origin** if it appears.
- **Terminal:**
  ```bash
  cd ~/Documents/ui-library && bash update.sh
  ```

### After you add something: save it to GitHub (push)

- **Easiest:** ask Claude: *"Save the UI library changes to GitHub."*
- **Terminal** (the text in quotes is a short note about what changed):
  ```bash
  cd ~/Documents/ui-library && bash save.sh "Added new icons"
  ```
- **GitHub Desktop:** type a short summary at the bottom left, click **Commit to main**, then **Push origin**.

> `save.sh` never uploads font files or 3D materials. They stay on the computer (they're too big for GitHub).

---

## 4. Fonts: download when you need them

The **list** of all 2,031 Google Fonts (with which ones support Vietnamese) is in the library. The **font files** are downloaded only when needed, into `assets/font/google-fonts/repo/`.

Run these from inside the library folder (`cd ~/Documents/ui-library` first):

| What you want | Command | Size / time |
|---|---|---|
| One or a few fonts | `python3 -I scripts/download_fonts.py "Be Vietnam Pro" "Inter"` | a few MB, seconds |
| All 543 Vietnamese-capable fonts | `python3 -I scripts/download_fonts.py --vietnamese` | about 1 GB, 5–15 min |
| Every font | `python3 -I scripts/download_fonts.py --all` | about 2.7 GB, 15–40 min |

- Font names must match the names shown in the lookup page's **Fonts** tab (use quotes when a name has spaces).
- You can safely run a command again: fonts already downloaded are skipped.
- Or simply ask Claude: *"Download the font Be Vietnam Pro into the UI library."*

---

## 5. 3D materials: download when you need them

3D materials are textures (wood, stone, metal…), 360° sky images (HDRIs) and 3D models. They're all **free (CC0)**, so you can use them in any project without credit. They live in `assets/3d-materials/`. Only the item lists (`index.json`) and a README are on GitHub.

### Option 1: one item, from the website (recommended)

| Source | What it has | Website |
|---|---|---|
| Poly Haven | HDRIs, textures, models | https://polyhaven.com |
| ambientCG | about 2,000 textures, HDRIs | https://ambientcg.com |
| Kenney | simple game-style 3D/2D packs | https://kenney.nl/assets |

1. Open the website and search for what you want (e.g. "oak floor").
2. On the item's page, choose a **1K** size (enough for websites) and the **JPG** format, then click **Download**.
3. Unzip it if needed and copy the files into your website project (for example `public/textures/`).
4. For textures, use the **NormalGL** normal map (not NormalDX); that's the one websites (three.js) use.

### Option 2: a whole collection, with a script

From inside the library folder:

| Collection | Command | Full size |
|---|---|---|
| Poly Haven | `python3 -I scripts/download_polyhaven.py` | about 8.5 GB |
| ambientCG | `python3 -I scripts/download_ambientcg.py` | about 10 GB |
| Kenney | `python3 -I scripts/download_kenney.py` | about 1 GB |

- Try a small sample first by adding `--limit 20` (downloads only 20 items).
- Poly Haven can do one type only: `--types hdris`, `--types textures` or `--types models`.
- The scripts can be stopped (close Terminal) and started again; finished items are skipped.
- After downloading, run `python3 scripts/build_tool.py` so the lookup page's **3D** tab shows them.

More details: [assets/3d-materials/README.md](assets/3d-materials/README.md).

---

## 6. Using a Windows computer

Everything works on Windows too, with small differences:

1. Install **Git for Windows** (https://git-scm.com/download/win; accept the defaults) and **Python 3** (https://www.python.org/downloads/; tick **"Add python.exe to PATH"** during setup).
2. Clone with **GitHub Desktop** (Option A in Step 3), into `Documents\ui-library`.
3. Open **Git Bash** (installed with Git), then run:
   ```bash
   cd ~/Documents/ui-library && bash install.sh
   ```
4. `OPEN_TOOL.command` is Mac-only. To open the lookup page on Windows, run this in Git Bash and then open http://localhost:8765/tool/ in your browser:
   ```bash
   cd ~/Documents/ui-library && python scripts/build_tool.py && python -m http.server 8765
   ```
5. On Windows, type `python` instead of `python3` in the font and 3D commands.

---

## 7. Troubleshooting

| Problem | What to do |
|---|---|
| `Repository not found` when cloning | You're signed in with the wrong GitHub account. Sign in as **rey-learn-to-code** (GitHub Desktop: **Settings → Accounts**; Terminal: `gh auth login`) |
| `Permission denied` or a password prompt when pushing | Same as above. GitHub no longer accepts your normal password in Terminal; use GitHub Desktop or `gh auth login` |
| `python3: command not found` | Run `xcode-select --install`, wait for it to finish, try again |
| The lookup page says "address already in use" | It's already open in another Terminal window. Use that one, or close it and try again |
| A font shows in the lookup page but doesn't preview | Its file isn't downloaded yet. Run `python3 -I scripts/download_fonts.py "Font Name"` |
| The 3D tab is empty | Normal on a new computer. Download what you need (section 5), then run `python3 scripts/build_tool.py` |
| `update.sh` says "Not possible to fast-forward" | You changed files on two computers without saving in between. Ask Claude: *"Fix the git conflict in my UI library."* |
| Claude doesn't seem to know the library | Run `bash install.sh` again, then restart Claude Code |

---

## 8. Cheat sheet

```text
First time on a computer:
  1. Clone   rey-learn-to-code/ui-library  ->  ~/Documents/ui-library   (GitHub Desktop)
  2. cd ~/Documents/ui-library && bash install.sh
  3. Restart Claude Code

Every time:
  Start of work :  bash update.sh
  End of work   :  bash save.sh "what changed"

On demand:
  Fonts  :  python3 -I scripts/download_fonts.py "Font Name"     (--vietnamese | --all)
  3D     :  website (polyhaven.com / ambientcg.com / kenney.nl)   or   scripts/download_*.py --limit 20
  Lookup :  double-click OPEN_TOOL.command  ->  http://localhost:8765/tool/
```
