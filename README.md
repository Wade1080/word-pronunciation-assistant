# 单词发音助手 (Word Pronunciation Assistant)

一个基于有道词典API的在线单词发音学习工具，提供英文单词发音、中文释义和例句等功能。

## 功能特点

- 🔊 英文单词发音（支持在线播放）
- 📚 中文释义显示
- 📝 英文例句及中文翻译
- 📋 最近查询历史记录
- ⭐ 生词本功能（本地保存）
- 💻 响应式界面设计
- 🚀 快速音频加载和缓存

## 技术栈

- 后端：Python Flask
- 前端：HTML + JavaScript
- UI框架：Tailwind CSS
- API：有道词典API

## 安装说明

1. 克隆项目到本地：
```bash
git clone https://github.com/你的用户名/word-pronunciation-assistant.git
cd word-pronunciation-assistant
```

2. 安装依赖：
```bash
pip install flask requests
```

## 使用说明

1. 启动服务器：
```bash
python pronounce_api.py
```

2. 打开浏览器访问：
```
http://localhost:5000
```

## 主要功能使用指南

### 查询单词
1. 在搜索框中输入要查询的英文单词
2. 点击"获取发音"按钮或按回车键
3. 系统会自动播放单词发音，并显示中文释义和例句

### 生词本功能
- 点击单词卡片右上角的书签图标可将单词添加到生词本
- 在"单词本"标签页中可查看所有收藏的单词
- 可随时播放生词本中单词的发音
- 点击删除图标可将单词从生词本中移除

### 历史记录
- 系统自动记录最近查询的10个单词
- 在"最近查询"标签页中可查看历史记录
- 点击历史记录中的单词可快速重新查询
- 点击播放图标可直接播放该单词的发音

## 注意事项

- 本项目仅供学习和个人使用
- 需要保持网络连接以访问有道词典API
- 生词本数据保存在浏览器本地存储中
- 建议使用现代浏览器（Chrome、Firefox、Edge等）访问

## 许可证

MIT License

## 贡献指南

欢迎提交Issue和Pull Request来帮助改进这个项目！ 