
class Foo:


    x1= 0;
    x2=0;

    def __init__(self, y1, y2):

        self.y1= y1
        self.y2=y2
        Foo.x2=y2;



class Test:

    def __init__(self):
        self.foo= Foo(2,4);

    def __init__(self, test):

        self.test= test;
        self.foo= test.foo;

    def output(self):
        print("foo.x1", self.foo.x1);
        print("foo.x2",self.foo.x2);
        print("foo.y1", self.foo.y1);
        print("foo.y2", self.foo.y2);

test= Test();
#test.output();

test2= Test(test);
test.output();