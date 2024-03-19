package main

import (
	"fmt"
)

func main() {
	// f floats d integers (templates)

	fmt.Println("Hello, World!")
	fmt.Printf("Your average: %f", average())

	fmt.Println()
	i, j := dolar()
	fmt.Printf("You can buy %f dolars with %f reais", i, j)
}
