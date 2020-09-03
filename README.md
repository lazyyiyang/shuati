# 备战秋招（2020-08-10)

知识点：
SQL、统计学、机器学习、python编程、业务分析、app了解、大数据


**已参加笔试**

字节游戏：游戏了解选择题、业务分析题

京东：专业知识选择题、算法编程（考察了最长公共子序列）

网易：业务分析题、sql编程（考察了group by、join、子查询）

美团：行测题

字节data：图形推理、数字推理、小学数学

神测数据：
1、从公司运营的角度为哔哩哔哩手机端设计三个关键数据指标；  
2、“日活数”、“月活数”、“留存率”含义的文字或公式表达；  
3、推算神策数据分析师校招参与人数，描述具体分析过程。  

滴滴：
sql:case when
偏差低方差大用什么算法，为什么
线性回归中随机误差假设
两类错误、卡方检验、t检验、f检验、w符号秩和检验
大数据情况，knn如何选择k
l1如何降维

众安保险：
**gbdt和xgb区别**
机器学习流程
**sql：case when**

爱奇艺机器学习：  
判别模型、生成模型；  
tf损失函数、交叉熵损失函数；  
python中iterable,iterator,generator关系；  
高斯朴素贝叶斯参数个数；  
bert、xlnet，gan；  
crf、memm；  
互信息；  
牛顿法；  

腾讯：  
快速幂取模！！！！   
遇到组合数！！别急着硬算！！！注意化简！！！！  

garena：  
栈、bfs、dfs、二叉树、可逆矩阵特征

小红书：
置信区间、假设检验、效能、box-cox、sql（行转列，json extract ）、ABtest

达达：  
sql（计算时间差，例如近七日数据、实现crosstab、索引、主键）、估计达达上海配送员工数量、影响履约（安全准时送达）的因素

58（偏产品）：
cps、cpc、cpa；dau、sem、seo；hybrid app、native app；  
举办活动，从几方面对活动效果评估；


---
## 复习资源：
游戏分析：

https://gameinstitute.qq.com/course/detail/10141

https://gameinstitute.qq.com/course/detail/10220

机器学习：

gbdt、xgb、lgb、cat面经整理——from牛客 - 马东什么的文章 - 知乎
https://zhuanlan.zhihu.com/p/82521899

AUC计算：  
https://blog.csdn.net/qq_22238533/article/details/78666436

决策树：https://www.jianshu.com/p/fb97b21aeb1d

说明关系型数据库通过索引提升查询效率的背后原理:
1. 如果没有索引，数据库引擎需要通过全表扫描来查找数据，这会产生大量的磁盘IO。

2. 关系型数据库使用B+树构建索引来加速加快查询。B+树是一种二叉查找树（每个节点的键值必须：比保存在左子树的任何键值都要大，比保存在右子树的任何键值都要小），这样随机查找某个键值时可以通过从根节点执行二叉查找来加速查询，查询成本取决于树的层数。

3. 针对范围查询和排序的优化：在每个叶子节点保存其下一个叶子节点的指针，这样当指定范围范围查询时，先从根节点根据范围的左值找到其叶子节点，之后通过向后遍历叶子节点即可找到对应范围右值，这样可以加速范围查询、排序、分组等数据库查询动作。

4. 针对磁盘读写速度的优化：除了叶子节点之外的其他节点只保存键值，这样对磁盘的单次读写可以获取到尽可能多的数据。以MySQL为例，一个1000万行的表对应的B+树按照主键查找理论上只需要3次磁盘IO，这相对于全表扫描带来的磁盘IO是多个量级的性能提升。

5. MySQL等数据库引擎在实际实现B+树索引的时候，针对磁盘读写做了优化：非叶子节点中只存放key值，叶子节点中除了key值也会存放数据，按照存放数据的不同索引区分为主索引（聚簇索引）和辅助索引：

   a) 主索引的叶子节点中存放该key值对应的完整记录，使用主索引进行查找时，可以直接输出记录；一个表只能创建一个主索引。

   b) 普通索引的叶子节点则存放对应主键的值，因此在使用辅助索引进行查找时，需要先查找到主键值，然后再到主索引中进行查找；一个表可以创建多个辅助索引。

6. 除了B+树，关系型数据库一般也支持哈希索引，哈希索引能够非常高效地进行随机查找，但是对于范围查询、排序和分组都不支持。


权限数字含义：
754对应3种用户的权限：文件所有者、同组用户、其他用户  
权限,    权限数值,       具体作用  
r,             4,               read，读取。当前用户可以读取文件内容，当前用户可以浏览目录。  
w,           2,              write，写入。当前用户可以新增或修改文件内容，当前用户可以删除、移动目录或目录内文件。  
x ,          1,              execute，执行。当前用户可以执行文件，当前用户可以进入目录。  


sem&seo知识：SEM和SEO有什么区别呢？ - 余杰的回答 - 知乎
https://www.zhihu.com/question/20307058/answer/1296919533

CPA、CPS、CPM、CPT、CPC 是什么
 https://www.a-edm.com/cpa.html



hivesql 行转列（collect_set）与列转行(explode和posexplode)

https://blog.csdn.net/zhouqi1991i/article/details/91957007?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.channel_param
