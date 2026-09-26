"""Offline normalization and proofs. No production imports, writes or concept painting."""
from pathlib import Path
import argparse, hashlib, json, math
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageStat, ImageChops

ROOT = Path(__file__).resolve().parents[2]
COMMON = ROOT / "C03-C04-Gameplay-Object-Review"
C04 = ROOT / "C04-Chain-Block"
C03 = ROOT / "C03-Player-Orb"
RESAMPLE = Image.Resampling.LANCZOS
FONT = "C:/Windows/Fonts/arial.ttf"
def font(n=16): return ImageFont.truetype(FONT, n)
def save(im, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path)
def box_alpha(im, threshold=8):
    return im.getchannel("A").point(lambda v: 255 if v >= threshold else 0).getbbox()
def resized(im, size):
    # Premultiplied alpha prevents dark/colored RGB in transparent pixels bleeding.
    return im.convert("RGBa").resize(size, RESAMPLE).convert("RGBA")
def normalized(src, n, family):
    im = Image.open(src).convert("RGBA")
    # Native outputs have isolated almost-transparent noise; remove only alpha 1..3.
    im.putalpha(im.getchannel("A").point(lambda a: 0 if a < 4 else a))
    bbox = box_alpha(im, 8)
    if family == "C03":
        # Technical circular alpha conditioning, not concept creation.
        # Uniform inscribed crop; no stretching, recoloring or invented material.
        bb = box_alpha(im, 128)
        cx,cy = (bb[0]+bb[2])/2,(bb[1]+bb[3])/2
        alpha=im.getchannel("A"); radii=[]
        for deg in range(360):
            a=math.radians(deg); last=0
            for r in range(1,math.ceil(max(bb[2]-bb[0],bb[3]-bb[1])/2)+3):
                x,y=round(cx+r*math.cos(a)),round(cy+r*math.sin(a))
                if alpha.getpixel((x,y)) < 128: break
                last=r
            radii.append(last)
        if min(radii)/max(radii) < .95:
            raise ValueError("Orb too irregular for minor technical normalization")
        r=min(radii)-1; left,top=round(cx-r),round(cy-r)
        body=resized(im.crop((left,top,left+2*r,top+2*r)),(round(n*.875),)*2)
        side=body.width
        mask=Image.new("L",(side*4,side*4)); ImageDraw.Draw(mask).ellipse((0,0,side*4-1,side*4-1),fill=255)
        mask=mask.resize((side,side),RESAMPLE)
        body.putalpha(ImageChops.darker(body.getchannel("A"),mask))
        out=Image.new("RGBA",(n,n)); out.alpha_composite(body,((n-side)//2,(n-side)//2))
        out.putalpha(out.getchannel("A").point(lambda a: 0 if a < 4 else a))
        return out
    support = im.getchannel("A").getbbox()
    body = im.crop(support)
    target = n * (0.75 if family == "C04" else 0.875)
    scale = target / max(bbox[2]-bbox[0], bbox[3]-bbox[1])
    body = resized(body, (round(body.width*scale), round(body.height*scale)))
    out = Image.new("RGBA", (n,n))
    out.alpha_composite(body, ((n-body.width)//2, (n-body.height)//2))
    # Remove subvisible resampling ringing; preserve antialiased edges.
    out.putalpha(out.getchannel("A").point(lambda a: 0 if a < 4 else a))
    return out
def body_sized(im, n):
    crop = im.crop(box_alpha(im))
    s = n / max(crop.size)
    return resized(crop, (round(crop.width*s), round(crop.height*s)))
def centered(bg, im, x, y):
    bg.alpha_composite(im, (round(x-im.width/2), round(y-im.height/2)))
def checker(w,h):
    im=Image.new("RGBA",(w,h),"#e3e3e3"); d=ImageDraw.Draw(im)
    for y in range(0,h,12):
        for x in range(0,w,12):
            if (x//12+y//12)%2: d.rectangle((x,y,x+11,y+11),fill="#aaaabb")
    return im
def metadata(path):
    im=Image.open(path).convert("RGBA"); a=im.getchannel("A")
    bbox=box_alpha(im,128); edge=list(a.crop((0,0,im.width,1)).getdata())+list(a.crop((0,im.height-1,im.width,im.height)).getdata())+list(a.crop((0,0,1,im.height)).getdata())+list(a.crop((im.width-1,0,im.width,im.height)).getdata())
    info=dict(path=path.relative_to(ROOT).as_posix(),width=im.width,height=im.height,mode=Image.open(path).mode,bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),alpha_extrema=a.getextrema(),body_bbox_alpha128=bbox,edge_alpha_max=max(edge))
    if bbox:
        w,h=bbox[2]-bbox[0],bbox[3]-bbox[1]
        info["body_wh"]=[w,h]; info["bbox_center_offset"]=[(bbox[0]+bbox[2])/2-im.width/2,(bbox[1]+bbox[3])/2-im.height/2]
    return info
def pi_overlay(n=44):
    # Review-only authored layer: runtime Georgia bold 25px, white alpha .95.
    s=4; im=Image.new("RGBA",(n*s,n*s))
    d=ImageDraw.Draw(im); f=ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf",round(25*n/44*s))
    bb=d.textbbox((0,0),"π",font=f)
    d.text(((n*s-(bb[2]-bb[0]))/2-bb[0],(n*s-(bb[3]-bb[1]))/2-bb[1]-n/44*s),"π",font=f,fill=(255,255,255,242))
    return resized(im,(n,n))
def controls():
    raw=Image.open(C03/"references/daily-gameplay.png").convert("RGBA")
    save(raw.crop((177,559,237,619)),C03/"references/current-player-crop.png")
    save(pi_overlay(),C03/"proofs/REVIEW-ONLY-pi-overlay-44.png")
def proof(family):
    folder=C04 if family=="C04" else C03
    cols=["CURRENT","A","B","C"]
    sheet=Image.new("RGBA",(1120,920),"#100b20"); d=ImageDraw.Draw(sheet)
    d.text((20,12),family+" | GAMEPLAY SCALE FIRST | no external halo on isolated candidates",font=font(18),fill="white")
    for i,k in enumerate(cols):
        x=20+i*275
        d.text((x,50),k,font=font(22),fill="#ffd166")
        if k=="CURRENT":
            if family=="C04": im=Image.open(folder/"references/current-chain-block-128w.png").convert("RGBA")
            else: im=Image.open(folder/"references/current-player-crop.png").convert("RGBA")
        else: im=Image.open(folder/f"normalized/{k}/{family}-{k}-128.png").convert("RGBA")
        y=98
        for n in ([45,32,64,128] if family=="C04" else [44,32,64,128]):
            panel=Image.new("RGBA",(245,145),"#2a1c4d")
            visible_n = 112 if family=="C03" and n==128 else n
            if family=="C04":
                obj=resized(im,(n,n))
                label=f"{n}px FILE box; body ~{round(n*.75)}px"
            elif k=="CURRENT":
                obj=resized(im,(round(60*visible_n/44),round(60*visible_n/44)))
                label=f"{visible_n}px nominal BODY (capture incl. pi)"
            else:
                obj=body_sized(im,visible_n); label=f"{visible_n}px BODY; no pi baked"
                if n==128: label="128px FILE / 112px BODY; no pi"
            centered(panel,obj,62,80)
            if family=="C03" and k!="CURRENT":
                centered(panel,obj,177,80); centered(panel,pi_overlay(visible_n),177,80)
            sheet.alpha_composite(panel,(x,y)); d.text((x+5,y+7),label,font=font(12),fill="white")
            if family=="C03" and k!="CURRENT": d.text((x+115,y+117),"+ review-only pi",font=font(12),fill="#d9c9ff")
            y+=155
        # Exact 45px body stress test for block; white/checker alpha inspection.
        panel=checker(245,125)
        if family=="C04":
            centered(panel,body_sized(im,45),58,64)
            centered(panel,resized(im,(96,96)),174,64)
        else:
            centered(panel,body_sized(im,44) if k!="CURRENT" else im,60,64)
            centered(panel,body_sized(im,96) if k!="CURRENT" else resized(im,(96,96)),174,64)
        sheet.alpha_composite(panel,(x,745))
        d.text((x,875),"Alpha / light background"+(" | 45px BODY stress" if family=="C04" else ""),font=font(12),fill="white")
    save(sheet.convert("RGB"),folder/f"proofs/{family}-SCALE-ALPHA-PROOF.png")
def normalize(family):
    folder=C04 if family=="C04" else C03
    sizes=[128,64,32] if family=="C04" else [128,64]
    stats=[]
    for k in "ABC":
        src=folder/f"candidates/{k}/{family}-{k}-v1-master.png"
        if not src.exists(): continue
        stats.append(metadata(src))
        for n in sizes:
            path=folder/f"normalized/{k}/{family}-{k}-{n}.png"
            save(normalized(src,n,family),path); stats.append(metadata(path))
        if family=="C03":
            im=Image.open(folder/f"normalized/{k}/{family}-{k}-128.png").convert("RGBA")
            for n in [44,32]:
                p=folder/f"proofs/{family}-{k}-body-{n}.png"; save(body_sized(im,n),p); stats.append(metadata(p))
    (folder/"review/IMAGE-METADATA.json").write_text(json.dumps(stats,indent=2),encoding="utf-8")
    proof(family)
def repair_player(im):
    # Static local review repair only: interpolate same-row colors around old body.
    # Preserves outside runtime halo; replaces old body and pi. Not runtime simulation.
    out=im.copy()
    for y in range(563,615):
        l=im.getpixel((180,y)); r=im.getpixel((234,y))
        for x in range(181,234):
            t=(x-180)/54
            out.putpixel((x,y),tuple(round(l[c]*(1-t)+r[c]*t) for c in range(4)))
    return out
def viewport():
    framed=Image.open(C04/"references/B2-gameplay-preview.png").convert("RGBA")
    return framed.crop((56,116,884,1588)).resize((414,736),RESAMPLE)
def draw_block(base,im,xy=(207,510),box=45):
    # Matched s=1 stress placement; faint backing/glow are separate review layers.
    layer=Image.new("RGBA",base.size); d=ImageDraw.Draw(layer); x,y=xy
    d.ellipse((x-30.6,y-30.6,x+30.6,y+30.6),fill=(255,255,255,25))
    d.ellipse((x-23.4,y-23.4,x+23.4,y+23.4),fill=(12,7,23,128))
    base.alpha_composite(layer); centered(base,resized(im,(box,box)),x,y)
def composites(family):
    folder=C04 if family=="C04" else C03
    for k in "ABC":
        v=viewport(); im=Image.open(folder/f"normalized/{k}/{family}-{k}-128.png").convert("RGBA")
        if family=="C04": draw_block(v,im)
        else:
            v=repair_player(v); centered(v,body_sized(im,44),207,589); centered(v,pi_overlay(),207,589)
        framed=Image.new("RGBA",(454,810),"#100b20"); d=ImageDraw.Draw(framed)
        d.text((20,10),family+"-"+k+" | REVIEW ONLY",font=font(18),fill="#ffd166")
        d.text((20,35),"45px sprite box" if family=="C04" else "44px body + separate authored pi",font=font(15),fill="white")
        framed.alpha_composite(v,(20,64))
        save(framed.convert("RGB"),folder/f"proofs/{family}-{k}-gameplay-preview.png")
def common():
    board=Image.new("RGBA",(1392,1700),"#100b20"); d=ImageDraw.Draw(board)
    d.text((20,12),"C03 + C04 | Current-control comparisons | 1 logical pixel = 1 image pixel",font=font(20),fill="white")
    for row,fam in enumerate(["C04","C03"]):
        for col,k in enumerate("ABC"):
            folder=C04 if fam=="C04" else C03
            im=Image.open(folder/f"proofs/{fam}-{k}-gameplay-preview.png").convert("RGBA")
            board.alpha_composite(im,(10+col*464,55+row*820))
    save(board.convert("RGB"),COMMON/"C03-C04-COMPARISON.png")
    # Selected material pair; real screenshot retained as side-by-side control.
    v=repair_player(viewport())
    orb=Image.open(C03/"normalized/A/C03-A-128.png").convert("RGBA")
    block=Image.open(C04/"normalized/C/C04-C-128.png").convert("RGBA")
    centered(v,body_sized(orb,44),207,589); centered(v,pi_overlay(),207,589)
    draw_block(v,block)
    out=Image.new("RGBA",(1322,830),"#100b20"); d=ImageDraw.Draw(out)
    current=Image.open(C04/"references/daily-gameplay.png").convert("RGBA")
    for x,im,title in [(10,current,"CURRENT PRODUCTION"),(454,viewport(),"B2 + CURRENT OBJECTS"),(898,v,"B2 + C04-C + C03-A (study)")]:
        d.text((x,15),title,font=font(17),fill="#ffd166"); out.alpha_composite(im,(x,60))
    d.text((10,803),"Static montage. Chain Block added at (207,510), scale=1 stress. Orb body 44px; pi separate. No runtime integration.",font=font(14),fill="white")
    save(out.convert("RGB"),COMMON/"C03-C04-GAMEPLAY-SCALE-PROOF.png")
if __name__=="__main__":
    parser=argparse.ArgumentParser(); parser.add_argument("stage",choices=["controls","C04","C03","common"]); args=parser.parse_args()
    if args.stage=="controls": controls()
    elif args.stage=="common": common()
    else: normalize(args.stage); composites(args.stage)
