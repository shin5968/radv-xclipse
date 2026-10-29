#!/usr/bin/env python3
"""Candidate fix for Gamescope 3.16.1 CPU/SHM snapshot reuse.
Usage: python3 fix-shm-cache.py /path/to/gamescope
This is not a validated fix for phone display flicker.
"""
from pathlib import Path
import sys
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
p = root / 'src/steamcompmgr.cpp'
s = p.read_text()
marker = '// CPU buffers are snapshots, not live DMA-BUF imports.'
if marker in s:
    print('Already patched'); raise SystemExit(0)
old_lookup = 'if ( gamescope::OwningRc<CVulkanTexture> pTexture = s_BufferMemos.LookupVulkanTexture( buf ) )'
new_lookup = '''// CPU buffers are snapshots, not live DMA-BUF imports.
    struct wlr_dmabuf_attributes memoDmabuf = {};
    const bool canMemoize = wlr_buffer_get_dmabuf( buf, &memoDmabuf );
    if ( gamescope::OwningRc<CVulkanTexture> pTexture = canMemoize ? s_BufferMemos.LookupVulkanTexture( buf ) : nullptr )'''
old_memo = 's_BufferMemos.MemoizeBuffer( buf, std::move( pOwnedTexture ) );'
new_memo = 'if ( canMemoize )\n        s_BufferMemos.MemoizeBuffer( buf, std::move( pOwnedTexture ) );'
old_duplicate = 'if ( already_exists && !reslistentry.feedback'
new_duplicate = '''struct wlr_dmabuf_attributes duplicateDmabuf = {};
    if ( already_exists && wlr_buffer_get_dmabuf( buf, &duplicateDmabuf ) && !reslistentry.feedback'''
for old in (old_lookup, old_memo, old_duplicate):
    if s.count(old) != 1:
        raise SystemExit('Unexpected source; no changes made: ' + old)
backup = p.with_name(p.name + '.before-shm-cache-fix')
if backup.exists():
    raise SystemExit('Backup already exists; inspect before retrying')
s = s.replace(old_lookup, new_lookup).replace(old_memo, new_memo).replace(old_duplicate, new_duplicate)
backup.write_bytes(p.read_bytes())
p.write_text(s)
print('Patched; original:', backup)
