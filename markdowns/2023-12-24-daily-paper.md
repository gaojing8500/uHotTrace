### [3D Pose Estimation of Two Interacting Hands from a Monocular Event Camera](http://arxiv.org/abs/2312.14157)
* paper_author:Christen Millerdurai, Diogo Luvizon, Viktor Rudnev, André Jonas, Jiayi Wang, Christian Theobalt, Vladislav Golyanik
* update_time:2023-12-21
* repo_url:None
* interprete: 这篇文章介绍了一种从单目事件相机中估计两只交互手的三维姿态的方法。由于手部交互、遮挡、左右手歧义和快速运动等问题，从单目视频中进行三维手部跟踪是一个非常具有挑战性的问题。现有方法大多依赖RGB输入，在低光条件下存在严重限制，并且容易受到运动模糊的影响。与之相反，事件相机捕捉局部亮度变化而不是完整图像帧，并且不会受到上述效应的影响。然而，由于数据模态之间存在显著差异，现有基于图像的技术不能直接应用于事件数据。为了解决这些挑战，本文提出了第一个针对单目事件相机中两只快速移动和交互手进行三维跟踪的框架。我们采用一种新颖半监督特征注意力机制来解决左右手歧义，并引入交集损失来修复手碰撞问题。为促进该研究领域的进展，我们发布了一个新型合成大规模数据集Ev2Hands-S和一个包含真实事件流和地面真值3D注释信息的真实基准数据集Ev2Hands-R。我们的方法在三维重建精度方面优于现有方法，并且能够适应严重光照条件下的真实数据。
### [Virtual Pets: Animatable Animal Generation in 3D Scenes](http://arxiv.org/abs/2312.14154)
* paper_author:Yen-Chi Cheng, Chieh Hubert Lin, Chaoyang Wang, Yash Kant, Sergey Tulyakov, Alexander Schwing, Liangyan Gui, Hsin-Ying Lee
* update_time:2023-12-21
* repo_url:None
* interprete: 这篇文章介绍了一种名为"Virtual Pets"的新型流程，用于在3D环境中模拟真实且多样化的动物运动。为了克服与环境几何对齐的3D运动数据有限的问题，作者利用单目互联网视频提取可变形NeRF表示来表示前景，并使用静态NeRF表示来表示背景。通过开发重建策略，包括物种级共享模板学习和每个视频微调，作者利用重建数据训练条件化的3D运动模型，在3D背景下学习前景动物的轨迹和关节活动。通过使用猫视频进行全面定性和定量评估展示了该流程的有效性，并展示了在未见过猫和室内环境中产生时间连贯4D输出以丰富虚拟体验能力。

简而言之，这篇文章介绍了一种基于生成模型技术实现在虚拟场景中生成逼真、多样化动物运动效果的方法，并通过猫作为案例进行验证。
### [DriveLM: Driving with Graph Visual Question Answering](http://arxiv.org/abs/2312.14150)
* paper_author:Chonghao Sima, Katrin Renz, Kashyap Chitta, Li Chen, Hanxue Zhang, Chengen Xie, Ping Luo, Andreas Geiger, Hongyang Li
* update_time:2023-12-21
* repo_url:https://github.com/opendrivelab/drivelm
* interprete: 本文介绍了一种名为DriveLM的驾驶图形视觉问答系统。该系统利用大规模数据训练的视觉-语言模型（VLMs）来增强自动驾驶系统的泛化能力，并实现与人类用户的互动。通过建立图形问答任务，模拟人类在决策过程中进行多步推理的方式，从关键对象定位开始，估计对象之间的相互作用并采取行动。作者基于nuScenes和CARLA构建了DriveLM-Data数据集，并提出了一个基于VLMs的基准方法（DriveLM-Agent），可以同时进行图形问答和端到端自动驾驶。实验证明，图形问答提供了一种简单、有原则性的框架来推理关于行车场景问题，而DriveLM-Data则为这个任务提供了一个具有挑战性的基准测试集。与最先进的专门针对自动驾驶设计架构相比较，在零样本情况下评估未见过对象或传感器配置时，我们所提出方法带来显著优势。希望这项工作能够启发如何将VLMs应用于自主驾驶领域，并且所有代码、数据和模型都对公众开放以促进未来研究。
### [TagAlign: Improving Vision-Language Alignment with Multi-Tag Classification](http://arxiv.org/abs/2312.14149)
* paper_author:Qinying Liu, Kecheng Zheng, Wu Wei, Zhan Tong, Yu Liu, Wei Chen, Zilei Wang, Yujun Shen
* update_time:2023-12-21
* repo_url:None
* interprete: 这篇文章介绍了一种名为TagAlign的方法，用于改善视觉和语言之间的对齐。该方法通过多标签分类来解决现有方法中存在的粗略对齐问题。作者提出了一个简单有效的自动解析流程，从图像和文本描述中提取对象和属性，并将其作为监督信号与常用的图像-文本对比损失相结合。实验证明，该方法在广泛的语义分割数据集上相比其他方法平均提升了3.65%。此外，可视化结果表明属性监督可以帮助视觉-语言模型准确地定位指定属性的对象。
### [Quantum Algorithms for the Pathwise Lasso](http://arxiv.org/abs/2312.14141)
* paper_author:João F. Doriguello, Debbie Lim, Chi Seng Pun, Patrick Rebentrost, Tushar Vaidya
* update_time:2023-12-21
* repo_url:None
* interprete: 这篇文章介绍了一种基于量子算法的高维线性回归方法，该方法使用经典LARS（Least Angle Regression）路径算法和$\ell_1$-penalty。与现有的经典数值算法类似，我们的量子算法可以在惩罚项变化时提供完整的正则化路径，并且在特定条件下每次迭代速度是二次快。通过使用Dürr和Hoyer（arXiv'96）提出的简单量子最小查找子程序来获得每次迭代中的连接时间，可以实现对特征/预测器数量$d$进行二次加速。然后，通过使用Chen和de Wolf（ICALP'23）最近提出的近似量子最小查找子程序，在特征数量$d$和观测数量$n$上实现了二次加速。作为我们主要贡献之一，我们构建了一个基于量子幅度估计来近似计算连接时间以供近似量子最小查找搜索使用的量子酉矩阵。由于连接时间不再精确计算，所以无法确定结果是否是一个好解决方案。作为我们第二个主要贡献，通过逐渐版本KKT条件和对偶间隙证明LARS算法（因此也包括我们的量子算法）对错误具有鲁棒性。这意味着如果连接时间只是近似计算，它仍然会输出最小化Lasso成本函数的路径，但可能存在一些误差。最后，在由未知系数向量生成观测值的模型中，我们证明了未知系数向量与近似Lasso解之间的差异，并推广了关于经典统计学习理论分析中收敛速度的已知结果。

该研究涉及领域包括：量子物理、机器学习、优化和控制。
### [HeadCraft: Modeling High-Detail Shape Variations for Animated 3DMMs](http://arxiv.org/abs/2312.14140)
* paper_author:Artem Sevastopolsky, Philip-William Grassal, Simon Giebenhain, ShahRukh Athar, Luisa Verdoliva, Matthias Niessner
* update_time:2023-12-21
* repo_url:None
* interprete: 这篇文章介绍了一种用于动画3DMM（三维形状模型）的高细节形状变化建模方法。该方法通过两个阶段的训练，实现了对头部几何结构的控制和高保真度的保留。首先，将参数化头部模型与准确的3D头部扫描数据集进行配准，并将位移信息嵌入手工制作的UV布局中。然后，使用StyleGAN模型对位移信息进行泛化训练。通过分解参数化模型和高质量顶点位移，可以对模型进行语义上的动画和修改。该方法在无条件生成和拟合全景或局部观测方面取得了良好结果。

这篇文章提供了项目页面链接以及视频演示，并附带有23页、19个图表、2个表格等详细内容。

总之，本文介绍了一种用于动画3DMM建模中高精度形状变化建模的新方法，并展示了其在不同应用场景下取得的成果。
### [Revisiting Foreground and Background Separation in Weakly-supervised Temporal Action Localization: A Clustering-based Approach](http://arxiv.org/abs/2312.14138)
* paper_author:Qinying Liu, Zilei Wang, Shenghai Rong, Junjie Li, Yixin Zhang
* update_time:2023-12-21
* repo_url:https://github.com/qinying-liu/case
* interprete: 这篇文章介绍了一种基于聚类的弱监督时序动作定位方法，旨在通过视频级别的动作标签来定位视频中的动作实例。该方法通过对片段进行无监督聚类，探索片段之间的潜在结构，并进一步将聚类结果分类为前景或背景。作者还引入了自我标记机制来生成高质量伪标签，以提高前景和背景分离效果。实验结果表明，该方法在三个基准数据集上取得了良好性能，并且比之前的方法更轻量化。
### [Fast kernel half-space depth for data with non-convex supports](http://arxiv.org/abs/2312.14136)
* paper_author:Arturo Castellanos, Pavlo Mozharovskyi, Florence d'Alché-Buc, Hicham Janati
* update_time:2023-12-21
* repo_url:None
* interprete: 这篇文章介绍了一种用于具有非凸支持的数据的快速核半空间深度方法。数据深度是一种统计函数，将排序和分位数推广到多变量设置及其他领域，如描述性和可视化统计、异常检测、测试等。传统的半空间深度假设数据支持为凸集，并需要指数级的计算成本。为了处理分布的多模态性，作者在再生核希尔伯特空间(RKHS)中扩展了半空间深度，并证明所得到的深度直观且与可证明浓缩界限保持一致，从而允许进行同质性测试。所提出的方法可以使用流形梯度进行计算，比传统半空间深度快几个数量级。通过数值模拟以及实际数据上进行异常检测和同质性测试等应用验证了该方法的性能。

### [$\textit{V}^*$: Guided Visual Search as a Core Mechanism in Multimodal LLMs](http://arxiv.org/abs/2312.14135)
* paper_author:Penghao Wu, Saining Xie
* update_time:2023-12-21
* repo_url:https://github.com/penghao-wu/vstar
* interprete: 本文介绍了一种名为$\textit{V}^*$的多模态LLM（Language and Vision Model）中的引导式视觉搜索机制。该机制利用LLM中的世界知识进行高效的视觉查询，以增强多模态系统在处理高分辨率和视觉拥挤图像时对重要视觉细节的关注能力。作者进一步创建了一个专门评估MLLM在处理高分辨率图像和关注视觉细节能力方面的基准测试集$\textit{V}^*$Bench。研究结果强调了将视觉搜索能力纳入多模态系统中的必要性。
### [Diffusion Reward: Learning Rewards via Conditional Video Diffusion](http://arxiv.org/abs/2312.14134)
* paper_author:Tao Huang, Guangqi Jiang, Yanjie Ze, Huazhe Xu
* update_time:2023-12-21
* repo_url:None
* interprete: 这篇文章介绍了一种名为"Diffusion Reward"的新框架，通过条件视频扩散模型从专家视频中学习奖励，以解决复杂的视觉强化学习问题。作者发现，在专家轨迹的条件下，生成多样性较低。因此，Diffusion Reward通过负条件熵来鼓励对专家行为进行有益探索。实验证明该方法在10个机器人操作任务上表现出色，并且能够成功有效地解决未见过的任务，远超基准方法。
