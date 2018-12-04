原文链接在这里：<a href="http://finalobject.cn/lucario/battleheart">finalobject.cn</a>

这个是我突发奇想然后在603做了几个晚上做出来的东西，然后后来做不动了就没有做下去。只实现了人物的移动、攻击动画和血条。游戏素材来源于battleheart，超级喜欢的一个游戏。

很久以前做的，一直没有整理，这次忽然想整理了，是因为我有点想认真的做点游戏，所以想把之前的东西整理整理就可以藏起来了，从头来过。毕竟之前用的是python下的pygame当作游戏引擎，感觉底层工作有点太多了，基础的开发工作量太大，也不方便后续的继续开发。目前物色了一个比较理想的引擎，叫做cocos2d。
<!--more-->
环境需要python2和pygame，然后用到的代码就是src/main.py和src/gameEngine.py，然后其他的几个py文件是比较独立的小程序，感兴趣自己看看。

<img class="wp-image-265 aligncenter" src="http://finalobject.cn/wp-content/uploads/2018/12/battleheart-2-300x204.jpg" alt="" width="418" height="284" />

下面可能会有几个词，没有做过游戏的可能会有点陌生。scene，这个词其实比较好理解，就是场景嘛，用来搭载游戏场景的抽象的对象。sprite，这个词可以理解成，游戏中的一个个小单元，他们一个个相对的比较独立，比如英雄、小兵等等。
<h3>工具库</h3>
下面两个是代码里用到的python库，在游戏制作里这种库有一个很厉害的名字，叫做游戏引擎。
<h4>pygame</h4>
python底下一个比较常用的游戏库，没有认真学习过，所以不能做太多评价。
感觉只是定义了游戏里的一些常用的scene、spirte这些东西，更多的判定啊啥的都需要自己实现，比如物理引擎什么的。
更多地感觉他像是一个用来做游戏引擎的一个引擎。。
<h4>gameEngine.py</h4>
这个是Andy Harris在2006做的简单的、基于pygame弄出来一个具体了很多的小引擎（我忘记我是从哪里下到的了，貌似是一本书上有介绍？），包含功能（自己总结的）如下
<ul>
    <li>scene对于自己的sprites进行统一的检查、控制、显示</li>
    <li>sprite中加入了速度、角速度、位移这部分的物理引擎</li>
    <li>sprite中加入了与边界的碰撞检测</li>
    <li>还实现了button、label、scroller、multiLabel这几个具体的小精灵</li>
</ul>
<h3>游戏素材</h3>
游戏素材来源于一个我超级喜欢的手机上的游戏，叫做battleheart！有时间一定要在<a href="http://finalobject.cn/category/mew">Mew</a>里更新一波这个游戏。感觉这个游戏的画风超棒的

<img class="size-medium wp-image-264 aligncenter" src="http://finalobject.cn/wp-content/uploads/2018/12/battleheart-1-300x169.jpeg" alt="" width="300" height="169" />
然后获取素材的方式相当原始，就是自己通过录屏获取游戏视频，然后截下一个关键动作然后扣掉背景。。总是非常原始和机械，同时的关键帧可能选取的太少了，或者时间间隔不够均匀，导致人物移动和攻击的时候有点生硬（非常生硬），下图是我扣出来的素材。

<img class="alignnone size-medium wp-image-266 aligncenter" src="http://finalobject.cn/wp-content/uploads/2018/12/battleheart-3-300x219.jpg" alt="" width="300" height="219" />
<h3>代码细节</h3>
代码。。。我看了一下觉得自己写的很糟糕，反正实现的功能就只有移动、攻击、还有血条变化，没有啥讲的，有兴趣自己扒代码吧。
觉得稍微有意思的地方，就是我觉得血条画的特别好看，还设计了绿血黄血和红血的模式。然后人物比较傻，平A一下自己会掉血。