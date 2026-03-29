# StudyBase

> AI 驱动的学习资料管理工具，帮助学生把分散的课程文件整理成结构清晰的课程空间。

---

## 项目简介

学生缺的不是资料，缺的是一个把资料整理好的地方。

StudyBase 帮助学生上传 syllabus、slides、论文等课程文件，自动提取关键信息（成绩比例、deadline、考试安排），并生成文档摘要——让"开始学习"这件事变得更容易。

---

## 核心功能

- 为每门课创建独立的课程空间，集中管理所有资料
- 上传多种格式的课程文件（PDF、PPT、Word）
- 从 syllabus 中自动提取 grading breakdown、deadline、考试信息与课程政策
- 对 slides 和论文生成结构化摘要
- 在课程 Dashboard 中统一展示所有关键信息

---

## 技术栈

| 层级 | 技术 |
|---|---|
| 前端 | Next.js · React · TypeScript |
| 后端 | FastAPI · Python |
| 数据库 | PostgreSQL |
| 云存储 | Supabase Storage / AWS S3 |

---

## 项目结构

```
studybase/
├── frontend/        # Web 界面（Next.js）
├── backend/         # API · 文档解析 · AI Pipeline（FastAPI）
└── docs/            # 产品文档 · 技术规划 · 会议记录
```

---

## 相关文档

- [产品介绍](./docs/product-intro.md)
- [MVP 文档](./docs/mvp.md)
- [系统架构](./docs/architecture.md)

---

## 当前状态

项目处于 **MVP 开发阶段**，核心目标是验证以下假设：

- 用户是否愿意将课程资料集中上传到一个平台
- AI 提取的关键信息是否准确、够用
- 课程空间是否真的帮助用户更快进入学习状态

---

*内部项目 · 持续迭代中*