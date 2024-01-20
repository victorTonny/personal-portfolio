// local storage
let themeColors = document.getElementsByClassName('theme-dot');

let theme = localStorage.getItem('theme');

// condition for theme 
if(theme == null){
    setTheme('light');
}
else{
    setTheme(theme);
}

for(let themeColor of themeColors){
    themeColor.addEventListener('click', function(){
        let mode = this.dataset.mode;
        console.log('Option clicked:', mode)
        setTheme(mode);
    });
}

// select the theme based on condition 
function setTheme(mode){
    if(mode == 'light'){
        document.getElementById('theme-style').href = 'default.css';
    }
    else if(mode == 'blue'){
        document.getElementById('theme-style').href = 'blue.css';
    }
    else if(mode == 'green'){
        document.getElementById('theme-style').href = 'green.css';
    }
    else if(mode == 'purple'){
        document.getElementById('theme-style').href = 'purple.css';
    }
    localStorage.setItem('theme', mode);
}

