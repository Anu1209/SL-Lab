function HourMinute(num)
{
    var mn = num%60
    var hr = Math.floor(num/60)
    console.log(hr,":",mn)
}

HourMinute(54)
