"""Render portable static pages with only Python's standard library."""
import json, html, pathlib, shutil
ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT/'src/content.json').read_text())
OUT = ROOT/'dist'
OUT.mkdir(exist_ok=True)
shutil.copytree(ROOT/'src/assets', OUT/'assets', dirs_exist_ok=True)
def e(value): return html.escape(str(value), quote=True)
def link(path, label, cls=''): return f'<a class="{cls}" href="{{ROOT}}{path}">{label}</a>'
def cards(items, section):
    return '<div class="cards">'+''.join(f'<a class="card" href="{{ROOT}}{section}/{x["slug"]}/"><span class="eyebrow">{e(x.get("category", "专业领域"))}</span><h3>{e(x["title"])}</h3><p>{e(x["desc"])}</p><span class="more">了解详情 <span aria-hidden="true">↗</span></span></a>' for x in items)+'</div>'
def section(title, body, cls=''):
    return f'<section class="section {cls}"><div class="container"><h2>{title}</h2>{body}</div></section>'
def hero(title, desc):
    return f'<div class="breadcrumb container">{link("", "首页")} <span>/</span> {e(title)}</div><section class="subhero"><div class="container"><span class="eyebrow">MINGHENG · LAW FIRM</span><h1>{e(title)}</h1><p>{e(desc)}</p></div></section>'
def render(path, title, body):
    folder=OUT/path; folder.mkdir(parents=True,exist_ok=True)
    root='../'*len(pathlib.PurePosixPath(path).parts) if path else './'
    nav=''.join(link(p,l) for p,l in [('services/','核心业务'),('cases/','标杆案例'),('blog/','博客'),('team/','关于我们')])
    page=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)} · {e(DATA['brand'])}（演示）</title><meta name="description" content="律所网站复刻演示，内容均为示例。"><meta name="robots" content="noindex,nofollow"><link rel="icon" href="{{ROOT}}assets/favicon.svg"><link rel="stylesheet" href="{{ROOT}}assets/style.css"><script defer src="{{ROOT}}assets/app.js"></script></head><body id="top"><a class="skip" href="#main">跳转到正文</a><header><div class="container header-inner">{link('',e(DATA['brand']), 'brand')}<button class="menu-toggle" aria-label="展开导航" aria-expanded="false" aria-controls="navigation">☰</button><nav id="navigation" aria-label="主导航">{link('#trust','信任基础')}{nav}</nav>{link('contact/','联系我们','button header-cta')}</div></header><main id="main">{body}</main><footer><div class="container footer-grid"><div><h2>{e(DATA['brand'])}</h2><p>民商事争议解决 · 专业与信任同行</p><p class="muted">网站演示｜名称、人员、案例均为虚构占位</p></div><div><p>邮箱：hello@example.com（示例）</p><p>地址：示例市示例路 100 号（占位）</p>{link('contact/','查看咨询方式 →')}</div></div><div class="container footer-bottom"><span>© 2026 明衡 · 网站演示　不构成法律意见</span>{link('#top','返回顶部 ↑')}</div></footer><div class="mobile-bar">{link('services/','服务领域')}{link('contact/','咨询演示','button')}</div></body></html>'''
    (folder/'index.html').write_text(page.replace('{ROOT}',root))
trust='<div class="trust-grid"><article class="panel"><span class="eyebrow">从事实出发</span><h3>先了解问题，再讨论处理路径</h3><ol class="checks">'+''.join(f'<li><strong>{a}</strong><p>{b}</p></li>' for a,b in [('明确争议关系','厘清参与主体、合同约定与事情经过。'),('梳理证据材料','整理合同、转账、对账与沟通记录。'),('评估推进条件','结合材料完整度，明确待核实的问题。'),('说明后续流程','介绍处理阶段与沟通节点。')])+'</ol></article><aside class="panel navy"><span class="eyebrow">可核验 · 可沟通 · 可追踪</span><h3>把复杂问题<br>拆解成清晰步骤</h3><div class="stats"><div><b>01</b><span>事实与材料</span></div><div><b>02</b><span>方案与路径</span></div><div><b>03</b><span>推进与反馈</span></div></div><p>正式上线时，请在此补充可核验的执业信息和服务说明。</p></aside></div>'
features='<div class="features">'+''.join(f'<article><span class="number">0{i+1}</span><h3>{t}</h3><p>{d}</p></article>' for i,(t,d) in enumerate([('聚焦民商事争议','围绕个人与企业的实际问题，组织服务内容。'),('材料先行','以事实与材料为基础，减少沟通中的信息遗漏。'),('过程透明','明确每个阶段的事项、材料与沟通安排。'),('线上协同','按实际需要安排远程沟通与材料整理。')]))+'</div>'
process='<div class="steps">'+''.join(f'<div><b>0{i+1}</b><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([('初步沟通','确认问题与服务需求'),('材料梳理','整理时间线与文件'),('方案讨论','说明范围与推进路径'),('委托确认','明确服务内容和费用'),('持续跟进','同步关键进展与事项')]))+'</div>'
faq='<div class="faq">'+''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in DATA['faq'])+'</div>'
cta='<div class="consult-banner"><div><span class="eyebrow">LET’S TALK</span><h2>先把问题讲清楚。</h2><p>从一次有准备的沟通开始。</p></div>'+link('contact/','了解咨询方式 →','button light')+'</div>'
home=f'<section class="hero"><div class="container"><span class="eyebrow">民商事法律服务 · 示例网站</span><h1>民商事经济纠纷<br>法律服务｜让每一步<br>维权，都有证据和路径</h1><p>{e(DATA["intro"])}</p><div class="actions">{link("contact/#consult-form","评估处理路径","button")}{link("services/","了解服务领域","button light")}</div></div></section><section id="trust" class="section"><div class="container"><span class="eyebrow">信任基础 · 民商事经济纠纷</span><h2>信任，建立在清晰的信息<br>与透明的服务流程上</h2>{trust}{features}</div></section>'
home+=section('服务流程',process,'soft')+section('常见问题',faq)+section('',cta)
render('', '民商事法律服务', home)
services=hero('民商事经济纠纷法律服务','从个人债务到企业合同，围绕具体问题组织材料与处理思路。')
for group,title in [('personal','个人债务与权益纠纷'),('business','企业合同与债务纠纷')]:
    services+=section(title,cards([x for x in DATA['services'] if x['group']==group],'services'))
render('services','核心业务',services)
for s in DATA['services']:
    render('services/'+s['slug'],s['title'],hero(s['title'],s['desc'])+section('服务内容（示例）','<div class="article"><p>本页面展示业务详情页的内容结构，正式使用时请由专业人员补充。</p><h3>常见咨询场景</h3><p>'+e(s['desc'])+'</p><h3>建议准备的材料</h3><ul><li>事情经过与关键时间节点</li><li>合同、协议及相关文件</li><li>付款凭证、往来记录与相关附件</li></ul><h3>沟通与推进</h3><p>先核实材料，再讨论服务范围和后续安排。具体处理方式需要结合实际情况判断。</p></div>')+section('服务流程',process,'soft')+section('',cta))
for key,title in [('cases','标杆案例'),('posts','博客')]:
    route='blog' if key=='posts' else 'cases'
    render(route,title,hero(title,'以下内容均为虚构演示，用于展示信息结构，不代表真实案件或实际业绩。')+section('实务观察' if key=='posts' else '案例示例',cards(DATA[key],route)))
    for item in DATA[key]:
        render(route+'/'+item['slug'],item['title'],hero(item['title'],item['category']+' · 示例内容')+section('',f'<article class="article"><p class="notice">演示内容，不代表真实案件、处理结果或法律意见。</p><p>{e(item["desc"])}</p><h2>背景与问题</h2><p>这是一个用于说明网站内容组织方式的简化样例。正式发布时，应补充经过核实的事实，并妥善处理相关信息。</p><h2>梳理思路</h2><ol><li>按照时间顺序整理关键事件。</li><li>将文件与事件逐一对应。</li><li>列出缺失材料和待确认问题。</li></ol><h2>示例总结</h2><p>清晰的信息结构有助于理解复杂事项。本样例不包含实际裁判结果。</p>{link(route+"/","← 返回列表")}</article>'))
render('team','关于我们',hero('专业协作，认真对待每一次托付','以清晰、审慎、透明的方式，为个人和企业提供服务。')+section('关于明衡','<div class="article"><p>明衡律师事务所为本演示的虚构名称。这里可替换为真实机构简介、执业信息和团队介绍。</p></div>')+section('团队介绍（虚构示例）','<div class="cards">'+''.join(f'<article class="card"><div class="avatar" aria-hidden="true">{n[0]}</div><h3>{n}</h3><p>{r} · 示例人物</p><p>关注合同争议、材料分析与客户沟通。</p></article>' for n,r in [('张律师','合伙人'),('李律师','专职律师'),('陈助理','服务协调')])+'</div>')+section('',cta))
form='''<div class="contact-grid"><div><span class="eyebrow">CONTACT US</span><h2>从清楚描述问题开始</h2><p>填写右侧信息，体验咨询表单流程。</p><p class="notice">这是演示表单：不发送、不保存您的输入。请勿填写真实案件或敏感信息。</p><p>联系邮箱：hello@example.com（示例）</p><p>办公地址：示例市示例路 100 号（占位）</p></div><form id="consult-form"><h2>咨询演示</h2><label for="name">称呼</label><input id="name" name="name" required maxlength="40" placeholder="例如：王先生（使用化名）"><label for="phone">手机号码（演示）</label><input id="phone" name="phone" type="tel" inputmode="numeric" pattern="1[0-9]{10}" required placeholder="例如：13800000000" aria-describedby="phone-help"><small id="phone-help">11 位数字，仅用于体验格式校验</small><label for="topic">咨询类型</label><select id="topic" name="topic"><option>债务追讨</option><option>合同纠纷</option><option>劳动与劳务</option><option>其他事项</option></select><label for="message">简要说明</label><textarea id="message" name="message" rows="4" maxlength="1000" required placeholder="请输入虚构的示例描述"></textarea><label class="checkbox"><input type="checkbox" required>我已了解这是演示，不会发送咨询请求</label><button class="button" type="submit">体验提交</button><p id="form-result" role="status" tabindex="-1"></p></form></div>'''
render('contact','联系我们',hero('联系我们','先整理材料，再开始一次高效的沟通。')+section('',form))
render('404','页面未找到',hero('页面未找到','你访问的页面不存在。')+section('',link('','返回首页','button')))
shutil.copyfile(OUT/'404/index.html',OUT/'404.html')
# The standalone 404 is at the root, so its assets should also be root-relative.
p=OUT/'404.html'; p.write_text(p.read_text().replace('../','./'))
print('Built',len(list(OUT.rglob('*.html'))),'HTML files')
