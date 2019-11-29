function AgeCover(num)
{
    num = num.split("-")
    var age = 2019 - Number(num[2])
    if(Number(num[1]>10))
        age = age - 1
    console.log(age)
}

AgeCover("16-12-1998")
