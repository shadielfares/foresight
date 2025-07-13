# Running Using Doppler

Doppler allows us to mask private keys while still keeping the repo public and open to judgement and critism from peers and interested parties.

Commands to compile a file such as `foo.py` with its key stored in a folder in doppler named `neo4j` would like:
```
doppler run --project neo4j -- python3 foo.py    
```