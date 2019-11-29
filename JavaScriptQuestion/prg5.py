function OddRange(num1,num2)
{
    odd = []

    for(var i=Number(num1)+1;i<num2;i++)
        if(i%2!=0)
            odd.push(i)
    return odd
}

var num1 = prompt("Enter the value for the first number")
var num2 = prompt("Enter the value for the second number")

console.log(OddRange(num1,num2))
