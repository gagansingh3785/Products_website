    let some_element = document.getElementsByClassName("some").length;
    some_element = some_element/4;
    let some_other_element;
    let previous = [];
    for(let i = 0 ; i < some_element; i++)
    {
        previous.push(document.getElementsByClassName("indicator"+ (i+1) +"")[0]);
        console.log(i);
        some_other_element = document.getElementsByClassName("indicator"+ (i+1) +"")[0];
        some_other_element.classList.add('my_active');
        console.log(some_other_element.classList);
    }
    function move1(counter)
    {
        previous[counter-1].classList.remove('my_active');
        previous[counter-1]= document.getElementsByClassName('indicator' + (counter) + "")[0];
        previous[counter-1].classList.add('my_active');
        console.log(counter);
        let ele = document.getElementsByClassName("images"+ counter +"");
        for(let i = 0; i< 4; i++)
            {
                ele[i].style.transition = '0.5s';
                ele[i].style.transform = 'translateX(0px)';
            }

    }
     function move2(counter)
    {
        previous[counter-1].classList.remove('my_active');
        previous[counter-1] = document.getElementsByClassName('indicator' + (counter) + "")[1];
        previous[counter-1].classList.add('my_active');
        console.log(counter);
        let ele = document.getElementsByClassName("images"+ counter +"");
        for(let i = 0; i< 4; i++)
            {
                ele[i].style.transition = '0.5s';
                ele[i].style.transform = 'translateX(-300px)';
            }

    }
     function move3(counter)
    {
        previous[counter-1].classList.remove('my_active');
        previous[counter-1] = document.getElementsByClassName('indicator' + (counter) + "")[2];
        previous[counter-1].classList.add('my_active');
        console.log(counter);
        let ele = document.getElementsByClassName("images"+ counter +"");
        for(let i = 0; i< 4; i++)
            {
                ele[i].style.transition = '0.5s';
                ele[i].style.transform = 'translateX(-600px)';
            }

    }
     function move4(counter)
    {
        previous[counter-1].classList.remove('my_active');
        previous[counter-1] = document.getElementsByClassName('indicator' + (counter) + "")[3];
        previous[counter-1].classList.add('my_active');
        console.log(counter);
        let ele = document.getElementsByClassName("images"+ counter +"");
        for(let i = 0; i< 4; i++)
            {
                ele[i].style.transition = '0.5s';
                ele[i].style.transform = 'translateX(-900px)';
            }

    }