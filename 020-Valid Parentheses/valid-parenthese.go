package main

import "log"

//import (
//	"github.com/golang-collections/collections/stack"
//	"log"
//)

type (
	Stack struct {
		top *node
		length int
	}
	node struct {
		value interface{}
		prev *node
	}
)
// Create a new stack
func New() *Stack {
	return &Stack{nil,0}
}
// Return the number of items in the stack
func (this *Stack) Len() int {
	return this.length
}
// View the top item on the stack
func (this *Stack) Peek() interface{} {
	if this.length == 0 {
		return nil
	}
	return this.top.value
}
// Pop the top item of the stack and return it
func (this *Stack) Pop() interface{} {
	if this.length == 0 {
		return nil
	}

	n := this.top
	this.top = n.prev
	this.length--
	return n.value
}
// Push a value onto the top of the stack
func (this *Stack) Push(value interface{}) {
	n := &node{value,this.top}
	this.top = n
	this.length++
}
func isValid(s string) bool {

	var stack = Stack{}
	var strMap = map[string]string{
		"]": "[",
		")": "(",
		"}": "{",
	}
	for _, value := range s {

		i := string(value)
		if stack.Len() > 0 {
			var strings string
			peek := stack.Peek().(string)
			strings = strMap[i]
			if strings == peek {
				stack.Pop()
			} else {
				stack.Push(i)
			}
		} else {
			stack.Push(i)
		}
	}

	return stack.Len()==0
}
func main() {
	log.Println(isValid("{[]}"))
	//log.Println(isValid("{}"))
	//log.Println(isValid("[]{}"))
	//log.Println(isValid("[{}]"))
	//var stack =Stack{}
	//stack.Push("1")
	//log.Println(stack.Peek())
	//stack.Push("2")
	//log.Println(stack.Peek())
	//stack.Push("3")
	//stack.Push("4")
	//log.Println(stack.Peek())
}