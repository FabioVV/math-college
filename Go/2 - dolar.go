package main

import "fmt"

func dolar() (float64, float64) {
	var dolar float64 = 4.9771
	var how_much_i_have float64

	fmt.Print("How much reais do you have? ")
	fmt.Scanln(&how_much_i_have)

	return how_much_i_have / dolar, how_much_i_have
}
