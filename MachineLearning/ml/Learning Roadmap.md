# 大模型学习路线图

## 总览

```
阶段一：数学基础
    ↓
阶段二：编程与工程能力
    ↓
阶段三：机器学习基础
    ↓
阶段四：深度学习核心
    ↓
阶段五：NLP 与大模型专项
    ↓
阶段六：动手实践（从小模型到大模型）
    ↓
阶段七：分布式训练与工程实践
```

---

## 阶段一：数学基础

> 目标：理解模型背后的数学原理，能推导简单的公式。

### 1. 线性代数

- 向量与矩阵运算
- 特征值分解、SVD 分解
- 向量空间与线性变换
- 矩阵求导

**推荐资源：**
- 3Blue1Brown《线性代数的本质》（视频）
- 《Introduction to Linear Algebra》Gilbert Strang

### 2. 微积分

- 偏导数与全微分
- 链式法则（反向传播的核心）
- 梯度与方向导数
- 泰勒展开

**推荐资源：**
- 3Blue1Brown《微积分的本质》（视频）

### 3. 概率与统计

- 常见概率分布（高斯、伯努利、多项式）
- 贝叶斯定理
- 最大似然估计（MLE）
- 信息熵与交叉熵

### 4. 优化理论

- 凸函数与凸优化
- 梯度下降法（BGD / SGD / Mini-batch）
- 拉格朗日乘子法
- KKT 条件

---

## 阶段二：编程与工程能力

> 目标：熟练使用深度学习框架，具备 GPU 编程和 Linux 操作能力。

### 1. Python 基础

- NumPy / Pandas 数据处理
- Matplotlib 可视化
- 面向对象编程

### 2. 深度学习框架

- **PyTorch**（推荐优先学习）
  - Tensor 操作与自动求导（autograd）
  - nn.Module 构建模型
  - DataLoader 与数据集处理
  - 训练循环编写
- TensorFlow / Keras（了解即可）

### 3. GPU 与硬件基础

- CUDA 基本概念
- 显存管理（OOM 问题排查）
- 混合精度训练（FP16 / BF16）

### 4. Linux 环境

- 命令行基本操作
- Shell 脚本编写
- 集群任务提交（Slurm / PBS）
- conda / pip 环境管理

---

## 阶段三：机器学习基础

> 目标：掌握经典机器学习算法，理解监督/无监督/强化学习的核心思想。
>
> 参考笔记：[ML note.md](ML%20note.md)

### 核心内容

- 监督学习：线性回归、逻辑回归、决策树、SVM
- 无监督学习：K-Means、PCA
- 强化学习：基本概念（状态、动作、奖励、策略）
- 模型评估：过拟合/欠拟合、交叉验证、评估指标
- 正则化：L1 / L2 / Dropout

**推荐资源：**
- 吴恩达《Machine Learning》课程（Coursera）
- 《统计学习方法》李航

---

## 阶段四：深度学习核心

> 目标：深入理解神经网络原理，能独立搭建和训练模型。
>
> 参考笔记：[Deep Learning note.md](Deep%20Learning%20note.md)

### 1. 神经网络基础

- 前向传播与反向传播
- 激活函数选择（ReLU / Tanh / Sigmoid / Softmax）
- 损失函数设计（交叉熵 / MSE）
- 优化器演进（SGD → Momentum → Adam → AdamW）
- 正则化技术（Dropout / BatchNorm / LayerNorm）

### 2. Transformer 架构（重点）

- 自注意力机制（Self-Attention）
- 多头注意力（Multi-Head Attention）
- 位置编码（Positional Encoding）
- 残差连接与 LayerNorm
- Encoder-Decoder 结构

**必读论文：**
- *Attention Is All You Need*（Vaswani et al., 2017）

### 3. 常见架构

- **CNN**：卷积、池化、经典网络（ResNet、VGG）
- **RNN**：LSTM、GRU、双向 RNN
- **Transformer 变体**：BERT（双向编码）、GPT（自回归生成）、T5（Seq2Seq）

**推荐资源：**
- 吴恩达《Deep Learning Specialization》课程
- 《动手学深度学习》（d2l.ai）李沐
- 李沐《论文精读》系列视频

---

## 阶段五：NLP 与大模型专项

> 目标：理解大语言模型的核心技术与训练流程。

### 1. 分词（Tokenization）

- Byte-Pair Encoding（BPE）
- WordPiece
- SentencePiece
- Tokenizer 的训练与词表设计

### 2. 预训练任务

- **因果语言建模（Causal LM）**：GPT 系列，从左到右预测下一个 token
- **掩码语言建模（Masked LM）**：BERT，预测被遮盖的 token
- **Span Corruption**：T5，预测被遮盖的文本片段

### 3. 缩放定律（Scaling Laws）

- 模型参数量、数据量、计算量三者的幂律关系
- Chinchilla 最优训练比例
- Emergent Abilities（涌现能力）

**必读论文：**
- *Scaling Laws for Neural Language Models*（Kaplan et al., 2020）
- *Training Compute-Optimal Large Language Models*（Hoffmann et al., 2022）

### 4. 对齐技术（Alignment）

- **SFT（Supervised Fine-Tuning）**：监督微调，让模型学会遵循指令
- **RLHF（Reinforcement Learning from Human Feedback）**：
  - 训练奖励模型（Reward Model）
  - 用 PPO 算法优化策略模型
- **DPO（Direct Preference Optimization）**：跳过奖励模型，直接优化偏好

**必读论文：**
- *InstructGPT*（Ouyang et al., 2022）
- *Direct Preference Optimization*（Rafailov et al., 2023）

---

## 阶段六：动手实践

> 目标：从训练一个小模型开始，逐步积累经验。

### 入门：nanoGPT

- 项目地址：https://github.com/karpathy/nanoGPT
- 用小数据集训练一个小型 GPT 模型
- 理解完整的训练流程：数据准备 → 模型定义 → 训练循环 → 生成文本

### 进阶：微调开源模型

- 使用 HuggingFace Transformers 加载预训练模型
- 学习 LoRA / QLoRA 参数高效微调
- 在自己的数据集上进行 SFT

### 高级：从零预训练

- 数据收集与清洗
- 设计模型架构与超参数
- 编写完整的训练流程
- 评估与基准测试

---

## 阶段七：分布式训练与工程实践

> 目标：掌握大模型训练的工程技巧，能处理实际训练中的问题。

### 1. 分布式训练策略

| 策略 | 说明 | 适用场景 |
|------|------|----------|
| 数据并行（DP） | 每张 GPU 持有完整模型，数据分片 | 模型能放进单卡 |
| 分布式数据并行（DDP） | DP 的高效版本，梯度同步 | 模型能放进单卡 |
| ZeRO 优化 | 将优化器状态、梯度、参数分片 | 模型接近单卡极限 |
| 张量并行（TP） | 将单层内部计算拆分到多卡 | 单层太大无法放入单卡 |
| 流水线并行（PP） | 将不同层分配到不同 GPU | 模型太深无法放入单卡 |
| 3D 并行 | TP + PP + DP 组合 | 超大模型训练 |

### 2. 显存优化

- **FlashAttention**：高效注意力计算，减少显存占用
- **梯度检查点（Gradient Checkpointing）**：用计算换显存
- **Offload**：将优化器状态卸载到 CPU 内存
- **混合精度训练**：FP16 / BF16 减少显存和加速计算

### 3. 训练稳定性

- 学习率策略：Warmup + Cosine Decay
- 梯度裁剪（Gradient Clipping）：防止梯度爆炸
- Loss Spike 处理：跳过异常 batch 或降低学习率
- 权重衰减（Weight Decay）

### 4. 常用框架

- **DeepSpeed**：微软开源，ZeRO 系列优化
- **Megatron-LM**：NVIDIA 开源，张量并行 + 流水线并行
- **FSDP**：PyTorch 原生全分片数据并行
- **ColossalAI**：一体化大模型训练系统

### 5. 数据工程

- 数据清洗：去重、去噪、去除低质量文本
- 数据配比：不同领域数据的混合比例
- 课程学习（Curriculum Learning）：从简单到复杂安排训练数据

---

## 推荐资源汇总

| 类别 | 资源 | 说明 |
|------|------|------|
| 视频课程 | 吴恩达 ML / DL 课程 | 入门首选 |
| 视频课程 | 李沐《动手学深度学习》 | 理论 + 代码实践 |
| 书籍 | 《统计学习方法》李航 | 经典机器学习 |
| 书籍 | 《深度学习》花书 | 深度学习理论 |
| 论文 | *Attention Is All You Need* | Transformer 开山之作 |
| 实践项目 | nanoGPT | 从零训练小型 GPT |
| 实践项目 | HuggingFace Transformers | 微调开源模型 |
| 框架文档 | DeepSpeed 官方文档 | 分布式训练 |
