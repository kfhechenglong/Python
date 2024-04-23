var a = 5
const obj = {
  a:3,
  test1:function() {
    console.log(this.a)
  },
  test2:() => {
    console.log(this.a)
  },
  test3() {
    console.log(this.a)
  },
  test4() {
    return function () {
      console.log(this.a)
    }
  }
}

const obj2 = {
  a:2
}
obj.test1()
obj.test2()
obj.test3()
obj2.test1 = obj.test1
obj2.test2 = obj.test2
obj2.test3 = obj.test3
obj2.test4 = obj.test4()

obj2.test1()
obj2.test2()
obj2.test3()
obj2.test4()
obj.test1.apply(obj2)