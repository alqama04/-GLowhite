(()=>{
    const openCollapsibe = document.querySelector('.collapsible-item')
    openPlus = document.querySelector('.collapsible-item')
    
    openCollapsibe.addEventListener('click', togglePlus)
       
        function togglePlus(){
            openPlus.classList.toggle('active')     
        }
    })()
    
    