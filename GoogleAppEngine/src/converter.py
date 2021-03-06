# author: Sven Kreiss <sk@svenkreiss.com>
import sys, re

replacements = [
    [r'\\textfractionsolidus', u'\u2044'],
    [r'\\leftrightsquigarrow', u'\u21AD'],
    [r'\\textpertenthousand', u'\u2031'],
    [r'\\blacktriangleright', u'\u25B8'],
    [r'\\blacktriangledown', u'\u25BE'],
    [r'\\blacktriangleleft', u'\u25C2'],
    [r'\\twoheadrightarrow', u'\u21A0'],
    [r'\\leftrightharpoons', u'\u21CB'],
    [r'\\rightleftharpoons', u'\u21CC'],
    [r'\\textreferencemark', u'\u203B'],
    [r'\\circlearrowright', u'\u21BB'],
    [r'\\rightrightarrows', u'\u21C9'],
    [r'\\vartriangleright', u'\u22B3'],
    [r'\\textordmasculine', u'\u00BA'],
    [r'\\textvisiblespace', u'\u2423'],
    [r'\\twoheadleftarrow', u'\u219E'],
    [r'\\downharpoonright', u'\u21C2'],
    [r'\\ntrianglerighteq', u'\u22ED'],
    [r'\\rightharpoondown', u'\u21C1'],
    [r'\\textperthousand', u'\u2030'],
    [r'\\leftrightarrows', u'\u21C6'],
    [r'\\textmusicalnote', u'\u266A'],
    [r'\\nleftrightarrow', u'\u21AE'],
    [r'\\rightleftarrows', u'\u21C4'],
    [r'\\bigtriangledown', u'\u25BD'],
    [r'\\textordfeminine', u'\u00AA'],
    [r'\\ntrianglelefteq', u'\u22EC'],
    [r'\\rightthreetimes', u'\u22CC'],
    [r'\\trianglerighteq', u'\u22B5'],
    [r'\\vartriangleleft', u'\u22B2'],
    [r'\\rightsquigarrow', u'\u21DD'],
    [r'\\downharpoonleft', u'\u21C3'],
    [r'\\curvearrowright', u'\u21B7'],
    [r'\\circlearrowleft', u'\u21BA'],
    [r'\\leftharpoondown', u'\u21BD'],
    [r'\\nLeftrightarrow', u'\u21CE'],
    [r'\\curvearrowleft', u'\u21B6'],
    [r'\\guilsinglright', u'\u203A'],
    [r'\\leftthreetimes', u'\u22CB'],
    [r'\\leftrightarrow', u'\u2194'],
    [r'\\rightharpoonup', u'\u21C0'],
    [r'\\guillemotright', u'\u00BB'],
    [r'\\downdownarrows', u'\u21CA'],
    [r'\\hookrightarrow', u'\u21AA'],
    [r'\\hspace\{0\.25em}', u'\u2005'],
    [r'\\dashrightarrow', u'\u21E2'],
    [r'\\leftleftarrows', u'\u21C7'],
    [r'\\trianglelefteq', u'\u22B4'],
    [r'\\ntriangleright', u'\u22EB'],
    [r'\\doublebarwedge', u'\u2306'],
    [r'\\upharpoonright', u'\u21BE'],
    [r'\\rightarrowtail', u'\u21A3'],
    [r'\\looparrowright', u'\u21AC'],
    [r'\\Leftrightarrow', u'\u21D4'],
    [r'\\sphericalangle', u'\u2222'],
    [r'\\divideontimes', u'\u22C7'],
    [r'\\measuredangle', u'\u2221'],
    [r'\\blacktriangle', u'\u25B4'],
    [r'\\ntriangleleft', u'\u22EA'],
    [r'\\mathchar"1356', u'\u2041'],
    [r'\\texttrademark', u'\u2122'],
    [r'\\mathchar"2208', u'\u2316'],
    [r'\\triangleright', u'\u25B9'],
    [r'\\leftarrowtail', u'\u21A2'],
    [r'\\guilsinglleft', u'\u2039'],
    [r'\\upharpoonleft', u'\u21BF'],
    [r'\\mathbb\{gamma}', u'\u213D'],
    [r'\\fallingdotseq', u'\u2252'],
    [r'\\dashleftarrow', u'\u21E0'],
    [r'\\looparrowleft', u'\u21AB'],
    [r'\\textbrokenbar', u'\u00A6'],
    [r'\\hookleftarrow', u'\u21A9'],
    [r'\\smallsetminus', u'\uFE68'],
    [r'\\guillemotleft', u'\u00AB'],
    [r'\\leftharpoonup', u'\u21BC'],
    [r'\\mathbb\{Gamma}', u'\u213E'],
    [r'\\bigtriangleup', u'\u25B3'],
    [r'\\textcircledP', u'\u2117'],
    [r'\\risingdotseq', u'\u2253'],
    [r'\\triangleleft', u'\u25C3'],
    [r'\\mathsterling', u'\u00A3'],
    [r'\\textcurrency', u'\u00A4'],
    [r'\\triangledown', u'\u25BF'],
    [r'\\blacklozenge', u'\uE80B'],
    [r'\\sfrac\{5}\{6}', u'\u215A'],
    [r'\\preccurlyeq', u'\u227C'],
    [r'\\Rrightarrow', u'\u21DB'],
    [r'\\circledcirc', u'\u229A'],
    [r'\\nRightarrow', u'\u21CF'],
    [r'\\sfrac\{3}\{8}', u'\u215C'],
    [r'\\sfrac\{1}\{3}', u'\u2153'],
    [r'\\sfrac\{2}\{5}', u'\u2156'],
    [r'\\vartriangle', u'\u25B5'],
    [r'\\Updownarrow', u'\u21D5'],
    [r'\\nrightarrow', u'\u219B'],
    [r'\\sfrac\{1}\{2}', u'\u00BD'],
    [r'\\sfrac\{3}\{5}', u'\u2157'],
    [r'\\succcurlyeq', u'\u227D'],
    [r'\\sfrac\{4}\{5}', u'\u2158'],
    [r'\\diamondsuit', u'\u2666'],
    [r'\\hphantom\{0}', u'\u2007'],
    [r'\\sfrac\{1}\{6}', u'\u2159'],
    [r'\\curlyeqsucc', u'\u22DF'],
    [r'\\blacksquare', u'\u25AA'],
    [r'\\hphantom\{,}', u'\u2008'],
    [r'\\curlyeqprec', u'\u22DE'],
    [r'\\sfrac\{1}\{8}', u'\u215B'],
    [r'\\sfrac\{7}\{8}', u'\u215E'],
    [r'\\sfrac\{1}\{5}', u'\u2155'],
    [r'\\sfrac\{2}\{3}', u'\u2154'],
    [r'\\updownarrow', u'\u2195'],
    [r'\\backepsilon', u'\u220D'],
    [r'\\circleddash', u'\u229D'],
    [r'\\eqslantless', u'\u22DC'],
    [r'\\sfrac\{3}\{4}', u'\u00BE'],
    [r'\\sfrac\{5}\{8}', u'\u215D'],
    [r'\\hspace\{1pt}', u'\u200A'],
    [r'\\sfrac\{1}\{4}', u'\u00BC'],
    [r'\\mathbb\{Pi}', u'\u213F'],
    [r'\\mathcal\{M}', u'\u2133'],
    [r'\\mathcal\{O}', u'\u1D4AA'],
    [r'\\mathcal\{o}', u'\u02134'],
    [r'\\nsupseteqq', u'\u2289'],
    [r'\\mathcal\{B}', u'\u212C'],
    [r'\\textrecipe', u'\u211E'],
    [r'\\nsubseteqq', u'\u2288'],
    [r'\\subsetneqq', u'\u228A'],
    [r'\\mathcal\{I}', u'\u2111'],
    [r'\\upuparrows', u'\u21C8'],
    [r'\\mathcal\{e}', u'\u212F'],
    [r'\\mathcal\{L}', u'\u2112'],
    [r'\\nleftarrow', u'\u219A'],
    [r'\\mathcal\{H}', u'\u210B'],
    [r'\\mathcal\{E}', u'\u2130'],
    [r'\\eqslantgtr', u'\u22DD'],
    [r'\\curlywedge', u'\u22CF'],
    [r'\\varepsilon', u'\u03B5'],
    [r'\\supsetneqq', u'\u228B'],
    [r'\\rightarrow', u'\u2192'],
    [r'\\mathcal\{R}', u'\u211B'],
    [r'\\sqsubseteq', u'\u2291'],
    [r'\\mathcal\{g}', u'\u210A'],
    [r'\\sqsupseteq', u'\u2292'],
    [r'\\complement', u'\u2201'],
    [r'\\Rightarrow', u'\u21D2'],
    [r'\\gtreqqless', u'\u22DB'],
    [r'\\lesseqqgtr', u'\u22DA'],
    [r'\\circledast', u'\u229B'],
    [r'\\nLeftarrow', u'\u21CD'],
    [r'\\Lleftarrow', u'\u21DA'],
    [r'\\Leftarrow', u'\u21D0'],
    [r'\\gvertneqq', u'\u2269'],
    [r'\\mathbb\{C}', u'\u2102'],
    [r'\\supsetneq', u'\u228B'],
    [r'\\leftarrow', u'\u2190'],
    [r'\\nleqslant', u'\u2270'],
    [r'\\mathbb\{Q}', u'\u211A'],
    [r'\\mathbb\{Z}', u'\u2124'],
    [r'\\llbracket', u'\u301A'],
    [r'\\mathbb\{H}', u'\u210D'],
    [r'\\spadesuit', u'\u2660'],
    [r'\\mathit\{o}', u'\u2134'],
    [r'\\mathbb\{P}', u'\u2119'],
    [r'\\rrbracket', u'\u301B'],
    [r'\\supseteqq', u'\u2287'],
    [r'\\copyright', u'\u00A9'],
    [r'\\textsc\{k}', u'\u0138'],
    [r'\\gtreqless', u'\u22DB'],
    [r'\\mathbb\{j}', u'\u2149'],
    [r'\\pitchfork', u'\u22D4'],
    [r'\\estimated', u'\u212E'],
    [r'\\ngeqslant', u'\u2271'],
    [r'\\mathbb\{e}', u'\u2147'],
    [r'\\therefore', u'\u2234'],
    [r'\\triangleq', u'\u225C'],
    [r'\\varpropto', u'\u221D'],
    [r'\\subsetneq', u'\u228A'],
    [r'\\heartsuit', u'\u2665'],
    [r'\\mathbb\{d}', u'\u2146'],
    [r'\\lvertneqq', u'\u2268'],
    [r'\\checkmark', u'\u2713'],
    [r'\\nparallel', u'\u2226'],
    [r'\\mathbb\{R}', u'\u211D'],
    [r'\\lesseqgtr', u'\u22DA'],
    [r'\\downarrow', u'\u2193'],
    [r'\\mathbb\{D}', u'\u2145'],
    [r'\\mathbb\{i}', u'\u2148'],
    [r'\\backsimeq', u'\u22CD'],
    [r'\\mathbb\{N}', u'\u2115'],
    [r'\\Downarrow', u'\u21D3'],
    [r'\\subseteqq', u'\u2286'],
    [r'\\setminus', u'\u2216'],
    [r'\\succnsim', u'\u22E9'],
    [r'\\doteqdot', u'\u2251'],
    [r'\\clubsuit', u'\u2663'],
    [r'\\emptyset', u'\u2205'],
    [r'\\varnothing', u'\u2205'],
    [r'\\sqsupset', u'\u2290'],
    [r'\\fbox\{~~}', u'\u25AD'],
    [r'\\curlyvee', u'\u22CE'],
    [r'\\varkappa', u'\u03F0'],
    [r'\\llcorner', u'\u231E'],
    [r'\\varsigma', u'\u03C2'],
    [r'\\approxeq', u'\u224A'],
    [r'\\backcong', u'\u224C'],
    [r'\\supseteq', u'\u2287'],
    [r'\\circledS', u'\u24C8'],
    [r'\\circledR', u'\u00AE'],
    [r'\\textcent', u'\u00A2'],
    [r'\\urcorner', u'\u231D'],
    [r'\\lrcorner', u'\u231F'],
    [r'\\boxminus', u'\u229F'],
    [r'\\texteuro', u'\u20AC'],
    [r'\\vartheta', u'\u03D1'],
    [r'\\barwedge', u'\u22BC'],
    [r'\\ding\{86}', u'\u2736'],
    [r'\\sqsubset', u'\u228F'],
    [r'\\subseteq', u'\u2286'],
    [r'\\intercal', u'\u22BA'],
    [r'\\ding\{73}', u'\u2606'],
    [r'\\ulcorner', u'\u231C'],
    [r'\\recorder', u'\u2315'],
    [r'\\precnsim', u'\u22E8'],
    [r'\\parallel', u'\u2225'],
    [r'\\boxtimes', u'\u22A0'],
    [r'\\ding\{55}', u'\u2717'],
    [r'\\multimap', u'\u22B8'],
    [r'\\maltese', u'\u2720'],
    [r'\\nearrow', u'\u2197'],
    [r'\\swarrow', u'\u2199'],
    [r'\\lozenge', u'\u25CA'],
    [r'\\succsim', u'\u227F'],
    [r'\\tilde\{}', u'\u007E'],
    [r'\\lessgtr', u'\u2276'],
    [r'\\Upsilon', u'\u03D2'],
    [r'\\Cdprime', u'\u042A'],
    [r'\\gtrless', u'\u2277'],
    [r'\\backsim', u'\u223D'],
    [r'\\nexists', u'\u2204'],
    [r'\\dotplus', u'\u2214'],
    [r'\\searrow', u'\u2198'],
    [r'\\lessdot', u'\u22D6'],
    [r'\\boxplus', u'\u229E'],
    [r'\\upsilon', u'\u03C5'],
    [r'\\epsilon', u'\u03B5'],
    [r'\\diamond', u'\u22C4'],
    [r'\\bigstar', u'\u2605'],
    [r'\\ddagger', u'\u2021'],
    [r'\\cdprime', u'\u044A'],
    [r'\\Uparrow', u'\u21D1'],
    [r'\\between', u'\u226C'],
    [r'\\sqangle', u'\u221F'],
    [r'\\digamma', u'\u03DC'],
    [r'\\uparrow', u'\u2191'],
    [r'\\nwarrow', u'\u2196'],
    [r'\\precsim', u'\u227E'],
    [r'\\breve\{}', u'\u02D8'],
    [r'\\because', u'\u2235'],
    [r'\\bigcirc', u'\u25EF'],
    [r'\\acute\{}', u'\u00B4'],
    [r'\\grave\{}', u'\u0060'],
    [r'\\check\{}', u'\u02C7'],
    [r'\\lesssim', u'\u2272'],
    [r'\\partial', u'\u2202'],
    [r'\\natural', u'\u266E'],
    [r'\\supset', u'\u2283'],
    [r'\\hstrok', u'\u0127'],
    [r'\\Tstrok', u'\u0166'],
    [r'\\coprod', u'\u2210'],
    [r'\\models', u'\u22A7'],
    [r'\\otimes', u'\u2297'],
    [r'\\degree', u'\u00B0'],
    [r'\\gtrdot', u'\u22D7'],
    [r'\\preceq', u'\u227C'],
    [r'\\Lambda', u'\u039B'],
    [r'\\lambda', u'\u03BB'],
    [r'\\cprime', u'\u044C'],
    [r'\\varrho', u'\u03F1'],
    [r'\\Bumpeq', u'\u224E'],
    [r'\\hybull', u'\u2043'],
    [r'\\lmidot', u'\u0140'],
    [r'\\nvdash', u'\u22AC'],
    [r'\\lbrace', u'\u007B'],
    [r'\\bullet', u'\u2022'],
    [r'\\varphi', u'\u03D5'],
    [r'\\bumpeq', u'\u224F'],
    [r'\\ddot\{}', u'\u00A8'],
    [r'\\Lmidot', u'\u013F'],
    [r'\\Cprime', u'\u042C'],
    [r'\\female', u'\u2640'],
    [r'\\rtimes', u'\u22CA'],
    [r'\\gtrsim', u'\u2273'],
    [r'\\mapsto', u'\u21A6'],
    [r'\\daleth', u'\u2138'],
    [r'\\square', u'\u25A0'],
    [r'\\nVDash', u'\u22AF'],
    [r'\\rangle', u'\u3009'],
    [r'\\tstrok', u'\u0167'],
    [r'\\oslash', u'\u2298'],
    [r'\\ltimes', u'\u22C9'],
    [r'\\lfloor', u'\u230A'],
    [r'\\marker', u'\u25AE'],
    [r'\\Subset', u'\u22D0'],
    [r'\\Vvdash', u'\u22AA'],
    [r'\\propto', u'\u221D'],
    [r'\\dlcrop', u'\u230D'],
    [r'\\Hstrok', u'\u0126'],
    [r'\\forall', u'\u2200'],
    [r'\\nVdash', u'\u22AE'],
    [r'\\Supset', u'\u22D1'],
    [r'\\langle', u'\u3008'],
    [r'\\ominus', u'\u2296'],
    [r'\\rfloor', u'\u230B'],
    [r'\\circeq', u'\u2257'],
    [r'\\eqcirc', u'\u2256'],
    [r'\\drcrop', u'\u230C'],
    [r'\\veebar', u'\u22BB'],
    [r'\\ulcrop', u'\u230F'],
    [r'\\nvDash', u'\u22AD'],
    [r'\\urcrop', u'\u230E'],
    [r'\\exists', u'\u2203'],
    [r'\\approx', u'\u2248'],
    [r'\\dagger', u'\u2020'],
    [r'\\boxdot', u'\u22A1'],
    [r'\\succeq', u'\u227D'],
    [r'\\bowtie', u'\u22C8'],
    [r'\\subset', u'\u2282'],
    [r'\\Sigma', u'\u03A3'],
    [r'\\Omega', u'\u03A9'],
    [r'\\nabla', u'\u2207'],
    [r'\\colon', u'\u003A'],
    [r'\\boxHu', u'\u2567'],
    [r'\\boxHd', u'\u2564'],
    [r'\\aleph', u'\u2135'],
    [r'\\gnsim', u'\u22E7'],
    [r'\\boxHU', u'\u2569'],
    [r'\\boxHD', u'\u2566'],
    [r'\\equiv', u'\u2261'],
    [r'\\lneqq', u'\u2268'],
    [r'\\alpha', u'\u03B1'],
    [r'\\amalg', u'\u2210'],
    [r'\\boxhU', u'\u2568'],
    [r'\\boxhD', u'\u2565'],
    [r'\\uplus', u'\u228E'],
    [r'\\boxhu', u'\u2534'],
    [r'\\kappa', u'\u03BA'],
    [r'\\sigma', u'\u03C3'],
    [r'\\boxDL', u'\u2557'],
    [r'\\Theta', u'\u0398'],
    [r'\\Vdash', u'\u22A9'],
    [r'\\boxDR', u'\u2554'],
    [r'\\boxDl', u'\u2556'],
    [r'\\sqcap', u'\u2293'],
    [r'\\boxDr', u'\u2553'],
    [r'\\bar\{}', u'\u00AF'],
    [r'\\dashv', u'\u22A3'],
    [r'\\vDash', u'\u22A8'],
    [r'\\boxdl', u'\u2510'],
    [r'\\boxVl', u'\u2562'],
    [r'\\boxVh', u'\u256B'],
    [r'\\boxVr', u'\u255F'],
    [r'\\boxdr', u'\u250C'],
    [r'\\boxdL', u'\u2555'],
    [r'\\boxVL', u'\u2563'],
    [r'\\boxVH', u'\u256C'],
    [r'\\boxVR', u'\u2560'],
    [r'\\boxdR', u'\u2552'],
    [r'\\theta', u'\u03B8'],
    [r'\\lhblk', u'\u2584'],
    [r'\\uhblk', u'\u2580'],
    [r'\\ldotp', u'\u002E'],
    [r'\\ldots', u'\u2026'],
    [r'\\boxvL', u'\u2561'],
    [r'\\boxvH', u'\u256A'],
    [r'\\boxvR', u'\u255E'],
    [r'\\boxvl', u'\u2524'],
    [r'\\boxvh', u'\u253C'],
    [r'\\boxvr', u'\u251C'],
    [r'\\Delta', u'\u0394'],
    [r'\\boxUR', u'\u255A'],
    [r'\\boxUL', u'\u255D'],
    [r'\\oplus', u'\u2295'],
    [r'\\boxUr', u'\u2559'],
    [r'\\boxUl', u'\u255C'],
    [r'\\doteq', u'\u2250'],
    [r'\\happy', u'\u32E1'],
    [r'\\varpi', u'\u03D6'],
    [r'\\boxur', u'\u2514'],
    [r'\\smile', u'\u263A'],
    [r'\\boxul', u'\u2518'],
    [r'\\simeq', u'\u2243'],
    [r'\\boxuR', u'\u2558'],
    [r'\\boxuL', u'\u255B'],
    [r'\\boxhd', u'\u252C'],
    [r'\\gimel', u'\u2137'],
    [r'\\Gamma', u'\u0393'],
    [r'\\lnsim', u'\u22E6'],
    [r'\\sqcup', u'\u2294'],
    [r'\\omega', u'\u03C9'],
    [r'\\sharp', u'\u266F'],
    [r'\\times', u'\u00D7'],
    [r'\\block', u'\u2588'],
    [r'\\hat\{}', u'\u005E'],
    [r'\\wedge', u'\u2227'],
    [r'\\vdash', u'\u22A2'],
    [r'\\angle', u'\u2220'],
    [r'\\infty', u'\u221E'],
    [r'\\gamma', u'\u03B3'],
    [r'\\asymp', u'\u224D'],
    [r'\\rceil', u'\u2309'],
    [r'\\dot\{}', u'\u02D9'],
    [r'\\lceil', u'\u2308'],
    [r'\\delta', u'\u03B4'],
    [r'\\gneqq', u'\u2269'],
    [r'\\frown', u'\u2322'],
    [r'\\phone', u'\u260E'],
    [r'\\vdots', u'\u22EE'],
    [r'\\k\{i}', u'\u012F'],
    [r'\\`\{I}', u'\u00CC'],
    [r'\\perp', u'\u22A5'],
    [r'\\"\{o}', u'\u00F6'],
    [r'\\=\{I}', u'\u012A'],
    [r'\\`\{a}', u'\u00E0'],
    [r'\\v\{T}', u'\u0164'],
    [r'\\surd', u'\u221A'],
    [r'\\H\{O}', u'\u0150'],
    [r'\\vert', u'\u007C'],
    [r'\\k\{I}', u'\u012E'],
    [r'\\"\{y}', u'\u00FF'],
    [r'\\"\{O}', u'\u00D6'],
    [r'\\\'\{Y}', u'\u00DD'],
    [r'\\u\{u}', u'\u045E'],
    [r'\\u\{G}', u'\u011E'],
    [r'\\\.\{E}', u'\u0116'],
    [r'\\\.\{z}', u'\u017C'],
    [r'\\\^\{s}', u'\u015D'],
    [r'\\v\{t}', u'\u0165'],
    [r'\\prec', u'\u227A'],
    [r'\\H\{o}', u'\u0151'],
    [r'\\mldr', u'\u2026'],
    [r'\\\'\{y}', u'\u00FD'],
    [r'\\cong', u'\u2245'],
    [r'\\\.\{e}', u'\u0117'],
    [r'\\\'\{L}', u'\u0139'],
    [r'\\star', u'\u002A'],
    [r'\\\.\{Z}', u'\u017B'],
    [r'\\r\{u}', u'\u016F'],
    [r'\\\'\{e}', u'\u00E9'],
    [r'\\geqq', u'\u2267'],
    [r'\\cdot', u'\u22C5'],
    [r'\\`\{U}', u'\u00D9'],
    [r'\\\'\{l}', u'\u013A'],
    [r'\\\^\{J}', u'\u0134'],
    [r'\\v\{L}', u'\u013D'],
    [r'\\c\{s}', u'\u015F'],
    [r'\\\'\{s}', u'\u015B'],
    [r'\\~\{A}', u'\u00C3'],
    [r'\\Vert', u'\u2016'],
    [r'\\k\{e}', u'\u0119'],
    [r'\\lnot', u'\u00AC'],
    [r'\\\'\{z}', u'\u017A'],
    [r'\\leqq', u'\u2266'],
    [r'\\beta', u'\u03B2'],
    [r'\\beth', u'\u2136'],
    [r'\\\'\{E}', u'\u00C9'],
    [r'\\~\{n}', u'\u00F1'],
    [r'\\u\{i}', u'\u0439'],
    [r'\\c\{S}', u'\u015E'],
    [r'\\c\{N}', u'\u0145'],
    [r'\\H\{u}', u'\u0171'],
    [r'\\v\{n}', u'\u0148'],
    [r'\\\'\{S}', u'\u015A'],
    [r'\\=\{U}', u'\u016A'],
    [r'\\~\{O}', u'\u00D5'],
    [r'\\\^\{I}', u'\u00CE'],
    [r'\\\'\{Z}', u'\u0179'],
    [r'\\v\{E}', u'\u011A'],
    [r'\\\'\{R}', u'\u0154'],
    [r'\\H\{U}', u'\u0170'],
    [r'\\v\{N}', u'\u0147'],
    [r'\\prod', u'\u220F'],
    [r'\\\^\{W}', u'\u0174'],
    [r'\\v\{s}', u'\u0161'],
    [r'\\"\{U}', u'\u00DC'],
    [r'\\c\{n}', u'\u0146'],
    [r'\\\^\{e}', u'\u00EA'],
    [r'\\k\{U}', u'\u0172'],
    [r'\\c\{R}', u'\u0156'],
    [r'\\\'\{A}', u'\u00C1'],
    [r'\\~\{o}', u'\u00F5'],
    [r'\\v\{e}', u'\u011B'],
    [r'\\\^\{w}', u'\u0175'],
    [r'\\v\{S}', u'\u0160'],
    [r'\\u\{A}', u'\u0102'],
    [r'\\circ', u'\u2218'],
    [r'\\"\{u}', u'\u00FC'],
    [r'\\\^\{E}', u'\u00CA'],
    [r'\\flat', u'\u266D'],
    [r'\\v\{z}', u'\u017E'],
    [r'\\\^\{S}', u'\u015C'],
    [r'\\\^\{a}', u'\u00E2'],
    [r'\\`\{O}', u'\u00D2'],
    [r'\\=\{u}', u'\u016B'],
    [r'\\oint', u'\u222E'],
    [r'\\c\{K}', u'\u0136'],
    [r'\\k\{u}', u'\u0173'],
    [r'\\not<', u'\u226E'],
    [r'\\not>', u'\u226F'],
    [r'\\`\{o}', u'\u00F2'],
    [r'\\"\{I}', u'\u00CF'],
    [r'\\v\{D}', u'\u010E'],
    [r'\\\^\{H}', u'\u0124'],
    [r'\\\.\{G}', u'\u0120'],
    [r'\\\^\{A}', u'\u00C2'],
    [r'\\\^\{o}', u'\u00F4'],
    [r'\\not=', u'\u2260'],
    [r'\\`\{u}', u'\u00F9'],
    [r'\\v\{c}', u'\u010D'],
    [r'\\c\{k}', u'\u0137'],
    [r'\\\^\{h}', u'\u0125'],
    [r'\\\.\{g}', u'\u0121'],
    [r'\\\'\{N}', u'\u0143'],
    [r'\\odot', u'\u2299'],
    [r'\\`\{e}', u'\u044D'],
    [r'\\c\{T}', u'\u0162'],
    [r'\\v\{d}', u'\u010F'],
    [r'\\"\{e}', u'\u0451'],
    [r'\\\'\{I}', u'\u00CD'],
    [r'\\v\{R}', u'\u0158'],
    [r'\\\^\{u}', u'\u00FB'],
    [r'\\k\{a}', u'\u0105'],
    [r'\\nldr', u'\u2025'],
    [r'\\\^\{O}', u'\u00D4'],
    [r'\\`\{A}', u'\u00C0'],
    [r'\\\'\{n}', u'\u0144'],
    [r'\\~\{N}', u'\u00D1'],
    [r'\\nmid', u'\u2224'],
    [r'\\\.\{C}', u'\u010A'],
    [r'\\zeta', u'\u03B6'],
    [r'\\~\{u}', u'\u0169'],
    [r'\\`\{E}', u'\u042D'],
    [r'\\~\{a}', u'\u00E3'],
    [r'\\c\{t}', u'\u0163'],
    [r'\\=\{o}', u'\u014D'],
    [r'\\v\{r}', u'\u0159'],
    [r'\\=\{A}', u'\u0100'],
    [r'\\\.\{c}', u'\u010B'],
    [r'\\r\{U}', u'\u016E'],
    [r'\\~\{U}', u'\u0168'],
    [r'\\k\{A}', u'\u0104'],
    [r'\\"\{a}', u'\u00E4'],
    [r'\\u\{U}', u'\u040E'],
    [r'\\iota', u'\u03B9'],
    [r'\\=\{O}', u'\u014C'],
    [r'\\c\{C}', u'\u00C7'],
    [r'\\gneq', u'\u2269'],
    [r'\\\'\{c}', u'\u0107'],
    [r'\\boxH', u'\u2550'],
    [r'\\hbar', u'\u210F'],
    [r'\\"\{A}', u'\u00C4'],
    [r'\\boxv', u'\u2502'],
    [r'\\boxh', u'\u2500'],
    [r'\\male', u'\u2642'],
    [r'\\\'\{u}', u'\u00FA'],
    [r'\\succ', u'\u227B'],
    [r'\\\^\{Y}', u'\u0176'],
    [r'\\\^\{g}', u'\u011D'],
    [r'\\c\{c}', u'\u00E7'],
    [r'\\\'\{C}', u'\u0106'],
    [r'\\\^\{C}', u'\u0108'],
    [r'\\v\{l}', u'\u013E'],
    [r'\\u\{a}', u'\u0103'],
    [r'\\v\{Z}', u'\u017D'],
    [r'\\\'\{o}', u'\u00F3'],
    [r'\\c\{G}', u'\u0122'],
    [r'\\\^\{G}', u'\u011C'],
    [r'\\v\{C}', u'\u010C'],
    [r'\\lneq', u'\u2268'],
    [r'\\"\{E}', u'\u0401'],
    [r'\\=\{a}', u'\u0101'],
    [r'\\\^\{y}', u'\u0177'],
    [r'\\\^\{U}', u'\u00DB'],
    [r'\\c\{l}', u'\u013C'],
    [r'\\\^\{c}', u'\u0109'],
    [r'\\\'\{a}', u'\u00E1'],
    [r'\\=\{E}', u'\u0112'],
    [r'\\boxV', u'\u2551'],
    [r'\\u\{g}', u'\u011F'],
    [r'\\\'\{O}', u'\u00D3'],
    [r'\\\'\{g}', u'\u01F5'],
    [r'\\u\{I}', u'\u0419'],
    [r'\\c\{L}', u'\u013B'],
    [r'\\k\{E}', u'\u0118'],
    [r'\\\.\{I}', u'\u0130'],
    [r'\\~\{I}', u'\u0128'],
    [r'\\quad', u'\u2003'],
    [r'\\c\{r}', u'\u0157'],
    [r'\\\'\{r}', u'\u0155'],
    [r'\\"\{Y}', u'\u0178'],
    [r'\\=\{e}', u'\u0113'],
    [r'\\\'\{U}', u'\u00DA'],
    [r'\\leq', u'\u2264'],
    [r'\\Cup', u'\u22D3'],
    [r'\\Psi', u'\u03A8'],
    [r'\\dzh', u'\u045F'],
    [r'\\H\{}', u'\u02DD'],
    [r'\\k\{}', u'\u02DB'],
    [r'\\=\{}', u'\u203E'],
    [r'\\cup', u'\u222A'],
    [r'\\geq', u'\u2265'],
    [r'\\mho', u'\u2127'],
    [r'\\Dzh', u'\u040F'],
    [r'\\cap', u'\u2229'],
    [r'\\bot', u'\u22A5'],
    [r'\\psi', u'\u03C8'],
    [r'\\chi', u'\u03C7'],
    [r'\\c\{}', u'\u00B8'],
    [r'\\Phi', u'\u03A6'],
    [r'\\ast', u'\u002A'],
    [r'\\ell', u'\u2113'],
    [r'\\top', u'\u22A4'],
    [r'\\lll', u'\u22D8'],
    [r'\\tau', u'\u03C4'],
    [r'\\Cap', u'\u22D2'],
    [r'\\sad', u'\u2639'],
    [r'\\iff', u'\u21D4'],
    [r'\\eta', u'\u03B7'],
    [r'\\eth', u'\u00F0'],
    [r'\\d\{}', u'\u0323'],
    [r'\\rho', u'\u03C1'],
    [r'\\div', u'\u00F7'],
    [r'\\phi', u'\u03C6'],
    [r'\\Rsh', u'\u21B1'],
    [r'\\vee', u'\u2228'],
    [r'\\b\{}', u'\u02CD'],
    [r'\\t\{}', u'\u0361'],
    [r'\\int', u'\u222B'],
    [r'\\sim', u'\u223C'],
    [r'\\r\{}', u'\u02DA'],
    [r'\\Lsh', u'\u21B0'],
    [r'\\yen', u'\u00A5'],
    [r'\\ggg', u'\u22D9'],
    [r'\\mid', u'\u2223'],
    [r'\\sum', u'\u2211'],
    [r'\\Dz', u'\u0405'],
    [r'\\Re', u'\u211C'],
    [r'\\oe', u'\u0153'],
    [r'\\DH', u'\u00D0'],
    [r'\\ll', u'\u226A'],
    [r'\\=e', u'\u0454'],
    [r'\\ng', u'\u014B'],
    [r'\\\'G', u'\u0403'],
    [r'\\wr', u'\u2240'],
    [r'\\wp', u'\u2118'],
    [r'\\=I', u'\u0406'],
    [r'\\:\)', u'\u263A'],
    [r'\\:\(', u'\u2639'],
    [r'\\AE', u'\u00C6'],
    [r'\\AA', u'\u00C5'],
    [r'\\ss', u'\u00DF'],
    [r'\\dz', u'\u0455'],
    [r'\\ae', u'\u00E6'],
    [r'\\aa', u'\u00E5'],
    [r'\\th', u'\u00FE'],
    [r'\\to', u'\u2192'],
    [r'\\Pi', u'\u03A0'],
    [r'\\mp', u'\u2213'],
    [r'\\Im', u'\u2111'],
    [r'\\pm', u'\u00B1'],
    [r'\\pi', u'\u03C0'],
    [r'\\"I', u'\u0407'],
    [r'\\\'C', u'\u040B'],
    [r'\\in', u'\u2208'],
    [r'\\\'k', u'\u045C'],
    [r'\\\'c', u'\u045B'],
    [r'\\\'g', u'\u0453'],
    [r'\\ni', u'\u220B'],
    [r'\\TH', u'\u00DE'],
    [r'\\Xi', u'\u039E'],
    [r'\\nu', u'\u03BD'],
    [r'\\NG', u'\u014A'],
    [r'\\:G', u'\u32E1'],
    [r'\\xi', u'\u03BE'],
    [r'\\\'K', u'\u040C'],
    [r'\\OE', u'\u0152'],
    [r'\\gg', u'\u226B'],
    [r'\\DJ', u'\u0110'],
    [r'\\=E', u'\u0404'],
    [r'\\mu', u'\u03BC'],
    [r'\\dj', u'\u0111'],
    [r'\^0', u'\u2070'],
    [r'_9', u'\u2089'],
    [r'_8', u'\u2088'],
    [r'_7', u'\u2087'],
    [r'_6', u'\u2086'],
    [r'_5', u'\u2085'],
    [r'_3', u'\u2083'],
    [r'_2', u'\u2082'],
    [r'_1', u'\u2081'],
    [r'_\+', u'\u208A'],
    [r'_\)', u'\u208E'],
    [r'_\(', u'\u208D'],
    [r'\^-', u'\u207B'],
    [r'\^9', u'\u2079'],
    [r'\^=', u'\u207C'],
    [r'\^1', u'\u00B9'],
    [r'\^2', u'\u00B2'],
    [r'\^3', u'\u00B3'],
    [r'\^4', u'\u2074'],
    [r'\^6', u'\u2076'],
    [r'\^7', u'\u2077'],
    [r'\^\(', u'\u207D'],
    [r'\^\)', u'\u207E'],
    [r'\^\*', u'\u002A'],
    [r'\^\+', u'\u207A'],
    [r'\^5', u'\u2075'],
    [r'_4', u'\u2084'],
    [r'_0', u'\u2080'],
    [r'\^8', u'\u2078'],
    [r'\\:', u'\u2004'],
    [r'\\;', u'\u2002'],
    [r'\\&', u'\u0026'],
    [r'\\\$', u'\u0024'],
    [r'\\%', u'\u0025'],
    [r'\\#', u'\u0023'],
    [r'\\,', u'\u2009'],
    [r'\\-', u'\u00AD'],
    [r'\\S', u'\u00A7'],
    [r'\\P', u'\u00B6'],
    [r'_=', u'\u208C'],
    [r'\\O', u'\u00D8'],
    [r'\\L', u'\u0141'],
    [r'\\}', u'\u007D'],
    [r'\\o', u'\u00F8'],
    [r'\\l', u'\u0142'],
    [r'\\h', u'\u210E'],
    [r'\\i', u'\u2139'],
    [r'_-', u'\u208B'],
    [r'\^i', u'\u2071'],
    [r'\^n', u'\u207F'],
]
combiningmarks = [
    [r'\\tilde', u'\u0303'],
    [r'\\grave', u'\u0300'],
    [r'\\dot', u'\u0307'],
    [r'\\acute', u'\u0301'],
    [r'\\doubleunderline', u'\u0333'],
    [r'\\ddot', u'\u0308'],
    [r'\\slash', u'\u0338'],
    [r'\\overline', u'\u0305'],
    [r'\\vec', u'\u20D7'],
    [r'\\hat', u'\u0302'],
    [r'\\breve', u'\u0306'],
    [r'\\underline', u'\u0332'],
    [r'\\strikethrough', u'\u0335'],
    [r'\\bar', u'\u0305'],
]


def replace(inp):
    result = []
    for f in inp:
        f = f.decode("utf-8")
        
        #f = re.sub(r"([^\\])([_|\^])", r"\1\\\2", f) # do not require backslash in front of ^ or _
        #f = re.sub(r"^([_|\^])", r"\\\1", f)
    
        # expand groups of subscripts: \_{01234}    
        offset = 0
        #for s in re.finditer(r"\\_\{[^\}]+\}", f):
        for s in re.finditer(r"_\{[0-9\+-=\(\)]+\}", f):
            newstring,n = re.subn(r"([0-9\+-=\(\)])", r"_\1", s.group(0)[2:-1])
            f = f[:s.start()+offset] + newstring + f[s.end()+offset:]
            offset += n*2 - (n + 3)
            
        # expand groups of superscripts: \^{01234}    
        offset = 0
        #for s in re.finditer(r"\\\^\{[^\}]+\}", f):
        for s in re.finditer(r"\^\{[0-9\+-=\(\)ni]+\}", f):
            newstring,n = re.subn(r"([0-9\+-=\(\)ni])", r"^\1", s.group(0)[2:-1])
            f = f[:s.start()+offset] + newstring + f[s.end()+offset:]
            offset += n*2 - (n + 3)
            
        # escape combining marks with a space after the backslash
        for c in combiningmarks:
            offset = 0
            for s in re.finditer(c[0], f):
                f = f[:s.start()+1+offset] + " " + f[s.start()+1+offset:]
                offset += 1
            
        for r in replacements:
            f = re.sub(r[0], r[1], f)
            
        # combining marks (unicode char modifies previous char)
        for c in combiningmarks:
            offset = 0
            for s in re.finditer(r"\\ "+c[0][2:]+r"\{[^\}]+\}", f):
                newstring,n = re.subn(r"(.)", r"\1"+c[1], s.group(0)[len(c[0])+1:-1])
                f = f[:s.start()+offset] + newstring + f[s.end()+offset:]
                offset += n - (n + len(c[0])+1)

        result.append( unicode(f).encode("utf-8") )
        
    return result


if __name__ == "__main__":
    result = replace(sys.argv[1:])
    for r in result: print(r)
    
