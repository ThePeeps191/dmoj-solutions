package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d\n", &n)
	for i := 0; i < n; i++ {
		var a int
		var b int
		fmt.Scanf("%d %d\n", &a, &b)
		fmt.Println(a + b)
	}
}
