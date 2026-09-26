"""Additional 1:1 body proofs and machine-readable delivery inventory."""
from pathlib import Path
import importlib.util, sys, json, hashlib
from PIL import Image, ImageDraw
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("proofs",HERE/"build_object_proofs.py")
p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
out=Image.new("RGBA",(1080,560),"#100b20"); d=ImageDraw.Draw(out)
d.text((20,15),"C04 | EXACT BODY stress 45px / 32px | separate from 45px runtime FILE box",font=p.font(18),fill="white")
for col,k in enumerate(["CURRENT","A","B","C"]):
 x=20+col*265
 src=p.C04/("references/current-chain-block-128w.png" if k=="CURRENT" else f"normalized/{k}/C04-{k}-128.png")
 im=Image.open(src).convert("RGBA")
 d.text((x,60),k,font=p.font(20),fill="#ffd166")
 for row,n in enumerate([45,32]):
  y=95+row*190
  for j,color in enumerate(["#2a1c4d","#ffffff","#090612"]):
   tile=Image.new("RGBA",(80,145),color)
   p.centered(tile,p.body_sized(im,n),40,80)
   out.alpha_composite(tile,(x+j*80,y))
  d.text((x,y+150),f"{n}px body (stress, NOT runtime sizing)",font=p.font(11),fill="white")
d.text((20,510),"At runtime FILE box 45px -> body ~34px. These larger BODY proofs do not authorize a larger hitbox.",font=p.font(16),fill="white")
p.save(out.convert("RGB"),p.C04/"proofs/C04-EXACT-BODY-STRESS.png")
# File inventory for all images including copies, derivatives and proofs.
rows=[]
for folder in [p.C03,p.C04,p.COMMON]:
 for path in sorted(folder.rglob("*.png")):
  rows.append(p.metadata(path))
(p.COMMON/"IMAGE-INVENTORY.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
print("PNG inventory count:",len(rows))
for folder in [p.C03,p.C04]:
 for path in (folder/"normalized").rglob("*.png"):
  meta=p.metadata(path)
  assert meta["edge_alpha_max"]==0,path
  assert meta["alpha_extrema"]== (0,255),path
print("Normalized sprites: true alpha, transparent border, no edge clipping.")

