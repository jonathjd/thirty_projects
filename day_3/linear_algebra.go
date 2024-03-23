package main

import "fmt"

func main() {
	fmt.Println("Let's do some math!")

	var x int16 = 5
	var y int16 = 10

	fmt.Println("Value of x:", x)
	fmt.Println("Value of y:", y)

	// addition
	var addition int16 = (x + y)
	fmt.Println("x + y =", addition)

	// subtraction
	var subtraction int16 = (x - y)
	fmt.Println("x - y =", subtraction)

	// division
	var division float32 = (float32(x) / float32(y))
	fmt.Println("x / y =", division)

	// multiplication
	var multiplication int16 = (x * y)
	fmt.Println("x * y =", multiplication)

	//////////// vectors - 1D //////////////////
	fmt.Println("----------Let's move on to vectors!-----------")

	var xArray = [5]float32{1.0, 2.0, 3.0, 4.0, 5.0}
	var yArray = [5]float32{6.0, 7.0, 8.0, 9.0, 10.0}

	fmt.Printf("Array x = %v and array y = %v\n", xArray, yArray)

	// addition
	var arrayAddition [5]float32
	for i := 0; i < len(xArray); i++ {
		arrayAddition[i] = xArray[i] + yArray[i]
	}
	fmt.Println("x + y =", arrayAddition)

	// subtraction
	var arraySubtraction [5]float32
	for i := 0; i < len(xArray); i++ {
		arraySubtraction[i] = xArray[i] - yArray[i]
	}
	fmt.Println("x - y =", arraySubtraction)

	// dot product
	var dotProduct float32
	for i := 0; i < len(xArray); i++ {
		dotProduct += xArray[i] / yArray[i]
	}
	fmt.Println("x * y =", dotProduct)

	// Hadamard Product
	var arrayMultiplication [5]float32
	for i := 0; i < len(xArray); i++ {
		arrayMultiplication[i] = xArray[i] * yArray[i]
	}
	fmt.Println("x x y =", arrayMultiplication)

	//////////// Matrices ///////////////////////
	fmt.Println("----------Finally, let's transform some matrices!-----------")

	type Matrix [2][2]float32

	var aMatrix = Matrix{{1, 2}, {3, 4}}
	var bMatrix = Matrix{{5, 6}, {7, 8}}

	fmt.Printf("Matrix A = %v and Matrix B = %v\n", aMatrix, bMatrix)

	// addition
	var matrixAddition Matrix
	for i := 0; i < len(aMatrix); i++ {
		for j := 0; j < len(aMatrix); j++ {
			matrixAddition[i][j] = aMatrix[i][j] + bMatrix[i][j]
		}
	}
	fmt.Println("A + B =", matrixAddition)

	// subtraction
	var matrixSubtraction Matrix
	for i := 0; i < len(aMatrix); i++ {
		for j := 0; j < len(aMatrix); j++ {
			matrixSubtraction[i][j] = aMatrix[i][j] - bMatrix[i][j]
		}
	}
	fmt.Println("A - B =", matrixSubtraction)

	// division
	var matrixDivision Matrix
	for i := 0; i < len(aMatrix); i++ {
		for j := 0; j < len(aMatrix); j++ {
			for k := 0; k < len(aMatrix); k++ {
				matrixDivision[i][j] += aMatrix[i][k] / bMatrix[k][j]
			}
		}
	}
	fmt.Println("A / B =", matrixDivision)

	// multiplication
	var matrixMultiplication Matrix
	for i := 0; i < len(aMatrix); i++ {
		for j := 0; j < len(aMatrix); j++ {
			for k := 0; k < len(aMatrix); k++ {
				matrixMultiplication[i][j] += aMatrix[i][k] * bMatrix[k][j]
			}
		}
	}
	fmt.Println("A * B =", matrixMultiplication)

}
