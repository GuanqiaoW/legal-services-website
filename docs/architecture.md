# 源代码与结构说明

## 实现方式

这是一个零前端依赖的多页面静态网站。Python 标准库读取 JSON，复用 header、footer、hero、section、cards 等模板函数，生成可直接访问的 HTML。浏览器只需要 CSS 和少量 JavaScript，不依赖构建服务器、数据库或框架运行时。

数据流：`src/content.json` → `scripts/build.py` → `dist/**/index.html`；`src/assets/` → `dist/assets/`。

## 代码职责

| 文件或函数 | 职责 | 修改场景 |
|---|---|---|
| content.json | 业务/文章/案例/FAQ 数据 | 替换示例文案、增加内容 |
| render() | HTML 文档、共享头尾、相对路径 | 修改导航、页脚、SEO 元信息 |
| hero() / section() | 页面标题与内容段落 | 调整页内布局 |
| cards() | 列表与详情链接 | 改案例、文章或服务卡片 |
| build.py 首页组合部分 | 首屏、信任基础、服务流程 | 调整营销展示逻辑 |
| style.css :root | 色彩 token | 修改主色/强调色 |
| style.css @media | 950px 与 680px 断点 | 平板和手机布局 |
| app.js | 菜单和演示表单事件 | 对接实际交互 |

源数据文本输出经过 HTML 转义。模板含固定可信 HTML；不应将未经处理的用户 HTML 直接拼接进模板。JSON 中 slug 属于开发者控制的路径，新增时使用不含斜线的英文标识。

## 参考站与本版本

保留：白色导航、金色机构名、灰蓝首页首屏、深蓝内页首屏、信任与流程模块、折叠 FAQ、多页面业务/案例/博客层级、联系入口。

简化：顶栏业务下拉改为业务列表页；首页大标题与排版做响应式调整；团队照片改为文字头像；文章和案例为短样例；真实资质、业绩数字、电话与备案号不复制。内容管理使用 JSON，没有 CMS 管理后台。不是对原站技术栈的鉴定或其服务器源代码备份。

## 页面与资源部署

所有链接均按页面深度生成相对路径，便于 GitHub Pages 子目录、普通静态托管及本地查看。`dist/404.html` 用于常见静态托管的 404 配置；不同平台可能需要单独配置错误页。未自动发布 GitHub Pages。

## 接入真实咨询的边界

当前 submit 只 preventDefault、展示状态和 reset，不进行 fetch，也不使用浏览器存储。接入业务时应增加服务端 API、服务端校验、频率限制、访问权限与保存期限；只有服务端确认成功后才显示收到咨询。邮件/CRM 密钥必须保留在服务端，不能写进静态文件。

正式上线还需添加每页独立描述、真实域名 canonical、sitemap 与合适的 robots 配置；使用可核验内容替换占位文案后再移除 noindex。当前演示没有虚构的法律机构结构化数据或用户评价。

## 验证方法

`python3 scripts/build.py` 生成全部 HTML；`node --check src/assets/app.js` 检查 JS 语法。可使用 Python HTMLParser 检查本地链接目标；浏览器重点验证首页、业务详情、FAQ 和表单的实际状态。
