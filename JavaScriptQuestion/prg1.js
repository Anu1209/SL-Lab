function convertString(word)
{
    var nwrd = ""
    for(var i=0;i<word.length;i++)
    {
        if(word.charAt(i)>='a' && word.charAt(i)<='z')
        {
            if(word.charAt(i)!='z')
                nwrd = nwrd + String.fromCharCode(word.charCodeAt(i) + 1)
            else 
                nwrd = nwrd + 'a'
        }
        else
            nwrd = nwrd + word.charAt(i)
    }

    for(var i=0;i<nwrd.length;i++)
        if(nwrd.charAt(i)=='a' || nwrd.charAt(i) == 'e' || nwrd.charAt(i)=='i' || nwrd.charAt(i)=='o' || nwrd.charAt(i) =='u')
        {
            nwrd = nwrd.slice(0,i) + (nwrd.slice(i,i+1)).toUpperCase() + nwrd.slice(i+1) 
        }
    console.log(nwrd)
}

convertString("zelloo*3")
