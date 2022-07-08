(()=>{

    const openCollapsibe = document.querySelector('.collapsible-item')
    openPlus = document.querySelector('.collapsible-item')
    
    openCollapsibe.addEventListener('click', toggleNav)
    
    
        function toggleNav(){
            openPlus.classList.toggle('active')     
        }
    
      

    })()