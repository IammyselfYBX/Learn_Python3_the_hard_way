class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):    # 需要写Child(Parent),()中表示需要继承的分类是什么

    def altered(self):
        print("Child, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()