# Repo slash commands

Shared via git — pull the branch and they appear in Claude Code automatically.

| Command | Use |
|---|---|
| `/skim-status` | Read-only: what is running, progress, proxy. Start here. |
| `/produce <vNN> <groups> [--channels X]` | Launch a campaign with all pre-flight gates. |
| `/validate-skim <vNN>` | Three-layer validation, then update the ledger. |

Each command encodes the traps in `skimmer/CLAUDE.md` §7 as mandatory steps,
so a fresh session does not rediscover them. Edit the markdown to change
behaviour; there is no code to rebuild.
