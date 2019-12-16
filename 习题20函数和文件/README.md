![ex20.png](ex20.png)
### 为什么seek(0)没有把 current_line 设为0
> 首先 seek() 函数处理的对象是<b>字节</b>不是<b>行</b>
> currnet_line 知识一个独立变量,和文件本身没有任何关系,<b>只能</b>手动为期增值

### readlind() 怎么知道每一行结束
/n