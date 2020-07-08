 console.log("fasdfasd");
    var flag = 1;
    var ele = document.getElementsByClassName('other1');

    function fun2()
    {
        console.log("inside the function");
        if(flag % 2 != 0)
        {
            console.log(flag);

            for(var i = 0; i < 2; i++)
            {
                ele[i].style.transform = 'translateY(' + 60*(i + 1) +'px)';
            }

        }
        if(flag % 2 == 0)
        {
            console.log(flag);

            for(var i = 0; i<2; i++)
            {
                ele[i].style.transform = 'translateY(0px)';
            }

        }
        flag++;
    }