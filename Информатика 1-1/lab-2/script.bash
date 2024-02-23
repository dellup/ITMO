#!/bin/bash
a=$1 
my_array=($(echo $a | tr "." "\n"))


function perevod ()
{
	num=$1
	a=
	while [ $num -gt 0 ]
	do
		b=$(( $num % 2 ))
		a="$b$a"
		num=$(( $num / 2 ))
	done
	echo $a
	
}

str=
for i in ${my_array[@]}
do
	bin=$(printf "%08d" $(perevod $i))
	str="$str$bin."
	
	result=$(perevod $i)
done
echo "${str%.}"
