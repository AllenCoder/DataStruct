package main

type node struct {
	value interface{}
	prev  *node
}

type Stack struct {
	top    *node
	length int
}

func (this *Stack) Push(value interface{}) {
	n := &node{value: value, prev: this.top}
	this.top = n
	this.length++
}
func (this *Stack) Pop() interface{} {
	if this.length == 0 {
		return nil
	}
	n := this.top
	this.top = n.prev
	this.length--
	return n.value
}
func (this *Stack) Peek() interface{} {
	if this.length == 0 {
		return nil
	}
	return this.top.value
}

type MyQueue struct {
	value  interface{}
	input  Stack
	output Stack
}

/** Initialize your data structure here. */
func Constructor() MyQueue {
	return MyQueue{
		input:  Stack{},
		output: Stack{},
	}

}

/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int) {
	this.input.Push(x)
}

/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	if this.output.length > 0 {
		return this.output.Pop().(int)
	} else {
		for i := 0; i < this.input.length; i++ {
			this.output.Push(this.input.Pop())
		}
	}
	return this.output.Pop().(int)
}

/** Get the front element. */
func (this *MyQueue) Peek() int {
	if this.output.length > 0 {
		return this.output.Peek().(int)
	} else {
		for i := 0; i < this.input.length; i++ {
			this.output.Push(this.input.Pop())
		}
	}
	return this.output.Peek().(int)
}

/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
	return this.input.length == 0 && this.output.length == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
func main() {
	obj := Constructor()
	param_2 := obj.Pop();
	param_3 := obj.Peek();
	param_4 := obj.Empty();
}
