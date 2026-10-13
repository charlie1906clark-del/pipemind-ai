# Backups and verification — single-node research pilot

PipeMind's pilot SQLite database uses WAL. A `cp file.sqlite` while the
service is writing is **not** a consistent backup. The new offline maintenance
command invokes the SQLite online-backup API to copy a consistent database,
then checks `PRAGMA integrity_check`, the complete audit hash chain and a
SHA256 sidecar before declaring the backup verified.

```bash
python -m pipemind.maintenance.backup create data/pipemind.sqlite /restricted/backups/backup-2026-10-13.sqlite
python -m pipemind.maintenance.backup verify /restricted/backups/backup-2026-10-13.sqlite
```

Backups cannot overwrite existing files and inherit file mode 0600 on POSIX.
A hash manifest is separate and must be secured alongside the snapshot.
The tool does **not** upload data, schedule backups, restore any production file,
encrypt the snapshot, protect the encryption key or provide immutable offsite
anchoring. Those remain explicitly unimplemented deployment gates.

**Before a real customer pilot**: set encrypted offsite storage with restricted
accounts, retention & deletion controls, scheduled backup monitoring and a
documented restore drill tested on a separate staging database. A same-server
hash can be rewritten by someone with root access; independent external
anchoring is necessary for tamper-evidence against privileged attackers.
