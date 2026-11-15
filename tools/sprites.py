# Pixel sprites for the Black Eclipse scene (original art).
HERO = [
"........HHHH............",
".......HHHHHH...........",
"......HHHHHHHH......GG..",
"......HHHSSSSH......GG..",
".......HHSSKSS......GG..",
".......HHSSSS.......GG..",
"........HSSS........GG..",
".....ccaaAAAAa......GG..",
"....cCaaAAAAAAaa..SSGGS.",
"....cCaAAAAAAAAAaaSSGGS.",
"...cCCaAAAaAAAA..IIIIIII",
"...cCCAAAAAaAAA...bBBB..",
"...cCCAAAAAAAAA...bBBB..",
"...cCCIAAAAAAAI...bBBB..",
"..cCCCIIIIIIIII...bBBB..",
"..cCCCAAAAaAAAA...bBBB..",
"..cCCCAAAA.AAAA...bBBB..",
"..cCCCAAAA..AAA...bBBB..",
".cCCCCAAA...AAA...bBBB..",
".cCCCCAAA...AAAa..bBBB..",
".cCCCCAAA....AAA..bBBB..",
".cCCCCAAAa...AAA..bBBB..",
".cCCCIAAA....AAA..bBBB..",
"cCCCCIAAA....AAAA.bBBB..",
"cCCCIIAAAA...AAAA.bBBB..",
"ccCII.IIIII..IIIII.bBB..",
]
# two cape-tail frames, drawn left of the hero (negative columns allowed via offset)
TAIL_A = [(18,-1),(19,-1),(20,-1),(21,-2),(22,-2),(23,-2),(24,-2),(24,-1),(25,-1)]
TAIL_B = [(14,1),(15,0),(16,0),(17,-1),(18,-1),(19,-2),(20,-2),(20,-3),(21,-3)]
PAL = {
 'H':'#1a1214','S':'#b98a6c','K':'#0b0809','A':'#2c2528','a':'#544a4f','I':'#121012',
 'C':'#6a1117','c':'#40090d','B':'#7b7d84','b':'#b9bcc4','G':'#5b4532',
}
OUT = '#040203'
CROW_A = ["K.......K",".K.....K.","..KKKKK..","...KKKKK.","....K...."]
CROW_B = [".........","..KKKKK..",".KKKKKKKK","K...K...K","........."]

def runs(grid, colors, ox=0, oy=0, px=7):
    """Merge horizontal runs of one color into rects."""
    out=[]
    for y,row in enumerate(grid):
        x=0
        while x < len(row):
            ch=row[x]
            if ch=='.':
                x+=1; continue
            s=x
            while x < len(row) and row[x]==ch: x+=1
            out.append(f'<rect x="{ox+s*px}" y="{oy+y*px}" width="{(x-s)*px}" height="{px}" fill="{colors[ch]}"/>')
    return ''.join(out)

def outline(grid):
    h=len(grid); w=len(grid[0])
    g=[['.']*(w+2) for _ in range(h+2)]
    for y in range(h):
        for x in range(w):
            if grid[y][x]!='.':
                for dy,dx in ((0,1),(1,0),(1,2),(2,1)):
                    if g[y+dy][x+dx]=='.': g[y+dy][x+dx]='O'
    for y in range(h):
        for x in range(w):
            if grid[y][x]!='.': g[y+1][x+1]='.'
    return [''.join(r) for r in g]

def pts(cells, ox, oy, px, color):
    return ''.join(f'<rect x="{ox+c*px}" y="{oy+r*px}" width="{px}" height="{px}" fill="{color}"/>' for r,c in cells)

def hero_svg(ox, oy, px=7):
    assert all(len(r)==24 for r in HERO), [len(r) for r in HERO]
    body = runs(HERO, PAL, ox, oy, px)
    ol = runs(outline(HERO), {'O':OUT}, ox-px, oy-px, px)
    ta = pts(TAIL_A, ox, oy, px, PAL['c'])
    tb = pts(TAIL_B, ox, oy, px, PAL['c'])
    glint = f'<rect class="glint" x="{ox+19*px}" y="{oy+11*px}" width="{px}" height="{px}" fill="#fff2e0"/>'
    return f'<g class="hero">{ol}<g class="tailA">{ta}</g><g class="tailB">{tb}</g>{body}{glint}</g>'

def crow_svg(cls, px=4):
    a = runs(CROW_A, {'K':'#060404'}, 0, 0, px)
    b = runs(CROW_B, {'K':'#060404'}, 0, 0, px)
    return f'<g class="crow {cls}"><g class="fa">{a}</g><g class="fb">{b}</g></g>'
