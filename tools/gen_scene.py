import random, sys
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import sprites
random.seed(7)
embers=[]
for i in range(34):
    x=random.randint(40,1560); r=round(random.uniform(1.2,3.6),1)
    dur=round(random.uniform(11,24),1); delay=round(-random.uniform(0,24),1)
    sway=random.choice(['a','b','c'])
    hot=random.random()<0.35
    embers.append(f'<circle class="e s{sway}{" hot" if hot else ""}" cx="{x}" cy="1030" r="{r}" style="animation-duration:{dur}s;animation-delay:{delay}s"/>')
ridge="M0 1000 L0 905 L70 880 L120 896 L190 850 L240 872 L300 838 L350 860 L420 820 L470 846 L540 832 L610 868 L680 850 L760 884 L840 866 L920 892 L1000 870 L1060 836 L1110 858 L1180 810 L1205 786 L1213 772 L1400 772 L1412 792 L1440 812 L1420 846 L1480 830 L1540 862 L1600 850 L1600 1000 Z"
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice">
<style>
.sky0{{stop-color:#2a0709}}.sky1{{stop-color:#120607}}.sky2{{stop-color:#070505}}
.ridge{{fill:#050303}}.mist{{fill:#3a0d10;opacity:.22}}
.corona{{fill:url(#cor);transform-origin:1300px 230px;animation:pulse 9s ease-in-out infinite}}
.moon{{fill:#030202}}.rim{{fill:none;stroke:#ff5a3c;stroke-width:2.2;opacity:.85;animation:flick 6s ease-in-out infinite}}
.ray{{stroke:#b3141c;stroke-width:1.4;opacity:.22;transform-origin:1300px 230px;animation:turn 120s linear infinite}}
.e{{fill:#e2521f;filter:url(#glow);animation-name:rise;animation-timing-function:linear;animation-iteration-count:infinite;opacity:0}}
.e.hot{{fill:#ffb347}}
.sa{{--dx:60px}}.sb{{--dx:-80px}}.sc{{--dx:30px}}
.m1{{animation:drift 70s linear infinite}}.m2{{animation:drift 95s linear infinite reverse}}
@keyframes rise{{0%{{transform:translate(0,0);opacity:0}}8%{{opacity:.9}}50%{{transform:translate(var(--dx),-560px)}}85%{{opacity:.55}}100%{{transform:translate(calc(var(--dx) * -0.4),-1120px);opacity:0}}}}
@keyframes pulse{{0%,100%{{transform:scale(1);opacity:.85}}50%{{transform:scale(1.07);opacity:1}}}}
@keyframes flick{{0%,100%{{opacity:.85}}45%{{opacity:.55}}60%{{opacity:1}}}}
@keyframes turn{{to{{transform:rotate(360deg)}}}}
@keyframes drift{{from{{transform:translateX(-400px)}}to{{transform:translateX(400px)}}}}
.hero{{shape-rendering:crispEdges}}
.tailA{{animation:capeA 1.4s steps(1) infinite}}.tailB{{animation:capeB 1.4s steps(1) infinite}}
@keyframes capeA{{0%{{opacity:1}}50%{{opacity:0}}}}@keyframes capeB{{0%{{opacity:0}}50%{{opacity:1}}}}
.glint{{opacity:0;animation:glint 8s steps(14) infinite}}
@keyframes glint{{0%,72%{{transform:translateY(0);opacity:0}}73%{{transform:translateY(0);opacity:1}}100%{{transform:translateY(98px);opacity:1}}}}
.crow{{shape-rendering:crispEdges;animation:fly linear infinite}}
.c1{{animation-duration:46s;animation-delay:-6s}}.c2{{animation-duration:58s;animation-delay:-30s}}.c3{{animation-duration:52s;animation-delay:-41s}}
.fa{{animation:capeA .5s steps(1) infinite}}.fb{{animation:capeB .5s steps(1) infinite}}
@keyframes fly{{0%{{transform:translate(-120px,var(--y))}}50%{{transform:translate(800px,calc(var(--y) - 40px))}}100%{{transform:translate(1720px,var(--y))}}}}
.c1{{--y:150px}}.c2{{--y:330px}}.c3{{--y:90px}}
@media (prefers-color-scheme: light){{
.sky0{{stop-color:#c9a990}}.sky1{{stop-color:#ddc9ad}}.sky2{{stop-color:#e8dcc5}}
.ridge{{fill:#3a2a24;opacity:.55}}.mist{{fill:#f2e8d6;opacity:.5}}
.moon{{fill:#1a0d0c}}.ray{{opacity:.3}}
}}
@media (max-aspect-ratio: 1/1){{.hero-wrap{{transform:translateX(-470px)}}.eclipse{{transform:translate(-300px,40px) scale(.8);transform-origin:1300px 230px}}}}
@media (prefers-reduced-motion: reduce){{*{{animation:none!important}}.e{{opacity:.5}}}}
</style>
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="sky0"/><stop offset=".55" class="sky1"/><stop offset="1" class="sky2"/></linearGradient>
<radialGradient id="cor" cx="1300" cy="230" r="300" gradientUnits="userSpaceOnUse">
<stop offset=".28" stop-color="#ff4a2a" stop-opacity="1"/><stop offset=".36" stop-color="#c0161e" stop-opacity=".8"/>
<stop offset=".6" stop-color="#7a0c12" stop-opacity=".35"/><stop offset="1" stop-color="#3a0507" stop-opacity="0"/></radialGradient>
<radialGradient id="aura"><stop offset="0" stop-color="#b3141c" stop-opacity=".45"/><stop offset="1" stop-color="#b3141c" stop-opacity="0"/></radialGradient>
<filter id="glow" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="1600" height="1000" fill="url(#sky)"/>
<g class="eclipse">
<g class="ray">{"".join(f'<line x1="1300" y1="230" x2="{1300+int(420*__import__("math").cos(a*0.2618))}" y2="{230+int(420*__import__("math").sin(a*0.2618))}"/>' for a in range(24))}</g>
<circle class="corona" cx="1300" cy="230" r="300"/>
<circle class="moon" cx="1300" cy="230" r="86"/>
<circle class="rim" cx="1300" cy="230" r="87"/>
</g>
<g class="m1"><ellipse class="mist" cx="500" cy="760" rx="700" ry="60"/></g>
<g class="m2"><ellipse class="mist" cx="1100" cy="840" rx="800" ry="70"/></g>
<g>{sprites.crow_svg("c1")}{sprites.crow_svg("c2")}{sprites.crow_svg("c3")}</g>
<path class="ridge" d="{ridge}"/>
<g class="hero-wrap"><ellipse cx="1300" cy="690" rx="190" ry="150" fill="url(#aura)"/>{sprites.hero_svg(1222,590)}</g>
<g>{"".join(embers)}</g>
</svg>'''
open(sys.argv[1],'w').write('// Generated scene: a blood-red eclipse, a pixel swordsman on a crag, crows, embers rising.\nexport const SCENE = `'+svg.replace('`','')+'`\n')
print(len(svg))
