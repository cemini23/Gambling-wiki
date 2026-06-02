# Private prod-only poker modules (not committed)

Copy exploit implementation here for production deploy:

```bash
cp examples/opponent_hud_stub.py private/opponent_hud_exploit.py
# Then merge from deploy bundle or pull from secure store — full exploit
# module lives in `private/opponent_hud_exploit.py` on operator machine only.
```

`deploy/deploy_to_cemini_prod.sh` rsyncs this folder to cemini-prod when present.
Public `examples/opponent_hud.py` stays a neutral facade with no exploit constants.
