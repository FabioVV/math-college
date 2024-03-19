package main

import "fmt"

func average() float64 {

	var how_many int
	var sum float64

	fmt.Print("How many numbers do you want to type in? ")
	fmt.Scanln(&how_many)

	for i := 0; i < how_many; i++ {
		temp := 0.0

		fmt.Printf("Number #%d ", i+1)
		fmt.Scanln(&temp)
		sum += temp
	}

	return sum / float64(how_many)
}
