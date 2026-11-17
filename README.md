# 律所展示网站复刻演示

参考 https://xrlaw.cn/ 的页面层级、深蓝/金色视觉、首屏、信任模块、流程与 FAQ 结构，自行实现。不是原站源码，也不是像素级完整复制；名称、文案、人物、案例均为虚构示例。不使用原站律师照片、真实联系方式、资质、备案号或业绩数字。

## 本地运行

要求 Python 3.9+。无第三方依赖。

```bash
git clone https://github.com/GuanqiaoW/legal-services-website.git
cd legal-services-website
python3 scripts/build.py
python3 -m http.server 8080 --directory dist
```

浏览器打开 http://localhost:8080 。如果当前已经在项目根目录，省略第一条命令。也可直接打开 `dist/index.html`；所有资源使用相对链接。

## 修改内容

- `src/content.json`：机构名称、业务、案例、文章和 FAQ。
- `scripts/build.py`：页面模板、共享导航/页脚、首页模块、联系表单。
- `src/assets/style.css`：颜色变量、布局、移动端断点与可访问性样式。
- `src/assets/app.js`：移动导航、Escape 关闭、表单演示。
- `src/assets/favicon.svg`：本项目原创矢量图标。
- `dist/`：生成后的完整静态站点，可直接部署。
- `docs/architecture.md`：结构说明、扩展方式、与参考站差异。

修改后重新运行 `python3 scripts/build.py`。生成文件会被覆盖，不建议直接修改 dist。

## 页面

首页 `/`；业务 `/services/` 及 6 个详情；案例 `/cases/` 及 3 个详情；博客 `/blog/` 及 3 个详情；关于 `/team/`；联系 `/contact/`；404 页面。

## 已实现

响应式布局、移动端菜单、原生 FAQ 折叠、站内导航、独立详情页、键盘焦点、跳转正文链接、标题/描述、表单必填与手机号格式校验。

**表单仅演示：不发送、不存储，也没有邮件通知或 CRM。** 提交后明确显示这一状态，并清空输入。没有真实电话按钮，避免打给无关人员。所有页面设置 noindex，避免示例内容进入搜索索引。

## 部署

任何静态托管均可部署 `dist/`，例如 GitHub Pages、Nginx 或静态对象存储。目录首页使用 index.html。GitHub Pages 应选择 dist 的内容作为发布根目录；本项目没有自动启用 Pages，也不会修改现有网站部署。

实际上线需替换真实内容、联系方式与经过核实的执业信息；接入安全的表单 API，再开启搜索索引。详见结构说明。

## 仓库迁移

本项目从 `GuanqiaoW/personal_web` 的 `feat/law-firm-demo-20261117` 分支提取到此独立仓库根目录。原分支保留备份。此仓库仅包含律所网站，不包含个人网站文件或其提交历史。
