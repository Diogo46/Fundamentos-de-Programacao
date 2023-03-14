# coding: utf-8

# This function computes the body mass index (BMI),
# given the height (in meter) and weight (in kg) of a person.
def bodyMassIndex(height, weight):
    # Complete the function definition...
	bmi = weight/(height**2)
	return bmi


# This function returns the BMI category acording to this table:
# BMI:        <18.5         [18.5, 25[      [25, 30[      30 or greater 
# Category:   Underweight   Normal weight   Overweight    Obesity 
def bmiCategory(bmi):
    # Complete the function definition...
	if bmi < 18.5:
		cat = 'Underweight'
	elif 18.5 <= bmi < 25:
		cat = 'Normal weight'
	elif 25 <= bmi < 30:
		cat = 'Overweight'
	else:
		cat = 'Obesity'
	return cat 


# This is the main function
def main():
	print("Índice de Massa Corporal")
    
	altura = float(input("Altura (m)? "))
	if altura < 0:
		print("ERRO: altura inválida!")
		exit(1)

	peso = float(input("Peso (kg)? "))
	if peso < 0:
		print("ERRO: peso inválido!")
		exit(1)

    # Complete the function calls...
	imc = bodyMassIndex(altura, peso)
	cat = bmiCategory(imc)

	print("BMI: {:.3f} kg/m2".format(imc))
	print("BMI category:", cat)


# Program starts executing here
main()

