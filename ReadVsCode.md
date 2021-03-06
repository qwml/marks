[TOC]







# 作业1：任正非新年致全体员工信

```
    全文各段首句都有总结，对于我个人而言，精简之后的内容，
         重点是：可靠性和可用性；
         方向是：基于可信导向来进行架构与设计；
         历史债务：重构腐化的架构及不符合软件工程规范和质量要求的历史代码；
     既然有了要求，那就得有实施的判断标准了，可信导向如何界定？
     现在我们需要做的内容：
         整理军规，代码严格执行（类似现在ci／cd，gitlab
         架构设计知识的积累以及能力提升
         了解各种业务的较优方案以及优缺点；如大日志监控，数据库的优化等
      Code wins argument
```
---
---
---
# 作业2：了解各项目的开发流程规范
```先vscode后gitlab``` 

**目的** 
``` 
     了解迭代周期以及规范性
            计划周期内的延期任务如何安排
            对于bugfix和新功能时间预估
            模块测试规范
            版本定义以及版本迭代的划分？bugfix推送规范？
            日志的处理，是否有接近完美的示例，有没有各种需求下的处理推荐方法？
            性能与可读性的权衡？如orm和原生sql
```
``` 
     了解code review的具体内容
            日常review着重检查逻辑以及性能
```

---

# vscode 
```
   原因：想了解微软的规范性以及文本编辑器的框架（如果有足够的时间 
```
## 关于开发周期

### roadmap
```
   vs以6-12个月为周期制定规划
```

### 迭代周期划分
```
   以自然月迭代，每个月有单独的plan和endgame
```

### 迭代周期内

```
      week1
            减少上一次迭代遗留的债务，解决上一周期遗留的关键性债务，计划下一周期
      week2
            按week1的计划
      week3
            按week1的计划
      final week
            按测试计划测试新功能等，并补充文档
            pre-release版本，邀请用户帮忙测试
      week1
            检查监控上一周期的pre-release，并解决遗留的关键性issue
            发布pre-release
```

### Triage(任务分配>里程碑)
```
     bug和feature都会被分配到milestone里程碑，带有优先级
          严重的bug会被安排在其他bug前面
     fixbug之后确认相关issue
```

### 周期(周)盘点
```
    每周整理迭代计划，关闭已完成的feature以及分配bug修复任务；
    结束里程碑的要求，必须0bug和0issue，部分bug和feature移动到下一个里程碑
```

### 周期完结
```
    最后一个里程碑被定义为endgame，打包feature，按测试计划测试并修复严重的bug
```


### master打包
```
     确认内部版本为最新
     确认持续生成为绿色（通过状态
     如果，生成失败，从build slack channel确认通知谁处理
     如果，编译失败，push一个修复的commit病通知开发者
     如果，测试失败，提交issue给开发者修复
```

### 关于endgame分支管理

```
    1、在endgame时期创建release-1.10
    2、打包上一步的分支并系统性的测试
    3、任何严重bug都应修复并推送到master以及release-1.10，并通过步骤2
    4、无严重bug即创建tag:release-1.10.0
    5、以tag:release-1.10.0打包并推送给用户
    6、任何修复打包都应该依赖于release-1.10，补丁版本定义为：1.10.1,1.10.2...
```

### Endgame一周的安排
```
      周一：保证持续生成绿色以及冻结代码
      周二：测试
      周三：测试和fix
      周四：fix和签名认证
      周五：暂停封存任务安排表，打包master，测试、修复，更新相关issue、评论等
```

## 代码组织
```
   The core is partitioned into the following layers:
   base: Provides general utilities and user interface building blocks
   platform: Defines service injection support and the base services for Code
   editor: The "Monaco" editor is available as a separate downloadable component
   languages: For historical reasons, not all languages are implemented as 
   				extensions (yet) - as Code evolves we will migrate more languages 
   				to towards extensions
   workbench: Hosts the "Monaco" editor and provides the framework for "viewlets" 
   				like the Explorer, Status Bar, or Menu Bar, leveraging Electron to
                implement the Code desktop application.
```

## 关于code review
```
https://github.com/microsoft/vscode/pulse
```
    https://github.com/microsoft/vscode/pull/82171#pullrequestreview-299623638
    https://github.com/microsoft/vscode/pull/82301
    实际上跟日常一样
    issue -- fix request review -- discuss -- merge
---
---
---

# gitlab：

**https://about.gitlab.com/direction/#dev **

![avatar](https://about.gitlab.com/direction/devops-loop-and-spans.png)



### 愿景
```
    希望以预配置通过devops流程，替换单个应用通过一系列不同的devops工具
    	更快的周期
    	更简单的工作流
```
## DevOps周期
```
    DevOps周期划分为dev和ops两个大阶段，细分之后可分为：plan、create、verify、package、release、configure、monitor
```
### Dev
```
    DevOps的dev周期包括manager、plan、create
```
#### Dev-manager
```
    该步骤是DevOps最开始的阶段，主要是完成软件的创建和开发上；开发阶段相对来说范围比较广，包括价值调研、项目管理、敏捷工具、IDEs、设计管理等；
```
##### Dev-开发分析
```
    SWOT分析以及挑战
        优点
        劣势
        机会
        威胁
        可视化的主题
        高效自动的code review
        价值衡量并提高效率
        项目管理转换成产品管理
        
    三年战略：三年内需要完成***
    一年计划：接下来的12个月将会曾为战略中不可以或缺的部分
```
#### Dev-Manage
```
    对于管理者而言，管理阶段是持续性的，需要管理人员、资金、风险等；
    当风险较高时，管理者把控项目应有经验，不应设置过于复杂的流程，并且管理者不应在安全性和规范性上妥协；
    管理者在gitlab中的角色是提供跨阶段性的帮助，协助分析更为便捷的配置；
```
#### Dev-plan
```
    看板
    从jira导入避免丢失数据
    加强项目组合以及项目路线图
    更方便的完整计划
    报告和分析
    需求管理
```
#### Dev-create
```
    增强code review体验
    在git操作大型文件
    投入精力到wiki
    更加便捷的提供共享到gitlab
    援助经验共享者
```

### CI/CD自动集成
```
    cicd概览

        代码构建/验证（验证）
        包装/分配（包装）
        软件交付（发布）
```

### Ops
```
    Ops阶段包括DevOps周期的configure和monitor监控阶段，通常描述该阶段为IT自动化、配置管理、运营管理
```
#### Ops-configure
```
    自动化配置应用、架构
```
#### Ops-monitor
```
    应用性能监控
    测试应用健康
```

### Ops-Secure
```
    集成安全功能完成开发周期
```

### Ops-defend
```
    收到安全入侵时保护应用、架构
```

---
---
---

# 面壁
```
    总体感觉:
        vs的wiki页面更偏向于短周期的迭代时间安排；更偏向规范
        gitlab的介绍更偏向于长时间的计划，罗列当前产品的优劣以及挑战点，完善项目；持续生成，更偏向便捷
        
        vscode的安排方式：
            以月为周期，周为节点，划分【计划(week1)、开发(week2 week3)、发布(final week)】
        gitlab的安排方式
            以12月为周期，以自然月划分【Dev、ci/cd、Ops】,致力于更快迭代更简洁自动化的流程
                dev阶段分析，包括项目价值、管理、开发
                ci/cd阶段主要是测试交付
                Ops是后续的监控内容
  	CCS项目的想法：
  		1、测试规范暂时不是很完整：部分功能未有足够测试就上线了；大部分是开发自测
  		2、由于是爬虫数据，缺少定期核查数据的安排；开发自查会遗漏检查，且比较耗时间
  		3、希望有个大而全的wiki页面，罗列了本周期应当修复bug和新feature，不做登陆方便查看
  		4、项目经理或产品整理上一周期遗留债务转移到下一期，并督促fix
  		5、vs偏向于时间的安排，gitlab偏向于流程的自动化上线；
```

```

** 理想 ** 是美好的，现实是骨感的，新需求时间不好预估

   1、关于jira，有两个想法
      没有一个大而全的页面，列出本周期需要fix的bug以及新功能完成状态的概览；
         按列表任务的方式过于详细，不利于大家了解全局的进展；特别是人数多了时间比较紧的项目；
         【按gitlab文档，可能未来会有类似的功能，见开发分析的plan部分】
      缺少了周期结束时的整理工作，未完成的工作顺利转移到未来的周期
         不需要全部人参与，全部人消耗过多时间，能把控项目进展的人完成就好，例如项目经理or产品
         产品有时比较忙，例如新模块的调研和原型，这时又有谁能顶上？


   2、ccs目前大部分代码都上了ci，书写较为规范，但一些经验经验积累问题：
         2.1 易读性与性能，如何做抉择？orm和原生sql(另：sqlalchemy是否有接口输出完整的原生sql)
         2.2 什么数据什么时候需要做检查？
         2.3 数据库连接需要注意什么？避免重复踩坑
            如非后端框架，数据计算为了性能协程多进程多线程都有用，哪些第三方包进程线程协程都安全？
         2.4 对于获取数据计算问题，如果本地机器内存无法支撑取回的数据如何处理？有没有一些好的建议
         	【spark可以自行缓存，不上这些大框架的处理方式】
         
         （由于vscode上面都是大佬的代码多， 想找一些建议性的review comment有难度）



```
 #最重要的部分：如何将规范性执行下去
​    


```

```
