function betterSurround(str)
{
    if((str.charAt(0) != '=' && str.charAt(0) != '+') || (str.charAt(str.length-1) != '=' && str.charAt(str.length-1) != '+'))
        return false
    else
    {
        for(var i =1;i<str.length-1;i++)
        {
            if(str.charAt(i)>='a' && str.charAt(i)<='z')
            {
                if(!(((str.charAt(i-1) == '+' || str.charAt(i-1) == '=') && (str.charAt(i+1) == '+' || str.charAt(i+1) == '='))))
                    return false
            }    
            else if(str.charAt(i-1)>='a' && str.charAt(i-1)<='z' && str.charAt(i+1)>='a' && str.charAt(i+1)<='z')
                return false

        }
    }
    return true
}

var newwrd = betterSurround("+f+=d+")

if(newwrd)
    console.log("y")
else
    console.log("n")
