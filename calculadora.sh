#!/usr/bin/env bash

echo "Ola! Bem bindo à calculadora EasyPeasy!:)"
read -p "Qual o seu nome?" nome

while true; do
	echo "$nome, escolha a operação matemática desejada:"
	echo "A - Adição, S - Subtração, M - Multiplicação, D - Divisão"
	echo "Ou digite E para sair"
	read -p "Digite a opção:" operacao

	if [[ "&operacao" =~ ^(E|e)$ ]];  then
		echo "Encerrando...tchau, $nome !"
		break
	fi

	# solicitação dos numeros
	read -p "Digite o primeiro número: " num1
	read -p "Digite o segundo número: " num2

	case "$operacao" in
		"A"|"a")
			resultado=$(echo "$num1 + $num2" | bc -l)
			simbolo="+"
			;;
		"S"|"s")
			resuldado=$(echo "$num1 - $num2" | bc -l) 
			simbolo="-"
			;;
		"M"|"m")
			resultado=$(echo "$num1 * $num2" | bc -l)
			simbolo="*"
			;;
		"D"|"d")
			# evita divisão por zero
			if [ "$(echo "$num2 == 0" | bc)" = "1" ]; then
				echo "Erro: divisão por zero não permitida!"
				continue
			fi
			resultado=$(echo "scale=2; $num1 / $num2" | bc -l)
			simbolo="/"
			;;
		*)
			echo "opção invalida!"
			continue
			;;
	esac

	echo "O resultado da operação $num1 $simbolo $num2 é: $resultado"

	read -p "Deseja fazer outra operação? (s/n):" continuar
	if [ "$continuar" != "s" ]; then
		echo "Encerrando a calculadora. Até mais, $nome!"
		break
	fi
done
